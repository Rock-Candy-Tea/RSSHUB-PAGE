
---
title: 'Electron介绍(一)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93b42ca307684d0486c86e7f8ef81f19~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Apr 2021 22:36:35 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93b42ca307684d0486c86e7f8ef81f19~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. Electron 发展现状</h1>
<p><img alt="v2-8f61f5a890e57260ef9ff5c4952cc111_r.jpg" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93b42ca307684d0486c86e7f8ef81f19~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
2020年5月SpaceX发射的Dragon 2载人航天飞船，使用了<strong>Chromium和JavaScript</strong>来构建用户界面。消息一出，立即引起了技术界的热烈关注，一个Web框架被使用到对效率和可靠性要求极高的航天应用场景，一方面反映了SpaceX在技术领域的敢于突破传统的实干精神，同时也把两个跨领域的技术：桌面客户端和Web技术栈的完美结合案例带入了大众的视野。
<strong>Electron</strong>作为一个优秀的PC端应用开发框架 ，主要应用在开发Windows/MAC的桌面应用。本人在2017年公司开始做一个PC端的游戏控制终端，类似于我们现在看到的自助唱K终端、麦当劳自助点餐和地铁站自助购票等终端，一方面，需要像传统WEB项目一样快频繁迭代UI界面和请求网络资源，另一方面需要使用设备端的原生资源，比如外部进程，串口/USB设备等。在这种需求的前提下，我们没有进行太多的甄选而选择了NW.js(和Electron 组成架构几乎一样), 而2019年新开了一个PC端的项目，我们又选择了electron来开发。其实NWJS和Electron的区别不大，这里主要介绍Electron相关的知识。</p>
<h1 data-id="heading-1">2 PC客户端的横向比较</h1>
<p>时间倒回到2015年以前，如果大家选择桌面端的开发框架，会在MFC，Qt和C#等框架中选择。这三者都有比较完善的功能类库，比如<strong>消息机制、组件钩子</strong>等，技术栈相对贴近操作系统底层，开发者需要了解Windows API 和 Linux系统的一些知识，入门的门槛也相对较高。比如Websocket这些在HTTP协议中非常成熟的应用协议，在这些框架中需要额外调用动态库或者插件来实现，架构的设计、代码的层次远比Web技术栈更加复杂。
当然这里不是完全的摒弃这三个UI框架的价值，在一些计算密集型场景，比如音视频播放、图像处理，或者说工业控制领域，如果现成已经有技术积累是在这几个框架的基础之上，那么继续采用MFC/QT/C#框架会是更好的选择。
在小团队或者应用场景相对简单的背景下，采用Electron会是一个好的选择。</p>
<h1 data-id="heading-2">3 Electron的框架介绍</h1>
<p><img alt="electron-parts.PNG" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fe2c5ec52304f109bf6bde63b3c8554~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
这个公式阐明了Electron的功能组成:</p>
<ol>
<li><strong>Chromium</strong>： 作为google推出的浏览器内核，大规模应用在了Chrome浏览器、360浏览器、QQ浏览器、微信内嵌网页等应用场景。</li>
<li><strong>NodeJS</strong>:  把JavaScript技术栈延伸到了服务器和操作系统(文件操作、异步读写、进程/线程管理等)领域，让前端技术的可应用场景进一步丰富和下沉。</li>
<li><strong>Native API</strong>: 对Window、Linux和IOS的跨平台做了兼容处理，把窗口操作、弹窗消息、操作系统信息等API封装了一遍, 使得Web界面和Native功能完美结合到一起。</li>
</ol>
<h1 data-id="heading-3">4. Electron的应用场景</h1>
<p>A. <strong>文件管理</strong>
比如开源的<strong>PicGo</strong>，一个图片管理软禁，github Star数已经12K+，就是集成了本地图片管理、云端上传等功能，类似于一个本地/远程同步的电子相册。
技术栈是Vue+Electron
阿里云OSS 的PC客户端也是基于Electron，前端框架是angular。</p>
<p>B. <strong>前端IDE</strong>
微软推出的 visual code是基于Electron，Electron的强大之处在于集成了很多前端的插件，比如代码规范、找回历史代码、代码比对、注释信息格式、甚至取变量名也有插件。
而且媲美notepad++的启动速度，以及永远免费的使用权限，受到了大批开发者，尤其是前端开发者的青睐。</p>
<p>C.  <strong>触屏客户端</strong>
国内第一家VR游戏自助终端-肉丸VR（现在改名为"弥天"VR）就是本人主导开发的，集成了游戏界面列表、玩家自助选择游戏、自助付费、体验游戏、商户运维等功能，最大的有特色就是界面的更新和迭代采用的是web前端技术，游戏进程的管理采用的是native模块，让客户端具有了前端界面开发的高效，以及native技术在操作系统层面的丰富资源。关于这其中的详细架构，在其它文章中国再详细阐述。
像国内现在随处可见的自助K歌、自助售货机等智能终端，它们的UI也有很多采用的是chromium + web + native的架构，与Electron的技术栈是异曲同工的。
后续的章节会继续介绍Electron的详细技术点，以及实际开发中会遇到的常见问题，请大家持续关注。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            