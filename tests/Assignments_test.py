from selenium import webdriver
import pytest
from pages.Assignment1_LoginPage import LoginPage
from pages.Assignment1_HomePage import HomePage
from pages.Assignment2_MytripPage import MytripPage
from utils import utils1 as utils1
import csv


@pytest.mark.usefixtures("test_setup")
class TestAssignmentTestLogin():
    def test_creat_users_assignment1(self,test_setup):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get(utils1.URL1)
        login = LoginPage(driver)
        path = r"tests\user_data.csv"
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                if row:
                    username    = row[0].strip()
                    password    = row[1].strip()
                    gender      = row[2].strip()
                    firstname   = row[3].strip()
                    lastname    = row[4].strip()
                    address     = row[5].strip()
                    city        = row[6].strip()
                    state       = row[7].strip()
                    zipcode     = row[8].strip()
                    phone       = row[9].strip()


                login.create_user(username,
                            gender, 
                            firstname, 
                            lastname,
                            password,
                            address,
                            city,
                            state,
                            zipcode,
                            phone)
                driver.implicitly_wait(10)
                print(f"user {username} created")
                driver.get(utils1.URL1)
                login.login_out()






        

    def test_assignment1_test(self,test_setup):
        driver = self.driver
        driver.implicitly_wait(10)
        #driver = driver.get(utils1.URL1)
        driver.get(utils1.URL1)
        login = LoginPage(driver)
        
        login.login_App(utils1.USERNAME,utils1.PASSWORD)
        driver.get(utils1.URL1)
        
        home = HomePage(driver)
        home.Shopping()
        driver.get(utils1.URL1)
        driver.implicitly_wait(5)

    def test_assignment2_test(self,test_setup):
        driver = self.driver
        driver.get(utils1.URL2)
        booking = MytripPage(driver)
        booking.Flight_booking(utils1.fromcity, utils1.tocity)

