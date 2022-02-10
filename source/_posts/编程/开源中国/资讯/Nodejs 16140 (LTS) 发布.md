
---
title: 'Node.js 16.14.0 (LTS) 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3312'
author: 开源中国
comments: false
date: Thu, 10 Feb 2022 07:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3312'
---

<div>   
<div class="content">
                                                                                            <p>Node.js 16.14.0 (LTS) 已发布。</p> 
<p>值得关注的变化：</p> 
<ul> 
 <li>导入 JSON 模块现在要求使用实验性的 import assertions 语法</li> 
</ul> 
<p>此版本增加了对 import assertions（处于 stage 3 阶段的提案）的实验性支持。</p> 
<p><span style="background-color:#ffffff; color:#333333">为了使 Node.js ESM 实现尽可能与 HTML 规范兼容，现在需要使用 </span>import assertions 语法<span style="background-color:#ffffff; color:#333333">来导入 JSON 模块：</span></p> 
<pre><code>import info from `./package.json` assert &#123; type: `json` &#125;;</code></pre> 
<p>或使用动态导入：</p> 
<pre><code>const info = await import(`./package.json`, &#123; assert: &#123; type: `json` &#125; &#125;);</code></pre> 
<p>其他值得关注的变化包括：</p> 
<ul> 
 <li><strong>async_hooks</strong>: 
  <ul> 
   <li><strong>(SEMVER-MINOR)</strong><span> expose </span>async_wrap providers<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F40760" target="_blank">#40760</a></li> 
  </ul> </li> 
 <li><strong>child_process</strong>: 
  <ul> 
   <li><strong>(SEMVER-MINOR)</strong><span> </span>为<code>cp.fork</code><span>添加对 URL 的支持 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F41225" target="_blank">#41225</a></li> 
  </ul> </li> 
 <li><strong>v8</strong>: 
  <ul> 
   <li><strong>(SEMVER-MINOR)</strong><span> </span>多租户 promise hook api (Stephen Belanger)<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fpull%2F39283" target="_blank">#39283</a></li> 
  </ul> </li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnodejs.org%2Fen%2Fblog%2Frelease%2Fv16.14.0%2F" target="_blank">更多内容查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            