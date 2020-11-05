from unittest import TestCase
from TAMA import mapmatching
import numpy as np

class Testmapmatching(TestCase):
    def test_find_link(self):
        a=np.array(range(10))
        zero=np.zeros(10)
        links = [[[0, 0], [10, 0]], [[0, 0], [0, 10]], [[10, 0], [10, 10]], [[0, 10], [10, 10]]]
        myclass = mapmatching(a, zero, links)
        print(myclass.find_link(a,zero))
        myclass = mapmatching(zero, a, links)
        print(myclass.find_link(zero,a))


    def test_point_to_curve(self):
        a = np.array(range(10))
        b = np.random.randint(-2, 2, 10)
        links = [[[0, 0], [10, 0]], [[0, 0], [0, 10]], [[10, 0], [10, 10]], [[0, 10], [10, 10]]]
        myclass = mapmatching(a, b, links)
        modified = myclass.point_to_curve()

    def test_rot_ydeg(self):
        m = np.random.randint(-10, 0, 10)
        m1 = np.random.randint(-10, 0, 10)
        p = np.random.randint(0, 10, 10)
        links = [[[0,0],[10,0]],[[0,0],[0,10]],[[10,0],[10,10]],[[0,10],[10,10]]]
        myclass = mapmatching(m,m1,links)
        x, y = myclass.rot_ydeg()
        assert (all(item < 0 for item in x))
        assert (all(item > 0 for item in y))
        myclass = mapmatching(p, m, links)
        x, y = myclass.rot_ydeg()
        assert (all(item < 0 for item in x))
        assert (all(item > 0 for item in y))
        #x, y = self.rot_deg(p, p)
        #assert (all(item < 0 for item in x))
        #assert (all(item > 0 for item in y))


if __name__ == '__main__':
    unittest.main()
