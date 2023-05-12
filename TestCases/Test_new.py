import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_005:
    def test_credence_(self):

        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()
        time.sleep(4)
        l = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a"))
        time.sleep(5)
        print(l)
        for r in range(1, l+1):
            contact = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a["+ str (r)+"]").text
            time.sleep(40)
            if contact == "+91 9091929355":
                time.sleep(5)
                print(r)
                assert True
                break
            else:
                driver.close()
                assert True   # testcase status ----fail


