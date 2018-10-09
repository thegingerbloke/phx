# PHX

A Django-based website.


## Requirements

* Python 3 (and pip)
* node (and npm)
* virtualenv


## Installation

Once you have cloned this repo, run through the following steps:


### Installation - frontend

* Install frontend dependencies:

  ```
  npm install
  ```

* Watch for frontend file changes during development:

  ```
  npm run watch
  ```


### Installation - backend

* Create a new config file - `phx/phx/settings/local.py` - and add the following (or see below for a more detailed example):

  ```
  from .base import *

  DEBUG = True
  ```

* Set up a virtualenv:

  ```
  virtualenv env
  source env/bin/activate
  ```

  Optionally, when setting up the virtualenv you can specify an exact path to the python 3 binary, for example:

  ```
  virtualenv env --python=/Users/pete/.pyenv/versions/3.6.5/bin/python
  ```

  The advantage of this is for the following commands you can replace `pip3` and `python3` with the more common `pip` and `python`.

* Install requirements:

  ```
  pip3 install -r requirements/local.txt
  ```

* Move from the root directory to the `phx` directory:

  ```
  cd phx
  ```

* Run database migrations:

  ```
  python3 manage.py migrate
  ```

* Create an admin superuser:

  ```
  python3 manage.py createsuperuser
  ```

* Start server:

  ```
  python3 manage.py runserver
  ```

  or

  ```
  django-admin runserver --pythonpath=. --settings=phx.settings.local
  ```

* Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in a browser

* To see the admin area, open [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) in a browser


### Optional site setup

* You can automate the site population with the following command:

  ```
  python3 manage.py loaddata fixtures results contact pages news home gallery
  ```

* Alternatively this can be done manually - from the admin area create a page for every top-level section of the site:

  - About
  - Fixtures
  - Results
  - Training
  - Events
  - Membership
  - Contact

* Add some news articles, fixtures, categories and results

* For the contact form, add some contacts and assign them to topics

* Create some users, some groups with permissions, and assign users to those groups


### Config

Example config files exist for `local`, `dev` and `production` environments. These are in the following directory:

```
phx/phx/settings/
```

To use them, duplicate the existing files (removing `.sample` from their filenames), and then fill in the relevant details within each file.



### Social media accounts

The site can post news articles and results to Twitter and Facebook. To do this, accounts/apps need to be set up for both social networks. The relevant access details for these accounts should then be added into the config files.


#### Twitter

* [Register a new app](https://developer.twitter.com/) with the relevant twitter account - take a note of the four different keys listed below, and make sure the app has read and write access. (Give it read and write access before creating your access tokens so they share this access, to check see [here](https://twitter.com/settings/applications))

#### Facebook

 - Follow: https://developers.facebook.com/docs/pages/getting-started
 - For the relevant page, find its page ID (from 'about' section)
 - [Register a new app](https://developers.facebook.com/apps/)
 - Note the new app id and app secret from `'settings' --> 'basic'`
 - Go to the [API explorer](https://developers.facebook.com/tools/explorer/)
 - Select `"Get Token" --> "Get User Access Token"`, tick `"manage_pages"` and `"publish_pages"`
 - Generate a [long-lived token](https://developers.facebook.com/docs/facebook-login/access-tokens/refreshing/#generate-long-lived-token)
 - From the API explorer, enter `GET /{page-id}?fields=access_token`
 - From the API explorer, test by entering `POST /{page-id}/feed?message={msg}` replacing `{msg}` with something.


### Cron

The site uses [Django-cron](http://django-cron.readthedocs.io/) to periodically post new content to the social media accounts above.

In order to set this up, the following `crontab` should be set up on the server:

```
* * * * * source env/bin/activate && python manage.py runcrons

```


## Development

All CSS/JS code should sit in the `/frontend` directory.

Anything in the `/frontend/static` directory will be served by the app


### Components

CSS and JS has been built with a component-led focus.

### CSS

CSS is built with [PostCSS](https://postcss.org/).

CSS follows the [SuitCSS naming conventions](https://github.com/suitcss/suit/blob/master/doc/naming-conventions.md).

### JS

JS is built with [webpack](https://webpack.js.org/).


### Linting

Linting with [Stylelint](https://stylelint.io/) for CSS and [ESLint](https://eslint.org/) for JS, along with [Prettier](https://prettier.io/) on the git pre-commit hook.

### VS Code

To set up Prettier with VS Code to automatically format CSS/JS on save, add this to the workspace settings:

```
{
  // Prettier - set default
  "editor.formatOnSave": false,

  // Prettier - enable per-language
  "[javascript]": {
    "editor.formatOnSave": true
  },
  "[css]": {
    "editor.formatOnSave": true
  },

  // ESlint - custom config
  "eslint.options": {
    "configFile": "eslint.config.js"
  }
}
```

## Linting and Testing

To lint the frontend code:

```
npm run lint
```

To lint the backend code:

```
flake8
```

To test the backend code:

```
pytest
```

## CI

A config for Circle CI has been set up to run linting and testing on every push to Github


## Deployment

* Set up a server, e.g. on [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04)

    - Note: When creating `gunicorn.service` file, the following needs to be added:

      ```
      --env DJANGO_SETTINGS_MODULE=phx.settings.dev/production
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
