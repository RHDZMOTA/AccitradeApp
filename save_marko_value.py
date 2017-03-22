#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 19:30:17 2017

@author: rhdzmota
"""

# %% 

from trading_session import * 

import time 
import datetime as dt
import numpy as np
import pandas as pd

# %% Open session 

ts = TradingSession(user='xd8877',pw='Mexico0r',alias='StaticMarkowitz')
time.sleep(5)

# %% Get portfolio value 

value = ts.browser.find_element_by_xpath('//span[@class="float_right"]').text
date  = dt.datetime.strftime(dt.datetime.now(),'%Y/%m/%d')

# %%

# load prev log and detemine index 
log = np.load('marko_value.npy').item()
n = np.max(list(log.keys())) + 1 

# save 
log[n]={'date':date,'value':value}
np.save('marko_value.npy',log)

# %%
ts.close()

# %%
