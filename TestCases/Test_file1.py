import pytest

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

class Test_py:
    @pytest.mark.xfail
    def test_sum_001(self):   # item -->Test Case --> start with 'test_'
        a = 3
        b = 5
        sum = a + b

        if sum == 8:
            print("test_sum_001 is Passed")
            assert True
        else:
            print("test_sum_001 is failed")
            assert False


    def test_mul_001(self):
        a = 3
        b = 5
        sum = a + b

        if sum == 16:
            print("test_mul_001 is Passed")
            assert False
        else:
            print("test_mul_001 is failed")
            assert True
    @pytest.mark.skip
    def test_mul_002(self):
        a = 3
        b = 5
        mul = a * b

        if mul == 16:
            print("test_mul_001 is Passed")
            assert False
        else:
            print("test_mul_001 is failed")
            assert True

    @pytest.mark.skip
    def sum_001(self):   # this item/function will not consier as testcase because of name
        a = 3
        b = 5
        sum = a + b

        if sum == 16:
            print("test_mul_001 is Passed")
            assert False
        else:
            print("test_mul_001 is failed")
            assert True

    @pytest.mark.group1
    def test_google(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.google.com/")
        logo = driver.find_element(By.CLASS_NAME, "lnXdpd").is_displayed()
        print(logo)
        if logo == True:
            driver.close()
            assert True
        else:
            driver.close()
            assert False
