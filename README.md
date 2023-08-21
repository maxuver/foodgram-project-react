### Description
The "Foodgram" project is a "grocery assistant". On this service, authorized users can publish recipes, subscribe to publications of other users, add favorite recipes to the "Favorites" list, and before going to the store, download a summary list of products needed to prepare one or more selected dishes. Unauthorized users can view recipes and authors' pages.

### How to run a project on a production server:

Install docker and docker-compose on the server. Copy the docker-compose.yaml and default.conf files to the server:

```
scp docker-compose.yml <server_login>@<server_ip>:/home/<server_login>/docker-compose.yml
scp nginx.conf <server_login>@<server_ip>:/home/<server_login>/nginx.conf

```

Add the following data to Secrets on Github:

```
DB_ENGINE=django.db.backends.postgresql # specify that the project works with postgresql
DB_NAME=postgres # database name
POSTGRES_USER=postgres # login to connect to the database
POSTGRES_PASSWORD=postgres # password to connect to the database
DB_HOST=db # name of the database service (container)
DB_PORT=5432 # port for connecting to the database
DOCKER_PASSWORD= # DockerHub account password
DOCKER_USERNAME= # Username in DockerHub account
HOST= # remote server IP
USER= # Login on remote server
SSH_KEY= # SSH-key of the computer from which the connection to the remote server will be made
PASSPHRASE= #If a passphrase is used for ssh
TELEGRAM_TO= #Telegram user ID
TELEGRAM_TOKEN= #ID of the bot in Telegram

```

Run commands:

* git add .
* git commit -m "Commit"
* git push

This will start the workflow processes:

* checking the code for compliance with the PEP8 standard (using the flake8 package) and running pytest
* building and delivering a docker image for the web container on Docker Hub
* automatic project deployment to the production server
* sending a notification to Telegram that the deployment process has completed successfully

After the successful completion of the workflow processes on the production server, the following commands should be executed:

```
sudo docker-compose exec web python manage.py migrate

```


```
sudo docker-compose exec web python manage.py collectstatic --no-input
```

Then it will be necessary to create a superuser and load information about the ingredients into the database:

```
sudo docker-compose exec web python manage.py createsuperuser

```

```
sudo docker-compose exec web python manage.py load_data_csv --path <file_path> --model_name <model_name> --app_name <app_name>

```

### How to run a project locally in containers:

Clone the repository and change into it on the command line:

``` git@github.com:mariyabykova/foodgram-project-react.git ```
``` cd foodgram-project-react ```

Run docker-compose:

```
docker-compose-up

```

After the containers are built, run the migrations:

```
docker-compose exec web python manage.py migrate

```

Create superuser:

```
docker-compose exec web python manage.py createsuperuser

```

Download static:

```
docker-compose exec web python manage.py collectstatic --no-input

```

Check the work of the project on the link:

```
http://localhost/
```


### How to run the project locally:

Clone the repository and change into it on the command line:

``` git@github.com:mariyabykova/foodgram-project-react.git ```
``` cd foodgram-project-react ```

Create and activate virtual environment:

``` python -m venv venv ```

* If you have Linux/macOS:
     ``` source venv/scripts/activate ```

* If you have Windows:
     ``` source venv/Scripts/activate ```
    
``` python -m pip install --upgrade pip ```

Install dependencies from requirements file:

``` pip install -r requirements.txt ```

Run migrations:

``` python manage.py migrate ```

Run project:

``` python manage.py runserver ```

### The following endpoints are available in the API:

* ```/api/users/``` Get-request - getting a list of users. POST request - registration of a new user. Available without a token.

* ```/api/users/{id}``` GET request - personal page of the user with the specified id (available without a token).

* ```/api/users/me/``` GET request is the page of the current user. PATCH request - editing your own page. Available to authorized users.

* ```/api/users/set_password``` POST request - change your own password. Available to authorized users.

* ```/api/auth/token/login/``` POST request - getting a token. Used for authorization by email and password, in order to further use the token for requests.

* ```/api/auth/token/logout/``` POST request - delete token.

* ```/api/tags/``` GET request - getting a list of all tags. Available without a token.

* ```/api/tags/{id}``` GET request - getting information about the tag and its id. Available without a token.

* ```/api/ingredients/``` GET request - get a list of all ingredients. Added search by partial occurrence at the beginning of the ingredient name. Available without a token.

Author of the project | My website
------------- | -------------
[maxuver](https://github.com/maxuver) | [maximpatsyuk.com](https://maximpatsyuk.com)