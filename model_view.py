from model import netD, netG
from torchsummary import summary
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
netG = netG().to(device)

summary(netG, (8, 3, 64, 64))
print(netG)