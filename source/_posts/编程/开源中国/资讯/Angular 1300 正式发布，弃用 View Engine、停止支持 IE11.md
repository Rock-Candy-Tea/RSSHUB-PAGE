
---
title: 'Angular 13.0.0 正式发布，弃用 View Engine、停止支持 IE11'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1106/081104_94EZ_5430600.png'
author: 开源中国
comments: false
date: Sat, 06 Nov 2021 00:14:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1106/081104_94EZ_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Angular 13.0.0 正式发布，此版本弃用了 View Engine ，改用 Ivy 引擎、同时停止支持 IE 11 和 4.4.2 之前的 TypeScript 版本。</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">弃用<span> </span><strong>View Engine </strong></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Angular 近几个版本一直在支持 Ivy 引擎 ，Angular 13 版本直接移除了 View Engine<strong> 。</strong>移除 View Engine 意味着可以减少对<code>ngcc</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv13.angular.io%2Fguide%2Fglossary%23ngcc" target="_blank">Angular 兼容性编译器</a>）的依赖，不包含元数据和摘要文件，可以更快地编译，大大提高生产力。</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">Angular CLI 改进</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">现在默认使用持久构建缓存，可以让构建速度加快68%。已有的项目要启用此功能可以将此配置添加到<code>angular.json</code>：</p> 
<table cellspacing="0" class="highlight js-file-line-container tab-size" style="-webkit-text-stroke-width:0px; background:var(--color-canvas-default); border-collapse:collapse; border:0px; color:#333333; font-family:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace; font-size:12px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:1.4; margin:0px; orphans:2; padding:0px; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <td style="background-color:rgba(0, 0, 0, 0); border-width:0px; text-align:left; vertical-align:top; white-space:pre">&#123;</td> 
  </tr> 
  <tr> 
   <td style="background-color:rgba(0, 0, 0, 0); text-align:right; vertical-align:top; white-space:nowrap; width:13.2031px"> </td> 
   <td style="background-color:rgba(0, 0, 0, 0); border-width:0px; text-align:left; vertical-align:top; white-space:pre"><span style="color:#22863a">"$schema"</span>: <span style="color:#032f62"><span style="color:#032f62">"</span>...<span style="color:#032f62">"</span></span>,</td> 
  </tr> 
  <tr> 
   <td style="background-color:rgba(0, 0, 0, 0); text-align:right; vertical-align:top; white-space:nowrap; width:13.2031px"> </td> 
   <td style="background-color:rgba(0, 0, 0, 0); border-width:0px; text-align:left; vertical-align:top; white-space:pre"><span style="color:#22863a">"cli"</span>: &#123;</td> 
  </tr> 
  <tr> 
   <td style="background-color:rgba(0, 0, 0, 0); text-align:right; vertical-align:top; white-space:nowrap; width:13.2031px"> </td> 
   <td style="background-color:rgba(0, 0, 0, 0); border-width:0px; text-align:left; vertical-align:top; white-space:pre"><span style="color:#22863a">"cache"</span>: &#123;</td> 
  </tr> 
  <tr> 
   <td style="background-color:rgba(0, 0, 0, 0); text-align:right; vertical-align:top; white-space:nowrap; width:13.2031px"> </td> 
   <td style="background-color:rgba(0, 0, 0, 0); border-width:0px; text-align:left; vertical-align:top; white-space:pre"><span style="color:#22863a">"enabled"</span>: <span style="color:#005cc5">true</span>,</td> 
  </tr> 
  <tr> 
   <td style="background-color:rgba(0, 0, 0, 0); text-align:right; vertical-align:top; white-space:nowrap; width:13.2031px"> </td> 
   <td style="background-color:rgba(0, 0, 0, 0); border-width:0px; text-align:left; vertical-align:top; white-space:pre"><span style="color:#22863a">"path"</span>: <span style="color:#032f62"><span style="color:#032f62">"</span>.cache<span style="color:#032f62">"</span></span>,</td> 
  </tr> 
  <tr> 
   <td style="background-color:rgba(0, 0, 0, 0); text-align:right; vertical-align:top; white-space:nowrap; width:13.2031px"> </td> 
   <td style="background-color:rgba(0, 0, 0, 0); border-width:0px; text-align:left; vertical-align:top; white-space:pre"><span style="color:#22863a">"environment"</span>: <span style="color:#032f62"><span style="color:#032f62">"</span>all<span style="color:#032f62">"</span></span></td> 
  </tr> 
  <tr> 
   <td style="background-color:rgba(0, 0, 0, 0); text-align:right; vertical-align:top; white-space:nowrap; width:13.2031px"> </td> 
   <td style="background-color:rgba(0, 0, 0, 0); border-width:0px; text-align:left; vertical-align:top; white-space:pre">&#125;</td> 
  </tr> 
  <tr> 
   <td style="background-color:rgba(0, 0, 0, 0); text-align:right; vertical-align:top; white-space:nowrap; width:13.2031px"> </td> 
   <td style="background-color:rgba(0, 0, 0, 0); border-width:0px; text-align:left; vertical-align:top; white-space:pre">&#125;</td> 
  </tr> 
  <tr> 
   <td style="background-color:rgba(0, 0, 0, 0); text-align:right; vertical-align:top; white-space:nowrap; width:13.2031px"> </td> 
   <td style="background-color:rgba(0, 0, 0, 0); border-width:0px; text-align:left; vertical-align:top; white-space:pre"><span style="background-color:#b31d28; color:#fafbfc">...</span></td> 
  </tr> 
  <tr> 
   <td style="background-color:rgba(0, 0, 0, 0); text-align:right; vertical-align:top; white-space:nowrap; width:13.2031px"> </td> 
   <td style="background-color:rgba(0, 0, 0, 0); border-width:0px; text-align:left; vertical-align:top; white-space:pre">&#125;</td> 
  </tr> 
 </tbody> 
</table> 
<p> </p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">组件 API 优化</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Ivy 还改善了开发人员动态创建组件的方式，之前动态创建组件需要大量样板代码。新 API 无需<code>ComponentFactoryResolver</code><span> </span>注入构造函数。Ivy 支持在<span> </span><code>ViewContainerRef.createComponent</code><span> </span>不创建关联工厂的情况下实例化组件。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">旧版本创建组件代码：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img height="273" src="https://static.oschina.net/uploads/space/2021/1106/081104_94EZ_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p>新 API，这段代码可以这样写</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img height="168" src="https://static.oschina.net/uploads/space/2021/1106/081117_gCJo_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">停止支持 IE 11</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>不支持 IE11 意味着 Angular 可以通过原生 Web API 利用现代浏览器功能，例如 CSS 变量和 Web 动画。</li> 
 <li>删除 IE 特定的 polyfills 和代码路径，代码减少了，程序加载也快了。</li> 
 <li>项目迁移期间，运行程序会自动删 IE 特定的 polyfill ，让包变得更简洁。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Angular 12 版本会一直维护到 2022 年 11 月 ，还想支持 IE 的人可以继续用 Angular 12。（ IE 真是前端永远的痛，支持不一定有用，但放弃一定很轻松。）</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">框架和依赖项更新</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"> Angular 13 必须用 RxJS 7.4，用 RxJS v6.x 的应用需要手动更新，用这个命令：<code>npm install rxjs@7.4</code>。</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">字体支持</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Angular 11 支持内联谷歌字体，13 版本扩展了对 Adobe 字体的支持，更新完就可以直接用。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"> </p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">除此之外， Angular 13 还有其他更新项，如 Angular 包格式 (APF) 的更改、Angular 测试的改进等，详情可以查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Freleases" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            