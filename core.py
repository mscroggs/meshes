try:
    from bempp.api.shapes.shapes import __generate_grid_from_geo_string as to_bempp
except ImportError:
    def to_bempp(string):
        raise ImportError("Could not import Bempp.")

class Mesh(object):
    def __init__(self, h=0.1, mesh_algorithm=1, **kwargs):
        self.kwargs = kwargs
        self.h = h
        self.mesh_algorithm = mesh_algorithm

    def as_bempp_grid(self):
        return to_bempp(self.as_geo_string())

    def as_geo_string(self):
        geo =  "lc = " + str(self.h) + ";"
        geo += self.geo()
        geo += "\nMesh.Algorithm = " + str(self.mesh_algorithm) + ";"
        return geo

    def geo(self):
        raise NotImplementedError
