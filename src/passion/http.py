# -*- coding: utf-8 -*-
# @place: Shenzhen, China
# @file: http.py
# @time: 2024/1/22 17:45
"""Http

this is why we play

"""
import requests


class Http:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, endpoint: str, params: dict = None):
        """count the tokens of _input in string or list of string format

        count the tokens of _input using OpenAI tiktoken module, the model is `gpt-3.5-turbo`
        by default. if the model is not supported, then use `cl100k_base` as backup.

        Args:
            endpoint: the input string or list of string
            params: the input string or list of string
        Examples:
            >>> http = Http()
            >>> http.get("who are you?")
            4
            >>> http.get(["who are you?", "How's it going on?"])
            [4, 6]

        Raises:
            NotImplementedError: if `model` is not in the list

        Returns:
            the number of token of a string or the list of token of each string in list
        """
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
