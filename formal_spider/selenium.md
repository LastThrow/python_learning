1、加载网页
from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com")
driver.save_screenshot("./baidu.png")

2、定位操作
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()

3、查看请求信息
driver.get_cookies()
driver.page_source  获取网页的html
driver.current_url

4、退出
driver.close()
driver.quit() 

Selenium可以控制浏览器
PhantomJS是无界面浏览器，可以把网页加载到内存，并指向JS代码
