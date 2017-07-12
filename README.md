# Linear series 


## Introduction

Linear series is a Python library for base point analysis for linear series of curves in the plane. 
This library depends on [SageMath](https://SageMath.org) libraries.

## Installation

* Install Sage from [SageMath](https://SageMath.org) 

* Type the following commands in your commandline. 
We assume that `sage` is accessible from your commandline interface.
```    
sage -pip install linear_series
```    

* To execute some [usecases](https://github.com/niels-lubbes/linear_series/blob/master/linear_series/src/linear_series/__main__.py) type
```    
sage -python -m linear_series
```

* The following commands show which files were installed and
how to upgrade the linear series package.
```
sage -pip show --files linear_series
sage -pip install --upgrade linear_series
```

## Examples

See also [this file](https://github.com/niels-lubbes/linear_series/blob/master/linear_series/src/linear_series/__main__.py) 
for example usecases. 

For running the examples below, either copy paste the code into the Sage interface or run them as a Python module:

    sage -python -m my_module_name.py


__Example 1: Base point analysis of linear series of curves in projective plane__
```python
from linear_series.class_poly_ring import PolyRing
from linear_series.class_linear_series import LinearSeries    
ls = LinearSeries( ['x^2', 'x*z + y^2'], PolyRing( 'x,y,z', True ) )
bp_tree = ls.get_bp_tree()
print( bp_tree )
```
Output:

    { 2, <<x^2, y^2 + x*z>>, QQ[x, y, z] }
    chart=z, depth=0, mult=1, sol=(0, 0), { 2, <<x^2, y^2 + x>>, QQ[x, y] }
        chart=t, depth=1, mult=1, sol=(0, 0), { 2, <<x^2*y, x + y>>, QQ[x, y] }
            chart=t, depth=2, mult=1, sol=(-1, 0), { 2, <<x^2*y^2, x + 1>>, QQ[x, y] }
                chart=t, depth=3, mult=1, sol=(0, 0), { 2, <<x^2*y^3 - 2*x*y^2 + y, x>>, QQ[x, y] } 

__Example 2: Base point analysis of linear series defined over number field__
```python
from linear_series.class_poly_ring import PolyRing
from linear_series.class_linear_series import LinearSeries      
ring = PolyRing( 'x,y,z', True )
ring.ext_num_field( 't^2 + 1' )
ring.ext_num_field( 't^3 + a0' )
ls = LinearSeries( ['x^2+a0*y*z','y+a1*z+x'], ring )
bp_tree = ls.get_bp_tree()
print( bp_tree )
```
Output:

    { 2, <<x^2 + a0*y*z, x + y + a1*z>>, QQ( <a0|t^2 + 1>, <a1|t^2 + a0*t - 1>, <a2|t^2 - a0*t - a0*a1> )[x, y, z] }
    chart=z, depth=0, mult=1, sol=(-a2 + a0, a2 - a1 - a0), { 2, <<x^2 + a0*y, x + y + a1>>, QQ( <a0|t^2 + 1>, <a1|t^2 + a0*t - 1>, <a2|t^2 - a0*t - a0*a1> )[x, y] }
    chart=z, depth=0, mult=1, sol=(a2, -a2 - a1), { 2, <<x^2 + a0*y, x + y + a1>>, QQ( <a0|t^2 + 1>, <a1|t^2 + a0*t - 1>, <a2|t^2 - a0*t - a0*a1> )[x, y] } 

__Example 3: Base point analysis of linear series of curves in P^1xP^1__
```python
from linear_series.class_poly_ring import PolyRing
from linear_series.class_linear_series import LinearSeries      
ls = LinearSeries( ['x*v-y*w', 'y*v+x*w' ], PolyRing( 'x,y,v,w' ) )
bp_tree = ls.get_bp_tree()
print( bp_tree )
```    
Output:    
    
    { 2, <<x*v - y*w, y*v + x*w>>, QQ( <a0|t^2 + 1> )[x, y, v, w] }
    chart=xv, depth=0, mult=1, sol=(a0, (-a0)), { 2, <<-y*w + 1, y + w>>, QQ( <a0|t^2 + 1> )[y, w] }
    chart=xv, depth=0, mult=1, sol=(-a0, (a0)), { 2, <<-y*w + 1, y + w>>, QQ( <a0|t^2 + 1> )[y, w] } 

__Example 4: Creating linear series of degree 2 curves in the projective plane__
```python
from linear_series.class_poly_ring import PolyRing
from linear_series.class_base_points import BasePointTree
from linear_series.class_linear_series import LinearSeries   
PolyRing.reset_base_field()
bp_tree = BasePointTree()
bp = bp_tree.add( 'z', ( 0, 0 ), 1 )
bp = bp.add( 't', ( 0, 0 ), 1 )
bp = bp.add( 't', ( -1, 0 ), 1 )
bp = bp.add( 't', ( 0, 0 ), 1 )   
print( LinearSeries.get( 2, bp_tree ) )
```
Output:

    { 2, <<x^2, y^2 + x*z>>, QQ[x, y, z] }
__Example 5: Creating linear series of bi-degree (1,1) curves in P^1xP^1__     
```python
from linear_series.class_poly_ring import PolyRing
from linear_series.class_base_points import BasePointTree
from linear_series.class_linear_series import LinearSeries  
ring = PolyRing( 'x,y,v,w', True )
ring.ext_num_field( 't^2 + 1' )
a0 = ring.root_gens()[0]
bp_tree = BasePointTree( ['xv', 'xw', 'yv', 'yw'] )
bp = bp_tree.add( 'xv', ( -a0, a0 ), 1 )
bp = bp_tree.add( 'xv', ( a0, -a0 ), 1 )
print( LinearSeries.get( 1, bp_tree ) )
```    
Output:    
    
    { 2, <<x*v - y*w, y*v + x*w>>, QQ( <a0|t^2 + 1> )[x, y, v, w] }        

__Example 6: Implicitizing parametric image of linear series__

We first create a linear series of bi-degree (2,2) curves in P^1xP^1. We consider the resulting linear series 
defined by 7 homogeneous polynomials, as a map from P^1xP^1 into P^6. We implicitize the image of this map.
```python
from linear_series.class_poly_ring import PolyRing
from linear_series.class_base_points import BasePointTree
from linear_series.class_linear_series import LinearSeries  
ring = PolyRing( 'x,y,v,w', True )
ring.ext_num_field( 't^2 + 1' )
a0 = ring.root_gens()[0]
bp_tree = BasePointTree( ['xv', 'xw', 'yv', 'yw'] )
bp = bp_tree.add( 'xv', ( -a0, a0 ), 1 )
bp = bp_tree.add( 'xv', ( a0, -a0 ), 1 )
ls = LinearSeries.get( 2, bp_tree )
print( ls.get_implicit_image() )
```
Output:  

    [x3*x5 + x5^2 - x2*x6 - x4*x6, x4^2 + x5^2 - x2*x6, x3*x4 + x4*x5 - x1*x6 + x5*x6, x2*x4 - x1*x5 + x2*x6, x1*x4 - x0*x5 + x1*x6 - x5*x6, x3^2 - x5^2 - x0*x6 + x2*x6 + 2*x4*x6, x2*x3 - x0*x5 + x1*x6 - x5*x6, x1*x3 - x0*x4 - x4*x6, x1^2 - x0*x2 - x2*x6, x0*x5^2 + x2*x5^2 - x2^2*x6 - 2*x1*x5*x6 + x5^2*x6 + x2*x6^2, x0*x4*x5 + x1*x5^2 - x1*x2*x6 - x0*x5*x6 + x4*x5*x6 + x1*x6^2 - x5*x6^2] 

     
    