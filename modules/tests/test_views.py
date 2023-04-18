from rest_framework.test import APIClient

client = APIClient()

class TestEdu_ModuleList:

    endpoint = '/api/education_modules_list/'

    def test_get_modules(self, module_one, module_two):
        response = client.get(self.endpoint)
        data = response.data['modules']

        assert response.status_code == 200
        assert len(data) == 2

    def test_post_module(self, module_one):
        payload = dict(title=module_one.title, description=module_one.description)
        response = client.post(self.endpoint, payload)
        data = response.data['modules']

        assert response.status_code == 201
        assert data['title'] == payload['title']
        assert data['description'] == payload['description']


class TestEdu_ModuleDetail:

    endpoint = '/api/education_modules_detail/'

    def test_get_module(self, module_one):
        response = client.get(self.endpoint + f'{module_one.pk}/')
        data = response.data['module']

        assert response.status_code == 200
        assert data['title'] == module_one.title
        assert data['description'] == module_one.description

    def test_update_module(self, module_two):
        payload = dict(title='title', description='description')
        response = client.put(self.endpoint + f'{module_two.pk}/', payload)
        data = response.data['module']

        assert response.status_code != 400
        assert data['title'] == payload['title']
        assert data['description'] == payload['description']

    def test_delete_module(self, module_one):
        response = client.delete(self.endpoint + f'{module_one.pk}/')

        assert response.status_code == 204


class TestSectionViewSet:

    endpoint = '/api/sections/'

    def test_get_sections(self, section_one, section_two):
        response = client.get(self.endpoint)
        data = response.data

        assert response.status_code == 200
        assert len(data) == 2

    def test_get_section(self, section_one):
        response = client.get(self.endpoint + f'{section_one.pk}/')
        data = response.data

        assert response.status_code == 200
        assert data['id'] == section_one.pk

    def test_post_section(self, module_one):
        payload = dict(title='Magic methods', module=module_one.pk)
        response = client.post(self.endpoint, payload)
        data = response.data

        assert response.status_code == 201
        assert data['title'] == payload['title']
        assert data['module'] == payload['module']

    def test_update_section(self, section_one, module_two):
        payload = dict(title='arguments', module=module_two.pk)
        response = client.put(self.endpoint + f'{section_one.pk}/', payload)
        data = response.data

        assert response.status_code == 200
        assert data['title'] == payload['title']
        assert data['module'] == payload['module']

    def test_delete_section(self, section_one):
        response = client.delete(self.endpoint + f'{section_one.pk}/')
        assert response.status_code == 204







