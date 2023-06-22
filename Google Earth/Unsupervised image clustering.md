

# Unsupervised Image Clustering

## Description
Unsupervised image clustering is a technique used in computer vision and machine learning to automatically group similar images together based on their visual content, without the need for any predefined labels or prior knowledge. It is a form of unsupervised learning, where the algorithm identifies patterns and similarities within the image data to create clusters or groups.

The process of unsupervised image clustering involves extracting meaningful features or representations from the images, such as color, texture, or shape descriptors. These features are then used to measure the similarity between images, and clustering algorithms are applied to partition the images into distinct groups. The goal is to maximize the similarity within each cluster while maximizing the dissimilarity between different clusters.

## Key Components

- **Feature Extraction**: In order to compare and measure similarity between images, meaningful features or representations are extracted from the images. Common features include color histograms, texture descriptors, and shape information.

- **Clustering Algorithms**: Various clustering algorithms can be employed for unsupervised image clustering, such as k-means, hierarchical clustering, or density-based clustering. These algorithms iteratively assign images to clusters based on their similarity, aiming to optimize a defined objective function.

## Code 

Here's an example code snippet demonstrating unsupervised image clustering using the k-means algorithm:

```python
var sentinelCollection = ee.ImageCollection('COPERNICUS/S2_SR')
.filterDate('2022-10-01', '2023-03-30')
// Pre-filter to get less cloudy granules.
.filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
.filterBounds(Punjab)  // punjab is the preimported shape file of Punjab
.median();
Map.addLayer(sentinelCollection,{bands:["B4" ,"B3" ,"B2"]});
var training=sentinelCollection.sample({
region:Punjab,
scale:30,
numPixels:5000,
tileScale: 4
});
var clusterer=ee.Clusterer.wekaKMeans(5).train(training);
var unsupervised=sentinelCollection.cluster(clusterer);
Map.addLayer(unsupervised.randomVisualizer(),{},'clusters');
```

## Result Image


![Punjab_clusttering](https://github.com/RahulKumar-007/Remote-Sensing-and-Satellite-imagery/assets/117337265/9dc881b1-0934-4f22-89e7-56e1fa600e88)

The image example showcases the results of unsupervised image clustering. Different colors represent different clusters, where similar patches within the image have been grouped together based on their visual content.

## Applications

Unsupervised image clustering has a wide range of applications, including:

- **Image Organization**: By automatically categorizing large image datasets, unsupervised image clustering makes it easier to manage and search through vast collections of images. It enables efficient organization and retrieval of images based on their visual similarity.

- **Image Retrieval**: Unsupervised clustering can be utilized for image retrieval systems, where similar images are retrieved based on a query image. Users can search for visually similar images without relying on manual annotations or tags.

- **Object Recognition**: Clustering can help in discovering patterns and similarities in image data, which can be utilized for object recognition tasks. By identifying clusters representing different object categories, the algorithm can learn to recognize objects based on their visual appearance.

- **Anomaly Detection**: Unsupervised image clustering can be used to detect anomalies or outliers in image datasets. By clustering normal patterns and identifying images that do not belong to any cluster, potential anomalies or irregularities can be flagged for further investigation.

## Conclusion

Unsupervised image clustering is a powerful technique for automatically grouping similar images together based on their visual content. It eliminates the need for labeled training data and enables efficient organization, retrieval, object recognition, and anomaly detection in large-scale image datasets. By leveraging clustering algorithms and feature extraction techniques, this approach provides valuable insights into the underlying
