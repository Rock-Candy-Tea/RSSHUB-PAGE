
---
title: 'Kornia v0.5.4 发布！新增多个数据增广 Container'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://discuss.pytorch.org/uploads/default/original/3X/2/4/24bb0f4520f547d3a321440293c1d44921ecadf8.jpeg'
author: 开源中国
comments: false
date: Sun, 13 Jun 2021 10:12:00 GMT
thumbnail: 'https://discuss.pytorch.org/uploads/default/original/3X/2/4/24bb0f4520f547d3a321440293c1d44921ecadf8.jpeg'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align: start;">本次Kornia 的更新中，主要增加对Canny的支持以及新增了多种图像处理容器（例如，视频容器，图像增广容器）。</p> 
<p style="text-align: start;">例如对于数据增广中的各种常见格式（mask, bbox, keypoints），以及图像变换的inverse：</p> 
<pre><code class="language-python">aug_list = AugmentationSequential(
    K.ColorJitter(0.1, 0.1, 0.1, 0.1, p=1.0),
    K.RandomAffine(360, [0.1, 0.1], [0.7, 1.2], [30., 50.], p=1.0),
    K.RandomPerspective(0.5, p=1.0),
    data_keys=["input", "bbox", "keypoints", "mask"],  # Just to define the future input here.
    return_transform=False,
    same_on_batch=False,
)
# forward the operation
out_tensors = aug_list(img_tensor, bbox, keypoints, mask)
# Inverse the operation
out_tensor_inv = aug_list.inverse(*out_tensor)</code></pre> 
<h3 style="text-align:start"><img alt height="190" src="https://discuss.pytorch.org/uploads/default/original/3X/2/4/24bb0f4520f547d3a321440293c1d44921ecadf8.jpeg" width="1100" referrerpolicy="no-referrer"></h3> 
<p>此外，我们新增了PatchAugmentSequential来支持更多最新的图像增强方法。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-9276525c48bb7185b90bb32e598e23f8e49.png" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">[0.5.4] - 2021-06-11</h3> 
<h3 style="text-align:start">Added</h3> 
<ul> 
 <li>Add Canny edge detection (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkornia%2Fkornia%2Fpull%2F1020" target="_blank">#1020</a>)</li> 
 <li>Added Batched forward function (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkornia%2Fkornia%2Fpull%2F1058" target="_blank">#1058</a>)</li> 
 <li>Added denormalize homography function <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkornia%2Fkornia%2Fpull%2F1061" target="_blank">(#1061</a>)</li> 
 <li>Added more augmentations containers (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkornia%2Fkornia%2Fpull%2F1014" target="_blank">#1014</a>)</li> 
 <li>Added calibration module and Undistort 2D points function (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkornia%2Fkornia%2Fpull%2F1026" target="_blank">#1026</a>)</li> 
 <li>Added patch augmentation container (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkornia%2Fkornia%2Fpull%2F1095" target="_blank">#1095</a>)</li> 
</ul> 
<h3 style="text-align:start">Fixed</h3> 
<ul> 
 <li>Remove lena (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkornia%2Fkornia%2Fpull%2F1059" target="_blank">#1059</a>) :)</li> 
</ul> 
<h3 style="text-align:start">Changed</h3> 
<ul> 
 <li>Resize regardless of number of dims, considering the last two dims as image (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkornia%2Fkornia%2Fpull%2F1047" target="_blank">#1047</a>)</li> 
 <li>Raise error if converting to unit8 image to gray with float weights (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkornia%2Fkornia%2Fpull%2F1057" target="_blank">#1057</a>)</li> 
 <li>Filter 2D->2d, 3D->3d (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkornia%2Fkornia%2Fpull%2F1069" target="_blank">#1069</a>)</li> 
 <li>Removed augmentation functional module. (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkornia%2Fkornia%2Fpull%2F1067" target="_blank">#1067</a>)</li> 
 <li>Make Morphology compatible with both OpenCV and Scipy (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkornia%2Fkornia%2Fpull%2F1084" target="_blank">#1084</a>)</li> 
</ul>
                                        </div>
                                      
</div>
            