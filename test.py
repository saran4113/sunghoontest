from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
hidden_browser = False


# selenium 브라우저를 숨긴채로 작업할것인지 선택 hidden_browser
# 디버그를 할때는 숨기지 않고 진행 권장
if hidden_browser:
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('disable-gpu')

capa = DesiredCapabilities.CHROME
capa['pageLoadStrategy'] = "none"
driver = webdriver.Chrome(ChromeDriverManager().install(),
                          desired_capabilities=capa
                          )

# 특정 개체를 로딩 될때까지 wait
wait = WebDriverWait(driver, 10)

# 카페24로그인 페이지
driver.get('https://eclogin.cafe24.com/Shop/')

# id 입력 input이 로딩될때까지 기다린후 id 와 passsword 입력
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mall_id')))

# js를 사용하여 해당 Id에 value 입력
driver.execute_script('''
document.getElementById('mall_id').value = 'dddd';
document.getElementById('userpasswd').value = 'www';
''')
driver.find_element_by_css_selector('#frm_user > div > div.mButton > button').click()
# cafe24 상위 메뉴가 로딩될때까지 기다리기
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#gnb')))

driver.close()