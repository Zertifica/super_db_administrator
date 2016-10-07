from selenium import webdriver

from django.test import LiveServerTestCase
from django.conf import settings


class SuperDBTestCase(LiveServerTestCase):

    def setUp(self):
        chromedriver = settings.BASE_DIR+'/../chromedriver'
        self.browser = webdriver.Chrome(chromedriver)
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_user_in_index(self):
        home_page = self.browser.get(self.live_server_url + '/')
        title_element = self.browser.find_element_by_css_selector('#main_heading')
        self.assertEqual('SuperDB Administrator', title_element.text)
