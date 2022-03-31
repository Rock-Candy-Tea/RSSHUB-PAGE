
---
title: 'Electron 18.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9926'
author: 开源中国
comments: false
date: Thu, 31 Mar 2022 07:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9926'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Electron 18.0.0</span><span style="background-color:#ffffff; color:#333333"> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.electronjs.org%2Fblog%2Felectron-18-0" target="_blank">已正式发布</a><span style="background-color:#ffffff; color:#333333">，包括对 Chromium 100、V8 10.0 和 Node.js 16.13.2 的升级。具体更新内容如下：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>发布节奏变化</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#1c1e21"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>从 Electron 15 开始，Electron 将每 8 周发布一个新的主要稳定版本，点此查看</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.electronjs.org%2Fblog%2F8-week-cadence" target="_blank">完整的详细信息</a>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#1c1e21"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>此外，Electron 已将支持的版本从最新的三个版本更改为最新的四个版本，直到 2022 年 5 月。关于 Electron 版本控制的更多详细信息，</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.electronjs.org%2Fdocs%2Flatest%2Ftutorial%2Felectron-versioning" target="_blank">可参阅版本控制文档</a><span><span><span style="color:#1c1e21"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>。2022 年 5 月之后，官方表示将恢复回支持最新的三个版本。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>技术栈变化</strong></p> 
<ul> 
 <li>Chromium<span> </span><code>100</code> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.chrome.com%2Fblog%2Fnew-in-chrome-100%2F" target="_blank">New in Chrome 100</a></li> 
  </ul> </li> 
 <li>Node.js<span> </span><code>16.13.2</code> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnodejs.org%2Fen%2Fblog%2Frelease%2Fv16.13.2%2F" target="_blank">Node 16.13.2 blog post</a></li> 
  </ul> </li> 
 <li>V8<span> </span><code>10.0</code></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Highlighted Feature</strong></p> 
<ul> 
 <li>添加了<code>ses.setCodeCachePath()</code>API 用于设置代码缓存目录。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F33286" target="_blank">#33286</a></li> 
 <li>删除了基于<code>BrowserWindowProxy</code>的<code>window.open</code>的旧实现，这也删除了<code>webPreferences</code>中的<code>nativeWindowOpen</code>选项。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29405" target="_blank">#29405</a></li> 
 <li>将“focus”和“blur'”事件添加到<code>WebContents</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F25873" target="_blank">#25873</a></li> 
 <li>在 macOS 上添加了 Substitutions 菜单角色：<code>showSubstitutions</code>, <code>toggleSmartQuotes</code>, <code>toggleSmartDashes</code>, <code>toggleTextReplacement</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32024" target="_blank">#32024</a></li> 
 <li>在<code>app.requestSingleInstanceLock()</code>flow 中添加了<code>first-instance-ack</code>事件，这样用户就可以从第二实例向第一实例传递一些数据。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F31460" target="_blank">#31460</a></li> 
 <li>在<code>setBackgroundColor</code>中增加了对更多颜色格式的支持。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F33364" target="_blank">#33364</a></li> 
</ul> 
<p style="text-align:start"><span><span><span style="color:#1c1e21"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>有关新功能和更改的完整列表，可参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Freleases%2Ftag%2Fv18.0.0" target="_blank">18.0.0 发行说明</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><strong>Breaking & API Changes</strong></p> 
<p style="text-align:start">Removed:<span> </span><code>nativeWindowOpen</code></p> 
<p style="text-align:start"><span><span><span style="color:#1c1e21"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>在 Electron 15 之前，<code>window.open</code></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>被默认为使用<span><span><span style="color:#1c1e21"><span><span><span><span><span><span><span><span><span><span><span><span><span><span><code>BrowserWindowProxy</code>. 这意味着<code>window.open('about:blank')</code>无法打开同步编写脚本的子窗口，以及其他不兼容问题。从 Electron 15开始，<code>nativeWindowOpen</code></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>已经被默认启用<span><span><span style="color:#1c1e21"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span><span style="color:#1c1e21"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>有关更多详细信息，可参阅 Electron 中<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.electronjs.org%2Fdocs%2Flatest%2Fapi%2Fwindow-open%23windowopenurl-framename-features" target="_blank">的 window.open 文档。</a>在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29405" target="_blank">#29405 中删除</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>停止支持 14.x.y</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.electronjs.org%2Fdocs%2Flatest%2Ftutorial%2Felectron-timelines%23version-support-policy" target="_blank">根据项目的支持政策</a>，<span style="color:#1c1e21">Electron 14.x.y<span> 已不再被支持。</span></span></p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; border-collapse:collapse; box-sizing:border-box; color:#1c1e21; display:block; font-family:system-ui,-apple-system,"Segoe UI",Roboto,Ubuntu,Cantarell,"Noto Sans",sans-serif,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:var(--ifm-spacing-vertical); orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <th style="background-color:var(--ifm-table-head-background)">E15 (Sep'21)</th> 
   <th style="background-color:var(--ifm-table-head-background)">E16 (Nov'21)</th> 
   <th style="background-color:var(--ifm-table-head-background)">E17 (Feb'22)</th> 
   <th style="background-color:var(--ifm-table-head-background)">E18 (Mar'22)</th> 
   <th style="background-color:var(--ifm-table-head-background)">E19 (May'22)</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td style="border-style:solid">15.x.y</td> 
   <td style="border-style:solid">16.x.y</td> 
   <td style="border-style:solid">17.x.y</td> 
   <td style="border-style:solid">18.x.y</td> 
   <td style="border-style:solid">19.x.y</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid">14.x.y</td> 
   <td style="border-style:solid">15.x.y</td> 
   <td style="border-style:solid">16.x.y</td> 
   <td style="border-style:solid">17.x.y</td> 
   <td style="border-style:solid">18.x.y</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid">13.x.y</td> 
   <td style="border-style:solid">14.x.y</td> 
   <td style="border-style:solid">15.x.y</td> 
   <td style="border-style:solid">16.x.y</td> 
   <td style="border-style:solid">17.x.y</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid">12.x.y</td> 
   <td style="border-style:solid">13.x.y</td> 
   <td style="border-style:solid">14.x.y</td> 
   <td style="border-style:solid">15.x.y</td> 
   <td style="border-style:solid">--</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>下一步计划</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#1c1e21">在短期内，团队将继续专注于跟上构成 Electron 的主要组件的开发，包括 Chromium、Node 和 V8。</span></p>
                                        </div>
                                      
</div>
            