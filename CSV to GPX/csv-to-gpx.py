import csv
from datetime import datetime
from zoneinfo import ZoneInfo

eastern = ZoneInfo("America/New_York")
utc = ZoneInfo("UTC")


with open('out.gpx', 'a') as outfile:
   outfile.write('''\
<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.1"
     creator="csv-to-gpx"
     xmlns="http://www.topografix.com/GPX/1/1"
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xsi:schemaLocation="
       http://www.topografix.com/GPX/1/1
       https://www.topografix.com/GPX/1/1/gpx.xsd">

  <trk>
    <name>Example Track</name>
''')

   outfile.write('''\
    <trkseg>
''')

   with open('raw.csv', newline='') as infile:
      reader = csv.reader(infile, skipinitialspace=True)

      for date, time, lat, lon, ele in reader:
         utc_dt = (datetime.fromisoformat(f'{date}T{time}')
                           .replace(tzinfo=eastern)
                           .astimezone(utc))
         utc_dt_str = utc_dt.isoformat().replace('+00:00', 'Z')

         outfile.write(f'''\
      <trkpt lat="{lat}" lon="{lon}">
        <ele>{ele}</ele>
        <time>{utc_dt_str}</time>
      </trkpt>
''')

   outfile.write('''\
    </trkseg>
''')

   outfile.write('''\
  </trk>

</gpx>
''')

