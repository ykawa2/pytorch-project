data = ["img1", "img2", "img3", "img4", "img5"]
boxes = [
    [[1, 1, 1, 1], [10, 10, 10, 10]],
    [[2, 2, 2, 2], [20, 20, 20, 20]],
    [[3, 3, 3, 3], [30, 30, 30, 30]],
    [[4, 4, 4, 4], [40, 40, 40, 40]],
    [[5, 5, 5, 5], [50, 50, 50, 50]],
]
masks = [["mask1", "mask10"], ["mask2", "mask20"], ["mask3", "mask30"], ["mask4", "mask40"], ["mask5", "mask50"]]


class Dataset:
    def __init__(self, data, boxes, masks):
        self.data = data
        self.boxes = boxes
        self.masks = masks

    def __getitem__(self, idx):
        return self.data[idx], self.boxes[idx], self.masks[idx]

    def __len__(self):
        return len(self.data)


before_collate = (data, boxes, masks)
print("before_collate:", before_collate)

collate_fn = lambda batch: tuple(zip(*batch))
after_collate = collate_fn(before_collate)
print("after_collate:", after_collate)

# Use Dataset class
print("---------------------")
dataset = Dataset(data, boxes, masks)
before_collate = [dataset[0], dataset[1], dataset[2], dataset[3], dataset[4]]
print("before_collate:", before_collate)
after_collate = collate_fn(before_collate)
print("after_collate:", after_collate)

# 2回目のcollateでは元のデータに戻る