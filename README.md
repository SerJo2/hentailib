# Placeholder for now
[![CodeFactor](https://www.codefactor.io/repository/github/serjo2/hentailibbadge)](https://www.codefactor.io/repository/github/serjo2/hentailib)

# 🎓 Hentailib

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Лицензия: MIT](https://img.shields.io/badge/Лицензия-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Версия PyPI](https://img.shields.io/pypi/v/hentailib.svg)](https://pypi.org/project/hentailib/)
[![Скачивания PyPI](https://img.shields.io/pypi/dm/hentailib.svg)](https://pypi.org/project/hentailib/)
English | [Russian](https://github.com/SerJo2/hentailib-lib/blob/master/README.ru.md)

A Python library for easy access and manipulation of hentai Sites

## ✨ Features

- 🚀 Simple and intuitive API
- 📅 Get random page or page by id from Rule34
- 🛡️ Full type annotations and error handling
- 📚 Comprehensive documentation
- ✨ Automatically autocomplete tags

## 📦 Installation

```bash
pip install hentailib
```

## 🚀 Quick Start
Get random page picture url
```python
from hentailib import Rule34Api

# set up client
client = Rule34Api("YOUR_API_HERE", "YOUR_USER_ID_HERE")

# get random page
response = client.utils.get_random_page("hu_tao")

# print url
print(response.url)
```
Get page by id
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
If you find a bug or have a feature request, please create an issue on GitHub.

## 🤝 Development
Development Installation
```bash
git clone https://github.com/SerJo2/hentailib.git
cd hentailib
```
Running Tests
```bash
pytest tests/ -v
```
## 📄 License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/SerJo2/hentailib-lib/blob/master/LICENSE) file for details.

## 👨‍💻 Author
#### Onii-Chan
- Email: skobochki.ad@mail.ru
- GitHub: [SerJo2](https://github.com/SerJo2)
## ⭐ If this project helped you, please give it a star on GitHub!
