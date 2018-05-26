# Building a Controller #

This is the readme for the C++ Drone Controller project.

 - [The tasks](#the-tasks)
 - [Evaluation](#evaluation)


#### The Code ####

The majority of controller code is in `src/QuadControl.cpp`.  
All the configuration files for your controller and the vehicle are in the `config` directory.  For example, for all your control gains and other desired tuning parameters, there is a config file called `QuadControlParams.txt` set up. While the simulator is running, you can edit this file in real time and see the affects your changes have on the quad!



#### Keyboard / Mouse Controls ####

There are a handful of keyboard / mouse commands to help with the simulator itself, including applying external forces on your drone to see how your controllers reacts!

 - Left drag - rotate
 - X + left drag - pan
 - Z + left drag - zoom
 - arrow keys - apply external force
 - C - clear all graphs
 - R - reset simulation
 - Space - pause simulation


## The Tasks ##
Implement the controller for the drone  which will be able to control it in the 3D environment. The architecture of the controller consists of altitude controller, position controller, and attitude controller.
![](animations/control1.png)
![](animations/control2.png)
### Body rate and roll/pitch control (scenario 2) ###
 In this scenario, you will see a quad above the origin.  It is created with a small initial rotation speed about its roll axis.  The controller will need to stabilize the rotational motion and bring the vehicle back to level attitude.

To accomplish this, you will:

1. Implement body rate control

- implement the code in the function `GenerateMotorCommands()`  
  So we need to redefine the force formulas given in lecture to correspond with these new definitions, as follows:  
  $F_{tot} = F0 + F1 + F2 + F3$  
  $\tau_x = (F0 - F1 + F2 - F3) * l$           // This is Roll  
  $\tau_y = (F0 + F1 - F2 - F3) * l$           // This is Pitch    
  $\tau_z = (-F0 + F1 + F2 - F3) * \kappa$      // This is Yaw  
  where l = L / $\sqrt{2}$   -  since, L is defined as half the distance between rotors
- implement the code in the function `BodyRateControl()`
Use body rate error and `kpPQR` to return the command moment.
- Tune `kpPQR` in `QuadControlParams.txt` to get the vehicle to stop spinning quickly but not overshoot. 
```
#Angle rate gains
kpPQR = 70, 70, 12
```
If successful, you should see the rotation of the vehicle about roll (omega.x) get controlled to 0 while other rates remain zero.  Note that the vehicle will keep flying off quite quickly, since the angle is not yet being controlled back to 0.  Also note that some overshoot will happen due to motor dynamics!.


2. Implement roll / pitch control
We won't be worrying about yaw just yet.

 - implement the code in the function `RollPitchControl()`
 - Tune `kpBank` in `QuadControlParams.txt` to minimize settling time but avoid too much overshoot
```
# Angle control gains
kpBank = 12
```

Now see the quad level itself (as shown below), though it’ll still be flying away slowly since we’re not controlling velocity/position!  You should also see the vehicle angle (Roll) get controlled to 0.

<p align="center">
<img src="animations/scenario2.gif" width="500"/>
</p>


### Position/velocity and yaw angle control (scenario 3) ###

Next, implement the position, altitude and yaw control for your quad.  For the simulation, you will use `Scenario 3`.  This will create 2 identical quads, one offset from its target point (but initialized with yaw = 0) and second offset from target point but yaw = 45 degrees.

1. implement the code in the function `LateralPositionControl()` and `AltitudeControl()`.
Use double integral control and tune parameters `kpPosXY`, `kpPosZ`, `kpVelXY` and `kpVelZ`.
```
# Position control gains
kpPosXY = 2.5
kpPosZ = 4
KiPosZ = 80
# Velocity control gains
kpVelXY = 10
kpVelZ = 20
```

If successful, the quads should be going to their destination points and tracking error should be going down (as shown below). However, one quad remains rotated in yaw.

2. implement the code in the function `YawControl()`.
 - tune parameters `kpYaw` and the 3rd (z) component of `kpPQR`
```
# Angle control gains
kpYaw = 2
```

Tune position control for settling time. Don’t try to tune yaw control too tightly, as yaw control requires a lot of control authority from a quadcopter and can really affect other degrees of freedom.  This is why you often see quadcopters with tilted motors, better yaw authority!

<p align="center">
<img src="animations/scenario3.gif" width="500"/>
</p>



### Non-idealities and robustness (scenario 4) ###

In this part, we will explore some of the non-idealities and robustness of a controller.  For this simulation, we will use `Scenario 4`.  This is a configuration with 3 quads that are all are trying to move one meter forward.  However, this time, these quads are all a bit different:
 - The green quad has its center of mass shifted back
 - The orange vehicle is an ideal quad
 - The red vehicle is heavier than usual

1. Run your controller & parameter set from Step 3.  Do all the quads seem to be moving OK?  If not, try to tweak the controller parameters to work for all 3 (tip: relax the controller).

2. Edit `AltitudeControl()` to add basic integral control to help with the different-mass vehicle.

3. Tune the integral control, and other control parameters until all the quads successfully move properly.  Your drones' motion should look like this:

<p align="center">
<img src="animations/scenario4.gif" width="500"/>
</p>


### Tracking trajectories ###

Now that we have all the working parts of a controller, you will put it all together and test it's performance once again on a trajectory.  For this simulation, you will use `Scenario 5`.  This scenario has two quadcopters:
 - the orange one is following `traj/FigureEight.txt`
 - the other one is following `traj/FigureEightFF.txt` - for now this is the same trajectory.  

How well is your drone able to follow the trajectory?  It is able to hold to the path fairly well?

