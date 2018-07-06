# PHX

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

* Set up a virtualenv:

  ```
  virtualenv env
  source env/bin/activate
  ```

* Install requirements:

  ```
  pip3 install -r requirements.txt
  ```

* Run database migrations:

  ```
  python3 manage.py migrate
  ```

* Create an admin superuser

  ```
  python3 manage.py createsuperuser
  ```

* Start server:

  ```
  python3 manage.py runserver
  ```

* Open [http://localhost:8000](http://localhost:8000) in a browser


## Development

### Components

CSS and JS has been built with a component-led focus.

### CSS

CSS is built with [PostCSS](https://postcss.org/).

CSS follows the [SuitCSS naming conventions](https://github.com/suitcss/suit/blob/master/doc/naming-conventions.md).

### JS

JS is built with [webpack](https://webpack.js.org/).


### Linting

Linting with [Stylelint](https://stylelint.io/) for CSS and [ESLint](https://eslint.org/) for JS along with [Prettier](https://prettier.io/) is set up on the git pre-commit hook.

### VS Code

To set up Prettier with VS Code to automatically format CSS/JS, add this to the workspace settings:

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

## Deployment

* Generate a build:

  ```
  npm run build
  ```