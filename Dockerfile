# textteaser
#

FROM python:2.7-alpine

# since we are using upstream's python image that installs python into /usr/local/bin, its fine to use /usr/local/bin/pip for this. we still use virtualenv for the app code so its all owned by the user
RUN pip install --no-cache-dir virtualenv

# create a user
RUN adduser -S textteaser

USER textteaser
ENV HOME=/home/textteaser
WORKDIR /home/textteaser
RUN virtualenv ~/pyenv \
 && . ~/pyenv/bin/activate

# install the code in a two step process to keep the cache smarter
ADD requirements.txt /tmp/requirements.txt
RUN . ~/pyenv/bin/activate \
 && pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /home/textteaser/src/textteaser
# todo: i wish copy would keep the user...
USER root
RUN mkdir /data \
 && chown -R textteaser:nogroup \
    /data \
    /home/textteaser/src

# install the app as the user, run the --help once to make sure it works
USER textteaser
WORKDIR /home/textteaser/src/textteaser
RUN . ~/pyenv/bin/activate \
 && pip install --no-cache-dir -r requirements.txt -e . \
 && echo hello, world | textteaser-cli

ENV TERM=xterm
ENTRYPOINT ["/home/textteaser/pyenv/bin/textteaser-loop"]
