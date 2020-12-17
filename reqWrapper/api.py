# -*- coding: utf-8 -*-

from time import sleep
from requests import Session
from .model import SafeResponse


def request(method, url, session=None, retry=5, wait=1, need_200=False, **kwargs):
    session: Session
    if session is None:
        session = Session()

    session.request(method=method, url=url, **kwargs)


def get(url, params=None, retry=5, wait=1, need_200=False, **kwargs):
    r"""Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`
    :param retry: Max retry count.
    :param wait: Time(seconds) between retry
    :param need_200: Set True if you only need status code 200
        else -> fail
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: reqWrapper.SafeResponse
    """

    kwargs.setdefault('allow_redirects', True)
    return request('get', url, params=params, retry=retry, wait=wait, need_200=need_200, **kwargs)


def options(url, retry=5, wait=1, need_200=False, **kwargs):
    r"""Sends an OPTIONS request.

    :param url: URL for the new :class:`Request` object.
    :param retry: Max retry count.
    :param wait: Time(seconds) between retry
    :param need_200: Set True if you only need status code 200
        else -> fail
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: reqWrapper.SafeResponse
    """

    kwargs.setdefault('allow_redirects', True)
    return request('options', url, retry=retry, wait=wait, need_200=need_200, **kwargs)


def head(url, retry=5, wait=1, need_200=False, **kwargs):
    r"""Sends a HEAD request.

    :param url: URL for the new :class:`Request` object.
    :param retry: Max retry count.
    :param wait: Time(seconds) between retry
    :param need_200: Set True if you only need status code 200
        else -> fail
    :param \*\*kwargs: Optional arguments that ``request`` takes. If
        `allow_redirects` is not provided, it will be set to `False` (as
        opposed to the default :meth:`request` behavior).
    :return: :class:`Response <Response>` object
    :rtype: reqWrapper.SafeResponse
    """

    kwargs.setdefault('allow_redirects', False)
    return request('head', url, retry=retry, wait=wait, need_200=need_200, **kwargs)


def post(url, data=None, json=None, retry=5, wait=1, need_200=False, **kwargs):
    r"""Sends a POST request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param retry: Max retry count.
    :param wait: Time(seconds) between retry
    :param need_200: Set True if you only need status code 200
        else -> fail
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: reqWrapper.SafeResponse
    """

    return request('post', url, data=data, json=json, retry=retry, wait=wait, need_200=need_200, **kwargs)


def put(url, data=None, retry=5, wait=1, need_200=False, **kwargs):
    r"""Sends a PUT request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param retry: Max retry count.
    :param wait: Time(seconds) between retry
    :param need_200: Set True if you only need status code 200
        else -> fail
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: reqWrapper.SafeResponse
    """

    return request('put', url, data=data, retry=retry, wait=wait, need_200=need_200, **kwargs)


def patch(url, data=None, retry=5, wait=1, need_200=False, **kwargs):
    r"""Sends a PATCH request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param retry: Max retry count.
    :param wait: Time(seconds) between retry
    :param need_200: Set True if you only need status code 200
        else -> fail
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: reqWrapper.SafeResponse
    """

    return request('patch', url, data=data, retry=retry, wait=wait, need_200=need_200, **kwargs)


def delete(url, retry=5, wait=1, need_200=False, **kwargs):
    r"""Sends a DELETE request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :param retry: Max retry count.
    :param wait: Time(seconds) between retry
    :param need_200: Set True if you only need status code 200
        else -> fail
    :return: :class:`Response <Response>` object
    :rtype: reqWrapper.SafeResponse
    """

    return request('delete', url, retry=retry, wait=wait, need_200=need_200, **kwargs)
