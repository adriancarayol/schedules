# schedules
Opening hours - (Micro)Service to store opening hours.

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#thoughts">Thoughts</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This microservice contains services to return humanised schedules.

It has been developed following the recommendations of:
[12factor](https://12factor.net/es/) and a [clean architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html), where dependencies are explicit.

[FastAPI](https://fastapi.tiangolo.com/) has been used over other Python frameworks because of its simplicity and performance.

### Project structure

* app
    Where lives all the microservice code, business logic...
* docker
    Docker files and gunicorn configuration, also the `sh` scripts used by the Dockerfile.
* scripts
    Scripts used mainly by the CI/CD
* tests
    Unit tests of the microservice.

### Styles, guidelines...

In this project, we're using `black`, `isort` and `flake8` to ensure the quaility of the code, following
[wemake](https://wemake-python-stylegui.de/en/latest/) styleguide.

## Getting Started

In order to use this project, you need to install some tools:

### Prerequisites
* **python** (python 3.8 or higher are recommended)
    Install python from: https://www.python.org/downloads/
* **docker**
    Install dockers from: https://docs.docker.com/engine/install/
* **docker-compose**
    Install docker-compose from: https://docs.docker.com/compose/install/
* **poetry**
    Install poetry from: https://python-poetry.org/docs/#installation

### Installation
1. Clone the repo
   ```sh
   git clone git@github.com:adriancarayol/schedules.git
   ```
2. Install python packages
   ```sh
   poetry install
   ```
3. Copy the content of `.env.sample` to `.env``
   ```sh
   cp .env.sample .env
   ```
4. Take a look at the `Makefile` to get started.

## Usage

### Running unit tests

#### Using Makefile:
```sh
make tests
```
#### Using custom command:
```sh
PYTHONPATH=app poetry run pytest --cov=tests --cov=app --cov-report=term-missing --cov-config=setup.cfg -vv
```

### Check styles and guidelines in the code
#### Using Makefile:
```sh
make styles
```

### Running the server
#### Using Makefile:
```sh
make up
```
#### Using custom command:
```sh
docker-compose up
```

### Doing some requests:
You can visit: http://localhost:8000/docs to open the Swagger to make requests to the API

****
or you can use `curl` to create some requests:

```sh
curl --request POST \
  --url http://localhost:8000/api/schedules \
  --header 'Content-Type: application/json' \
  --data '{
   "opening_hours":{
      "monday":[
         
      ],
      "tuesday":[
         {
            "type":"open",
            "value":36000
         },
         {
            "type":"close",
            "value":64800
         }
      ],
      "wednesday":[
         
      ],
      "thursday":[
         {
            "type":"open",
            "value":37800
         },
         {
            "type":"close",
            "value":64800
         }
      ],
      "friday":[
         {
            "type":"open",
            "value":36000
         }
      ],
      "saturday":[
         {
            "type":"close",
            "value":3600
         },
         {
            "type":"open",
            "value":36000
         }
      ],
      "sunday":[
         {
            "type":"close",
            "value":3600
         },
         {
            "type":"open",
            "value":43200
         },
         {
            "type":"close",
            "value":75600
         }
      ]
   }
}'
```

## Thoughts
Well, I think using JSON to store this data structure is interesting from the point of view
that it is quite flexible to add new fields.

For example, it is quite common for a business to have **different opening hours**
depending on the season of the year.

Even public holidays depending on the city or country.

On the other hand, I don't see that it is unreasonable to store it in a conventional SQL table, for example:

```sh
schedules table
--------- 
uuid | weekday | from_time | to_time | season 

holidays table
---------
...
```

Even restrictions could be added at the database level so that the same day is not defined twice etc...

But, since it's information that won't change frequently, I'll stick with the flexibility of storing it in JSON.