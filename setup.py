from setuptools import setup

setup(
    name='reqWrap',
    version='1.0.0',
    packages=['reqWrapper'],
    url='https://github.com/box-archived/reqWrap',
    license='Apache License 2.0',
    author='box-archived',
    author_email='box.cassette@gmail.com',
    description='Wrapper of requests with retry options',
    setup_requires=['certifi~=2020.12.5',
                    'chardet~=4.0.0',
                    'idna~=2.10',
                    'requests~=2.25.1',
                    'urllib3~=1.26.2']
)
