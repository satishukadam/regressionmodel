import io
import os
from configs import config
from setuptools import setup, find_packages


NAME = 'regression_model'
DESCRIPTION = 'Train and deploy regression model.'
URL = 'your github project'
EMAIL = 'your_email@email.com'
AUTHOR = 'Your name'
REQUIRES_PYTHON = '>=3.6.0'
# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(config.ROOT_DIR, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


setup(name=NAME,
      version='1.0',
      description=DESCRIPTION,
      long_description=long_description,
      classifiers=[
          # Trove classifiers
          # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy'
      ],
      keywords='regression',
      url='http://github.com/satishukadam/regression',
      author='Satish Kadam',
      author_email='satishukadam@gmail.com',
      license='MIT',
      packages=find_packages(where='src'),
      package_dir = {'regression': 'src/regression'},
      package_data={'regression': ['*.py']},
      install_requires=['numpy', 'scipy', 'pandas', 'scikit-learn'],
      include_package_data=True,
      zip_safe=False)

