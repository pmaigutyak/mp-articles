
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='django-mp-articles',
    version='1.0.0',
    description='',
    long_description=open('README.md').read(),
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url='https://github.com/pmaigutyak/mp-articles',
    download_url='https://github.com/pmaigutyak/mp-articles/archive/1.0.tar.gz',
    packages=['articles'],
    license='MIT',
    install_requires=[
        'django-ckeditor==5.2.1',
        'django-pure-pagination==0.3.0'
    ]
)
