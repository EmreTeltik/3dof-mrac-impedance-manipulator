"""Ideal yaw-pitch-pitch geometry only; not a robot control program."""
import argparse
import json
import math

L2=0.150
L3=0.120

def check_lengths(l2,l3):
    if not all(math.isfinite(v) and v>0 for v in (l2,l3)):
        raise ValueError('link lengths must be positive finite metres')

def forward(q,l2=L2,l3=L3):
    check_lengths(l2,l3)
    if len(q)!=3 or not all(math.isfinite(v) for v in q):
        raise ValueError('provide three finite angles in radians')
    q1,q2,q3=q
    r=l2*math.cos(q2)+l3*math.cos(q2+q3)
    return (r*math.cos(q1),r*math.sin(q1),
            l2*math.sin(q2)+l3*math.sin(q2+q3))

def jacobian(q,l2=L2,l3=L3):
    forward(q,l2,l3)
    q1,q2,q3=q
    c1,s1=math.cos(q1),math.sin(q1)
    r=l2*math.cos(q2)+l3*math.cos(q2+q3)
    dr2=-l2*math.sin(q2)-l3*math.sin(q2+q3)
    dr3=-l3*math.sin(q2+q3)
    dz3=l3*math.cos(q2+q3)
    return ((-r*s1,dr2*c1,dr3*c1),
            (r*c1,dr2*s1,dr3*s1),(0.0,r,dz3))

def inverse(position,elbow=1,l2=L2,l3=L3):
    check_lengths(l2,l3)
    if len(position)!=3 or not all(math.isfinite(v) for v in position):
        raise ValueError('provide three finite Cartesian coordinates in metres')
    if elbow not in (-1,1):
        raise ValueError('elbow must be +1 or -1')
    x,y,z=position
    rho=math.hypot(x,y)
    if rho<1e-12:
        raise ValueError('base yaw is underdetermined on the z-axis')
    c3=(rho*rho+z*z-l2*l2-l3*l3)/(2*l2*l3)
    if c3 < -1-1e-10 or c3 > 1+1e-10:
        raise ValueError('outside ideal two-link distance bounds')
    c3=max(-1.0,min(1.0,c3))
    q3=elbow*math.acos(c3)
    q2=math.atan2(z,rho)-math.atan2(l3*math.sin(q3),l2+l3*math.cos(q3))
    return (math.atan2(y,x),q2,q3)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--angles-deg',nargs=3,type=float,default=[0,30,-45],
                        metavar=('Q1','Q2','Q3'))
    args=parser.parse_args()
    q=tuple(math.radians(v) for v in args.angles_deg)
    try:
        p=forward(q)
        j=jacobian(q)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps({'model':'ideal zero-offset yaw-pitch-pitch; not final CAD',
                      'link_lengths_m':[L2,L3],
                      'angles_deg':args.angles_deg,
                      'position_m':p,'jacobian_m_per_rad':j},indent=2))

if __name__=='__main__':
    main()
