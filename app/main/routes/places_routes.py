from http import HTTPStatus

from fastapi import APIRouter, Header, Response, Path

from app.main.adapters import fast_api_adapter
from app.domain.params import VehiclesParams
from app.main.factories import (create_place_factory,
                                list_places_factory,
                                consult_place_factory,
                                update_place_factory)


vehicles_router = APIRouter(
    prefix='/places',
    tags=['Places']
)


@vehicles_router.post(
    '/create',
    responses={
        HTTPStatus.OK.value: {
            'description': 'Localização incluída na base do transporte'
        },
    },
    summary='Efetua o cadastro do localização no banco de dados',
    description='Cria um tipo de localização no transporte',
    status_code=HTTPStatus.OK.value,
)
def create_place(
    body: VehiclesParams,
    response: Response
):
    http_request = {
        'body': body,
        'headers': None,
        'query': None
    }
    result = fast_api_adapter(http_request, create_place_factory())
    response.status_code = result.status_code
    if result.body:
        return result.body
    return response


@vehicles_router.get(
    '/list',
    responses={
        HTTPStatus.OK.value: {
            'description': 'Lista localizações incluído na base do transporte'
        },
    },
    summary='Efetua a listagem de localizações no banco de dados',
    description='Lista um tipo de localizações no transporte',
    status_code=HTTPStatus.OK.value,
)
def list_places(
    response: Response,
):
    http_request = {
        'headers': None,
        'query': None,
        'body': {}
    }
    result = fast_api_adapter(http_request, list_places_factory())
    response.status_code = result.status_code
    if result.body:
        return result.body
    return response


@vehicles_router.get(
    '/list/{_id}',
    responses={
        HTTPStatus.OK.value: {
            'description': 'Consulta localização incluído na base do transporte'
        },
    },
    summary='Efetua a listagem de localização no banco de dados',
    description='Lista um tipo de localização no transporte',
    status_code=HTTPStatus.OK.value,
)
def list_place(
    response: Response,
    _id: str = Path(...)
):
    http_request = {
        'headers': None,
        'query': None,
        'body': {}
    }
    result = fast_api_adapter(http_request, consult_place_factory(_id))
    response.status_code = result.status_code
    if result.body:
        return result.body
    return response


@vehicles_router.get(
    '/update/{_id}',
    responses={
        HTTPStatus.OK.value: {
            'description': 'Atualiza localização incluído na base do transporte'
        },
    },
    summary='Efetua a atualização de cadastro de um localidade',
    description='É possível atualizar localização de transporte',
    status_code=HTTPStatus.OK.value,
)
def update_place(
    response: Response,
    _id: str = Path(...)
):
    http_request = {
        'headers': None,
        'query': None,
        'body': {}
    }
    result = fast_api_adapter(http_request, update_place_factory(_id))
    response.status_code = result.status_code
    if result.body:
        return result.body
    return response
