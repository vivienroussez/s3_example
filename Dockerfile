FROM python:3.9.6-buster

# Copy all files in the folder
COPY requirements.txt .
COPY get_size.py .
# Install python packages
RUN pip install --no-cache-dir -r requirements.txt