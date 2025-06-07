# -*- coding: utf-8 -*-

"""Http类

这是一个非常好用的http封装类

"""
import requests


class Http:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, endpoint: str, params: dict = None) -> str:
        """发起get请求

        Args:
            endpoint: url
            params: get参数

        Examples:
            >>> http = Http()
            >>> http.get("who are you?")

        Note:
            切记，只支持https

        Raises:
            NotImplementedError: if `model` is not in the list

        Returns:
            返回json
        """
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
