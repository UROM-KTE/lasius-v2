# Lasius project

## Development

### Init project

#### Prerequisites

    python version: 3.12
    docker
    docker-compose

#### Setting up environment variables

There are 2 environment variables in the project. One is for the docker,
the other one is for the Django application.

##### Docker configuration
The file must be `{project_root}/docker/.env`.

Example:

```
# Docker environment
COMPOSE_PROJECT_NAME=lasius
COMPOSE_FILE=docker-compose.yml

# Postgres administration for docker-compose.yml
PGDATA=/var/lib/postgresql/data/pgdata
POSTGRES_PASSWORD=postgres
```

##### Django configuration

The file must be `{project_root}/.env`.


#### Install development environment

1. Create and activate a python virtual environment  
    In the project's root folder run the following commands:  
    ```python3.12 -m venv .venv```  
    ```source .venv/bin/activate```

2. Install python packages from `requirements.txt`  
    ```pip install -r requirements.txt```

3. Start the postgresql development database  
    To make the database initialisation script runable, in the docker folder
    run the following:  
    ```chmod +x init-lasius-app-db.sh```  
    Then run this command:  
    ```docker-compose up -d```

4. Run the migrations
    Inside the `{project_root}/src` folder run the following command:
    ```python manage.py migrate```

5. Create django admin (optional)  
    Inside the `{project_root}/src` folder run the following command:
    ```python manage.py createsuperuser```  
    Add the prompted information.

6. Start the development server  
    Inside the `{project_root}/src` folder run the following command:  
    ```python manage.py runserver```  
    If you want to specify a port (default is 8000) for development server, run the following:  
    ```python manage.py runserver 8001```

### Model modification

When you modifiy a model, you have to migrate the database. To create a migration file,
inside the `{project_root}/src` folder run the following command:  
```python manage.py makemigrations```  

If it was successful, a file created in the app's migrations folder, starting with a 4-digit number.
Run the following, where `wxyz` is the 4-digit number of the migration file:  
```python manage.py sqlmigrate {{ your_app_name }} {{ wxyz }}```

### File storage

If an apps has models contain file or image field, you have to create a FileSystemStorage
inside the default storage.

### Testing
