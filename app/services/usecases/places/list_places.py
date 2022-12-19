from http import HTTPStatus


from app.domain.usecases import UseCase
from app.services.helpers.http import HttpError, HttpResponse


class ListPlacesUsecase(UseCase):
    def execute(self, params: dict) -> HttpResponse:
        return HttpResponse(HTTPStatus.OK, {'task_code': params})
