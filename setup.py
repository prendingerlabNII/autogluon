from setuptools import setup, find_packages

setup(
    name='autogluon',  # Your main package name
    version='0.1.0',  # Your version
    packages=find_packages(where='.', include=['autogluon', 'autogluon.*']),
    package_dir={
        'autogluon.timeseries': 'timeseries/src/autogluon/timeseries',
        'autogluon.core': 'core',
        'autogluon.common': 'common',
    },
    # You can include other metadata and dependencies here,
    # or keep them in setup.cfg
)