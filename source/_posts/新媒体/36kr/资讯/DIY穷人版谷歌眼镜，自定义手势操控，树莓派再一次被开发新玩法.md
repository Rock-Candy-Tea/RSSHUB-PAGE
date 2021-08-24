
---
title: 'DIY穷人版谷歌眼镜，自定义手势操控，树莓派再一次被开发新玩法'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210824/v2_e9351e4a236440e6b9cdb71a26300718_img_000'
author: 36kr
comments: false
date: Tue, 24 Aug 2021 09:13:20 GMT
thumbnail: 'https://img.36krcdn.com/20210824/v2_e9351e4a236440e6b9cdb71a26300718_img_000'
---

<div>   
<p>通过帅气的手势，操控投影在眼前的电子成像，这不就是科幻片里的基础配置嘛。</p> 
<p class="image-wrapper"><img data-img-size-val="640,360" src="https://img.36krcdn.com/20210824/v2_e9351e4a236440e6b9cdb71a26300718_img_000" referrerpolicy="no-referrer"></p> 
<p>现在，有人把它从科幻电影中带入了现实。动动手指，实现对眼前世界的掌控。</p> 
<p>热衷于制作智能小物件的油管博主Teemu Laurila，利用树莓派DIY了一副可识别自定义手势的AR眼镜。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,736" src="https://img.36krcdn.com/20210824/v2_15b37d833f3a4438ab3393a462b0120a_img_000" referrerpolicy="no-referrer"></p> 
<p>将自己想设置的手势录入装置，即可实现炫酷操作。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,605" src="https://img.36krcdn.com/20210824/v2_007c545ddd38411881e9db6599327588_img_000" referrerpolicy="no-referrer"></p> 
<p>我有了一个大胆的想法！</p> 
<p class="image-wrapper"><img data-img-size-val="690,720" src="https://img.36krcdn.com/20210824/v2_f00f767a144f489db5292c3bb8fd38b3_img_000" referrerpolicy="no-referrer"></p> 
<h2><strong>自制AR眼镜中的世界</strong></h2> 
<p>先开始表演吧！</p> 
<p>捏住手<a class="project-link" data-id="70487" data-name="指上" data-logo="https://img.36krcdn.com/20210807/v2_787320f8e84049c09e9afac9ee4e5070_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/70487" target="_blank">指上</a>下拉，就可以完成调整亮度指令。（这是你的第一人称视角）</p> 
<p class="image-wrapper"><img data-img-size-val="640,360" src="https://img.36krcdn.com/20210824/v2_b2c92c2474b841ac88b905233a6f7ff2_img_000" referrerpolicy="no-referrer"></p> 
<p>对手势识别，叠加显示在镜头成像中。</p> 
<p class="image-wrapper"><img data-img-size-val="640,360" src="https://img.36krcdn.com/20210824/v2_b95bccfa81ed4f03bd73a5dc60abf9e3_img_000" referrerpolicy="no-referrer"></p> 
<p>再来一个更直观点的视角，通过眼镜看看效果。</p> 
<p class="image-wrapper"><img data-img-size-val="640,360" src="https://img.36krcdn.com/20210824/v2_5a2677f618d2491d8bdb7f95cc392dd5_img_000" referrerpolicy="no-referrer"></p> 
<h2><strong>DIY过程</strong></h2> 
<p>AR眼镜本身就充满了科技感，让现实世界充满<a class="project-link" data-id="331494" data-name="赛博" data-logo="https://img.36krcdn.com/20210810/v2_ad0b14836e86460880d64547a1f1125a_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/331494" target="_blank">赛博</a>朋克的味道。</p> 
<p>那不如更炫酷一点。打个响指，就能运行命令，这不必博人传燃？</p> 
<p>说干就干，首先需要设计出，装置会包含有哪些部分。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,500" src="https://img.36krcdn.com/20210824/v2_c1d20f09d1e64c98afaaa657cff17c6c_img_000" referrerpolicy="no-referrer"></p> 
<p>除了本体眼镜框架，硬件部分还包括了<a class="project-link" data-id="518927" data-name="透镜" data-logo="https://img.36krcdn.com/20210813/v2_de35e372cb414c1494fd7cbee275d508_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/518927" target="_blank">透镜</a>组，0.6 mm PETG投影镜片，配件部分由聚乳酸材料3D打印制成。</p> 
<p>毕竟它是智能装置的DIY，怎么可以不请万能迷你电脑树莓派出场。</p> 
<p>而软件部分，手势识别程序依赖于python<a class="project-link" data-id="4262185" data-name="开源项目" data-logo="https://img.36krcdn.com/20210603/v2_43fe3145b6494227bd8db07dcdc0147b_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/4262185" target="_blank">开源项目</a><strong>MediaPipe</strong>。</p> 
<p>除此之外，Teemu Laurila还写了两个程序脚本。</p> 
<p>一个是通过捏手指控制亮度的应用示例，另一个是捕获实时视频中的手势传送到电脑进行处理，并通过智能眼镜叠加显示。</p> 
<p><strong>条件都齐了，那么动手组装起来试试。</strong></p> 
<p>经历多次调整，各部分零件最终组合成如下装置。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,774" src="https://img.36krcdn.com/20210824/v2_8f60824737d64e2caccab379f73eaa60_img_000" referrerpolicy="no-referrer"></p> 
<p>想让程序在装置上可用，首先，需要一个树莓派作为程序支持。</p> 
<p>随后设置好内存、驱动、运行环境、多媒体接口、网络等条件，让整个装置超频运行。</p> 
<p>硬件软件环境都准备好以后，调试应用程序。</p> 
<p>应用程序功能的核心——手势识别模型由3个框架组成，包括手掌识别模型BlazePalm（用于识别手的整体框架和方向）、Landmark模型（识别立体手部节点）、手势识别模型（将识别到的节点分类成一系列手势）。</p> 
<p>识别算法的训练过程中，BlazePalm模型识别手掌初始位置，对移动端的实时识别进行优化。</p> 
<p>在BlazePalm识别到的手掌范围内，Landmark模型识别其中21个立体节点坐标。</p> 
<p>手势识别模型则在此基础上，根据关节角度识别每根手指状态，将状态映射到预定义的手势上，预测基础静态手势。</p> 
<p>通过树莓派Zero W，对手势信息捕获。图像信息传输到电脑中，由手势识别AI进行处理。之后再传达给装置，发出对应的手势命令，并同步在投影图像中。</p> 
<h2><strong>它的前世今生</strong></h2> 
<p>等一下，有摄像头，有微型投影仪，还有电脑处理器，并且还是一侧投影显示。这样的AR眼镜好像在哪里见过。</p> 
<p class="image-wrapper"><img data-img-size-val="720,268" src="https://img.36krcdn.com/20210824/v2_361c854e8dab4885ad70c18824a66fae_img_000" referrerpolicy="no-referrer"></p> 
<p>没错，就连用到的手势识别代码也都是<a class="project-link" data-id="3968996" data-name="谷歌" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968996" target="_blank">谷歌</a>开源的。</p> 
<p>虽然没<a class="project-link" data-id="610396" data-name="有谷" data-logo="https://img.36krcdn.com/20210814/v2_8ae4fc1814f64be68058ae14a7e28ec4_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/610396" target="_blank">有谷</a>歌智能眼镜类似智能手机的功能，但是相比其语音控制和触控功能，Teemu Laurila的智能眼镜选择了使用自定义手势触发命令，更多一分黑科技的味道。</p> 
<p>另外，谷歌眼镜摄像头只用<a class="project-link" data-id="591302" data-name="来拍" data-logo="https://img.36krcdn.com/20210814/v2_dc3132f84ee944b5b5f179e43157f2cb_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/591302" target="_blank">来拍</a>照录像，Teemu Laurila的摄像头还承担了接受手势指令、传达指令功能。同时，投影也选择了更大尺寸的方形镜片，方便视野观察。</p> 
<p>这款装置已经是Teemu Laurila完成的第二版智能眼镜，在外观和性能上均有优化。</p> 
<p>材料的选择上，采用了0.6mm厚度投影镜片替代1mm厚度；以聚乳酸材料代替丙烯酸；增加了螺栓固定支架，弃用胶水。</p> 
<p>最重要的优化是，照相机使用方形透镜让画面更清晰。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,513" src="https://img.36krcdn.com/20210824/v2_79b6a33c267042d9a5c38b4f7b5e026d_img_000" referrerpolicy="no-referrer"></p> 
<p>Teemu Laurila将自己补充的两段代码，分享在了GitHub平台，供感兴趣的观众自己复刻。</p> 
<p>参考链接：</p> 
<p>https://www.tomshardware.com/news/raspberry-pi-smart-glasses-recognize-hand-gestureshttps://www.youtube.com/watch?v=60Os5Iqdbswhttps://www.youtube.com/watch?v=Gu4oOYo38rQ</p> 
<p>GitHub链接：</p> 
<p>https://github.com/Teneppa/CameraStreamhttps://github.com/Teneppa/HandTrackingBrightnessControl</p> 
<p class="editor-note">本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/9Jq_TdV60mqvGEdsiVHKSQ">“量子位”（ID:QbitAI）</a>，作者：兴坤，36氪经授权发布。</p>  
</div>
            