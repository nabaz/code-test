# code-test

- To Run Django App Go to ./backend pip install -r requirements.txt from a virtual environment
- Create .env file in the root folder and set these values:

```
DB_NAME= 'dbname'
DB_USER='dbuser'
DB_PASSWORD='dbpassword'
DB_HOST='localhost'
DB_PORT='5432'

```

## then run migration
```
python manage.py migrate

```

## to run django test:

```
inisde api folder:

python manage.py test ./tests/

```
# To test Frontend:
## go to ./frontend
## run this
```
npm install
```
## then run this
```
ng serve

http://localhost:4200
```
