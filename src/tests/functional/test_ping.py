# src/tests/test_ping.py

import json

# Follow the given-when-then framework for writing tests - https://martinfowler.com/bliki/GivenWhenThen.html
def test_ping(test_app):
    # Given - the state of the application before the test runs - setup code, fixtures, database state
    client = test_app.test_client()
    # When - the behavior/logic being tested - code under stress
    resp = client.get('/ping')
    data = json.loads(resp.data.decode())
    # Then - the expected changes based on the behavior - asserts
    assert resp.status_code == 200
    assert 'pong' in data['message']
    assert 'success' in data['status']

# code to run all tests: docker-compose exec api python -m pytest "src/tests"
# code to run tests that have the config in the name: docker-compose exec api python -m pytest "src/tests" -k config