from .core import Mesh

class Apple(Mesh):
    def geo(self):
        # Inner cylinder
        # R is big radius of handle
        # r is small radius of handle
        # th is thickness of sides
        # dep is depth of middle
        geo = "R = 1.2;r = 0.3;th=0.3;dep=2;\n"
        geo += """
                Point(1) = {1.3,0,0,lc};
                Point(2) = {1.3,0,3.3,lc};
                Point(3) = {0,0,2.41,lc};
                Point(4) = {0.51,0,-3,lc};
                Point(5) = {3.2,0,0,lc};
                Point(6) = {0,0,0,lc};
                Point(7) = {0,0,-3,lc};

                Point(11) = {0,1.3,0,lc};
                Point(12) = {0,1.3,3.3,lc};
                Point(14) = {0,0.51,-3,lc};
                Point(15) = {0,3.2,0,lc};

                Point(21) = {-1.3,0,0,lc};
                Point(22) = {-1.3,0,3.3,lc};
                Point(24) = {-0.51,0,-3,lc};
                Point(25) = {-3.2,0,0,lc};

                Point(31) = {0,-1.3,0,lc};
                Point(32) = {0,-1.3,3.3,lc};
                Point(34) = {0,-0.51,-3,lc};
                Point(35) = {0,-3.2,0,lc};

                Ellipse(1) = {3,1,2,5};
                Ellipse(2) = {4,1,2,5};
                Ellipse(11) = {3,11,12,15};
                Ellipse(12) = {14,11,12,15};
                Ellipse(21) = {3,21,22,25};
                Ellipse(22) = {24,21,22,25};
                Ellipse(31) = {3,31,32,35};
                Ellipse(32) = {34,31,32,35};

                Circle(3) = {4,7,14};
                Circle(4) = {14,7,24};
                Circle(5) = {24,7,34};
                Circle(6) = {34,7,4};

                Circle(7) = {5,6,15};
                Circle(8) = {15,6,25};
                Circle(9) = {25,6,35};
                Circle(10) = {35,6,5};

                Line Loop(1) = {-6,-5,-4,-3};
                Line Loop(2) = {3,12,-7,-2};
                Line Loop(3) = {4,22,-8,-12};
                Line Loop(4) = {5,32,-9,-22};
                Line Loop(5) = {6,2,-10,-32};
                Line Loop(6) = {7,-11,1};
                Line Loop(7) = {8,-21,11};
                Line Loop(8) = {9,-31,21};
                Line Loop(9) = {10,-1,31};

                Ruled Surface(1) = {1};
                Ruled Surface(2) = {2};
                Ruled Surface(3) = {3};
                Ruled Surface(4) = {4};
                Ruled Surface(5) = {5};
                Ruled Surface(6) = {6};
                Ruled Surface(7) = {7};
                Ruled Surface(8) = {8};
                Ruled Surface(9) = {9};

                """
        return geo

