# Parking Lot Analyzer

A computer vision project to detect parking slot occupancy.

## Project Structure

- `src/`: Python source files for cropping, training, and inference.
- `config/`: Configuration files (e.g., `slots.json`).
- `models/`: Trained model files (ignored by Git, except for `.gitkeep`).
- `dataset/`: Local folder for training images (ignored by Git).

## Workflow

1.  **Data Collection**: Place raw images or videos in the `dataset/` folder.
2.  **Mapping**: Run `src/crop_tool.py` to define parking slot coordinates in `config/slots.json`.
3.  **Training**: Run `src/train.py` to extract patches and train the ML model.
4.  **Inference**: Run `src/inference.py` to test the model on live or recorded footage.

## Collaboration

- **Code**: All `.py` and `.json` files are tracked via GitHub.
- **Data**: Large datasets stay local on each machine.
- **Models**: Trained model weights (`.pkl`, `.pth`) should be shared via a secure external drive/cloud storage.

## Setup

```bash
pip install -r requirements.txt
```
