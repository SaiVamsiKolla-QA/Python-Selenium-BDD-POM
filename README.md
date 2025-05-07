# Python Selenium BDD+POM Framework

A robust automation framework developed in Python using Selenium, Pytest, and Behave, combining Behavior-Driven
Development (BDD) with the Page Object Model (POM) design pattern.Designed to automate UI test cases for Swag Labs demo
website.

## Features

* Page Object Model (POM) design pattern
* Behavior-Driven Development (BDD) with Gherkin syntax
* Configuration management with config.ini
* Cross-browser testing support (Chrome, Firefox, Edge)
* Modular and maintainable test architecture
* Utilities for logging and configuration

## Prerequisites

* Python 3.9 or higher
* Git
* Google Chrome
* Java JDK 8 or higher *(required for Allure reporting)*
* Poetry

## Setup

**1. Install Poetry**

```bash
# Windows (PowerShell)

(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# Mac/Linux

pip install poetry
```

**2. Install dependencies**

```bash
# Clone the repository

git clone https://github.com/SaiVamsiKolla-QA/Python-Selenium-BDD-POM.git
cd Python-Selenium-BDD-POM

# Install all dependencies

poetry install

# Activate the virtual environment

poetry shell
```

## Install Allure (if needed)

**Mac:**

```bash
brew install allure
```

**Windows (Scoop):**

```bash
scoop install allure
```

**Windows (Chocolatey):**

```bash
choco install allure-commandline
```

## Project Structure

```
Python-Selenium-BDD-POM/
├── features/
│   ├── Pages/              # Page Object classes
│   ├── steps/              # Step definitions for BDD scenarios
│   ├── environment.py      # Behave hooks for setup and teardown
│   └── *.feature           # Feature files with Gherkin scenarios
├── utilities/
│   ├── init.py         # Package initialization
│   ├── screenshot_utils.py # Screenshot capture utilities
│   ├── log_utils.py        # Logging utilities
│   └── config_reader.py    # Configuration reader utilities
├── Test-artifacts/         # Test execution artifacts
│   ├── Logs/               # Generated log files
│   ├── Reports/            # Test reports
│   └── Screenshots/        # Captured screenshots
├── pyproject.toml          # Poetry configuration
├── poetry.lock             # Poetry lock file (generated)
└── Testcases-SwagLabs.xlsx # Manual test scenarios
```
## Running Tests
```bash
#Run all Test
poetry run behave

# Run all tests with allure reporting
poetry run behave -f allure_behave.formatter:AllureFormatter -o ./Test-artifacts/Reports
# To see the report 
allure serve ./Test-artifacts/Reports 
```

## Benefits of using Poetry

- Consistent dependency versions across different environments
- Automatic virtual environment management
- Simplified Workflow: Single command to install all dependencies
- Better dependency resolution and conflict handling
- CI/CD Integration: Easy to integrate with Jenkins and other CI systems

## For Contributors

When adding new dependencies to the project:

```bash
# Add a new dependency
poetry add package-name

# Add a development dependency
poetry add --group dev package-name
```





