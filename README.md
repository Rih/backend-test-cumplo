# backend-cloud-test

 A nice map for inaturalist observations

# Stack & Technologies
### Backend
* Docker & docker-compose
* Python 3.7
* Django 2.2
* PostgreSQL
* Redis
* Recaptcha v3


## Libraries & 3rd parties
* Django restframework & simplejwt
* Google Bigquery
* Google Bigquery
* Swagger
* Flake8

### Frontend
* Vue & Vuex
* Bulma
* Sass
* Recaptcha
* [Leaflet](https://vue2-leaflet.netlify.app/) 

### Frontend Tools
* Prettier (alt + shift + f !!!)
* Typescript
* Jest

### API Rest doc
* localhost:8000/swagger

## App structure tree

```
|__ back
    |__ account
        |__ bl (bussiness logics)
            |__ recaptcha.py (validate function)
            |__ user_profile.py
            |__ utils.py (utility functions)
            |__ tests
                |__ unit
                    |__ tests_*.py
                |__ integration
                    |__ tests_*.py
                |__ mocks.py  (custom mock functions/classes/data)
        |__ fixtures (default users and profile json)
        |__ models.py
        |__ factories.py (creational class for User)
        |__ urls.py (urls related to account management)
        |__ views.py
    |__ api
        |__ bl (bussiness logics)
            |__ bigquery.py (google bigquery class)
            |__ inaturalist.py (inaturalist class)
        |__ tests
                |__ unit
                    |__ tests_*.py
                |__ integration
                    |__ tests_*.py
                |__ mocks.py  (custom mock functions/classes/data)
            |__ views.py
            |__ urls.py
    |__ setup (files to use in production)
        |__ nginx (nginx setup)
        |__ *.json (google credential)
    |__ inaturalist
        |__ ...config py files
        |__ uwsgi.init  (server config for production)
    |__ docker-compose.yml (config for development environment)
    )
|__ bin  (utility bash scripts)
    |__ *.sh (bash scripts)

|__ front
    |__ tests (unit or e2e) empty atm :'(
    |__ src
        |__ assets (imgs)
        |__ components (all reusable vue components)
        |__ guards (for route protection)
        |__ js
            |__ API.js
            |__ AxiosWrapper.js
            |__ constants.js
            |__ dialog.js (class for popup confirmation action)
            |__ helpers.js (general purpose utilitary functions)
            |__ Interceptor.js (used to check requests)
        |__ router (url path)
        |__ store (vuex files)
        |__ views (main vue components for routes)
    |__ env.development.local (config variables)
```

## Setup Server development
* In root directory, define env.example properly
    - GCP_BQ_CREDS_JSON it means the .json name for GCP connection
    - wait for receive a working setup
* rename .env.example into .env
* rename inaturalist/uwsgi.py.example into inaturalist/uwsgi.py
* Build docker: `sh bin/build-server.sh`
* In front folder, define env.development.local properly
    - the important are: VUE_APP_RECAPTCHA_V3 and VUE_APP_BASE_URL
    - wait for receive a working setup
* Run migrations: `python3.7 manage.py migrate`

## Bash scripts
* Enter web container terminal: `sh bin/enter-dev-server.sh`
* Enter front container terminal: `sh bin/enter-front-server.sh`
* Start container service: `sh bin/start-dev-server.sh`
* Stop container service: `sh bin/stop-dev-server.sh`
* Run development server: `sh bin/run-back-server.sh`
* Run vue development server: `sh bin/run-front-server.sh`