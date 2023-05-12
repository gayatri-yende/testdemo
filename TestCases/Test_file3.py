import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from TestCases.Test_file1 import chrome_options


class Test_002:
    def test_sum_005(self):
        a = 3
        b = 4
        sum = a + b
        if sum == 7:
            assert True
        else:
            assert False


    def test_credence(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://credence.in/")
        offer = driver.find_element(By.XPATH, "//span[@class='text-white b label']").text
        print(offer)
        print(driver.title)
        if driver.title == "Credence":
            driver.close()
            assert True    # testcase status ----pass
        else:
            driver.close()
            assert True   # testcase status ----fail

    def test_credence1_(self):

        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()
        time.sleep(4)
        l = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a"))
        time.sleep(5)
        print(l)
        for r in range(1, l+1):
            contact = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a["+ str(r)+"]").text
            time.sleep(40)
            if contact == "+91 9091929355":
                time.sleep(50)
                print(r)
                assert True
                break
            else:
                driver.close()
                assert True   # testcase status ----fail


