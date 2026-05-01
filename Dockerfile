FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

# Install Firefox + driver (simple version)
RUN apt-get update && apt-get install -y firefox-esr

ENV MOZ_HEADLESS=1

CMD ["pytest", "-v"]