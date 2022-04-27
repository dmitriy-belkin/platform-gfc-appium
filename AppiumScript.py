from appium import webdriver

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "11",
    "deviceName": "Android Emulator",
    "app": "D:/app.apk",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
