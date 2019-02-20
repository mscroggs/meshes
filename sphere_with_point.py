from .core import Mesh
from math import pi,sin,cos

class SphereWithPoint(Mesh):
    def geo(self):
        angle = self.kwargs["angle"] if "angle" in self.kwargs else pi/2
        height = self.kwargs["height"] if "height" in self.kwargs else 0
        dist = 1/sin(angle/2)
        x = cos(pi/2-angle/2)
        y = sin(pi/2-angle/2)

        geo = """
            Point(1) = {0,0,0,lc};
            Point(3) = {0,1,0,lc};
            Point(4) = {-1,0,0,lc};
            Point(6) = {0,0,-1,lc};
            Point(7) = {0,0,1,lc};
        """

        geo += "Point(8) = {" + str(dist) + ",0,0,lc};\n"
        geo += "Point(9) = {" + str(x) + "," + str(y) + ",0,lc};\n"
        geo += "Point(10) = {" + str(x) + ",0," + str(y) + ",lc};\n"
        geo += "Point(12) = {" + str(x) + ",0," + str(-y) + ",lc};\n"
        geo += "Point(13) = {" + str(x) + ",0,0,lc};\n"

        geo += """
            Circle(1) = {9,1,3};
            Circle(2) = {3,1,4};
            Circle(5) = {3,1,6};
            Circle(8) = {7,1,3};
            Circle(9) = {10,1,7};
            Circle(10) = {7,1,4};
            Circle(11) = {4,1,6};
            Circle(12) = {6,1,12};

            Circle(13) = {9,13,10};
            Circle(16) = {12,13,9};

            Line(17) = {9,8};
            Line(18) = {10,8};
            Line(20) = {12,8};

            Line Loop(13) = {2,8,-10};
            Ruled Surface(14) = {13};
            Line Loop(17) = {-8,-9,-13,1};
            Ruled Surface(18) = {17};
            Line Loop(19) = {-11,-2,5};
            Ruled Surface(20) = {19};
            Line Loop(21) = {-5,-12,-1,-16};
            Ruled Surface(22) = {21};


            Line Loop(29) = {18,-17,13};
            Ruled Surface(30) = {29};
            Line Loop(35) = {17,-20,16};
            Ruled Surface(36) = {35};


            Physical Surface(1) = {14};
            Physical Surface(3) = {18};
            Physical Surface(4) = {20};
            Physical Surface(5) = {22};
            Physical Surface(9) = {30};
            Physical Surface(12) = {36};
        """
        if height == 0:
            geo += "Point(5) = {0,-1,0,lc};\n"
            geo += "Point(11) = {" + str(x) + "," + str(-y) + ",0,lc};\n"
            geo += """
                Circle(3) = {4,1,5};
                Circle(4) = {5,1,11};
                Circle(6) = {6,1,5};
                Circle(7) = {5,1,7};

                Circle(14) = {10,13,11};
                Circle(15) = {11,13,12};

                Line(19) = {11,8};

                Line Loop(15) = {10,3,7};
                Ruled Surface(16) = {15};
                Line Loop(23) = {-3,11,6};
                Ruled Surface(24) = {23};
                Line Loop(25) = {-7,4,-14,9};
                Ruled Surface(26) = {25};
                Line Loop(27) = {-4,-15,12,-6};
                Ruled Surface(28) = {27};

                Line Loop(31) = {19,-18,14};
                Ruled Surface(32) = {31};
                Line Loop(33) = {20,-19,15};
                Ruled Surface(34) = {33};


                Physical Surface(2) = {16};
                Physical Surface(6) = {24};
                Physical Surface(7) = {26};
                Physical Surface(8) = {28};
                Physical Surface(10) = {32};
                Physical Surface(11) = {34};
            """
            geo += """
                Surface Loop(29) = {28,26,16,14,20,24,22,18,30,32,34,36};
                Volume(30) = {29};
            """
        else:
            geo += "height = "+str(height)+";\n"
            geo += """
                Point(21) = {0,-height,0,lc};
                Point(23) = {0,-height-1,0,lc};
                Point(24) = {-1,-height,0,lc};
                Point(26) = {0,-height,1,lc};
                Point(27) = {0,-height,-1,lc};
            """

            geo += "Point(28) = {" + str(dist) + ",-height,0,lc};\n"
            geo += "Point(29) = {" + str(x) + ",-height-" + str(y) + ",0,lc};\n"
            geo += "Point(30) = {" + str(x) + ",-height," + str(-y) + ",lc};\n"
            geo += "Point(32) = {" + str(x) + ",-height," + str(y) + ",lc};\n"
            geo += "Point(33) = {" + str(x) + ",-height,0,lc};\n"

            geo += """
                Circle(21) = {29,21,23};
                Circle(22) = {23,21,24};
                Circle(25) = {23,21,26};
                Circle(28) = {27,21,23};
                Circle(29) = {30,21,27};
                Circle(30) = {27,21,24};
                Circle(31) = {24,21,26};
                Circle(32) = {26,21,32};

                Circle(33) = {29,33,30};
                Circle(36) = {32,33,29};

                Line(37) = {29,28};
                Line(38) = {30,28};
                Line(40) = {32,28};

                Line Loop(113) = {22,28,-30};
                Ruled Surface(114) = {113};
                Line Loop(117) = {-28,-29,-33,21};
                Ruled Surface(118) = {117};
                Line Loop(119) = {-31,-22,25};
                Ruled Surface(120) = {119};
                Line Loop(121) = {-25,-32,-21,-36};
                Ruled Surface(122) = {121};


                Line Loop(129) = {38,-37,33};
                Ruled Surface(130) = {129};
                Line Loop(135) = {37,-40,36};
                Ruled Surface(136) = {135};


                Physical Surface(2) = {114};
                Physical Surface(6) = {118};
                Physical Surface(7) = {120};
                Physical Surface(8) = {122};
                Physical Surface(10) = {130};
                Physical Surface(11) = {136};
            """

            geo += """
                Line(200) = {4,24};
                Line(201) = {6,27};
                Line(202) = {7,26};
                Line(203) = {8,28};
                Line(204) = {10,32};
                Line(205) = {12,30};

                Line Loop(200) = {200,31,-202,10};
                Line Loop(201) = {202,32,-204,9};
                Line Loop(202) = {204,40,-203,-18};
                Line Loop(203) = {203,-38,-205,20};
                Line Loop(204) = {205,29,-201,12};
                Line Loop(205) = {201,30,-200,11};
            """
            for i in range(6):
                geo += "Ruled Surface("+str(200+2*i)+") = {"+str(200+i)+"};\n"
                geo += "Physical Surface("+str(13+i)+") = {"+str(200+2*i)+"};\n"

            geo += """
                Surface Loop(29) = {14,14,20,22,30,36,114,118,120,122,130,136,200,202,204,206,208,210};
                Volume(30) = {29};
            """


        return geo

