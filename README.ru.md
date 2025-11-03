# Placeholder for now
[![CodeFactor](https://www.codefactor.io/repository/github/serjo2/hentailibbadge)](https://www.codefactor.io/repository/github/serjo2/hentailib)

# 🎓 FESTU Timetable Library

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Лицензия: MIT](https://img.shields.io/badge/Лицензия-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Версия PyPI](https://img.shields.io/pypi/v/hentailib.svg)](https://pypi.org/project/hentailib/)
[![Скачивания PyPI](https://img.shields.io/pypi/dm/hentailib.svg)](https://pypi.org/project/hentailib/)
English | [Russian](https://github.com/SerJo2/hentailib-lib/blob/master/README.ru.md)

A Python library for easy access and manipulation of FESTU (Far Eastern State Transport University) class schedules.
Библиотека для удобного получения и работы с хентай сайтами
## ✨ Features

- 🚀 Простой и интуитивно понятный API
- 📅 Получение случайно страницы или страницы по id
- 🛡️ Full type annotations and error handling
- 📚 Полная типизация и обработка ошибок
- ✨ Автоматическое автодополнение тэгов

## 📦 Установка

```bash
pip install hentailib
```

## 🚀 Быстрый стартt
Получение url случайной страницы с rule34
```python
from hentailib import Rule34Api

# set up client
client = Rule34Api("YOUR_API_HERE", "YOUR_USER_ID_HERE")

# get random page
response = client.utils.get_random_page("hu_tao")

# print url
print(response.url)
```
Получение страницы по id
```python
from hentailib import Rule34Api

# set up client
client = Rule34Api("YOUR_API_HERE", "YOUR_USER_ID_HERE")

# get random page
response = client.get_title(15220657)

# print url
print(response.url)
```

## 🐛 Bug Reports and Issues
Если вы обнаружили ошибку или у вас есть предложение по улучшению, создайте [issue](https://github.com/SerJo2/hentailib/issues) на GitHub.

## 🤝 Разработка
Установка для разработки
```bash
git clone https://github.com/SerJo2/hentailib.git
cd hentailib
```
Running Tests
```bash
pytest tests/ -v
```
## 📄 License
Этот проект распространяется под лицензией MIT. Подробнее см. в файле [LICENSE](https://github.com/SerJo2/hentailib/blob/master/LICENSE).

## 👨‍💻 Автор
#### Onii-Chan
- Email: skobochki.ad@mail.ru
- GitHub: [SerJo2](https://github.com/SerJo2)
## ⭐ ⭐ Не забудьте поставить звезду на GitHub, если проект вам помог!
