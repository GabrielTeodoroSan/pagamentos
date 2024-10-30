FROM python:3.12

WORKDIR /pagamentos

COPY . /pagamentos 
COPY pyproject.toml /pagamentos 
COPY poetry.lock /pagamentos

ENV PYTHONPATH=${PYTHONPATH}:{PWD}
ENV POETRY_VIRTUALENVS_CREATE=false

RUN pip install poetry 
RUN poetry install --without dev --no-root

CMD uvicorn api.main:app --host 0.0.0.0 