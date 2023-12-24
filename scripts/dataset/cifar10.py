import torchvision.datasets as datasets

data_root = "/home/docker/Datasets/tutorial"

# Datasetクラスを継承したVisionDatasetクラスを継承しており、Datasetと同様に使用することが出来る。
# __getitem__が呼ばれた際に引数transformやtarget_transformに指定した関数を呼び出している。
train_set = datasets.CIFAR10(root=data_root, train=True, download=True)
print(train_set)

# __getitem__が呼ばれた際にTensorオブジェクトをPIL.Imageに変換して返している。
image, label = train_set[0]
print(type(image), type(label))
