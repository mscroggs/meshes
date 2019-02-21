from .core import Mesh
from math import sqrt

class Hemisphere(Mesh):
    def geo(self):
        return SphereWithFace(h=self.h, height=0).geo()

class SphereWithFace(Mesh):
    def geo(self):
        x = self.kwargs["height"] if "height" in self.kwargs else 0.5
        y = sqrt(1-x**2)

        if x > 0:

            geo = """
                Point(1) = {0,0,0,lc};
                Point(3) = {0,1,0,lc};
                Point(4) = {-1,0,0,lc};
                Point(5) = {0,-1,0,lc};
                Point(6) = {0,0,-1,lc};
                Point(7) = {0,0,1,lc};
            """
            geo += "Point(9) = {" + str(x) + "," + str(y) + ",0,lc};\n"
            geo += "Point(10) = {" + str(x) + ",0," + str(y) + ",lc};\n"
            geo += "Point(11) = {" + str(x) + "," + str(-y) + ",0,lc};\n"
            geo += "Point(12) = {" + str(x) + ",0," + str(-y) + ",lc};\n"
            geo += "Point(13) = {" + str(x) + ",0,0,lc};\n"
            geo += """
                Circle(1) = {9,1,3};
                Circle(2) = {3,1,4};
                Circle(3) = {4,1,5};
                Circle(4) = {5,1,11};
                Circle(5) = {3,1,6};
                Circle(6) = {6,1,5};
                Circle(7) = {5,1,7};
                Circle(8) = {7,1,3};
                Circle(9) = {10,1,7};
                Circle(10) = {7,1,4};
                Circle(11) = {4,1,6};
                Circle(12) = {6,1,12};

                Circle(13) = {9,13,10};
                Circle(14) = {10,13,11};
                Circle(15) = {11,13,12};
                Circle(16) = {12,13,9};

                Line Loop(13) = {2,8,-10};
                Ruled Surface(14) = {13};
                Line Loop(15) = {10,3,7};
                Ruled Surface(16) = {15};
                Line Loop(17) = {-8,-9,-13,1};
                Ruled Surface(18) = {17};
                Line Loop(19) = {-11,-2,5};
                Ruled Surface(20) = {19};
                Line Loop(21) = {-5,-12,-1,-16};
                Ruled Surface(22) = {21};
                Line Loop(23) = {-3,11,6};
                Ruled Surface(24) = {23};
                Line Loop(25) = {-7,4,-14,9};
                Ruled Surface(26) = {25};
                Line Loop(27) = {-4,-15,12,-6};
                Ruled Surface(28) = {27};

                Line Loop(29) = {13,14,15,16};
                Surface(30) = {29};



                Physical Surface(1) = {14};
                Physical Surface(2) = {16};
                Physical Surface(3) = {18};
                Physical Surface(4) = {20};
                Physical Surface(5) = {22};
                Physical Surface(6) = {24};
                Physical Surface(7) = {26};
                Physical Surface(8) = {28};
                Physical Surface(9) = {30};

                Surface Loop(29) = {28,26,16,14,20,24,22,18,30};
                Volume(30) = {29};
            """
        else:
            geo = """
                Point(1) = {0,0,0,lc};
                Point(4) = {-1,0,0,lc};
            """
            geo += "Point(9) = {" + str(x) + "," + str(y) + ",0,lc};\n"
            geo += "Point(10) = {" + str(x) + ",0," + str(y) + ",lc};\n"
            geo += "Point(11) = {" + str(x) + "," + str(-y) + ",0,lc};\n"
            geo += "Point(12) = {" + str(x) + ",0," + str(-y) + ",lc};\n"
            geo += "Point(13) = {" + str(x) + ",0,0,lc};\n"
            geo += """
                Circle(1) = {4,1,9};
                Circle(2) = {4,1,10};
                Circle(3) = {4,1,11};
                Circle(4) = {4,1,12};

                Circle(13) = {9,13,10};
                Circle(14) = {10,13,11};
                Circle(15) = {11,13,12};
                Circle(16) = {12,13,9};

                Line Loop(1) = {2,-13,-1};
                Line Loop(2) = {3,-14,-2};
                Line Loop(3) = {4,-15,-3};
                Line Loop(4) = {1,-16,-4};
                Line Loop(5) = {13,14,15,16};

                Ruled Surface(1) = {1};
                Ruled Surface(2) = {2};
                Ruled Surface(3) = {3};
                Ruled Surface(4) = {4};
                Ruled Surface(5) = {5};

                Physical Surface(1) = {1};
                Physical Surface(2) = {2};
                Physical Surface(3) = {3};
                Physical Surface(4) = {4};
                Physical Surface(5) = {5};

                Surface Loop(1) = {1,2,3,4,5};
                Volume(1) = {1};
            """

        return geo

