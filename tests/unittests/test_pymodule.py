import os
import subprocess

import pytest

from pymodule import pymodule

os_keys = {
    'MODULE_VERSION_STACK': None,
    'MODULE_VERSION': None,
    'MODULESHOME': None,
    'MODULEPATH': None,
    'LOADEDMODULES': None,
}

pymodule_keys = {
    'MODULE_VERSION': pymodule.MODULE_VERSION,
    'MODULESHOME': pymodule.MODULESHOME,
    'MODULE_RE': pymodule.MODULE_RE,
}


def set_or_del(key, val):
    if val is None:
        try:
            del os.environ[key]
        except KeyError:
            pass
    else:
        os.environ[key] = val


@pytest.fixture(autouse=True)
def reset():
    for key in os_keys.keys():
        os_keys[key] = os.environ.get(key, None)
    for key in pymodule_keys.keys():
        pymodule_keys[key] = getattr(pymodule, key, None)
    yield
    for key, val in os_keys.items():
        set_or_del(key, val)
    for key, val in pymodule_keys.items():
        setattr(pymodule, key, val)


@pytest.fixture()
def setup_module_version():
    pymodule.PyModule.setup_module_version()


@pytest.fixture()
def setup_moduleshome():
    pymodule.PyModule.setup_moduleshome()


@pytest.fixture()
def setup_modulepath():
    pymodule.PyModule.setup_modulepath()


def test_setup_module_version():
    pymodule.PyModule.setup_module_version()
    assert os.environ['MODULE_VERSION_STACK'] == pymodule_keys[
        'MODULE_VERSION'] and os.environ['MODULE_VERSION'] == pymodule_keys[
            'MODULE_VERSION']


def test_setup_module_version_exists():
    os.environ['MODULE_VERSION'] = 'TEST'
    pymodule.PyModule.setup_module_version()
    assert os.environ['MODULE_VERSION_STACK'] == 'TEST' and os.environ[
        'MODULE_VERSION'] == 'TEST'


def test_setup_moduleshome():
    pymodule.PyModule.setup_module_version()
    assert os.environ['MODULESHOME'] == pymodule_keys['MODULESHOME']


def test_setup_modulepath(setup_moduleshome):
    pymodule.PyModule.setup_module_version()
    assert os.environ['MODULEPATH']


def test_setup_modulepath_exists(setup_moduleshome):
    os.environ['MODULEPATH'] = 'TEST'
    pymodule.PyModule.setup_module_version()
    assert os.environ['MODULEPATH'] == 'TEST'


def test_clear_loadedmodules():
    module = pymodule.PyModule()
    module('purge')
    pymodule.PyModule.clear_loadedmodules()
    assert not os.environ['LOADEDMODULES']


def test_parse_stderr():
    modules_text = b'''Currently Loaded Modulefiles:
  1) git/2.11.0                  2) anaconda/5.2.0/python/3.6
  '''
    parsed = ['git/2.11.0', 'anaconda/5.2.0/python/3.6']
    assert pymodule.PyModule.parse_stderr(modules_text) == parsed


def test__run_cmd():
    module = pymodule.PyModule()
    with pytest.raises(subprocess.CalledProcessError):
        module('mekmek')


def test_list():
    module = pymodule.PyModule()
    module('purge')
    assert module.list() == []
