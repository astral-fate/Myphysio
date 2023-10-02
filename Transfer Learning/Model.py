json_folder = "D:/Append"
json_files = [f for f in os.listdir(json_folder) if f.endswith('.json')]

df_list = []  # List to hold dataframes
for json_file in json_files:
    json_path = os.path.join(json_folder, json_file)
    with open(json_path, 'r') as file:
        data = json.load(file)
        temp_df = pd.DataFrame(data)
        df_list.append(temp_df)
        

final_df = pd.concat(df_list, ignore_index=True)

final_df.to_csv('final_dataframe.csv', index=False)


base_model = tf.keras.applications.MobileNetV2(input_shape=(160, 160, 3), include_top=False, weights='imagenet')

base_model.trainable = False
global_average_layer = tf.keras.layers.GlobalAveragePooling2D()

labels_dict = ['armraise', 'bicyclecrunch', 'birddog', 'curl', 'fly', 'legraise',
       'overheadpress', 'pushup', 'squat', 'superman']

prediction_layer = tf.keras.layers.Dense(len(labels_dict), activation='softmax')
inputs = tf.keras.Input(shape=(160, 160, 3))
x = base_model(inputs, training=False)
x = global_average_layer(x)


outputs = prediction_layer(x)
model = tf.keras.Model(inputs, outputs)


train_datagen = ImageDataGenerator(rescale=1./255)

val_datagen = ImageDataGenerator(rescale=1./255)   # for validation, only rescaling is needed


train_gen = train_datagen.flow_from_dataframe(
    dataframe=final_df,
    directory=None,
    x_col="image_path",
    y_col="label",
    target_size=(160, 160),
    class_mode='categorical', 
    batch_size=32
)


val_gen = val_datagen.flow_from_dataframe(
    dataframe=final_df,
    directory=None,  
    x_col="image_path",
    y_col="label",
    target_size=(160, 160),
    class_mode='categorical',  
    batch_size=32
)


# Assuming "image_path" is the column in your dataframe that contains the file paths to the images
# and "label" is the column that contains the labels
image_paths = final_df['image_path']
labels = final_df['label']  # or 'encoded_label' if you want to use the encoded labels

# Split the dataset into train and validation sets
train_files, val_files, train_labels, val_labels = train_test_split(
    image_paths, 
    labels, 
    test_size=0.2
)

# Load the MobileNetV2 model
base_model = tf.keras.applications.MobileNetV2(input_shape=(160, 160, 3), include_top=False, weights='imagenet')
base_model.trainable = False


# Add a classification head
global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
prediction_layer = tf.keras.layers.Dense(len(labels_dict), activation='softmax')

# Build the model
inputs = tf.keras.Input(shape=(160, 160, 3))
x = base_model(inputs, training=False)
x = global_average_layer(x)
outputs = prediction_layer(x)
model = tf.keras.Model(inputs, outputs)


model.compile(optimizer='adam',
              loss='categorical_crossentropy',  # Use categorical_crossentropy
              metrics=['accuracy'])

# Fit the model and get the history
history = model.fit(train_gen, 
                    epochs=10, 
                    validation_data=val_gen)

# Plot training & validation accuracy values
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Validation'], loc='upper left')

# Plot training & validation loss values
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train', 'Validation'], loc='upper left')

plt.show()
