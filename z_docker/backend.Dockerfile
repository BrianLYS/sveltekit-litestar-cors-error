# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY /requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY /backend .

# Copy the init_admin.sh script from same folder into the container
COPY ./z_docker/init_admin.sh .

# Expose the port the app runs on
EXPOSE 8000

# Run the init_admin.sh script and then start the application
CMD ["sh", "-c", "./init_admin.sh && litestar run -r"]