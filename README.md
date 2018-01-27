# ProcessoIclinic

API REST em Django referente ao processo seletivo para desenvolvedor backend Iclinic.

## Começando

Inicialmente, instalar os pré-requisitos e executar alguns comando django.

### Pré-requisitos

É necessário instalar as seguintes dependências:

* Django==1.11.9
* django-rest-swagger==2.1.2
* djangorestframework==3.7.7


### Instalando

Para instanciar o banco de dados, executar os comandos:

```
python manage.py makemigrations
python manage.py migrate
```

Para criar um superusuário (não obrigatório, pois não foi tratado questões de autenticação):

```
python manage.py createsuperuser
```

Para executar o servidor:

```
python manage.py runserver
```

### Rotas

* localhost:8000/: página inicial e documentação;
** admin/: administração;
** agendamentos/: lista de agendamentos (GET) e cadastro de novo agendamento (POST); 

** agendamentos/(?P<pk>[0-9]+)/: detalhe de agendamento (GET), atualização de agendamento (update) e exclusão de agendamento (DELETE).

## Executando os testes

Para a execução dos testes, executar o seguinte comando (estando na pasta do manage.py)

```
  python manage.py test
```

Os testes se encontram no arquivo agendamento/tests.py.

## Desenvolvimento

Algumas questões de formatação não foram implementadas para ficarem mais parecidas com o formato do banco de dados, deixando essa questão para o desenvolvimento frontEnd.


## Construído com

* [Django](https://www.djangoproject.com/) - Framework web usado.
* [Django Rest Framework](http://www.django-rest-framework.org/) - Framework para API REST.
* [Swagger](https://marcgibbons.com/django-rest-swagger/) - Usado para geração de documentação.
