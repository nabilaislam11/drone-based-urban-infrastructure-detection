# Object-Detection Experiment Configuration

This document records the experiment commands and parameters preserved in the research notebooks.

## YOLOv5

| Parameter | Notebook configuration |
| --- | --- |
| Model initialization | `yolov5s.pt` |
| Input image size | 416 |
| Batch size | 16 |
| Training epochs | 100 |
| Dataset format | Roboflow YOLOv5 export |
| Validation/inference confidence | 0.2 (detection command) |

The notebook includes dataset import, training, TensorBoard visualization, prediction, and model-weight export.

## YOLOv7

| Parameter | Notebook configuration |
| --- | --- |
| Model initialization | `yolov7.pt` |
| Input image size | 416 |
| Batch size | 16 |
| Training epochs | 40 |
| Dataset format | Roboflow YOLOv7 export |
| Validation/inference confidence | 0.2 (detection command) |

The notebook covers training, TensorBoard visualization, detection, model-weight export, and additional evaluation-related code.

## YOLOv8

| Parameter | Notebook configuration |
| --- | --- |
| Ultralytics package | `ultralytics==8.0.196` |
| Model initialization | `yolov8s.pt` |
| Input image size | 800 |
| Training epochs | 100 |
| Dataset format | Roboflow YOLOv8 export |

The notebook includes pretrained inference examples, custom-dataset training, validation, prediction, and deployment-related sections.

## Custom-Image Inference

The separate YOLOv8 categorization notebook contains inference code using a trained `bestv8.pt` checkpoint and an image-level urban categorization rule based on detected building counts.

## Dataset Versioning

The original notebooks reference different Roboflow dataset export versions: **version 1** in the YOLOv5 notebook and **version 8** in the YOLOv7 notebook. These are preserved as notebook-specific configurations, not presented as identical experimental splits.

## Research Context

The thesis compares object-detection approaches using drone-captured infrastructure imagery from Bangladesh. See [dataset methodology](dataset-methodology.md) and the [published paper](https://doi.org/10.1109/ICECE64886.2024.11025116).
