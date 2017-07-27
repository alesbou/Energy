# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:21:21 2017

@author: escriva
"""

import os
import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols


#Working inside subdirectory
abspath = os.path.abspath(__file__)
absname = os.path.dirname(abspath)
os.chdir(absname)

data = pd.read_csv('energy.csv')
datac = data[data["Retired_Unit"]==False]
datac["diversionInt2011"]=datac.Diversion2011*1000000/datac.GenerationMWh2011
datac["diversionInt2012"]=datac.Diversion2012*1000000/datac.GenerationMWh2012
datac["diversionInt2013"]=datac.Diversion2013*1000000/datac.GenerationMWh2013
datac["diversionInt2014"]=datac.Diversion2014*1000000/datac.GenerationMWh2014
datac["diversionInt2015"]=datac.Diversion2015*1000000/datac.GenerationMWh2015
datac["withdrawalInt2011"]=datac.Withdrawal2011*1000000/datac.GenerationMWh2011
datac["withdrawalInt2012"]=datac.Withdrawal2012*1000000/datac.GenerationMWh2012
datac["withdrawalInt2013"]=datac.Withdrawal2013*1000000/datac.GenerationMWh2013
datac["withdrawalInt2014"]=datac.Withdrawal2014*1000000/datac.GenerationMWh2014
datac["withdrawalInt2015"]=datac.Withdrawal2015*1000000/datac.GenerationMWh2015

datac["appliedInt2011"]=(datac.Diversion2011+datac.Withdrawal2011)*1000000/datac.GenerationMWh2011
datac["appliedInt2012"]=(datac.Diversion2012+datac.Withdrawal2012)*1000000/datac.GenerationMWh2012
datac["appliedInt2013"]=(datac.Diversion2013+datac.Withdrawal2013)*1000000/datac.GenerationMWh2013
datac["appliedInt2014"]=(datac.Diversion2014+datac.Withdrawal2014)*1000000/datac.GenerationMWh2014
datac["appliedInt2015"]=(datac.Diversion2015+datac.Withdrawal2015)*1000000/datac.GenerationMWh2015

datac["consumptionInt2011"]=datac.Consumption2011*1000000/datac.GenerationMWh2011
datac["consumptionInt2012"]=datac.Consumption2012*1000000/datac.GenerationMWh2012
datac["consumptionInt2013"]=datac.Consumption2013*1000000/datac.GenerationMWh2013
datac["consumptionInt2014"]=datac.Consumption2014*1000000/datac.GenerationMWh2014
datac["consumptionInt2015"]=datac.Consumption2015*1000000/datac.GenerationMWh2015

datac = datac[datac.Consumption2015>0]
axes = datac.boxplot(column='consumptionInt2015',rot=20,by="Prime_Mover_Description", return_type='axes')
for ax in axes.values():
    ax.set_ylim(0, 20000) 