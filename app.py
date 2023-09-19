from flask_openapi3 import OpenAPI, Info, Tag
from flask import Flask, request, render_template, redirect
from flask_cors import CORS
from urllib.parse import unquote
from unidecode import unidecode

from sqlalchemy.exc import IntegrityError

from model import Session, Pet
from logger import logger
from schemas import *

info = Info(title="API Pet-Vaccines", version="1.0.0") 
app = OpenAPI(__name__, info=info)

CORS(app)
#cors = CORS(app, resources={r"/pets": {"origins": "*"}})


#definindo Tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
user_tag = Tag(name="Usuário", description="Adição de um usuário à base")
pet_tag = Tag(name="Pet", description="Adição, consulta e exclusão de animal(pet) à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a visualização da documentação da API
    """
    return redirect('/openapi')
    

#Rotas de Pet
# @app.route('/pet', methods=['POST'])
@app.post('/pet', tags=[pet_tag],
          responses={"200": PetViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_pet(form: PetViewSchema):
    """Adiciona um novo Pet à base de dados

    Retorna uma representação dos pet.
    """
    pet = Pet(
        name=form.name,
        birthday=form.birthday,
        type=form.type,
        gender=form.gender,
        breed=form.breed,
        weight=form.weight,
        microchip=form.microchip
    )
    logger.debug(f"Adicionando pet de nome: '{pet.name}'")
    try:
        # criando conexão com a base
        session = Session()
        #adicionando pet
        session.add(pet)
        #efetivando a adição do pet
        session.commit()
        logger.debug(f"Adicionado pet de nome: '{pet.name}'")
        return view_pet(pet), 200
    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Pet com nome já existente :/"
        logger.warning(f"Erro ao adicionar pet '{pet.nome}', {error_msg}")
        return {"mesage": error_msg}, 409
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar o novo pet :/"
        logger.warning(f"Erro ao adicionar pet '{pet.nome}', {error_msg}")
        
    
# @app.route('/pet/<id>', methods=['GET'])
@app.get('/pets', tags=[pet_tag],
          responses={"200": PetViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def get_pets():
    """Faz a busca por todos os Pets cadastrados

    Retorna uma representação da listagem de pets.
    """
    logger.debug(f"Coletando pets ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    pets = session.query(Pet).all()

    if not pets:
        # se não há pets cadastrados
        return {"pets": []}, 200
    else:
        logger.debug(f"%d pets econtrados" % len(pets))
        # retorna a representação de pet
        print(pets)
        return view_pets(pets), 200


@app.get('/pet', tags=[pet_tag],
         responses={"200": PetViewSchema, "404": ErrorSchema})
def get_pet(query: PetFindByIdSchema):
    """Faz a busca por um pet a partir do id do pet

    Retorna uma representação dos pets.
    """
    pet_id = query.id
    logger.debug(f"Coletando dados sobre pet #{pet_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    pet = session.query(Pet).filter(Pet.id == pet_id).first()

    if not pet:
        # se o pet não foi encontrado
        error_msg = "Pet não encontrado na base :/"
        logger.warning(f"Erro ao buscar pet '{pet_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Pet econtrado: '{pet.name}'")
        # retorna a representação de pet
        return view_pet(pet), 200
    

@app.delete('/pet', tags=[pet_tag],
            responses={"200": PetDelSchema, "404": ErrorSchema})
def del_pet(query: PetFindByNameSchema):
    """Deleta um pet a partir do nome de pet informado

    Retorna uma mensagem de confirmação da remoção.
    """
    pet_name = unquote(unquote(query.name))
    print(pet_name)
    logger.debug(f"Deletando dados sobre pet #{pet_name}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Pet).filter(Pet.name == pet_name).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado pet #{pet_name}")
        return {"mesage": "Pet removido", "id": pet_name}
    else:
        # se o pet não foi encontrado
        error_msg = "pet não encontrado na base :/"
        logger.warning(f"Erro ao deletar pet #'{pet_name}', {error_msg}")
        return {"mesage": error_msg}, 404



    