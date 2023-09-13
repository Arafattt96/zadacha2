from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from conftest import driver
from objects_fold.ContactObjectClass import ContactClass


@pytest.mark.parametrize("first_name,last_name,phone,email", [("Jone","Doe","+7 (777) 999-34-34","ara@mail.ru")])
def test_add_contact(driver, first_name, last_name, phone, email):
    contact = ContactClass(driver)
    contact.open_app()
    contact.add_contact(first_name, last_name, phone, email)
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "com.google.android.contacts:id/large_title"))).text == f'{first_name} {last_name}'
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//android.widget.RelativeLayout[@content-desc="Call Mobile {phone}"]/android.widget.RelativeLayout/android.widget.TextView[1]'))).text == phone
    contact.click_on_back_button()

def test_delete_contact(driver):
    contact = ContactClass(driver)
    contact.open_app()
    contact.click_on_contact()
    contact.click_on_more_button()
    contact.click_on_delete_button()

def test_cancel_add_contact(driver):
    contact = ContactClass(driver)
    contact.open_app()
    contact.click_add_button()
    contact.click_on_cancel_with_add_contact()