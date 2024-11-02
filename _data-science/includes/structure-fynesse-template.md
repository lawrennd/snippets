\ifndef{structureFynesseTemplate}
\define{structureFynesseTemplate}

\editme

\subsection{Structuring Your Code using the Fynesse Template}

\figure{\includepng{\diagramsDir/data-science/fynesse-template}{60%}}{The Fynesse Template gives you a starting point for building your data science library. You can fork the template, and then create a new repository from the template. You can use that repository for your analysis.}{fynesse-template}

\notes{Along this notebook, you have created different pieces of code to manage your data. You first executed some commands to download and explore your data. Then, you used pieces of code to plot and assess the datasets. In the end, you explored some statistical concepts to analyse your data.

The problems a data scientist faces and the strategies for their resolution are usually quite similar between domains and datasets. For example, you might want to download different datasets but the API request follows always the same logic. It makes sense then to structure your code in a way it can be reused and you save time. That is one of the technical goals we want you to achieve in this course. To facilitate this, you should use the Fynesse template for structuring your code.

The Fynesse template provides a Python template repo for doing data analysis according to the Fynesse framework (Access, Assess, and Address). You will use this template to create your own data analysis library. If you define such a library in a general enough way, you should be able to use the code you write in this course in your future data science projects.

We expect you to keep this library updated and use it during the course practicals and final assessment. In fact, for the final assignment, you will provide a short repository overview describing how you have implemented the different parts of the project and where you have placed those parts in your library. We will use your library to understand and reconstruct the thinking behind your analysis.}

\notes{Please follow this instructions to create your Python library based on the Fynesse Template:

You should start by forking the Fynesse Template repository.

A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.

You can fork the repository using your web explorer and your GitHub account. In [the Fynesse template](https://github.com/lawrennd/fynesse_template) GitHub repository click on the `Fork` box, and then click on `+ Create a new fork`. You will see another page to set the details of your library. Name your repository using your CRSid with the following format: `[CRSid]_ads_2024`.

Ensure you copy the main branch only. You can change the description as you wish and then click on `Create fork`.

After creating the fork, you should have the template in your own GitHub as a repository with the name you set when creating the fork. Clone this repo in your machine and open it using the IDE of your preference so you can start making changes to your library following the Fynesse template.

Let's create a `Hello World!` method in the `access` layer.

```
def hello_world():
  print("Hello from the data science library!")
```

Copy the code above to the `access.py` file in your library. The file is in the path `./fynesse/access.py`.

Commit and push your changes. Now, you are ready to import and use your library from this notebook.}

\code{%pip uninstall --yes fynesse
# Replace this with the location of your fynesse implementation
%pip install git+https://github.com/githubusername/fynesse_template.git
}

\setupcode{import fynesse}

\code{fynesse.access.hello_world()}

\endif
