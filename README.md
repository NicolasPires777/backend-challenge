# Backend-Challenge

A proposta do desafio é implementar um microserviço para um formulário de contato que, ao ser preenchido, envie um e-mail à empresa que está utilizando o microserviço e também envie uma cópia ao cliente para que ele acompanhe a resolução via e-mail.

## Índice

- [Visão Geral](#visão-geral)
- [Como Utilizar](#como-utilizar)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Rodar Localmente](#como-rodar-localmente)
- [Estrutura do Projeto](#estrutura-do-projeto)

## Visão Geral

Este projeto consiste em um microserviço para gerenciar formulários de contato, garantindo que cada solicitação seja enviada tanto para a empresa quanto para o cliente. O serviço é projetado para ser fácil de integrar e escalável.

## Como Utilizar

Caso você queira apenas visualizar o resultado como usuário final, acesse [este link](http://18.231.160.177) (Talvez esse link não esteja disponível no futuro).

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

4. Com os dois conteiners rodando nas portas especificas acima, acesse [localhost](http://127.0.0.1:80)

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
└── README.md```
