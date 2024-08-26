FROM python:3.11

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    nmap \
    wget \
    unzip \
    ca-certificates \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/projectdiscovery/nuclei/releases/download/v2.9.5/nuclei_2.9.5_linux_amd64.zip && \
    unzip nuclei_2.9.5_linux_amd64.zip && \
    mv nuclei /usr/local/bin/ && \
    rm nuclei_2.9.5_linux_amd64.zip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

CMD ["pytest", "-v"]