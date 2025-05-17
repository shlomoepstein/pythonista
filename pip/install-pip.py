import sys
import requests
from os.path import basename
from io import BytesIO
from zipfile import ZipFile


site_packages = next(
   p for p in sys.path
   if p.startswith('/private')
   and basename(p) == 'site-packages-3')


ZipFile(BytesIO(requests.get(
   'https://files.pythonhosted.org/packages/29/a2/d40fb2460e883eca5199c62cfc2463fd261f760556ae6290f88488c362c0/pip-25.1.1-py3-none-any.whl'
).content)).extractall(site_packages)

print('downloaded pip')

