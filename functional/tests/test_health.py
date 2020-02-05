import pytest
from functional.tests.test_case import TestCase


class TestHealth(TestCase):

    @pytest.mark.health_test
    def test_health(self):
        is_healthy = True
        assert is_healthy

    @pytest.mark.health_test
    def test_health_2(self):
        is_healthy = True
        assert is_healthy
