from http import HTTPStatus

from app.domain.usecases import UseCase
from app.services.helpers.http import HttpError, HttpResponse


class UpdateDemandUsecase(UseCase):
    def execute(self, params: dict) -> HttpResponse:
        return HttpResponse(HTTPStatus.NO_CONTENT)
