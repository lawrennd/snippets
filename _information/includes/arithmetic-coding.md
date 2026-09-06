\ifndef{arithmeticCoding}
\define{arithmeticCoding}

\editme

\subsection{Arithmetic Coding}

\notes{In Chapter 6 of *Information Theory, Inference, and Learning Algorithms*
[@MacKay-information03], MacKay introduces arithmetic coding with a clear
philosophy: *compression of data from a source entails probabilistic
modelling of that source*.  The encoding operation is then almost an
afterthought — once you can predict, you can code.}

\slides{
* Compression entails probabilistic modelling [@MacKay-information03, Ch.~6]
* Predict next symbol → encode cheaply when the prediction is sharp
* Modelling separated from the bit-string construction
}

\subsubsection{The guessing game}

\notes{Section 6.1 motivates the idea with a guessing game.  An English
speaker tries to predict the next character of a text; after each correct
guess we record *how many* attempts it took.  The sequence of guess-counts
is highly skewed toward 1 and 2, so it compresses easily.  Decoding needs
an *identical twin* who makes the same sequence of guesses: stop them after
the recorded number of attempts and they land on the right letter.}

\slides{
* Human predicts next character (MacKay Sec.~6.1)
* Record guess-rank → skewed alphabet → easy to compress
* Decoder: identical twin, stopped after the same number of guesses
}

\notes{The game demonstrates two design principles we will keep: (i) a
*time-varying* predictive mapping is allowed — the predictor may use as much
context as it likes; (ii) encoder and decoder must share an identical
model.}

\subsubsection{From guesses to intervals}

\notes{Section 6.2 replaces the human by a program that, given the string so
far, returns a predictive distribution $\{p_i\}$ over the next symbol.
Arithmetic coding turns that distribution into nested intervals on
$[0,1)$ (Figures 6.1–6.2).  A binary transmission itself defines an
interval — the string ``01`` is the dyadic interval $[0.25, 0.50)$ — so
encoding means: find a bit-string whose interval sits *inside* the interval
that the model assigned to the message.}

\slides{
* Model supplies $P(x_n \mid x_{<n})$ — any context-dependent distribution
* Subdivide $[0,1)$ so each symbol interval has length equal to its probability
* Code = any bit-string whose dyadic interval ⊆ message interval
* Length of final interval $= P(\text{message}\mid\text{model})$
}

\notes{MacKay's Algorithm 6.3 is the iterative form.  Write $Q_n$ and $R_n$
for the lower and upper cumulative predictive probabilities.  Starting from
$u=0$, $v=1$, $p=v-u$, each symbol updates
$$
v \leftarrow u + p\,R_n(x_n\mid x_{<n}),\qquad
u \leftarrow u + p\,Q_n(x_n\mid x_{<n}),\qquad
p \leftarrow v-u.
$$
The Shannon information content of the string is
$h(x\mid H)=\log[1/P(x\mid H)]$; Exercise 6.1 shows the coded length stays
within two bits of that ideal.}

\setupcode{import json
import math
from collections import defaultdict}

\notes{First the predictive model.  Arithmetic coding does not prescribe
*how* predictions are made — only that encoder and decoder agree.  For
Dasher we use a unigram–bigram blend
$P(c \mid c') \propto w\,P_{\mathrm{bi}}(c \mid c') + (1-w)\,P_{\mathrm{uni}}(c)$.}

