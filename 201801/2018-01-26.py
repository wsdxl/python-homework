'''
python的 ActionChains方法
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get('http://118.31.19.120:3000/signin')
driver.find_element_by_id('name').send_keys('helloworld')
driver.find_element_by_id('pass').send_keys('123456')
driver.find_element_by_class_name('span-primary').click()
driver.find_element_by_class_name('span-success').click()
driver.find_element_by_id('tab-value').click()
driver.find_element_by_css_selector('#tab-value > option:nth-child(2)').click()
driver.find_element_by_id('title').send_keys('1234567890')
menu=driver.find_element_by_class_name('CodeMirror-scroll')
ActionChains(driver).move_to_element(menu).click().perform()
area=driver.find_element_by_css_selector('div.CodeMirror-scroll > div:nth-child(2)')
ActionChains(driver).move_to_element(menu).send_keys('2222222222222222').perform()
driver.find_element_by_class_name('submit_btn').click()