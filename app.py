import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from webdriver_manager.chrome import ChromeDriverManager
import platform
from webdriver_manager.core.utils import ChromeType

st.title('米国株価可視化アプリ')

def aaaaaa():
    url = "https://www.irisplaza.co.jp/index.php?KB=SHOSAI&SID=P537205"
    if (platform.system() == "Windows"):
        options = webdriver.ChromeOptions()
        chrome_service = fs.Service(executable_path=ChromeDriverManager().install())
    else:
        options = webdriver.ChromeOptions()
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        options.add_argument('--user-agent=' + ua)
        options.add_argument("--headless")
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        chrome_service = fs.Service(executable_path=ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

    browser = webdriver.Chrome(options=options,service=chrome_service)
    browser.close()





if st.button('Say hello'):
    st.write('Why hello there')
    aaaaaa()
    
    st.write('Done')
else:
    st.write('Goodbye')
