from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class YourStoreSearch():
#-----------------------#
    def __init__(self, driver):
        self.driver = driver
        self.value = 'value'
        self.homeback = '//*[@id="logo"]/h1/a'
        self.search_bar = 'search'
        self.search_button = '//*[@id="search"]/span/button/i'
        self.itemfound = '//*[@id="content"]/div[3]/div/div/div[1]/a/img'
        self.quantity = 'quantity'
        self.buttoncart = 'button-cart'
        self.cartotal = 'cart-total' 
        self.viewcart = '//*[@id="cart"]/ul/li[2]/div/p/a[1]/strong/i'
        self.desktopdrop = '//*[@id="menu"]/div[2]/ul/li[1]/a'
        self.seealldesk = 'see-all'
        self.lapnotdrop = '//*[@id="menu"]/div[2]/ul/li[2]/a'
        self.seealllapnot = '//*[@id="menu"]/div[2]/ul/li[2]/div/a'
        self.components = '//*[@id="menu"]/div[2]/ul/li[3]/a'
        self.seallcomponents = '//*[@id="menu"]/div[2]/ul/li[3]/div/a'
        self.tablets = '//*[@id="menu"]/div[2]/ul/li[4]/a'
        self.software = '//*[@id="menu"]/div[2]/ul/li[5]/a'
        self.phones = '//*[@id="menu"]/div[2]/ul/li[6]/a'
        self.cameras = '//*[@id="menu"]/div[2]/ul/li[7]/a'
        self.mp3s = '//*[@id="menu"]/div[2]/ul/li[8]/a'
        self.seeallmp3s = '//*[@id="menu"]/div[2]/ul/li[8]/div/a'
        self.removeitem = '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[2]/i'
        self.checkoutbutton = '//*[@id="content"]/div[3]/div[2]/a'
        self.accountbutton = 'button-account' 
        self.name = 'firstname'
        self.lastname = 'lastname'
        self.email = 'input-payment-email'
        self.phone = 'telephone'
        self.password = 'input-payment-password'
        self.passconfirm = 'input-payment-confirm'
        self.adress = 'address_1'
        self.city = 'city'
        self.postcode = 'postcode'
        self.countrydrop = '//*[@id="input-payment-country"]'
        self.regiondrop = '//*[@id="input-payment-zone"]'
        self.shipping = 'shipping_address'
        self.agree = 'agree'
        self.buttonregister = 'button-register'
        self.buttonship = 'button-shipping-address'
        self.shipmethod = '//*[@id="button-shipping-method"]'
        self.paymethod = 'payment_method'
        self.continueship = 'button-payment-method'
        self.confirm = 'button-confirm' 
        self.myaccount = '//*[@id="top-links"]/ul/li[2]'
        self.regiser = '//*[@id="top-links"]/ul/li[2]/ul/li[1]/a'
        self.usermail = 'input-email'
        self.userphone = 'input-telephone'
        self.userpassword = 'input-password'
        self.userpasswordconf = 'input-confirm'
        self.useragree = '//*[@id="content"]/form/div/div/input[1]'
        self.go = '//*[@id="content"]/form/div/div/input[2]'
    #--------------------------------------------#
    def home(self):
        self.driver.find_element(By. XPATH, self.homeback).click()

    def search(self, item):
        self.driver.find_element(By. NAME, self.search_bar).click()
        self.driver.find_element(By. NAME, self.search_bar).send_keys(item)
        self.driver.find_element(By. XPATH, self.search_button).click()
        self.driver.find_element(By. XPATH, self.itemfound).click()
    
    def categories(self):
        self.driver.find_element(By. XPATH, self.desktopdrop).click()
        self.driver.find_element(By. CLASS_NAME, self.seealldesk).click()
        self.driver.find_element(By. XPATH, self.lapnotdrop).click()
        self.driver.find_element(By. XPATH, self.seealllapnot).click()
        self.driver.find_element(By. XPATH, self.components).click()
        self.driver.find_element(By. XPATH, self.seallcomponents).click()
        self.driver.find_element(By. XPATH, self.tablets).click()
        self.driver.find_element(By. XPATH, self.software).click()
        self.driver.find_element(By. XPATH, self.phones).click()
        self.driver.find_element(By. XPATH, self.cameras).click()
        self.driver.find_element(By. XPATH, self.mp3s).click()
        self.driver.find_element(By. XPATH, self.seeallmp3s).click()
    
    def add(self, item):
        self.driver.find_element(By. NAME, self.quantity).clear()
        self.driver.find_element(By. NAME, self.quantity).send_keys(item)
        self.driver.find_element(By. ID, self.buttoncart).click()
        self.driver.find_element(By. ID, self.cartotal).click()
        self.driver.find_element(By. XPATH, self.viewcart).click()
    
    def remove(self):
        self.driver.find_element(By. XPATH, self.removeitem).click()

    def checkout(self, name, lastname, email, phone, password, confirm, adress, city, postcode):
        self.driver.find_element(By. XPATH, self.checkoutbutton).click()
        self.driver.find_element(By. ID, self.accountbutton).click()
        self.driver.find_element(By. NAME, self.name).send_keys(name)
        self.driver.find_element(By. NAME, self.lastname).send_keys(lastname)
        self.driver.find_element(By. ID, self.email).send_keys(email)
        self.driver.find_element(By. NAME, self.phone).send_keys(phone)
        self.driver.find_element(By. ID, self.password).send_keys(password)
        self.driver.find_element(By. ID, self.passconfirm).send_keys(confirm)
        self.driver.find_element(By. NAME, self.adress).send_keys(adress)
        self.driver.find_element(By. NAME, self.city).send_keys(city)
        self.driver.find_element(By. NAME, self.postcode).send_keys(postcode)
        selectcountry = Select(self.driver.find_element(By. XPATH, self.countrydrop))
        selectcountry.select_by_visible_text('Argentina')
        selectstate = Select(self.driver.find_element(By. XPATH, self.regiondrop))
        selectstate.select_by_visible_text('Buenos Aires')
        self.driver.find_element(By. NAME, self.shipping).click()
        self.driver.find_element(By. NAME, self.agree).click()
        self.driver.find_element(By. ID, self.buttonregister).click()
        self.driver.find_element(By. ID, self.buttonship).click()
        self.driver.find_element(By. XPATH, self.shipmethod).click()          
        self.driver.find_element(By. NAME, self.agree).click()
        self.driver.find_element(By. ID, self.continueship).click()
        self.driver.find_element(By. ID, self.confirm).click()
    
    def createAccount(self, name, lastname, email, phone, password, confirmpassword):
        self.driver.find_element(By. XPATH, self.myaccount).click()
        self.driver.find_element(By. XPATH, self.regiser).click()
        self.driver.find_element(By. NAME, self.name).send_keys(name)
        self.driver.find_element(By. NAME, self.lastname).send_keys(lastname)
        self.driver.find_element(By. ID, self.usermail).send_keys(email)
        self.driver.find_element(By. ID, self.userphone).send_keys(phone)
        self.driver.find_element(By. ID, self.userpassword).send_keys(password)
        self.driver.find_element(By. ID, self.userpasswordconf).send_keys(confirmpassword)
        self.driver.find_element(By. XPATH, self.useragree).click()
        self.driver.find_element(By. XPATH, self.go).click()