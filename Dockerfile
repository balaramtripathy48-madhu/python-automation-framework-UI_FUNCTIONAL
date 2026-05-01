FROM python:3.10-slim

WORKDIR /app

COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Install Firefox + geckodriver
RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget \
    && wget https://github.com/mozilla/geckodriver/releases/download/v0.36.0/geckodriver-v0.36.0-linux64.tar.gz \
    && tar -xvzf geckodriver-v0.36.0-linux64.tar.gz \
    && mv geckodriver /usr/local/bin/ \
    && chmod +x /usr/local/bin/geckodriver

CMD ["pytest", "-v"]