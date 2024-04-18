from selenium import webdriver
import zipfile
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

# 193.124.226.189:64895:4k9BYdsF:M3m7qdqa
# 136.0.191.42:62933:4k9BYdsF:M3m7qdqa
# 5.188.194.132:64441:4k9BYdsF:M3m7qdqa
# 138.124.32.228:64813:4k9BYdsF:M3m7qdqa

PROXY_HOST = '185.162.130.85' # rotating proxy or host
PROXY_PORT = 10000 # proxy port
PROXY_USER = 'OgyGFpqS' # username
PROXY_PASS = 'RNW78Fm5' # password

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)


def get_chromedriver(use_proxy=False, user_agent=None):
    chrome_options = webdriver.ChromeOptions()
    
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    if use_proxy:
        plugin_file = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(plugin_file, 'w') as zp:
            zp.writestr('manifest.json', manifest_json)
            zp.writestr('background.js', background_js)

        chrome_options.add_extension(plugin_file)

    if user_agent:
        chrome_options.add_argument(f'--user-agent={user_agent}')

    driver = webdriver.Chrome(options=chrome_options)

    return driver


def registration(driver):    
    driver.get('https://xion.bonusblock.io/explore')
    time.sleep(2)
    
    driver.find_element(By.XPATH, "//div[. = ' CONNECT ']").click()
    time.sleep(2)
    
    driver.find_element(By.TAG_NAME, "input").send_keys("gcbklgsd@tenermail.com")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[. = 'Log in / Sign up']").click()
    main_window_handle = driver.current_window_handle
    time.sleep(2)
    
    driver.switch_to.new_window()
    
    driver.get("https://firstmail.ltd/webmail/login")
    time.sleep(2)
    driver.find_element(By.ID, "email").send_keys("gcbklgsd@tenermail.com")
    driver.find_element(By.ID, "password").send_keys("lhxrbsfeS5560")
    driver.find_element(By.XPATH, "//button[. = 'Войти']").click()
    time.sleep(10)
    driver.find_elements(By.CLASS_NAME, "email-list-item")[0].click()
    time.sleep(2)
    
    frame = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(frame)
    verification_code = driver.find_element(By.TAG_NAME, "p").text[0:6]
    
    driver.close()
    driver.switch_to.window(main_window_handle)
    time.sleep(5)
    
    driver.find_element(By.TAG_NAME, "input").send_keys(verification_code)
    driver.find_element(By.XPATH, "//button[. = 'Confirm']").click()
    time.sleep(5)
    driver.find_element(By.TAG_NAME, "svg").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[. = 'Allow and Continue']").click()
    time.sleep(60)
    
def complete_first_task(driver):
    driver.get('https://testnet.staking.burnt.com/')
    time.sleep(5)
    
    driver.find_elements(By.TAG_NAME, "button")[1].click()
    time.sleep(5)
    driver.find_element(By.TAG_NAME, "input").send_keys("josecarter1960@floriamail.com")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[. = 'Log in / Sign up']").click()
    main_window_handle = driver.current_window_handle
    time.sleep(2)
    
    driver.switch_to.new_window()
    
    driver.get("https://firstmail.ltd/webmail/login")
    time.sleep(2)
    driver.find_element(By.ID, "email").send_keys("josecarter1960@floriamail.com")
    driver.find_element(By.ID, "password").send_keys("pflilrlpX2566")
    driver.find_element(By.XPATH, "//button[. = 'Войти']").click()
    time.sleep(10)
    driver.find_elements(By.CLASS_NAME, "email-list-item")[0].click()
    time.sleep(2)
    
    frame = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(frame)
    verification_code = driver.find_element(By.TAG_NAME, "p").text[0:6]
    
    driver.close()
    driver.switch_to.window(main_window_handle)
    time.sleep(5)
    
    driver.find_element(By.TAG_NAME, "input").send_keys(verification_code)
    driver.find_element(By.XPATH, "//button[. = 'Confirm']").click()
    time.sleep(10)
    driver.find_element(By.TAG_NAME, "svg").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[. = 'Allow and Continue']").click()
    time.sleep(30)
    
    driver.find_element(By.XPATH, "//button[. = 'Faucet 1 XION']").click()
    time.sleep(10)
    for i in range(2):
        driver.find_elements(By.XPATH, "//button[. = 'Delegate']")[0].click()
        time.sleep(2)
        driver.find_elements(By.TAG_NAME, "input")[1].send_keys("0.5")
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[. = 'DELEGATE NOW']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[. = 'CONFIRM']").click()
        time.sleep(20)
        driver.find_element(By.XPATH, "//button[. = 'CLOSE']").click()
        time.sleep(10)
    
    driver.find_element(By.XPATH, "//button[. = 'Faucet 1 XION']").click()
    time.sleep(10)
    driver.find_elements(By.XPATH, "//button[. = 'Delegate']")[0].click()
    time.sleep(2)
    driver.find_element(By.TAG_NAME, "input").send_keys("0.5")
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[. = 'DELEGATE NOW']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[. = 'CONFIRM']").click()
    time.sleep(20)
    driver.find_element(By.XPATH, "//button[. = 'CLOSE']").click()
    time.sleep(10)
    
    time.sleep(500)
    

if __name__ == '__main__':
    
    driver = get_chromedriver()
    
    complete_first_task(driver=driver)