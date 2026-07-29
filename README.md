# Selenium QA Automation Portfolio

![Tests](https://github.com/mirandaxjill0215/selenium-qa-portfolio/actions/workflows/tests.yml/badge.svg)

Automated test suite for [Sauce Demo](https://www.saucedemo.com), a demo e-commerce site used for practicing test automation. Built with Python and Selenium using the Page Object Model design pattern, with tests running automatically on every push via GitHub Actions.

## What This Covers

- **Login flow**: valid login, invalid credentials, empty fields, locked-out user
- **Cart functionality**: adding items, verifying cart contents across pages
- **Sorting**: verifying price sort order (low to high)
- **Homepage load**: basic smoke test

7 tests total, all passing, with an HTML report generated on every run.

## Tech Stack

- Python 3.9
- Selenium 4
- pytest + pytest-html
- GitHub Actions (CI)

## Project Structure

- pages/ - Page Object Model classes (login_page.py, inventory_page.py, cart_page.py)
- tests/ - Test files (test_homepage.py, test_login.py, test_cart.py, test_sorting.py)
- driver_factory.py - Shared Chrome driver setup (CI-compatible)
- .github/workflows/ - CI pipeline

## Running Locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v --html=report.html --self-contained-html
```

## Notes

Chrome runs with `--no-sandbox` and `--disable-dev-shm-usage` flags to support running headlessly in CI environments (GitHub Actions runners don't have a display, so these flags plus a fixed window size keep Chrome stable without a physical screen).
