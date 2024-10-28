# snippets

This is a repository that contains reusable snippets of lectures and notes that can be combined together to give talks. The system provides a flexible way to create presentations and teaching materials while maintaining consistency and reducing duplication.

It was originally started in latex to avoid creating large power point decks that were variants of the same talk, but it has been moved to a format based around markdown, pandoc and reveal.


## Overview

The snippets system is built around markdown files that use custom macros for handling different output formats (slides, notes, LaTeX, HTML, etc). Each snippet is a self-contained piece of content that can be included in multiple presentations. 


## Compilation

The snippets are compiled using the [lamd](https://github.com/lawrennd/lamd) tool, which processes the markdown and macros to generate the desired output format.

## Related Projects

For related projects see:

[lamd](https://github.com/lawrennd/lamd) - Contains the scripts for compiling these snippets.

[talks](https://github.com/lawrennd/talks) - The original repository where the snippets were hosted and contains talks composed from these snippets.

## Key Features

- Write once, use many times
- Support for multiple output formats including slides, notes, LaTeX, HTML and Jupyter notebooks
- Conditional content rendering based on output format
- Section management with \section, \subsection macros
- Figure handling with captions and references
- Code block management for different languages
- Support for speaker notes and slide incrementals
- YouTube, Vimeo and other media embedding

## Directory Structure

Snippets are organized into subject-specific directories:
```
_compsci/      - Computer Science content
_physics/      - Physics content
_ml/           - Machine Learning content
...
```

Each directory contains an `includes/` subdirectory for the actual snippet files.

## Key Macros

### Content Structure
```markdown
\section{title}          - Creates a new section
\subsection{title}      - Creates a new subsection
\notes{text}            - Content that appears in notes but not slides
\slides{text}           - Content that appears in slides but not notes
```

### Figures and Media
```markdown
\figure{contents}{caption}{label}  - Creates a figure with caption and reference
\includediagram{filename}{width}   - Includes an SVG/PNG diagram
\includeyoutube{id}{width}{height} - Embeds a YouTube video
```

### Code Blocks
```markdown
\code{content}             - Generic code block
\pythonblockstart         - Start a Python code block
\pythonblockend           - End a Python code block
\setupcode{content}       - Code that needs to run first
```

### Slide Controls
```markdown
\newslide{title}          - Starts a new slide
\speakernotes{text}       - Adds speaker notes to a slide
\fragment{text}{type}     - Creates reveal.js fragments
```

### Including Other Snippets
```markdown
\include{path/to/snippet.md}  - Includes another snippet file
```

## Example Snippet

Here's a detailed example of a snippet file with explanations of each component:

```markdown
\ifndef{gaussianProcess}
# This prevents multiple definition if the snippet is included more than once
\define{gaussianProcess}

\editme
# Adds an edit button linking to the source file on GitHub

\section{Gaussian Processes}
# Creates a section header that will be appropriately formatted in all output formats

\notes{
Gaussian processes provide a flexible framework for performing Bayesian inference over functions.
This text only appears in the notes version of the output.
}

\slides{
* Flexible framework
* Bayesian inference over functions
* Non-parametric model
This appears only in slides format as bullet points.
}

\figure{\includediagram{../diagrams/gp-sample}{80%}}{Sample functions drawn from a Gaussian process prior.}{gp-samples}
# Creates a figure from `gp-sample.svg` with width 80%, caption "Sample functions drawn from a GP prior" and label "gp-samples"

\speakernotes{Remember to emphasize the flexibility of the framework}
# Adds notes that appear in the speaker view of the presentation

\endif
# Closes the definition block
```


## Contributing

When creating new snippets:
1. Place them in the appropriate subject directory under `includes/`
2. Use the \ifndef/\define pattern to avoid duplicate definitions
3. Include the \editme macro at the start
4. Begin with a section or subsection marker where appropriate
5. Use \notes and \slides to differentiate content by format

