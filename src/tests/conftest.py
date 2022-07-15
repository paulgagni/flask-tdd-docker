# src/tests/conftest.py

import pytest
from src import app, db

#n pytest, “fixtures” are functions you define that serve this purpose. But they don’t have to be limited to just the arrange steps. 
# They can provide the act step, as well, and this can be a powerful technique for designing more complex tests, especially given how pytest’s fixture system works. 
# We can tell pytest that a particular function is a fixture by decorating it with @pytest.fixture.
# Fixtures are reusable objects for tests. https://testdriven.io/blog/flask-pytest/#fixtures They have a scope associated with them, which indicates how often the fixture is invoked:

# 1. function - once per test function (default)
# 2. class - once per test class
# 3. module - once per test module
# 4. session - once per test session

@pytest.fixture(scope='module')
def test_app():
    app.config.from_object('src.config.TestingConfig')
    with app.app_context():
        yield app #Testing occurs here


@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db # Testing occurs here - all code before the yield statement serves as setup code while everything after serves as the teardown.
    db.session.remove()
    db.drop_all()

#More on fixtures: https://docs.pytest.org/en/latest/explanation/fixtures.html#improvements-over-xunit-style-setup-teardown-functions 