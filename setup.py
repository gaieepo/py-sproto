from distutils.core import setup, Extension

module1 = Extension('pysproto',
                    sources = ['pysproto.c', "clib/sproto.c"])

setup (name = 'PackageName',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])
