import pytest
from makeup.env import env, get_env, set_env
import os

TEST_VAR = 'ENV_TEST_VAR'
TEST_VAR_FAIL = 'ENV_TEST_VAR_FAIL'

if os.environ.get(TEST_VAR_FAIL):
    del os.environ[TEST_VAR_FAIL]

os.environ[TEST_VAR] = 'SUCCESS'

def test_env_normal():
    assert env(TEST_VAR) == 'SUCCESS'

def test_env_dotenv():
    assert env('AM_I_LOADED', envfile='test.env') == 'true'

def test_env_not_found():
    with pytest.raises(KeyError):
        env(TEST_VAR_FAIL)

def test_env_default():
    assert env(TEST_VAR_FAIL, 'my_default') == 'my_default'

def test_get_env():
    assert get_env(TEST_VAR) == 'SUCCESS'

def test_get_env_not_found():
    assert get_env(TEST_VAR_FAIL) is None

def test_set_env():
    del os.environ[TEST_VAR]
    assert get_env(TEST_VAR) is None
    set_env(TEST_VAR, 'SUCCESS')
    assert get_env(TEST_VAR) == 'SUCCESS'
