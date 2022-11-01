import numpy as np
from scipy.stats import binom_test
from scipy.stats import ttest_1samp
from scipy.stats import chi2_contingency

# ONE-SAMPLE T-TEST:
# Useful for: quantitative data (e.g. how long people spent doing an activity)

sample_observation_list = []
exp_value = 10

tstat, pval = ttest_1samp(
    a = sample_observation_list, # Sample distribution
    popmean = exp_value # Expected value (mean) in null hypothesis
)

# TWO-SIDED BINOMIAL TEST:
# Useful for: categorical data (e.g. whether or not someone does something - binary categorical variable)

# Sample of 100 subscribers, 15 people read an article.
# Null Hypothesis: 10% of subscribers who see an article will read it
# Alternative Hypothesis: More than 10% of subscribers who see an article will read it

# Given that 15 people read an article in the sample of 100, can we reject the null hypothesis?
# ... and therefore say we have evidence to accept the alternative hypothesis?

# Will the resulting p-value be 'significant' (less than significance threshold) or 'not significant'?

p_value_2sided = binom_test(
    x = 15,  # Observed sample statistic / observed successes
    n = 100,  # Sample size / total number of trials
    p = 0.1,  # Probability of event, assuming null hypothesis is true / expected probability of success
    alternative = 'two-sided'  # Alternative hypothesis stating different than 10%
)

p_value_1sided = binom_test(
    x = 15,
    n = 100,
    p = 0.1,
    alternative = 'greater' # Alternative hypothesis: greater than 10%
)

p_value_1sided = binom_test(
    x = 15,
    n = 100,
    p = 0.1,
    alternative = 'less' # Alternative hypothesis: less than 10%
)