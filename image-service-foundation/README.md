[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-3614/)
 <a href="">
        <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/example-template-service"></a>

#  Image Service Foundation

The foundation library contains shared python code that can be reused in the Python projects.
For this project it mainly handels the functions that we frequently use to read configuration files and also functions that are needed to access ML models that are hosted in cloud [Google/ Dropbox]  

## Getting Started

### Installation from repo
Run the following commands:
```
sudo apt-get install libyaml-dev
cd <install-directory>/image-service-foundation
poetry update
poerty install
poetry build
```

Alternatively, install the module from PYPI:
```
pip install image-service-foundation
```

### Build

Individual packages can be build with

```bash

poetry build

```
and published to PYPI using
```bash

 twine upload -r packahe_name dist/*

```

Or with Poetry

```bash

poetry publish

```

## Authors

* **Anustup Das** anustup@mediadistillery.com

## License

MIT.


### Release Notes 
1.0.0: Change log one can maintain for each release.
