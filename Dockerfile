# NVIDIA Deep Learning Institute (DLI)
FROM nvcr.io/nvidia/dli/dli-nano-ai:v2.0.1-r32.5.0

WORKDIR /home

# utils
RUN apt-get update && \
    apt-get install -y rsync i2c-tools

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP run.py
ENV DEBUG True

COPY requirements.txt .

# install python dependencies
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY env.sample .env

COPY . .

# RUN flask db init
# RUN flask db migrate
# RUN flask db upgrade

# install pip utils
RUN pip3 install loguru \
                pandas

# gunicorn
# CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
# gunicorn --config gunicorn-cfg.py run:app