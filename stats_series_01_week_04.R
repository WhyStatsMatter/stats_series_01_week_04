# Snippet 1
# Complementary Probability
p_a <- 0.4
p_not_a <- 1 - p_a

# Snippet 2
# Binomial Distribution
n <- 5  # Number of trials
p <- 0.5  # Probability of success
x <- 3  # Number of successes

binomial_prob <- dbinom(x, size = n, prob = p)

# Snippet 3
# Poisson Distribution
lambda_val <- 5  # Mean
k <- 3  # Number of occurrences

poisson_prob <- dpois(k, lambda = lambda_val)

# Snippet 4
# Z-Score
data <- c(2, 4, 4, 4, 5, 5, 7, 9)
z_scores <- scale(data)
