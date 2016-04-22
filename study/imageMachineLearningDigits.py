#-*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/digits.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cells =  [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]

x = np.array(cells)

train = x[:,50:100].reshape(-1,400).astype(np.float32)
test = x[:,:50].reshape(-1,400).astype(np.float32)

k = np.arange(10)
train_labels = np.repeat(k, 250)[:,np.newaxis]
test_labels = train_labels.copy()

knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)

ret, result, neighbours, dist = knn.findNearest(test, k=5)

matches = result==test_labels
correct = np.count_nonzero(matches)
accuracy = correct*100.0/result.size
print accuracy