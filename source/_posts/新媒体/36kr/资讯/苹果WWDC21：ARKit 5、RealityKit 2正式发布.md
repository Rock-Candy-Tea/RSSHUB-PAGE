
---
title: '苹果WWDC21：ARKit 5、RealityKit 2正式发布'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210608/v2_740c36e28933471190da32582978c7d9_img_000'
author: 36kr
comments: false
date: Tue, 08 Jun 2021 05:45:21 GMT
thumbnail: 'https://img.36krcdn.com/20210608/v2_740c36e28933471190da32582978c7d9_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/7FvAOJiQtMa92P6X7yWoeA">“青亭网”（ID:qingtinwang）</a>，编辑：hi188，36氪经授权发布。</p> 
<p><img src="https://img.36krcdn.com/20210608/v2_740c36e28933471190da32582978c7d9_img_000" data-img-size-val="1080,610" referrerpolicy="no-referrer"></p> 
<p>在今天凌晨举行的WWDC21上，苹果正式发布家族四大操作系统的全新版本，其在很多细节进行更新迭代，很多功能也比较有意思，例如SharePlay多人共享、专注模式等等。</p> 
<p>虽然新的功能没有预期中给力，但是苹果自己在应用和设备互动生态中的玩法也已经凸显了出来。例如，用Mac的键鼠可以无缝接管iPad，实现无缝管理、文件传输等等。</p> 
<p>不过，还是希望苹果在OS稳定性上多花功夫，iOS发热、续航问题被诟病已久。</p> 
<p><img src="https://img.36krcdn.com/20210608/v2_119a4b8cc35d4f9292690ad83b875447_img_000" data-img-size-val="800,451" referrerpolicy="no-referrer"></p> 
<p>话说回来，苹果每年一度的ARKit开发工具依旧在WWDC<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>更新，只不过最新的ARKit 5并没有出现在主会场中，一度让人们忘记了它的存在。与此同时，AR开发框架RealityKit 2也同期更新。</p> 
<p>同时，苹果已经是世界上最大的AR平台，支持AR的苹果设备已经超过10亿台。下面我们来看看它们都有什么新功能。</p> 
<h2>ARKit 5</h2> 
<p>之所以没放在主会场，还是因为整体功能点太少了。其中ARKit 5带来的新功能主要有两点：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>位置锚定支持更多地区；</p></li> 
 <li><p>人脸追踪功能升级；</p></li> 
 <li><p>改进运动追踪。</p></li> 
</ul> 
<p>首先，位置锚定功能最初出现在ARKit 4中，它的特点就是结合地理的经纬度、海拔信息实现虚拟物体的持久性锚定，此前仅能在美国少数城市使用。而最新的ARKit 5则支持美国更多城市（疑问中，官方文档尚未查到，该功能应和苹果地图高度绑定），同时伦敦也支持。注意：这一功能仅支持iPhone XS，iPhone XS Max，iPhone XR或更新机型。</p> 
<p><img src="https://img.36krcdn.com/20210608/v2_3312818d5bbc4a1ca41a8d504cb4b055_img_000" data-img-size-val="800,449" referrerpolicy="no-referrer"></p> 
<p>同时苹果提到，你可以将轻应用、或AR本地应用中的虚拟物体分享，方式是通过App Clip Code二维码。这样，附近的其他玩家只需扫描二维即可快速查看虚拟物体。</p> 
<p>怎么感觉就这一点支撑不起来一个新版本号迭代，毕竟自从ARKit 4和ARKit 5的新特性实在太少。</p> 
<p>面部追踪方面，ARKit中人脸追踪支持更多配备A12芯片的设备，例如iPhone SE也支持前置摄像头的人脸追踪功能。同时，最新的iPad Pro 2021前置采用超广角摄像头，ARKit 5同样支持。</p> 
<p>与此同时，在配备原深感相机（Face ID）的设备中，ARKit 5将同时支持3个面部信息。</p> 
<h2>RealityKit 2</h2> 
<p>在主会场中，重点介绍了一下Object Capture API，这应该也是RealityKit 2的重要更新。</p> 
<p>相信不少人还记得，苹果LiDAR在iPad Pro 2020出现后很多人都在尝试基于LiDAR的3D建模。显然苹果当时并没<a class="project-link" data-id="1205494" data-name="有充" data-logo="https://img.36krcdn.com/20210409/v2_e00365c18c634083adc7020e946f88bc_img_000" data-refer-type="1" href="https://p.36kr.com/space/3436012335" target="_blank">有充</a>分发挥LiDAR的实力，以至于很多第三方App都主打3D扫描，但效果一般。以至于我们在介绍LiDAR时，感觉非常吃力。直到现在，我们依然只能说LiDAR开启苹果房间级AR体验。</p> 
<p>RealityKit 2的目标依然是打造超逼真、照片级的渲染、动画、物理交互等效果，可结合ARKit、Swift API、人体骨骼追踪、空间音频、姿态追踪等让AR开发变得更轻松。</p> 
<p><img src="https://img.36krcdn.com/20210608/v2_163e7316766646879fd2f4b23b6171c3_img_000" data-img-size-val="659,283" referrerpolicy="no-referrer"></p> 
<p>RealityKit 2新功能如下：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>3D扫描；</p></li> 
 <li><p>自定义着色器；</p></li> 
 <li><p>动态加载方式；</p></li> 
 <li><p>系统模块定制；</p></li> 
 <li><p>虚拟角色控制器。</p></li> 
