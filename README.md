OpenWifi
========

An Israeli Pirate Party project, dedicated to mapping open WiFi networks.

Dev
---
Development of OpenWifi follows the standard Python dev environment setup, and assumes knowledge of such tools:

 1. `git clone git://github.com/israelipirates/openwifi.git`
 2. `cd openwifi`
 3. `mkvirtualenv openwifi`
 4. `pip install -r requirements.txt`
 5. `python app.py`

Deployment
----------
OpenWifi is built to be deployed on the Heroku platform. Follow the usual steps for Heroku deployment:

 1. `heroku create`
 2. `git push heroku master`

Note that the Redis add-on is required for persistence.
