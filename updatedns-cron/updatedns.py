#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-
# updatedns.py

import xmlrpclib, urllib2, time, re, sys, os

import logging
logging.basicConfig(filename='/var/log/updatedns.log',level=logging.INFO)

# API de Production
api = xmlrpclib.ServerProxy('https://rpc.gandi.net/xmlrpc/')

#########################

# URL de la page retournant l'ip publique
url_page = 'http://ifconfig.me/ip'

# Renseignez ici votre clef API générée depuis l'interface Gandi:
apikey = str(os.environ["GANDI_API"])

# Domaine concerné
mydomain = str(os.environ["GANDI_DOMAIN"])

# Enregistrement
allrecord = [{'name': '@', 'type': 'A'}, {'name':'*', 'type':'A'}]

# TTL
myttl = 300

# id de la zone concernée
zone_id = int(os.environ["GANDI_ZONE_ID"])

# date et heure du changement d'IP
asctime = time.asctime( time.localtime() )

####################################

# Récupération de l'ancienne ip
oldip = api.domain.zone.record.list(apikey, zone_id, 0, allrecord[0])[0].get('value')

try:
    # Récupération de l'ip actuelle
    f = urllib2.urlopen(url_page)
    data = f.read()
    f.close()
    pattern = re.compile('\d+\.\d+\.\d+\.\d+')
    result = pattern.search(data, 0)
    if result == None:
        print("Pas d'ip dans cette page.")
        sys.exit()
    else:
        currentip = result.group(0)

    # Comparaison et mise a jour si besoin
    if oldip != currentip:
        # On cree une nouvelle version de la zone
        version = api.domain.zone.version.new(apikey, zone_id)
        # Mise a jour (suppression puis création de l'enregistrement)
        for myrecord in allrecord:
            api.domain.zone.record.delete(apikey, zone_id, version, myrecord)
            myrecord['value'] = currentip
            myrecord['ttl'] = myttl
            api.domain.zone.record.add(apikey, zone_id, version, myrecord)
        # On valide les modifications sur la zone
        api.domain.zone.version.set(apikey, zone_id, version)
        api.domain.zone.set(apikey, mydomain, zone_id)
        logging.info("Modification de l'enregistrement effectuée le %s" % asctime)
        logging.info("avec l'adresse IP : %s" % currentip)
except urllib2.HTTPError, xmlrpclib.ProtocolError:
    logging.info("Site indisponible.")
finally:
    sys.exit()

