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


def similar(p1, p2, eps=1e-3):
   lat1, lon1 = float(p1.lat), float(p1.lon)
   lat2, lon2 = float(p2.lat), float(p2.lon)

   return (abs(lat1 - lat2) <= eps
           and abs(lon1 - lon2) <= eps)


with open('out.gpx', 'w') as outfile:
   outfile.write(preamble)

   with open('raw.csv', newline='') as infile:
      reader = csv.reader(infile, skipinitialspace=True)

      outfile.write(segstart)
      inseg = True
      prev = Point._make(next(reader))

      for curr in map(Point._make, reader):
         if inseg:
            outfile.write(gpxpoint(prev))

            if similar(curr, prev):
               outfile.write(segend)
               inseg = False

         elif not similar(curr, prev):
            outfile.write(segstart)
            outfile.write(gpxpoint(prev))
            inseg = True

         prev = curr

      if inseg:
         outfile.write(gpxpoint(prev))
         outfile.write(segend)

   outfile.write(postamble)

