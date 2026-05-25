import torch
from torchvision import transforms as T

def preprocess(image):
    normalize = T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    transform = T.Compose([
        T.Resize((224, 224)),
        normalize,
    ])
    return transform(image)
