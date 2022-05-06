
---
title: 'KPlayer v0.5.4 版本发布，更适合的云服务器直播推流工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://camo.githubusercontent.com/8dd765adaa4394f5def6b211b689cb208e6c12e3965058c57d855bf52079237b/68747470733a2f2f73332e626d702e6f76682f696d67732f323032322f30342f32392f316365373434613534393162623361342e706e67'
author: 开源中国
comments: false
date: Fri, 06 May 2022 10:01:00 GMT
thumbnail: 'https://camo.githubusercontent.com/8dd765adaa4394f5def6b211b689cb208e6c12e3965058c57d855bf52079237b/68747470733a2f2f73332e626d702e6f76682f696d67732f323032322f30342f32392f316365373434613534393162623361342e706e67'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0px; margin-right:0px; text-align:center"><img alt="cgapp logo" src="https://camo.githubusercontent.com/8dd765adaa4394f5def6b211b689cb208e6c12e3965058c57d855bf52079237b/68747470733a2f2f73332e626d702e6f76682f696d67732f323032322f30342f32392f316365373434613534393162623361342e706e67" referrerpolicy="no-referrer"></h1> 
<p style="color:#24292f; text-align:center"><strong>KPlayer帮助你不依赖图形界面快速的在服务器上进行视频资源的直播推流</strong></p> 
<hr> 
<h3 style="text-align:start">💬<span> </span>kplayer是什么</h3> 
<p style="color:#24292f; text-align:start">kplayer为你提供最小化成本搭建视频推流功能的工具，最优的推流方案OBS或其他软件依赖与xWindow或图形化界面的需要，不适合在服务端与云服务器上进行部署。KPlayer无需依赖图形化界面，您可以使用任意一款你喜欢的发行版本即可实现多视频资源无缝推流的方案。</p> 
<p style="color:#24292f; text-align:start">只需要定义您的配置文件，针对定制化的修改。即可达成想要的结果。并且可以24小时无人值守的方式运行它。</p> 
<p style="color:#24292f; text-align:start">使用文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkplayer.net%2Fp%2F1" target="_blank">https://kplayer.net/p/1</a></p> 
<h3 style="text-align:start">🚀<span> v0.5.4更新内容</span></h3> 
<ul> 
 <li>添加配置文件中指定<code>play_mode</code>中的列表随机<code>random</code>与队列<code>queue</code>模式 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkplayer.net%2Fd%2F37" target="_blank">#37</a></li> 
 <li>添加自适应分辨率参数选项<code>fill_strategy</code>用来配置设置分辨率与源视频分辨率不一致时的缩放策略。支持<code>tile</code>按比例拉伸、<code>ratio</code>自适应比例进行黑色背景填充</li> 
 <li>升级插件版本至v1.5.0。提供插件中允许嵌套子插件的功能、提供插件初始化完成回调函数、允许自定义可修改参数白名单 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkplayer.net%2Fd%2F38" target="_blank">#38</a></li> 
 <li>添加输出与插件资源前置加载问题，解决插件异步加载造成的加载延迟的问题。添加插件按照当前配置文件顺序加载 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkplayer.net%2Fd%2F35" target="_blank">#35</a></li> 
 <li>添加插件管理器模块，以适应不用版本插件版本的差异化加载</li> 
 <li>修复生成缓存再某些条件下效率异常的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkplayer.net%2Fd%2F42" target="_blank">#42</a></li> 
 <li>修复在使用缓存输出时，输出资源列表断开或为空时内存泄漏问题</li> 
 <li>修复在使用缓存进行推流播放时再某些C版本标准库时造成的内存泄漏，长时间内存占用过大触发<code>Killed</code>的错误</li> 
 <li>优化输入资源UniqueName的生成策略，使得同名同路径资源文件unique始终不变</li> 
 <li>优化音视频同步策略，解决采用<code>flv.js</code>（例如bilibili网页版）等库的兼容性。提高推流流畅性</li> 
</ul> 
<h3>下载地址</h3> 
<p>arm64: <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdownload.bytelang.cn%2Fkplayer-v0.5.4-linux_arm64.tar.gz" target="_blank">http://download.bytelang.cn/kplayer-v0.5.4-linux_arm64.tar.gz</a></p> 
<p>amd64: <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdownload.bytelang.cn%2Fkplayer-v0.5.4-linux_amd64.tar.gz" target="_blank">http://download.bytelang.cn/kplayer-v0.5.4-linux_amd64.tar.gz</a></p> 
<h3>docker镜像</h3> 
<pre><code class="language-shell">docker pull bytelang/kplayer:latest

docker pull bytelang/kplayer:v0.5.4
</code></pre> 
<h3>github</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbytelang%2Fkplayer-go%2Ftree%2Fv0.5.4" target="_blank">https://github.com/bytelang/kplayer-go/tree/v0.5.4</a></p>
                                        </div>
                                      
</div>
            