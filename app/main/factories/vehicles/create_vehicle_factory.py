from typing import Optional

from app.domain.usecases import UseCase
from app.services.usecases import CreateVehicle


def create_vehicle_factory() -> UseCase:

    return CreateVehicle()
