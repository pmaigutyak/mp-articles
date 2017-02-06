
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='articles',
    version='1.0.0',
    description='',
    long_description=open('README.md').read(),
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url='https://github.com/pmaigutyak/mp-articles',
    packages=['articles'],
    license='MIT',
    install_requires=[
        'django-ckeditor==5.2.1'
    ]
)
