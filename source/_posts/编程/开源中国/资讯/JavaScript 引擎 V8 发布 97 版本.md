
---
title: 'JavaScript 引擎 V8 发布 9.7 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2197'
author: 开源中国
comments: false
date: Thu, 18 Nov 2021 07:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2197'
---

<div>   
<div class="content">
                                                                                            <p>JavaScript 引擎 V8 上周发布了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv8.dev%2Fblog%2Fv8-release-97" target="_blank">最新版本 9.7</a>，目前处于测试阶段。正式版本将在几周后随 Chrome 97 稳定版一起推出。9.7 版本带来了一些面向开发人员的特性，主要亮点包括：</p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>JavaScript</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><code>findLast</code>和<code>findLastIndex</code>数组方法</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="text-align:start"><code>Array</code><span style="background-color:#ffffff; color:#000000">和</span><code>TypedArray</code>上<span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>的<code>findLast</code>和<code>findLastIndex</code>方法</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>可以从数组的末端找到符合预定条件的元素。</p> 
<p style="text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>例如：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<pre><code>[1,2,3,4].findLast((el) => el % 2 === 0)
// → 4 (last even element)</code></pre> 
<p style="text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>从 v9.7 开始，这些方法无需 flag 即可使用。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>更多详细信息查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv8.dev%2Ffeatures%2Ffinding-in-arrays%23finding-elements-from-the-end" target="_blank">功能说明</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>V8 API</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>使用<code>git log branch-heads/9.6..branch-heads/9.7 include/v8\*.h</code>命令获取 API 更改列表。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>具有活动 V8 checkout 权限的开发者可通过<code>git checkout -b 9.7 -t branch-heads/9.7</code>来试验 V8 v9.7 中的新功能。或者可以<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.google.com%2Fchrome%2Fbrowser%2Fbeta.html" target="_blank">订阅 Chrome Beta 频道</a>亲自试用新功能。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p>
                                        </div>
                                      
</div>
            