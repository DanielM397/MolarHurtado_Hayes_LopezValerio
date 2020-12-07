'''

Super Project Group 5

Daniel Molar Hurtado

Nicholas Hayes

Rebeca Lopez Valerio

EE104 Super Project Option 4

'''
# make a prediction for a new image.
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import time
start_time = time.time()

# load and prepare the image
def load_image(filename):
    # load the image
    img = load_img(filename, target_size=(32, 32))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 32, 32, 3)
    # prepare pixel data
    img = img.astype('float32')
    img = img / 255.0
    return img

# load an image and predict the class
def run_example():
    # load the image
    img = load_image('ImageTest.png')
    # load model
    model = load_model('Final.h5')
    # predict the class
    result = model.predict_classes(img)
    time.sleep(2)
    print("CIFAR-10 Classes or Categories (0-9):")
    print("['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']")
    plt.imshow(mpimg.imread('ImageTest.png'))
    print("CIFAR-10 Class or Category:")
    print(result[0])

# entry point, run the example
run_example()

print("\nTime Elapsed:",(time.time() - start_time))