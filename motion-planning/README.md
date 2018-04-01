## Project: 3D Motion Planning
![Quad Image](./misc/enroute.png)


---

### Writeup / README

### The Starter Code

####  The functionality of what's provided in `motion_planning.py` and `planning_utils.py`
These scripts contain a basic planning implementation that includes the utilitie that creates the grid of the obstacles and planning utilities like A* function which does not include diagonal movement and path pruning. 

The starter code provides a planning that moves by one unit at a time in a zig-zag way to the goal.



### Implementing Your Path Planning Algorithm

#### 1. Set your global home position
- read the first line of the csv file  
- extract lat0 and lon0 as floating point values by using regular expression 
- use the self.set_home_position() method to set global home to (lon0, lan0, 0)


And here is a lovely picture of our downtown San Francisco environment from above!
![Map of SF](./misc/map.png)

#### 2. Set your current local position
The local position is extracted by the helper utility function global_to_local(). The first argement is the current position (self._longitude, self._latitude,self._altitude) and the second argument is self.global_home.


Meanwhile, here's a picture of me flying through the trees!
![Forest Flying](./misc/in_the_trees.png)

#### 3. Set grid start position from local position
- extract the north_offset and east_offset
- set the grid start with local position considering the offsets.

#### 4. Set grid goal position from geodetic coords
- find the free grid position(if free the value is 0) and set it to goal position
```
# free_space = np.where(grid == 0)
# index = np.random.choice(len(free_space[0]))
# grid_goal = (-north_offset + free_space[0][index], -east_offset + free_space[1][index])
```
- to reduce the complexity, the goal position is set to a position with the coordinates (-north_offset + 275, -east_offset -31)

#### 5. Modify A* to include diagonal motion (or replace A* altogether)

- the diagonal actions includes flying northwest, northeast, southwest and southeast are added to the valid drone actions in addition to flying north, east, west, south.
- the cost of diagonal movement is set to sqrt(2)
- if the movement is illegal then the movement is removed from the available action list


#### 6. Cull waypoints 
- collinearity_check is used to remove the redundant waypoints in the path. 
- if the determinant of the matrix three points' coordinates is less than 1e-6, the point the second point of the three will be removed.
- The idea is simply to prune the path of unnecessary waypoints. 


### [rubric](https://review.udacity.com/#!/rubrics/1534/view) points.
  
# Extra Challenges: Real World Planning

For an extra challenge, consider implementing some of the techniques described in the "Real World Planning" lesson. You could try implementing a vehicle model to take dynamic constraints into account, or implement a replanning method to invoke if you get off course or encounter unexpected obstacles.


