# -*- coding: utf-8 -*-

from requests import Response, Session


class SafeResponse(object):
    def __init__(self, success, response, session):
        self.__success: bool = success
        self.__response: Response = response
        self.__session: Session = session

    @property
    def response(self):
        return self.__response

    @property
    def success(self):
        return self.__success

    @property
    def status_code(self):
        return self.__response.status_code

    @property
    def session(self):
        return self.__session
