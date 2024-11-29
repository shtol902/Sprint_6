from selenium.webdriver.common.by import By

class CookieButton:
    ACCEPT_COOKIE = (By.XPATH, ".//button[@id='rcc-confirm-button']")

class OrderButtonLocators:
    BUTTON_TO_ORDER_HEADER = (By.XPATH, ".//button[@class='Button_Button__ra12g']")
    BUTTON_TO_ORDER_BODY = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

class OrderFormLocators1:
    INPUT_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
    INPUT_LAST_NAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO_STATION = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    KRASNOSELSKAYA_STATION = (By.XPATH, ".//*[contains(text(), 'Красносельская')]")
    LUBYANKA_STATION = (By.XPATH, ".//*[contains(text(), 'Лубянка')]")
    INPUT_PHONE = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[contains(text(),'Далее')]")

class OrderFormLocators2:
    TITLE_ABOUT_RENT = (By.XPATH, ".//*[@class='Order_Header__BZXOb']")
    INPUT_DATA_ORDER = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    CALENDAR_DATA_10 = (By.XPATH, ".//*[@class='react-datepicker__day react-datepicker__day--010']")
    CALENDAR_DATA_20 = (By.XPATH, ".//*[@class='react-datepicker__day react-datepicker__day--020']")
    INPUT_RENTAL_PERIOD = (By.XPATH, ".//*[@class='Dropdown-placeholder']")
    RENT_1_DAY = (By.XPATH, ".//*[contains(text(), 'сутки')]")
    RENT_2_DAYS = (By.XPATH, ".//*[contains(text(), 'двое суток')]")
    CHECKBOX_BLACK_COLOR = (By.XPATH, ".//input[@id='black']")
    CHECKBOX_GREY_COLOR = (By.XPATH, ".//input[@id='grey']")
    INPUT_COMMENT_FOR_COURIER = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    BUTTON_TO_ORDER_IN_FORM = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    DELIVERY_DATE_TOMORROW = (By.XPATH, "//div[contains(@class, 'today')]/following-sibling::div[1]")

class OrderWindowLocators:
    BUTTON_YES_ORDER = (By.XPATH, ".//*[contains(text(), 'Да')]")
    POP_UP_WINDOW_SUCCESSFUL_ORDER = (By.XPATH, ".//*[contains(text(), 'Заказ оформлен')]")
    BUTTON_VIEW_STATUS = (By.XPATH, ".//*[contains(text(), 'Посмотреть статус')]")