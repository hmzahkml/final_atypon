FROM python:3.9-slim-buster

# Set working directory
WORKDIR /src

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Set permissions for entrypoint.sh
RUN chmod +x entrypoint.sh

# Expose port
EXPOSE 8000

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Run entrypoint.sh
CMD ["/bin/sh", "-c", "entrypoint.sh"]
