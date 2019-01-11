from .core import Mesh

class Mug(Mesh):
    def geo(self):
        # Inner cylinder
        geo = "R = 1.7;\nr = 0.1;\n"
        geo += """
                Point(1) = {0,0,0,lc};
                Point(2) = {2,0,0,lc};
                Point(3) = {0,2,0,lc};
                Point(4) = {-2,0,0,lc};
                Point(5) = {0,-2,0,lc};

                Circle(1) = {2,1,3};
                Circle(2) = {3,1,4};
                Circle(3) = {4,1,5};
                Circle(4) = {5,1,2};

                Point(6) = {0,0,4,lc};
                Point(7) = {2,0,4,lc};
                Point(8) = {0,2,4,lc};
                Point(9) = {-2,0,4,lc};
                Point(10) = {0,-2,4,lc};

                Circle(5) = {7,6,8};
                Circle(6) = {8,6,9};
                Circle(7) = {9,6,10};
                Circle(8) = {10,6,7};

                Line Loop(12) = {5,6,7,8};

                Line Loop(1) = {1,2,3,4};
                Plane Surface(1) = {-1};

                Point(11) = {1.8,0,4,lc};
                Point(12) = {0,1.8,4,lc};
                Point(13) = {-1.8,0,4,lc};
                Point(14) = {0,-1.8,4,lc};

                Point(15) = {0,0,0.2,lc};
                Point(16) = {1.8,0,0.2,lc};
                Point(17) = {0,1.8,0.2,lc};
                Point(18) = {-1.8,0,0.2,lc};
                Point(19) = {0,-1.8,0.2,lc};

                Circle(13) = {11,6,12};
                Circle(14) = {12,6,13};
                Circle(15) = {13,6,14};
                Circle(16) = {14,6,11};

                Circle(17) = {16,15,17};
                Circle(18) = {17,15,18};
                Circle(19) = {18,15,19};
                Circle(20) = {19,15,16};

                Line(21) = {11,16};
                Line(22) = {12,17};
                Line(23) = {13,18};
                Line(24) = {14,19};

                Line Loop(6) = {13,14,15,16};
                Line Loop(7) = {17,18,19,20};
                Line Loop(8) = {13,22,-17,-21};
                Line Loop(9) = {14,23,-18,-22};
                Line Loop(10) = {15,24,-19,-23};
                Line Loop(11) = {16,21,-20,-24};

                Ruled Surface(2) = {12,6};
                Ruled Surface(3) = {7};
                Ruled Surface(4) = {8};
                Ruled Surface(5) = {9};
                Ruled Surface(6) = {10};
                Ruled Surface(7) = {11};
                """
        # Handle
        geo += """
                Point(20) = {2,0,2,lc};
                Point(21) = {2,0.1,2,lc};
                Point(22) = {2,-0.1,2,lc};

                Point(23) = {2,0,3.7,lc};
                Point(24) = {2,0,3.8,lc};
                Point(25) = {2,0.1,3.7,lc};
                Point(26) = {2,0,3.6,lc};
                Point(27) = {2,-0.1,3.7,lc};

                Circle(25) = {24,23,25};
                Circle(26) = {25,23,26};
                Circle(27) = {26,23,27};
                Circle(28) = {27,23,24};

                Point(28) = {2,0,0.3,lc};
                Point(29) = {2,0,0.2,lc};
                Point(30) = {2,0.1,0.3,lc};
                Point(31) = {2,0,0.4,lc};
                Point(32) = {2,-0.1,0.3,lc};

                Circle(29) = {29,28,30};
                Circle(30) = {30,28,31};
                Circle(31) = {31,28,32};
                Circle(32) = {32,28,29};

                Point(33) = {3.7,0,2,lc};
                Point(34) = {3.8,0,2,lc};
                Point(35) = {3.7,0.1,2,lc};
                Point(36) = {3.6,0,2,lc};
                Point(37) = {3.7,-0.1,2,lc};

                Circle(33) = {34,33,35};
                Circle(34) = {35,33,36};
                Circle(35) = {36,33,37};
                Circle(36) = {37,33,34};

                Circle(37) = {24,20,34};
                Circle(38) = {25,21,35};
                Circle(39) = {26,20,36};
                Circle(40) = {27,22,37};

                Circle(41) = {34,20,29};
                Circle(42) = {35,21,30};
                Circle(43) = {36,20,31};
                Circle(44) = {37,22,32};

                Line Loop(100) = {41,-32,-44,36};
                Line Loop(101) = {42,-29,-41,33};
                Line Loop(102) = {43,-30,-42,34};
                Line Loop(103) = {44,-31,-43,35};

                Ruled Surface(20) = {100};
                Ruled Surface(21) = {101};
                Ruled Surface(22) = {102};
                Ruled Surface(23) = {103};
                """
        # Outer cylinder
        geo += """

                Point(50) = {0,0,0.2,lc};
                Point(52) = {0,2,0.2,lc};
                Point(53) = {-2,0,0.2,lc};
                Point(54) = {0,-2,0.2,lc};

                Circle(50) = {29,50,52};
                Circle(51) = {52,50,53};
                Circle(52) = {53,50,54};
                Circle(53) = {54,50,29};

                Line(54) = {2,29};
                Line(55) = {3,52};
                Line(56) = {4,53};
                Line(57) = {5,54};

                Line Loop(50) = {54,50,-55,-1};
                Line Loop(51) = {55,51,-56,-2};
                Line Loop(52) = {56,52,-57,-3};
                Line Loop(53) = {57,53,-54,-4};

                Ruled Surface(8) = {50};
                Ruled Surface(9) = {51};
                Ruled Surface(10) = {52};
                Ruled Surface(11) = {53};

                Point(55) = {0,0,0.3,lc};

                Point(57) = {0,2,0.3,lc};
                Point(58) = {-2,0,0.3,lc};
                Point(59) = {0,-2,0.3,lc};

                Circle(59) = {30,55,57};
                Circle(60) = {57,55,58};
                Circle(61) = {58,55,59};
                Circle(62) = {59,55,32};

                Line(64) = {52,57};
                Line(65) = {53,58};
                Line(66) = {54,59};

                Line Loop(54) = {59,-64,-50,29};
                Line Loop(55) = {60,-65,-51,64};
                Line Loop(56) = {61,-66,-52,65};
                Line Loop(57) = {62,32,-53,66};

                Ruled Surface(12) = {54};
                Ruled Surface(13) = {55};
                Ruled Surface(14) = {56};
                Ruled Surface(15) = {57};

                Point(60) = {0,0,0.4,lc};
                Point(61) = {0,2,0.4,lc};
                Point(62) = {-2,0,0.4,lc};
                Point(63) = {0,-2,0.4,lc};

                Circle(67) = {31,60,61};
                Circle(68) = {61,60,62};
                Circle(69) = {62,60,63};
                Circle(70) = {63,60,31};

                Line(71) = {57,61};
                Line(72) = {58,62};
                Line(73) = {59,63};

                Line Loop(58) = {67,-71,-59,30};
                Line Loop(59) = {68,-72,-60,71};
                Line Loop(60) = {69,-73,-61,72};
                Line Loop(61) = {70,31,-62,73};

                Ruled Surface(16) = {58};
                Ruled Surface(17) = {59};
                Ruled Surface(18) = {60};
                Ruled Surface(19) = {61};

                """
        return geo
