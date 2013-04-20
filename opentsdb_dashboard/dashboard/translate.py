import csv
import urllib2
from django.http import HttpResponse
from django.utils import simplejson


def nvd3(request):
    # generate nvd3 json here
    #url = 'http://hotcpc9882:4242/q?start=2013/04/10-17:22:55&ignore=2&m=sum:10m-avg:rate:tsd.hbase.rpcs%7Bhost=*,type=*%7D&o=&m=sum:10m-avg:rate:tsd.rpc.received%7Bhost=*,type=*%7D&o=axis%20x1y2&yrange=%5B1:%5D&y2range=%5B1:%5D&ylog&y2log&key=out%20right%20top%20box&wxh=1627x758&ascii'
    url = 'http://localhost:8000/static/tsd.hbase.rpcs-short.txt'

    # spliturl = urlparse.urlsplit(url)
    # parsedquery = urlparse.parse_qs(spliturl[3])
    # unspliturl = urlparse.urlunsplit([spliturl[0], spliturl[1], spliturl[2], spliturl[3], parsedquery])
    # print unspliturl

    serv_req = urllib2.Request(url=url)
    serv_resp = urllib2.urlopen(serv_req)

    allmetrics = []
    metricreader = csv.DictReader(serv_resp,
                                  fieldnames=['metric', 'time', 'value'],
                                  restkey='tags',
                                  delimiter=' ')
    for row in metricreader:
        # Create a unique key
        key = ''.join([row['metric'], '{', ', '.join(row['tags']), '}'])
        # Make a copy of row['tags']
        tags = row['tags']
        # Replace it with a dict version
        row['tags'] = dict()
        for tag in tags:
            t, v = tag.split('=')
            row['tags'].update({t: v})

        new = True
        # Check to see if we have this metric type already
        for m in allmetrics:
            if m['key'] == key:
                new = False
                # If so, just add the data points
                m['values'].append({'x': int(row['time']),
                                       'y': float(row['value'])
                                       })
        if new:
            # If not, Add a new metric type
            allmetrics.append({'key': key,
                               'metric': row['metric'],
                               'tags': row['tags'],
                               'values': [{'x': int(row['time']),
                                           'y': float(row['value'])
                                           }]
                             })
    allmetrics = simplejson.dumps(allmetrics)

    return HttpResponse(allmetrics, mimetype='application/json')
