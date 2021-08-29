from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait as WD
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pymysql

driver = webdriver.Chrome(ChromeDriverManager().install())

for i in range(1, 4):
    driver.get(f"https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page={i}")

    wait = WD(driver, 30)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#revolution_main_table > tbody > tr:nth-child(7)')))

    # xpath = "//*[@id='revolution_main_table']/tbody/tr"
    data_1 = driver.find_elements_by_class_name('list1')
    data_2 = driver.find_elements_by_class_name('list0')
    data_1_list = []
    data_2_list = []

    for j in data_1:
        try:
            tag_number = j.text[:7]
            title = j.find_element_by_tag_name('font').text
            reply_count = j.find_element_by_class_name('list_comment2').text
            data = [tag_number, title, reply_count]
            data_1_list.append(data)
        except:
            continue

    for j in data_2:
        try:
            tag_number = j.text[:7]
            title = j.find_element_by_tag_name('font').text
            reply_count = j.find_element_by_class_name('list_comment2').text

            data = [tag_number, title, reply_count]
            data_2_list.append(data)
        except:
            continue

    data_list = data_1_list + data_2_list


driver.close()
