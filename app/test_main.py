import pytest
from main import greeting

greets = [('Nikita', 'Privet, Nikita!'), ('Olga', 'Privet, Olga!')]
caps = [
    ('Yandex dzen', 'Privet, Yandex Dzen!'),
    ('ilya kuprik', 'Privet, Ilya Kuprik!'),
]


@pytest.mark.parametrize('name,expected', greets)
def test_greeting(name: str, expected: str):
    """Текст приветствия зависит от имени."""
    assert greeting(name) == expected


@pytest.mark.parametrize('name,expected', caps)
def test_capitalize(name: str, expected: str):
    """Слова в имени приветсвия печатаются начинаются прописью."""
    assert greeting(name) == expected
