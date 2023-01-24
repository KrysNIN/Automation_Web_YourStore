import time
import unittest
from selenium import webdriver
from YourStore_item import YourStoreItem
from YourStore_search import YourStoreSearch
from selenium.webdriver.chrome.options import Options

class YourStore(unittest.TestCase):
#----------------------------------#
    def setUp(self):
        option = Options()
        option.add_argument ('--ignore-ssl-errors=yes')
        option.add_argument ('--ignore-certificate-errors')        
        self.driver = webdriver.Chrome(chrome_options = option, executable_path='C:/WebDriver/chromedriver.exe')        
        self.driver.get('http://opencart.abstracta.us/')
        self.driver.implicitly_wait(5)
        self.search = YourStoreSearch(self.driver)
        self.item = YourStoreItem(self.driver)
    #-----------------------------------------#
    def test_home(self):
        self.search.home()
        time.sleep(3)
        self.assertTrue('Your Store' in self.item.banner())
    
    def test_search_item(self):
        self.search.search('iphone')
        time.sleep(3)
        self.assertEqual(self.item.productSearch(), 'iPhone')
    
    def test_categories(self):
        self.search.categories()
        time.sleep(5)
        self.assertTrue('MP3 Players' in self.item.findCategorie())

    def test_add_cart(self):
        self.search.search('iphone')
        self.search.add(3)
        time.sleep(3)
        self.assertEqual(self.item.cartTotal(), '$369.60')
    
    def test_remove_item(self):
        self.search.search('iphone')
        self.search.add(3)
        self.search.remove()
        time.sleep(3)
        self.assertEqual(self.item.removeItem(), 'Your shopping cart is empty!')
    
    def test_checkout(self):
        self.search.search('iphone')
        self.search.add(3)
        self.search.checkout(
            'Kryst',
            'NINf',
            '2k2rn@krn.com',
            '12345637',
            '123456',
            '123456',
            'qwerty23c4',
            'Capitol',
            '8000'
            )
        time.sleep(5)
        self.assertTrue('Your order has been placed!' in self.item.confirmOrder())
            
    def test_create_account(self):
        self.search.createAccount(
            'Gabriel',
            'Rodriguez',
            'qwew23i2@eew.com',
            '1114547',
            '123456',
            '123456'
            )
        time.sleep(5)
        self.assertTrue('Congratulations! Your new account has been successfully created!' in self.item.confirmAccount())

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
#-------------------------#
if __name__ == '__main__':
    unittest.main()