\helpercode{DEFAULT_CHARS = "abcdefghijklmnopqrstuvwxyz "
DEFAULT_BIGRAM_WEIGHT = 0.82

def normalise_text(text, chars=DEFAULT_CHARS, map_other_to_space=True):
    """Lower-case onto the alphabet; newlines/tabs → space."""
    alpha = set(chars)
    out = []
    for raw in text:
        ch = raw.lower()
        if ch in alpha:
            out.append(ch)
        elif map_other_to_space and ch in "\n\r\t ":
            if " " in alpha:
                out.append(" ")
    return "".join(out)

class CharModel:
    """Unigram + bigram blend (same predictive form as Dasher)."""

    def __init__(self, chars=DEFAULT_CHARS, bigram_weight=DEFAULT_BIGRAM_WEIGHT,
                 uni=None, bi=None):
        self.chars = chars
        self.bigram_weight = bigram_weight
        self.uni = uni or {}
        self.bi = bi or {}

    def predict(self, context):
        """P(c | last character of context) over self.chars."""
        last = context[-1].lower() if context else ""
        row = self.bi.get(last, {})
        w = self.bigram_weight
        out = {}
        for ch in self.chars:
            bp = row.get(ch, 0.0)
            up = self.uni.get(ch, 1e-4)
            out[ch] = w * bp + (1.0 - w) * up
        z = sum(out.values())
        if z <= 0:
            u = 1.0 / len(self.chars)
            return {ch: u for ch in self.chars}
        return {ch: p / z for ch, p in out.items()}

    def entropy_rate(self, context=""):
        """H(next | context) in bits."""
        probs = self.predict(context)
        return -sum(p * math.log2(p) for p in probs.values() if p > 0)

    def to_dasher_dict(self):
        """JSON object for Dasher.setLanguageModel / dasher-lm.json."""
        return {
            "chars": self.chars,
            "bigramWeight": self.bigram_weight,
            "uni": {ch: self.uni.get(ch, 0.0) for ch in self.chars},
            "bi": {prev: {ch: float(p) for ch, p in row.items()}
                   for prev, row in self.bi.items()},
        }

def train_from_text(text, chars=DEFAULT_CHARS,
                    bigram_weight=DEFAULT_BIGRAM_WEIGHT, add_k=0.0):
    """Count characters → CharModel (MacKay: the predictor is separate)."""
    data = normalise_text(text, chars)
    if not data:
        raise ValueError("training text contains no alphabet characters")
    uni_counts = {ch: add_k for ch in chars}
    bi_counts = defaultdict(lambda: {ch: add_k for ch in chars})
    prev = None
    for ch in data:
        uni_counts[ch] += 1.0
        if prev is not None:
            bi_counts[prev][ch] += 1.0
        prev = ch
    n = sum(uni_counts.values())
    uni = {ch: uni_counts[ch] / n for ch in chars}
    bi = {}
    for prev_ch, row in bi_counts.items():
        total = sum(row.values())
        if total <= 0:
            continue
        sparse = {ch: row[ch] / total for ch in chars if row[ch] > 0}
        if sparse:
            bi[prev_ch] = sparse
    return CharModel(chars=chars, bigram_weight=bigram_weight, uni=uni, bi=bi)

def write_dasher_lm(model, path):
    """Write dasher-lm.json for the visualiser."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(model.to_dasher_dict(), f, indent=2)
        f.write("\n")}

\newslide{Train a Predictive Model}

\code{corpus = """
Alice was beginning to get very tired of sitting by her sister on the bank,
and of having nothing to do: once or twice she had peeped into the book her
sister was reading, but it had no pictures or conversations in it.
"""
model = train_from_text(corpus, bigram_weight=0.82)
print(f"H(next | ∅)    = {model.entropy_rate(''):.3f} bits/char")
print(f"H(next | 't')  = {model.entropy_rate('t'):.3f} bits/char")
print(f"H(next | 'th') = {model.entropy_rate('th'):.3f} bits/char")}

\notes{After ``th`` the predictive mass concentrates on ``e``, so the
conditional entropy drops.  That drop *is* the tall ``e`` box in Dasher.}

\newslide{Algorithm 6.3 in Code}

\notes{The helpers below follow MacKay's Algorithm 6.3 and Figure 6.1:
narrow $[u,v)\subseteq[0,1)$, then pick a dyadic bit-string inside it.
The decoder is the identical twin — same predictions, ask which symbol
interval contains the number defined by the bits.}

\helpercode{def cumulative_QR(probs, chars):
    """MacKay's Q_n (lower) and R_n (upper) cumulatives."""
    Q, R = {}, {}
    cum = 0.0
    for ch in chars:
        Q[ch] = cum
        cum += probs.get(ch, 0.0)
        R[ch] = cum
    if chars:
        R[chars[-1]] = 1.0
    return Q, R

def encode_interval(message, model):
    """Algorithm 6.3 → (u, v, ideal_bits).  Width v−u = P(message|model)."""
    u, v = 0.0, 1.0
    p = v - u
    ideal = 0.0
    for i, ch in enumerate(message):
        probs = model.predict(message[:i])
        pc = probs[ch]
        if pc <= 0:
            raise ValueError(f"zero probability for {ch!r}")
        ideal -= math.log2(pc)
        Q, R = cumulative_QR(probs, model.chars)
        v = u + p * R[ch]
        u = u + p * Q[ch]
        p = v - u
    return u, v, ideal

def tag_bits(u, v):
    """Bit-string whose dyadic interval lies inside [u, v) (Fig. 6.1)."""
    target = 0.5 * (u + v)
    lo, hi = 0.0, 1.0
    bits = []
    for _ in range(64):
        if lo >= u and hi <= v:
            break
        mid = 0.5 * (lo + hi)
        if target < mid:
            bits.append("0")
            hi = mid
        else:
            bits.append("1")
            lo = mid
    return "".join(bits)

def encode(message, model):
    """Return (bitstring, ideal_bits)."""
    if not message:
        return "", 0.0
    u, v, ideal = encode_interval(message, model)
    return tag_bits(u, v), ideal

def decode(bitstring, length, model):
    """Identical-twin decoder: same model, recover `length` symbols."""
    value = 0.0
    scale = 0.5
    for b in bitstring:
        if b == "1":
            value += scale
        scale *= 0.5
    value += 0.5 * scale  # midpoint of the dyadic interval
    u, v = 0.0, 1.0
    out = []
    for _ in range(length):
        p = v - u
        probs = model.predict("".join(out))
        Q, R = cumulative_QR(probs, model.chars)
        chosen = None
        for ch in model.chars:
            lo = u + p * Q[ch]
            hi = u + p * R[ch]
            if lo <= value < hi or (ch == model.chars[-1] and lo <= value <= hi):
                chosen = ch
                u, v = lo, hi
                break
        if chosen is None:
            raise ValueError("value outside all symbol bins")
        out.append(chosen)
    return "".join(out)

def interval_trace(message, model):
    """Nested [u, v) after each symbol — Fig. 6.2 / Dasher zoom as data."""
    u, v = 0.0, 1.0
    p = v - u
    steps = []
    for i, ch in enumerate(message):
        probs = model.predict(message[:i])
        Q, R = cumulative_QR(probs, model.chars)
        v = u + p * R[ch]
        u = u + p * Q[ch]
        p = v - u
        steps.append({
            "char": ch, "p": probs[ch],
            "bits": -math.log2(probs[ch]),
            "u": u, "v": v, "width": p,
        })
    return steps}

