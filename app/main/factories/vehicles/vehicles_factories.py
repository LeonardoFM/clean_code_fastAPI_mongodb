
from app.domain.usecases import UseCase

from app.services.usecases import (ListVehicleUsecase,
                                   ConsultVehicleByIdUsecase,
                                   CreateVehicleUsecase)


def create_vehicle_factory() -> UseCase:
    return CreateVehicleUsecase()


def list_vehicles_factory() -> UseCase:
    return ListVehicleUsecase()


def consult_vehicle_by_id_factory(_id: str) -> UseCase:
    return ConsultVehicleByIdUsecase(_id)
