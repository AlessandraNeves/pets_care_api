from pydantic import BaseModel
from typing import Optional, List
from model.pet import Pet


class PetSchema(BaseModel):
    """Define como um novo pet a ser adicionado deve ser representado
    """
    name: str = "Senna"
    birthday: str = "02/05/2023"
    type: str = "dog"
    gender: str = "M"
    breed: Optional[str] = "Poodle"
    weight: Optional[float] = 12.210
    microchip: Optional[int] = 658732


class PetViewSchema(BaseModel):
    """ Define como um pet será retornado: pet.
    """
    id: int = 1
    name: str = "Senna"
    birthday: str = "2023-02-05"
    type: str = "Cão"
    gender: Optional[str] = "M"
    breed: Optional[str] = "Poodle"
    weight: Optional[float] = 13.4
    microchip: Optional[int] = 6548723


class PetFindByIdSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita com base no nome do pet e na identificação do usuário (user.id).
    """
    id: int = 1


class PetFindByNameSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do pet.
    """
    name: str = "Senna"


class PetDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    name: str


def view_pet(pet: Pet):
    """ Retorna uma representação do pet seguindo o schema definido em
        PetViewSchema.
    """
    return {
        "name": pet.name,
        "birthday": pet.birthday,
        "type": pet.type,
        "gender": pet.gender,
        "breed": pet.breed,
        "weight": pet.weight,
        "microchip": pet.microchip
    }


def view_pets(pets: List[Pet]):
    """ Retorna uma representação do pet seguindo o schema definido em
        PetViewSchema.
    """
    result = []
    for pet in pets:
        result.append({
            "id": pet.id,
            "name": pet.name,
            "birthday": pet.birthday,
            "type": pet.type,
            "gender": pet.gender,
            "breed": pet.breed,
            "weight": pet.weight,
            "microchip": pet.microchip,
        })
    return {"pets": result}


class list_pets(BaseModel):
    """ Define como uma listagem de pets será retornada.
    """
    pets:List[PetViewSchema]

