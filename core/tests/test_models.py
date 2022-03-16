from django.test import TestCase
from django.contrib.auth import get_user_model
# Импортируем данную функцию для получения последней актуальной версии модели пользователя (т.к. мы ее будем менять)


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Тестируем устпешное создание пользователя с почтовым адресом"""

        email = 'test@test.com'  # Создаем переменную в которую запишем корректный адрес почты
        password = 'TestPassword123'  # Тоже самое делаем с паролем

        user = get_user_model().objects.create_user(  # С помощью импортированной функции создаем нового пользователя
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)  # Далее собственно проверяем
        self.assertTrue(user.check_password(password))

        # py manage.py test   Запускаем тесты с помощью этой комманды

        # переходим в модели и прописываем изменнения для пользователей

