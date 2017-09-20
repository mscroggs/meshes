import cake as _cake
import christmas as _christmas
from bempp.api.shapes.shapes import __generate_grid_from_geo_string

def cake(h=0.1):
    return __generate_grid_from_geo_string(_cake.cake(h))

def christmas_tree(h=0.1):
    return __generate_grid_from_geo_string(_christmas.tree(h))
