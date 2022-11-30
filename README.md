# Mycontacts

O projeto consiste em uma agenda de contatos web que permite 
a criação de contas de usuários e, após criada uma conta, criar, editar e excluir contatos.
O projeto utiliza a linguagem de programção Python juntamente
com o framework Django e banco de dados SQLite(integrado ao Django).



## Funcionalidades

- Permite criar diferentes contas de usuários;
- Uso de imagens para o perfil dos contatos;
- Pesquisa de contatos;
- Adição, edição e exclusão de contatos.


## Instalação

**Observação:**
O banco de dados utilizado no projeto foi o SQLite, padrão do Django e integrado neste repositório, não sendo
necessário scripts para criação de banco de dados para executar o projeto.

**Usuário administrador do Django:** teste  
**Senha do usuário administrador do Django:** teste

Usuário de conta já cadastrado no sistema e com alguns contatos registrados para testes:  
**Usuário:** juan  
**Senha:** 123456teste

Baixe ou clone este repositório:

```bash
 git clone https://github.com/jcmjuan/mycontacts.git
```
Acesse a pasta do projeto usando o terminal ou terminal 
integrado do Visual Studio Code e ative virtual enviroment:
```bash
 .\env\scripts\activate.ps1
``` 
Instale o Django e demais dependências do projeto:
```bash
pip install django django-tinymce4-lite pillow pi
```
Para rodar o projeto, digite no terminal:
```bash
python manage.py runserver
```



![Captura de Tela (19)](https://user-images.githubusercontent.com/82816159/204632529-94e88d83-2617-4344-982f-fc57b59309b7.png)

![Captura de Tela (20)](https://user-images.githubusercontent.com/82816159/204632600-f3aa682d-ccc2-466f-bff3-4fab2219f242.png)

![Captura de Tela (21)](https://user-images.githubusercontent.com/82816159/204632631-8335ebfb-c0ed-40d5-9dfa-3bba3108e0fd.png)

![Captura de Tela (22)](https://user-images.githubusercontent.com/82816159/204632725-29ffd2f5-d50d-45bd-8dbb-07af6ab3ed09.png)
