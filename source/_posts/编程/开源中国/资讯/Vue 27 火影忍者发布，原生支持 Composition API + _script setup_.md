
---
title: 'Vue 2.7 火影忍者发布，原生支持 Composition API + _script setup_'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c4ecc5ad44efd2defcc2a5a8ca1edb317ff.png'
author: 开源中国
comments: false
date: Fri, 01 Jul 2022 07:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c4ecc5ad44efd2defcc2a5a8ca1edb317ff.png'
---

<div>   
<div class="content">
                                                                                            <p>Vue 创始人尤雨溪刚刚发布了 Vue 2.x 最后一个版本：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.vuejs.org%2Fposts%2Fvue-2-7-naruto.html" target="_blank">Vue 2.7</a>，代号 "<span style="background-color:#ffffff; color:#0f1419">Naruto</span>"（火影忍者）。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-c4ecc5ad44efd2defcc2a5a8ca1edb317ff.png" referrerpolicy="no-referrer"></p> 
<p>按照发布计划，Vue 2.7 是 2.x 的最后一个次要版本，也是 LTS 版本，获得官方提供的 <strong>18 个月技术支持</strong>。这就意味着，<strong>Vue 2 将在 2023 年底结束生命周期</strong>。</p> 
<p>Vue 2.7 从 Vue 3 向后移植了一些最重要的功能，包括：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvuejs.org%2Fguide%2Fextras%2Fcomposition-api-faq.html" target="_blank">Composition API</a></li> 
 <li>SFC<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvuejs.org%2Fapi%2Fsfc-script-setup.html" target="_blank"><code><script setup></code></a></li> 
 <li>SFC<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvuejs.org%2Fapi%2Fsfc-css-features.html%23v-bind-in-css" target="_blank">CSS v-bind</a></li> 
</ul> 
<p>此外，以下功能已明确不会进行移植：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>createApp()</code><span> </span>(Vue 2 doesn't have isolated app scope)</li> 
 <li>Top-level<span> </span><code>await</code><span> </span>in<span> </span><code><script setup></code><span> </span>(Vue 2 does not support async component initialization)</li> 
 <li>TypeScript syntax in template expressions (incompatible w/ Vue 2 parser)</li> 
 <li>Reactivity transform (still experimental)</li> 
 <li><code>expose</code><span> </span>option is not supported for options components (but<span> </span><code>defineExpose()</code><span> </span>is supported in<span> </span><code><script setup></code>).</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.vuejs.org%2Fposts%2Fvue-2-7-naruto.html" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            