# Reproducibility Guide

This guide documents how to inspect and reproduce the original undergraduate research experiments. It is based on the preserved notebooks and the verified YOLOv8 checkpoint; it does **not** claim that all historical experiments have been rerun in the current environment.

## Research Artifacts

| Artifact | Repository location | Purpose |
| --- | --- | --- |
| YOLOv5 notebook | [Original YOLOv5 notebook](../notebooks/YoloV5_Aerial%20Image.ipynb) | Dataset import, training, and detection |
| YOLOv7 notebook | [Original YOLOv7 notebook](../notebooks/Yolo_v7.ipynb) | Dataset import, training, and detection |
| YOLOv8 notebook | [Original YOLOv8 notebook](../notebooks/V2_yolov8_object_detection_on_our%20custom_dataset.ipynb) | Dataset import, training, validation, and prediction |
| Custom-image inference | [Original inference notebook](../notebooks/Categorization%20v8_trained%20best.pt%20and%20custom%20image.ipynb) | Detection using trained YOLOv8 weights |
| Trained YOLOv8 weights | [bestv8.pt](../bestv8.pt) | Preserved checkpoint |
| Original figures | [Experimental figure gallery](experimental-figure-gallery.md) | Visual results from the final thesis presentation |

## Dataset Provenance and Versioning

The notebooks reference these distinct Roboflow datasets and versions:

| Experiment | Roboflow workspace | Project | Version | Export |
| --- | --- | --- | --- | --- |
| YOLOv5 | `thesis-9qcbz` | `aerial-image-2` | 1 | `yolov5` |
| YOLOv7 | `thesis-9qcbz` | `aerial-image-2` | 8 | `yolov7` |
| YOLOv8 | `aerial-image-3` | `aerial-image-new` | 4 | `yolov8` |

These are the versions referenced in the original source notebooks. **They must not be represented as the same export or as guaranteed identical training/validation/test splits.** Access to the source dataset exports is subject to the relevant Roboflow project permissions.

## Experiment Commands

The following commands are preserved here for technical reference. They assume the corresponding model repositories, dependencies, and dataset exports have already been prepared.

### YOLOv5

```bash
python train.py --img 416 --batch 16 --epochs 100 --data /path/to/yolov5-export/data.yaml --weights yolov5s.pt --cache
```

### YOLOv7

```bash
python train.py --img 416 --batch 16 --epochs 40 --data /path/to/yolov7-export/data.yaml --weights yolov7.pt --cache
```

### YOLOv8

The original notebook installs `ultralytics==8.0.196` and uses:

```bash
yolo task=detect mode=train model=yolov8s.pt data=/path/to/yolov8-export/data.yaml epochs=100 imgsz=800 plots=True
```

The preserved YOLOv8 checkpoint records a batch size of 16. Configured epochs do not by themselves establish how many epochs actually completed.

## Inference with the Preserved YOLOv8 Checkpoint

The original custom-image notebook uses the trained `bestv8.pt` file for prediction. In a compatible environment with a trusted checkpoint and the appropriate Ultralytics version, a local inference command is:

```bash
yolo task=detect mode=predict model=bestv8.pt source=/path/to/image.jpg save=True
```

Run commands from the repository root or adjust paths accordingly. This is an example workflow, **not a claim that inference has been executed or validated in a fresh environment**.

## Credential Handling

The preserved historical notebooks include hardcoded Roboflow credentials. **Do not reuse those credentials.** The project owner should revoke/rotate the exposed credentials in Roboflow before sharing or executing the notebooks.

For any new reproduction workflow, load a newly issued credential from a private environment variable or secret manager, rather than committing it to a notebook or source file. Removing a secret from the current file does not remove it from prior Git commits; repository history requires separate remediation.

## Interpretation

The experiments reflect the original thesis team's research workflow. Numerical comparison across different runs requires checking dataset versions, splits, class mappings, preprocessing, and evaluation settings. The [original results gallery](experimental-figure-gallery.md) provides preserved research figures; it should not be mistaken for a newly standardized benchmark.

**Publication:** [IEEE ICECE 2024 paper](https://doi.org/10.1109/ICECE64886.2024.11025116).
