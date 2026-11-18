# Original Bangladesh-Based Drone Imagery Dataset

## Why the Dataset Matters

This undergraduate research was built around a **locally collected and manually annotated aerial-imagery dataset**, rather than solely using a pre-existing public benchmark. The team collected imagery of the urban environment around **BRAC University's new campus in Merul Badda, Dhaka, Bangladesh**, with drone photography undertaken from the campus rooftop.

The collection coincided with the period surrounding BRAC University's move from Mohakhali to its new campus in Badda. The team captured the surrounding landscape at **multiple stages** to observe changes in urban infrastructure over time. This is a **multi-stage acquisition strategy**; it should not be confused with a separately validated automated temporal change-detection model.

## Drone Image Collection and Annotation

The final thesis presentation reports:

| Dataset development measure | Value documented in thesis |
| --- | ---: |
| Raw aerial photographs | 350 |
| Drone videos | 17 |
| Image-acquisition sessions | 3 |
| Approximate interval between sessions | 2 months |
| Manual object annotations | Approximately 50,000 |
| Final research class taxonomy | 11 classes |

The research team organized drone-based collection, prepared imagery, manually annotated infrastructure objects using Roboflow, and used the resulting dataset in experiments involving YOLOv5, YOLOv7, YOLOv8, and a custom approach.

## Dataset Research Contribution

The original dataset supports the research team's investigation of infrastructure recognition in Bangladesh's urban environment. The collection strategy combines local aerial imagery, repeated observation across acquisition sessions, and manual annotation of infrastructure categories.

The dataset development process and its application to the comparative detection experiments are described in the [dataset methodology](dataset-methodology.md) and [experiment configurations](experiment-configurations.md).

## Annotated Examples

The [experimental figure gallery](experimental-figure-gallery.md) shows original detection results from the thesis presentation. A curated set of raw and annotated dataset samples may be added separately when public sharing is authorized.

## Individual Contribution

**Nabila Islam Borno** contributed to dataset preparation, manual image annotation, results analysis and visualization, and research writing/documentation. Drone acquisition and the broader model experiments were **collaborative team activities**.

## Relationship to the Published Thesis

The dataset was an enabling research contribution for the comparative infrastructure-detection study, not a separate published benchmark release.

- [Main research repository](../README.md)
- [Dataset acquisition and preparation methodology](dataset-methodology.md)
- [Experimental figures](experimental-figure-gallery.md)
- [IEEE ICECE publication](https://doi.org/10.1109/ICECE64886.2024.11025116)
