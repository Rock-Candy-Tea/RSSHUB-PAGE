
---
title: '开发淘宝双 11 喵糖的 Eva.js v1.2 版本正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0cbb21841520f0e1cc041ff1272f7d8abe1.png'
author: 开源中国
comments: false
date: Wed, 22 Dec 2021 15:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0cbb21841520f0e1cc041ff1272f7d8abe1.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://eva-engine.gitee.io/" target="_blank"><em><span>Eva.js</span></em></a><em><span><span> </span>v1.2</span></em><span><span> </span>版本正式发布，本版本是双11喵糖的使用版本。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>欢迎使用<span> </span></span><em><span>Eva.js v1.2<span> </span></span></em><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js" target="_blank"><em><span>GitHub</span></em></a><em><span>!</span></em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>本次版本主要支持了</span><strong><span>压缩纹理</span></strong><span>的渲染，首要解决GPU内存压力。支持实时修改</span><strong><span>游戏播放速度</span></strong><span>，增加更多表现力。新增</span><strong><span><span> </span></span></strong><strong><em><span>Spine4.0<span> </span></span></em></strong><span>的支持，并且抽离了spine的公共文件，降低多个 Spine 版本功能同步的成本。提供</span><strong><span>扩展type的能力</span></strong><span>，插件开发可增加对引擎核心能力的扩展。为交互事件提供相对于</span><strong><span>当前对象的点击位置</span></strong><span>。优化帧动画能力，可</span><strong><span>停止在最后一帧</span></strong><span>。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>主要</span><strong><span>修复了一些常见问题</span></strong><span>，Spine 在特定参数下无法播放问题，资源加载进度问题以及A11y的DOM层级问题。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>在生态方面，</span><strong><span>支持淘宝/支付宝小程序</span></strong><span>中运行，IIFE支持</span><strong><span>微信小游戏</span></strong><span>中使用Eva.js。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>Eva.js v1.2 已在以下项目中使用：</span><strong><span>淘宝双11 / 芭芭农场 / 淘宝斗地主 / 薅羊毛赚话费</span></strong><span>，目前版本已经升级到1.2.2，我们一般在自己的业务中验证大版本稳定性，在进行正式发布。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>感谢各个</span><strong><span>兄弟团队</span></strong><span>和</span><strong><span>业界伙伴</span></strong><span>的信赖，正是大家的信赖，Eva.js 才能做到更加丰富的</span><strong><span>表现力</span></strong><span>、更加优质的</span><strong><span>性能</span></strong><span>、更加流畅的</span><strong><span>开发体验</span></strong><span>。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="238" src="https://oscimg.oschina.net/oscnet/up-0cbb21841520f0e1cc041ff1272f7d8abe1.png" width="1032" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>重点特性介绍</span></h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>压缩纹理</span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#1c1e21">常见的图片文件格式，比如PNG/JPEG/Webp等，是为了存储图像信息的特殊编码方式，只能存在硬盘中或内存中，无法被GPU直接识别。纹理压缩格式，是一种GPU能直接读取并显示的格式，使得图像无需解压即可进行渲染，节约大量的内存。</span><a href="https://eva-engine.gitee.io/docs/tutorials/compressedTexture" target="_blank"><span>点击进入压缩纹理文档</span></a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>可以通过官方提供的<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Ftexture-compressor" target="_blank"><span>texture-compressor</span></a><span><span> </span>工具生成压缩纹理文件。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#1c1e21">阿里巴巴内网用户结合<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Feva.alibaba-inc.com" target="_blank"><span>EVA Store</span></a><span style="color:#1c1e21">提供的资源管理能力，点击<span> </span></span><strong><span style="color:#1c1e21">预览代码</span></strong><span style="color:#1c1e21"><span> </span>可以直接生成压缩纹理并且直接提供 Eva.js 支持的代码。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="400" src="https://oscimg.oschina.net/oscnet/up-a876471d33c43e70bab5ec894803e702910.png" width="708" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>游戏播放速度控制</span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://eva-engine.gitee.io/docs/tutorials/game#%E4%BF%AE%E6%94%B9%E6%B8%B8%E6%88%8F%E6%92%AD%E6%94%BE%E9%80%9F%E5%BA%A6" target="_blank"><span>播放速度文档</span></a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>通过控制游戏播放速度，可以实现更丰富的游戏效果。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="714" src="https://oscimg.oschina.net/oscnet/up-cd0d290e9097452cd53e3d4af1baa87e84c.gif" width="738" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>淘宝/支付宝小程序</span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#e4f7d2">Eva.js@^1.2.2</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>Evs.js 现已支持淘宝/支付宝小程序中互动游戏的开发。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="960" src="https://oscimg.oschina.net/oscnet/up-d7b6a5d6c8ff828e5390af7cef936b47ec9.gif" width="448" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>微信小游戏</span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva-multi-platform-demo" target="_blank">EVA小游戏开发脚手架</a>，通过微信weapp-adapter快速支持小程序，虽然需要使用IIFE的方式引入Eva.js文件，但能够顺利渲染成功，为未来生态扩展提供一个可行性方案。</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>升级内容概览</span></h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>能力</span></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span>压缩纹理支持<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F84" target="_blank"><span>#84</span></a></li> 
 <li><span>游戏播放速度控制<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F132" target="_blank"><span>#132</span></a></li> 
