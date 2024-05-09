correlation_coef <- function(x, y, n) {
# Sort x and y by x
  sorted_indices <- order(x)
  x_sorted <- x[sorted_indices]
  y_sorted <- y[sorted_indices]
  # Remove records whose values of x are outside the 0.01-0.99 quantile range to avoid outliers
  a <- quantile(x, 0.01)
  b <- quantile(x, 0.99)
  # Spliting into intervals by x
  intervals <- seq(a, b, length.out = n + 1)
  # Calculate local variances
  local_variances <- numeric(n)
  for (i in 1:n) {
    x_interval <- x_sorted[x_sorted >= intervals[i] & x_sorted < intervals[i + 1]]
    y_interval <- y_sorted[x_sorted >= intervals[i] & x_sorted < intervals[i + 1]]
    local_variances[i] <- var(y_interval) * length(y_interval)
  }
# Calculate coefficient
  total_variance <- var(y)
  total_points <- length(y)
  dispersion_ratio <- sum(local_variances) / total_points / total_variance
  return(dispersion_ratio)
}
