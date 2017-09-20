def cake(h=0.1):
    """
    Returns a birthday cake

    Parameters
    ----------
    h : float
        Size of the elements.

    """

    geo = "lc = " + str(h) + ";"

    # First cylinder
    geo += """
            Point(1) = {0,0,0,lc};
            Point(2) = {2,0,0,lc};
            Point(3) = {0,2,0,lc};
            Point(4) = {-2,0,0,lc};
            Point(5) = {0,-2,0,lc};

            Point(6) = {0,0,1,lc};
            Point(7) = {2,0,1,lc};
            Point(8) = {0,2,1,lc};
            Point(9) = {-2,0,1,lc};
            Point(10) = {0,-2,1,lc};

            Circle(1) = {2,1,3};
            Circle(2) = {3,1,4};
            Circle(3) = {4,1,5};
            Circle(4) = {5,1,2};

            Circle(5) = {7,6,8};
            Circle(6) = {8,6,9};
            Circle(7) = {9,6,10};
            Circle(8) = {10,6,7};

            Line(9) = {2,7};
            Line(10) = {3,8};
            Line(11) = {4,9};
            Line(12) = {5,10};

            Line Loop(1) = {1,2,3,4};

            Line Loop(2) = {1,10,-5,-9};
            Line Loop(3) = {2,11,-6,-10};
            Line Loop(4) = {3,12,-7,-11};
            Line Loop(5) = {4,9,-8,-12};

            Plane Surface(1) = {-1};
            Ruled Surface(2) = {2};
            Ruled Surface(3) = {3};
            Ruled Surface(4) = {4};
            Ruled Surface(5) = {5};
            """
    # Jam
    geo += """
            Point(11) = {0,0,1.2,lc};
            Point(12) = {2,0,1.2,lc};
            Point(13) = {0,2,1.2,lc};
            Point(14) = {-2,0,1.2,lc};
            Point(15) = {0,-2,1.2,lc};

            Point(16) = {2.1,0,1.1,lc};
            Point(17) = {0,2.1,1.1,lc};
            Point(18) = {-2.1,0,1.1,lc};
            Point(19) = {0,-2.1,1.1,lc};

            Circle(13) = {12,11,13};
            Circle(14) = {13,11,14};
            Circle(15) = {14,11,15};
            Circle(16) = {15,11,12};

            Circle(17) = {7,16,12};
            Circle(18) = {8,17,13};
            Circle(19) = {9,18,14};
            Circle(20) = {10,19,15};

            Line Loop(6) = {5,18,-13,-17};
            Line Loop(7) = {6,19,-14,-18};
            Line Loop(8) = {7,20,-15,-19};
            Line Loop(9) = {8,17,-16,-20};

            Ruled Surface(6) = {6};
            Ruled Surface(7) = {7};
            Ruled Surface(8) = {8};
            Ruled Surface(9) = {9};
            """
    # Second cylinder
    geo += """
            Point(20) = {0,0,2.2,lc};
            Point(21) = {2,0,2.2,lc};
            Point(22) = {0,2,2.2,lc};
            Point(23) = {-2,0,2.2,lc};
            Point(24) = {0,-2,2.2,lc};

            Line(21) = {12,21};
            Line(22) = {13,22};
            Line(23) = {14,23};
            Line(24) = {15,24};

            Circle(25) = {21,20,22};
            Circle(26) = {22,20,23};
            Circle(27) = {23,20,24};
            Circle(28) = {24,20,21};

            Line Loop(10) = {13,22,-25,-21};
            Line Loop(11) = {14,23,-26,-22};
            Line Loop(12) = {15,24,-27,-23};
            Line Loop(13) = {16,21,-28,-24};

            Ruled Surface(10) = {10};
            Ruled Surface(11) = {11};
            Ruled Surface(12) = {12};
            Ruled Surface(13) = {13};
            """
    # Top of cake
    geo += """
            Point(25) = {.2,0,2.2,lc};
            Point(26) = {0,.2,2.2,lc};
            Point(27) = {-.2,0,2.2,lc};
            Point(28) = {0,-.2,2.2,lc};

            Circle(29) = {25,20,26};
            Circle(30) = {26,20,27};
            Circle(31) = {27,20,28};
            Circle(32) = {28,20,25};

            Line Loop(14) = {29,30,31,32};
            Line Loop(15) = {25,26,27,28};

            Ruled Surface(14) = {15,14};
            """    
    # Candle
    geo += """
            Point(29) = {0,0,2.7,lc};
            Point(30) = {.2,0,2.7,lc};
            Point(31) = {0,.2,2.7,lc};
            Point(32) = {-.2,0,2.7,lc};
            Point(33) = {0,-.2,2.7,lc};

            Line(33) = {25,30};
            Line(34) = {26,31};
            Line(35) = {27,32};
            Line(36) = {28,33};

            Circle(37) = {30,29,31};
            Circle(38) = {31,29,32};
            Circle(39) = {32,29,33};
            Circle(40) = {33,29,30};

            Line Loop(16) = {29,34,-37,-33};
            Line Loop(17) = {30,35,-38,-34};
            Line Loop(18) = {31,36,-39,-35};
            Line Loop(19) = {32,33,-40,-36};

            Ruled Surface(15) = {16};
            Ruled Surface(16) = {17};
            Ruled Surface(17) = {18};
            Ruled Surface(18) = {19};

            """
    # Top of candle
    geo += """
            Point(34) = {.15,0,2.7,lc};
            Point(35) = {0,.15,2.7,lc};
            Point(36) = {-.15,0,2.7,lc};
            Point(37) = {0,-.15,2.7,lc};

            Circle(41) = {34,29,35};
            Circle(42) = {35,29,36};
            Circle(43) = {36,29,37};
            Circle(44) = {37,29,34};

            Line Loop(20) = {41,42,43,44};
            Line Loop(21) = {37,38,39,40};

            Ruled Surface(19) = {21,20};
            """
    # Flame
    geo += """
            h = 2.860934769394311;
            Point(38) = {0,0,h,lc};
            Point(39) = {0.22,0,h,lc};
            Point(40) = {0,0.22,h,lc};
            Point(41) = {-0.22,0,h,lc};
            Point(42) = {0,-0.22,h,lc};

            Circle(45) = {34,38,39};
            Circle(46) = {35,38,40};
            Circle(47) = {36,38,41};
            Circle(48) = {37,38,42};

            Circle(49) = {39,38,40};
            Circle(50) = {40,38,41};
            Circle(51) = {41,38,42};
            Circle(52) = {42,38,39};

            Line Loop(22) = {45,49,-46,-41};
            Line Loop(23) = {46,50,-47,-42};
            Line Loop(24) = {47,51,-48,-43};
            Line Loop(25) = {48,52,-45,-44};
            Ruled Surface(20) = {-22};
            Ruled Surface(21) = {-23};
            Ruled Surface(22) = {-24};
            Ruled Surface(23) = {-25};

            Point(43) = {0,0,3.3,lc};

            Line(53) = {39,43};
            Line(54) = {40,43};
            Line(55) = {41,43};
            Line(56) = {42,43};

            Line Loop(26) = {53,-54,-49};
            Line Loop(27) = {54,-55,-50};
            Line Loop(28) = {55,-56,-51};
            Line Loop(29) = {56,-53,-52};

            Ruled Surface(24) = {-26};
            Ruled Surface(25) = {-27};
            Ruled Surface(26) = {-28};
            Ruled Surface(27) = {-29};
            """


    geo += "\nMesh.Algorithm = 6;"
    return geo
