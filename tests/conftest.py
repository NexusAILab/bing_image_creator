import pytest

pytest.register_assert_rewrite('tests')

def pytest_configure(config):
    config.addinivalue_line(
        "asyncio_default_fixture_loop_scope",
        "function"
    ) 