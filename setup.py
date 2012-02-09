from distutils.core import setup
import os

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('aloha'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[6:] # Strip "aloha/" or "aloha\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


setup(name='aloha',
      version='1.0.2',
      description='A Django template tag renders a "Hello" in different langauges',
      author='Andreas Aderhold',
      author_email='aderhold.andreas@gmail.com',
      url='http://github.com/aha/aloha/',
      package_dir={'aloha': 'aloha'},
      packages=packages,
      package_data={'aloha': data_files},
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
