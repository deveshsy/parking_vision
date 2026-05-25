import os
import cv2
import json

# Define paths relative to the project root
DATASET_DIR = os.path.join("..", "dataset")
CONFIG_DIR = os.path.join("..", "config")
MODELS_DIR = os.path.join("..", "models")

def load_data():
    if not os.path.exists(DATASET_DIR):
        print(f"Error: {DATASET_DIR} not found. Please create it and add your images.")
        return
    print(f"Loading data from {DATASET_DIR}...")

def train():
    print("Training model...")
    # Add training logic here

if __name__ == "__main__":
    load_data()
    train()
