
---
title: '可模拟金属动态光影，苹果研发移动端HDR AR渲染方案'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210701/v2_caf98a741731421f8aac8d5eca055b63_img_000'
author: 36kr
comments: false
date: Thu, 01 Jul 2021 10:34:11 GMT
thumbnail: 'https://img.36krcdn.com/20210701/v2_caf98a741731421f8aac8d5eca055b63_img_000'
---

<div>   
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/55U3CKQ7epfVdrxAsVb11g">“青亭网”（ID:qingtinwang）</a>，编辑：Esther，36氪经授权发布。</p> 
<p class="image-wrapper"><img data-img-size-val="742,400" src="https://img.36krcdn.com/20210701/v2_caf98a741731421f8aac8d5eca055b63_img_000" referrerpolicy="no-referrer"></p> 
<p>丰富的光影细节对于一张好照片来说足够重要，为了接近拍出接近人眼视觉的照片，市面上越来越多的相机、手机摄像头开始支持HDR功能，也就是高动态光照渲染技术。其中，动态范围指的是更多样的光线变化，也就是说HDR照片比普通照片对光的感知范围更大，更讨好人眼的视觉习惯。</p> 
<p class="image-wrapper"><img data-img-size-val="654,365" src="https://img.36krcdn.com/20210701/v2_fa96526ef17f4cb3afc6806e4659ce21_img_png" referrerpolicy="no-referrer"></p> 
<p>与普通的呈现技术相比，HDR图像可显示更多动态范围和细节，其原理是通过拍摄多种不同曝光版本（LDR）的照片，然后通过实时后期处理，将三张照片合成为一张。</p> 
<p>不仅如此，iPhone 12 Pro系列也是苹果首款同时支持拍摄剪辑和显示HDR视频能力的移动设备。这样一来假如将HDR与AR结合，那么iPhone 12系列还是无敌的存在，奈何当前用户感知还不是很强。</p> 
<p>那么，HDR是否能进一步提升AR图像的逼真感，让AR更融入真实场景呢？</p> 
<h2>移动端HDR AR方案</h2> 
<p>近期，苹果计算机视觉科研部门研发了一种基于HDR图像技术的AR渲染方案，其特点是无需重复训练，即可在各种新场景中动态渲染AR模型表面的反光/光影效果，逼真模拟金属等自然纹理。据悉，在一篇名为《基于HDR环境映射预测的实时AR技术》的论文中，苹果计算机视觉研发工程师Gowri Somanath和高级机器学习经理Daniel Kurz提出，该方案基于一种支持AR实时渲染、动态HDR效果的卷积神经网络EnvMapNet，该网络模型可在移动端处理器运行，在3D扫描场景后，可渲染出接近实物、支持动态场景感知的AR。</p> 
<p>在iPhone XS上运行时，延迟可低于9毫秒，而与此前已有的渲染方案相比，该方案渲染光线反射的方向误差可降低50%。</p> 
<p>简单来讲，采用卷曲神经网络的原因是，由于手机摄像头比人眼视场角更窄，因此只能通过摄像头捕捉到的有限场景数据去预测完整的360°场景。EnvMapNet不仅可以预测3D场景中的光影信息，还可以合成高分辨率的完整场景。</p> 
<p>科研人员表示：移动端AR渲染的局限在于，摄像头的视场角和移动范围有限，通常可捕捉的范围不到100°。相比之下，人眼的视场角要高得多，因此为了渲染视觉观感自然的AR效果，EnvMapNet需要同时预测出摄像头未捕捉到的场景数据。</p> 
<p>其原理是，通过有限视野的LDR（低动态光照渲染）摄像头成像（部分场景图），实时预测并渲染HDR场景（完整场景图），可为AR物体模拟视觉感官逼真的光影效果。换句话来讲，就是可以让AR模拟镜面或漫反射在不同光照环境中的动态变化。</p> 
<p>此外，EnvMapNet合成的3D场景中不仅包含环境光的强度和温度等低频信息，还包括光源类型（吊灯等等）更多细节。接着，利用生成对抗网络（GANs），EnvMapNet所生成的3D场景将支持环境感知，也就是说可以适用于多种不同的场景。</p> 
<h2>可在iPhone XS上运行</h2> 
<p>EnvMapNet的另一个特点是，由于是通过LDR图像预测HDR场景，它不依赖很高端的硬件配置。</p> 
<p class="image-wrapper"><img data-img-size-val="400,225" src="https://img.36krcdn.com/20210701/v2_c3675d3e569640dc9fa18ccc7ec59eac_img_000" referrerpolicy="no-referrer"></p> 
<p>实际上，通过16核神经网络引擎和GPU渲染，搭载A14仿生芯片的iPhone 12，已经足以处理HDR多帧合成任务。可以说，iPhone 12 Pro已经是能够拍摄、显示HDR内容的完美消费级设备，与此同时，AR将成为拍摄和显示HDR的重要延伸场景。尤其是通过iPhone 12 Pro搭载的LiDAR传感器模组，3D扫描和AR模型生成的效果又将进一步提升。</p> 
<p class="image-wrapper"><img data-img-size-val="400,201" src="https://img.36krcdn.com/20210701/v2_0719ca60c4324fd68da981bf65f05b82_img_000" referrerpolicy="no-referrer"></p> 
<p>不过，为了进一步探索EnvMapNet的通用性，科研人员在iPhone XS上测试运行一个基于ARKit的iOS原型应用，通过ARKit提供的设备姿态和平面几何数据，将摄像头捕捉的图像弯曲成部分环境图，接着再将预测的完整环境图通过SceneKit框架来渲染AR模型，发现预测时间仅需9毫秒。</p> 
<p>此外，苹果科研人员指出，EnvMapNet在iPhone XS上可实现逼真的反光效果，与此前已有的渲染方案相比，该方案渲染光线反射的方向误差可降低50%。</p> 
<p class="image-wrapper"><img data-img-size-val="467,293" src="https://img.36krcdn.com/20210701/v2_575b631eb94e4b028ff825b4655187a9_img_000" referrerpolicy="no-referrer"></p> 
<p>细节方面，该方案的运行流程是首先对周围场景进行扫描，然后卷曲神经网络EnvMapNet根据ARKit框架收集的图像帧、姿态、场景几何和AR定位信息，来预测HDR影像的完整立体图像，这种计算方式也被称为IBL，即：基于图像的光照技术。而生成的完整立体图像则被称为：光照探头（似乎是一个3D开发术语），其中包含高分辨率反射纹理、场景中的光源预测结果。接下来，该立体图像会继续识别场景中各种光源强度，并计算出渲染时亮度的占比。</p> 
<p class="image-wrapper"><img data-img-size-val="651,395" src="https://img.36krcdn.com/20210701/v2_4e09936fa77446c3af5e0a77e8a99e04_img_png" referrerpolicy="no-referrer"></p> 
<p>在拍摄特效电影时，片场的工作人员会将一个金属球体作为参考，通过捕捉球面的反光效果，来反向拆解3D环境的亮度变化，也就是HDRI图像。然后在利用生成的HDRI图像来重建逼真的CGI场景。据悉，《终结者2》中的液态金属效果就是利用类似的技术来模拟的。</p> 
<h2>其他应用场景</h2> 
<p>除了AR外，EnvMapNet算法或许也可以与神经渲染结合，应用场景包括：基于神经渲染的3D动态头像、3D地图模型、游戏场景渲染等等。此前，为了研发逼真的3D地图渲染方案，<a class="project-link" data-id="3968996" data-name="谷歌" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968996" target="_blank">谷歌</a>科研人员训<a class="project-link" data-id="633086" data-name="练了" data-logo="https://img.36krcdn.com/20201112/v2_a8d3a45e971d496eacb7f53636d21150_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/633086" target="_blank">练了</a>一个基于NeRF（神经辐射场）的学习算法，通过分析光线总之的位置，从2D图像提取3D深度，并生成3D效果图。如果在NeRF算法基础上，加入HDR渲染技术，或许可以模拟CGI的全局照明效果，实现对场景的动态光影渲染。</p> 
<p>相比之下，HDR模拟技术似乎也能用于实现基于神经学习的反光效果模拟，从而优化3D模型、场景的视觉效果。</p> 
<p class="image-wrapper"><img data-img-size-val="400,222" src="https://img.36krcdn.com/20210701/v2_666d89a005924e8ab635b713f2ecd81b_img_000" referrerpolicy="no-referrer"></p> 
<p>注：神经渲染是一种图像和视频生成方案，其特点是基于深度生成模型和图形学领域的光学物理特性，可通过显性或隐性的方式，去调整图像中场景的亮度、摄像头参数、姿态、几何、外观和语义结构。应用场景包括电影工业、AR/VR、智慧城市等等。</p> 
<p class="image-wrapper"><img data-img-size-val="738,395" src="https://img.36krcdn.com/20210701/v2_66a2533985a442af9c3fc9f59d9b4b14_img_000" referrerpolicy="no-referrer"></p> 
<p>总之，随着AR定位和渲染等技术不断发展，AR已经可以模拟实时遮挡、物理交互等真实物体的效果。同时，苹果持续投资AR技术开发，此前还发布基于USDZ的AR快速查看功能，以及快速生成高质量3D扫描模型的功能：Object Capture API。未来，如果苹果将HDR光影渲染用于移动端AR或AR眼镜，那么AR可能会与真实场景越来越难以区分。</p> 
<p>参考：</p> 
<p>https://www.unite.ai/can-apples-hdr-augmented-reality-environments-solve-reflections-for-neural-rendering/</p>  
</div>
            