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

# Run your tests
poetry run behave
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
│   ├── steps/              # Step definitions for BDD scenarios   ── steps/              # Step definitions for BDD scenarios
│   ├── environment.py      # Behave hooks for setup and teardown
│   └── *.feature           # Feature files with Gherkin scenarios
├── utilities/
│   ├── config_reader.py    # Utilities for reading configuration
│   └── generating_logs.py  # Logging utilities
├── logs/                   # Generated logs reports
├── pyproject.toml          # Poetry configuration
├── poetry.lock             # Poetry lock file (generated)
└── Testcases-SwagLabs.xlsx # Manual test scenarios
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





