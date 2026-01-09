\ifndef{logisticRegressionDeployed}
\define{logisticRegressionDeployed}


\editme

\subsection{Ad Matching for Facebook}

\slides{
* This approach used in many internet companies.
* Example: ad matching for Facebook.
  * Millions of advertisers
  * Billions of users
  * How do you choose who to show what?
* Logistic regression used in combination with [decision trees]()
* [Paper available here](http://www.herbrich.me/papers/adclicksfacebook.pdf)
}

\notes{Logistic regression is a widely used technique in many real world application domains. Within social media, the first wave of machine learning solutions were targeted at challenges such as ad matching or news-post ranking. In these domains the users are characterised by their previous behaviour (such as which posts they have liked) and other contextual information (such as which friends they have). The logistic regression approach is then used to predict which ads should be shown. For example Facebook's ad matching system faces the complex challenge of connecting millions of advertisers with billions of users. The scale of this matching problem is immense:

- Facebook has millions of potential advertisers, each with different target audiences and budgets
- There are billions of users, each with unique interests and behaviors
- Decisions about which ads to show must be made in real-time
- The system needs to balance between user experience and advertiser ROI

Facebook's solution employed a system that combines logistic regression with decision trees. The system considers various features including:

- User demographics and behaviour
- Historical ad performance
- Advertiser parameters and budgets
- Contextual information

The hybrid approach allows Facebook to make rapid predictions about ad performance while handling the massive scale of their platform. The details of this system are described in a [technical paper by Herbrich et al.](http://www.herbrich.me/papers/adclicksfacebook.pdf), which describes Facebook's click prediction system for online advertising, which combines decision trees with logistic regression to predict ad clicks. At the time Facebook had over 750 million daily active users and 1 million advertisers at the time. The authors found that a hybrid model outperformed either decision trees or logistic regression alone.}

\notes{Importantly, from our perspective, the researchers found that *feature selection* was the most critical factor - particularly choosing the features that capture historical information about users and ads. Given the 'right' features and model architecture, adapting the system to accommodate other aspects such as data freshness and learning rate tuning provided smaller incremental gains. To handle the scale of the task the system used a cascade of classifies to handle thecandidate ads per request efficiently. The hybrid model served as the final stage classifier. The paper also discusses practical considerations around implementing online learning and managing computational resources at scale.}

\endif
