FROM python:3.9-slim-buster

RUN mkdir /src
# Set working directory
WORKDIR /src
COPY .  /src

# Install dependencies
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# Copy project files
# Set permissions for entrypoint.sh
RUN chmod +x entrypoint.sh
# Expose port
EXPOSE 800
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Run entrypoint.sh
CMD ["/bin/sh", "-c", "./entrypoint.sh"]
