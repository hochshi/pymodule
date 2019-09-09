# pymodule
Provide a python interface to RHEL module.
Two functions are provided:
* **list** - List loaded modules
* **\_\_call\_\_** - will run module with the given args as a list of strings or multiple string arguments

## Usage
```python
    from pymodule import pymodule
    module = pymodule.PyModule()
    # List loaded modules:
    module.list()
    # Load modules
    module('load', 'bash')
    module(['load','bash'])
    # The entire set of commands are supported via __call__
    # as example
    module('purge')
```

## Configuration
Please override the following defaults with your system specific ones before creating a PyModule instance, the defaults are shown in parentheses
* MODULE_VERSION ('3.2.10') - used to set the version
* MODULESHOME ('/apps/RH7U2/Modules/%s' % MODULE_VERSION) - used as base path to bin/modulecmd and to init/.modulespath
* MODULE_RE ('\d+\)\s+([\w/\.]+)') - used to parse module list output and return match 'module/version' i.e. git/2.11.0