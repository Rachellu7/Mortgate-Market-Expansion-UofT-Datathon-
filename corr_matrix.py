# %%
########## SOURCE CODE FOR HOMEWORK 1 lin 5-113 #######
import matplotlib
import numpy as np
from numpy.core.fromnumeric import shape
from numpy.lib.arraysetops import unique #linear algrebra
import pandas as pd #data processing
import os
import matplotlib.pyplot as plt
from pandas.core.tools.numeric import to_numeric
import seaborn as sns
from pylab import rcParams
import matplotlib.cm as cm
import warnings
warnings.filterwarnings('ignore')
# %%
mortgage = pd.read_csv('/Users/xj/Desktop/datathon/mortgage.csv')
# %%
# looking for missing value
pd.isnull(mortgage).sum()
# %%
mortgage['good_loan'].value_counts()
# %%
mortgage.info()
# %%
# select key factors
mortgage_key = mortgage[['LAST_STAT','ORIG_CHN','SELLER','SERVICER','orig_rt','LAST_RT','orig_amt',
'ORIG_VAL','LAST_UPB','orig_trm','oltv','ocltv','num_bo','dti','CSCORE_B','CSCORE_C','FTHB_FLG','purpose',
'PROP_TYP','NUM_UNIT','occ_stat','msa','mi_pct','NET_LOSS','relo_flg','good_loan']]
# %%
mortgage_key.info()
# %%
corrDF = mortgage_key[:-1].apply(lambda x: pd.factorize(x)[0])
corrDF.head()
# %%
corr = corrDF.corr()
corr
# %%
plt.figure(figsize=(20,16))
ax = sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns,
linewidths=0.2,cmap='YlGnBu',annot=True)
plt.title('Correlation between variables')