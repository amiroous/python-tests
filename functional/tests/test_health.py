import pytest


class TestHealth:

    @pytest.mark.health_test
    def test_health(self):
        is_healthy = True
        assert is_healthy

    @pytest.mark.health_test
    def test_health_2(self):
        is_healthy = True
        assert is_healthy
