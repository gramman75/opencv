#-*-coding:utf-8-*-
"""
    #GrabCut
        - FG와 BG를 분리하는 algorithm
        - 작업순서
            . 사용자가 FG가 포함이되는 사각형 영역을 표시함.
            . 사각형 영역안은 Unknown 영역이 되고, 그 안에서 다시 사용자는 FG와 BG를 표시함.
            . Computer는 사용자가 표시한 것을 바탕으로 hard-labelling을 함.(FG와 BG의 각 Pixel에 FG/B표시를 함)
            . Gaussian Mixture Model(GMM)을 통해서 Pixel distribution을 생성함. Hard-label을 바탕으로 Unknown영역에
              대해서 probable FG, probable BG로 Labelling을 함.
            . 여기에 Source node와 Sink node를 추가하여 FG는 Source Node, BG는 Sink Node와 연결
            . 각 pixel은 Edge정보와 주변 pixel과의 유사도에 따라서 가중치가 부여됨.
            . 주변과 차이가 크면, 그 edge에 낮은 가중치를 부여함.
            . mincut algorithm을 통해서 낮은 가중치를 부여한 곳을 중심으로 cut를 하고, source node와 연결된곳은 FG,
              sink node와 연결된 곳은 BG가 됨.

    # cv2.grabCut(img, mask, rect, bdgModel, fgdModel, iterCount, mode)
        . img : Input Image
        . mask : BG/FG가 포함된 영역, cv2.GC_BGD, cv2.GC_FGD, cv2.GC_PR_BGD,cv2.GC_PR_FGD, or simply pass 0,1,2,3 to image
          return된 결과임.
        . rect : FG가 완전히 포함된 사각형 영역(x,y,w,h)
        . bdgModel, fdgModel : algorithm 내부에서 사용하는 Array. np.float64 type의 zero array(1,64) 사이즈
        . iterCount : algorithm 반복 횟수
        . mode. cv2.GC_INIT_WITH_RECT or cv2.GC_INIT_WITH_MASK or combined which decides whether
          we are drawing rectangle or final touchup strokes
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi.png')
mask = np.zeros(img.shape[:2],np.uint8)

bdgModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (50,50,355,230)

cv2.grabCut(img, mask, rect, bdgModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# mask의 값이 BG의 경우(0,2) 0으로 FG는 1로 변경
mask2 = np.where((mask ==2) | (mask==0),0,1).astype('uint8')

img = img*mask2[:,:,np.newaxis]

# 추가로 분리가 필요한 부분을 위한 manuall mask
newmask = cv2.imread('newmask.png',0)

mask[newmask == 0] = 0
mask[newmask == 255] = 1

# cv2.imshow('img',mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Mask mode적용시
mask, bdgModel, fgdModel = cv2.grabCut(img, mask, None, bdgModel, fgdModel, 5, cv2.GC_INIT_WITH_MASK)
mask  = np.where((mask==2)|(mask==0),0,1).astype('uint8')

img = img*mask[:,:,np.newaxis]


plt.imshow(img),plt.colorbar(),plt.show()



