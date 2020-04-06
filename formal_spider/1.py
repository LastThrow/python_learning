from selenium import webdriver
import time


def main():
    # driver = webdriver.Chrome()
    driver = webdriver.PhantomJS()
    driver.get("http://www.baidu.com")

    # 进行页面截屏
    driver.save_screenshot("./baidu.png")
    # 设置窗口大小
    driver.set_window_size(1920, 1080)
    # 最大化窗口
    driver.maximize_window()

    # 元素定位方法
    # driver.find_element_by_id("kw").send_keys("python")
    # driver.find_element_by_id("su").click()

    # driver获取cookie
    # cookies = driver.get_cookies()
    # print(cookies)
    # print("*"*100)
    # cookies = {i["name"]:i["value"] for i in cookies}

    # driver获取html字符串
    # 得到得是js执行之后的内容，也就是elements的内容，可以按照element些XPath
    print(driver.page_source)
    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    main()
