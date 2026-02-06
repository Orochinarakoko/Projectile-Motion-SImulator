# Projectile-Motion-SImulator
A python script simulating how a body would behave if projected , using an eulerian integration.

# How it works

1) The user inputs all required variables to calcuate horizontal and vertical velocities and acceleration.
2) The euler integration begins, and the x and y components of the bodies position are added to 2 lists, and it's x and y velocities are calculated using trigonometry.
3) The acceleration acting in the x and y directions due to weight and air resistance are calcuated using their respective equations( w=k, ar prop to v^2), and then the velocites for the next timestep are calculated using v = u + a*dt
4) The velocities are then used to calcuate the new x and y positions of the body, using s=u*dt
5) Steps 2-4 are repeated untill the calculated y position is less than zero, in which a linear approximation is used to calculate where the ball will approximately land
6) Vpython is then used to render the projectile and the ground, and using the calcuated positions of the projectile, as well as a fixed rate of update, to show what the projction would actually look like.
7) Matplotlib is then used to create a graph of x position against y position.
