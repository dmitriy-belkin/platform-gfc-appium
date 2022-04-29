"""Модули"""
import time
import selenium.webdriver.common.action_chains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


def test_wait(driver):
    """
    Первый тест, на залогин, потом превратить в фикстуру
    """

    actions = selenium.webdriver.common.action_chains.ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver,
                                        mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    time.sleep(30)

    actions.w3c_actions.pointer_action.move_to_location(x=532, y=1100).pointer_up()
