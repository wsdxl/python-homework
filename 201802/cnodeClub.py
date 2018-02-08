from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
class CnodeJS(object):
    def __init__(self):
        pass


    def register(self, userName,passwd,repasswd,email):
        pass

    def active(self,userName):
        pass

    def login(self, driver, username, passwd):
        driver.get("http://118.31.19.120:3000/")
        loginlink = driver.find_element_by_css_selector('body > div.navbar > div > div > ul > li:nth-child(6) > a')
        loginlink.click()

        usernameInput = driver.find_element_by_id('name')

        usernameInput.clear()
        usernameInput.send_keys(username)

        passInput = driver.find_element_by_id('pass')
        passInput.clear()
        passInput.send_keys(passwd)
        driver.find_element_by_class_name('span-primary').click()
        loginUserName = driver.find_element_by_css_selector('#sidebar > div:nth-child(1) > div.inner > div > div > span.user_name > a').text
        # driver.quit()
        return loginUserName


    def createATopic(self,driver,title,content1):
        driver.get("http://118.31.19.120:3000/")
        driver.find_element_by_css_selector('#create_topic_btn > span').click()
        assertVal = driver.find_element_by_css_selector('#content > div > div.header > ol > li.active').text
        assert assertVal in "发布话题"
        options = driver.find_element_by_id('tab-value').click()
        ask = driver.find_element_by_xpath('//*[@id="tab-value"]/option[3]').click()
        driver.find_element_by_css_selector('#title').send_keys(title)
        content = driver.find_element_by_xpath('//*[@id="create_topic_form"]/fieldset/div/div/div[2]/div[6]/div[1]/div/div/div/div[3]/pre')
        content.click()
        ActionChains(driver).move_to_element(content).key_down(Keys.CONTROL).send_keys('b').key_up(Keys.CONTROL).send_keys(content1).perform()
        # ActionChains(dr).move_to_element(content).send_keys("I don't know her").perform()

        uploadImageIcon = driver.find_element_by_class_name('eicon-image')
        uploadImageIcon.click()
        uploadimageInput = driver.find_element_by_class_name('webuploader-element-invisible')
        uploadimageInput.send_keys('C:\\Users\\Public\\Pictures\\Sample Pictures\\timg.jpg')
        # 一定要找input属性去sendkeys才能传文件'''  '''
        time.sleep(5)
        submitBtn = driver.find_element_by_xpath('//*[@id="create_topic_form"]/fieldset/div/div/div[4]/input')
        # ActionChains(dr).move_to_element(submitBtn).click().perform()
        time.sleep(3)
        submitBtn.click()
        title1 = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/span').text
        return title1



