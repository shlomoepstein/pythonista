import csv
from collections import namedtuple
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


with open('out.gpx', 'a') as outfile:
   outfile.write(preamble)
   outfile.write(segstart)

   with open('raw.csv', newline='') as infile:
      reader = csv.reader(infile, skipinitialspace=True)

      for point in map(Point._make, reader):
         outfile.write(gpxpoint(point))

   outfile.write(segend)
   outfile.write(postamble)

