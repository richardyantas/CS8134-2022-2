from PIL import Image
from matplotlib.pyplot import imshow
import cv2
import pathlib
import smart_open
import torch
from torchvision import transforms
from pathlib import Path
import json
import argparse
import numpy as np

IMG_SIZE = 256
VIDEO_DIR = pathlib.Path(__file__).resolve().parent

class DigitPredictor:
    def __init__(self) -> None:
        lit_model = torch.load("model.pt")
        lit_model.eval()
        self.scripted_model = lit_model.to_torchscript(method="script", file_path=None)

    def predict(self, image):        
        res = 28
        img_pil = Image.open(image)
        print("shape: ", img_pil.size)
        # img_pil = img_pil.resize(res)
        img_pil = img_pil.convert(mode="L") # grayscale convertion
        img_pil.show()
        transform = transforms.Compose([transforms.ToTensor()])
        img_tensor = transform(img_pil)
        print(img_tensor)
        #cv2.imshow(img)
        y_pred = self.scripted_model(img_tensor.unsqueeze(axis=0))[0]
        # print(y_pred)
        return y_pred




def main():
    # """
    # Example runs:
    # ```
    # python detector.py example.png
    # """
    parser = argparse.ArgumentParser(description="Recognize handwritten text in an image file.")
    parser.add_argument("filename", type=str)
    args = parser.parse_args()    
    digit_predictor = DigitPredictor()
    pred_str = digit_predictor.predict(args.filename)
    print("pred: ", pred_str)
    _,yhat=torch.max(pred_str,-1)
    # yhat= np.argmax(pred_str)
    print("after max: ", yhat)


if __name__ == "__main__":
    main()







