Learn FastAPI through <https://fastapi.tiangolo.com/>

Follow the [commits](https://github.com/east4ming/learn_fastapi/commits/main/)' orders, from [first commit](https://github.com/east4ming/learn_fastapi/commit/9d0d3cccf4a889a95eb0ca751806c6dbeced6cb2) to learn.

## Install FastAPI

> 📚️
> <https://fastapi.tiangolo.com/tutorial/#fastapi>

### Prerequisites

```shell
# pyenv
# install python 3.11 with pyenv
pyenv install 3.11
# swith to python 3.11 with pyenv
pyenv local 3.11

# create virtualenv with `venv`
python3.11 -m venv env && source env/bin/activate
```

### Install FastAPI

```shell
python -m pip install "fastapi[all]"
# or
python -m pip install fastapi "uvicorn[standard]"
```

### Or, Use go-task Executor All Above

```shell
# install go-task
sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d

# install pyenv and requirements
task install
```

## 🧑‍🎓Learn

### 1️⃣First Steps

* Import FastAPI.
* Create an `app` instance.
* Write a path operation decorator (like `@app.get("/")`).
* Write a path operation function (like `def root():` ... above).
* Run the development server (like `uvicorn main:app --reload`).

### Path Parameters

With FastAPI, by using short, intuitive and standard Python type declarations, you get:

* Editor support: error checks, autocompletion, etc.
* Data "parsing"
* Data validation
* API annotation and automatic documentation

### Query Parameters

When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

The query is the set of key-value pairs that go after the `?` in a URL, separated by `&` characters.

* Query Defaults
* Optional parameters
* Query parameter type conversion
* Multiple path and query parameters
* Required query parameters

## 📚️ Reference

* [FastAPI Docs](https://fastapi.tiangolo.com/)
* [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)
* [go-task](https://taskfile.dev/)
