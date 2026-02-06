# Projectile-Motion-SImulator
A python script simulating how a body would behave if projected , using an eulerian integration.

# How it works

1) The user inputs all required variables to calcuate horizontal and vertical velocities and acceleration.
2) The euler integration begins, and the x and y components of the bodies position are added to 2 lists, and it's x and y velocities are calculated using trigonometry.
3) The acceleration acting in the x and y directions due to weight and air resistance are calcuated using their respective equations( w=k, ar prop to v^2), and then the velocites for the next timestep are calculated using v = u + a*dt
4) The velocities are ten used to calcuate the new x and y positions of the body, using s=
