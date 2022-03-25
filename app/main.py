"""Генератор приветствий."""


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name (str): Имя пользователя

    Returns:
        str: Текст приветствия
    """
    return 'Privet, {print_name}!'.format(print_name=name.title())
