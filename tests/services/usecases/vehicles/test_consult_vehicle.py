import pytest
from app.services.usecases.vehicles import ConsultVehicleByIdUsecase


@pytest.fixture
def uco() -> ConsultVehicleByIdUsecase:
    return ConsultVehicleByIdUsecase(_id=1)


@pytest.fixture
def params() -> dict:
    return {}


def test_create_vehicle(uco: ConsultVehicleByIdUsecase, params: dict):
    response = uco.execute(params)
    assert response.status_code == 200
