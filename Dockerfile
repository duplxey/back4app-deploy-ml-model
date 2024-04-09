FROM python:3.12.2-alpine3.19

# Install the required dependencies (gcc)
RUN apk add build-base

# Set the working directory
WORKDIR /app

# Set environmental variables
# PYTHONWRITEBYTECODE: If set to 1, Python will not write .pyc files
# PYTHONUNBUFFERED: If set to 1, Python will not buffer the output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy over the requirements file and install the dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

# Copy over the source code
COPY . .

# Expose the port
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]