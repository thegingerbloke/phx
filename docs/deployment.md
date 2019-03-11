# PHX - Deployment

[&laquo; Back](../README.md)

How to deploy the app


## Deployment

* Set up a server, e.g. on [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04)

    - Note: When creating `gunicorn.service` file, the following needs to be added:

      ```
      --env DJANGO_SETTINGS_MODULE=phx.settings.dev (or .production)
      ```

* Check out this project

* Install requirements:

  ```
  pip install -r dev.txt (or production.txt)
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

* Manually create settings files: `/phx/phx/settings/dev.py` / `/phx/phx/settings/production.py` using the sample files in that directory

* Collect static assets:

  ```
  manage.py collectstatic  --settings=phx.settings.dev/prod
  ```

* Migrate DB:

  ```
  manage.py migrate  --settings=phx.settings.dev/prod
  ```

* Optional: manually (generate, upload and) load fixture data:

  ```
  manage.py loaddata fixtures results contact pages news home gallery
  ```

### Deployment - making updates:

 - Push to repo, wait for tests to complete
 - Log into server

    ```
    cd phx/
    source env/bin/activate
    git pull -p
    npm run build
    pip install -r requirements/production.txt
    cd phx/
    python manage.py migrate --settings=phx.settings.production
    python manage.py collectstatic --settings=phx.settings.production
    python manage.py loaddata fixtures results contact pages news home gallery --settings=phx.settings.production
    sudo systemctl restart gunicorn
    ```
