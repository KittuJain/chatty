from setuptools import setup, find_packages

setup(
    name='leavebot',
    version='0.1',
    packages=['agent_portal','engine/src/api','engine/src/core'],
    url='www.thoughtworks.com',
    license='Apache License 2.0',
    long_description='True virtual agent help',
    zip_safe=False,
    install_requires=['Flask', 'nltk'],
    data_files = [('engine/src/api',['engine/src/api/application.cfg']),
                  ('engine/src', ['engine/src/requirements.txt'])]
)
