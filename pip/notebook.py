import pip
import sys

site_packages = next(filter(
  lambda x: 'site-packages-3' in x,
  sys.path
))

print(
  pip.main(f'install ',
           f'--target {site_packages} '
           f'notebook'.
  split(' '))
)

