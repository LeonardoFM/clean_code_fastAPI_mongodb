from http import HTTPStatus

from fastapi import APIRouter, Header, Response, Path

from app.main.adapters import fast_api_adapter
from app.domain.params import VehiclesParams
from app.main.factories import create_vehicle_factory, list_vehicles_factory, consult_vehicle_by_id_factory


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


@vehicles_router.get(
    '/list',
    responses={
        HTTPStatus.OK.value: {
            'description': 'Lista Veículo incluído na base do transporte'
        },
    },
    summary='Efetua a listagem do veículo no banco de dados',
    description='Lista um tipo de veículo no transporte',
    status_code=HTTPStatus.OK.value,
)
def list_vehicles(
    response: Response,
):
    http_request = {
        'headers': None,
        'query': None,
        'body': {}
    }
    result = fast_api_adapter(http_request, list_vehicle_by_id_factory())
    response.status_code = result.status_code
    if result.body:
        return result.body
    return response


@vehicles_router.get(
    '/list/{_id}',
    responses={
        HTTPStatus.OK.value: {
            'description': 'Lista Veículo incluído na base do transporte'
        },
    },
    summary='Efetua a listagem do veículo no banco de dados',
    description='Lista um tipo de veículo no transporte',
    status_code=HTTPStatus.OK.value,
)
def list_vehicle(
    response: Response,
    _id: str = Path(...)
):
    http_request = {
        'headers': None,
        'query': None,
        'body': {}
    }
    result = fast_api_adapter(http_request, consult_vehicle_by_id_factory(_id))
    response.status_code = result.status_code
    if result.body:
        return result.body
    return response
