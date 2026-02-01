# Base Image: Lightweight Python
FROM python:3.10-slim

# Set Working Directory
WORKDIR /app

# Install system dependencies (if needed later)
# RUN apt-get update && apt-get install -y ...

# Copy Requirements (Create this file dynamically or copy it)
# We will create a requirements.txt in the next step, but for now let's write it here or copy it.
COPY requirements.txt .

# Install Python Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Application Code
COPY . .

# Expose Streamlit Port
EXPOSE 8501

# Command to run the application
ENTRYPOINT ["streamlit", "run", "level6_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
