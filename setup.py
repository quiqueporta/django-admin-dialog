from setuptools import setup

from django_admin_dialog import get_version


setup(
    name='django-admin-dialog',
    version=get_version(),
    license='GPLv2',
    author='Quique Porta',
    author_email='quiqueporta@gmail.com',
    description='Shows a dialog popup with helptext for the admin fields that you have indicated.',
    long_description=open('README.md').read(),
    url='https://github.com/quiqueporta/django-admin-dialog',
    download_url='https://github.com/quiqueporta/django-admin-dialog/releases',
    keywords=['django', 'tools'],
    packages=['django_admin_dialog'],
    install_requires=['django', 'django-redactoreditor'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP'
    ],
)
