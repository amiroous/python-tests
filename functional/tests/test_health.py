import pytest


@pytest.mark.health_test
class TestHealth:

    def test_health(self):
        is_healthy = True
        assert is_healthy
