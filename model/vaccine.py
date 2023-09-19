from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from  model import Base


class Vaccine(Base):
    __tablename__ = 'vaccine'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    type = Column(String(20), nullable=False)
    first_dose =Column(Integer, nullable=False)
    second_dose =Column(Integer)
    third_dose =Column(Integer)
    booster_dose = Column(String(50))
    mandatory = Column(Integer, nullable=False) 

    def __init__(self, name:str, type:str, first_dose:int, second_dose:int, third_dose:int, booster_dose:str, mandatory:int):
        """
        Cria o cadastro de uma vacina (Vaccine) a ser administrada em um aminal (Pet)

        Arguments:
            name: nome que identifica a vacina.
            type: tipo de animal a qual a vacina se destina
            first_dose: quantidade de dias, a contar do nascimento, para cálculo da data da primeira dose
            second_dose: quantidade de dias, a contar da primeira dose, para cálculo da data da segunda dose
            third_dose: quantidade de dias, a contar da segunda dose, para cálculo da data da terceira dose
            booster_dose: tipo indicativo da forma como calcular a data da dose de reforço
            mandatory: indicativo de obrigatoriedade (0 = não obrigatório; 1 = obrigatório)

        """
        self.name = name
        self.type = type
        self.first_dose = first_dose
        self.second_dose = second_dose
        self.third_dose = third_dose
        self.booster_dose = booster_dose
        self.mandatory = mandatory



