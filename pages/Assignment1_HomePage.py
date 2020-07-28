from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.proceedToCheckOut1_button_xpath = '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a'
        self.proceedToCheckOut2_button_xpath = '//*[@id="center_column"]/p[2]/a[1]'
        self.proceedToCheckOut3_button_xpath = "//span[text()='Proceed to checkout']"
        self.proceedToCheckOut4_button_xpath = '//*[@id="form"]/p/button'
        self.agree_Checkbox__id= "cgv"
        self.bankpayment_button_xpath= "//a[@class='bankwire']"
        self.confirmPayment_xpath = "//span[text()='I confirm my order']"


    def Shopping(self):

        wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(10)

        #find menu item women
        element = self.driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[1]/a')

        #hover and click on T-shirts
        hov = ActionChains(self.driver).move_to_element(element)
        hov.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/ul/li[1]/ul/li[1]/a'))).click()
        
        #keep track of windows
        self.parent = self.driver.current_window_handle
        self.handles = self.driver.window_handles

        #find product image
        element = self.driver.find_element_by_xpath('//*[@id="center_column"]/ul/li/div/div[1]/div/a[1]')

        #hover and click add to cart
        hov = ActionChains(self.driver).move_to_element(element)
        hov.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a[1]'))).click()

        # change to frame
 
        for i in self.handles:
            if (i not in self.parent):
                self.driver.switch_to.window(i)

        self.driver.find_element_by_xpath(self.proceedToCheckOut1_button_xpath).click()
        self.driver.switch_to.window(self.parent)
        self.driver.execute_script("window.scrollBy(0, 600);")

        self.driver.find_element_by_xpath(self.proceedToCheckOut2_button_xpath).click()


        self.driver.find_element_by_xpath(self.proceedToCheckOut3_button_xpath).click()

        

        self.driver.find_element_by_id(self.agree_Checkbox__id).click()
        self.driver.find_element_by_xpath(self.proceedToCheckOut4_button_xpath).click()
        self.driver.execute_script("window.scrollBy(0, 600);")

        self.driver.find_element_by_xpath(self.bankpayment_button_xpath).click()
        self.driver.find_element_by_xpath(self.confirmPayment_xpath).click()
        print("Order confirmed successfully")
