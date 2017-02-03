#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 21:19:04 2017

@author: rhdzmota
"""

# %%


# %% ACTITRADE 
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

class TradingSession(object):
    
    desc = 'Trading Session for Accitrade.'
    url = 'https://www.accitrade.com/AcciTradeCoach/home.action'
    
    def __init__(self, user,pw,driv_r='',alias=''):
        self.browser = webdriver.Chrome(driv_r)
        self.browser.get(self.url)
        self.browser.find_element_by_id('username_login').send_keys(user)
        self.browser.find_element_by_id('password_login').send_keys(pw)
        self.browser.find_element_by_id('password_login').submit()
        
    def getAllElements(self):
        ls = self.browser.find_elements_by_xpath('//*[@id]')
        for i in ls:
            print('{} ---- {}'.format(i.get_attribute('id'),i.tag_name))
    
    def getOptions(self):
        
        # Get the right option 
        self.browser.find_element_by_xpath('//*[@data-url="/AG/operacion.do"]').click()
        time.sleep(2)
        
        # Read Stocks Available
        stocks = self.browser.find_element_by_xpath('//select[@id="idEmision"]').text
        return [i.strip(' ') for i in stocks.split('\n') if len(i.strip(' ')) > 1]

    def performOperation(self,nature,stock,number,price):
        
        # Get the right option 
        self.browser.find_element_by_xpath('//*[@data-url="/AG/operacion.do"]').click()
        time.sleep(2)
        
        # Define Buy or Sell (compra / venta)
        if not 'om' in nature:
            self.browser.find_element_by_xpath('//input[@id="{}"]'.format(nature)).click()
            
        # Record aimed stock
        time.sleep(2)
        select = Select(self.browser.find_element_by_xpath('//select[@id="idEmision"]'))
        select.select_by_visible_text(stock)
        
        # Define number of stocks
        self.browser.find_element_by_xpath('//input[@id="numTitulos"]').send_keys(str(number))
        
        # Define Price
        if not 'erca' in str(price):
            self.browser.find_element_by_xpath('//input[@id="limitado"]').click()
            self.browser.find_element_by_xpath('//input[@id="capPrecio"]').send_keys(str(price))
            
        # Validate
        #self.browser.find_element_by_xpath('//a[@id="validar"]').submit()
        
        
    def getExchangeRates(self):
        
        # Go to right option
        self.browser.find_element_by_xpath('//*[@data-url="/AG/mercado.do"]').click()
        time.sleep(2)
        
        # Select right menu
        left_menu = self.browser.find_element_by_xpath('//ul[@id="left-menu"]')
        opt = left_menu.find_element_by_xpath('//li[@class="dcjq-parent-li"]/a[@class="left-menu-element dcjq-parent jfpw-lvl-1"][@data-prioridad="2"]')
        opt.click()
        time.sleep(2)
        
        # click into "Divisas" 
        #left_menu.find_element_by_xpath('//a[@data-url="/mercado/getGeneralDivisas.do"]').click()
        opt.find_element_by_xpath('//a[@data-url="/mercado/getGeneralDivisas.do"]').click()
        time.sleep(2)
        
        self.browser.find_element_by_xpath('//*[@data-url="/mercado/getGeneralDivisas.do"]').click()
        time.sleep(2)
        elements = self.browser.find_element_by_id("container-tipocambio").text.split('\n')
        dollar = {}
        dollar['Buy'],dollar['Sell'] = float(elements[1]),float(elements[2])
        return dollar
    
    def close(self):
        self.browser.find_element_by_id('log-out').click()
        self.browser.quit()
        
        
        
# %% 

# specify driver 
#driv_r = '/home/rhdzmota/Downloads/chromedriver'


#ts = TradingSession(user='sd8892',pw='Mexico0r',driv_r=driv_r,alias='Trading Session')
#index_ts = TradingSession(user='sd8892',pw='Mexico0r',driv_r=driv_r,alias='Index Replicator')

# %% 

#ts.getExchangeRates()

# %% 

#ts.browser.quit()

# %% 

# %% 