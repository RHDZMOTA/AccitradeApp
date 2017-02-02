#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 21:19:04 2017

@author: rhdzmota
"""

# %%


# %% ACTITRADE 
from selenium import webdriver

class TradingSession(object):
    
    desc = 'Trading Session for Accitrade.'
    url = 'https://www.accitrade.com/AcciTradeCoach/home.action'
    
    def __init__(self, user,pw,driv_r='',alias=''):
        self.browser = webdriver.Chrome(driv_r)
        self.browser.get(self.url)
        self.browser.find_element_by_id('username_login').send_keys(user)
        self.browser.find_element_by_id('password_login').send_keys(pw)
        self.browser.find_element_by_id('password_login').submit()
    
    def getOptions(self):
        self.browser.find_element_by_xpath('//*[@data-url="/AG/operacion.do"]').click()
        stocks = self.browser.find_element_by_id('"idEmision"').text
        pass
    
    def buyOperation(self):
        self.browser.find_element_by_xpath('//*[@data-url="/AG/operacion.do"]').click()
        pass
        
    def sellOperation(self):
        self.browser.find_element_by_xpath('//*[@data-url="/AG/operacion.do"]').click()
        pass
        
    def getExchangeRates(self):
        self.browser.find_element_by_xpath('//*[@data-url="/AG/mercado.do"]').click()
        self.browser.find_element_by_class_name('"left-menu-element dcjq-parent jfpw-lvl-1 active"')
        self.browser.find_element_by_xpath('//*[@data-url="/mercado/getGeneralDivisas.do"]').click()
        elements = ts.browser.find_element_by_id("container-tipocambio").text.split('\n')
        dollar = {}
        dollar['Buy'],dollar['Sell'] = float(elements[1]),float(elements[2])
        return dollar
    
    def close(self):
        self.browser.find_element_by_id('log-out').click()
        self.browser.quit()
        
        
        
# %% 

# specify driver 
driv_r = '/home/rhdzmota/Downloads/chromedriver'


ts = TradingSession(user='sd8892',pw='Mexico0r',driv_r=driv_r,alias='Trading Session')
#index_ts = TradingSession(user='sd8892',pw='Mexico0r',driv_r=driv_r,alias='Index Replicator')

# %% 

ts.getExchangeRates()

# %% 

ts.browser.quit()

# %% 

# %% 