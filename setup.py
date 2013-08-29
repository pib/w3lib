from setuptools import setup

setup(
    name='w3lib',
    version='1.3',
    license='BSD',
    description='Library of web-related functions',
    author='Scrapy project',
    author_email='info@scrapy.org',
    url='https://github.com/scrapy/w3lib',
    packages=['w3lib'],
    platforms = ['Any'],
    use_2to3=True,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
