# Dataset Acquisition and Preparation

## Study Area

The research team collected aerial imagery around **Merul Badda, Dhaka, Bangladesh**, focusing on the area surrounding BRAC University's new campus development. The imagery covers built infrastructure and the surrounding urban landscape.

## Aerial Image Collection

The thesis presentation documents **three image-acquisition sessions**, spaced approximately **two months apart**. The collection included **350 raw images and 17 videos**. Additional images were extracted from video frames for dataset preparation.

## Annotation

The team used **Roboflow** for image annotation and preparation. The presentation reports approximately **50,000 manually created annotations**, with infrastructure objects labeled across **11 classes**.

## Preprocessing

The documented workflow includes:

1. **Image filtering:** Removing null or corrupted images.
2. **Object isolation:** Identifying and annotating infrastructure objects.
3. **Image scaling:** Standardizing image dimensions to **640 × 640 pixels**.
4. **Orientation correction:** Standardizing irregular image orientation.

## Research Application

The annotated dataset was used in comparative infrastructure-detection experiments involving **YOLOv5, YOLOv7, YOLOv8, and a custom model**.

The research also explored applications involving photogrammetry, building-height estimation, distance analysis, and geolocation-based mapping.

## Publication

[Enhancing Infrastructure Detection Using Drone Imagery — IEEE ICECE 2024](https://doi.org/10.1109/ICECE64886.2024.11025116)
