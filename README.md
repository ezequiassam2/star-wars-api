# Star Wars API

This is a CRUD API for managing planets and films using Flask, MongoDB, and Clean Architecture.

## Getting Started

### Prerequisites

#### Using Docker

- Docker
- Docker Compose

#### Without Docker

- Python 3.8+
- MongoDB

### Installation

#### Using Docker

1. Clone the repository:
    ```bash
    git clone https://github.com/ezequiassam2/star-wars-api.git
    cd star-wars-api
    ```

2. Build and start the Docker containers:
    ```bash
    docker-compose up --build
    ```

#### Without Docker

1. Clone the repository:
    ```bash
    git clone https://github.com/ezequiassam2/star-wars-api.git
    cd star-wars-api
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Update the MongoDB URI in `config_local.py` if necessary:
    ```bash
    MONGO_URI = "mongodb://localhost:27017/star_wars_api"
    ```

### Running the Application

#### Using Docker

The API will be available at `http://127.0.0.1:5000`.

#### Without Docker

1. Start the Flask application:
    ```bash
    flask run
    ```

2. The API will be available at `http://127.0.0.1:5000`.

### Running Tests

#### Using Docker

1. To run the tests, use:
    ```bash
    docker-compose run web pytest
    ```

#### Without Docker

1. To run the tests, use:
    ```bash
    pytest
    ```

## API Endpoints

### Planets

- **POST** `/planets` - Add a new planet
- **GET** `/planets` - Get all planets
- **GET** `/planets/{id}` - Get a planet by ID
- **PUT** `/planets/{id}` - Update a planet by ID
- **DELETE** `/planets/{id}` - Delete a planet by ID

### Films

- **POST** `/films` - Add a new film
- **GET** `/films` - Get all films
- **GET** `/films/{id}` - Get a film by ID
- **PUT** `/films/{id}` - Update a film by ID
- **DELETE** `/films/{id}` - Delete a film by ID
