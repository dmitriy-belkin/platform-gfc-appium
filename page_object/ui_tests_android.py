"""Модули"""
import selenium.webdriver.common.action_chains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput



def test_wait(driver):
    """
    Первый тест, на залогин, потом превратить в фикстуру
    """
    actions = selenium.webdriver.common.action_chains.ActionChains(driver)
    driver.implicitly_wait(5)
    actions.w3c_actions = ActionBuilder(driver,
                                        mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(x=230, y=220)
    actions.w3c_actions.pointer_action.click()
    actions.w3c_actions.perform()
    print('done')
