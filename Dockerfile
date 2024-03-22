
# using an Python3 image as the base image
FROM python:3.10

# run a graphical application to use a virtual display that enables gui simulation
RUN apt-get update && apt-get install -y xvfb

WORKDIR /first-docker-app

COPY ./src ./src

# there are no dependencies!

CMD ["xvfb-run","python3", "./src/main.py"]
