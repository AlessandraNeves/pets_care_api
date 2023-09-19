from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime

from  model import Base


class Dose(Base):
    __tablename__ = 'dose'

    id = Column(Integer, primary_key=True)
    pet_id = Column(Integer, nullable=False)
    vaccine_id = Column(Integer, nullable=False)
    expected_date = Column(DateTime, nullable=False)
    completion_date = Column(DateTime)
    

    # Definição do relacionamento entre a dose e pet.
    # Aqui está sendo definido a coluna 'pet_id' que vai guardar
    # a referencia do 'pet.id', a chave estrangeira que relaciona
    # uma dose a um pet.
    pet_id = Column(Integer, ForeignKey("pet.id"), nullable=False)

    # Definição do relacionamento entre a dose e a vaccine.
    # Aqui está sendo definido a coluna 'vaccine_id' que vai guardar
    # a referencia da 'vaccine.id', a chave estrangeira que relaciona
    # uma dose a uma vacina.
    vaccine_id = Column(Integer, ForeignKey("vaccine.id"), nullable=False)

    def __init__(self, pet_id:int, vaccine_id:int, expected_date:datetime, completion_date:datetime):
        """
        Cria o cadastro das doses (Dose) de vacinas (Vaccine) administradas em um Animal (Pet)

        Arguments:
            pet_id: identificação do animal
            vaccine_id:identificação da vacina
            expected_date: data esperada para administração da vacina
            completion_date: data da administração da vacina no animal
        """
        self.pet_id = pet_id
        self.vaccine_id = vaccine_id
        self.expected_date = expected_date
        self.completion_date = completion_date
