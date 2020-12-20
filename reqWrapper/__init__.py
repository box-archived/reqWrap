# -*- coding: utf-8 -*-

import requests as requests
from requests import utils
from requests import packages
from requests import Request, Response, PreparedRequest
from requests import session, Session
from requests import codes
from requests.exceptions import (
    RequestException, Timeout, URLRequired,
    TooManyRedirects, HTTPError, ConnectionError,
    FileModeWarning, ConnectTimeout, ReadTimeout
)

from .api import request, get, options, head, post, put, patch, delete
from .model import SafeResponse
