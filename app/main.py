"""Генератор приветствий."""


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name (str): Имя пользователя

    Returns:
        str: Текст приветствия
    """
    words = map(lambda word: word.capitalize(), name.split(' '))
    return 'Privet, {0}!'.format(' '.join(words))
