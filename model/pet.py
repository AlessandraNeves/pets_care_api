from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship

from  model import Base

class Pet(Base):
    __tablename__ = 'pet'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    birthday = Column(String(10), nullable=False)
    type = Column(String(10), nullable=False)
    gender = Column(String(1))
    breed = Column(String(30))
    weight = Column(Float)
    microchip = Column(Integer, unique=True)
    
    def __init__(self, name:str, birthday:str, type:str, gender:str, breed:str, weight:float, microchip:int):
        """
        Cria o cadastro de um animal (Pet)

        Arguments:
            name: nome do animal
            birthday: data de nascimento
            type: tipo do animal (cão, gato, ...)
            gender: sexo do animal
            breed: raça do animal
            weight: peso do animal
            microchip: número do microchip implantado no animal
        """
        self.name = name
        self.birthday = birthday
        self.type = type
        self.gender = gender
        self.breed = breed
        self.weight = weight
        self.microchip = microchip
