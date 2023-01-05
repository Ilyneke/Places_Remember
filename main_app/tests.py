from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, get_user
from random import randint
from re import search


class BaseFunctions(TestCase):
    def main_test(self, usr='test_user', passw='test_password'):
        # создание тестового клиента
        c = Client()

        # проверка доступности сайта
        response = c.get('/')
        assert response.status_code == 200

        # создание тестового пользователя
        User.objects.create_user(username=usr, password=passw)
        assert usr in str(*get_user_model().objects.all())

        # авторизация
        assert c.login(username=usr, password=passw)

        # проверка того что записей нет
        empty_get = c.get('/').content.decode('utf-8')
        assert 'У вас нет ни одного воспоминания' in empty_get

        # получаем csrf токен
        csrf_token = search(pattern='"csrfmiddlewaretoken" value="([A-Za-z0-9]+)"', string=empty_get).group(1)

        # генерируем уникальные поля формы
        fields = {
            'title': 'Заголовок #' + str(randint(0, 99)),  # с помощью randint() генерируем случайные поля
            'description': 'Описание #' + str(randint(0, 99)),
        }

        # формируем поля для post запроса
        data = {'csrfmiddlewaretoken': csrf_token,
                'title': fields['title'],
                'description': fields['description'],
                'author': get_user(c).pk,
                'lat': '6745475',
                'lng': '7732314',
                'zoom': '10',
                }

        # отправляем форму
        c.post('/', data)

        # проверяем, что запись появилась
        not_empty_get = c.get('/').content.decode('utf-8')
        for field in fields.values():  # ищем сгенерированные записи на странице
            assert field in not_empty_get
