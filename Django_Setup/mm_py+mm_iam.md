 This is intended to extend docker-compose-base.yml for use with the interactive dev
 environment. (See <https://docs.docker.com/compose/extends/multiple-compose-files>.)
 E.G.:

   * ``docker compose --file docker-compose-base.yml --file docker-compose-dev.yml up
     --build --detach``
   * ``docker compose --file docker-compose-base.yml --file docker-compose-dev.yml logs
     --follow``
   * ``docker compose --file docker-compose-base.yml --file docker-compose-dev.yml down
     --remove-orphans --timeout 4 --volumes``

 The run-docker-compose-dev.sh helper script provides a shorthand. The above is
 respectively equivalent to:

   * ``./helpers/run-docker-compose-dev.sh up --build --detach``
   * ``./helpers/run-docker-compose-dev.sh logs --follow``
   * ``./helpers/run-docker-compose-dev.sh down --remove-orphans --timeout 4 --volumes``


## build container and see log (remember the timeout 5 for finding the AWS tokens they are not errors just waiting for them to load)
docker compose up --build --detach
docker compose logs --follow

## close containers
docker compose down --remove-orphans --timeout 4

## this is for COMPLETE teardown (Probably don't need this unless changing data model!)
docker compose down --remove-orphans --timeout 4 --volumes

## commit checks
pre-commit run --all-files

## making migrations
./iam/manage.sh makemigrations
./iam/manage.sh migrate

## How add Faux Data for Testing ?


## JWT Testing?

<!-- ./iam/manage.sh loaddata ./iam/initial_data.json

DJANGO_CONFIGURATION=DevRuntimeConfiguration ./iam/manage.sh migrate

PYTHONPATH="${HOME}/mm/oz/py" python ./iam/manage.py makemigrations
AWS_ENDPOINT_URL= ./iam/manage.sh makemigrations -->


( source ~/mm/oz/dev.env ; exec mysql -h mysql --user root "--password=${MYSQL_ROOT_PASSWORD}" )
SHOW DATABASES; USE mm_iam; SHOW TABLES;


# for Dev time configuratiosn
./iam/manage.sh migrate --configuration DevRuntimeConfiguration --settings mm.dev.iam_dev_settings


# for later production
./iam/manage.sh migrate --configuration ProdRuntimeConfiguration --settings mm.iam.settings
