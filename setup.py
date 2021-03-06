#!/usr/bin/python

import distutils.core

distutils.core.setup(name='acc',
      version='12',
      license='GPL3',
      description='A system to manage the pam_access access.conf file',
      long_description='''This tool is a easy to use front-end to allow scripts
      and system administrators to build and maintain an access.conf file for use
      with pam_access.so. The tool is designed so that scripts and humans don't
      trample on each other.''',
      url='http://www.evad.io',
      author='David Bell',
      author_email='dave@evad.io',
      scripts=['acc'],
options = {'bdist_rpm':{'post_install' : 'post_install',
                        'post_uninstall' : 'post_uninstall'}},
      )
