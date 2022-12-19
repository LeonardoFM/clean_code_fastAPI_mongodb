from app.domain.usecases import UseCase

from app.services.usecases import (ListPlacesUsecase,
                                   ConsultPlaceUsecase,
                                   CreatePlaceUsecase,
                                   UpdatePlaceUsecase)


def create_place_factory() -> UseCase:
    return CreatePlaceUsecase()


def list_places_factory() -> UseCase:
    return ListPlacesUsecase()


def consult_place_factory(_id: str) -> UseCase:
    return ConsultPlaceUsecase()


def update_place_factory(_id: str):
    return UpdatePlaceUsecase()
