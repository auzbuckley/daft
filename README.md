# daft.ie tests

## Setup
1. Ensure you have python 2.7 or later installed https://www.python.org/downloads/. To check what version you may already have installed, you can type:

  `$ python --version`
  
2. Check that you have pip installed:

  `$ pip --version`
  
  If you get `pip: command not found`, do:
  
  `$ sudo easy_install pip`
  
3. [optional (but recommended)] please install and use virtualenv to create a virtual python environment. 

  To install virtualenv wrapper on a **mac** use:

  `$ pip install virtualenvwrapper` NOTE: you may need to use sudo e.g. `$ sudo pip install virtualenvwrapper`
  
  On some operating systems such as El Capitan you may get an error similar to:
  
  `OSError: [Errno 1] Operation not permitted: '/tmp/pip-fwQzor-uninstall/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/six-1.4.1-py2.7.egg-info'`
  
  Here you will have to tell pip to ignore the six package:
  
  `$ pip install virtualenvwrapper --ignore-installed six`
  
  Add the following two lines to the bottom of your `.bashrc`, or equivalent files (such as `.zshrc`) []:

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
  environment is created, afterwich you should see `(venv)$` in your command line which indicated that you are
  working on this environment.
  
  ### Useful virtualenvwrapper commands:
  
  To deactivate your environment (stop working on it):
  
  `$ deactivate`
  
  To work on your environment:
  
  `$ workon venv`
  
  To delete your environment:
  
  `$ rmvirtualenv venv`
  

4. Either inside you virtual env, or on your local installation of python, change directory to `daft_tests/` directory and run:

  `$ pip install -r requirements.txt`
  
5. Ensure that you have Mozilla Firefox installed. (The frontend tests use the firefox driver.)

## Frontend Tests
To run frontend tests, change directory to the `frontend_tests/` directory:

  `$ behave --no-capture --format plain --logging-level INFO`
  
The test output should show in your console.

## API Tests
To run api tests, change directory to the `API_tests/` directory and run:

  `$ API_KEY=<YOUR_API_KEY> pytest distance_tests.py`
  
  This will run all tests found within the distance_tests.py file. To run a single test, use:
  
  `test_file.py::TestClass::test_method`
  
  e.g. `$ API_KEY=<YOUR_API_KEY> pytest distance_tests.py::TestDirectionsAPI::test_optional_parameters_only`
  
The test output should show in your console.

## NOTES:

### API tests:

- I believe in agile's view of "working software over comprehensive documentation" and have found that mindmaps are a great way to explore the product and testing ideas holistically. Not everything in this [mind map](https://github.com/auzbuckley/daft/blob/master/API_tests/mindmap.png) may correlate directly to automation, but helps give an overall view of the parts of the product, how they are connected and what could/should be tested (either manually, or automatically). It is also good to create these mind maps as a team so that everyone can contribute. The mind map can be used to highlight major risks, performance and load criteria, features, conditions etc.

- I am on the fence about where to specify request data. My initial line of thinking is to place it within the relevant tests, making the code easier to read. Although, often it can be good practice to assign such information to variables at the top of the file or in a completely separate file so that it can be reused, and changed only in the one place. One plus with having such data within the test in this particular case is that it can be different for each test (e.g. different origins, destinations, modes etc) thus increasing test coverage.

- I would spend a bit more time on the naming of the tests as this is important for legibility.

- The test `test_no_output_specified_returns_404` has no explicit assert. This is partly because of how I designed the response code assert into the `get_distance` method to reduce repetitive code. However as a side effect it has meant that the above-mentioned test does not clearly show that anything is being asserted. So if I had more time, I would think more about how to handle this.

- The client.py file is probably not the best for the private `_assert_code` method.

- The test `test_multiple_origins_and_destinations_returns_correct_results` is quite a large test. In most circumstances I would try to keep each individual test's assertions to a minimum for debugging/ clarity reasons. However here, we have a large response object on which we want to perform multiple checks, as opposed to having multiple tests (and therefore multiple requests) that return the same response object in order to perform single checks.

- The private methods are a bit 'rough' and could do with further refactoring.

- Logging and error handling should be more thorough and descriptive.

### Frontend tests

- I designed the test as one long 'flow' test rather than breaking it up into smaller tests for example, one for the homepage search, and another for the advanced search.

- Occasionally, a `StaleElementReferenceException` is raised when the webdriver attempts to click on the city in the dropdown. This is likely due to the webdriver being too fast, finding the element before javascript changes the element, and the clicking the element that is now no longer in the DOM. This would need to be handled by an explicit wait or implicit wait as last resort.

- I ended up using a few more xpaths than I would like, however css selectors and xpaths now generally perform the same on modern browsers. It can be useful for developers to add a qa specific tag attribute so that items can be identified efficiently.

- In the steps, I have instantiated the page objects on an as-needed basis. However this means that the order of the steps becomes important. For example, if one step instantiates the HomePage class, then it can't be used in an preceeding steps unless it is instantiated there also. So it might make sense to simply instantiate all page objects once in the before all hook.

- Logging and error handling should be more thorough and descriptive.
