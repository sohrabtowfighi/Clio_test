"""
    Challenge Project Submission - QA Automation
    Aaron (Sohrab) Towfighi - August 31, 2015
    1.  Use google (google.ca) to find and locate the page and link 
        with latest version of Selenium IDE.
    2.  Use google to perform a search for a random string (ie. running 
        the script will search for a different string each time it is run).
    3.  Use google to enter "bourbon" in the search field. Then find and 
        click the "I'm Feeling Lucky" link for one of the auto-complete 
        suggestions.
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import unittest
import random
import re
from pdb import set_trace

class Tests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)  # set 10 second timeout

    def test_1(self):
        driver = self.driver
        driver.get("http://www.google.ca")
        self.assertIn("Google", driver.title)
        elem = driver.find_element_by_id("lst-ib")
        elem.send_keys("Selenium IDE Download")
        elem.submit()
        elem2= driver.find_element_by_link_text("Download Selenium IDE")
        elem2.click()
        self.assertEquals("http://www.seleniumhq.org/download/",
                          driver.current_url)
        pat = 'http://release\.seleniumhq\.org/selenium-ide/\d\.\d\.\d/selenium-ide-\d\.\d\.\d\.xpi'
        reg = re.compile(pat)
        matches = reg.findall(driver.page_source)
        #if matches is None:
        #    self.assert 0, "Did not find Selenium-IDE download link"
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()



def setup():
    browser = webdriver.Firefox()
    browser.get("https://www.google.ca")
    return browser
    
def wind_down(browser):
    browser.close()
    
def test_1():
    """
        1.  Use google (google.ca) to find and locate the page and link 
            with latest version of Selenium IDE.
    """
    browser = setup()
    assert "Google" in browser.title
    elem = browser.find_element_by_id("lst-ib") # Find the query box
    elem.send_keys("Selenium IDE Download" + Keys.ENTER)
    try:
        elem_2B_clicked = browser.find_element_by_link_text("Download Selenium IDE")
    except NoSuchElementException:
        assert 0, "Did not find seleniumhq"
    elem_2B_clicked.click()
    try:
        element = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.ID, "myDynamicElement")))
    except:
        set_trace()
    find_elements_by_partial_link_text
        

#Keys.DOWN
if __name__ == "__main__":
    test_1()