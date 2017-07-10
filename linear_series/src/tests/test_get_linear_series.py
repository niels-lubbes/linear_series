'''
Use of this source code is governed by a MIT-style license that can be found in the LICENSE file.
Created on Jul 6, 2017
@author: Niels Lubbes
'''
from sage.all import *


from linear_series.class_poly_ring import *
from linear_series.class_base_points import *
from linear_series.class_linear_series import *


class TestGetLinearSeries:


    def test__get_mon_lst__2_xyz( self ):
        mon_lst = get_mon_lst( 2, PolyRing( 'x,y,z' ).gens() )
        assert str( mon_lst ) == '[x^2, x*y, x*z, y^2, y*z, z^2]'


    def test__get_mon_lst__1_xyvw( self ):
        mon_lst = get_mon_lst( 1, PolyRing( 'x,y,v,w' ).gens() )
        assert str( mon_lst ) == '[x*v, x*w, y*v, y*w]'


    def test__get_mon_lst__2_xyvw( self ):
        mon_lst = get_mon_lst( 2, PolyRing( 'x,y,v,w' ).gens() )
        assert str( mon_lst ) == '[x^2*v^2, x^2*v*w, x^2*w^2, x*y*v^2, x*y*v*w, x*y*w^2, y^2*v^2, y^2*v*w, y^2*w^2]'


    def test__get_linear_series__1( self ):

        # Example from phd thesis of Niels Lubbes (page 159).
        bp_tree = BasePointTree()
        bp = bp_tree.add( 'z', ( 0, 0 ), 1 )
        bp = bp.add( 't', ( 0, 0 ), 1 )
        bp = bp.add( 't', ( -1, 0 ), 1 )
        bp = bp.add( 't', ( 0, 0 ), 1 )

        ls = LinearSeries.get( 2, bp_tree )

        assert str( ls ) == '{ 2, <<x^2, y^2 + x*z>>, QQ[x, y, z] }'


if __name__ == '__main__':

    # LSTools.filter( 'test_get_linear_series.py' )
    # TestGetLinearSeries().test__get_mon_lst__2_xyz()
    # TestGetLinearSeries().test__get_mon_lst__1_xyvw()
    # TestGetLinearSeries().test__get_mon_lst__2_xyvw()
    # TestGetLinearSeries().test__get_linear_series__1()

    pass