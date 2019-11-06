# PHX - Deployment

[&laquo; Back](../README.md)

How to deploy the app


## Deployment

* Set up a server, e.g. using the [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04) instructions.

    - Note: When creating `gunicorn.service` file, the following needs to be added:

      ```
      --env DJANGO_SETTINGS_MODULE=phx.settings.production
      ```

* Check out this project

* Install requirements:

  ```
  pip install -r production.txt
  ```
  or
  ```
  pip-sync production.txt
  ```


* Install [nodejs and npm](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-18-04)

* Install front-end dependencies:

  ```
  npm install
  ```

* Run frontend build:

  ```
  npm run build
  ```

* Optional: manually upload any existing media files, into `/phx/media`

* Manually create an `.env` file in the root, using the sample `.env.production.example` file

* Collect static assets:

  ```
  manage.py collectstatic  --settings=phx.settings.production
  ```

* Migrate DB:

  ```
  manage.py migrate  --settings=phx.settings.production
  ```

* Optional: manually (generate, upload and) load fixture data:

  ```
  manage.py loaddata fixtures results contact pages news home gallery --settings=phx.settings.production
  ```

### Deployment - making updates:

 - Push to repo, wait for tests to complete
 - Log into server

    ```
    # update code
    cd phx/
    source env/bin/activate
    git pull -p

    # front-end dependencies
    npm install
    npm run build

    # backend dependencies
    pip install -r requirements/production.txt  # or pip-sync production.txt

    # update content
    cd phx/
    python manage.py migrate --settings=phx.settings.production
    python manage.py collectstatic --settings=phx.settings.production

    # if loading data
    # python manage.py loaddata fixtures results contact pages news home gallery --settings=phx.settings.production

    # restart server
    sudo systemctl restart gunicorn
    sudo systemctl restart nginx
    ```
