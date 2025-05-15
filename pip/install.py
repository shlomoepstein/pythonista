import requests
import sys
from io import BytesIO
from zipfile import ZipFile

# Get the location of the Python 3 site-packages
site_packages = next(filter(
  lambda x: 'site-packages-3' in x,
  sys.path
))

# extract directly into site-packages
ZipFile(BytesIO(requests.get(
    'https://files.pythonhosted.org/packages/90/a9/1ea3a69a51dcc679724e3512fc2aa1668999eed59976f749134eb02229c8/pip-21.3-py3-none-any.whl'
).content)).extractall(site_packages)

print("Downloaded pip")

