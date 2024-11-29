from selenium.webdriver.common.by import By

class LogoLocators:
    LOGO_YANDEX = (By.XPATH, ".//*[@class='Header_LogoYandex__3TSOI']")
    LOGO_SCOOTER = (By.XPATH, ".//*[@class='Header_LogoScooter__3lsAR']")
    LOGO_DZEN = (By.XPATH, "//div[@class='dzen-layout--desktop-base-header__logoContainer-pu dzen-layout--desktop-base-header__isMorda-2n']")