from http import HTTPStatus

from fastapi import APIRouter, Header, Response

from app.main.adapters import fast_api_adapter
from app.domain.params import VehiclesParams
from app.main.factories import create_vehicle_factory


vehicles_router = APIRouter(
    prefix='/vehicles',
    tags=['Vehicles']
)


@vehicles_router.post(
    '/create',
    responses={
        HTTPStatus.OK.value: {
            'description': 'Veículo incluído na base do transporte'
        },
    },
    summary='Efetua o cadastro do veículo no banco de dados',
    description='Cria um tipo de veículo no transporte',
    status_code=HTTPStatus.OK.value,
)
def create_vehicle(
    body: VehiclesParams,
    response: Response
):
    http_request = {
        'body': body,
        'headers': None,
        'query': None
    }
    result = fast_api_adapter(http_request, create_vehicle_factory())
    response.status_code = result.status_code
    if result.body:
        return result.body
    return response
