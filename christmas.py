from .core import Mesh

class ChristmasTree(Mesh):
    def geo(self):
        geo += """
            Point(1)={0,0,0,lc};
            Point(2)={1,0,0,lc};
            Point(3)={0,1,0,lc};
            Point(4)={-1,0,0,lc};
            Point(5)={0,-1,0,lc};

            Point(6)={0,0,1,lc};
            Point(7)={1,0,1,lc};
            Point(8)={0,1,1,lc};
            Point(9)={-1,0,1,lc};
            oint(10)={0,-1,1,lc};

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

            Line Loop(1)={1,2,3,4};
            Line Loop(2)={5,6,7,8};

            Line Loop(3)={1,10,-5,-9};
            Line Loop(4)={2,11,-6,-10};
            Line Loop(5)={3,12,-7,-11};
            Line Loop(6)={4,9,-8,-12};

            Plane Surface(1)={1};
            Plane Surface(2)={-2};
            Ruled Surface(3)={3};
            Ruled Surface(4)={4};
            Ruled Surface(5)={5};
            Ruled Surface(6)={6};
        """
        return geo
