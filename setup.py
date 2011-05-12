from setuptools import setup, find_packages

setup(
  name="GML Analyzer Server",
  version="0.0.1",
  description="A web service for finding similarities between Graffiti Markup Language tags",
  author="Golan Levin",
  author_email="golan@flong.com",
  packages=find_packages(),
  test_suite='nose.collector',
  tests_require=['nose'],
  install_requires=[
    'Flask>=0.3'
  ]
)