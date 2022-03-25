import pytest

from app.main import greeting


@pytest.mark.parametrize(
    'name, expected',
    (
        ('Nikita', 'Privet, Nikita!'),
        ('Olga', 'Privet, Olga!'),
    ),
)
def test_greeting(name: str, expected: str):
    """Текст приветствия зависит от имени."""
    assert greeting(name) == expected


@pytest.mark.parametrize(
    'name, expected',
    (
        ('Yandex dzen', 'Privet, Yandex Dzen!'),
        ('ilya kuprik', 'Privet, Ilya Kuprik!'),
    ),
)
def test_capitalize(name: str, expected: str):
    """Слова в имени приветсвия печатаются начинаются прописью."""
    assert greeting(name) == expected
