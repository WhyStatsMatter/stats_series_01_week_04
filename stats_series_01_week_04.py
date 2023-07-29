# Snippet 1
# Complementary Probability
p_a = 0.4
p_not_a = 1 - p_a

# Snippet 2
# Binomial Distribution
from scipy.stats import binom

n = 5  # Number of trials
p = 0.5  # Probability of success
x = 3  # Number of successes

binomial_prob = binom.pmf(x, n, p)

# Snippet 3
# Poisson Distribution
from scipy.stats import poisson

lambda_val = 5  # Mean
k = 3  # Number of occurrences

poisson_prob = poisson.pmf(k, lambda_val)

# Snippet 4
# Z-Score
from scipy.stats import zscore

data = [2, 4, 4, 4, 5, 5, 7, 9]
z_scores = zscore(data)
