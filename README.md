# Backend-Challenge

A proposta do desafio é implementar um microserviço para um formulário de contato que, ao ser preenchido, envie um e-mail à empresa que está utilizando o microserviço e também envie uma cópia ao cliente para que ele acompanhe a resolução via e-mail.

## Índice

- [Visão Geral](#visão-geral)
- [Como Utilizar](#como-utilizar)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Rodar Localmente](#como-rodar-localmente)
- [Sobre a API](#sobre-a-api)
- [Estrutura do Projeto](#estrutura-do-projeto)

## Visão Geral

Este projeto consiste em um microserviço para gerenciar formulários de contato, garantindo que cada solicitação seja enviada tanto para a empresa quanto para o cliente. O serviço é projetado para ser fácil de integrar e escalável.

## Como Utilizar

Caso você queira apenas visualizar o resultado como usuário final, acesse [este link](http://18.231.47.85) (Talvez esse link não esteja disponível no futuro).

## Tecnologias Utilizadas

- **Backend:** Python, FlaskAPI
- **Frontend:** HTML5
- **Outras:** Docker, Nginx

## Como Rodar Localmente

Como rodar o FrontEnd e o Backend separadamente

### Requisitos

- Docker

### Passos

1. Clone o repositório:
    ```sh
    git clone https://github.com/NicolasPires777/backend-challenge.git
    cd backend-challenge
    ```

2. Faça o build da imagem e rode o container do backend:
    ```sh
    cd backend
    docker build -t backend .
    docker run -p 5000:5000 backend
    ```

3. Em outro terminal, faça o build da imagem e rode o container do frontend:
    ```sh
    cd front
    docker build -t frontend .
    docker run -p 80:80 frontend
    ```

4. Com os dois conteiners rodando nas portas especificas acima, acesse [localhost](http://localhost:80)
   Obs: O Captcha funciona apenas em http://localhost:80, http://127.0.0.1:80 não possui chave válida

## Sobre a API

Caso você deseja visualizar apenas a API, o arquivo "OpenAPI.yaml" tem as informações sobre o que a API espera receber e como ela deve responder, você pode também copiar todo conteúdo desse arquivo e colar em https://editor.swagger.io/ para melhor visualização

## Estrutura do Projeto

```plaintext
backend-challenge/
├── backend/
│   ├── app/
│   |   ├── __init__.py
│   |   ├── controller.py
│   |   ├── routes.py
│   |   ├── service.py
│   ├── run.py
│   ├── OpenAPI.yaml
│   └── dockerfile
├── front/
│   ├── assets/
│   ├── index.html
│   ├── styles.css
│   ├── scripts.js
│   ├── docker-compose.yml
│   └── dockerfile
└── README.md


