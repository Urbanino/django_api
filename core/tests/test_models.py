from django.test import TestCase
from django.contrib.auth import get_user_model
# Импортируем данную функцию для получения последней актуальной версии модели пользователя (т.к. мы ее будем менять)
from core import models # импортируем модели


def sample_user(email='test@admin.com', password='testpass'):
    """Создает пользователя"""
    return get_user_model().objects.create_user(email, password)


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

    def test_tag_str(self):
        """Тест на текстовое представление модели"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Рыба'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Тест на текстовое представление модели"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Тест на текстовое представление модели"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Steak and mushroom sauce',
            time_minutes=5,
            price=5.00
        )

        self.assertEqual(str(recipe), recipe.title)


