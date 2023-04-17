import pytest

from rest_framework.test import APIClient
from modules.models import Edu_module

client = APIClient()


@pytest.mark.django_db
class TestEdu_ModuleList:
    def test_get_modules(self, module_one, module_two):
        response = client.get('/api/education_modules_list/')

        assert response.status_code == 200

    def test_post_module(self, module_one):
        payload = dict(
            title=module_one.title,
            description=module_one.description
        )
        response = client.post('/api/education_modules_list/', payload)
        data = response.data['modules']

        assert response.status_code == 201
        assert data['title'] == payload['title']
        assert data['description'] == payload['description']


@pytest.mark.django_db
class TestEdu_ModuleDetail:
    def test_get_module(self, module_one):
        response = client.get(f'/api/education_modules_detail/{module_one.pk}/')
        data = response.data['module']

        assert response.status_code == 200
        assert data['title'] == module_one.title
        assert data['description'] == module_one.description

    def test_update_module(self, module_two):
        payload = dict(
            title='title',
            description='description'
        )
        print(module_two.title)
        response = client.put(f'/api/education_modules_detail/{module_two.pk}/', payload)
        print(module_two.title)
        data = response.data['module']

        assert response.status_code != 400
        assert data['title'] == payload['title']
        assert data['description'] == payload['description']

    def test_delete_module(self, module_one):
        response = client.delete(f'/api/education_modules_detail/{module_one.pk}/')

        assert response.status_code == 204

class TestSectionViewSet:
    pass






