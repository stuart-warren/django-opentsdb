django-opentsdb
===============

Django site to play with as a nicer front end to OpenTSDB. Uses NVD3.js graphs

Install django 1.4.3 [https://docs.djangoproject.com/en/1.4/intro/install/]
```
cd opentsdb_dashboard/
python manage.py runserver
```

Open browser to http://127.0.0.1:8000

Initial version uses a static data file.

To point to actual data, see dashboard/translate.py. 
Change url to one for opentsdb ascii data for metrics you want (may want to down-sample)
