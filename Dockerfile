# base image
FROM python:3

# install python pip and flask
RUN pip install flask

# inform Docker that the container listens on port 5000 at runtime
EXPOSE 5000
