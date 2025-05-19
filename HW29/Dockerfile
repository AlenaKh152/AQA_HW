FROM jenkins/jenkins:lts
USER root

RUN ln -sf /usr/share/zoneinfo/Europe/Minsk /etc/localtime && \
    echo "Europe/Minsk" > /etc/timezone


RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    git \
    curl \
    unzip \
    wget && \
    rm -rf /var/lib/apt/lists/*


ENV VENV_PATH=/opt/venv
RUN python3 -m venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"


RUN pip install --upgrade pip setuptools wheel
RUN pip install pytest allure-pytest requests

USER jenkins
WORKDIR /home/jenkins/workspace
