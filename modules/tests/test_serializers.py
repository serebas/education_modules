from django.forms import model_to_dict

from modules.serializers import *

class TestEdu_ModuleSerializer:

    serializer = Edu_ModuleSerializer

    def test_serialize_model(self, module_one):
        serializer = self.serializer(module_one)

        assert serializer.data
        assert serializer.data['title'] == module_one.title
        assert serializer.data['description'] == module_one.description

    def test_serializer_data(self, module_one):
        expected_data = dict(title='Test title', description='Test description')
        serializer = self.serializer(module_one, data=expected_data)

        assert serializer.is_valid()
        assert serializer.validated_data == expected_data
        assert serializer.errors == {}


class TestSectionSerializer:

    serializer = SectionSerializer

    def test_serialize_section(self, section_one, section_two):
        serializer = self.serializer([section_one, section_two], many=True)

        assert serializer.data

    def test_serializer_data(self, section_one, module_two):
        expected_data = dict(title='Test title', module=module_two.pk)
        serializer = self.serializer(section_one, data=expected_data)

        assert serializer.is_valid()
        assert serializer.errors == {}



