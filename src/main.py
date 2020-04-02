import os
import sys

import numpy as np
import torch
from torchvision import transforms
from PIL import Image
from torch.autograd import Variable

from train import CustomConvNet

if __name__ == "__main__":
    weights_file = './model.pth'
    image_source = './sibal.jpg'
    print("Sibal")
    device = torch.device('cpu')
    model = CustomConvNet()
    model.load_state_dict(torch.load(weights_file, map_location=device))
    model.eval()

    transformation = transforms.Compose([transforms.Resize((128, 128)),
                                         transforms.RandomRotation(10.),
                                         transforms.ToTensor()])
    image = Image.open(image_source)
    image = image.resize((342, 256))
    image.save('./temp.png')
    image = transformation(image)[:1]

    data = Variable(image, volatile=True)
    data = data.unsqueeze(0)

    pred = model(data).argmax(dim=1)[0].item()
    print(pred)
