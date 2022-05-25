
---
title: 'Electron 19.0 发布，回归支持最新的三个主要版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5186'
author: 开源中国
comments: false
date: Wed, 25 May 2022 11:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5186'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Electron 团队于今天正式发布了 Electron 19.0，你可以使用 <code>npm install electron@latest</code> 用 npm 安装它，或者从官方网站下载它。它包括对 Chromium 102、V8 10.2 和 Node.js 16.14.2 的升级。</p> 
<h3>Electron 发布周期的改变</h3> 
<p>Electron 项目将恢复其早期的政策，即支持最新的三个主要版本。在这之前官方曾短暂修改政策为支持最新的四个主要版本，以帮助用户适应从 Electron 15 开始的新的发布节奏。</p> 
<h3>技术栈变化</h3> 
<ul> 
 <li>Chromium 102</li> 
 <li>Node.js 16.14.2</li> 
 <li>V8 10.2</li> 
</ul> 
<h3>API & 重要变化</h3> 
<ul> 
 <li> <p>在 Linux 上不支持： <code>.skipTaskbar</code></p> <p>BrowserWindow 构造器的选项 <code>skipTaskbar</code> 在 Linux 上不再被支持。</p> </li> 
 <li> <p>移除了 WebPreferences.preloadURL</p> <p><code>preloadURL</code> 属性已从 WebPreferences 中移除。应该使用 <code>WebPreferences.preload</code> 来代替。</p> </li> 
</ul> 
<h3>结束对 15.x.y 和 16.x.y 的支持</h3> 
<p>Electron 15.x.y 和 16.x.y 都已经达到了支持的终点。这使 Electron 回到了它现有的支持最新三个主要版本的政策，并鼓励开发者和应用程序升级到更新的 Electron 版本。</p> 
<table> 
 <thead> 
  <tr> 
   <th>E15 (Sep'21)</th> 
   <th>E16 (Nov'21)</th> 
   <th>E17 (Feb'22)</th> 
   <th>E18 (Mar'22)</th> 
   <th>E19 (May'22)</th> 
  </tr> 
  <tr> 
   <td>15.x.y</td> 
   <td>16.x.y</td> 
   <td>17.x.y</td> 
   <td>18.x.y</td> 
   <td>19.x.y</td> 
  </tr> 
  <tr> 
   <td>14.x.y</td> 
   <td>15.x.y</td> 
   <td>16.x.y</td> 
   <td>17.x.y</td> 
   <td>18.x.y</td> 
  </tr> 
  <tr> 
   <td>13.x.y</td> 
   <td>14.x.y</td> 
   <td>15.x.y</td> 
   <td>16.x.y</td> 
   <td>17.x.y</td> 
  </tr> 
  <tr> 
   <td>12.x.y</td> 
   <td>13.x.y</td> 
   <td>14.x.y</td> 
   <td>15.x.y</td> 
   <td>--</td> 
  </tr> 
 </thead> 
</table> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Freleases%2Ftag%2Fv19.0.0" target="_blank">https://github.com/electron/electron/releases/tag/v19.0.0</a></p>
                                        </div>
                                      
</div>
            