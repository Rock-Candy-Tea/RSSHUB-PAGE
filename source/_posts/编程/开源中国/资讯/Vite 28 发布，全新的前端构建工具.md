
---
title: 'Vite 2.8 发布，全新的前端构建工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0219/110504_HzXh_2720166.jpg'
author: 开源中国
comments: false
date: Mon, 14 Feb 2022 07:10:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0219/110504_HzXh_2720166.jpg'
---

<div>   
<div class="content">
                                                                                            <p>Vite 2.8 已发布。</p> 
<p>主要更新内容：</p> 
<ul> 
 <li>升级底层：esbuild 0.14 & TypeScript 4.5</li> 
 <li>Workers 使用新的 URL() 模式</li> 
 <li>减少内存占用空间：2.8 的发布包大小约为 2.7 的 1/4，安装包大小减少了约一半</li> 
</ul> 
<p><strong>减少内存占用空间</strong></p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#24292f; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; max-width:100%; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:max-content; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>Version</th> 
   <th>Publish Size</th> 
   <th>Install Size</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackagephobia.com%2Fresult%3Fp%3Dvite%25402.7.0" target="_blank">2.7.0</a></td> 
   <td style="border-style:solid; border-width:1px">12.7MB</td> 
   <td style="border-style:solid; border-width:1px">25.2MB</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackagephobia.com%2Fresult%3Fp%3Dvite%25402.8.0" target="_blank">2.8.0</a></td> 
   <td style="border-style:solid; border-width:1px">4.6MB</td> 
   <td style="border-style:solid; border-width:1px">17.4MB</td> 
  </tr> 
 </tbody> 
</table> 
<p><strong>默认预览端口</strong></p> 
<p><code>vite preview</code>的新默认端口是 4173（避免与 MacOS 使用的 5000 端口冲突）</p> 
<p><strong>Workers 使用了标准语法</strong></p> 
<p>当使用<code>new URL('path', import.meta.url)</code><span style="background-color:#ffffff; color:#24292f">语法时，可检测和捆绑到 </span>Workers，取代了使用<code>?worker</code>后缀的需求，并确保 Vite 与标准模式一致。</p> 
<p>旧写法：</p> 
<pre><code class="language-javascript">import MyWorker from './worker.js?worker'
const worker = new MyWorker()</code></pre> 
<p>新写法</p> 
<pre><code class="language-javascript">const worker = new Worker(
  new URL('./worker.js', import.meta.url), &#123; type: 'module' &#125;
)</code></pre> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2Fmain%2Fpackages%2Fvite%2FCHANGELOG.md%23280-2022-02-09" target="_blank">详细内容查看 Changelog</a>。</p> 
<hr> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Vite（法语意思是 “快”，发音为 /vit/，类似 veet）是一种全新的前端构建工具。你可以把它理解为一个开箱即用的开发服务器 + 打包工具的组合，但是更轻更快。Vite 利用浏览器原生的 ES 模块支持和用编译到原生的语言开发的工具（如 esbuild）来提供一个快速且现代的开发体验。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://static.oschina.net/uploads/space/2021/0219/110504_HzXh_2720166.jpg" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Vite 有多快？在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepl.it%2F" target="_blank">Repl.it</a> 上从零启动一个基于 Vite 的 React 应用，浏览器页面加载完毕的时候，CRA（create-react-app）甚至还没有装完依赖。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如果你还没听说过 Vite 到底是什么，可以到<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcn.vitejs.dev%2Fguide%2Fwhy.html" target="_blank">这里</a>了解一下项目的设计初衷。如果你想要了解 Vite 跟其它一些类似的工具有什么区别，可以参考这里的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcn.vitejs.dev%2Fguide%2Fcomparisons.html" target="_blank">对比</a>。</p>
                                        </div>
                                      
</div>
            