FROM ubuntu:latest

ARG FABRICATION_ENV

# Set environment variables
ENV FABRICATION_ENV=${FABRICATION_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0.0

############## System Level Dependencies ######################

# Install system level dependencies
RUN apt-get update
RUN apt install -y curl
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nginx python3-pip  git make build-essential python-dev libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev curl libffi-dev

# Pyenv for our baseline python environment for poetry later on.
RUN git clone git://github.com/yyuu/pyenv.git .pyenv
RUN git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

ENV HOME  /
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
ENV ENV_FILE_LOCATION=.env

RUN pyenv install 3.8.0
RUN pyenv global 3.8.0


# Install NPM to install our frontend...
RUN curl -sL https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt install nodejs


WORKDIR /code

# Install our python dependency manager
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml /code/

# Project initialization:
WORKDIR /code
RUN poetry config virtualenvs.create false && poetry install $(if [ "$FABRICATION_ENV" == 'production' ]; then echo "--no-dev"; fi) --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /code
# Generate JWT Key for the purposes of signing
RUN JWT_KEY=$(openssl rand -base64 172 | tr -d '\n') && echo "JWT_SECRET_KEY = \"${JWT_KEY}\"" > .env
# Expose
EXPOSE 80
# Run
CMD ["python", "run.py"]