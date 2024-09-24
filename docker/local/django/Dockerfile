FROM python:3.10.0-slim-buster

# Set environment variables
ENV APP_HOME=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create app directories
RUN mkdir -p $APP_HOME/staticfiles

# Set working directory
WORKDIR $APP_HOME

# Label for maintainer
LABEL maintainer="salu33956@gmail.com"

# Install dependencies
RUN apt-get update \
  && apt-get install -y build-essential libpq-dev gettext \
  && apt-get install -y netcat gcc postgresql \
  && apt-get purge -y --auto-remove \
  && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip3 install --no-cache-dir --upgrade pip

# Install Python dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy entrypoint and start scripts
COPY ./docker/local/django/entrypoint /entrypoint
COPY ./docker/local/django/start /start

# Fix line endings and permissions
RUN sed -i 's/\r$//g' /entrypoint /start
RUN chmod +x /entrypoint /start

# Use entrypoint script to initialize the container
ENTRYPOINT ["/entrypoint"]

# Default command to run Django's development server
CMD ["/start"]
