import torch

print("Torch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

x = torch.randn(1).cuda()
print("Tensor device:", x.device)
