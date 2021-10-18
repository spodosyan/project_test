import pytest
from pages.contact import Contacts
from time import sleep
from pages.base_page import Base
from selenium.common.exceptions import NoSuchElementException

@pytest.mark.usefixtures('set_up')
class TestPositive(Base):
    def test_submit(self):
        driver = self.driver
        contact = Contacts(driver)
        contact.enter_name('Vle')
        contact.enter_email('project@gmail.com')
        contact.enter_telephone(8895922)
        contact.submit_()
        success_message = contact.show_success_message()
        sleep(3)
        try:
            assert success_message.text == "Feedback has been sent to the administrator"
        except NoSuchElementException:
            print('Field error')


@pytest.mark.parametrize('get_func1, output', [(Contacts.get_name, ''), (Contacts.get_email, ''),
                                               (Contacts.get_telephone, ''), (Contacts.get_country, ''),
                                               (Contacts.get_company, ''), (Contacts.get_message, '')])
def test_clear_(self, get_func1, output):
    driver = self.driver
    contact = Contacts(driver)
    contact.enter_name('Vle')
    contact.enter_email('project@gmail.com')
    contact.enter_telephone(158481515)
    contact.enter_country('  ')
    contact.enter_company('BDG')
    contact.enter_message('cvbhjfghmhb, xfcvgb')
    contact.clear_()
    sleep(3)
    assert get_func1(contact) == output