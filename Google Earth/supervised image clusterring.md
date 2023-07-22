

# Supervised Image Clustering

## Description
Supervised image clustering, also known as supervised image classification, is a technique used in computer vision and machine learning to categorize images into predefined classes or labels. Unlike unsupervised image clustering, this approach requires a labeled dataset, where each image is associated with a known class label. The algorithm learns from these labeled examples during the training phase to make predictions on new, unseen images.

The process of supervised image clustering involves extracting meaningful features or representations from the images, similar to unsupervised clustering. These features are used to train a classification model, which learns to map the input images to their corresponding class labels. During training, the algorithm optimizes its parameters to minimize the classification error and improve the accuracy of predictions.

## Key Components

- **Feature Extraction**: Just like in unsupervised image clustering, meaningful features or representations need to be extracted from the images. Common feature extraction techniques include Histogram of Oriented Gradients (HOG), Local Binary Patterns (LBP), and Convolutional Neural Networks (CNNs). These features capture relevant information from the images and serve as input to the classification model.
- **Supervised Learning Algorithms**: Various supervised learning models can be used for image clustering, such as Support Vector Machines (SVM), Random Forests, or Convolutional Neural Networks (CNNs). These models are trained on the labeled dataset, learning to associate specific features with their corresponding class labels. In this example we have manually selected  a few points on the map and classified them in the respective category to train the machine learing model.

## Code 

Here's an example code snippet demonstrating Supervised image clustering :

```python

var image = ee.ImageCollection('COPERNICUS/S2_SR')
.filterDate('2022-10-01', '2023-03-30')
// Pre-filter to get less cloudy granules.
.filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
.filterBounds(Punjab)
.median();

var visParamsTrue = {bands: ['B4', 'B3', 'B2'], min: 0, max: 2500, gamma: 1.1};
Map.addLayer(image, visParamsTrue, "Sentinel 2017");
Map.centerObject(Punjab, 8);


// // Create Training Data
var training = Land.merge(Buildup).merge(Water).merge(road).merge(Vegetation);   // water land vegatation buildup and road are Featurecollection objects selected manually on the map 
print(training);

// This property stores the land cover labels as consecutive
// integers starting from zero.
var label = 'Class';
var bands = ['B2', 'B3', 'B4', 'B8']; // These are bands with 10 meter spatial resolution. 
var input = image.select(bands);

// Overlay the points on the imagery to get training.
var trainImage = input.sampleRegions({
  collection: training,
  properties: [label],
  scale: 30
});

var trainingData = trainImage.randomColumn();
var trainSet = trainingData.filter(ee.Filter.lessThan('random', 0.8));
var testSet = trainingData.filter(ee.Filter.greaterThanOrEquals('random', 0.8));

// Classification Model
var classifier = ee.Classifier.smileCart().train(trainSet, label, bands);

// Classify the image
var classified = input.classify(classifier);
print(classified.getInfo());

// Define a palette for the classification.
var landcoverPalette = [
  '253494', //Water (0)
  '00FF00', //vegatation (1)
  '000000', //road (2)
  'ff8000', //land (3)
  '969696', //Buildup (4)
];

Map.addLayer(classified, {palette: landcoverPalette, min: 1, max: 6}, 'classification');

// Accuracy Assessment
//Classify the testingSet and get a confusion matrix.
var confusionMatrix = ee.ConfusionMatrix(testSet.classify(classifier)
    .errorMatrix({
      actual: 'Class', 
      predicted: 'classification'
    }));

print('Confusion matrix:', confusionMatrix);
print('Overall Accuracy:', confusionMatrix.accuracy());
print('Producers Accuracy:', confusionMatrix.producersAccuracy());
print('Consumers Accuracy:', confusionMatrix.consumersAccuracy());

// Export classified map to Google Drive
Export.image.toDrive({
  image: classified,
  description: 'Sentinel_2_Classified_CART',
  scale: 10,
  region: Punjab,
  maxPixels: 1e13,
});


```

## Result Image ##
![supervised](https://github.com/RahulKumar-007/Remote-Sensing-and-Satellite-imagery/assets/117337265/20f29cdc-d9ea-422c-baf5-24fae9297166)




The image example showcases the results of Supervised image clustering. Different colors represent different clusters, where similar patches within the image have been grouped together based on their visual content.

## Applications

Supervised image clustering has a wide range of applications, including:

- **Object Recognition**:By learning from labeled data, supervised image clustering can be utilized to recognize and classify specific objects within images. For example, it can be used to distinguish between different animal species, identify vehicles, or recognize handwritten digits.
- **Medical Image Analysis**: In medical imaging, supervised clustering can aid in the detection and diagnosis of diseases. By training on labeled medical images, the algorithm can learn to identify anomalies or specific structures, assisting healthcare professionals in making accurate diagnoses.
- **Scene Undestanding**: Supervised image clustering can be used for scene understanding tasks, where images are classified into various environmental or architectural categories. This can be helpful in applications like autonomous vehicles, where understanding the surrounding scene is crucial for decision-making.
- **Quality Control and Inspection**: In manufacturing and industrial settings, supervised image clustering can be employed for quality control and inspection. The algorithm can be trained to identify defects or anomalies in products, ensuring that only high-quality items are delivered to consumers.
## Conclusion

Supervised image clustering is a valuable approach for image classification tasks, where labeled data is available for training. By leveraging the power of supervised learning models, this technique enables accurate and efficient categorization of images into predefined classes. The trained models can be deployed to handle real-world applications such as object recognition, medical image analysis, scene understanding, and quality control, making it a versatile tool in the field of computer vision and machine learning.
