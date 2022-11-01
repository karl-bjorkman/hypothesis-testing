# Hypothesis Testing Practice

1. Ask a Question
2. Define the Null and Alternative Hypotheses
3. Determine the Null Distribution
> The distribution (across repeated samples) of the statistic we are interested in
> if the null hypothesis is true
> In practice: calculate and store the average for each sample (which should be big enough)
> ... then plot a histogram of those averages (it should be normally distributed)
4. Calculate a P-Value (or Confidence Interval)
5. Interpret the Results

> The alternative hypothesis and significance threshold
> should be chosen prior to data collection.

## One-Sample T-Tests:

### Used to compare a *sample average* to a *hypothetical population average*.
### They might be used to address questions such as:
- Is the average amount of time that visitors spend on a website *different* from 5 minutes?
- Is the average amount of money that customers spend on a purchase *more than* $10?

### Assumptions:
1. Sample was randomly selected from the population
2. The individual observations were independent
3. The data is normally distributed without outliers *or* the sample size is large enough

## Binomial Tests:

### Used to compare the *frequency of some outcome in a sample* to the *expected probability* of that outcome.
### They might be used to address questions such as:
- If we expect 90% of ticketed passengers to show up for their flight but only 80 of 100 ticketed passengers actually show up, we could use a binomial test to determine whether 80 is significantly different from 90.

### They are different from One-Sample T-Tests in that...
- They are used for binary categorical data to compare a sample frequency to an expected population-level probability
- One-Sample T-Tests are used for quantitative data to compare a sample mean to an expected population mean