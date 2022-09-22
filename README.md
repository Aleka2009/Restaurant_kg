PROJECT'S NAME: Restaurant_kg

CLONING PROJECT

for HTTPS:

https://github.com/Aleka2009/Restaurant_kg.git

for SSH key:

git@github.com:Aleka2009/Restaurant_kg.git

NEXT STEPS:

1.Install venv in project:

python3 -m venv venv 

2.Start virtualenv:

source venv/bin/activate

3.Installing all requirements:

pip install -r requirements.txt

TO START PROJECT:

1)sudo su (+ your password)

2)docker-compose up --build(to building docker and run server)

3)In another terminal:  docker-compose exec web python manage.py migrate --noinput

4)go to your browser and write in the search bar: 127.0.0.1:8000 or localhost:8000

IF YOU NEED TO GO IN DJANGO ADMIN PANEL AND YOU NEED TO CREATE SUPERUSER(ADMIN): 
(127.0.0.1:8000/admin/) or (localhost:8000)

1.In terminal:

docker ps -a

YOU MUST GET A NAME restaurant_kg_web_1

NEXT: docker exec -it restaurant_kg_web_1 sh

AND WRITE THIS FOR CREATING SUPERUSER(ADMIN):

python manage.py createsuperuser

ANYTHING URLS YOU HAVE IN DIR "restaurant", FILE "urls.py"

TESTS: DIR "rest", FILE "tests.py"

NEED TO ADD ENV VARS:

SECRET_KEY

DEBUG

DATABASE_ENGINE

DATABASE_NAME

DATABASE_USER

DATABASE_PASSWORD

DATABASE_HOST

DATABASE_PORT