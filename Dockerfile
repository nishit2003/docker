# Nishit Grover
# Project 3: Docker

# I will use python:alpine as the base image
FROM python:alpine

# Now, set the given location of the working directory
WORKDIR /home/data

# Copy the files to the working directory
COPY scripts.py IF.txt AlwaysRememberUsThisWay.txt /home/data/

# Run the Python code
CMD ["python", "/home/data/scripts.py"]

