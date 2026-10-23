"""Math consistency checks only, without hardware/control assertions."""
import importlib.util
import math
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('kinematics',ROOT/'tools/kinematics_preview.py')
kin=importlib.util.module_from_spec(spec);spec.loader.exec_module(kin)

class KinematicsTests(unittest.TestCase):
    def assertVector(self,a,b,places=9):
        for x,y in zip(a,b):self.assertAlmostEqual(x,y,places=places)

    def test_zero_pose(self):
        self.assertVector(kin.forward((0,0,0)),(.270,0,0))

    def test_base_rotation(self):
        self.assertVector(kin.forward((math.pi/2,0,0)),(0,.270,0))

    def test_vertical_shoulder(self):
        self.assertVector(kin.forward((0,math.pi/2,0)),(0,0,.270))

    def test_both_elbow_branches_reproduce_point(self):
        p=kin.forward((.4,.5,-.8))
        for elbow in (-1,1):
            self.assertVector(kin.forward(kin.inverse(p,elbow)),p)

    def test_unreachable_points_and_axis_ambiguity(self):
        for p in ((1,0,0),(.001,0,0),(0,0,.1)):
            with self.subTest(p=p):
                with self.assertRaises(ValueError):kin.inverse(p)

    def test_jacobian_against_central_finite_difference(self):
        eps=1e-6
        for q in ((.2,.3,-.4),(.7,-.2,.9),(0,0,0)):
            analytical=kin.jacobian(q)
            for j in range(3):
                plus=list(q);minus=list(q);plus[j]+=eps;minus[j]-=eps
                fp=kin.forward(plus);fm=kin.forward(minus)
                for i in range(3):
                    self.assertAlmostEqual(analytical[i][j],(fp[i]-fm[i])/(2*eps),places=8)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):kin.forward((0,math.nan,0))
        with self.assertRaises(ValueError):kin.forward((0,0,0),l2=-1)
        with self.assertRaises(ValueError):kin.inverse((.15,0,.1),elbow=0)

if __name__=='__main__':
    unittest.main()
