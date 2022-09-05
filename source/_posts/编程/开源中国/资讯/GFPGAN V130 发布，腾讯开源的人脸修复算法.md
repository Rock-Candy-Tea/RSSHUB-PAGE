
---
title: 'GFPGAN V1.3.0 发布，腾讯开源的人脸修复算法'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0905/070709_NNF9_5430600.png'
author: 开源中国
comments: false
date: Mon, 05 Sep 2022 07:07:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0905/070709_NNF9_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">GFPGAN 是腾讯开源的人脸修复算法，它利用预先训练好的面部 GAN（如 StyleGAN2）中封装的丰富和多样的先验因素进行盲脸 (blind face) 修复，旨在开发用于现实世界人脸修复的实用算法。</span></p> 
<p><img alt height="369" src="https://static.oschina.net/uploads/space/2022/0905/070709_NNF9_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p>目前 GFPGAN V1.3.0 发布了，带来如下改动：</p> 
<ul> 
 <li>添加 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencentARC%2FGFPGAN%2Freleases%2Fdownload%2Fv1.3.0%2FGFPGANv1.3.pth" target="_blank">V1.3 模型</a>，它可以产生<strong>更自然的</strong>恢复结果，并且在非常低质量/高质量的输入上产生更好的结果。</li> 
 <li>添加“双线性”架构，这是清洁架构的原始架构，可以用来微调模型。</li> 
 <li>添加<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fapp.baseten.co%2Fapplications%2FQ04Lz0d%2Foperator_views%2F8qZG6Bg" target="_blank">c068e4d</a>提供的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencentARC%2FGFPGAN%2Fcommit%2Fc068e4d113ebbca1f624e4e90854d21601f9c2ef" target="_blank">baseten.co demo</a></li> 
</ul> 
<p>此版本还存储以下预训练模型</p> 
<ul> 
 <li>GFPGAN v1.3.pth</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencentARC%2FGFPGAN%2Freleases%2Ftag%2Fv1.3.0" target="_blank">https://github.com/TencentARC/GFPGAN/releases/tag/v1.3.0</a></p>
                                        </div>
                                      
</div>
            