# Python Selenium BDD+POM Framework

A robust automation framework developed in Python using Selenium, Pytest, and Behave, combining Behavior-Driven Development (BDD) with the Page Object Model (POM) design pattern. Integrated  Allure for detailed reporting. Designed to automate UI test cases for Swag Labs demo website.

## Features

* Page Object Model (POM) design pattern
* Behavior-Driven Development (BDD) with Gherkin syntax
* Allure reports with screenshots at every test step


## Prerequisites

* Python 3.9 or higher
* Git
* Google Chrome
* Java JDK 8 or higher *(required for Allure reporting)*

## Setup

**1. Clone the repository**

```
git clone https://github.com/SaiVamsiKolla-QA/Python-Selenium-BDD-POM.git
cd Python-Selenium-BDD-POM
```

**2. Create and activate the virtual environment**

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r Requirements.txt
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
│   ├── steps/              # Step definitions for BDD scenarios
├── allure-results/         # Allure results directory
├── reports/                # Generated test reports
├── setup_check.py          # Environment verification script
└── Testcases-SwagLabs.xlsx # Manual test scenarios
```







