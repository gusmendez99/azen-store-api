<a href="http://github.com/gusmendez99/AzenStoreMobile"><img src="https://i.imgur.com/SKZIB6d.jpg" title="FVCproductions" alt="FVCproductions" height=200 ></a>

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
  - [Routes](#routes)
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

## Routes

Here are the main routes used in the API

*  Auth
   * Email Register (POST)
      * http://azenstore.herokuapp.com/api/v1/auth/registration/
   * Facebook Register/Login (POST)
      * http://azenstore.herokuapp.com/api/v1/auth/facebook/
   * Login (POST)
      * http://azenstore.herokuapp.com/api/v1/auth/login/
   * Token Refresh (POST)
      * http://azenstore.herokuapp.com/api/v1/token-refresh/
*  Categories
   * Get Categories (GET)
      * https://azenstore.herokuapp.com/api/v1/categories/
   * Create Category (POST)
      * https://azenstore.herokuapp.com/api/v1/categories/
*  Products
   * Get Products (GET)
      * http://azenstore.herokuapp.com/api/v1/products/
   * Create Product (POST)
      * http://azenstore.herokuapp.com/api/v1/products/
   * Get Product Categories (GET)
      * http://azenstore.herokuapp.com/api/v1/products/1/categories/
*  Carts
   * Get Carts (GET)
      * http://azenstore.herokuapp.com/api/v1/carts/
   * Create Cart (POST)
      * http://azenstore.herokuapp.com/api/v1/carts/
   * Get Cart Items (GET)
      * http://azenstore.herokuapp.com/api/v1/cart-items/
   * Add Cart Item (POST)
      * http://azenstore.herokuapp.com/api/v1/cart-items/
   * Remove Cart Item (DELETE)
      * http://azenstore.herokuapp.com/api/v1/cart-items/1/
   * Update Cart Item (PUT)
      * http://azenstore.herokuapp.com/api/v1/cart-items/1/
   * Clear Cart (POST)
      * http://azenstore.herokuapp.com/api/v1/carts/1/clear/
   * Get Cart By User Id (GET)
      * https://azenstore.herokuapp.com/api/v1/carts?user=1
   * Get Cart Items given a user id (GET)
      * http://azenstore.herokuapp.com/api/v1/users/7/cart-items/
*  Coupons
   * Get Coupons (GET)
      * https://azenstore.herokuapp.com/api/v1/coupons/  
*  Orders
   * Get Orders (GET)
      * http://azenstore.herokuapp.com/api/v1/orders/
   * Create Order (POST)
      * http://azenstore.herokuapp.com/api/v1/orders/    
   * Process Order (Cleans Cart) (POST)
      * http://azenstore.herokuapp.com/api/v1/orders/1/process/
*  Wishlists
   * Get Wishlists (GET)
      * http://azenstore.herokuapp.com/api/v1/wishlists/
   * Create Wishlist (POST)
      * http://azenstore.herokuapp.com/api/v1/wishlists/
   * Get Wishlist given a userId (GET)
      * http://azenstore.herokuapp.com/api/v1/wishlists/?user=5
   * Get Wishlist Products (GET)
      * http://azenstore.herokuapp.com/api/v1/wishlists/1/products/
*  Invoices
   * Get Invoices (GET)
      * http://azenstore.herokuapp.com/api/v1/invoices/
   * Create Invoice (POST)
      * http://azenstore.herokuapp.com/api/v1/invoices/
*  Payments
   * Get Payments (GET)
      * http://azenstore.herokuapp.com/api/v1/payments/
   * Create Payment (POST)
      * http://azenstore.herokuapp.com/api/v1/payments/       
*  Reviews
   * Get Reviews (GET)
      * http://azenstore.herokuapp.com/api/v1/reviews/
   * Create Reviews (POST)
      * http://azenstore.herokuapp.com/api/v1/reviews/     

  

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
