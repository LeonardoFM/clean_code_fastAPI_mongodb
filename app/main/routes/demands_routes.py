from http import HTTPStatus

from fastapi import APIRouter, Header, Response, Path

from app.main.adapters import fast_api_adapter
from app.domain.params import VehiclesParams
from app.main.factories import (create_demand_factory,
                                list_demands_factory,
                                consult_demand_factory,
                                update_demand_factory)


vehicles_router = APIRouter(
    prefix='/demands',
    tags=['Demands']
)


@vehicles_router.post(
    '/create',
    responses={
        HTTPStatus.OK.value: {
            'description': 'Demanda incluída na base do transporte'
        },
    },
    summary='Efetua o cadastro da demanda no banco de dados',
    description='Cria um tipo de demanda no transporte',
    status_code=HTTPStatus.OK.value,
)
def create_demand(
    body: VehiclesParams,
    response: Response
):
    http_request = {
        'body': body,
        'headers': None,
        'query': None
    }
    result = fast_api_adapter(http_request, create_demand_factory())
    response.status_code = result.status_code
    if result.body:
        return result.body
    return response


@vehicles_router.get(
    '/list',
    responses={
        HTTPStatus.OK.value: {
            'description': 'Lista demandas incluído na base do transporte'
        },
    },
    summary='Efetua a listagem de demandas no banco de dados',
    description='Lista um tipo de demandas no transporte',
    status_code=HTTPStatus.OK.value,
)
def list_demands(
    response: Response,
):
    http_request = {
        'headers': None,
        'query': None,
        'body': {}
    }
    result = fast_api_adapter(http_request, list_demands_factory())
    response.status_code = result.status_code
    if result.body:
        return result.body
    return response


@vehicles_router.get(
    '/list/{_id}',
    responses={
        HTTPStatus.OK.value: {
            'description': 'Consulta demanda incluído na base do transporte'
        },
    },
    summary='Efetua a listagem de demanda no banco de dados',
    description='Lista um tipo de demanda no transporte',
    status_code=HTTPStatus.OK.value,
)
def list_demand(
    response: Response,
    _id: str = Path(...)
):
    http_request = {
        'headers': None,
        'query': None,
        'body': {}
    }
    result = fast_api_adapter(http_request, consult_demand_factory(_id))
    response.status_code = result.status_code
    if result.body:
        return result.body
    return response


@vehicles_router.get(
    '/update/{_id}',
    responses={
        HTTPStatus.OK.value: {
            'description': 'Atualiza demanda incluído na base do transporte'
        },
    },
    summary='Efetua a atualização de cadastro de uma demanda',
    description='É possível atualizar demanda de transporte',
    status_code=HTTPStatus.OK.value,
)
def update_demand(
    response: Response,
    _id: str = Path(...)
):
    http_request = {
        'headers': None,
        'query': None,
        'body': {}
    }
    result = fast_api_adapter(http_request, update_demand_factory(_id))
    response.status_code = result.status_code
    if result.body:
        return result.body
    return response
