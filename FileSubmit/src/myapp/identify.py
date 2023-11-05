import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def identify(arg1 = 'C:\\Users\\joshu\\Desktop\\FileSubmit\\src\\media\\documents\\hand.jpeg'):
    plt.imshow(arg1)
    plt.show()
    model = tf.keras.models.load_model('C:\\Users\\joshu\\Desktop\\FileSubmit\\src\\myapp\\goated2.keras')
    image_path = arg1
    image_size = [50,50]

    # Convert image to tensor
    image = tf.io.read_file(image_path)
    image = tf.io.decode_jpeg(image, channels = 1) # This greyscales the image as well
    image = tf.image.resize(image, image_size)

    # Convert to numpy array
    data = image.numpy() / 255 # to normalise the data
    pred = model.predict(data.reshape(-1, 50, 50, 1)) # reshape to be accepted by model
    pred_arr = np.array(pred[0])

    # Link to letter predictions, and print 3 most likely letters according to the model.

    letterpred = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'nothing']

    letter_prediction_dict = {letterpred[i]: predarray[i] for i in range(len(letterpred))}
    predarrayordered = sorted(predarray, reverse=True)
    high1 = predarrayordered[0]
    high2 = predarrayordered[1]
    high3 = predarrayordered[2]
    for key,value in letter_prediction_dict.items():
        if value==high1:
            print("Predicted Character 1: ", key)
            print('Confidence 1: ', 100*value)
        elif value==high2:
            print("Predicted Character 2: ", key)
            print('Confidence 2: ', 100*value)
        elif value==high3:
            print("Predicted Character 3: ", key)
            print('Confidence 3: ', 100*value)

identify('C:\\Users\\joshu\\Desktop\\FileSubmit\\src\\media\\documents\\hand.jpeg')