
---
title: 'layui-vue 0.3.8 发布，基于 vue 3.0 的桌面端组件库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c2adca8f63743d6a7d51af8c5b99950bb85.png'
author: 开源中国
comments: false
date: Tue, 22 Feb 2022 09:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c2adca8f63743d6a7d51af8c5b99950bb85.png'
---

<div>   
<div class="content">
                                                                                            <p>更新内容：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[新增] fullscreen 全屏组件。</li> 
 <li>[新增] icon-picker 颜色选择器。</li> 
 <li>[新增] config-provider 全局配置, 用于主题与国际化切换。</li> 
 <li>[修复] container 容器在不同的分辨率无法自适应的问题</li> 
 <li>[修复] dropdown 组件无法嵌套使用的问题。</li> 
 <li>[修复] menu 组件导航模式菜单错位问题。</li> 
 <li>[修复] quote 引用的 nm 灰色主题失效。</li> 
 <li>[升级] icons-vue 1.0.7 版本。</li> 
 <li>[升级] layer-vue 1.3.5 版本。</li> 
</ul> 
<p>颜色选择器的发布，意味着 layui-vue 对主题的支持。全局 config-provider 配置将为开发者提供更友好的在线主题切换解决方案。</p> 
<p>接下来，我们来看如何为现有项目，增加主题切换支持。</p> 
<pre style="margin-left:0; margin-right:0; text-align:justify"><code><span><span style="color:#dd1144"><template></span></span></code><code><span>  <span style="color:#dd1144"><lay-config-provider :themeVariable="themeVariable"></span></span></code><code><span>    <span style="color:#dd1144"><router-view></span><span style="color:#dd1144"></router-view></span></span></code><code><span>  <span style="color:#dd1144"></lay-config-provider></span></span></code><code><span><span style="color:#dd1144"></template></span></span></code><code><span><span style="color:#dd1144"><script setup></span></span></code><code><span><span style="color:#0e9ce5">import</span> &#123; ref &#125; from <span style="color:#dd1144">"vue"</span>;</span></code><code><span><span style="color:#0e9ce5">const</span> themeVariable = ref(&#123;</span></code><code><span>   "--<span style="color:#0e9ce5">global</span>-primary-color<span style="color:#dd1144">": "</span>#009688<span style="color:#dd1144">",</span></span></code><code><span><span>   "</span>--global-checked-color<span style="color:#dd1144">": "</span>#5fb878<span style="color:#dd1144">"</span></span></code><code><span>&#125;)</span></code><code><span></script></span></code></pre> 
<p>在你看到 ref 关键字时，说明 themeVariable 是具有响应的变量。这意味着对 themeVariable 值的修改，将成为你切换主题的关键。</p> 
<p><img height="522" src="https://oscimg.oschina.net/oscnet/up-c2adca8f63743d6a7d51af8c5b99950bb85.png" width="1080" referrerpolicy="no-referrer"></p> 
<p>以下为当前版本可用的主题配置变量，后续我们将开放更细粒度的主题变量</p> 
<pre style="margin-left:0; margin-right:0; text-align:justify"><code><span><span style="color:#dd1144">"--global-primary-color"</span>: <span style="color:#dd1144">"#009688"</span>, <em>// 主题色</em></span></code><code><span><span style="color:#dd1144">"--global-normal-color"</span>: <span style="color:#dd1144">"#1e9fff"</span>, <em>// 通用色</em></span></code><code><span><span style="color:#dd1144">"--global-warm-color"</span>: <span style="color:#dd1144">"#ffb800"</span>, <em>// 警告色</em></span></code><code><span><span style="color:#dd1144">"--global-danger-color"</span>: <span style="color:#dd1144">"#ff5722"</span>, <em>// 危险色</em></span></code><code><span><span style="color:#dd1144">"--global-checked-color"</span>: <span style="color:#dd1144">"#5fb878"</span>, <em>// 选中色</em></span></code><code><span><span style="color:#dd1144">"--global-border-radius"</span>: <span style="color:#dd1144">"10px"</span> <em>// 圆角</em></span></code>
</pre> 
<p>在新版本发布的同时，我们开放 物料 板块，用于收录用户投递组件或集成模板，让每一个轮子产生价值 </p> 
<p><img height="885" src="https://oscimg.oschina.net/oscnet/up-7872868728e50aca1cf5643ee2b850f9684.png" width="1914" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            