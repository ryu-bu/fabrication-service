FROM ubuntu:latest

EXPOSE 8080:8080

ARG CHARTARUM_ENV

# Set environment variables
ENV CHARTARUM_ENV=${CHARTARUM_ENV} \
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
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y ncbi-blast+ nginx python3-pip

# Using Anaconda as our base python installation due to some Poetry
# shenanigans.
RUN curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN chmod +x Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -b -p /usr/local/miniconda

# Install NPM to install our frontend...
RUN curl -sL https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt install nodejs


WORKDIR /code
# Get our NCBI Databases

# Size of Swissprot: 176 mb
RUN curl -O 'ftp://ftp.ncbi.nlm.nih.gov/blast/db/swissprot.tar.gz'
RUN tar -xvf swissprot.tar.gz
RUN rm swissprot.tar.gz

# Size of NB as of 08/14/2020: 84.18 gb. So, we might not want to do this.
#RUN wget 'ftp://ftp.ncbi.nlm.nih.gov/blast/db/nr.*.tar.gz'
#COPY nr.*.tar.gz /code/blast-databases
#RUN tar -xvf nr.*.tar.gz .
#RUN rm nr.*.tar.gz


# Install our python dependency manager
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
COPY backend/poetry.lock pyproject.toml /code/

# Project initialization:
WORKDIR /code
RUN poetry config virtualenvs.create false && poetry install $(if [ "$CHARTARUM_ENV" == 'production' ]; then echo "--no-dev"; fi) --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /code

# Service Spinup goes here