Learn FastAPI through <https://fastapi.tiangolo.com/>

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

## 📚️ Reference

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)
- [go-task](https://taskfile.dev/)
