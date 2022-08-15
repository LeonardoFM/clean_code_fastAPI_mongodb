from app.domain.usecases import UseCase


class CreateVehicle(UseCase):
    def execute(self, params: dict):
        return {'teste': 'teste'}
