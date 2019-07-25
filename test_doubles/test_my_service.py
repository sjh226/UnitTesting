import unittest

from my_service import MyService
from single_sign_on import *

# three kinds of assert:
#   check the return value or an exception
#   check a state change(use a public API)
#   check a method call (use a mock or spy)

# a mock can take an initiative and fail a test

# stub or fake may have functionality that is never called

# spy will listen in on communication between the class you're trying
# to test and the collaborating class
#   MyService and SSORegistry
# spy fails in the assert, mock fails in the act

# a stub returns a hard coded answer to and query
# a fake is a real implementation, yet unsuitable for production
# a mock is a stub, and additionally verifies interactions
# a test spy lets you query afterwards to find out what happened
# a dummy is for when the interface requires an argument that does not have to be used

# COVERAGE
# python -m pytest --cov-report html --cov tennis
# # pragma: no coverage
#   will exclude code from coverage

class MyServiceTest(unittest.TestCase):
    def test_invalid_token(self):
        registry = FakeSingleSignOnRegistry()
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=None)
        self.assertIn("please enter your login details", response)

    def test_valid_token(self):
        registry = FakeSingleSignOnRegistry()
        token = registry.register("valid credentials")
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token)
        self.assertIn("hello world", response)

    # following two methods are to "check a method call"
    def test_invalid_token_with_mock(self):
        token = SSOToken()
        registry = MockSingleSignOnRegistry(expected_token=token, token_is_valid=False)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=token)
        self.assertTrue(registry.is_valid_was_called)

    def test_valid_token_with_mock(self):
        token = SSOToken()
        registry = MockSingleSignOnRegistry(expected_token=token, token_is_valid=True)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=token)
        self.assertTrue(registry.is_valid_was_called)

    def test_invalid_token_with_spy(self):
        token = SSOToken()
        registry = SpySingleSignOnRegistry(accept_all_tokens=False)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=token)
        self.assertIn(token, registry.checked_tokens)

    def test_valid_token_with_spy(self):
        token = SSOToken()
        registry = SpySingleSignOnRegistry(accept_all_tokens=True)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=token)
        self.assertIn(token, registry.checked_tokens)
