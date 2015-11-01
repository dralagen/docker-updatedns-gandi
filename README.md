# docker-updatedns-gandi
Docker container to auto update your gandi's zone dns

## Gandi information

In *updatedns-cron/Dockerfile* we need to change environement variables with good information

```
# API key find on webinterface of gandi
ENV GANDI_API yourApiKey
# Domain managed
ENV GANDI_DOMAIN exemple.com
# Zone id to edit (can find on webinterface of gandi)
ENV GANDI_ZONE_ID yourZoneId
```


## Cron sendmail

wee need to add *updatedns-cron/ssmtp.conf* file with good information to send mail

```
root=me@exemple.com
hostname=updatedns.domain
mailhub=mail.exemple.com:465
AuthUser=username
AuthPass=password
UseTLS=YES
```
