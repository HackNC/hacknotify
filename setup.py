from distutils.core import setup

setup(name='HackNC Notify',
      version='1.0',
      description='HackNC Notification System',
      author='Brandon Davis',
      author_email='bd@unc.edu',
      url='https://hacknc.com/',
      entry_points={
        'console_scripts': ['hacknotify=hacknotify.notify:main']
      },
      packages=['hacknotify'],
      install_requires=[
        'google-api-python-client==1.5.3',
        'httplib2==0.9.2',
        'lxml==3.7.2',
        'oauth2client==3.0.0',
        'packaging==16.8',
        'phonenumbers==7.7.2',
        'plivo==0.11.1',
        'pyasn1==0.1.9',
        'pyasn1-modules==0.0.8',
        'pyparsing==2.1.10',
        'python-dateutil==2.6.0',
        'requests==2.11.1',
        'rsa==3.4.2',
        'simplejson==3.8.2',
        'six==1.10.0',
        'uritemplate==0.6',
        'pysocks==1.6.6',
        'pytz==2016.10',
        'twilio==5.7.0'
      ],
     )