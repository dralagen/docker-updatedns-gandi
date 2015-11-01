#!/usr/bin/env python2.7
# run-cron.py
# sets environment variable crontab fragments and runs cron

import os
from subprocess import call
import fileinput

# read docker environment variables and set them in the appropriate crontab fragment
apikey = os.environ["GANDI_API"]
mydomain = os.environ["GANDI_DOMAIN"]
zoneid = os.environ["GANDI_ZONE_ID"]

for line in fileinput.input("/etc/cron.d/cron-updatedns",inplace=1):
	    print line.replace("DOCKER_GANDI_API", apikey)\
				.replace("DOCKER_GANDI_DOMAIN", mydomain)\
				.replace("DOCKER_GANDI_ZONE_ID", zoneid)

args = ["cron","-f"]
call(args)

