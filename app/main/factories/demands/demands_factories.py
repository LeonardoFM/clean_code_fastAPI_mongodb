from app.domain.usecases import UseCase

from app.services.usecases import (ListDemandsUsecase,
                                   ConsultDemandUsecase,
                                   CreateDemandUsecase,
                                   UpdateDemandUsecase)


def create_demand_factory() -> UseCase:
    return CreateDemandUsecase()


def list_demands_factory() -> UseCase:
    return ListDemandsUsecase()


def consult_demand_factory(_id: str) -> UseCase:
    return ConsultDemandUsecase()


def update_demand_factory(_id: str):
    return UpdateDemandUsecase()
