#coding=utf-8
import time,re,requests
import selenium
#from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from multiprocessing import Process, Pool

#CMCCAdmin
#aDm8H%MdA

global driver, time_start, time_end,startip,endip
def get_out_ip():
    global endip
    try:
        r = requests.get(r'http://2018.ip138.com/ic.asp')
        endip = re.findall(r'\d+.\d+.\d+.\d+', r.text)[0]
    except:
        print("还没有网络 稍等")
        time.sleep(5)
        get_out_ip()


r = requests.get(r'http://2018.ip138.com/ic.asp')
startip = re.findall(r'\d+.\d+.\d+.\d+', r.text)[0]
print(startip)

# 一直等待某元素可见，默认超时10秒
def is_visible(locator, timeout=10,type="select"):
    if type == "xpath":
        try:
            ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False
    else:
        try:
            ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except TimeoutException:
            return False

# 一直等待某个元素消失，默认超时10秒
def is_not_visible(locator, timeout=10):
    try:
        ui.WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False



t = 5
# 不带界面写法
driver = selenium.webdriver.PhantomJS(executable_path=r"phantomjs-2.1.1-windows\bin\phantomjs.exe")
# 使用谷歌浏览器
#driver = webdriver.Chrome(r"chromedriver.exe")

driver.maximize_window()

print("访问网站")
driver.get('http://192.168.1.1/')

print("输入账号")
if is_visible('[id="txt_Username"]', t + 60):
    driver.find_element_by_id("txt_Username").send_keys('CMCCAdmin')

print("输入密码")
if is_visible('[id="txt_Password"]', t + 60):
    driver.find_element_by_id("txt_Password").send_keys('aDm8H%MdA')

print("点击登录按钮")
if is_visible('[id="btnSubmit"]', t + 60):
    driver.find_element_by_id("btnSubmit").click()

print("选择管理")
if is_visible('[name="mainrel_Managemen"]', t + 60):
    driver.find_element_by_css_selector('[name="mainrel_Managemen"]').click()

print("选择管理2")
if is_visible('[name="subrel_cmccdevicereset" ]', t + 60):
    driver.find_element_by_css_selector('[name="subrel_cmccdevicereset"]').click()

print("切换iframe")
if is_visible('[id="frameContent"]', t + 60):
    driver.switch_to_frame(driver.find_element_by_id('frameContent'))
time_start = time.time()
print("确定弹出框")
driver.execute_script("window.confirm = function(msg) { return true; }")

print("点击重启路由器")
if is_visible('[id="Restart_button"]', t + 60):
    driver.execute_script('''document.querySelector("[id='Restart_button']").click();''')
    # driver.find_element_by_css_selector('[id="Restart_button"]').click()
    print("点击重启路由器成功")


#driver.switch_to_alert().accept()

time.sleep(5)
driver.close()


time.sleep(5)
try:
    r = requests.get(r'http://2018.ip138.com/ic.asp')
    endip = re.findall(r'\d+.\d+.\d+.\d+', r.text)[0]
except:
    print("还没有网络 稍等")
    time.sleep(5)
    get_out_ip()

time_end=time.time()
print('totally cost',time_end-time_start)
print(startip)
print(endip)
