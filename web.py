import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# **1️⃣ Streamlit 页面设置**
st.set_page_config(page_title="微博投诉自动化", layout="wide")
st.title("微博投诉自动化工具 🚀")
st.markdown("### **请输入投诉链接（不同分类输入不同框，不填的分类会自动跳过）**")

st.markdown("**📝 请确保你已经登录微博，否则投诉可能无法提交！**")
st.markdown("[👉 点击这里登录微博](https://weibo.com/) （请在新窗口登录后返回）")

# **2️⃣ 创建不同类别的输入框**
categories = {
    "网暴他人-LWK": st.text_area("🛑 网暴他人-xxx（每行一个链接）"),
    "网暴他人-WCC": st.text_area("🛑 网暴他人-yyy（每行一个链接）"),
    "饭圈不友善": st.text_area("🤬 饭圈不友善（每行一个链接）"),
    "饭圈谩骂": st.text_area("💢 饭圈谩骂（每行一个链接）"),
    "涉黄/低俗信息": st.text_area("🔞 涉黄/低俗信息（每行一个链接）"),
}

options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222"  # 连接到已打开的 Chrome 进程

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# **7️⃣ "开始投诉" 按钮**
if st.button("🚀 开始投诉"):
    for category, links in categories.items():
        link_list = links.strip().split("\n") if links.strip() else []
        for url in link_list:
            if category == "网暴他人-xxx":
                try:
                    print(f"🔗 处理链接: {url}")
                    driver.get(url)
                    time.sleep(3)  # 确保页面加载

                    # 尝试查找 "展开全部分类"，如果找不到直接跳过
                    try:
                        expand_button = driver.find_element(By.XPATH, "//span[contains(text(), '展开全部分类')]")
                        expand_button.click()
                        time.sleep(1)
                    except:
                        print(f"⚠️ {url} 找不到 '展开全部分类'，跳过！")
                        continue  # 直接跳过当前链接，进入下一个

                    # 选择 "网络暴力"
                    cyberbullying_link = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), '网络暴力')]"))
                    )
                    driver.execute_script("arguments[0].click();", cyberbullying_link)
                    time.sleep(1)

                    # 选择 "网暴他人"
                    cyberbullying_link = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), '网暴他人')]"))
                    )
                    driver.execute_script("arguments[0].click();", cyberbullying_link)
                    time.sleep(1)

                    # 点击 "继续投诉"
                    continue_report_button = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[@node-type='continueReportBtn']"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView();", continue_report_button)
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", continue_report_button)
                    time.sleep(1)

                    # 点击 "授权实名认证信息"
                    authorize_button = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '点击授权认证信息')]"))
                    )
                    authorize_button.click()
                    time.sleep(1)

                    # 输入被投诉人昵称
                    text_input = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@node-type='netAttackUserNameTextEl']"))
                    )
                    text_input.send_keys("xxx's weibo id")

                    # 输入投诉内容
                    text_area = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//textarea[@node-type='textEl']"))
                    )
                    text_area.send_keys("恶意网暴诋毁中伤国家运动员，宣传不良风气，有损国家统一。") #可自行修改

                    # 勾选 "我已阅读"
                    checkbox = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@node-type='readRoleInput']"))
                    )
                    if not checkbox.is_selected():
                        checkbox.click()

                    # 点击 "提交"
                    submit_button = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[@node-type='subBtn']"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", submit_button)

                    print(f"✅ {url} 投诉提交成功！")
                    time.sleep(2)  # 确保页面提交完毕后再进行下一个

                except Exception as e:
                    print(f"❌ {url} 发生错误，跳过此链接: {e}")
                    continue  # 继续下一个链接

            elif category == "网暴他人-yyy":
                try:
                    print(f"🔗 处理链接: {url}")
                    driver.get(url)
                    time.sleep(3)  # 确保页面加载

                    # 尝试查找 "展开全部分类"，如果找不到直接跳过
                    try:
                        expand_button = driver.find_element(By.XPATH, "//span[contains(text(), '展开全部分类')]")
                        expand_button.click()
                        time.sleep(1)
                    except:
                        print(f"⚠️ {url} 找不到 '展开全部分类'，跳过！")
                        continue  # 直接跳过当前链接，进入下一个

                    # 选择 "网络暴力"
                    cyberbullying_link = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), '网络暴力')]"))
                    )
                    driver.execute_script("arguments[0].click();", cyberbullying_link)
                    time.sleep(1)

                    # 选择 "网暴他人"
                    cyberbullying_link = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), '网暴他人')]"))
                    )
                    driver.execute_script("arguments[0].click();", cyberbullying_link)
                    time.sleep(1)

                    # 点击 "继续投诉"
                    continue_report_button = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[@node-type='continueReportBtn']"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView();", continue_report_button)
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", continue_report_button)
                    time.sleep(1)

                    # 点击 "授权实名认证信息"
                    authorize_button = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '点击授权认证信息')]"))
                    )
                    authorize_button.click()
                    time.sleep(1)

                    # 输入被投诉人昵称
                    text_input = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@node-type='netAttackUserNameTextEl']"))
                    )
                    text_input.send_keys("yyy's weibo id") 

                    # 输入投诉内容
                    text_area = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//textarea[@node-type='textEl']"))
                    )
                    text_area.send_keys("恶意网暴诋毁中伤国家运动员，宣传不良风气，有损国家统一。")

                    # 勾选 "我已阅读"
                    checkbox = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@node-type='readRoleInput']"))
                    )
                    if not checkbox.is_selected():
                        checkbox.click()

                    # 点击 "提交"
                    submit_button = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[@node-type='subBtn']"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", submit_button)

                    print(f"✅ {url} 投诉提交成功！")
                    time.sleep(2)  # 确保页面提交完毕后再进行下一个

                except Exception as e:
                    print(f"❌ {url} 发生错误，跳过此链接: {e}")
                    continue  # 继续下一个链接

            elif category == "饭圈不友善":
                try:
                    print(f"🔗 处理链接: {url}")
                    driver.get(url)
                    time.sleep(3)  # 确保页面加载

                    # 尝试查找 "展开全部分类"，如果找不到直接跳过
                    try:
                        expand_button = driver.find_element(By.XPATH, "//span[contains(text(), '展开全部分类')]")
                        expand_button.click()
                        time.sleep(1)
                    except:
                        print(f"⚠️ {url} 找不到 '展开全部分类'，跳过！")
                        continue  # 直接跳过当前链接，进入下一个

                    # 选择 "饭圈不友善"
                    cyberbullying_link = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), '饭圈不友善')]"))
                    )
                    driver.execute_script("arguments[0].click();", cyberbullying_link)
                    time.sleep(1)

                    # 点击 "继续投诉"
                    continue_report_button = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[@node-type='continueReportBtn']"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView();", continue_report_button)
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", continue_report_button)
                    time.sleep(1)

                    # 勾选 "我已阅读"
                    checkbox = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@node-type='readRoleInput']"))
                    )
                    if not checkbox.is_selected():
                        checkbox.click()

                    # 点击 "提交"
                    submit_button = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[@node-type='subBtn']"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", submit_button)

                    print(f"✅ {url} 投诉提交成功！")
                    time.sleep(2)  # 确保页面提交完毕后再进行下一个

                except Exception as e:
                    print(f"❌ {url} 发生错误，跳过此链接: {e}")
                    continue  # 继续下一个链接
            elif category == "饭圈谩骂":
                try:
                    print(f"🔗 处理链接: {url}")
                    driver.get(url)
                    time.sleep(3)  # 确保页面加载

                    # 尝试查找 "展开全部分类"，如果找不到直接跳过
                    try:
                        expand_button = driver.find_element(By.XPATH, "//span[contains(text(), '展开全部分类')]")
                        expand_button.click()
                        time.sleep(1)
                    except:
                        print(f"⚠️ {url} 找不到 '展开全部分类'，跳过！")
                        continue  # 直接跳过当前链接，进入下一个

                    # 选择 "网络暴力"
                    cyberbullying_link = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), '网络暴力')]"))
                    )
                    driver.execute_script("arguments[0].click();", cyberbullying_link)
                    time.sleep(1)

                    # 选择 "网暴他人"
                    cyberbullying_link = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), '网暴他人')]"))
                    )
                    driver.execute_script("arguments[0].click();", cyberbullying_link)
                    time.sleep(1)

                    # 点击 "继续投诉"
                    continue_report_button = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[@node-type='continueReportBtn']"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView();", continue_report_button)
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", continue_report_button)
                    time.sleep(1)

                    # 点击 "授权实名认证信息"
                    authorize_button = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '点击授权认证信息')]"))
                    )
                    authorize_button.click()
                    time.sleep(1)

                    # 输入被投诉人昵称 "王昶天天都想拿冠军"
                    text_input = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@node-type='netAttackUserNameTextEl']"))
                    )
                    text_input.send_keys("王昶天天都想拿冠军") 

                    # 输入投诉内容
                    text_area = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//textarea[@node-type='textEl']"))
                    )
                    text_area.send_keys("恶意网暴诋毁中伤国家运动员，宣传不良风气，有损国家统一。")

                    # 勾选 "我已阅读"
                    checkbox = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@node-type='readRoleInput']"))
                    )
                    if not checkbox.is_selected():
                        checkbox.click()

                    # 点击 "提交"
                    submit_button = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[@node-type='subBtn']"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", submit_button)

                    print(f"✅ {url} 投诉提交成功！")
                    time.sleep(2)  # 确保页面提交完毕后再进行下一个

                except Exception as e:
                    print(f"❌ {url} 发生错误，跳过此链接: {e}")
                    continue  # 继续下一个链接

            elif category == "涉黄/低俗信息":
                try:
                    print(f"🔗 处理链接: {url}")
                    driver.get(url)
                    time.sleep(3)  # 确保页面加载

                    # 尝试查找 "展开全部分类"，如果找不到直接跳过
                    try:
                        expand_button = driver.find_element(By.XPATH, "//span[contains(text(), '展开全部分类')]")
                        expand_button.click()
                        time.sleep(1)
                    except:
                        print(f"⚠️ {url} 找不到 '展开全部分类'，跳过！")
                        continue  # 直接跳过当前链接，进入下一个

                    # 选择 "涉黄信息"
                    cyberbullying_link = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), '涉黄信息')]"))
                    )
                    driver.execute_script("arguments[0].click();", cyberbullying_link)
                    time.sleep(1)

                    # 选择 "低俗信息"
                    cyberbullying_link = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), '低俗信息')]"))
                    )
                    driver.execute_script("arguments[0].click();", cyberbullying_link)
                    time.sleep(1)

                    # 点击 "继续投诉"
                    continue_report_button = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[@node-type='continueReportBtn']"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView();", continue_report_button)
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", continue_report_button)
                    time.sleep(1)

                    # 勾选 "我已阅读"
                    checkbox = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@node-type='readRoleInput']"))
                    )
                    if not checkbox.is_selected():
                        checkbox.click()

                    # 点击 "提交"
                    submit_button = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//a[@node-type='subBtn']"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", submit_button)

                    print(f"✅ {url} 投诉提交成功！")
                    time.sleep(2)  # 确保页面提交完毕后再进行下一个

                except Exception as e:
                    print(f"❌ {url} 发生错误，跳过此链接: {e}")
                    continue  # 继续下一个链接
    st.success("🎉 **所有投诉已提交完成！**")

# **8️⃣ 关闭 WebDriver**
driver.quit()
