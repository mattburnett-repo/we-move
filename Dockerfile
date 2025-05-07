# docker build -t we-move .
# docker run --rm --name we-move -p 5000:5000 we-move


FROM python:3.10-slim

# Set environment variables
#  Prevent Python from writing .pyc files to the filesystem
ENV PYTHONDONTWRITEBYTECODE=1
#  Docker logs to show up in real time
ENV PYTHONUNBUFFERED=1

ENV FLASK_APP=app
ENV FLASK_ENV=development

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

EXPOSE 5000

# Run the app (adjust if needed)
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]