\ifndef{entropyNogoProbabilityPrescription}
\define{entropyNogoProbabilityPrescription}

\editme

\subsection{Entropy Forbids; Probability Prescribes}

\notes{I've spent most of my career in machine learning thinking about uncertainty, and very often that's been through probability. For so-called "Bayesian" researchers, one of the most important texts is Ed Jaynes's "Probability, the Logic of Science" [@Jaynes-probability03], which has become almost akin to a religious text. However, alongside probability, and also in Jaynes's work there's been a recurring theme of entropy and information arising.}

\notes{I started my PhD in 1996 at Aston University, but in 1998 moved to Cambridge, following my PhD supervisor who'd moved to Microsoft Research. I was excited because one of the most important researchers studying uncertainty in neural networks was based in Cambridge in the Cavendish lab. His name was David MacKay, and because there were no neural network researchers in the Computer Lab at the time I went to his group meetings. His group was called the inference group.}

\notes{MacKay's work had been inspired by Stephen Gull's work in the MaxEnt, and his PhD thesis had introduced an approach to dealing with uncertainty in neural networks known as the Laplace approximation. I was excited to learn more. So you can imagine I was surprised and confused to see that David had become more interested in *error correcting codes* and information theory. Or at least that's where his group's focus had shifted. And one of the main mathematical objects underpinning these codes was *entropy*.}

\notes{As a mechanical engineer, lacking the mathematical background of the physicists around me, I had to learn somewhat by osmosis. Chemical osmosis is driven by ionic gradients. Intellectual osmosis is driven by intriguing explanations.}

\notes{A mechanical engineer needs to learn thermodynamics. I answered exams using tables that contained the entropy of superheated steam. I studied thermodynamics in my undergraduate degree at Southampton from a textbook by Rogers and Mayhew in the 1990s. It was the same textbook my father had studied from when he studied mechanical engineering in Sheffield in the 1960s. }

\notes{So, I think this got me to thinking about a few things. What was the entropy of steam to do with the entropy of a communication code (if anything?). In the nearly three decades things those meetings I find I've been thinknga bout that for some time. And I notice that while my understanding of entropy has (I hope!) evolved, Rogers and Mayhew is still an assigned textbook for some thermodynamics courses <https://library.buid.ac.ae/meng234>.}

\notes{Probability and entropy are tightly interlinked. And I've been increasingly thinking if entropy should really be the principal object we think about when considering uncertainty, not probability.  I don't know if I'm write, but the idea of this course is to share some of those ideas.} 

\notes{Why do I think entropy should be the principal object? Well there's a funny thing about it that I can't quite put my finger on, an aspect of entropy that has teased me for a while. And I'd like to explore that aspect in this course with you.}

\notes{Here's the problem with probability. Every time I specify a probability distribution, I need to specify all that happens. I don't get to say that the distribution looks like a bell curve on the right, but I don't know what's going on on the left.  I need my probability to both cover the things I'm interested in in, and the things I might not be interested in. It feels like with probability I have to specify everything that's going to happen.[^probability-specify] Entropy however is different. With entropy, it feels like I get to talk about what's *not* going to happen. In information theory forms of entropy help us understand "no-go" areas, like the amount of information a channel is *not* going to carry per second ... or at least an upper bound on the information that the channel will carry. In physics, the second law of thermodynamics helps us understand that perpetual motion won't happen. It doesn't tell us the mechanism by which a system will lose energy and eventually slow and stop. It doesn't tell us when it will happen (unless we start looking at rates of energy to entropy conversion) it just tells us that it's going to happen.}


\notes{[^probability-specify]: THat's not strictly true because I can marginalise things I'm not interested in ... but gives me a challenge of integrating over those variables which can lead to mathematical (or computational) headaches.}

\notes{I find that intriguing.}

\notes{But just because I find something intriguing it doesn't make it true. So in some sense this will be a course about opinion. And it needs to be so. Because opinions about entropy vary. We'll try and capture that variety as we go. But to try and bring some narrative coherence to the course, we will explore the variety through a narrative based on my opinion.  That doesn't make my opinon right, it just makes it the easiest way to deliver the course.}

\notes{But why study entropy in Computer Science? Well, while we're on the subject of opinion, and bear in mind I'm really a mechanical engineer, so don't take my opinion too seriously. If there is any science in computer science, then it must be the science of how information evolves. The time it takes to process it and the transformations we can apply to it. But information theory is often absent from computer science courses. Why is that? Well because until now we have had to focus mainly on the techniques and tools we need to use to process data. On programming, on hardware implementation. On the mechanics of the information processing. Not the thermodynamics of the information processing. We have focussed on the mechanisms through which we transform information, not the fundamental rules by which it is transformed.}

\notes{Today things are shifting rapidly, my community has developed tools that allow the comptuer to communicate directly in natural language with humans and program for them. We have finally created computer systems that can be driven by anyone through natural language, just as my mechanical engineering predecessors created cars that could be driven by anyone without having to have an understanding of how a connecting rod is connected to a crank shaft.}

\notes{The field is changing rapidly. But students are being taught thermodynamics today from books that are the same as it was taught from 60 years ago.}

\notes{It's my instinct that those books provide important theory that tell us about the limits of computing machines. Today there are many making promises about superintelligent AGI machines that do all we can do more rapidly and more capably. A world where cognitive decision making knows no bounds. This course is built on the following premise. That premise is that there will be bounds and that those bounds will be dictated by information theory. Or more precisely, the information dynamics of the system.}

\notes{Just as thermodynamics tells us that there is no perpetual motion, I believe information dynamics will tell us that there are boundaries to the notion of superintelligence singularity. We won't achieve those boundaries in this course, but we will provide a journey through the landscape of entropy in a way that may persuade you that these are interesting tools to seek those boundaries with.[^practical]}

\notes{[^practical]: Fortunately, even if I'm totally wrong, the tools are widely deployed in a number of domains and your efforts in understanding them will bear fruit in one domain or another.}

When modelling in practice, we often account for this with cost functions. We There's a funny thing about entropy too. A friustrating thing about modellingSo why should we look at entropy?  One idea that will emerge across the course is the notion that probability tells us what a system will do. But entropy (somehow) tells us what a system won't do.  For example, we know that perpetual motion machines can't exist because, by the second law of thermodynamics, the cause entropy to be produced.  This tells us that if we see a wheel spinning, and we are not injecting energy into the wheel, eventually the wheel will stop spinning.  It doesn't tell us the dynamics by which the spinning will stop.  It doesn't tell us when it will stop.  It just tells us that it won't keep spinning for ever.  If we had the probability distribution that described the system, that would tell us when the wheel was likely to stop. So somehow probability tells us what's going to happen, where as entropy tells us whats not going to happen.  We'll explore this intuition as we go through the course, but its behind the idea why we might look to entropy to place limits on the performance of an intelligent system.}

\slidesincremental{
* Entropy: no-go theorems
* Probability: what we should do
* Same $H$, two jobs
}

\newslide{Two Jobs}

\notes{The second law does not tell you how to build an engine. It tells you that you cannot build one that does work for nothing. The Boltzmann distribution then tells you how a system at temperature $T$ occupies its energy levels. Shannon's capacity theorem does not give you a code. It tells you that you cannot send faster than $C$. The capacity-achieving input is the distribution you should use. Jaynes does not invent a new entropy. He uses entropy as a prohibition on extra structure, and probability as the least-committal recipe consistent with what you know.}

\slidesincremental{
* No-go: what is forbidden
* Prescription: the $p$ you should adopt
* We will draw this idea out every week
}

\endif
