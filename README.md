Learn FastAPI through <https://fastapi.tiangolo.com/>

Follow the commits' orders, from [first commit](https://github.com/east4ming/learn_fastapi/commit/9d0d3cccf4a889a95eb0ca751806c6dbeced6cb2) to learn.

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

## 📚️ Reference

* [FastAPI Docs](https://fastapi.tiangolo.com/)
* [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)
* [go-task](https://taskfile.dev/)
