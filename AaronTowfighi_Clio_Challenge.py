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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import re

def remove_periods(myString):
    string_list = []
    for i in myString:
        if i != '.':
            string_list.append(i)
    return ''.join(string_list)

def get_latest_version_href(myMatchesString):
    version_numbers = list()
    pat_version = '\d\.\d\.\d'
    reg_version = re.compile(pat_version)
    max_version_int = 0
    max_version_index = 0
    for i in range(0,len(myMatchesString)):
        match = reg_version.search(myMatchesString[i])
        current_version = match.group(0)
        current_version_int = int(remove_periods(current_version))
        if current_version_int > max_version_int:
            max_version_int = current_version_int
            max_version_index = i
    latest_version_href = myMatchesString[max_version_index]
    return latest_version_href
    
class Tests(object):

    def setUp(self):
        self.driver = webdriver.Firefox()
        # set 10 second timeout for element search
        self.driver.implicitly_wait(10) 
        self.wait = WebDriverWait(self.driver, 10)

    def test_1(self):
        driver = self.driver
        driver.get("http://www.google.ca")     
        assert "Google" in driver.title
        elem_query = driver.find_element_by_name("q")
        elem_query.send_keys("Selenium IDE Download" + Keys.ENTER)
        search_result_xpath = ".//*[@id='rso']/div[2]/div[1]/div/h3/a"
        elem_result = driver.find_element_by_xpath(search_result_xpath)
        elem_result.click()
        self.wait.until(EC.title_contains('Downloads'))
        assert "http://www.seleniumhq.org/download/" == driver.current_url                          
        pat = 'http://release\.seleniumhq\.org/selenium-ide/\d\.\d\.\d/selenium-ide-\d\.\d\.\d\.xpi'
        reg = re.compile(pat)
        matches = reg.findall(driver.page_source)
        if matches is not None:  # result found
            latest_version = get_latest_version_href(matches)
        assert matches is not None, "No latest version of Selenium IDE found"
        
    
   # def test_2(self):
   #     driver = self.driver
   #     driver.get("http://www.google.ca")
        #rand_str = random.random()
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    test = Tests()
    test.setUp()
    test.test_1()
    test.tearDown()
