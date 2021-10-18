#Locators

class LocatorsXPath:
    name = "//body/div[@id='page']/div[@id='main']/div[2]/div[1]/aside[1]/div[1]/section[2]/form[1]/div[1]/span[1]/input[1]"
    email ="//body/div[@id='page']/div[@id='main']/div[2]/div[1]/aside[1]/div[1]/section[2]/form[1]/div[1]/span[2]/input[1]"
    telephone ="//body/div[@id='page']/div[@id='main']/div[2]/div[1]/aside[1]/div[1]/section[2]/form[1]/div[1]/span[3]/input[1]"
    country ="//body/div[@id='page']/div[@id='main']/div[2]/div[1]/aside[1]/div[1]/section[2]/form[1]/div[1]/span[4]/input[1]"
    company = "//body/div[@id='page']/div[@id='main']/div[2]/div[1]/aside[1]/div[1]/section[2]/form[1]/div[1]/span[5]/input[1]"
    message = "//textarea[@name='message']"
    submit = "//a[text()='Submit']"
    clear = "//a[text()='clear']"
    name_error_message = "//div[@class='form-validation-field-0formError parentFormundefined formError']/div[text() = '* This field is required']"
    name_error_form = "//div[@class='form-validation-field-0formError parentFormundefined formError']"
    success_message = "//div[text()='Feedback has been sent to the administrator']"
    email_error_message = "//*[contains(text(), 'This field is required') or contains(text(), 'Invalid email address')]"
    phone_error_message = "//*[contains(text(), 'This field is required') or contains(text(), 'Invalid phone number')]"
