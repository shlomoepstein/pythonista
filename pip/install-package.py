import sys
import pip
from os.path import basename


# edit this variable and run
package = 'html5lib'

site_packages = next(
   p for p in sys.path
   if p.startswith('/private')
   and basename(p) == 'site-packages-3')


pip.main([
   'install',
   '--target', site_packages,
   package])

print('done')

