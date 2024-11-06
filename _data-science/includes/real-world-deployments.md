\ifndef{realWorldDeployments}
\define{realWorldDeployments}

\editme

\section{Real World Deployments}

\newslide{Current Approach}

\slides{
* Focus on technology and model performance
* Example learning model pipeline:
```
Learning Model <inputs> → <prediction>
```
}

\newslide{Performance Focus}

\slides{
* Typical metrics focus:

| Model    | Accuracy | Latency | Resource Demand |
|----------|----------|---------|-----------------|
| Model v1 | 88%      | 3 secs  | Low            |
| Model v2 | 90%      | 4 secs  | Medium         |
| Model v3 | 98%      | 10 secs | High           |
}

\notes{This focus on pure model performance can lead us to overlook critical deployment considerations like latency requirements and resource constraints.}

\newslide{Context Matters}

\slides{
* Learning models are part of larger systems
* Systems must address end user requirements
* Multiple interacting components
* System outputs are aggregations of many processes
}

\endif
