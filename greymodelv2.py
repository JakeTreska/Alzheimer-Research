import os
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image
from sklearn.preprocessing import LabelEncoder

# Define paths to the training and validation datasets
train_data_dir = r'C:\Users\farha\Downloads\Alzheimers\MODELS\greytest\train'
validation_data_dir = r'C:\Users\farha\Downloads\Alzheimers\MODELS\greytest\validation'

# Image dimensions
img_width, img_height = 224, 224

# Data generators for loading images
train_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=32,
    class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=32,
    class_mode='binary')

# Build MLP model
def build_model():
    base_model = VGG16(weights='imagenet', include_top=False, input_shape=(img_width, img_height, 3))
    x = base_model.output
    x = Flatten()(x)
    x = Dense(512, activation='relu')(x)
    predictions = Dense(1, activation='sigmoid')(x)
    model = Model(inputs=base_model.input, outputs=predictions)
    
    for layer in base_model.layers:
        layer.trainable = False
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

model = build_model()

# Train the model
model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    epochs=10,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // validation_generator.batch_size)

# Function to classify subfolders
def classify_subfolders(model, root_dir):
    grey_folders = []
    black_folders = []
    
    for subdir, _, files in os.walk(root_dir):
        if files:
            images = []
            for file in files:
                img_path = os.path.join(subdir, file)
                img = image.load_img(img_path, target_size=(img_width, img_height))
                img_array = image.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)
                img_array = preprocess_input(img_array)
                images.append(img_array)
            
            images = np.vstack(images)
            predictions = model.predict(images)
            avg_prediction = np.mean(predictions)
            
            if avg_prediction > 0.5:
                black_folders.append(subdir)
            else:
                grey_folders.append(subdir)
    
    return grey_folders, black_folders

# Get paths of subfolders containing "grey" and "black" images
test_data_dir = r'C:\Users\farha\Downloads\Alzheimers\MODELS\greytest\test'  # Add the path to your test dataset here
grey_folders, black_folders = classify_subfolders(model, test_data_dir)

print("Grey folders:", grey_folders)
print("Black folders:", black_folders)
