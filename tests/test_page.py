"""Модули"""
import time
import selenium.webdriver.common.action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.touch_action import TouchAction


def test_wait(driver):
    """
    Первый тест, на залогин, потом превратить в фикстуру
    """

    actions = selenium.webdriver.common.action_chains.ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver,
                                        mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    time.sleep(30)
    actions = TouchAction(driver)
    actions.perform()
