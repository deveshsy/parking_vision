import os
import torch
import torch.optim as optim
from models.rcnn import RCNN
from dataset import acpds

def main():
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    print(f"Using device: {device}")

    # Set correct path to dataset
    data_path = os.path.join("..", "dataset", "Action-Camera_Parking", "data")
    
    if not os.path.exists(data_path):
        print(f"Error: Dataset not found at {data_path}")
        print("Please follow the instructions in README.md to download and place the data.")
        return

    # Load dataset
    train_ds, valid_ds, test_ds = acpds.create_datasets(data_path)
    
    # Initialize Model
    model = RCNN().to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    print("Setup complete. Ready to begin training cycles.")

if __name__ == "__main__":
    main()
