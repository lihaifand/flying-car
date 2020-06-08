# VGG with Tensorflow

1. VGG paper review

2. Tensorflow implementation

3. Fine-tuning from parameters trained on ImageNet dataset
# VGG Paper
https://arxiv.org/abs/1409.1556

# Paper keypoints
1. the effect of the convolutional network **depth** on its accuracy in the large-scale image recognition setting
  
2. using an architecture with very small (3 X 3) convolution filters, with stride 1
  
3. max-pooling is performed over a 2 × 2 pixel window, with stride 2
  
4. conv + 3 fully-connected layers (number of FC neurons: 4096 > 4096 > n_classes)
  
5. learning rate decay, parameter initializaiton from pre-trained models, etc.

# Training

1. load pre-trained parameters (trained on ImageNet dataset, 1000 classes), you can download the parameter file (vgg16.npy, about 500M) here:
https://mega.nz/#!YU1FWJrA!O1ywiCS2IiOlUCtCpI6HTJOMrneN-Qdv3ywQP5poecM

2. Remove the final layer, add one layer with 10 nodes to test the CIFAR10 dataset(binary version).
https://www.cs.toronto.edu/~kriz/cifar.html

3. It took me around one hour to train with 15000 training steps and learning rate is 0.01. The testing accuracy on the CIFAR10 test dataset is about 85.69%.

# References

1. https://github.com/tensorflow/tensorflow/blob/129665119ea60640f7ed921f36db9b5c23455224/tensorflow/contrib/slim/python/slim/learning.py

2. https://github.com/huyng/tensorflow-vgg

3. https://hackernoon.com/learning-keras-by-implementing-vgg16-from-scratch-d036733f2d5

4. http://stackoverflow.com/questions/33783672/how-can-i-visualize-the-weightsvariables-in-cnn-in-tensorflow

5. http://r2rt.com/implementing-batch-normalization-in-tensorflow.html

6. https://github.com/boyw165/tensorflow-vgg

7. http://cs231n.github.io/

8. etc.
