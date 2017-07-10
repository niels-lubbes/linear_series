'''
Use of this source code is governed by a MIT-style license that can be found in the LICENSE file.
Created on Jul 06, 2017
@author: Niels Lubbes
'''
from sage.all import *

import inspect
import time
import sys


class LSTools():
    '''
    For accessing static variables in python see for example:
    <http://stackoverflow.com/questions/68645/static-class-variables-in-python>    
    '''

    # Private dictionary object for caching result
    # used by ".get_tool_dct()" and ".save_tool_dct()".
    # If "enable_tool_dct" is false then caching in
    # disabled. This is useful for example in test
    # methods. However, it should be noted that it
    # could take a long time to compute the data.
    #
    __tool_dct = None
    __enable_tool_dct = True

    # private variable for timer
    #
    __start_time = None
    __end_time = None

    # private static variables used by ".verbose()"
    #
    __filter_fname = None
    __prev_filter_fname = None


    @staticmethod
    def filter( filter_fname ):
        '''
        It is adviced to access this method 
        as LSTools.filter().  
        
        INPUT:
            - "filter_fname" -- File name 
        '''
        LSTools.__filter_fname = filter_fname
        LSTools.__prev_filter_fname = filter_fname


    @staticmethod
    def filter_unset():
        '''
        Output via ".p()" will not be surpressed.
        '''
        LSTools.__filter_fname = None


    @staticmethod
    def filter_reset():
        '''
        Resets filter state to before previous ".filter_unset()" call.
        '''
        LSTools.__filter_fname = LSTools.__prev_filter_fname


    @staticmethod
    def p( *arg_lst ):
        '''
        INPUT:
            - "*arg_lst" -- List of arguments.
        OUTPUT:
            - If ".filter_on(<fname>)" has been called and the file name
              of the calling module does not coincide with <fname>
              then the output is surpressed and "None" is returned.
                            
              Otherwise, this method prints arguments to "sys.stdout" 
              together with reflection info from "inspect.stack()".
              Additional returns the output string.
              
              Call ".filter_off()" to turn off filter, such that
              all output is send to "sys.stdout".  
                                   
        '''
        # collect relevant info from stack trace
        sk_lst_lst = inspect.stack()
        file_name = str( sk_lst_lst[1][1] )
        line = str( sk_lst_lst[1][2] )
        method_name = str( sk_lst_lst[1][3] )

        # only output when op is called from "op.input_file_name"
        if LSTools.__filter_fname != None:
            if not file_name.endswith( LSTools.__filter_fname ):
                return

        # construct output string
        s = method_name + '(' + line + ')' + ': '
        for arg in arg_lst:
            s += str( arg ) + ' '

        # print output
        print( s )
        sys.stdout.flush()

        return s


    @staticmethod
    def set_enable_tool_dct( enable_tool_dct ):
        LSTools.__enable_tool_dct = enable_tool_dct


    @staticmethod
    def get_tool_dct( fname = 'ls_tools' ):
        '''
        INPUT:
            - "fname" -- Name of file without extension.
        OUTPUT:
            - Sets static private variable "__tool_dct" 
              in memory from file "<local path>/<fname>.sobj"
              if called for the first time.
              
            - Returns ".__tool_dct" if ".__enable_tool_dct==True" 
              and "{}" otherwise.
        '''
        if not LSTools.__enable_tool_dct:
            LSTools.filter_unset()
            LSTools.p( 'Caching is disabled!' )
            LSTools.filter_reset()
            return {}

        path = os.path.dirname( os.path.abspath( __file__ ) ) + '/'
        file_name = path + fname
        if LSTools.__tool_dct == None:

            LSTools.filter_unset()
            try:

                LSTools.p( 'Loading from:', file_name )
                LSTools.__tool_dct = load( file_name )

            except Exception as e:

                LSTools.p( 'Cannot load ".__tool_dct": ', e )
                LSTools.__tool_dct = {}

            LSTools.filter_reset()

        return LSTools.__tool_dct


    @staticmethod
    def save_tool_dct( fname = 'ls_tools' ):
        '''
        INPUT:
            - "fname" -- Name of file without extension.        
        OUTPUT:
            - Saves ".__tool_dct" to  "fname" if ".enable_tool_dct==True" 
              otherwise do nothing.
        '''
        if not LSTools.__enable_tool_dct:
            LSTools.filter_unset()
            LSTools.p( 'Data is not saved to disk!' )
            LSTools.filter_reset()
            return

        path = os.path.dirname( os.path.abspath( __file__ ) ) + '/'
        file_name = path + fname

        LSTools.filter_unset()
        LSTools.p( 'Saving to:', file_name )
        LSTools.filter_reset()

        save( LSTools.__tool_dct, file_name )


    @staticmethod
    def start_timer():
        '''
        OUTPUT:
            - Prints the current time and starts timer.
        '''
        # get time
        LSTools.__start_time = time.clock()  # set static variable.

        LSTools.filter_unset()
        LSTools.p( 'start time =', LSTools.__start_time )
        LSTools.filter_reset()


    @staticmethod
    def stop_timer():
        '''
        OUTPUT:
            - Prints time passed since last call of ".start_timer()".
        '''
        LSTools.__end_time = time.clock()
        passed_time = LSTools.__end_time - LSTools.__start_time

        LSTools.filter_unset()
        LSTools.p( 'time passed =', passed_time )
        LSTools.filter_reset()




