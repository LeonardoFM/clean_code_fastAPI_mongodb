from typing import Any

from app.domain.usecases import UseCase
from app.services.helpers.http import HttpResponse, HttpError, HttpRequest


def fast_api_adapter(request: Any, usecase: UseCase) -> HttpResponse:

    try:
        http_request = HttpRequest(
            header=request['headers'],
            body=request['body'],
            query=request['query']
        )
        response = usecase.execute(http_request.body)
    except HttpError as ex:
        return HttpResponse(status_code=ex.status_code, body=ex.message)

    return response
