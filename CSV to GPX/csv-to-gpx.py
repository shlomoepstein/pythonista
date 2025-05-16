import csv
from collections import namedtuple
from operator import itemgetter
from itertools import groupby
from datetime import datetime
from zoneinfo import ZoneInfo


Point = namedtuple('Point', 'date time lat lon ele')

eastern = ZoneInfo('America/New_York')
utc = ZoneInfo('UTC')

preamble = '''\
<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.1"
  creator="csv-to-gpx"
  xmlns="http://www.topografix.com/GPX/1/1"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="
    http://www.topografix.com/GPX/1/1
    https://www.topografix.com/GPX/1/1/gpx.xsd">
  <trk>
    <name>csv to gpx</name>'''
segstart = '''
    <trkseg>'''
segend = '''
    </trkseg>'''
postamble = '''
  </trk>
</gpx>\n'''


def gpxpoint(point):
   utc_dt = (datetime.fromisoformat(f'{point.date}T{point.time}')
                     .replace(tzinfo=eastern)
                     .astimezone(utc)
                     .isoformat()
                     .replace('+00:00', 'Z'))
   return f'''
      <trkpt lat="{point.lat}" lon="{point.lon}">
        <ele>{point.ele}</ele>
        <time>{utc_dt}</time>
      </trkpt>'''


def similar(p1, p2, eps):
   lat1, lon1 = float(p1.lat), float(p1.lon)
   lat2, lon2 = float(p2.lat), float(p2.lon)

   return (abs(lat1 - lat2) <= eps
           and abs(lon1 - lon2) <= eps)


# give each cluster a unique id
def cid_points(points, eps=1e-3):
   prev = next(points)
   cid = 0
   yield cid, prev

   for curr in points:
      if not similar(curr, prev, eps):
         cid += 1
      prev = curr
      yield cid, curr


with (open('locations.csv', newline='') as infile,
      open('out.gpx', 'w', encoding='utf-8', newline='') as outfile):

   reader = csv.reader(infile, skipinitialspace=True)
   points = map(Point._make, reader)

   outfile.write(preamble)
   outfile.write(segstart)

   for cid, group in groupby(cid_points(points), itemgetter(0)):
      cluster = [point for cid, point in group]

      if len(cluster) == 1:
         outfile.write(gpxpoint(cluster[0]))
      else:
         outfile.write(gpxpoint(cluster[0]))
         outfile.write(segend)
         outfile.write(segstart)
         outfile.write(gpxpoint(cluster[-1]))

   outfile.write(segend)
   outfile.write(postamble)

