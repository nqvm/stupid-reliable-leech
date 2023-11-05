# stupid-reliable-leech
Durhack repository for team: stupid-reliable-leech.

![Our father, Daniel Chambers](https://github.com/nqvm/stupid-reliable-leech/blob/8808a928c147140689c88224ec6f149ef17f02fa/Daniel-Chambers-Feature.png)

- [Durhack live](https://live.durhack.com/)  
- [Megateams](https://megateams.durhack.com/hacker)
- [Devpost](https://durhack-2023.devpost.com/)
- [MLH Prizes (not all of 'em)](https://hack.mlh.io/durhack-2023-4f/prizes)

## I Introduction  
CNN (goated.keros) model was developed on [this](https://www.kaggle.com/code/madz2000/cnn-using-keras-100-accuracy/notebook). This CNN model was trained on 50 x 50

## II How to use  
**Input:** Single 28 x 28 pixel image with greyscale values between 0-255.  
**Using the model:**  First, load the model:
```
import tensorflow as tf
model = tf.keras.models.load_model("filepath/to/goated.keras")
```   
To put in an input image, we must

Further outlined on [this page](https://www.tensorflow.org/guide/keras/serialization_and_saving).


### Important Links

- [Inspiration and starting point for CNN](https://www.kaggle.com/code/madz2000/cnn-using-keras-100-accuracy/notebook#Loading-the-ASL-dataset)
- [^ same](https://towardsdatascience.com/sign-language-recognition-with-advanced-computer-vision-7b74f20f3442)
- [First dataset used](https://www.kaggle.com/datasets/datamunge/sign-language-mnist)
- [Second (and larger) dataset](https://www.kaggle.com/datasets/grassknoted/asl-alphabet/data)
- [CNN Tutorial](https://www.kaggle.com/code/ryanholbrook/the-convolutional-classifier)
