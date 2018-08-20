import csv
import cv2
import numpy as np
import matplotlib.pyplot as plt
from os.path import isfile
from sklearn.utils import shuffle
from keras.models import Sequential, load_model
from sklearn.model_selection import train_test_split
from keras.layers import Flatten, Dense, Lambda, Convolution2D, MaxPooling2D, Cropping2D

samples = []
folder = './sharpcurve'
with open(folder + '/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        samples.append(line)

train_samples, validation_samples = train_test_split(samples, test_size=0.2)

def generator(samples, batch_size=64):
    num_samples = len(samples)
    correction = [0, 0.001, -0.001]
    while 1: # Loop forever so the generator never terminates
        shuffle(samples)
        for offset in range(0, num_samples, batch_size):
            batch_samples = samples[offset:offset+batch_size]
            images = []
            angles = []
            for batch_sample in batch_samples:
                # for i in range(3):
                name = folder + '/IMG/'+batch_sample[0].split('/')[-1]
                center_image = cv2.imread(name)
                center_angle = float(batch_sample[3])# + correction[i]
                images.append(center_image)
                angles.append(center_angle)
                #image augmentation
                images.append(cv2.flip(center_image, 1))
                angles.append(center_angle*-1.0)

            # trim image to only see section with road
            X_train = np.array(images)
            y_train = np.array(angles)
            yield shuffle(X_train, y_train)

# compile and train the model using the generator function
train_generator = generator(train_samples, batch_size=32)
validation_generator = generator(validation_samples, batch_size=32)

def layers():
    model = Sequential()
    model.add(Lambda(lambda x: x / 255.0 - 0.5, input_shape=(160,320,3)))
    model.add(Cropping2D(cropping=((70,25),(0,0))))
    model.add(Convolution2D(24,5,5,subsample=(2,2),activation="relu"))
    model.add(Convolution2D(36,5,5,subsample=(2,2),activation="relu"))
    model.add(Convolution2D(48,5,5,subsample=(2,2),activation="relu"))
    model.add(Convolution2D(64,3,3,activation="relu"))
    model.add(Convolution2D(64,3,3,activation="relu"))
    model.add(Flatten())
    model.add(Dense(100))
    model.add(Dense(50))
    model.add(Dense(10))
    model.add(Dense(1))
    model.compile(loss='mse', optimizer='adam')

if isfile(folder + '/model.h5'):
    # continue training if the model exists
    model = load_model(folder + '/model.h5')
else: 
    model = layers()

# model.fit(X_train, y_train, validation_split=0.2, shuffle=True, nb_epoch=1)
history_object = model.fit_generator(train_generator, samples_per_epoch= \
len(train_samples), validation_data=validation_generator, \
            nb_val_samples=len(validation_samples), nb_epoch=2, verbose=1)
model.save(folder + '/modelnew.h5')

### print the keys contained in the history object
print(history_object.history.keys())

### plot the training and validation loss for each epoch
plt.plot(history_object.history['loss'])
plt.plot(history_object.history['val_loss'])
plt.title('model mean squared error loss')
plt.ylabel('mean squared error loss')
plt.xlabel('epoch')
plt.legend(['training set', 'validation set'], loc='upper right')
plt.show()