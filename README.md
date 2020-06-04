<a href="http://fvcproductions.com"><img src="https://www.buythelogo.com/wp-content/uploads/2019/03/Letter-E-geometric-line-abstract-shape-logo-vector.jpg" title="FVCproductions" alt="FVCproductions" height=200 ></a>

# Azen Store API

> Web Development Project - E-commerce mobile application


[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) 


## Table of Contents
- [Azen](#azen-store-api)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Clone](#clone)
    - [Setup](#setup)
  - [Features](#features)
  - [Team](#team)
  - [License](#license)



---

## Installation


### Clone

- Clone this repo to your local machine using `https://github.com/gusmendez99/AzenStoreAPI`

### Setup
> Configure the database you are using by changing the DATABASES dictionary in ./directory-where-you-cloned-this-repo/AzenStoreApi/azenstoreapi/settings.py.
> Below configuration is an example, you should provide the values of your database to the NAME, USER, PASSWORD, HOST and PORT keys.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
> Create and activate your virtual enviroment, see `https://docs.python.org/3/library/venv.html` for a step by step guide. 
> Then navigate to './directory-where-you-cloned-this-repo/AzenStoreApi' and install the dependencies of the 
project listed in the requirements.txt file by running: 

```shell
$ pip install -r requirements.txt
```
> Run the migrations for each Django app
```shell
$ python manage.py makemigrations

```
> Create the tables in the database

```shell
$ python manage.py migrate
```
> Start the django server and run the app
```shell
$ python manage.py runserver
```
- The Django app will run port `8000` (default configuration).

---

## Features
- Django using a PostgreSQL database
- JWT Authentication
- Social Account Auth


## Team


| Gustavo Mendez | Luis Urbina |
| :---: |:---:|
| [![Gustavo](https://avatars0.githubusercontent.com/u/19374517?s=200&u=c1481289dc10f8babb1bdd0853e0bcf82a213d26&v=4)](http://github.com/gusmendez99)    | [![Urbina](https://avatars3.githubusercontent.com/u/35355445?s=200&u=851bb2374c95ac3baaaca3de5f51212441ebff57&v=4)](http://github.com/virtualmonkey) |
| <a href="http://github.com/gusmendez99" target="_blank">`github.com/gusmendez99`</a> | <a href="http://github.com/virtualmonkey" target="_blank">`github.com/virtualmonkey`</a> |

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="http://gusmendez99.github.io" target="_blank">Gus Mendez</a> & <a href="https://github.com/virtualmonkey" target="_blank">Luis Urbina</a>.
