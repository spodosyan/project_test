from typing import Text
from locators.Locators import LocatorsXPath
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Contacts:
    def __init__(self, driver):
        self.driver = driver
        self.name = LocatorsXPath.name
        self.email = LocatorsXPath.email
        self.telephone = LocatorsXPath.telephone
        self.country = LocatorsXPath.country
        self.company = LocatorsXPath.company
        self.message = LocatorsXPath.message
        self.submit = LocatorsXPath.submit
        self.clear = LocatorsXPath.clear
        self.name_error_message = LocatorsXPath.name_error_message
        self.name_error_field = LocatorsXPath.name_error_form
        self.success_message = LocatorsXPath.success_message
        self.email_error_message = LocatorsXPath.email_error_message
        self.phone_error_message = LocatorsXPath.phone_error_message



    def enter_name(self, name):
        input_name = self.driver.find_element_by_xpath(self.name)
        input_name.send_keys(name)
        print("name")

    def get_name(self):
        return self.driver.find_element_by_xpath(self.name).get_attribute('value')

    def enter_email(self, email):
        input_email = self.driver.find_element_by_xpath(self.email)
        input_email.send_keys(email)
        print("email")

    def get_email(self):
        return self.driver.find_element_by_xpath(self.email).get_attribute('value')

    def enter_telephone(self, phone):
        input_telephone = self.driver.find_element_by_xpath(self.telephone)
        input_telephone.send_keys(phone)
        print("phone")

    def get_telephone(self):
        return self.driver.find_element_by_xpath(self.telephone).get_attribute('value')

    def enter_country(self, country):
        input_country = self.driver.find_element_by_xpath(self.country)
        input_country.send_keys(country)
        print("country")

    def get_country(self):
        return self.driver.find_element_by_xpath(self.country).get_attribute('value')

    def enter_company(self, company):
        input_company = self.driver.find_element_by_xpath(self.company)
        input_company.send_keys(company)
        print("company")

    def get_company(self):
        return self.driver.find_element_by_xpath(self.company).get_attribute('value')

    def enter_message(self, message):
        input_message = self.driver.find_element_by_xpath(self.message)
        input_message.send_keys(message)


    def get_message(self):
        return self.driver.find_element_by_xpath(self.message).get_attribute('value')

    def submit_(self):
        self.driver.find_element_by_xpath(self.submit).click()

    def clear_(self):
        self.driver.find_element_by_xpath(self.clear).click()

    def find_name_error(self):
        return self.driver.find_element_by_xpath(self.name_error_message)

    def show_name_error(self):
        self.driver.find_element_by_xpath(self.name_error_field)

    def show_success_message(self):
        return self.driver.find_element_by_xpath(self.success_message)

    def find_email_error(self):
        return self.driver.find_element_by_xpath(self.email_error_message)

    def find_phone_error(self):
        return self.driver.find_element_by_xpath(self.phone_error_message)