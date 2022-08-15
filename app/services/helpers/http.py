from typing import Any, Dict
from http import HTTPStatus


class HttpResponse:

    def __init__(self, status_code: int, body: Any = None):
        self.status_code = status_code
        self.body = body

    def __repr__(self):
        return f"HttpResponse (status_code={self.status_code}, body={self.body})"


class HttpError(Exception):
    def __init__(
        self,
        status_code: int,
        message: str = HTTPStatus.INTERNAL_SERVER_ERROR.phrase
    ):
        self.status_code = status_code
        self.message = message

    def __repr__(self):
        return f'HttpError (status_code={self.status_code}, message={self.message})'


class HttpStatus:
    @staticmethod
    def ok_200(body: Any) -> HttpResponse:
        return HttpResponse(HTTPStatus.OK, body)


class HttpRequest:
    def __init__(self, header: Dict = {}, body: Dict = {}, query: Dict = {}):
        self.header = header
        self.body = body
        self.query = query

    def __repr__(self):
        return (
            f"HttpRequest (header={self.header}, body={self.body}, query={self.query})"
        )
