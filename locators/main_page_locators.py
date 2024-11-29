from selenium.webdriver.common.by import By

class MainPageLocators:
    LOCATOR_QUESTION = (By.XPATH, ".//*[@id='accordion__heading-{}']")
    LOCATOR_ANSWER = (By.XPATH, ".//*[@id='accordion__panel-{}']")
    SUB_HEADER = (By.XPATH, "//div[contains(text(),'Вопросы о важном')]")