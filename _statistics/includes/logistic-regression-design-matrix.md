\ifndef{logisticRegressionEvaluation}
\define{logisticRegressionEvaluation}

\editme

\subsubsection{Design Matrix for Logistic Regression}

\slides{
* The design matrix $\designMatrix$ stores our features
* Each row represents one data point
* Each column represents one feature
* For $n$ data points and $p$ features:
  $$\designMatrix = \begin{bmatrix} 
  1 & x_{11} & x_{12} & \cdots & x_{1p} \\
  1 & x_{21} & x_{22} & \cdots & x_{2p} \\
  \vdots & \vdots & \vdots & \ddots & \vdots \\
  1 & x_{n1} & x_{n2} & \cdots & x_{np}
  \end{bmatrix}$$
* First column of 1s provides intercept term
}

\notes{The design matrix in logistic regression works similarly to linear regression but with some important differences. Each row represents an observation, and columns represent features. However, the interpretation of the model changes:

For logistic regression:
$$\text{logit}(p_i) = \log\left(\frac{p_i}{1-p_i}\right) = \designMatrix_i \mappingVector$$

where $\designMatrix_i$ is the $i$-th row of the design matrix and $p_i = p(\dataScalar_i = 1|\inputVector_i)$.

**Feature Engineering for Classification:**
We can enhance the design matrix with additional transformed features:

- **Polynomial Features**: $x_1^2$, $x_2^2$ for capturing non-linear relationships
- **Interaction Terms**: $x_1 \times x_2$ for capturing feature synergies  
- **Categorical Encodings**: One-hot encoding for categorical variables
- **Standardized Features**: Z-score normalization for better numerical stability

The choice of features in the design matrix directly affects the model's ability to capture complex decision boundaries while maintaining interpretability.}



\endif