\code{message = normalise_text("the rabbit")
u, v, ideal_bits = encode_interval(message, model)
bitstring, _ = encode(message, model)
recovered = decode(bitstring, len(message), model)
print(f"message:   {message!r}")
print(f"[u, v)  = [{u:.6f}, {v:.6f})  width={v-u:.3e}")
print(f"ideal:     {ideal_bits:.3f} bits  "
      f"({ideal_bits / len(message):.3f} bits/char)")
print(f"bitstring: {bitstring}  ({len(bitstring)} bits)")
print(f"decoded:   {recovered!r}  ok={recovered == message}")
for step in interval_trace(message, model)[:4]:
    print(f"  '{step['char']}': p={step['p']:.3f}  "
          f"bits={step['bits']:.2f}  "
          f"[u,v)=[{step['u']:.4f},{step['v']:.4f})")}

\code{uniform = len(message) * math.log2(len(model.chars))
print(f"uniform: {uniform:.3f} bits  "
      f"({uniform / len(message):.3f} bits/char)")
print(f"saving:  {uniform - ideal_bits:.3f} bits vs uniform")}

\notes{Compare with a uniform code over the same alphabet.  A model that
knows English beats uniform — and the gap is exactly what good prediction
buys you.}

\newslide{Export for Dasher}

\notes{Dasher [@MacKay-dasher98; @Ward-dasher00] *draws* Algorithm 6.3:
each letter is a vertical interval whose height is its predictive
probability, and zooming into a letter is the update
$(u,v)\leftarrow(u+pQ,\,u+pR)$.  Write the trained tables to JSON; point
the canvas at your file (or replace the default ``dasher-lm.json``) and the
box sizes become *your* $P(c\mid\mathrm{context})$.}

\code{write_dasher_lm(model, "dasher-lm.json")
print(sorted(model.to_dasher_dict().keys()))}

\slides{
* Retrain on another corpus → rewrite JSON → reload Dasher
* Box heights follow your $P(c \mid \mathrm{context})$
}

\notes{For a one-shot shell export from the talks tree (same logic as the
helpers above):
```
python arithmetic_coding.py path/to/corpus.txt \
    -o scripts/dasher/dasher-lm.json --demo
```}

\endif
