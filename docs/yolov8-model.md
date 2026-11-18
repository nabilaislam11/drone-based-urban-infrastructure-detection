# YOLOv8 Trained Model Checkpoint

## Model Overview

**Artifact:** `bestv8.pt`  
**Model family:** Ultralytics YOLOv8  
**Architecture:** YOLOv8 small object-detection model  
**Research domain:** Infrastructure detection in drone-captured imagery from Bangladesh

This checkpoint is associated with the thesis research **“Enhancing Infrastructure Detection Using Drone Imagery: A Comparative Analysis Using Machine Learning Models with a Custom Bangladesh-Based Dataset for Improved Urban Planning.”**

## Training Configuration

The checkpoint records the following configuration:

| Parameter | Recorded value |
| --- | --- |
| Base model | `yolov8s.pt` |
| Training epochs configured | 100 |
| Batch size | 16 |
| Input image size | 800 |
| Number of classes | 11 |
| Ultralytics version | 8.0.196 |
| Dataset path recorded in checkpoint | `/content/datasets/Aerial-Image-new-4/data.yaml` |
| Checkpoint date | 2024-05-20 |

The values above are derived from checkpoint metadata. The configured epoch count is not, by itself, a claim that all 100 epochs completed.

## Object Classes

| ID | Class |
| --- | --- |
| 0 | Building |
| 1 | Field |
| 2 | Free space |
| 3 | Greenery |
| 4 | Human |
| 5 | Pond |
| 6 | Roads |
| 7 | Solar-Panel |
| 8 | Tin-shed-House |
| 9 | Vehicles |
| 10 | Water |

## Model Integrity

The checkpoint was compared byte-for-byte with the research artifact originally hosted separately using its Git blob identifier.

- **File:** `bestv8.pt`
- **Size:** 22,554,841 bytes
- **Git blob SHA-1:** `06edb888084dae7b3448e2d376c6e9efde25a58c`
- **SHA-256:** `431c9b9b70a3cf3194901b6eb18444a0309422d265ba6bd6c925f9f9f470c8f6`

## Related Research

- [YOLOv8 experiment configuration](experiment-configurations.md)
- [Dataset methodology](dataset-methodology.md)
- [Original research notebooks](../notebooks/)
- [IEEE ICECE publication](https://doi.org/10.1109/ICECE64886.2024.11025116)

**Security:** PyTorch checkpoints can contain serialized Python objects. Only load model weights from trusted sources in a controlled environment.
