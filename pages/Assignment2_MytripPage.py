
import time
import datetime

class MytripPage():

    def __init__(self, driver):
       self.driver = driver

       self.someclick_id = "root"
       self.more_dropdown_xpath = "//li[@data-cy='menu_More']"
       self.deals_dropdown_xpath = "//a[@data-cy='submenu_Deals']"
       self.fromcity_id = "hp-widget__sfrom"
       self.bangalore_xpath = "(//li[contains(@aria-label , 'Top Cities : Bangalore, India ')])[1]"
       self.tocity_text_id="hp-widget__sTo"
       self.departDate_id = "hp-widget__depart"
       self.datetoselect_xpath = "//div[@class='ui-datepicker-group ui-datepicker-group-last']//td//a[1]"
       self.search_button_id = "searchBtn"
       #self.indigo_checkbox_xpath = "//p[text()='Non Stop']"
       #self.flights_xpath = "//span[@class='airlineInfo-sctn']"


    def  Flight_booking(self, fromcity, tocity):
        print("Test Started")
        time.sleep(5)
        #print("parent Handle:", self.driver.current_window_handle)
        self.driver.find_element_by_id(self.someclick_id).click()
        self.driver.find_element_by_xpath(self.more_dropdown_xpath).click()
        self.driver.find_element_by_xpath(self.deals_dropdown_xpath).click()
        handles = self.driver.window_handles
        #print(handles)

        self.parent = self.driver.current_window_handle
        handles = self.driver.window_handles

        for i in handles:
            if i not in self.parent:
                self.driver.switch_to.window(i)

        #print("child Handle:", self.driver.current_window_handle)
        time.sleep(2)

        self.fromcity =self.driver.find_element_by_id(self.fromcity_id)
        #self.fromcity.click()
        #self.fromcity.send_keys("New Delhi (DEL)")
        #self.fromcity.clear()
        self.fromcity.send_keys("Bangalore (BLR)")

        #self.driver.find_element_by_xpath('// *[ @ id = "searchWidget"] / div[2]').click()

        #self.fromcity.send_keys("BLR")
        time.sleep(2)
        self.driver.find_element_by_id(self.tocity_text_id).send_keys("Hyderabad (HYD)")
        #   self.driver.find_element_by_id(self.tocity_text_id).send_keys("Hyderabad, India")
        time.sleep(2)

        self.driver.find_element_by_id(self.departDate_id).click()
        self.driver.find_element_by_xpath(self.datetoselect_xpath).click()
        time.sleep(2)
        #self.driver.find_element_by_xpath('//*[@id="js-switch__option"]/div[1]/label').click()
        #time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="js-switch__option"]/div[1]/label').click()
        time.sleep(2)
        self.driver.find_element_by_id(self.search_button_id).click()

        time.sleep(5)

        self.flights = self.driver.find_elements_by_class_name('fli-list one-way')
        print("Total number of flights available for that date: ", len(self.flights))






