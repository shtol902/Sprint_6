import allure
import pytest
from data import Url, Questions, Answers
from pages.main_page import HomePage

@allure.feature('Тесты - вопросы о важном')
class TestHomePage:
    @pytest.mark.parametrize(
        'num, question, answer',
        [
            (0, Questions.QUESTION_1, Answers.ANSWER_1),
            (1, Questions.QUESTION_2, Answers.ANSWER_2),
            (2, Questions.QUESTION_3, Answers.ANSWER_3),
            (3, Questions.QUESTION_4, Answers.ANSWER_4),
            (4, Questions.QUESTION_5, Answers.ANSWER_5),
            (5, Questions.QUESTION_6, Answers.ANSWER_6),
            (6, Questions.QUESTION_7, Answers.ANSWER_7),
            (7, Questions.QUESTION_8, Answers.ANSWER_8)
        ]
    )
    @allure.title('Проверка на соответствие текста в вопросах и ответах')
    @allure.description(
        'Находим на главной странице раздел "Вопросы о важном", проверяем текст вопросов и ответов.'
    )
    def test_check_questions_and_answers(self, driver, num, question, answer):
        driver.get(Url.SCOOTER_HOMEPAGE)
        home_page = HomePage(driver)
        assert home_page.check_question_text(num) == question
        assert home_page.check_answer_text(num) == answer