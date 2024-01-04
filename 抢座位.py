from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get('https://libseat.sjtu.edu.cn/#/ic/home')

input("登录并选择分区后继续")
#driver.get('https://libseat.sjtu.edu.cn/#/ic/seatPredetermine/15')
input("请选择好日期以后继续")
#driver.get('https://libseat.sjtu.edu.cn/#/ic/seatPredetermine/15')
wait = WebDriverWait(driver, 50)
x = str(input("请输入你想要的座位号"))

while(True):
    driver.refresh()
    print("尝试中")
    try:
        driver.get('https://libseat.sjtu.edu.cn/#/ic/seatPredetermine/15')
        wait = WebDriverWait(driver, 50)
        # 使用完整的XPath定位元素
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[1]/div['+x+']')))
        # 使用不同的方式滚动到元素
        driver.execute_script("arguments[0].scrollIntoViewIfNeeded();", element)
        #/html/body/div[4]/div/div[3]/span/button[2]

        
        if element.is_displayed() and element.is_enabled():
            print("元素已找到，按Enter键点击.")
            try:
                element.click()
                short_wait = WebDriverWait(driver, 3)
                popup = short_wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]')))
                print("弹窗已出现")
                time.sleep(1)
                confirm_button = short_wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[3]/span/button[2]')))
                print("找到确认按钮")

            # 点击确认按钮
                ActionChains(driver).move_to_element(confirm_button).click().perform()
                print("点击了确认按钮")
                
                popup = short_wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div/div[3]/div[1]')))
                print("弹窗已出现")
                time.sleep(1)
                confirm_button = short_wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div/div[3]/div[1]/div/div[3]/span/button[1]')))
                print("找到确认按钮")

            # 点击确认按钮
                ActionChains(driver).move_to_element(confirm_button).click().perform()
                print("点击了确认按钮")
            except:
                print("被人约了")
                continue
        else:
            print("找到了元素，但它不可见或不可点击")
    except (NoSuchElementException, TimeoutException) as e:
        print("未能找到元素或超时:", e)
# finally:
    #     driver.quit()
