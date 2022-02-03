
---
title: 'Electron 17.0.0 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9158bd86bb5f27c113eb8cbf629b57666c6.png'
author: 开源中国
comments: false
date: Wed, 02 Feb 2022 07:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9158bd86bb5f27c113eb8cbf629b57666c6.png'
---

<div>   
<div class="content">
                                                                                            <p>Electron 17.0.0<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.electronjs.org%2Fblog%2Felectron-17-0" target="_blank">已正式发布</a>。更新内容包括将 Chromium 升级至 98、将 Node.js 升级至 v16.13.0，以及将 V8 引擎升级至 v9.8 等。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>发布节奏变化</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#1c1e21"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>从 Electron 15 开始，Electron 将每 8 周发布一个新的主要稳定版本，点此查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.electronjs.org%2Fblog%2F8-week-cadence" target="_blank">完整的详细信息</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#1c1e21"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>此外，Electron 已将支持的版本从最新的三个版本更改为最新的四个版本，直到 2022 年 5 月。关于 Electron 版本控制的更多详细信息，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.electronjs.org%2Fdocs%2Flatest%2Ftutorial%2Felectron-versioning" target="_blank">可查阅版本控制文档</a>。2022 年 5 月之后，官方表示将恢复回支持最新的三个版本。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>技术栈变化</strong></p> 
<ul> 
 <li>Chromium<span> </span><code>98</code> 
  <ul style="margin-left:0; margin-right:0"> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.chrome.com%2Fblog%2Fnew-in-chrome-98%2F" target="_blank">New in Chrome 98</a></li> 
  </ul> </li> 
 <li>Node.js<span> </span><code>16.13.0</code> 
  <ul style="margin-left:0; margin-right:0"> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnodejs.org%2Fen%2Fblog%2Frelease%2Fv16.13.0%2F" target="_blank">Node 16.13.0 blog post</a></li> 
  </ul> </li> 
 <li>V8<span> </span><code>9.8</code></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Highlighted Feature</strong></p> 
<ul> 
 <li>已添加<code>webContents.getMediaSourceId()</code>，可用于<code>getUserMedia</code>一起使用，以获取 WebContents 的 stream。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F31204" target="_blank">#31204</a></li> 
 <li>弃用<code>webContents.getPrinters()</code>并引入<code>webContents.getPrintersAsync()</code>. <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F31023" target="_blank">#31023</a></li> 
 <li><code>desktopCapturer.getSources</code>现在仅在主进程中可用。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F30720" target="_blank">#30720</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">有关新功能和更改的完整列表，可参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Freleases%2Ftag%2Fv17.0.0" target="_blank">17.0.0 发行说明</a>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">停止支持 13.x.y</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.electronjs.org%2Fdocs%2Flatest%2Ftutorial%2Fsupport%23supported-versions" target="_blank">根据 Electron 的支持政策</a>，<span style="color:#1c1e21">Electron 13.x.y<span> 已不再被支持。</span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="232" src="https://oscimg.oschina.net/oscnet/up-9158bd86bb5f27c113eb8cbf629b57666c6.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>下一步计划</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">官方表示，<span style="color:#1c1e21">在短期内，期望团队继续专注于跟上 Electron 主要组件的开发节奏，包括 Chromium、Node 和 V8。</span></p>
                                        </div>
                                      
</div>
            