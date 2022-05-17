from pathlib import Path
import os.path
import pytest
import base64
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


@pytest.fixture(name="driver", scope="session")
def driver():
    """
    Настройка и запуск драйвера
    """
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "12",
        "deviceName": "Android Emulator",
        "app": "C:/app-release.apk",
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def recorder(driver):
    """
    Запись видео и конвертация файла
    """
    driver.start_recording_screen()
    yield
    video_rawdata = driver.stop_recording_screen()
    video_name = driver.current_activity + time.strftime("%H_%M_%S__%d_%m_%Y")
    project = Path.cwd()
    filepath = os.path.join(str(project) + "/reports/" + str(video_name) + ".mp4")
    with open(filepath, "wb") as vd:
        vd.write(base64.b64decode(video_rawdata))


@pytest.fixture(scope="function")
def prepare(driver):
    """
    Подготовка к тестированию
    Перед началом тестирования происходит авторизация
    По кончанию тестирования - разлогин
    """
    time.sleep(2)
    driver.find_element_by_accessibility_id("Продолжить").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("Профиль, Вкладка 4 из 5").click()
    time.sleep(2)
    driver.tap([(700, 600)])
    #driver.find_element_by_accessibility_id("E-mail")
    time.sleep(5)
    #driver.find_element(By.NAME, "E-mail").send_keys('demetrius.belkin@gmail.com')
    time.sleep(15)