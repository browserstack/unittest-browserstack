# UnitTest-BrowserStack

A sample to run python unittests over BrowserStack Automate.

### Install dependencies

Navigate to appropriate directory for testing and then install the dependencies by running

`pip install -r requirements.txt`

### BrowserStack Authentication

Export the environment variables for the username and access key of your BrowserStack account.
These can be found on the automate accounts page on [BrowserStack](https://www.browserstack.com/accounts/automate)

`export BROWSERSTACK_USERNAME=<browserstack-username>`

`export BROWSERSTACK_ACCESS_KEY=<browserstack-access-key>`

### Run the tests

- To run series tests, run `python -m unittest manager`
- To run series tests with local, run `TEST_TYPE=local python -m unittest manager`
- To run tests with parallel, run `TEST_TYPE=parallel nosetests manager.py -v --processes=4 --process-timeout=600`
- To run tests with parallel with local, run `TEST_TYPE=parallel,local nosetests manager.py -v --processes=4 --process-timeout=600`

------

#### How to specify the capabilities

The [Code Generator](https://www.browserstack.com/automate/python#setting-os-and-browser) can come in very handy when specifying the capabilities especially for mobile devices.
