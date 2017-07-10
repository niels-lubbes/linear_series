'''
Use of this source code is governed by a MIT-style license that can be found in the LICENSE file.
Created on Jul 6, 2017
@author: Niels Lubbes
'''
from sage.all import *

from linear_series.class_ls_tools import LSTools
from linear_series.class_poly_ring import *
from linear_series.class_linear_series import *


class TestGetBasePointTree:


    def test__get_base_point_tree( self ):
        ring = PolyRing( 'x,y,z', True )
        ring.ext_num_field( 't^2 + 1' )
        ring.ext_num_field( 't^3 + a0' )

        ls = LinearSeries( ['x^2+a0*y*z', 'y+a1*z+x' ], ring )

        out = str( ls.get_bp_tree() )
        chk = """
            { 2, <<x^2 + a0*y*z, x + y + a1*z>>, QQ( <a0|t^2 + 1>, <a1|t^2 + a0*t - 1>, <a2|t^2 - a0*t - a0*a1> )[x, y, z] }
            chart=z, depth=0, mult=1, sol=(-a2 + a0, a2 - a1 - a0), { 2, <<x^2 + a0*y, x + y + a1>>, QQ( <a0|t^2 + 1>, <a1|t^2 + a0*t - 1>, <a2|t^2 - a0*t - a0*a1> )[x, y] }
            chart=z, depth=0, mult=1, sol=(a2, -a2 - a1), { 2, <<x^2 + a0*y, x + y + a1>>, QQ( <a0|t^2 + 1>, <a1|t^2 + a0*t - 1>, <a2|t^2 - a0*t - a0*a1> )[x, y] }
            """

        while '  ' in out or '\t' in out:
            out = out.replace( '  ', ' ' )
            out = out.replace( '\t', ' ' )

        while '  ' in chk or '\t' in chk:
            chk = chk.replace( '  ', ' ' )
            chk = chk.replace( '\t', ' ' )
        chk = chk[0:-2]

        assert out == chk


if __name__ == '__main__':

    # LSTools.filter( 'test_get_linear_series.py' )
    # TestGetBasePointTree().test__get_base_point_tree()

    pass