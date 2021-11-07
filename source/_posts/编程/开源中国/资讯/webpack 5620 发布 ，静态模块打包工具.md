
---
title: 'webpack 5.62.0 发布 ，静态模块打包工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8199'
author: 开源中国
comments: false
date: Sat, 06 Nov 2021 23:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8199'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">Webpack v </span><span style="color:#000000">5.62.0</span><span style="color:#333333"> 发布了！Webpack 是一个常见的静态模块打包工具，主要用途是在浏览器上打包 JavaScript 文件。</span></p> 
<h3><span style="color:#333333">新特性</span></h3> 
<ul> 
 <li><span style="color:#333333">加入 </span><span style="color:#24292f">parser.javascript.reexportExportsPresence: false ，用于 TypeScript 类型再导出。</span><span style="color:#2e3033">允许在 </span><code>export ... from "..."</code><span style="color:#24292f"> 到 </span><code>export type ... from "..."</code><span style="color:#2e3033"> 迁移期间对不存在的导出禁用警告。</span></li> 
 <li>添加<code>experiments.backCompat: false</code>，用于禁用一些高性能消耗的功能，以获得更好的性能。</li> 
</ul> 
<h2 style="margin-left:0px"><strong>Bug 修复</strong></h2> 
<ul> 
 <li><span style="color:#24292f">用 </span><code>['catch']</code><span style="color:#24292f"> 代替 </span><code>.catch</code>，更好地支持 <span style="color:#24292f">ES3 。</span></li> 
 <li><span style="color:#24292f">修复</span>使用 <code>new (require("...")).Something()</code> 时会删除括号的问题。</li> 
 <li><span style="color:#2e3033">修复 &#123;require&#125; 对象字面量</span> 。</li> 
 <li><span style="color:#2e3033"><code>splitChunks.chunks</code> 选项现在正确地用于 <code>splitChunks.fallbackCacheGroup.maxSize</code> 。</span></li> 
 <li><span style="color:#2e3033">修复 </span><code>listen</code><span style="color:#24292f"> </span><span style="color:#2e3033">选项的模式，允许省略 </span><span style="color:#24292f"><code>port</code></span>。</li> 
 <li>对不同隔离区的 <span style="color:#24292f">Promises 有更好的支持。</span></li> 
</ul> 
<h3><span style="color:#24292f">开发者体验优化</span></h3> 
<p><span style="color:#2e3033"><strong>为模块中可用的 webpack API 添加 </strong></span><span style="color:#24292f"><strong>typings</strong></span></p> 
<ul> 
 <li><span style="color:#24292f">用 <code>/// <reference types="webpack/module" /></code> ，可以使用 typescript 模块的 typings </span></li> 
 <li><span style="color:#24292f">或者在 tsconfig 里用  <code>"types": [..., "webpack/module"]</code></span></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwebpack%2Fwebpack%2Freleases%2Ftag%2Fv5.62.0" target="_blank">https://github.com/webpack/webpack/releases/tag/v5.62.0</a></p>
                                        </div>
                                      
</div>
            