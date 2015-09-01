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

def remove_periods(mystring):
    string_list = []
    for i in mystring:
        if i != '.':
            string_list.append(i)
    return ''.join(string_list)

def get_latest_version_href(mymatches):
    version = list()
    pat_version = '\d\.\d\.\d'
    reg_version = re.compile(pat_version)
    max_version = 0
    max_version_index = 0
    for i in range(0,len(mymatches)):
        match = reg_version.search(mymatches[i].groups(0))
        version.append(match.groups(0))
        current_version = remove_periods(version[-1])
        if current_version > max_version:
            max_version = current_version
            max_version_index = i
    latest_version_url = mymatches[max_version_index].groups(0)
    return latest_version_url
    
class Tests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)  # set 10 second timeout

    def test_1(self):
        driver = self.driver
        driver.get("http://www.google.ca")
        set_trace()
        self.assertIn("Google", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("Selenium IDE Download")
        elem2 = driver.find_element_by_id("btnK")
        elem2.click()
        # find the first result
        # advertisements use different xpath
        elem3 = driver.find_element_by_xpath(".//*[@id='rso']/div[2]/div[1]/div/h3/a")
        elem3.click()
        self.assertEqual("http://www.seleniumhq.org/download/",
                          driver.current_url)
                          
        set_trace()
        pat = 'http://release\.seleniumhq\.org/selenium-ide/\d\.\d\.\d/selenium-ide-\d\.\d\.\d\.xpi'
        reg = re.compile(pat)
        matches = reg.findall(driver.page_source)
        if matches is not None:  # result found
            latest_version = get_latest_version_href(matches)
    
   # def test_2(self):
   #     driver = self.driver
   #     driver.get("http://www.google.ca")
        #rand_str = random.random()
    
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