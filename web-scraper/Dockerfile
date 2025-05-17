# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY scraper.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint
CMD ["python", "scraper.py"]
