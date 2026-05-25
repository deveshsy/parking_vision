# Parking Lot Analyzer

A computer vision project to detect parking slot occupancy.

## Project Structure

- `src/`: Python source files for cropping, training, and inference.
- `config/`: Configuration files (e.g., `slots.json`).
- `models/`: Trained model files (ignored by Git, except for `.gitkeep`).
- `dataset/`: Local folder for training images (ignored by Git).

## Dataset

We are using the **Action-Camera Parking** dataset from OpenDataLab (~727MB).

1.  Download the dataset from: [OpenDataLab Link](https://opendatalab.com/OpenDataLab/Action-Camera_Parking)
2.  Extract it into the `dataset/` folder.
3.  Ensure the folder name is `Action-Camera_Parking`.

**DO NOT commit the dataset folder to GitHub.** The `.gitignore` file is already set up to prevent this.

## Collaboration

- **Code**: All `.py` and `.json` files are tracked via GitHub.
- **Data**: Large datasets stay local on each machine.
- **Models**: Trained model weights (`.pkl`, `.pth`) should be shared via a secure external drive/cloud storage.

## Setup

```bash
pip install -r requirements.txt
```
