Django Cride
=============

Group-bounded, invite-only, carpooling platform# Django-Cride

This README provides comprehensive instructions for setting up and understanding my Django-Cride. This was created with an advance Django Course that helped me understand the advance concepts of this Framework.

- ## Description
Instagram-based app created by Platzi using Python.

#### Features
- Creation and Login for users <br>
- Post Creation ( photo with description )<br>
- Feed to see posts of other users<br>
- User details and button to update profile<br>
- Post detail view when clicking a post<br>

#### Technologies
- Python
- Django
- Sqlite
- CSS
- HTML
- Bootstrap

#### Folders Structure

```bash

Platzigram/
├── media/                # includes binaries from users
├── static/               # have the binaries from the app and CSS 
├── templates/            # results of the analysis (data, tables, figures)
├── platzigram/           # data files used in the project
│   ├── settings.py       # settings for the core app
│   └── middleware.py     # handles specific interactions with the app
│   └── ...
├── posts/                # folder with all the posts related components
│   ├── views.py          # contains all the views from the posts
│   ├── models.py         # contains all the models from the posts
│   └── ...
├── users/                # folder with all the users related components
│   ├── views.py          # contains all the views from the user
│   ├── models.py         # contains all the models from the user
│   └── ...
├── README.md             # overview of the project
├── requirements.txt      # software requirements and dependencies
├── manage.py             # handles administrative tasks for Django Framework

```

- ## Installation

First, clone the repository following the steps provided by GitHub

Second, we install a virtual environment
``` python -m venv venv ```

Initialize the virtual environment:
``` .\venv\Scripts\activate ```

Finally, to install all the required packages, we need to type in the console:

``` pip install -r requirements.txt ```

- ## Execute App

Type ``` python manage.py runserver ``` to initialize the app.

- ## App's Screenshots 

- ### Login View

![image](https://github.com/luisdiaz2022/Django-Platzigram/assets/98700136/665f2ac5-38bb-46e7-a051-8fac56378d37)

- ### Signup View

![image](https://github.com/luisdiaz2022/Django-Platzigram/assets/98700136/7a346270-2886-4258-9465-5a01920d6bba)

- ### Feed View

![image](https://github.com/luisdiaz2022/Django-Platzigram/assets/98700136/33afafdf-e0d2-4fb6-8992-8f0b13d8fdce)


- ### Profile View

![image](https://github.com/luisdiaz2022/Django-Platzigram/assets/98700136/043adef1-6152-45af-a577-17f870ef07e4)
