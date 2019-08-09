from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as t
driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)

driver.get('http://ms.advt.sfc.com/login')
'''
#driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/button').click()
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/button').send_keys('123')
'''
# 登录
driver.find_element_by_name('username').click()
driver.implicitly_wait(3000)
driver.find_element_by_name('username').clear()
driver.find_element_by_name('username').send_keys("guanshuxin")
driver.implicitly_wait(3000)
driver.find_element_by_name('password').click()
driver.implicitly_wait(3000)
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys("123456")
driver.implicitly_wait(3000)
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/button/span').click()
driver.implicitly_wait(3000)
# 展开Priceminister下拉框
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/ul/div/li[3]/div').click()
driver.implicitly_wait(3000)
# 选择广告管理
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/ul/div/li[3]/ul/a[1]/li').click()
driver.implicitly_wait(3000)
# 选择上传失败状态
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/span[5]/span').click()
driver.implicitly_wait(3000)
# 用Product id筛选
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[2]/div/div/input').send_keys('80006106')
driver.implicitly_wait(1000)
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[7]/div/button[1]/span').click()
t.sleep(5)
# 下拉展开详情
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div[1]/div[3]/table/tbody/tr/td[1]/div/div/i').click()
t.sleep(5)
# 进入广告详情页面
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div[1]/div[3]/table/tbody/tr/td[11]/div/button').click()
t.sleep(20)

driver.find_element_by_xpath('//*[@id="el-collapse-content-6315"]/div/form/div[5]/div/div/div/div[5]/div[1]').click()
t.sleep(10)










'''
# 删除readonly属性
def js():
    js = "$('input[id=select-date-dom]').removeAttr('readonly')"  # 2.jQuery，移除属性       【成功】
    driver.execute_script(js)
'''
# 添加计划
'''
driver.find_element_by_xpath('/html/body/div[4]').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]/span').click()
driver.implicitly_wait(5)
'''
# 执行完退出
#driver.quit()