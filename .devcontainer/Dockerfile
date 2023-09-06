FROM mcr.microsoft.com/devcontainers/python:0-3.11

COPY pyproject.toml ./

ENV PYTHONUNBUFFERED 1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=0 \
    POETRY_VIRTUALENVS_CREATE=0 \
    PIP_DEFAULT_TIMEOUT=100\
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN pip install poetry &&\
    poetry install --no-root &&\
    rm -rf $POETRY_CACHE_DIR

# WORKDIR $HOME
# RUN git clone --depth=1 https://github.com/pyenv/pyenv.git .pyenv
# 
# ENV PYENV_ROOT="$HOME/.pyenv"
# ENV PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"
# 
# RUN pyenv install 3.7.0 &&\
#      pyenv install 3.8.0 &&\
#      pyenv install 3.9.0 &&\
#      pyenv install 3.10.0 &&\
#      pyenv install 3.11.0 &&\
#      pyenv install 3.12-dev &&\
#      pyenv install 3.13-dev