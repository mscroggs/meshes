class Mesh(object):
    def __init__(self, h=0.1, **kwargs):
        self.kwargs = kwargs
        self.h = h

    def as_bempp_grid(self):
        from bempp.api.shapes.shapes import __generate_grid_from_geo_string
        __generate_grid_from_geo_string(self.as_geo_string)

    def as_geo_string(self):
        geo =  "lc = " + str(self.h) + ";"
        geo += self.geo()
        geo += "\nMesh.Algorithm = 6;"
        return geo

    def geo(self):
        raise NotImplementedError
