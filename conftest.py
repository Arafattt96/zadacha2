from appium import webdriver
import pytest

server = 'http://localhost:4723/wd/hub'

capabilities = {
  "deviceName": "emulator-5554",
  "automationName": "UIAutomator2",
  "platformName": "Android"
}

@pytest.fixture()
def driver():
    driver = webdriver.Remote(server, capabilities)
    yield driver
    driver.quit()