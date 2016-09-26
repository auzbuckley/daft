# daft.ie tests

## Setup
1. Ensure you have python 2.7 or later installed. To check what version you may already have installed, you can type:

  `$ python --version`
  
2. [optional (but recommended)] please install and use virtualenv to create a virtual python environment. 

  To install on a **mac** use:

  `$ pip install virtualenvwrapper`
  
  Add the following two lines to the bottom of your `.bashrc`, `.profile` or equivalent files (such as `.zshrc`):

  ```
  export WORKON_HOME=$HOME/.virtualenvs
  source /usr/local/bin/virtualenvwrapper.sh
  ```
  
  Restart your terminal or `$ source .bashrc`
  
  To install on **windows** use:
  
  `$ pip install virtualenvwrapper-win`
  
  In windows, the default path for WORKON_HOME is %USERPROFILE%Envs
  
  Then create a virtual environment by running:
  
  `$ mkvirtualenv venv`
  
  Where `venv` is the name of your environment. You should now see several output lines as your virtual
  environment is created, afterwich you should see `(venv)$` in your command line.
  
  To deactivate your environment (stop working on it):
  
  `$ deactivate`
  
  To work on your environment:
  
  `$ workon venv`
  
  To delete your environment:
  
  `$ rmvirtualenv venv`
  

3. Either inside you virtual env, or on your local installation of python, change directory to `daft_tests/` directory and run:

  `$ pip install -r requirements.txt`

## Frontend Tests
To run frontend tests, change directory to the `frontend_tests/` directory:

  `$ behave --no-capture --format plain --logging-level INFO`

## API Tests
To run api tests, change directory to the `API_tests/` directory and run:

  `$ API_KEY=abc123 pytest distance_tests.py`
  
  This will run all tests found within the distance_tests.py file. To run a single test, use:
  
  `test_file.py::TestClass::test_method`
  
  e.g. `$ API_KEY=abc123 pytest distance_tests.py::TestDirectionsAPI::test_optional_parameters_only`
