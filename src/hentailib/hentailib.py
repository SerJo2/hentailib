from sys import audit

import requests
from random import choice
from typing import Optional, List


class Rule34Api:
    """Class Rule34Api used for store api key and use other classes

        Attributes:
            api_key (str): Api key from Rule34Api
            base_url (str): Base url for requests
            _utils (Utils): Utils class instance

    """

    def __init__(self, api_key: str, base_url: str = "https://api.rule34.xxx/index.php?page=dapi&s=post&q=index"):
        """Initializes Rule34Api class with the given parameters.

        Args:
            api_key: Api key from Rule34Api
            base_url: Base url for requests. Default is "https://api.rule34.xxx/index.php?page=dapi&s=post&q=index"

        """
        self.api_key = api_key
        self.base_url = base_url
        self._utils = Utils(self)

    @property
    def utils(self):
        """



        """
        return self._utils

    def get_title(self, page_id: int) -> 'TitleClass':
        """

        Args:
            page_id: Page id

        Returns:
            TitleClass: Contains information about the requested title

        """
        return TitleClass(page_id, self)


class Utils:
    """Class Utils contains various utilities for working with rule34.

    Attributes:
        site_api (Rule34Api): Api Class for use a Rule34 Api

    """

    def __init__(self, site_api: Rule34Api):
        """Initializes Utils with the given parameters.

        Args:
            site_api (Rule34Api): Api Class for use a Rule34 Api
        """
        self.site_api = site_api

    def get_random_page(self, tags: str, limit=100, do_autocomplete=True) -> Optional['TitleClass']:
        """Get a random page from Rule34 with given tags

        Args:
            tags (str): Tags used for searching
            limit (int): The number of pages from which random selection will be made. Default is 100
            do_autocomplete (bool): Will autocomplete from the site be used

        Returns:
            TitleClass: Page from Rule34
        """
        try:
            tags = self.autocomplete_multiple_tags(tags)

            params = {
                "limit": limit,
                "tags": tags,
                "json": 1
            }

            response = requests.get(self.site_api.base_url + self.site_api.api_key,
                                    params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            print(data)
            data = choice(data)
            page_id = data["id"]
            print(data["id"])
            return TitleClass(page_id, self.site_api)

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def get_pages_by_tags(self, tags: List[str]) -> List['TitleClass']:
        pass

    @staticmethod
    def autocomplete_single_tag(text: str, ranking=0) -> str:
        """Autocompletes one tag(without spaces) by Rule34 autocomplete

        Args:
            text: Single tag
            ranking: Which tag rank from zero will be used

        Returns:
            str: autocompleted tag
        """
        attrs = ""
        if text[0] == "-":
            attrs = "-"
            text = text[1:]

        response = requests.get("https://api.rule34.xxx/autocomplete.php?q=" + text).json()
        return attrs + response[ranking]["value"]

    def autocomplete_multiple_tags(self, tags: str):
        split_tags = tags.split()
        autocompleted_tags = list()
        for i in split_tags:
            x = self.autocomplete_single_tag(i)
            autocompleted_tags.append(x)

        return " ".join(autocompleted_tags)



class TitleClass:
    """A class containing information about a specific title

    Attributes:
        site_api (Rule34Api): Api Class for use a Rule34 Api
        id (int): Page id
        url (str): Url link to picture
        width (int): Image width
        height (int): Image height
        owner (str): Image uploader
        score (int): Score of the post
        source (str): Source of the picture
        tags (str): Tags

    """

    def __init__(self, page_id: int, site_api: Rule34Api):
        """Initializes TitleClass with the given parameters.

        Calls __get_data() to request title data.

            Args:
                site_api (Rule34Api): Api Class for use a Rule34 Api
                page_id (int): Page id
        """

        self.site_api = site_api
        self.id = page_id
        self.url = None
        self.width = None
        self.height = None
        self.owner = None
        self.score = None
        self.source = None
        self.tags = None

        self.__get_data()

    def __get_data(self):
        """Get data from Rule34Api

        """
        try:
            params = {
                "limit": 1,
                "id": self.id,
                "json": 1
            }

            response = requests.get(self.site_api.base_url + self.site_api.api_key,
                                    params=params, timeout=10)

            response.raise_for_status()
            print(response.text)
            data = response.json()

            self.url = data[0]["file_url"]
            self.width = data[0]["width"]
            self.height = data[0]["height"]
            self.owner = data[0]["owner"]
            self.score = data[0]["score"]
            self.source = data[0]["source"]
            self.tags = data[0]["tags"]

        except requests.exceptions.RequestException as e:
            raise PageLoadError(f"Не удалось загрузить страницу {self.id}: {e}")
        except KeyError as e:
            raise PageLoadError(f"Неверный формат данных страницы: отсутствует ключ {e}")


class PageLoadError(Exception):
    """Exception class for loading page errors


    """
    def __init__(self, message="An unexpected custom error occurred."):
        self.message = message
        super().__init__(self.message)
