from .core import Mesh

class ChristmasTree(Mesh):
    def geo(self):
        geo = """
            Point(1) ={ 0,   0,   0,lc};
            Point(2) ={ 0.5, 0,   0,lc};
            Point(3) ={ 0,   0.5, 0,lc};
            Point(4) ={-0.5, 0,   0,lc};
            Point(5) ={ 0,  -0.5, 0,lc};

            Point(6) ={ 0,   0,   1,lc};
            Point(7) ={ 0.7, 0,   1,lc};
            Point(8) ={ 0,   0.7, 1,lc};
            Point(9) ={-0.7, 0,   1,lc};
            Point(10)={ 0,  -0.7, 1,lc};

            Point(11)={ 0.2, 0,   1,lc};
            Point(12)={ 0,   0.2, 1,lc};
            Point(13)={-0.2, 0,   1,lc};
            Point(14)={ 0,  -0.2, 1,lc};

            Point(15)={ 0,   0,   1.5,lc};
            Point(16)={ 0.2, 0,   1.5,lc};
            Point(17)={ 0,   0.2, 1.5,lc};
            Point(18)={-0.2, 0,   1.5,lc};
            Point(19)={ 0,  -0.2, 1.5,lc};

            Point(20)={ 1.5, 0,   1.5,lc};
            Point(21)={ 0,   1.5, 1.5,lc};
            Point(22)={-1.5, 0,   1.5,lc};
            Point(23)={ 0,  -1.5, 1.5,lc};

            Point(24)={ 0,   0,   2.5,lc};
            Point(25)={ 0.4, 0,   2.5,lc};
            Point(26)={ 0,   0.4, 2.5,lc};
            Point(27)={-0.4, 0,   2.5,lc};
            Point(28)={ 0,  -0.4, 2.5,lc};

            Point(29)={ 1.3, 0,   2.5,lc};
            Point(30)={ 0,   1.3, 2.5,lc};
            Point(31)={-1.3, 0,   2.5,lc};
            Point(32)={ 0,  -1.3, 2.5,lc};

            Point(33)={ 0,   0,   3.5,lc};
            Point(34)={ 0.3, 0,   3.5,lc};
            Point(35)={ 0,   0.3, 3.5,lc};
            Point(36)={-0.3, 0,   3.5,lc};
            Point(37)={ 0,  -0.3, 3.5,lc};

            Point(38)={ 1, 0, 3.5,lc};
            Point(39)={ 0, 1, 3.5,lc};
            Point(40)={-1, 0, 3.5,lc};
            Point(41)={ 0,-1, 3.5,lc};

            Point(42)={0,0,4.5,lc};

            Circle(1)={2,1,3};
            Circle(2)={3,1,4};
            Circle(3)={4,1,5};
            Circle(4)={5,1,2};

            Circle(5)={7,6,8};
            Circle(6)={8,6,9};
            Circle(7)={9,6,10};
            Circle(8)={10,6,7};

            Line(9)={2,7};
            Line(10)={3,8};
            Line(11)={4,9};
            Line(12)={5,10};

            Circle(13)={11,6,12};
            Circle(14)={12,6,13};
            Circle(15)={13,6,14};
            Circle(16)={14,6,11};

            Circle(17)={16,15,17};
            Circle(18)={17,15,18};
            Circle(19)={18,15,19};
            Circle(20)={19,15,16};

            Line(21)={11,16};
            Line(22)={12,17};
            Line(23)={13,18};
            Line(24)={14,19};

            Circle(25)={20,15,21};
            Circle(26)={21,15,22};
            Circle(27)={22,15,23};
            Circle(28)={23,15,20};

            Circle(29)={25,24,26};
            Circle(30)={26,24,27};
            Circle(31)={27,24,28};
            Circle(32)={28,24,25};

            Line(33)={20,25};
            Line(34)={21,26};
            Line(35)={22,27};
            Line(36)={23,28};

            Circle(37)={29,24,30};
            Circle(38)={30,24,31};
            Circle(39)={31,24,32};
            Circle(40)={32,24,29};

            Circle(41)={34,33,35};
            Circle(42)={35,33,36};
            Circle(43)={36,33,37};
            Circle(44)={37,33,34};

            Line(45)={29,34};
            Line(46)={30,35};
            Line(47)={31,36};
            Line(48)={32,37};

            Circle(49)={38,33,39};
            Circle(50)={39,33,40};
            Circle(51)={40,33,41};
            Circle(52)={41,33,38};

            Line(53)={38,42};
            Line(54)={39,42};
            Line(55)={40,42};
            Line(56)={41,42};

            Line Loop(1)={1,2,3,4};
            Line Loop(2)={5,6,7,8};

            Line Loop(3)={1,10,-5,-9};
            Line Loop(4)={2,11,-6,-10};
            Line Loop(5)={3,12,-7,-11};
            Line Loop(6)={4,9,-8,-12};

            Line Loop(7)={13,14,15,16};
            Line Loop(8)={17,18,19,20};

            Line Loop(9)= {13,22,-17,-21};
            Line Loop(10)={14,23,-18,-22};
            Line Loop(11)={15,24,-19,-23};
            Line Loop(12)={16,21,-20,-24};

            Line Loop(13)={25,26,27,28};

            Line Loop(14)={29,30,31,32};

            Line Loop(15)={25,34,-29,-33};
            Line Loop(16)={26,35,-30,-34};
            Line Loop(17)={27,36,-31,-35};
            Line Loop(18)={28,33,-32,-36};

            Line Loop(19)={37,38,39,40};

            Line Loop(20)={41,42,43,44};

            Line Loop(21)={37,46,-41,-45};
            Line Loop(22)={38,47,-42,-46};
            Line Loop(23)={39,48,-43,-47};
            Line Loop(24)={40,45,-44,-48};

            Line Loop(25)={49,50,51,52};

            Line Loop(26)={49,54,-53};
            Line Loop(27)={50,55,-54};
            Line Loop(28)={51,56,-55};
            Line Loop(29)={52,53,-56};

            Plane Surface(1)={-1};
            Plane Surface(2)={2,7};
            Ruled Surface(3)={3};
            Ruled Surface(4)={4};
            Ruled Surface(5)={5};
            Ruled Surface(6)={6};
            Ruled Surface(7)={9};
            Ruled Surface(8)={10};
            Ruled Surface(9)={11};
            Ruled Surface(10)={12};
            Plane Surface(11)={-13,-8};
            Ruled Surface(12)={15};
            Ruled Surface(13)={16};
            Ruled Surface(14)={17};
            Ruled Surface(15)={18};
            Ruled Surface(16)={-19,-14};
            Ruled Surface(17)={21};
            Ruled Surface(18)={22};
            Ruled Surface(19)={23};
            Ruled Surface(20)={24};
            Ruled Surface(21)={-25,-20};
            Ruled Surface(22)={26};
            Ruled Surface(23)={27};
            Ruled Surface(24)={28};
            Ruled Surface(25)={29};
        """
        return geo
