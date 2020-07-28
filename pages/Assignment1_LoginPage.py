from selenium.webdriver.support.ui import Select

class LoginPage():

    def __init__(self, driver):
      self.driver = driver
      self.sign_in_xpath = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
      self.sign_out_xpath = '//*[@id="header"]/div[2]/div/div/nav/div[2]/a'
      self.username_textbox_id = "email"
      self.password_textbox_id = "passwd"
      #self.login_button_xpath = "span[text()='Sign in']"
      self.submit_login = "SubmitLogin"

      #create user data
      self.create_user_email_textbox_id = 'email_create'
      self.create_user_submit_button_id = 'SubmitCreate'
      self.create_user_id_gender_id_1 = 'id_gender1'
      self.create_user_id_gender_id_2 = 'id_gender2'
      self.create_user_firstname_textbox_id = 'customer_firstname'
      self.create_user_lastname_textbox_id = 'customer_lastname'
      self.create_user_password_textbox_id = 'passwd'
      self.create_user_address1_textbox_id = 'address1'
      self.create_user_city_textbox_id = 'city'
      self.create_user_state_textbox_id = 'id_state'
      self.create_user_postcode_textbox_id = 'postcode'
      self.create_user_phone_textbox_id = 'phone_mobile'
      self.create_user_register_button_id = 'submitAccount'


      # = 'days'
      # = 'months'
      # = 'years'


    def  create_user(self, email,
                        gender, 
                        firstname, 
                        lastname,
                        password,
                        address,
                        city,
                        state,
                        zipcode,
                        phone):
        
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.sign_in_xpath).click()
        self.driver.implicitly_wait(5)
        
        elem = self.driver.find_element_by_id(self.create_user_email_textbox_id)
        elem.clear()
        elem.send_keys(email)
        elem = self.driver.find_element_by_id(self.create_user_submit_button_id)
        elem.click()
        self.driver.implicitly_wait(5)
        if gender == "Mr":
            elem = self.driver.find_element_by_id(self.create_user_id_gender_id_1)
        elif gender == "Ms":
            elem = self.driver.find_element_by_id(self.create_user_id_gender_id_2)
        elem.click()

        elem = self.driver.find_element_by_id(self.create_user_firstname_textbox_id)
        elem.clear()
        elem.send_keys(firstname)

        elem = self.driver.find_element_by_id(self.create_user_lastname_textbox_id)
        elem.clear()
        elem.send_keys(lastname)

        elem = self.driver.find_element_by_id(self.create_user_password_textbox_id)
        elem.clear()
        elem.send_keys(password)

        elem = self.driver.find_element_by_id(self.create_user_address1_textbox_id)
        elem.clear()
        elem.send_keys(address)

        elem = self.driver.find_element_by_id(self.create_user_city_textbox_id)
        elem.clear()
        elem.send_keys(city)

        elem = Select(self.driver.find_element_by_id(self.create_user_state_textbox_id))
        elem.select_by_visible_text(state)
        #elem.send_keys(state)

        elem = self.driver.find_element_by_id(self.create_user_postcode_textbox_id)
        elem.clear()
        elem.send_keys(zipcode) 

        elem = self.driver.find_element_by_id(self.create_user_phone_textbox_id)
        elem.clear()
        elem.send_keys(phone) 
                

        elem = self.driver.find_element_by_id(self.create_user_register_button_id).click()




    def  login_App(self, username, password):
        
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.sign_in_xpath).click()
        elem = self.driver.find_element_by_id(self.username_textbox_id)
        elem.clear()
        elem.send_keys(username)

        elem = self.driver.find_element_by_id(self.password_textbox_id)
        elem.clear()
        elem.send_keys(password)
        elem = self.driver.find_element_by_id(self.submit_login).click()

    def  login_out(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.sign_out_xpath).click()
   
    