# BUILD-USING: docker build -t updatedns-cron .
# RUN-USING:   docker run --volumes-from updatedns-logs --detach=true --name updatedns updatedns-cron

FROM debian:wheezy
MAINTAINER dralagen@dralagen.fr

#
# Set correct environment variables.
ENV HOME /root

# API key find on webinterface of gandi
ENV GANDI_API yourApiKey
# Domain managed
ENV GANDI_DOMAIN exemple.com
# Zone id to edit (can find on webinterface of gandi)
ENV GANDI_ZONE_ID yourZoneId

RUN apt-get update && apt-get install -y software-properties-common python-software-properties && apt-get update

# Install Python Setuptools
RUN apt-get install -y python2.7 cron ssmtp

RUN apt-get purge -y python-software-properties software-properties-common && apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD cron-updatedns /etc/cron.d/
ADD updatedns.py /
ADD run-cron.py /

ADD ssmtp.conf /etc/ssmtp/ssmtp.conf

RUN chmod a+x updatedns.py run-cron.py

# Set the time zone to the local time zone
RUN echo "Europe/Paris" > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

CMD ["/run-cron.py"]

