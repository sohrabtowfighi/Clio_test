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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import random
import re
import unittest
import string
#from pdb import set_trace


def removePeriods(myString):
    string_list = []
    for i in myString:
        if i != '.':
            string_list.append(i)
    return ''.join(string_list)

def getURLofLatestVersion(URL_List):
    version_numbers = list()
    pat_version = '\d\.\d\.\d'
    reg_version = re.compile(pat_version)
    max_version_int = 0
    max_version_index = 0
    for i in range(0,len(URL_List)):
        match = reg_version.search(URL_List[i])
        current_version = match.group(0)
        current_version_int = int(removePeriods(current_version))
        if current_version_int > max_version_int:
            max_version_int = current_version_int
            max_version_index = i
    latest_version_href = URL_List[max_version_index]
    return latest_version_href
    
class Tests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        # set 10 second timeout for element search
        self.driver.implicitly_wait(10) 
        self.wait = WebDriverWait(self.driver, 10)
    
    def test1(self):
        """
        1.  Use google (google.ca) to find and locate the page and link 
            with latest version of Selenium IDE.
        """
        driver = self.driver
        driver.get("http://www.google.ca")     
        assert "Google" in driver.title
        elem_query = driver.find_element_by_name("q")
        elem_query.send_keys("Selenium IDE Download")
        elem_query.send_keys(Keys.ENTER)
        elem_result = driver.find_element_by_link_text("Download Selenium IDE")
        elem_result.click()
        self.wait.until(EC.title_contains('Downloads'))
        assert "http://www.seleniumhq.org/download/" == driver.current_url                          
        pat = 'http://release\.seleniumhq\.org/selenium-ide/\d\.\d\.\d/selenium-ide-\d\.\d\.\d\.xpi'
        reg = re.compile(pat)
        matches = reg.findall(driver.page_source)
        if matches is not None:  # install IDE URL found
            latest_version = getURLofLatestVersion(matches)
        assert matches is not None, "No version of Selenium IDE found"
            
    def test2(self, size=5):
        """
        2.  Use google to perform a search for a random string (ie. running 
            the script will search for a different string each time it is run).
        """
        driver = self.driver
        driver.get("http://www.google.ca")     
        assert "Google" in driver.title
        elem_query = driver.find_element_by_name("q")
        chars = string.ascii_uppercase + string.digits
        random_string = ''.join(random.choice(chars) for i in range(size))
        elem_query.send_keys(random_string + Keys.ENTER)
        # check that a search result loads
        search_result_xpath = ".//*[@id='rso']/div[2]/div[1]/div/h3/a"
        elem_result = driver.find_element_by_xpath(search_result_xpath)      
        assert random_string in driver.title, "Random string is not in title"
    
    def test3(self):
        """
        3.  Use google to enter "bourbon" in the search field. Then find and 
            click the "I'm Feeling Lucky" link for one of the auto-complete 
            suggestions.
        """
        driver = self.driver
        driver.get("http://www.google.ca")     
        assert "Google" in driver.title
        elem_query = driver.find_element_by_name("q")
        elem_query.send_keys('bourbon')
        elem_query.click()  # set focus so that DOWN & RIGHT work.
        elem_query.send_keys(Keys.DOWN*2)# + Keys.RIGHT)
        elem_btn = driver.find_element_by_css_selector(".sbqs_a")
        title = elem_btn.text
        elem_btn.click()
        self.wait.until(EC.title_contains(title))
        assert 'google' not in driver.title.lower()
    
    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()