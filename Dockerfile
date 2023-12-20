# Use the python:3.9-slim image to build and install dependencies
FROM python:3.9 as build

# create app directory in container
RUN mkdir -p /app
WORKDIR /app

# copy source code to container
COPY . /app

# Use the python:3.9-alpine image to run the application
FROM python:3.9-alpine

# create app directory in container
RUN mkdir -p /app
WORKDIR /app

# copy source code and dependencies from the build stage
COPY --from=build /app /app

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

# set environment variable
ENV TOKEN=yourtokenhere

# run the application
# CMD ["/bin/sh"]
CMD ["python3", "main.py"]
