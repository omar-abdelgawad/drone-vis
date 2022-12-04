from typing import List
from dronevis.config.config import COCO_NAMES
from torchvision.transforms.functional import to_pil_image
from torchvision.models.detection import (
    fasterrcnn_mobilenet_v3_large_320_fpn,
    FasterRCNN_MobileNet_V3_Large_320_FPN_Weights
)
from dronevis.object_detection_models import TorchDetectionModel

class FasterRCNNTorch(TorchDetectionModel):
    def __init__(self) -> None:
        """Initialize faster R-CNN model"""
        super(FasterRCNNTorch, self).__init__()
        self.weights = FasterRCNN_MobileNet_V3_Large_320_FPN_Weights.DEFAULT
        self.transform = self.weights.transforms()


    def load_model(self):
        """Load model from PyTorchHub

        Args:
            model_path (str, optional): no need to use it, only for integrity with absract class. Defaults to None.
        """
        print("Loading Faster R-CNN model ...")
        self.net = fasterrcnn_mobilenet_v3_large_320_fpn(weights=self.weights)
        self.net = self.net.eval().to(self.device)


if __name__ == "__main__":
    model = FasterRCNNTorch()
    model.load_model()
    model.detect_webcam()
