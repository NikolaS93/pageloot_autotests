# Pageloot Autotests 

### Language: Python v3.6

Install dependencies
=====================
* Install the required packages in ``requirements.txt`` using ``pip install -r requirements.txt``

Initialization of driver
=====================
In Pageloot/base/__init__.py is placed website url and initialization of chrome webdriver

Create new test case
=====================

* In Pageloot/base/basepage webdriver is passed to page object classes
* In Pageloot/pages are stored all pages 
* Tests are stored in **tests** folder 

Run the test case
==================

In order to run the test case, use the below command:

``python -m pytest tests/test_QR_creation.py``
