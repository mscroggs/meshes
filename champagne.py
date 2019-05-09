from .core import Mesh

class BottleAndCork(Mesh):
    def geo(self):
        # Bottle
        # R is big radius of bottle
        # r is small radius of bottle
        # H is height of large bit of bottle
        # h is height of small bit of bottle
        geo = "R = 1;r = 0.3;H=3;h=1;\n"
        geo += """
                rt2 = 1.41421356237;
                alpha = (R-r)/0.82842712474;
                Point(1) = {R,0,0,lc};
                Point(2) = {R,0,H,lc};
                Point(3) = {R-rt2*alpha,0,H,lc};
                Point(4) = {R+(1-rt2)*alpha,0,H+alpha,lc};
                Point(5) = {r+rt2*alpha,0,H+2*alpha,lc};
                Point(6) = {r,0,H+2*alpha,lc};
                Point(7) = {r,0,H+h+2*alpha,lc};

                Point(11) = {0,R,0,lc};
                Point(12) = {0,R,H,lc};
                Point(13) = {0,R-rt2*alpha,H,lc};
                Point(14) = {0,R+(1-rt2)*alpha,H+alpha,lc};
                Point(15) = {0,r+rt2*alpha,H+2*alpha,lc};
                Point(16) = {0,r,H+2*alpha,lc};
                Point(17) = {0,r,H+h+2*alpha,lc};

                Point(21) = {-R,0,0,lc};
                Point(22) = {-R,0,H,lc};
                Point(23) = {-R+rt2*alpha,0,H,lc};
                Point(24) = {-R-(1-rt2)*alpha,0,H+alpha,lc};
                Point(25) = {-r-rt2*alpha,0,H+2*alpha,lc};
                Point(26) = {-r,0,H+2*alpha,lc};
                Point(27) = {-r,0,H+h+2*alpha,lc};

                Point(31) = {0,-R,0,lc};
                Point(32) = {0,-R,H,lc};
                Point(33) = {0,-R+rt2*alpha,H,lc};
                Point(34) = {0,-R-(1-rt2)*alpha,H+alpha,lc};
                Point(35) = {0,-r-rt2*alpha,H+2*alpha,lc};
                Point(36) = {0,-r,H+2*alpha,lc};
                Point(37) = {0,-r,H+h+2*alpha,lc};

                Point(60) = {0,0,0,lc};
                Point(70) = {0,0,H,lc};
                Point(80) = {0,0,H+alpha,lc};
                Point(90) = {0,0,H+2*alpha,lc};
                Point(100) = {0,0,H+2*alpha+h,lc};

                Line(1) = {1,2};
                Circle(2) = {2,3,4};
                Circle(3) = {4,5,6};
                Line(4) = {6,7};

                Line(11) = {11,12};
                Circle(12) = {12,13,14};
                Circle(13) = {14,15,16};
                Line(14) = {16,17};

                Line(21) = {21,22};
                Circle(22) = {22,23,24};
                Circle(23) = {24,25,26};
                Line(24) = {26,27};

                Line(31) = {31,32};
                Circle(32) = {32,33,34};
                Circle(33) = {34,35,36};
                Line(34) = {36,37};

                Circle(60) = {1,60,11};
                Circle(61) = {11,60,21};
                Circle(62) = {21,60,31};
                Circle(63) = {31,60,1};
                Circle(70) = {2,70,12};
                Circle(71) = {12,70,22};
                Circle(72) = {22,70,32};
                Circle(73) = {32,70,2};
                Circle(80) = {4,80,14};
                Circle(81) = {14,80,24};
                Circle(82) = {24,80,34};
                Circle(83) = {34,80,4};
                Circle(90) = {6,90,16};
                Circle(91) = {16,90,26};
                Circle(92) = {26,90,36};
                Circle(93) = {36,90,6};
                Circle(100) = {7,100,17};
                Circle(101) = {17,100,27};
                Circle(102) = {27,100,37};
                Circle(103) = {37,100,7};

                Line Loop(1) = {11,60,-1,-70};
                Line Loop(2) = {21,61,-11,-71};
                Line Loop(3) = {31,62,-21,-72};
                Line Loop(4) = {1,63,-31,-73};
                Line Loop(5) = {-63,-62,-61,-60};

                Line Loop(6) = {12,70,-2,-80};
                Line Loop(7) = {22,71,-12,-81};
                Line Loop(8) = {32,72,-22,-82};
                Line Loop(9) = {2,73,-32,-83};

                Line Loop(10) = {13,80,-3,-90};
                Line Loop(11) = {23,81,-13,-91};
                Line Loop(12) = {33,82,-23,-92};
                Line Loop(13) = {3,83,-33,-93};

                Line Loop(14) = {14,90,-4,-100};
                Line Loop(15) = {24,91,-14,-101};
                Line Loop(16) = {34,92,-24,-102};
                Line Loop(17) = {4,93,-34,-103};

                Line Loop(18) = {100,101,102,103};

                """
        for i in range(1,19):
            geo += "Ruled Surface("+str(i)+") = {"+str(i)+"};\n"

        # Cork
        # cr is radius of cork
        # cz is z-value of centre cork
        geo += "cr = 0.3;cz=8;"
        geo += """
                Point(201) = {0,0,cz,lc};
                Point(202) = {0,0,cz+cr,lc};

                Point(211) = {cr,0,cz,lc};
                Point(212) = {cr/rt2,0,cz-cr/rt2,lc};
                Point(213) = {cr/rt2+0.05,0,cz-cr/rt2-cr,lc};
                Point(221) = {0,cr,cz,lc};
                Point(222) = {0,cr/rt2,cz-cr/rt2,lc};
                Point(223) = {0,cr/rt2+0.05,cz-cr/rt2-cr,lc};
                Point(231) = {-cr,0,cz,lc};
                Point(232) = {-cr/rt2,0,cz-cr/rt2,lc};
                Point(233) = {-cr/rt2-0.05,0,cz-cr/rt2-cr,lc};
                Point(241) = {0,-cr,cz,lc};
                Point(242) = {0,-cr/rt2,cz-cr/rt2,lc};
                Point(243) = {0,-cr/rt2-0.05,cz-cr/rt2-cr,lc};

                Point(250) = {0,0,cz-cr/rt2,lc};
                Point(251) = {0,0,cz-cr/rt2-cr,lc};

                Circle(211) = {202,201,211};
                Circle(212) = {211,201,212};
                Line(213) = {212,213};
                Circle(221) = {202,201,221};
                Circle(222) = {221,201,222};
                Line(223) = {222,223};
                Circle(231) = {202,201,231};
                Circle(232) = {231,201,232};
                Line(233) = {232,233};
                Circle(241) = {202,201,241};
                Circle(242) = {241,201,242};
                Line(243) = {242,243};

                Circle(271) = {211,201,221};
                Circle(272) = {221,201,231};
                Circle(273) = {231,201,241};
                Circle(274) = {241,201,211};
                Circle(281) = {212,250,222};
                Circle(282) = {222,250,232};
                Circle(283) = {232,250,242};
                Circle(284) = {242,250,212};
                Circle(291) = {213,251,223};
                Circle(292) = {223,251,233};
                Circle(293) = {233,251,243};
                Circle(294) = {243,251,213};

                Line Loop(200) = {-294,-293,-292,-291};
                Line Loop(201) = {213,291,-223,-281};
                Line Loop(202) = {223,292,-233,-282};
                Line Loop(203) = {233,293,-243,-283};
                Line Loop(204) = {243,294,-213,-284};
                Line Loop(205) = {212,281,-222,-271};
                Line Loop(206) = {222,282,-232,-272};
                Line Loop(207) = {232,283,-242,-273};
                Line Loop(208) = {242,284,-212,-274};
                Line Loop(209) = {211,271,-221};
                Line Loop(210) = {221,272,-231};
                Line Loop(211) = {231,273,-241};
                Line Loop(212) = {241,274,-211};

                """

        for i in range(200,213):
            geo += "Ruled Surface("+str(i)+") = {"+str(i)+"};\n"
        return geo

