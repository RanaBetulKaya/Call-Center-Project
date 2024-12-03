FROM python:3.10
 
# Install necessary system libraries
RUN apt-get update && apt-get install -y libsndfile1

# Set up the working directory
WORKDIR /app

# Copy your app files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start the application
CMD ["python", "Main.py"]
