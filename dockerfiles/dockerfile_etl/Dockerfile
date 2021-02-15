FROM python:3.7

# USER root
# COPY . ./

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app/q_pack"

WORKDIR /app

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

CMD xvfb-run --server-args="-screen 0 1024x768x24"
# CMD gunicorn --bind :60 app:app
# CMD gunicorn app:app


# Another way to give root access without password in the compose
    # environment:
    #   GRANT_SUDO: "yes"
    # user:
    #   "root"