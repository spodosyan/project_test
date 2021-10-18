# #Negative - check that the name field contains only letters and is not empty
# Negative - check that the email is valid
# Negative - phone only digits, not letters, not empty
# Negative - Country only letters and spaces
# Negative- Message cannot have more than 180 letters, can be empty
# Positive - Check the clear button
# Positive - Check that the success notification pops up after form submission

from pages.base_page import Base
from pages.contact import Contacts
import pytest
from time import sleep
from selenium.common.exceptions import NoSuchElementException

@pytest.mark.usefixtures('set_up')
class TestNegative(Base):
    @pytest.mark.parametrize('name', ['blaba55', '$jsncx[', ' '])
    def test_name(self, name):
        driver = self.driver
        contact = Contacts(driver)
        contact.enter_name(name)
        contact.enter_email('project@gmail.com')
        contact.enter_telephone(88989898)
        contact.submit_()
        try:
            contact.show_name_error()
        except NoSuchElementException:
            print("Field error")

    @pytest.mark.parametrize('email, output', [('ghchcgh', '* Invalid email address'),
                                               ('ygug@', '* Invalid email address'),
                                               ('bhh@1515test.com', '* Invalid email address'),
                                               ('gvv@test.hjvj', '* Invalid email address'),
                                               ('  ', '* This field is required\n* Invalid email address')
                                               ]
                             )
    def test_email(self, email, output):
        driver = self.driver
        contact = Contacts(driver)
        contact.enter_name('Vle')
        contact.enter_email(email)
        contact.enter_telephone(648641)
        contact.submit_()
        sleep(3)
        assert contact.find_email_error().text == output

    @pytest.mark.parametrize('phone, output', [('k', '* Invalid phone number'),
                                               ('1', '* Invalid phone number'),
                                               ('dfcbjs155', '* Invalid phone number'),
                                               ('|"?>', '* Invalid phone number'),
                                               ('', '* This field is required\n* Invalid phone number')
                                               ])
    def test_phone(self, phone, output):
        driver = self.driver
        contact = Contacts(driver)
        contact.enter_name('Vle')
        contact.enter_email('project@gmail.com')
        contact.enter_telephone(phone)
        contact.submit_()
        sleep(3)
        try:
            assert contact.find_phone_error().text == output
        except NoSuchElementException:
            print('Field error')
    
    @pytest.mark.parametrize('country', ['blaba55', '$jsncx[', ' '])
    def test_country(self, country,):
        driver = self.driver
        contact = Contacts(driver)
        contact.enter_name('Vle')
        contact.enter_email('project@gmail.com')
        contact.enter_telephone(5415105)
        contact.enter_country(country)
        contact.submit_()
        sleep(3)
        try:
            contact.show_name_error()
        except NoSuchElementException:
            print("Field error")

    @pytest.mark.parametrize('message',[('One morning, when Gregor Samsa woke from troubled dreams,he found himsel transformed in his bed into a horrible vermin. He layon his armour-like back, and if he lifted his head a little he could se')])
    def test_message(self, message):
        driver = self.driver
        contact = Contacts(driver)
        contact.enter_message(message)
        contact.submit_()

        try:
            assert len(message) <= 180

        except:
            print("Field error - Message cannot have more than 180 characters")

