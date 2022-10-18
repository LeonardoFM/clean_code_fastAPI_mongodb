
from app.domain.usecases.usecases import UseCase
from app.services.helpers.http import HttpResponse


class ListVehicleUsecase(UseCase):

    def execute(self, params: dict) -> HttpResponse:
        return HttpResponse(status_code=200, body={'message': 'lknakljns'})
