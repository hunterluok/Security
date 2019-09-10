"""
方差分析和卡方检验
"""



from scipy import stats
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols

####
chisquare=4.2
freedom_degree=7

#p_value=1.0-
stats.chi2.cdf(chisquare, freedom_degree)
# from scipy.stats import t
# interval=t.interval(alpha,df)

def print_anova(mydata, x, y):
    """
    为连续型变量，x为目标变量
    """
    anova_reA= anova_lm(ols('{}~C({})'.format(y, x), data=mydata[[y, x]]).fit())
    print("x is {}, y is {} ---".format(x, y))
    print(anova_reA)
    print('\t')



# 卡方检验

# stats.chi2_contingency(t2)