#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse as _argparse
import datetime as _dt
import sys as _sys
import os as _os

from app import create_app

_DESCRIPTION_MSG = """ """

_EPILOG_MSG = '''
    Examples:
'''

class MainArgParse(object):
    
    def __init__(self):
        
        self._g_help = False
        self.__verbose__ = False
        
        self._subparser_name = None
        
        self.configuration = ''
        self.port = 1234
        
        psr = _argparse.ArgumentParser(prog=__file__,
                                       description=_DESCRIPTION_MSG,
                                       epilog=_EPILOG_MSG,
                                       formatter_class=_argparse.RawTextHelpFormatter)
        
        self._add_generic_args(psr)
        
        self._add_subparser(psr)
        
        if len(_sys.argv) == 1:
            psr.print_help()
            _sys.exit()
            
        psr.parse_args(args=self._sort_args(), namespace=self)
            
            
    def apply(self):
        if self._subparser_name == 'prod':
            print("Launching Production App!")
            self.app = create_app('PROD')
        elif self._subparser_name == 'dev':
            print("Launching Development App!")
            self.app = create_app('DEV')
            
        self.port = self.app.config['PORT']
            
    def _add_subparser(self, psr):
        
        sub = psr.add_subparsers(dest='_subparser_name',
                                 metavar='sub_commands',
                                 help='this is help')

        prod = sub.add_parser('prod', help='launch production app')
        dev = sub.add_parser('dev', help='launch devlopment app')
        
        self._sub_list = [ prod, dev ]
        
        for item in self._sub_list:
            self._add_generic_args(item)
            
            
    @staticmethod
    def _add_generic_args(psr):
        
        psr.add_argument('-v', '--verbose', dest="__verbose__", action="store_true", 
                 default=False, help='enable verbose output debug')
        
    def _sort_args(self):
        
        """
        Move all subparsers to the front
        """
        
        sub_names = [x.prog.split()[1] for x in self._sub_list ]
        
        sargs = _sys.argv[1:]
        
        for f in sub_names:
            if f in sargs:
                sargs.remove(f)
                sargs.insert(0,f)
        return sargs
        
    def __str__(self):
        
        return '\n'.join(['Class info goes here!'])
    
    
##############################################################################
if __name__ == '__main__':
    
    """
    Main script entry point
    """
    
    _tb = _dt.datetime.now()
    
    _arg = MainArgParse()
    
    _arg.apply()
    
    _arg.app.run( port=_arg.port)
    
  