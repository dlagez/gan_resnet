训练，将自己的数据放进data里面。

运行：

```
python train.py --epoch 200 --batchSize 128 --data_path resnetimg --outf data
```

如果你的GPU比较大的话。可以将batchSize设置的大一点，他会跑的快一点。

我在设置的时候640可能会占用一到两个G的GPU。

设置batchSize注意：

需要在model.py文件里面把batchSize设置一下。然后和上面的batchSize对应即可

![image-20211220150044711](https://cdn.jsdelivr.net/gh/dlagez/img@master/image-20211220150044711.png)

数据集下载链接：

https://drive.google.com/file/d/1fMJrg2KH0S00PO2SK8in3BArU8MbTe1J/view?usp=sharing