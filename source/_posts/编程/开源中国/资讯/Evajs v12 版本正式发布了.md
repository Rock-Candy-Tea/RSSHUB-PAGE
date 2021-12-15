
---
title: 'Eva.js v1.2 版本正式发布了'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1215/172953_kUQj_4937141.png'
author: 开源中国
comments: false
date: Wed, 15 Dec 2021 09:38:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1215/172953_kUQj_4937141.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt height="390" src="https://static.oschina.net/uploads/space/2021/1215/172953_kUQj_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><span>Eva.js<span> </span>v1.2<span> </span>版本正式发布，本版本是双11喵糖的使用版本。欢迎使用<span> </span></span>Eva.js v1.2<span> </span>GitHub! （https://github.com/eva-engine/eva.js）</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">本次版本主要支持了压缩纹理的渲染，首要解决GPU内存压力。支持实时修改游戏播放速度，增加更多表现力。新增 Spine4.0<span> </span>的支持，并且抽离了spine的公共文件，降低多个 Spine 版本功能同步的成本。提供扩展type的能力，插件开发可增加对引擎核心能力的扩展。为交互事件提供相对于当前对象的点击位置。优化帧动画能力，可停止在最后一帧。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">主要修复了一些常见问题，Spine 在特定参数下无法播放问题，资源加载进度问题以及A11y的DOM层级问题。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">在生态方面，支持淘宝/支付宝小程序中运行，IIFE支持微信小游戏中使用Eva.js。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">Eva.js v1.2 已在以下项目中使用：淘宝双11 / 芭芭农场 / 淘宝斗地主 / 薅羊毛赚话费，目前版本已经升级到1.2.2，我们一般在自己的业务中验证大版本稳定性，在进行正式发布。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">感谢各个兄弟团队和业界伙伴的信赖，正是大家的信赖，Eva.js 才能做到更加丰富的表现力、更加优质的性能、更加流畅的开发体验。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FQTNzZR6KeD8kzZzgAdYVFChaV7CoU9WhYdRwsSyuNNPKszibm54EPictgtYWaNVQzOsdUaH3MnJjnjVibxcTBgwMg%2F640%3Fwx_fmt%3Dpng" target="_blank"><img alt height="211" src="https://static.oschina.net/uploads/space/2021/1215/173051_TvC0_4937141.png" width="700" referrerpolicy="no-referrer"></a></p> 
<h2>重点特性介绍</h2> 
<h4>压缩纹理</h4> 
<p>常见的图片文件格式，比如 PNG/JPEG/Webp 等，是为了存储图像信息的特殊编码方式，只能存在硬盘中或内存中，无法被 GPU 直接识别。纹理压缩格式，是一种 GPU 能直接读取并显示的格式，使得图像无需解压即可进行渲染，节约大量的内存。点击进入压缩纹理文档 (<a href="https://eva-engine.gitee.io/docs/tutorials/compressedTexture/">https://eva-engine.gitee.io/docs/tutorials/compressedTexture/</a>)</p> 
<p>可以通过官方提供的 texture-compressor 工具生成压缩纹理文件。</p> 
<p>阿里巴巴内网用户结合 EVA Store 提供的资源管理能力，点击 预览代码 可以直接生成压缩纹理并且直接提供 Eva.js 支持的代码。</p> 
<p><img alt height="397" src="https://static.oschina.net/uploads/space/2021/1215/173112_yaHH_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h4>游戏播放速度控制</h4> 
<p>通过控制游戏播放速度，可以实现更丰富的游戏效果。</p> 
<p><img alt src="https://static.oschina.net/uploads/space/2021/1215/173130_B1rh_4937141.gif" width="700" referrerpolicy="no-referrer"></p> 
<h4>淘宝 / 支付宝小程序</h4> 
<p>Eva.js@^1.2.2</p> 
<p>Evs.js 现已支持淘宝 / 支付宝小程序中互动游戏的开发。</p> 
<p><img alt height="960" src="https://static.oschina.net/uploads/space/2021/1215/173236_NsJU_4937141.gif" width="448" referrerpolicy="no-referrer"></p> 
<h4>微信小游戏</h4> 
<p>通过微信 weapp-adapter 快速支持小程序，虽然需要使用 IIFE 的方式引入 Eva.js 文件，但能够顺利渲染成功，为未来生态扩展提供一个可行性方案。</p> 
<h2>升级内容概览</h2> 
<h4>能力</h4> 
<ul> 
 <li>压缩纹理支持 #84(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F84" target="_blank">https://github.com/eva-engine/eva.js/pull/84</a>)</li> 
 <li>游戏播放速度控制 #132(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F132" target="_blank">https://github.com/eva-engine/eva.js/pull/132</a>)</li> 
 <li>新增 Spine4.0 支持，同时支持 Spine 3.6/3.8/4.0，抽离 Spine 公共部分 #154(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F154" target="_blank">https://github.com/eva-engine/eva.js/pull/154</a>)</li> 
 <li>在插件中扩展 Eva.js 的 type 能力 #154(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F154" target="_blank">https://github.com/eva-engine/eva.js/pull/154</a>)</li> 
 <li>优化交互事件，可获取当前点击 localPosition #158(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F158" target="_blank">https://github.com/eva-engine/eva.js/pull/158</a>)</li> 
 <li>优化帧动画能力，可停止在最后一帧 #159(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F159" target="_blank">https://github.com/eva-engine/eva.js/pull/159</a>)</li> 
</ul> 
<h4>生态</h4> 
<ul> 
 <li>支持淘宝 / 支付宝小程序 #156(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F156" target="_blank">https://github.com/eva-engine/eva.js/pull/156</a>)</li> 
 <li>IIFE 文件支持微信小游戏使用 #153(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F153" target="_blank">https://github.com/eva-engine/eva.js/pull/153</a>)</li> 
</ul> 
<h4>修复</h4> 
<ul> 
 <li>spine 动画 autoplay 为 false，调用 play 无法播放问题 #164</li> 
 <li>资源加载进度暂停问题 #165</li> 
 <li>A11y 组件 DOM 层 zIndex 可配置 #147</li> 
</ul> 
<h2>生态周边</h2> 
<h4>RaxEva 开源</h4> 
<p>RaxEva 是一个让开发同学能够在 Rax 技术体系下，利用 Eva.js 的游戏研发能力，开发动画、游戏类场景的框架。它可以让开发同学用熟悉的 JSX 和（仅支持）Hooks 语法编写动画、游戏场景的代码。</p> 
<p>未来，社区将在 RaxEva API 基础上实现 ReatEva，让更广大的前端开发者能够快速上手 Eva.js。</p> 
<p><img alt height="548" src="https://static.oschina.net/uploads/space/2021/1215/173307_XXbZ_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h4>Live2D</h4> 
<p>非官方插件  Live2D 可以让你的 2D 表现的更立体，在二次元游戏、动漫领域非常流行，现在非常多的虚拟主播也使用了 Live2D 的技术。GitHub 仓库 在线 demo(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffanmingfei%2Feva-plugin-renderer-live2d" target="_blank">https://github.com/fanmingfei/eva-plugin-renderer-live2d</a>)</p> 
<p><img alt height="501" src="https://static.oschina.net/uploads/space/2021/1215/173330_cnt1_4937141.gif" width="448" referrerpolicy="no-referrer"></p> 
<h4>虚拟摇杆</h4> 
<p>非官方插件在游戏中经常会用到摇杆的效果。GitHub 仓库在线 Demo(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffanmingfei%2Feva-plugin-joystick" target="_blank">https://github.com/fanmingfei/eva-plugin-joystick</a>)</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FQTNzZR6KeD8kzZzgAdYVFChaV7CoU9Whk1ibyW3vqMCRyicvQKvEoObLlSRzElwaUHtnUBAoKyicnRe6efsia2jBoQ%2F640%3Fwx_fmt%3Dgif" target="_blank"><img alt height="510" src="https://static.oschina.net/uploads/space/2021/1215/173418_ZTT5_4937141.gif" width="700" referrerpolicy="no-referrer"></a></p> 
<h4>Spine 降级</h4> 
<p>未开源。Eva.js & EVA Store 提供了一个 Spine 渲染降级方案，可选取 Spine 动画中的一帧作为在低端机上展示的图片，结合 CDN 的方式，可以实现动态加载 Spine 插件。</p> 
<p><img alt height="957" src="https://static.oschina.net/uploads/space/2021/1215/173440_ZorZ_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>计划</h2> 
<h4>引擎</h4> 
<ul> 
 <li>v1.3 版本将会支持粒子动画 #109(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js%2Fpull%2F109" target="_blank">https://github.com/eva-engine/eva.js/pull/109</a>)。</li> 
 <li>提升 Eva.js 打包编译速度</li> 
 <li>可视化编辑器设计中</li> 
</ul> 
<h4>社区</h4> 
<ul> 
 <li>react-eva 实现基于 JSX 和 Hooks 语法编写动画、游戏场景的代码。</li> 
 <li>开放 Spine 降级能力源码</li> 
 <li>逐步开源资源工具链</li> 
 <li>Eva.js 开源小组建设 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Feva%2Fos-group" target="_blank">https://www.yuque.com/eva/os-group</a>)（欢迎大家加入）</li> 
</ul> 
<h4>扩展阅读</h4> 
<ul> 
 <li>Eva.js 官网 (<a href="https://eva-engine.gitee.io/">https://eva-engine.gitee.io/</a>)</li> 
 <li>Eva.js GitHub(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Feva.js" target="_blank">https://github.com/eva-engine/eva.js</a>)（欢迎 Star 支持）</li> 
 <li>Eva.js Awesome(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feva-engine%2Fawesome" target="_blank">https://github.com/eva-engine/awesome</a>)</li> 
 <li>为什么需要纹理压缩 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Ffuckgiser%2Fp%2F5497013.html" target="_blank">https://www.cnblogs.com/fuckgiser/p/5497013.html</a>)</li> 
 <li>压缩纹理兼容性 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTimvanScherpenzeel%2Ftexture-compressor%2Fblob%2Fmaster%2Fdocs%2FSUPPORTED%255C%255C_DEVICES%255C%255C_TABLE.md" target="_blank">https://github.com/TimvanScherpenzeel/texture-compressor/blob/master/docs/SUPPORTED\\_DEVICES\\_TABLE.md</a>)</li> 
 <li>Live2D 官网 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.live2d.com%2F" target="_blank">https://www.live2d.com/</a>)</li> 
 <li>Live2D - 维基百科 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FLive2D" target="_blank">https://zh.wikipedia.org/wiki/Live2D</a>)</li> 
 <li>如何看待 Live2D 这项技术 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F28130936" target="_blank">https://www.zhihu.com/question/28130936</a>)</li> 
 <li>支撑双 11 五亿玩家的互动游戏引擎 Eva.js 开源啦！(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Feva%2Fblog%2Fbeeosi" target="_blank">https://www.yuque.com/eva/blog/beeosi</a>) <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FqqqbosoFxDNzf0GO8kP2Aw" target="_blank">https://mp.weixin.qq.com/s/qqqbosoFxDNzf0GO8kP2Aw</a></li> 
</ul>
                                        </div>
                                      
</div>
            