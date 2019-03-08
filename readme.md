[![Build Status](https://travis-ci.org/bisonlou/questioner.svg?branch=ft-164364453-create-user-login)](https://travis-ci.org/bisonlou/questioner) [![Coverage Status](https://coveralls.io/repos/github/kbjude/questioner/badge.svg?branch=ch-164393776-setup-testing-environment)](https://coveralls.io/github/kbjude/questioner?branch=ch-164393776-setup-testing-environment) [![Maintainability](https://api.codeclimate.com/v1/badges/a41afe011f4784815a00/maintainability)](https://codeclimate.com/github/bisonlou/questioner/maintainability)



# Questioner
by The dojos


 Questioner is ...


 ## Installation:
  - Clone this repository.
  - Setup a virtual environment and activate it.
  - Install the requirements.txt
  - Add a ".env" file that has:
    - export DJANGO_SETTINGS_MODULE="questioner.settings"
<<<<<<< HEAD
    - export DATABASE_NAME
    - export DATABASE_HOST
    - export DATABASE_USER
    - export DATABASE_PASSWORD
=======
    - export Database
    - export Host
    - export User
    - export Password
>>>>>>> ft-164364453-create-user-login


 ## Running the application:
  Open the directory of the application in the terminal and execute:

    python manage.py migrate
    python manage.py runserver

   In a browser type the Url: http//localhost:8000.


 ## Sign Up

  Using postman login with endpoint
   ```
    http://127.0.0.1:8000/auth/signup/
  ```
  Provide your credentials under the body tab
  ```
  {
  	"username": "your-username",
  	"email": "your-email",
	  "password": "your-password"
  }

  ```

 ## Login

  Using postman login with endpoint
   ```
    http://127.0.0.1:8000/auth/login/
  ```
  Provide your credentials under the body tab
  ```
  {
  	"username": "your-username",
	  "password": "your-password"
  }

  ```

 ## Endpoints
| Method | Endpoint         | Description |
| ------ | -----------------| ----------- |
| GET    | /                | Index       |
| POST   |/auth/signup      | Sign up     |
| POST   |/auth/login       | login       |
