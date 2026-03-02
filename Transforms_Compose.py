"""
範例程式碼
train_tf = transforms.Compose([
    transforms.RandomResizedCrop(224, scale=(0.7, 1.0)),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(degrees=15),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
    transforms.ToTensor(),
])
"""

"""
Python 的層級關係，其結構關係是：

torchvision      ← 套件 (package)
 └─ transforms   ← 模組 (module)
      └─ Compose ← 類別 (class)

所以 Compose 只是針對類別的定義
