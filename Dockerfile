# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script to the working directory
COPY mac_address_vendor.py .

# Set the entry point for the container
ENTRYPOINT ["python", "mac_address_vendor.py"]

# Set the default command argument
CMD ["<default_argument>"]