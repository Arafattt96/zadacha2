from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BaseClass():

    def __init__(self, driver):
        self.driver = driver

    def open_app(self):
        self.driver.activate_app("com.google.android.contacts")

    def click_add_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'com.google.android.contacts:id/floating_action_button'))).click()

    def click_save_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'com.google.android.contacts:id/toolbar_button'))).click()

    def click_on_contact(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.slidingpanelayout.widget.SlidingPaneLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ListView/android.view.ViewGroup[2]'))).click()

    def click_on_back_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]'))).click()

    def click_on_more_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageView[@content-desc="More options"]'))).click()

    def click_on_delete_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView'))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'android:id/button1'))).click()

    def click_on_cancel_with_add_contact(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageButton[@content-desc="Cancel"]'))).click()
