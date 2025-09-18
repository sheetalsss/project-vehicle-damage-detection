from PIL import Image
import torch
from torch import nn
from torchvision import transforms, models

class CarClassifierResNet(nn.Module):
    def __init__(self, num_classes=6, dropout_rate=0.2):
        super().__init__()
        self.model = models.resnet50(weights='DEFAULT')
        for param in self.model.parameters():
            param.requires_grad = False

            # Unfreeze layer4 and fc layers
        for param in self.model.layer4.parameters():
            param.requires_grad = True

            # Replace the final fully connected layer
        self.model.fc = nn.Sequential(
            nn.Dropout(dropout_rate),
            nn.Linear(self.model.fc.in_features, num_classes)
        )
    def forward(self, x):
        x = self.model(x)
        return x


class_names = ['Front Breakage' , 'Front Crushed', 'Front Normal', 'Rear Breakage', 'Rear Crushed', 'Rear Normal']

trained_model = None
def predict(image_path):
     image =  Image.open(image_path).convert('RGB')
     transform = transforms.Compose([
         transforms.Resize([224, 224]),
         transforms.ToTensor(),
         transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
     ])
     image_tensor =   transform(image).unsqueeze_(0) # transform(image) --> (32, 3, 224, 224)

     global trained_model
     if trained_model is None:
         trained_model = CarClassifierResNet()
         trained_model.load_state_dict(torch.load('model/saved_model.pth'))
         trained_model.eval()

     with torch.no_grad():
         output = trained_model(image_tensor)
         _, predicted_class = torch.max(output, 1)
         return class_names[predicted_class.item()]