</ul> 
<p>Object Capture将会让众多第三方3D扫描应用得到更好的体验，对3D创作者而言也会缩短流程，提高效率。</p> 
<p><img src="https://img.36krcdn.com/20210608/v2_286d9d485a7a4703b2f702f9dba8229b_img_000" data-img-size-val="800,449" referrerpolicy="no-referrer"></p> 
<p>根据苹果Object Capture文档，这个API实际上是属于macOS Monterey，也就是电脑端的API。它需要不同角度的照片即可生成高质量3D模型，可以借助iPhone或iPad，也可以是单反相机，然后再回到Mac进行3D模型的输出。</p> 
<p><img src="https://img.36krcdn.com/20210608/v2_0ae84314c4684e6297ed61a32cfe40fd_img_000" data-img-size-val="800,465" referrerpolicy="no-referrer"></p> 
<p>苹果号称，Object Capture可在几分钟内即可输出高质量3D模型，也就是USDZ，理所当然的也支持AR快速预览，导入Reality Composer或其它工具。</p> 
<p><img src="https://img.36krcdn.com/20210608/v2_a4238bc8c9f341c1be82127e1ff69bd7_img_000" data-img-size-val="800,448" referrerpolicy="no-referrer"></p> 
<p>自定义着色器可以实现更高级的渲染能力，基于高清3D模型，基于物理环境、环境光反射，阴影，相机噪点、运动模糊等可以让虚拟物体和现实环境更融合。</p> 
<p>此外，苹果还强调了基于ARKit 5的轻应用（App Clips）模式。相关阅读：《<a href="http://mp.weixin.qq.com/s?__biz=MzIxOTI0MjYyNg==&mid=2651567698&idx=1&sn=c55e0e8b6d2390563a3f6f2196f3d418&chksm=8c215fbfbb56d6a9326607ad221d54e6eea39a6c8018d224702e2b569f4d5594f47fb3ef7d13&scene=21#wechat_redirect">苹果AR主管：轻应用才是杀手级的AR体验</a>》。</p> 
<h2>地图AR导航</h2> 
<p>另外，苹果地图也在推进更新，其中涉及到AR的一个功能是支持AR导航，当你不知道方向时，可以直接拿iPhone扫描周边环境和建筑物，即可进行定位。据悉，该功能尽在配备A12或更新芯片的设备中提供支持。</p> 
<p><img src="https://img.36krcdn.com/20210608/v2_277fb200253540348877c82d34d2d369_img_000" data-img-size-val="800,494" referrerpolicy="no-referrer"></p> 
<p>支持AR导航的城市截止到今年底包括：伦敦、洛杉矶、纽约、费城、圣地亚哥、加利福尼亚海湾地区、华盛顿。</p>  
</div>
            