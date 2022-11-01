import pytest
from app.services.usecases.vehicles.create_vehicle import CreateVehicleUsecase


@pytest.fixture
def uco() -> CreateVehicleUsecase:
    return CreateVehicleUsecase()


@pytest.fixture
def params() -> dict:
    return {}


def test_create_vehicle(uco: CreateVehicleUsecase, params: dict):
    response = uco.execute(params)
    assert response.status_code == 201
