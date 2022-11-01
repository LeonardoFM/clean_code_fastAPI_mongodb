import pytest
from app.services.usecases.vehicles import ListVehicleUsecase


@pytest.fixture
def uco() -> ListVehicleUsecase:
    return ListVehicleUsecase()


@pytest.fixture
def params() -> dict:
    return {}


def test_create_vehicle(uco: ListVehicleUsecase, params: dict):
    response = uco.execute(params)
    assert response.status_code == 200
