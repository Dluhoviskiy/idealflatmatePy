# The guide for running ui-tests

- Install Python 3.7 https://www.python.org/downloads/ (use the latest stable version)

- Install virtualenv package in the project

$ pip install virtualenv

- Create a virtual environment with, for example, "venv" identifier

$ virtualenv venv

- Activate the virtual environment

$ source venv/bin/activate
- for Win10
$ venv\Scripts\activate
 

- Go to "Project Name" folder and install the packages which are necessary to have the tests work

$ cd <Project Name>

$ pip install -r requirements.txt

- Install Java (use java 8)

- Install Allure via Homebrew 

$ brew install allure

For Windows, Allure is available from the Scoop commandline-installer.

To install Allure, download and install Scoop and then execute in the Powershell (write "PowerShell" and open it).

Execute the command in Powershell:

$ Set-ExecutionPolicy RemoteSigned -scope CurrentUser

Then execute the following command in Powershell:

$ iex (new-object net.webclient).downloadstring('https://get.scoop.sh')

Use Powershell again and execute the following command:

$ scoop install allure

Also Scoop is capable of updating Allure distribution installations. To do so navigate to the Scoop installation directory and execute

$ \bin\checkver.ps1 allure -u

This will check for newer versions of Allure, and update the manifest file. Then execute

$ scoop update allure

to install a newer version.

- Install allure for pytest

Use a command line and execute

$ pip install allure-pytest

- Download Selenium Server Standalone https://www.seleniumhq.org/download/

- Download ChromeDriver https://sites.google.com/a/chromium.org/chromedriver/downloads

- Unzip it 

$ unzip chromedriver_<os>.zip

- Run all tests with creating allure reports

$ pytest -q --alluredir ./allure-reports

- Generate report in a HTML

$ allure serve ./allure-reports