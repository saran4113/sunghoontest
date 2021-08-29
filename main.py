from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

for i in range(1,4):
    driver.get(f"https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page={i}")

    wait = WebDriverWait(driver,100)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#revolution_main_table > tbody > tr:nth-child(7)')))

    data_1 =driver.find_elements_by_class_name('list1')
    data_2 = driver.find_elements_by_class_name('list0')

    data_1_list =[i.text for i in data_1]
    data_2_list = [i.text for i in data_2]
    data_list=data_1_list+data_2_list
    print(data_list)

driver.close()