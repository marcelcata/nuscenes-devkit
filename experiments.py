from pyquaternion import Quaternion
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from nuscenes.nuscenes import NuScenes


nusc = NuScenes(version='v0.1', dataroot='/home/marcel/Documents/Datasets/NuScenes', verbose=True)

asdf = []
for i, file in enumerate(os.listdir('/home/marcel/Documents/Datasets/NuScenes/samples/CAM_FRONT')):
    if i < 3:
        asdf.append([sd for sd in nusc.sample_data if sd['filename'] == os.path.join('samples/CAM_FRONT', file)][0])
    #sd2_im = [sd for sd in nusc.sample_data if sd['filename'] == 'samples/CAM_FRONT/n015-2018-07-18-11-18-34+0800__CAM_FRONT__1531884168362460.jpg'][0]
sd1_im = asdf[0]
s1 = nusc.get('sample', sd1_im['sample_token'])
#s2 = nusc.get('sample', sd2_im['sample_token'])

# Camera
sd1 = sd1_im
#sd2 = sd2_im
_, boxes1, intrinsics = nusc.get_sample_data(sd1['token'], box_vis_level=0)
#_, boxes2, _ = nusc.get_sample_data(sd2['token'], box_vis_level=0)
box1 = boxes1[0]
#box2 = boxes2[3]
box2d = box1.box_2d(intrinsics)
#yaw2 = quaternion_yaw(box2.orientation) / np.pi * 180
#yaw_diff = yaw1 - yaw2
print(box2d)
#print(yaw2)
#print(yaw_diff)
nusc.render_sample_data(sd1['token'], box_vis_level=0)
rect = patches.Rectangle((box2d[0], box2d[1]), box2d[2]-box2d[0], box2d[3]-box2d[1],
                         linewidth=1, edgecolor='r', facecolor='none')
# rect2 = patches.Rectangle((box2d[0], box2d[3]), box2d[2]-box2d[0], box2d[3]-box2d[1],
#                          linewidth=1, edgecolor='k', facecolor='none')
# rect3 = patches.Rectangle((799, 1499), 100, 100,
#                          linewidth=1, edgecolor='b', facecolor='none')
# Add the patch to the Axes
ax = plt.gca()
ax.add_patch(rect)
#ax.add_patch(rect2)
# ax.add_patch(rect3)
plt.show()

#nusc.render_sample_data(sd2['token']); plt.show()