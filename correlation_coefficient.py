def corr_coef(df: pd.DataFrame, y: str, x: str, n = 100):
    # Remove records whose values of x are outside the 0.01-0.99 quantile range to avoid outliers
    quantile_min = df[x].quantile(0.001)
    quantile_max = df[x].quantile(0.999)
    df_filtered = df[df[x].between(quantile_min, quantile_max)]
    
    # Calculate step size
    steps_count = int(len(df_filtered) / n) + 1
    step = (df_filtered[x].max() - df_filtered[x].min()) / steps_count
 
    # Calculate local variances
    y_vars = []
    for i in range(steps_count):
        x_min = quantile_min + step * i
        x_max = quantile_min + step * (i + 1)
        y_values = df_filtered[y][(df_filtered[x] >= x_min) & (df_filtered[x] < x_max)]
        y_count = len(y_values)
        y_vars.append(y_values.var() * y_count)
 
    # Calculation general variance and sum of local variances
    df_var = df_filtered[y].var()
    cov = sum(y_vars)
 
    # Return coef value
    return (1 - cov / (len(df_filtered) * df_var))
