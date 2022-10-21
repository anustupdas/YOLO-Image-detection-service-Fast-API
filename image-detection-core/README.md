[![Python 3.6](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-3614/)
 <a href="">
        <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/example-template-service"></a>

#  Image Detection Core

The core library may contain python code that is core to a specific project which mainly deals with the business logic, such as model initialization, inference and data pre- or post-processing.
For this project all main functions related to the inferencing of the yolo4 model along with all the pre and post-processing of the input image. 

## Getting Started

### Installation from repo
Run the following commands:
```
sudo apt-get install libyaml-dev
cd <install-directory>/image-detection-core
poetry update
poetry install
poetry build
```

Alternatively, install the module from pip:
```
pip install image-detection-core
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

* **Your_Name** your_mail@address.com

## License

MIT.

### Release Notes 
* `0.1.0`
    * First Version of the image detection core

    




