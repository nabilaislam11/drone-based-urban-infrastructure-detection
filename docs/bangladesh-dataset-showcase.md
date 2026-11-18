# Original Bangladesh-Based Drone Imagery Dataset

## Why the Dataset Matters

This undergraduate research was built around a **locally collected and manually annotated aerial-imagery dataset**, rather than solely using a pre-existing public benchmark. The team collected imagery of the urban environment around **BRAC University's new campus in Merul Badda, Dhaka, Bangladesh**, with drone photography undertaken from the campus rooftop.

The collection coincided with the period surrounding BRAC University's move from Mohakhali to its new campus in Badda. The team captured the surrounding landscape at **multiple stages** to observe changes in urban infrastructure over time. This is a **multi-stage acquisition strategy**; it should not be confused with a separately validated automated temporal change-detection model.

## Historical Collection and Annotation

The final thesis presentation reports:

| Historical research measure | Reported value |
| --- | ---: |
| Raw aerial photographs | 350 |
| Drone videos | 17 |
| Image-acquisition sessions | 3 |
| Approximate interval between sessions | 2 months |
| Manual object annotations | Approximately 50,000 |
| Final research class taxonomy | 11 classes |

These are **historical figures from the team's thesis presentation**, not independently reconstructed counts from the currently available dataset ZIP files.

The research team organized drone-based collection, prepared imagery, manually annotated infrastructure objects using Roboflow, and used the resulting dataset in experiments involving YOLOv5, YOLOv7, YOLOv8, and a custom approach.

## Preserved Dataset Evidence

Two earlier Roboflow projects were recovered as dataset exports. They are useful evidence of the team's annotation workflow but **do not constitute the complete final thesis dataset**.

| Recovered project/version | Generated images | Classes | Notes |
| --- | ---: | ---: | --- |
| `aerial-image-gdys3`, version 1 | 93 | 9 | Earlier export |
| `aerial-image-gdys3`, version 2 | 96 | 9 | Includes generated/augmented training images |
| `aerial-image-2`, version 3 | 108 | 9 | YOLOv5 and YOLOv7 exports of the same version |

**Generated images are not equivalent to independent original drone photographs.** Counts from different exports should not be added together to estimate unique source images. These recovered versions also have **nine classes**, while the thesis presentation documents **eleven classes** for the later research dataset.

The dataset exports are marked **Private** in their Roboflow metadata. They are not distributed publicly here; any public sample release should be reviewed for appropriate rights and team approval.

## Annotated Examples

A small, curated selection of authentic image-and-label examples can be added here after publication rights are confirmed. The original experimental prediction figures are already available in the [experimental figure gallery](experimental-figure-gallery.md); they should not be represented as raw dataset photographs.

## Individual Contribution

**Nabila Islam Borno** contributed to dataset preparation, manual image annotation, results analysis and visualization, and research writing/documentation. Drone acquisition and the broader model experiments were **collaborative team activities**.

## Relationship to the Published Thesis

The dataset was an enabling research contribution for the comparative infrastructure-detection study, not a separate published benchmark release.

- [Main research repository](../README.md)
- [Dataset acquisition and preparation methodology](dataset-methodology.md)
- [Experimental figures](experimental-figure-gallery.md)
- [IEEE ICECE publication](https://doi.org/10.1109/ICECE64886.2024.11025116)
