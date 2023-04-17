import pytest
from rest_framework.test import APIClient

from modules.models import Edu_module, Section

#фикстуры для моделей
#____________________________________________________________________________________________
@pytest.fixture
def module_one(db):
    return Edu_module.objects.create(title='Classes in Python', description='Something 1')

@pytest.fixture
def module_two(db):
    return Edu_module.objects.create(title='Functions in Python', description='Something 2')

@pytest.fixture
def section_one(db, module_one):
    return Section.objects.create(title='Objects', module=module_one)

@pytest.fixture
def section_two(db, module_two):
    return Section.objects.create(title='Decorator', module=module_two)

#фикстуры для видов
#_____________________________________________________________________________________________