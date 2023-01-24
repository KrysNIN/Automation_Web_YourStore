from selenium.webdriver.common.by import By

class YourStoreItem():
#---------------------#
    def __init__(self, driver):
        self.driver = driver        
        self.value = 'value'
        self.result_banner = '//*[@id="logo"]/h1/a'
        self.founded = '//*[@id="content"]/div[1]/div[2]/h1'
        self.cart = '//*[@id="content"]/div[2]/div/table/tbody/tr[4]/td[2]'
        self.seeall_banner = '//*[@id="content"]/h2'
        self.removebanner = '//*[@id="content"]/p'
        self.confirmbanner = '//*[@id="content"]/h1'
        self.confirmaccount = '//*[@id="content"]/p[1]'
    #---------------------------#
    def banner(self):
        return self.driver.find_element(By. XPATH, self.result_banner).text
    
    def productSearch(self):
        return self.driver.find_element(By. XPATH, self.founded).text
    
    def cartTotal(self):
        return self.driver.find_element(By. XPATH, self.cart).text
    
    def findCategorie(self):
        return self.driver.find_element(By. XPATH, self.seeall_banner).text
    
    def removeItem(self):
        return self.driver.find_element(By. XPATH, self.removebanner).text
    
    def confirmOrder(self):
        return self.driver.find_element(By. XPATH, self.confirmbanner).text
    
    def confirmAccount(self):
        return self.driver.find_element(By. XPATH, self.confirmaccount).text