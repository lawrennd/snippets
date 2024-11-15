\ifndef{dataScienceAsDebugging}
\define{dataScienceAsDebugging}
\editme

\subsection{Data Science as Debugging}

\notes{One challenge for existing information technology professionals
is realizing the extent to which a software ecosystem based on data
differs from a classical ecosystem. In particular, by ingesting data
we bring unknowns/uncontrollables into our decision-making
system. This presents opportunity for adversarial exploitation and
unforeseen operation.}

\slides{
* Analogies: For Software Engineers [describe data science as *debugging*](http://inverseprobability.com/2017/03/14/data-science-as-debugging).
}

\addblog{Data Science as Debugging}{2017/03/14/data-science-as-debugging}

\notes{Starting with the analysis of a data set, the nature of data
science is somewhat difference from classical software engineering.}

\notes{One analogy I find helpful for understanding the depth of
change we need is the following. Imagine as a software engineer, you
find a USB stick on the ground. And for some reason you *know* that on
that USB stick is a particular API call that will enable you to make a
significant positive difference on a business problem. You don't know
which of the many library functions on the USB stick are the ones that
will help. And it could be that some of those library functions will
hinder, perhaps because they are just inappropriate or perhaps because
they have been placed there maliciously. The most secure thing to do
would be to *not* introduce this code into your production system at all. But
what if your manager told you to do so, how would you go about
incorporating this code base?}

\notes{The answer is *very* carefully. You would have to engage in a process
more akin to debugging than regular software engineering. As you
understood the code base, for your work to be reproducible, you should
be documenting it, not just what you discovered, but how you discovered
it. In the end, you typically find a single API call that is the one
that most benefits your system. But more thought has been placed into
this line of code than any line of code you have written before.}

\notes{An enormous amount of debugging would be required. As the
nature of the code base is understood, software tests to verify it
also need to be constructed. At the end of all your work, the lines of
software you write to interact with the software on the USB
stick are likely to be minimal. But more thought would be put into
those lines than perhaps any other lines of code in the system.}

\notes{Even then, when your API code is introduced into your production system,
it needs to be deployed in an environment that monitors it. We cannot
rely on an individual’s decision making to ensure the quality of all our
systems. We need to create an environment that includes quality
controls, checks, and bounds, tests, all designed to ensure that
assumptions made about this foreign code base are remaining valid.}

\notes{This situation is akin to what we are doing when we incorporate data in
our production systems. When we are consuming data from others, we
cannot assume that it has been produced in alignment with our goals for
our own systems. Worst case, it may have been adversarially produced. A
further challenge is that data is dynamic. So, in effect, the code on
the USB stick is evolving over time.}

\notes{It might see that this process is easy to formalize now, we
simply need to check what the formal software engineering process is
for debugging, because that is the current software engineering
activity that data science is closest to. But when we look for a
formalization of debugging, we find that there is none. Indeed, modern
software engineering mainly focusses on ensuring that code is written
without bugs in the first place.}

\newslide{80/20 in Data Science}
\slides{
* Anecdotally for a given challenge 
    * 80% of time is spent on data wrangling.
	* 20% of time spent on modelling.
* Many companies employ ML Engineers focussing on *models* not *data*.
}

\subsubsection{Lessons}

\slides{1. When you begin an analysis behave as a debugger
* Write test code as you go. 
  * document tests ... make them accessible.
* Be constantly skeptical.
* Develop deep understanding of best tools.
* Share your experience of challenges, have others review work}

\newslide{Lessons}

\slides{2. When managing a data science process.
  * Don't deploy standard agile development. Explore modifications e.g. Kanban
  * Don't leave data scientist alone to wade through mess.
  * Integrate the data analysis with other team activities
    * Have software engineers and domain experts work closely with data scientists}

\notes{When you begin a data analysis approach it with the mindset of a debugger: write test code continuously as you go through your analysis, ensure that the tests are documented and accessible to those who need to review or build upon your work.

Take time to thouroughly understand the context of your data before diving in. Expore multiple approaches and continually revisit your initial assumptions. Maintain a healtky skepticism about your results through the process and proactively explore potential issues or inconsistencies in the data.

Leverage the best tools available and develop a deep understanding of how they work. Don't just treat the tools as black boxes, develop your understanding of tehri strengths, limmitations and appropriate use. Share challenges you are facing and progress you are making with colleagues. Seek regular views from business stakholders, software engineers, fellow data scientists and managers. Bringing in their different perspectives can help identify potential issues early.

Don't rush to implementing your end-solution. Just as you wouldn't immediately write an API call for unknown code you've found on a discarded USB code, you shouldn't jump straght into running complex classsification algorithms before gaining an intuition for your data through some basic visualisation and ohter tests. The documentation of the analysis process should be such that if issues do arise in production the documentation can be used to support tracing back to where the problems have originated and rapidly rectifying them. 

Always remember that the data science process differs fundamentally from standard software development, so traditional agile development pipelines may not be appropriate. You have to adapt your processes to handle inherrent uncertainty and accomidate the iterative and recursive nature of data science work. Think carefully about how you will handle not just individual bugs but systematic issues that may emerge from your data.

Don't work in isolation, the complexity of data work means that close collaboration with domain experts, software engineers and other data scientists is essention. The collaboration serves multiple purposes: it provides you with the necessary technical support, helps maintain realistic expectations among stakeholders in terms of both outcome and delivery time lines. And it ensures that the solutions developed actually address the underlying business problem. }

\recommendation{Anecdotally, resolving a machine learning challenge
requires 80% of the resource to be focused on the data and perhaps 20%
to be focused on the model. But many companies are too keen to employ
machine learning engineers who focus on the models, not the data. We
should change our hiring priorities and training. Universities cannot
provide the understanding of how to data-wrangle.  Companies must fill
this gap.}


\endif
