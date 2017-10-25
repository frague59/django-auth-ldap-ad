# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import os
from distutils.core import setup
from setuptools import find_packages

# Loads the version from package
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from django_ldap_ad import __version__ as version

setup(
    name='django-auth-ldap-ad',
    version=version,
    description='An application providing some template tags to add buttons to pages',
    author='François GUÉRIN',
    author_email='fguerin@ville-tourcoing.fr',
    url='https://github.com/frague59/django-auth-ldap-ad',
    license='BSD',
    keywords=['Django', 'LDAP', 'Active Directory'],
    classifiers=['Development Status :: 4 - Beta',
                 'Framework :: Django :: 1.9',
                 'Framework :: Django :: 1.10',
                 'Framework :: Django :: 1.11',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python',
                 'Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP',
                 ],
    install_requires=['Django',
                      'django-appconf',
                      'ldap'],
    # Source files
    packages=find_packages('.'),

    # Includes static files
    include_package_data=True,
    packages_data={'docs': ["*", ],
                   'static': ["*", ],
                   'templates': ["*", ]},

)

