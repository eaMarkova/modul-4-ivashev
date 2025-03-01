# проверка гита

import doctest

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class TypeOfGenre(Enum):
    BUSINESS_BOOKS = 'Бизнес-книги'
    CLASSICAL_LITERATURE = 'Классическая литература'
    FOREIGN_LITERATURE = 'Зарубежная литература'
    RUSSIAN_LITERATURE = 'Русская литература '
    CHILDREN_BOOKS = 'Детские книги'
    DETECTIVES = 'Детективы'
    FANTASY = 'Фэнтези'
    MODERN_PROSE = 'Современная проза '
    ADVENTURES = 'Приключения'
    HORROR_MYSTICISM = 'Ужасы, мистика'
    NONFICTION_LITERATURE = 'Публицистическая литература'
    ROMANCE_NOVELS = 'Любовные романы'
    ACTION_FILMS_ACTION_PACKED_LITERATURE = 'Боевики, остросюжетная литература'
    PSYCHOLOGY = 'Психология'
    NOVELS_SHORT_STORIES = 'Повести, рассказы'
    POETRY_AND_DRAMA = 'Поэзия и драматургия'
    SCIENCE_AND_EDUCATION = 'Наука и образование'
    HOME_FAMILY_HOBBIES_AND_LEISURE = 'Дом, семья, хобби и досуг'
    COMICS_MANGA_GRAPHIC_NOVELS = 'Комиксы, манга, графические романы'
    ESOTERICISM = 'Эзотерика'
    CULTURE_AND_ART = 'Культура и искусство'
    HUMOROUS_LITERATURE = 'Юмористическая литература'
    RELIGION = 'Религия'
    DICTIONARIES_REFERENCE_BOOKS = 'Словари, справочники'
    BEAUTY_AND_HEALTH = 'Красота и здоровье'
    COMPUTER_LITERATURE = 'Компьютерная литература'



@dataclass
class Years:
    value: int
    tod = datetime.now()
    today = int(f'{tod}'[0:4])

    def __post_init__(self) -> None:
        """
        Метод, проверяет, соответствует ли год издания временным рамкам

        :raise ValueError: Нельзя написать год издания ранее 1564 и позже нынешнего года
        :return: None:

        >>> test_year = Book('Информация','Эмис Мартин',Years(1500),TypeOfGenre.ROMANCE_NOVELS)
        Traceback (most recent call last):
        ...
        ValueError: Нельзя написать год издания ранее 1564 и позже нынешнего года: 1500
        """
        if self.value < 1564 or self.today < self.value:
            raise ValueError(f'Нельзя написать год издания ранее 1564 и позже нынешнего года: {self.value}')



class Publication:
    """
    Класс, представляющий публикации
    """
    def __init__(self,title: str,author: str,year: Years) -> None :
        """
        Создание и подготовка к работе объекты класса

        :param title: str: название публикации
        :param author: str: автор
        :param year: Years: год издания
        """
        self.title: str = title
        self.author: str = author
        self.year: Years = year

    def get_info(self) -> str:
        """
        Метод, выводит информацию объектов класса

        :return: str: главная информация о публикации
        """
        return f'Название : {self.title}, Автор: {self.author}, Год издания: {self.year.value}'


class Book(Publication):
    """
    Класс, представляющий книги
    """
    def __init__(self,title: str,author: str,year: Years, genre: TypeOfGenre) -> None:
        """
        Объединение объектов родительского класса с дочерним

        :param title: str: название публикации
        :param author: str: автор
        :param year: Years: год издания
        :param genre: TypeOfGenre: жанр
        """
        Publication.__init__(self, title,author,year)
        self.genre: TypeOfGenre = genre

    def get_info(self) -> str:
        """
        Метод изменяет информацию о публикации: книга

        :return: str: полная информация о газете + жанр книги
        """
        info: str = super().get_info()
        return f'{info}, Жанр книги: {self.genre.value}'

class Magazine(Publication):
    """
    Класс, представляющий журналы
    """
    def __init__(self, title: str,author: str,year: Years, issue_number: str)-> None:
        """
        Объединение объектов родительского класса с дочерним

        :param title: str: название публикации
        :param author: str: автор
        :param year: Years: год издания
        :param issue_number: номер выпуска
        """
        Publication.__init__(self, title, author, year)
        self.issue_number = issue_number

    def get_info(self)-> str:
        """
        Метод изменяет информацию о публикации: журнал

        :return: str: полная информация о газете + номер выпуска
        """
        info: str = super().get_info()
        return f'{info},Номер выпуска журнала: {self.issue_number}'

class Newspaper(Publication):
    """
    Класс, представляющий газеты
    """
    def __init__(self, title: str,author: str,year: Years, publisher: str)-> None:
        """
        Объединение объектов родительского класса с дочерним

        :param title: str: название публикации
        :param author: str: автор
        :param year: Years: год издания
        :param publisher: издатель
        """
        Publication.__init__(self, title, author, year)
        self.publisher = publisher

    def get_info(self) -> str:
        """
        Метод изменяет информацию о публикации: газета

        :return: str : полная информация о газете + издатель
        """
        info: str = super().get_info()
        return f'{info},Издатель газеты: {self.publisher}'

doctest.testmod()

book = Book('Информация','Эмис Мартин',Years(2007),TypeOfGenre.ROMANCE_NOVELS)
magazine = Magazine('Cosmopolitan', 'Кейт Уайт', Years(2019), '№2')
newspapers = Newspaper('Известия', ' С. В. Сергеев', Years(2022), 'ФГУП «Издательство „Известия“»')

print(book.get_info())
print(magazine.get_info())
print(newspapers.get_info())