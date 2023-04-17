import pytest

from modules.models import Edu_module, Section


class TestEdu_Module:
    def test_create_module(self, module_one):
        assert module_one == Edu_module.objects.get(pk=module_one.pk)
        assert hasattr(module_one, 'title')
        assert hasattr(module_one, 'description')

    def test_update_module(self, module_one):
        title, description = 'Title 2', 'Description 2'
        module_one.title = title
        module_one.description = description
        module_one.save()
        module_one_from_db = Edu_module.objects.get(title=title)
        assert module_one_from_db.description == description
        assert module_one_from_db.title == title

    def test_filter_module(self, module_two):
        assert Edu_module.objects.filter(title=module_two.title).exists()
        assert Edu_module.objects.filter(description=module_two.description).exists()


class TestSection:
    def test_section_create(self, section_one):
        assert section_one == Section.objects.get(pk=section_one.pk)
        assert hasattr(section_one, 'title')
        assert hasattr(section_one, 'module')

    def test_update_section(self, section_two, module_one):
        title = 'Something'
        section_two.title = title
        section_two.module = module_one
        section_two.save()
        section_two_from_db = Section.objects.get(title=title)
        assert section_two_from_db.title == title
        assert section_two_from_db.module == module_one

    def test_two_different_sections_create(self, section_one, section_two):
        assert section_one.pk != section_two.pk

    def test_correct_sections_module(self, section_one, section_two):
        assert section_one.module != section_two.module


