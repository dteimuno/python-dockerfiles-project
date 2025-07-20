FROM python:3.13-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .
#Expose the port the app runs on
EXPOSE 5276
# Run the app
CMD ["python", "app.py"]
