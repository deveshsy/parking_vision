import torch
import torch.nn as nn
from torchvision.models import resnet18

class RCNN(nn.Module):
    def __init__(self, roi_res=64, pooling_type='square'):
        super(RCNN, self).__init__()
        # Simplified baseline using ResNet18 as a backbone
        self.backbone = resnet18(pretrained=True)
        self.backbone.fc = nn.Linear(512, 2) # Binary classification: Empty vs Occupied

    def forward(self, x, rois):
        # In a real RCNN, we would use the ROIs to crop the image
        # This is a skeleton for the architecture
        return self.backbone(x)
