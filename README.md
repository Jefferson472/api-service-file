# API Service File
## Descrição do Projeto
Projeto de API para upload de arquivos similar ao S3, permitindo upload, download de arquivos organizado por pastas para cada usuário. Desenvolvido como task de entrevista.

---

## Tasks
- [x] Testes automatizados
- [x] quaisquer barras no caminho devem ser tratadas como pastas
- [x] quando um arquivo é acessado, permitir download
- [x] quando uma pasta é acessada seu conteúdo deve ser listado
- [x] você deve poder deletar arquivos e caminhos órfãos
- [x] Se o mesmo arquivo for carregado duas vezes e sua conteúdo diferem, você deve armazenar o mais recente
- [x] somente arquivos txt, pdf, xml
- [x] documentar no readme ou especificação openAPI

## Bonus Tasks
- [ ] Tornar os uploads retomáveis;
- [ ] Faça com que o serviço trate corretamente as tentativas de upload do mesmo arquivo no
mesmo tempo (escolha um comportamento que você acha que faz sentido);
- [ ] Adicione alguns campos de metadados aos arquivos.


---

## Requirements
- Python 3.10
- Django 4.1
- Django Rest Framework 3.13
- Docker
- Docker compose v2.10.2

---

## Executando o Projeto
Para executar o projeto siga os passos abaixo:

1. Inicie o container com o comando:

```json
    docker compose up -d
```

2. Inicialize o banco de dados:

```json
    docker exec -it app bash -c "cd src && python manage.py makemigrations"
    docker exec -it app bash -c "cd src && python manage.py migrate"
```

3. Crie um usuário:

```json
    docker exec -it app bash -c "cd src && python manage.py createsuperuser"
```

4. A aplicação pode ser acessada no link: http://localhost:8000/api/

---

## Endpoints
### Autenticação
Os arquivos são separados por usuário, por é necessário uma autenticação. Utilize as credencial criada no passo 3 da seção , Executando o projeto. 

Obs.: Se estiver usando Postman, utilize `Basic Auth`

---
### Uploads
Permite o upload de arquivos para uma pasta `/username/home`. Caso exista um `path` na requisição, os arquivos serão salvos em `/username/home/path`. 

`api/upload/`

`ALLOW_METHODS = POST, PUT`

Extensões permitidas: `.pdf, .txt, .xml`
```json
{
    "file": file
    "path": 'your-path',
}
```

### Listando Arquivos
Retorna uma lista de arquivos cadastrados em formato json. Caso exista uma `path`, será lsitado somente os arquivos daquela pasta e subsequentes.

`api/files/`

`api/files/<path>`

`ALLOW_METHODS = GET`
```json
{
    "id": 1,
    "file_name": "file",
    "file": "http://127.0.0.1:8000/media/username/home/file",
    "path": "your-path",
    "created": "2022-10-02T19:43:25.376159-03:00",
    "updated": "2022-10-02T19:43:31.977652-03:00"
}
```
---
### Download de Arvquivos
Baixa o arquivo do caminho especificado

`api/files/<file>`

`ALLOW_METHODS = GET`

---

### Deletando Pastas e Arquivos
É possível deletar arquivos e pastas sem conteúdo:

Para deletar um único arquivo:

`api/file/<id>`

`ALLOW_METHODS = DELETE`

Para deletas uma pasta:

`api/path/<path>`

`ALLOW_METHODS = DELETE`

Obs.: Irá retornar um erro `400` caso a pastas não esteja vazia 

## Executando os Testes
Para rodar os testes execute o comando abaixo:

`python src/api/manage.py test`
