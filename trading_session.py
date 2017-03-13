#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 21:19:04 2017

@author: rhdzmota
"""

# %%


# Map company name to available stock name
long_dict = {
    'Arca Continental':'AC',
    'Alfa':'ALFA.A',
    'Alsea':'ALSEA',
    'América Móvil':'AMX.L',
    'Grupo Aeroportuario del Sureste':'ASUR.B',
    'Grupo Bimbo':'BIMBO.A',
    'CEMEX':'CEMEX.CPO',
    'Grupo Elektra':'ELEKTRA',
    'Fomento Económico Mexicano':'FEMSA.UBD',
    'Grupo Aeroportuario del Pacífico':'GAP.B',
    'Grupo Carso':'GCARSO.A1',
    'Gentera':'GENTERA',
    'Grupo Financiero Inbursa':'GFINBUR.O',
    'Grupo Financiero Banorte':'GFNORTE.O',
    'Banregio Grupo Financiero':'GFREGIO.O',
    'Grupo México':'GMEXICO.B',
    'Gruma':'GRUMA.B',
    'Empresas ICA':'ICA',
    'Industrias CH':'ICH.B',
    'Infraestructura Energética Nova':'IENOVA',
    'Kimberly-Clark de México':'KIMBER.A',
    'Coca-Cola FEMSA':'KOF.L',
    'Genomma Lab Internacional':'LAB.B',
    'La Comer':'LACOMER.UBC',
    'Grupo Lala':'LALA.B',
    'EL PUERTO DE LIVERPOOL':'LIVEPOL.C1',
    'Mexichem':'MEXCHEM',
    'iShares NAFTRAC':'NAFTRAC.ISHRS',
    'Nemak':'NEMAK.A',
    'OHL México':'OHLMEX',
    'Grupo Aeroportuario del Centro Norte':'OMA.B',
    'INDUSTRIAS PE?OLES':'PENOLES',
    'Promotora y Operadora de Infraestructura':'PINFRA',
    'Grupo Financiero Santander Mexico':'SANMEX.B',
    'Grupo Simec':'SIMEC.B',
    'Grupo Televisa':'TLEVISA.CPO',
    'Wal-Mart de México':'WALMEX'
}

# Map available stock name to yahoo format
yahoo_dict = {
    'AC':'AC.MX',
    'ALFA.A':'ALFAA.MX',
    'ALSEA':'ALSEA.MX',
    'AMX.L':'AMXL.MX',
    'ASUR.B':'ASURB.MX',
    'BIMBO.A':'BIMBOA.MX',
    'CEMEX.CPO':'CEMEXCPO.MX',
    'ELEKTRA':'ELEKTRA.MX',
    'FEMSA.UBD':'FEMSAUBD.MX',
    'GAP.B':'GAPB.MX',
    'GCARSO.A1':'GCARSOA1.MX',
    'GENTERA':'GENTERA.MX',
    'GFINBUR.O':'GFINBURO.MX',
    'GFNORTE.O':'GFNORTEO.MX',
    'GFREGIO.O':'GFREGIOO.MX',
    'GMEXICO.B':'GMEXICOB.MX',
    'GRUMA.B':'GRUMAB.MX',
    'ICA':'ICA.MX',
    'ICH.B':'ICHB.MX',
    'IENOVA':'IENOVA.MX',
    'KIMBER.A':'KIMBERA.MX',
    'KOF.L':'KOFL.MX',
    'LAB.B':'LABB.MX',
    'LACOMER.UBC':'LACOMERUBC.MX',
    'LALA.B':'LALAB.MX',
    'LIVEPOL.C1':'LIVEPOLC1.MX',
    'MEXCHEM':'MEXCHEM.MX',
    'NAFTRAC.ISHRS':'NAFTRACISHRS.MX',
    'NEMAK.A':'NEMAKA.MX',
    'OHLMEX':'OHLMEX.MX',
    'OMA.B':'OMAB.MX',
    'PENOLES':'PENOLES.MX',
    'PINFRA':'PINFRA.MX',
    'SANMEX.B':'SANMEXB.MX',
    'SIMEC.B':'SIMECB.MX',
    'TLEVISA.CPO':'TLEVISACPO.MX',
    'WALMEX':'WALMEX.MX'
}



# %% ACTITRADE 
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

class TradingSession(object):
    
    desc = 'Trading Session for Accitrade.'
    url = 'https://www.accitrade.com/AcciTradeCoach/home.action'
    
    def __init__(self, user,pw,driv_r='',alias=''):
        
        # get operative system: Linux, Windows, Darwin 
        import platform
        operative_system = platform.system().lower()
        if len(driv_r)==0:
            driv_r = 'drivers/{}/chromedriver'.format(operative_system)
        
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
            
        # Validate and submit 
        self.browser.find_element_by_xpath('//a[@id="validar"]').click()
        time.sleep(3)
        self.browser.find_element_by_xpath('//a[@id="enviar"]').click()
        
        
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