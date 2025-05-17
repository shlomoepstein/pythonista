import re


inputfile = 'electron-configurations.html'
outputfile = 'electron-configurations-linked.html'


with open(inputfile, encoding='utf-8') as infile:
   html = infile.read()

pattern = re.compile(r'<td>([A-Za-z]+)</td>')

def makelink(match):
   name = match.group(1)
   url = f'https://en.wikipedia.org/wiki/{name}'
   return f'''<td>
          <a href="{url}" target="_blank" rel="noopener noreferrer">{name}</a>
        </td>'''

new_html = pattern.sub(makelink, html)

with open(outputfile, 'w', encoding='utf-8') as outfile:
   outfile.write(new_html)

