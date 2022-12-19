from http import HTTPStatus

from app.domain.usecases.usecases import UseCase
from app.services.helpers.http import HttpResponse


class ConsultVehicleByIdUsecase(UseCase):

    def __init__(self, _id):
        self._id = _id

    def execute(self, params: dict) -> HttpResponse:
        return HttpResponse(HTTPStatus.OK, {})
