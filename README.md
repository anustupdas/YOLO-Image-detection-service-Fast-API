![MD Logo](Tools.png)

<h1 align="center">From zero to production in less than a day</h1>
<h3 align="center">A template for hosting your ML solutions quickly with fastAPI </h3>

<p align="center">
	<a href="https://mediadistillery.com/">
    	<img alt="Website Media Distillery" src="https://img.shields.io/website-up-down-green-red/http/shields.io.svg"></a>
	<a href="https://github.com/mediadistillery/ExampleTemplateService/blob/main/LICENSE.txt">
    	<img alt="PyPI License: MIT" src="https://img.shields.io/pypi/l/ansicolortags.svg"></a>
    <a href="https://github.com/psf/black">
		<img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
	<a href="https://svgshare.com/i/Zhy.svg">
        <img alt="Linux" src="https://svgshare.com/i/Zhy.svg"></a>
	<a href="https://github.com/mediadistillery/ExampleTemplateService"><img alt="Ask Me Anything !" src="https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg"></a>
   
<a href="">
        <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/example-template-service"></a>
	<a href="">
        <img alt="Awesome Badges" src="https://img.shields.io/badge/badges-awesome-green.svg"></a>
</p>



Do you have an amazing Machine Learning Solution but you are thinking you do not know how to create a webservice out of it? Well, this project exactly solves your problem. This repo can be used as a kickstarter to convert your local ML application into a running webservice that can be deployed to the server/local.

This is an example project that can help you understand how you can use the framework to design a FastAPI webservice that actually detects objects in an image with the help of **YOLOv4** model that is generally used at Media Distillery.

<h3>In addition, you can also learn about other activities needed to deploy a solution to servers [Production], including:</h3>

- Dependency management and packaging in Python using Poetry.
  * How a simple <b><i> pyproject.toml</b></i> looks like for poetry, can be found under each package. 
  * How you can custom that <b><i> pyproject.toml</b></i> for your project specific needs. 
- Creating the deployable containers of the ML services using Docker.
  * Example <b><i> Dockerfile</b></i> can be found at:
    > image-detection-service/docker/Dockerfile

---

**[Read the blog for more details!](https://bit.ly/From_zero_to_Production_in_less_than_a_day)**

---

## Project Structure

### image-service-foundation:
The foundation library may contain shared python code and functions that can be reused in several Python projects or services.
For this project it mainly handels the functions that we frequently use to read configuration files and also functions that are needed to access ML models that are hosted in cloud [Google/ Dropbox]  

#### Note
The name of the **foundation** package is a bit different from the other package as the **foundation** package is intended to be used by a wide variety or umbrella of projects and services of which **image-detection-service** is one, that can commonly use the functionalities of this package
### image-detection-core:
The core library may contain python code that is core to a specific project which mainly deals with the business logic, such as model initialization, inference and data pre- or post-processing.
For this project all main functions related to the inferencing of the yolo4 model along with all the pre and post-processing of the input image. 

### image-detection-service:
The purpose of the service package is to make the functionalities of the core accessible through a REST API.
This Becomes the main entry point of the webservice which is used to detec objects in an Image.

### Please read the README for each individual package.

You can replace <i>"example-template" </i> with your custom package names while renaming the packages and add custom packages as required. You may need to update other things as well depending on your intended use.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## Authors

* **Anustup** anustup@mediadistillery.com
* **Ryan** ryan@mediadistillery.com
