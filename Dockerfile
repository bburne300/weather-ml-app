FROM python:3.9-slim 

# Set the working directory in the container 

WORKDIR /app 

# Copy the current directory contents into the container at /app  

COPY . /app 

# Installs dependencies from file  

RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container 

EXPOSE 5000 

# Run the app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
