from .core import Mesh
from math import sqrt

class RoundedCube(Mesh):
    def geo(self):
        r = self.kwargs["radius"] if "radius" in self.kwargs else 0.2
        if r == 0:
            geo = """
                Point(1) = {0,0,0,lc};
                Point(2) = {1,0,0,lc};
                Point(3) = {1,1,0,lc};
                Point(4) = {0,1,0,lc};
                Point(5) = {0,0,1,lc};
                Point(6) = {1,0,1,lc};
                Point(7) = {1,1,1,lc};
                Point(8) = {0,1,1,lc};

                Line(1) = {1,2};
                Line(2) = {2,3};
                Line(3) = {3,4};
                Line(4) = {4,1};
                Line(5) = {5,6};
                Line(6) = {6,7};
                Line(7) = {7,8};
                Line(8) = {8,5};
                Line(9) = {1,5};
                Line(10) = {2,6};
                Line(11) = {3,7};
                Line(12) = {4,8};

                Line Loop(1) = {-4,-3,-2,-1};
                Line Loop(2) = {5,6,7,8};
                Line Loop(3) = {1,10,-5,-9};
                Line Loop(4) = {2,11,-6,-10};
                Line Loop(5) = {3,12,-7,-11};
                Line Loop(6) = {4,9,-8,-12};
            """
            for i in range(1,7):
                geo += "Plane Surface("+str(i)+") = {"+str(i)+"};\n"
                geo += "Physical Surface("+str(i)+") = {"+str(i)+"};\n"
            geo += """
                Surface Loop(1) = {1,2,3,4,5,6};
                Volume(1) = {1};
            """
            return geo


        geo = ""

        for i,points in enumerate([
                    [(r,r,0),(r,1-r,0),(1-r,1-r,0),(1-r,r,0)],
                    [(r,r,1),(r,1-r,1),(1-r,1-r,1),(1-r,r,1)][::-1],
                    [(r,0,r),(r,0,1-r),(1-r,0,1-r),(1-r,0,r)][::-1],
                    [(r,1,r),(r,1,1-r),(1-r,1,1-r),(1-r,1,r)],
                    [(0,r,r),(0,r,1-r),(0,1-r,1-r),(0,1-r,r)],
                    [(1,r,r),(1,r,1-r),(1,1-r,1-r),(1,1-r,r)][::-1]
                ]):
            for j,p in enumerate(points):
                geo += "Point("+str(i*4+j+1)+") = {"+str(p[0])+","+str(p[1])+","+str(p[2])+",lc};\n"
            for j in range(4):
                geo += "Line("+str(i*4+j+1)+") = {"+str(i*4+j+1)+","+str(i*4+(j+1)%4+1)+"};\n"
            geo += "Line Loop("+str(i+1)+") = {"+(",".join(str(i*4+j+1) for j in range(4)))+"};\n"
            geo += "Plane Surface("+str(i+1)+") = {"+str(i+1)+"};\n"
            geo += "Physical Surface("+str(i+1)+") = {"+str(i+1)+"};\n"


        for i,(p,points) in enumerate([
                    [(r,r,r),(1,12,17)],
                    [(r,r,1-r),(18,11,8)],
                    [(r,1-r,r),(13,2,20)],
                    [(r,1-r,1-r),(14,19,7)],
                    [(1-r,r,r),(24,9,4)],
                    [(1-r,r,1-r),(5,10,23)],
                    [(1-r,1-r,r),(16,21,3)],
                    [(1-r,1-r,1-r),(15,6,22)]
                ]):
            geo += "Point("+str(25+i)+") = {"+str(p[0])+","+str(p[1])+","+str(p[2])+",lc};\n"
            for j,(a,b) in enumerate(zip(points,points[1:] + points[:1])):
                geo += "Circle("+str(25+i*3+j)+") = {"+str(a)+","+str(25+i)+","+str(b)+"};\n"
            geo += "Line Loop("+str(7+i)+") = {"+str(25+i*3)+","+str(26+i*3)+","+str(27+i*3)+"};\n"
            geo += "Ruled Surface("+str(7+i)+") = {"+str(7+i)+"};\n"
            geo += "Physical Surface("+str(7+i)+") = {"+str(7+i)+"};\n"

        for i,edges in enumerate([
                    [-29,-10,-40,-8],
                    [-14,-36,-6,-46],
                    [-2,-31,-16,-45],
                    [-12,-25,-4,-38],
                    [-9,-37,-23,-41],
                    [-17,-26,-11,-28],
                    [-13,-33,-19,-34],
                    [-21,-43,-15,-48],
                    [-22,-47,-5,-42],
                    [-3,-44,-24,-39],
                    [-20,-32,-1,-27],
                    [-7,-35,-18,-30]
                ]):

            geo += "Line Loop("+str(15+i)+") = {"+(",".join(str(j) for j in edges))+"};\n"
            geo += "Ruled Surface("+str(15+i)+") = {"+str(15+i)+"};\n"
            geo += "Physical Surface("+str(15+i)+") = {"+str(15+i)+"};\n"

        geo2 = """
            Point(1) = {0,0,0,lc};
            Point(2) = {1,0,0,lc};
            Point(3) = {1,1,0,lc};
            Point(4) = {0,1,0,lc};
            Point(5) = {0,0,1,lc};
            Point(6) = {1,0,1,lc};
            Point(7) = {1,1,1,lc};
            Point(8) = {0,1,1,lc};

            Line(1) = {1,2};
            Line(2) = {2,3};
            Line(3) = {3,4};
            Line(4) = {4,1};
            Line(5) = {5,6};
            Line(6) = {6,7};
            Line(7) = {7,8};
            Line(8) = {8,5};
            Line(9) = {1,5};
            Line(10) = {2,6};
            Line(11) = {3,7};
            Line(12) = {4,8};

            Line Loop(1) = {-4,-3,-2,-1};
            Line Loop(2) = {5,6,7,8};
            Line Loop(3) = {1,10,-5,-9};
            Line Loop(4) = {2,11,-6,-10};
            Line Loop(5) = {3,12,-7,-11};
            Line Loop(6) = {4,9,-8,-12};
        """
        for i in range(1,7):
            geo2 += "Plane Surface("+str(i)+") = {"+str(i)+"};\n"
            geo2 += "Ruled Surface("+str(6+i)+") = {"+str(i)+"};\n"
        geo2 += """
            Surface Loop(1) = {7,8,9,10,11,12};
            Volume(1) = {1};
        """
        return geo
