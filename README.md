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
 2. `heroku addons:add heroku-postgresql:dev`
 3. `heroku pg:promote HEROKU_POSTGRESQL_<COLOR>`
 4. `git push heroku master`

Database
--------
In either case database tables should be created via a Python interactive console (`python` locally or `heroku run python` on Heroku):

```python
from app import app
from models import db
with app.test_request_context():
    db.create_all()
```

License
-------
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

