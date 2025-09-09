\ifndef{noFreeLunchTheorem}
\define{noFreeLunchTheorem}

\editme

\subsection{No Free Lunch Theorem}

\notes{Also related to generalisation error is the  'no free lunch theorem', which refers to our inability to decide what a better learning algorithm is without making assumptions about the data [@Wolpert-lack96] (see also @Wolpert-supervised02).}

\slides{* No universally best learner across all data-generating processes
* Performance gains arise from assumptions (inductive bias) matching the task
* Implication: model choice and regularisation must reflect prior beliefs about the problem}

\newslide{Statement (Informal)}
\slides{* Averaged over all possible labelings/functions, all algorithms have the same expected error
* Differences in performance come only from restricting the problem family (assumptions)}
\notes{NFL results show that without constraints on the data-generating distribution, no learning algorithm outperforms another in expectation. Any advantage derives from aligning the learner's inductive bias with the structure present in the data.}

\newslide{Position in this Lecture}
\slides{* After bias–variance and bootstrap: why we cannot expect one degree/basis to win universally
* Connects to cross-validation and model selection: choose bias consistent with data
* Motivates regularisation: encode assumptions to trade bias for variance appropriately}
\notes{We've seen how model complexity trades bias for variance and how resampling quantifies variability. The no free lunch theorem explains why there is no globally optimal choice: effective generalisation requires assumptions tailored to the task (basis choice, degree, smoothness, priors).}

\newslide{Practical Takeaways}
\slides{* Use validation to select assumptions that fit the domain
* Prefer simple models unless evidence supports added complexity
* Make assumptions explicit (document basis, priors, regularisers)}

\endif
