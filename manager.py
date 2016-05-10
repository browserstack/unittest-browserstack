import os
import unittest
from selenium import webdriver
from browserstack.local import Local

# Edit these to match your credentials
USERNAME = None
BROWSERSTACK_KEY = None
test_type = 'single'

if "BROWSERSTACK_USERNAME" in os.environ:
    USERNAME = os.environ["BROWSERSTACK_USERNAME"]
if "BROWSERSTACK_ACCESS_KEY" in os.environ:
    BROWSERSTACK_KEY = os.environ["BROWSERSTACK_ACCESS_KEY"]
if "TEST_TYPE" in os.environ:
    test_type = os.environ["TEST_TYPE"]

if not (USERNAME and BROWSERSTACK_KEY):
    raise Exception("Please provide your BrowserStack username and access key")
    sys.exit(1)

class TestBrowserStackSearch(unittest.TestCase):
    _multiprocess_shared_ = True
    driver = None
    bs_local = None

    @classmethod
    def create_driver(self):
        desired_capabilities = TestBrowserStackSearch.get_caps()

        return webdriver.Remote(
                desired_capabilities=desired_capabilities,
                command_executor="http://%s:%s@hub.browserstack.com/wd/hub" % (
                    USERNAME, BROWSERSTACK_KEY
                    )
                )

    @classmethod
    def get_caps(self):
        desired_capabilities = {}
        desired_capabilities['os'] = 'OS X'
        desired_capabilities['os_version'] = 'El Capitan'
        desired_capabilities['browser'] = 'firefox'
        desired_capabilities['browser_version'] = '46'
        desired_capabilities['build'] = 'Sample python tests using unittest'
        desired_capabilities['name'] = 'Sample python unittest'
        if 'local' in test_type.lower():
            desired_capabilities['browserstack.local'] = True
        return desired_capabilities

    @classmethod
    def start_local(self):
        self.bs_local = Local()
        bs_local_args = { "key": "sUiJatw6NhJZpsttcY35", "forcelocal": "true" }
        self.bs_local.start(**bs_local_args)

    @classmethod
    def stop_local(self):
        if self.bs_local is not None:
            self.bs_local.stop()

    @classmethod
    def setUpClass(self):
        if 'local' in test_type.lower():
            self.start_local()
        if 'parallel' not in test_type.lower():
            self.driver = TestBrowserStackSearch.create_driver()

    @classmethod
    def tearDownClass(self):
        self.stop_local()
        if 'parallel' not in test_type.lower():
            self.driver.quit()

    def setUp(self):
        if 'parallel' in test_type.lower():
            self.driver = TestBrowserStackSearch.create_driver()

    def tearDown(self):
        if 'parallel' in test_type.lower():
            self.driver.quit()

    def test_google_search(self):
        self.driver.get("http://www.google.com")
        if not "Google" in self.driver.title:
            raise Exception("Unable to load google page!")
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("BrowserStack")
        elem.submit()
        self.driver.find_element_by_name("btnG").click()
        self.assertTrue("browserstack" in self.driver.title.lower())

    def test_google_search_clone(self):
        self.driver.get("http://www.google.com")
        if not "Google" in self.driver.title:
            raise Exception("Unable to load google page!")
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("BrowserStack")
        elem.submit()
        self.driver.find_element_by_name("btnG").click()
        self.assertTrue("browserstack" in self.driver.title.lower())

if __name__ == '__main__':
    unittest.main()
