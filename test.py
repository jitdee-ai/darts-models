import darmo
import torch
from collections import OrderedDict

model = darmo.create_model("relative_nas", num_classes=1000, pretrained=True)
model.reset_classifier(num_classes=100, dropout=0.2)
print(model)
