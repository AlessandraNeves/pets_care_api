# My Pet Care - Gestão de cuidados do Pet

O sistema My Pet Care ajudará os tutores de animais a manter o protocolo de vacinas e medicamentos em dia prevenindo doenças que podem surgir em qualquer fase da vida do animal. 


## Ambiente Virtual  

É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Para criar:
> **python -m venv venv**


Para ativar o ambiente virtual:
> **.\venv\scripts\activate**

Para desativar o ambiente virtual:
> .\venv\scripts\deactivate


## Como executar
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

Para instalar as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

>**(venv)$ pip install -r requirements.txt**


Para definir o ambiente de execução:

>set FLASK_ENV=development 

ou

>set FLASK_ENV=production


Para executar a API  basta executar (ambiente virtual ativado):

>(venv)$ flask run 

ou (para reload após salvar)

>(venv)$ flask run --reload


Verificação de execução da API:
```
