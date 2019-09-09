"""A singleton class which provide a python interface to RHEL module
"""

import os
import re
import subprocess
import typing as tp

MODULE_VERSION = '3.2.10'
MODULESHOME = '/apps/RH7U2/Modules/%s' % MODULE_VERSION
MODULE_RE = r'\d+\)\s+([\w/\.]+)'
MODCULE_CMD = '%s/bin/modulecmd' % MODULESHOME


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,
                                        cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class PyModule(metaclass=Singleton):
    def __init__(self):
        self.setup_module_version()
        self.setup_moduleshome()

        self.setup_modulepath()
        self.clear_loadedmodules()

    @staticmethod
    def setup_module_version():
        if 'MODULE_VERSION' not in os.environ:
            os.environ['MODULE_VERSION_STACK'] = MODULE_VERSION
            os.environ['MODULE_VERSION'] = MODULE_VERSION
        else:
            os.environ['MODULE_VERSION_STACK'] = os.environ['MODULE_VERSION']

    @staticmethod
    def setup_moduleshome():
        os.environ['MODULESHOME'] = MODULESHOME

    @staticmethod
    def setup_modulepath():
        if 'MODULEPATH' not in os.environ:
            path = []
            with open(os.environ['MODULESHOME'] + "/init/.modulespath",
                      "r") as inf:
                for line in inf:
                    line = re.sub("#.*$", '', line.strip())
                    if line:
                        path.append(line.strip())
            os.environ['MODULEPATH'] = ':'.join(path)

    @staticmethod
    def clear_loadedmodules():
        if 'LOADEDMODULES' not in os.environ:
            os.environ['LOADEDMODULES'] = ''

    @staticmethod
    def parse_stderr(stderr: bytes) -> tp.List[str]:
        return re.findall(MODULE_RE, stderr.decode('utf-8'))

    @property
    def cmd(self):
        return [MODCULE_CMD, 'python']

    def _run_cmd(self, args) -> subprocess.CompletedProcess:
        return subprocess.run(self.cmd + args,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              check=True,
                              shell=False)

    def list(self) -> tp.List[str]:
        proc_res = self._run_cmd(['list'])
        if proc_res.stderr:
            return self.parse_stderr(proc_res.stderr)
        return []

    def __call__(self, arg: tp.Union[str, tp.List[str]],
                 *args: str) -> tp.List[str]:
        cmd_args: tp.Union[None, tp.List[str]] = None
        if isinstance(arg, (list)):
            cmd_args = arg
        else:
            cmd_args = list((arg, ) + args)

        proc_res = self._run_cmd(cmd_args)
        if proc_res.stdout:
            ccode = compile(proc_res.stdout, filename='<strip>', mode='exec')
            exec(ccode)
        return self.list()