</ul> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span>新增Spine4.0支持，同时支持Spine 3.6/3.8/4.0，抽离Spine公共部分<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F154" target="_blank"><span>#154</span></a></li> 
 <li><span>在插件中扩展 Eva.js 的 type 能力<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F154" target="_blank"><span>#154</span></a></li> 
 <li><span>优化交互事件，可获取当前点击localPosition<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F158" target="_blank"><span>#158</span></a></li> 
 <li><span>优化帧动画能力，可停止在最后一帧<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F159" target="_blank"><span>#159</span></a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>生态</span></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span>支持淘宝/支付宝小程序<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F156" target="_blank"><span>#156</span></a></li> 
 <li><span>IIFE文件支持微信小游戏使用<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F153" target="_blank"><span>#153</span></a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>修复</span></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span>spine 动画 autoplay 为 false，调用play无法播放问题<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F164" target="_blank"><span>#164</span></a></li> 
 <li><span>资源加载进度暂停问题<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F165" target="_blank"><span>#165</span></a></li> 
 <li><span>A11y组件DOM层zIndex可配置<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F147" target="_blank"><span>#147</span></a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>生态周边</span></h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>RaxEva 开源</span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Frax-eva" target="_blank"><span>RaxEva</span></a><span>是一个让开发同学能够在</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frax.js.org%2F" target="_blank"><span>Rax</span></a><span>技术体系下，利用Eva.js的游戏研发能力，开发动画、游戏类场景的框架。它可以让开发同学用熟悉的JSX和（仅支持）Hooks语法编写动画、游戏场景的代码。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>未来，社区将在 RaxEva API 基础上实现 ReatEva，让更广大的前端开发者能够快速上手Eva.js。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="845" src="https://oscimg.oschina.net/oscnet/up-e47e677c6967499092e1abec3392071e931.png" width="1078" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>Live2D</span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffa940; color:#ffffff">非官方插件<span> </span></span><span>Live2D 可以让你的 2D 表现的更立体，在二次元游戏、动漫领域非常流行，现在非常多的虚拟主播也使用了 Live2D 的技术。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffanmingfei%2Feva-plugin-renderer-live2d" target="_blank"><span>GitHub仓库</span></a><span><span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffanmingfei.github.io%2Feva-plugin-renderer-live2d%2F" target="_blank"><span>在线demo</span></a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="608" src="https://oscimg.oschina.net/oscnet/up-192e64f3d8d9f67b61c594735232407f547.gif" width="544" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>虚拟摇杆</span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffa940; color:#ffffff">非官方插件<span> </span></span><span>在游戏中经常会用到摇杆的效果。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffanmingfei%2Feva-plugin-joystick" target="_blank"><span>GitHub仓库</span></a><span><span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffanmingfei.github.io%2Feva-plugin-joystick%2F" target="_blank"><span>在线Demo</span></a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="632" src="https://oscimg.oschina.net/oscnet/up-f4639af57b4c37b1e38b2b9a69cf45deb60.gif" width="868" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>Spine 降级</span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffa940; color:#ffffff">未开源<span> </span></span><span>Eva.js & EVA Store 提供了一个Spine渲染降级方案，可选取Spine动画中的一帧作为在低端机上展示的图片，结合CDN的方式，可以实现动态加载Spine插件。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="1094" src="https://oscimg.oschina.net/oscnet/up-a44651eacd6e2bbc51dbcb4f3bb6dc3be2a.png" width="800" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>计划</span></h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>引擎</span></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span>v1.3 版本将会支持<span> </span></span><strong><span>粒子动画<span> </span></span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F109" target="_blank"><span>#109</span></a><strong><span>。</span></strong></li> 
 <li><span>提升Eva.js打包编译速度</span></li> 
</ul> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span>可视化编辑器设计中</span></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>社区</span></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Freact-eva" target="_blank">react-eva</a><span> </span>实现基于JSX和Hooks语法编写动画、游戏场景的代码。</span></li> 
 <li><span>开放Spine降级能力源码</span></li> 
</ul> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span>逐步开源资源工具链</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Feva%2Fos-group" target="_blank"><span>Eva.js 开源小组建设</span></a><span>（欢迎大家加入）</span></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>扩展阅读</span></h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://eva-engine.gitee.io/" target="_blank"><span>Eva.js 官网</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js" target="_blank"><span>Eva.js GitHub</span></a><span>（欢迎Star支持）</span></li> 
</ul> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Fawesome" target="_blank"><span>Eva.js Awesome</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Ffuckgiser%2Fp%2F5497013.html" target="_blank"><span>为什么需要纹理压缩</span></a></li> 
</ul> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTimvanScherpenzeel%2Ftexture-compressor%2Fblob%2Fmaster%2Fdocs%2FSUPPORTED_DEVICES_TABLE.md" target="_blank"><span>压缩纹理兼容性</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.live2d.com%2F" target="_blank"><span>Live2D官网</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FLive2D" target="_blank"><span>Live2D - 维基百科</span></a></li> 
</ul> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F28130936" target="_blank"><span>如何看待Live2D这项技术</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Feva%2Fblog%2Fbeeosi" target="_blank"><span>支撑双11五亿玩家的互动游戏引擎Eva.js开源啦！</span></a></li> 
</ul>
                                        </div>
                                      
</div>
            