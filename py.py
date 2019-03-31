# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import random

def Login():
    username=""
    uid=""
    password=""

    chrome_driver="D:\Python\ChromeDrive\chromedriver.exe"

    browser = webdriver.Chrome(executable_path=chrome_driver)

    browser.get("http://www.weibo.com/")
    browser.maximize_window()
    time.sleep(7)
    # input id="loginname" name="username"
    # input id="password"

    input_username=browser.find_element_by_id("loginname")
    input_username.clear()
    input_username.send_keys(username)

    input_password=browser.find_element_by_name("password")
    input_password.clear()
    input_password.send_keys(password)

    time.sleep(2)
        
    codeimg=browser.find_element_by_xpath("//img[@node-type='verifycode_image']")
    if(codeimg.get_attribute("src")=="about:blank"):
        browser.find_element_by_class_name("W_btn_a").click()
    else:
        input_code=browser.find_element_by_xpath("//input[@value='验证码']")
        input_code.clear()
        code=input("Input Code：")
        input_code.send_keys(code)
        time.sleep(1)
        browser.find_element_by_class_name("W_btn_a").click()
    time.sleep(1)

    while("输入的验证码不正确" in browser.page_source or "请填写" in browser.page_source):
        print("Wrong Verification Code")
        input_code.clear()
        code=input("Input Code：")
        input_code.send_keys(code)
        browser.find_element_by_class_name("W_btn_a").click()
        
    time.sleep(1)

    browser.get("https://weibo.com/u/"+uid+"/home")
    
    time.sleep(1)
    return browser


def post(n, txt):
	input_post=browser.find_element_by_xpath("//textarea[@title='微博输入框']")
	for i in range(n):
		time.sleep(1)
		input_post.clear()
		txt=txt+" ["+str(i)+"] ("+str(random.random())+")"
		input_post.send_keys(txt)
		time.sleep(1)
		browser.find_element_by_xpath("//a[@title='发布微博按钮']").click()
		time.sleep(3)
		if("微博发的太多啦，休息一会再发啦！" in browser.page_source):
			print("发太多，暂时不能发惹。。")
			browser.find_element_by_xpath("//a[@action-type='ok']").click()
			input_post.clear()
			return
		print("Post %d Successfully, %d waitting to post." % (i+1, n-i-1))

#post(20, "test")

def deleteALL():
	time.sleep(3)
	browser.find_element_by_xpath("//a[@nm='name']").click()
	time.sleep(3)
	#browser.get("http://www.weibo.com/5848719965")
	while("ouid" in browser.page_source):
		del_list1=browser.find_elements_by_xpath("//a[@action-type='fl_menu']")
		del_list2=browser.find_elements_by_xpath("//a[@action-type='feed_list_delete']")
		#time.sleep(1)
		for i in range(len(del_list2)):
			del_list1[i].click()
			time.sleep(1)
			del_list2[i].click()
			#time.sleep(1)
			browser.find_element_by_xpath("//a[@action-type='ok']").click()
			time.sleep(1)
			print("Delete 1 Weibo Successfully")
		browser.refresh()
		time.sleep(2)


def delete(n, browser):
    time.sleep(3)
    browser.find_element_by_xpath("//a[@nm='name']").click()
    time.sleep(5)
    count=0
    for i in range(n):
        #time.sleep(1)
        while True:
            try:
                click1=browser.find_element_by_xpath("//a[@action-type='fl_menu']")
            except NoSuchElementException:
                print("Can't find the menu. wait 2 s.")
                sleep(2)
            except Exception:
                print("Exception, refresh and retry. ")
                return "Exception"
            else:
                try:
                    click1.click()
                except Exception:
                    print("Exception, refresh and retry. ")
                    return "Exception"
                else:
                    break
        time.sleep(0.5)
        while True:
            try:
                click2=browser.find_element_by_xpath("//a[@action-type='feed_list_delete']")
            except NoSuchElementException:
                print("Can't find the del btn. wait 2 s.")
                sleep(2)
            except Exception:
                print("Exception, refresh and retry. ")
                return "Exception"
            else:
                try:
                    click2.click()
                except Exception:
                    print("Exception, refresh and retry. ")
                    return "Exception"
                else:
                    break
        time.sleep(1)
        while True:
            try:
                click3=browser.find_element_by_xpath("//a[@action-type='ok']")
            except NoSuchElementException:
                print("Can't find the ok btn. wait 2 s.")
                sleep(2)
            except Exception:
                print("Exception, refresh and retry. ")
                return "Exception"
            else:
                try:
                    click3.click()
                except Exception:
                    print("Exception, refresh and retry. ")
                    return "Exception"
                else:
                    break
        time.sleep(1)
        count+=1
        while(count==10):
            browser.refresh()
            time.sleep(5)
            count=0
        print("Delete %d Weibo Successfully, %d Weibo waitting to delete." % (i+1, n-i-1))
    print("Successfully")
    return 1

# 一次最多删除一页的微博，如果想全部删除，不加参数。
def main():
    browser=Login()
    if browser is not None:
        while True:
            flag=delete(1100, browser)
            if(flag=="Exception"):
                browser.refresh()
            else:
                break
main()
