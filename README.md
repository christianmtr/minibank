# Minibak

## Requirements

- Python 3.12.1
- Packages in `requirements.txt`

## Instalation

- Install Python 3.12.1.
```
pyenv install 3.12.1
```
- Create a new virtual environment called `venv-minibank`.
```
pyenv virtualenv venv-minibank
```
- Activate the virtual environment.
```
pyenv activate venv-minibank
```
- Install required packages.
```
pip install -r requirements.txt
```

## Setup

- Create a `.env` file.
- Get a new secret key:
```
openssl rand -hex 32
```
- Copy the result to the `.env` file:
```
SECRET_KEY="<secret-string>"
```
