# **Finding Lane Lines on the Road** 
---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


---

### Reflection

### 1. Pipeline details
**Please look into P1.ipynb file for the details**  
My pipeline consisted of 6 steps. 
1. gray scale  
![](pipeline/gray.jpg) 
2. gaussian bluring
![](pipeline/blur.jpg)
3. canny function for edge detection
![](pipeline/canny.jpg)
4. set the region of interest  
![](pipeline/region.jpg)
5. Hough Tranform line detection
![](pipeline/hough.jpg)
6. draw the line
![](pipeline/result.jpg)

### 2. The potential shortcomings with current pipeline


1. This function sometimes draw multiple lines instead of single line.
2. When the image has high exposures, it can't detect the line.

### 3. The possible improvements to current pipeline

1. Tune the parameters more carefully.
2. Add some other image processing steps to handle the special cases