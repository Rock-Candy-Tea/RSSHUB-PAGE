
---
title: 'Taro 3.4 beta 发布：支持 Preact 为应用开辟更多体积空间'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://cors.zfour.workers.dev/?http://storage.360buyimg.com/taro-jd-com/static/contact_taro_harmony_qr.png'
author: 开源中国
comments: false
date: Thu, 25 Nov 2021 18:53:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://storage.360buyimg.com/taro-jd-com/static/contact_taro_harmony_qr.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#666666; margin-left:0; margin-right:0">项目体积是困扰小程序开发者的一大问题，如果开发者使用 Taro React 进行开发，更是不得不引入接近 100K 的 React 相关依赖，这让项目体积变得更加捉襟见肘。因此，Taro v3.4 的主要方向，是探索对于 Preact 的支持。</p> 
<blockquote> 
 <p style="color:#999999; margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpreactjs.com%2F" target="_blank">Preact</a> 是一款体积超小的类 React 框架，提供和 React 几乎一致的 API，而体积只有 5k 左右。</p> 
</blockquote> 
<h2><span>支持使用 Preact</span></h2> 
<p style="color:#666666; margin-left:0; margin-right:0">Taro v3.4 正式实现了对 Preact 的支持，下文将简单介绍适配思路及用法。</p> 
<h3><span>适配思路</span></h3> 
<h4 style="margin-left:auto; margin-right:auto"><span>1. 运行时改造</span></h4> 
<p style="color:#666666; margin-left:0; margin-right:0">Taro 在小程序环境模拟实现了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fdocs%2Fnext%2Fimplement-note%23%25E8%25BF%2590%25E8%25A1%258C%25E6%2597%25B6" target="_blank">类浏览器环境</a>，因此理论上任意的前端框架都可以在 Taro 中使用。</p> 
<p style="color:#666666; margin-left:0; margin-right:0">对于 Preact，它与 React 最大的不同在于没有实现<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freactjs.org%2Fdocs%2Fevents.html" target="_blank">合成事件系统</a>，而是直接使用浏览器的事件方法，此外还使用了少量和 React 不一样的 DOM API。</p> 
<p style="color:#666666; margin-left:0; margin-right:0">对于事件的适配，Taro 已经提供了浏览器规范的事件方法，因此只需要再处理 Preact 的事件名与小程序事件名的差异。而对于 DOM 方法，则需要额外实现 Preact 使用到的 DOM API。</p> 
<h4 style="margin-left:auto; margin-right:auto"><span>2. 兼容 React 生态</span></h4> 
<p style="color:#666666; margin-left:0; margin-right:0">Preact 使用了 <code>preact/compat</code> 去磨平与 React 的 API 差异，让 React 的各种生态库可以直接运行在 Preact 上。得益于此，开发时我们可以使用任意的 React 生态库，甚至对 React、ReactDOM 的 API 引用也不需要修改，只需要简单地配置 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpreactjs.com%2Fguide%2Fv10%2Fswitching-to-preact%23setting-up-compat" target="_blank">alias</a> 即可：</p> 
<pre><code><em>// Webpack config</em>
<span style="color:#c678dd">const</span> config = &#123;
  <span style="color:#98c379">"resolve"</span>: &#123;
    <span style="color:#98c379">"alias"</span>: &#123;
      <span style="color:#98c379">"react"</span>: <span style="color:#98c379">"preact/compat"</span>,
      <span style="color:#98c379">"react-dom/test-utils"</span>: <span style="color:#98c379">"preact/test-utils"</span>,
      <span style="color:#98c379">"react-dom"</span>: <span style="color:#98c379">"preact/compat"</span>,
      <span style="color:#98c379">"react/jsx-runtime"</span>: <span style="color:#98c379">"preact/jsx-runtime"</span>
    &#125;,
  &#125;
&#125;
</code></pre> 
<h3><span>用法介绍</span></h3> 
<blockquote> 
 <p style="color:#999999; margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fdocs%2Fnext%2Fpreact" target="_blank">文档地址</a></p> 
</blockquote> 
<h4 style="margin-left:auto; margin-right:auto"><span>新项目</span></h4> 
<p style="color:#666666; margin-left:0; margin-right:0">运行 <code>taro init</code> 时，框架选择 <strong style="color:hsl(216, 80%, 44%)">Preact</strong> 即可创建基于 Preact 的项目。</p> 
<h4 style="margin-left:auto; margin-right:auto"><span>现有的 React 项目</span></h4> 
<ol style="list-style-type:decimal"> 
 <li> <p style="color:#666666; margin-left:0; margin-right:0">将 CLI、项目中 Taro 相关的依赖更新到 <code>v3.4.0-beta</code> 版本。</p> </li> 
 <li> <p style="color:#666666; margin-left:0; margin-right:0">安装依赖：</p> </li> 
</ol> 
<pre><code>yarn add preact @tarojs/plugin-framework-react
</code></pre> 
<ol start="3" style="list-style-type:decimal"> 
 <li> <p>修改 Taro 编译配置：</p> </li> 
</ol> 
<pre><code><span style="color:#c678dd">const</span> config = &#123;
  <em>// ...</em>
  <span style="color:#d19a66">framework</span>: <span style="color:#98c379">'preact'</span>
&#125;
</code></pre> 
<ol start="4" style="list-style-type:decimal"> 
 <li> <p>修改 Babel 配置：</p> </li> 
</ol> 
<pre><code><span style="color:#e6c07b">module</span>.exports = &#123;
  <span style="color:#d19a66">presets</span>: [
    [<span style="color:#98c379">'taro'</span>, &#123;
      <span style="color:#d19a66">framework</span>: <span style="color:#98c379">'preact'</span>
    &#125;]
  ]
&#125;
</code></pre> 
<ol start="5" style="list-style-type:decimal"> 
 <li> <p>如果项目使用了 TypeScript，请打开 <code>skipLibCheck</code> 配置，以避免和其它 React 生态库配合使用时报类型错误：</p> </li> 
</ol> 
<pre><code>&#123;
  ...
  <span style="color:#98c379">"skipLibCheck"</span>: <span style="color:#56b6c2">true</span>,
&#125;
</code></pre> 
<h2><span>Vue 3 支持 Composition API 版本的小程序生命周期钩子</span></h2> 
<blockquote> 
 <p style="color:#999999; margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fdocs%2Fnext%2Fcomposition-api" target="_blank">文档地址</a></p> 
</blockquote> 
<p style="color:#666666; margin-left:0; margin-right:0">Vue3 提供了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv3.vuejs.org%2Fguide%2Fcomposition-api-introduction.html%23why-composition-api" target="_blank">Composition API（组合式 API）</a> 特性，和传统的 Options API 不同，Composition API 提供了全新的编码方式 ，可以让我们更好地去组织和复用代码逻辑。</p> 
<p style="color:#666666; margin-left:0; margin-right:0">过去 Taro 只提供了 Options API 版本的小程序生命周期钩子，开发者往往对于这些钩子和 <code>setup</code> 函数内部该如何通讯、如何共享数据等问题感到困惑，更是不能很好地兼容 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv3.vuejs.org%2Fapi%2Fsfc-script-setup.html%23basic-syntax" target="_blank">script setup</a> 语法。</p> 
<p style="color:#666666; margin-left:0; margin-right:0">因此 Taro v3.4 提供了 Composition API 版本的小程序生命周期钩子，让开发者更方便地使用 <code>setup</code> 语法，例子：</p> 
<pre><code><span><<span style="color:#e06c75">script</span> <span style="color:#d19a66">setup</span>></span>
<span><span style="color:#c678dd">import</span> &#123; useDidShow &#125; <span style="color:#c678dd">from</span> <span style="color:#98c379">'@tarojs/taro'</span>

useDidShow(<span><span>()</span> =></span> <span style="color:#e6c07b">console</span>.log(<span style="color:#98c379">'onShow'</span>))
</span><span></<span style="color:#e06c75">script</span>></span>
</code></pre> 
<h2><span>运行时体积优化</span></h2> 
<p style="color:#666666; margin-left:0; margin-right:0">目前 Taro 对于前端框架的适配层代码都放在了运行时库 <code>@tarojs/runtime</code> 里，意思即当开发者使用 React 时，还是会包含 Vue2、Vue3 的适配层代码。（Tree Shaking 失败的原因是使用了 Webpack Provider Plugin 导出 <code>@tarojs/runtime</code> 里的 BOM API）</p> 
<p style="color:#666666; margin-left:0; margin-right:0">因此，Taro v3.4 以 Taro 插件的形式去实现对于各前端框架的适配，其中一个好处是可以把上述运行时适配层的代码拆分到各个插件内。加上对运行时代码的写法优化，3.4 版本的运行时减少了约 <strong style="color:hsl(216, 80%, 44%)">30k</strong> 的空间。</p> 
<p style="color:#666666; margin-left:0; margin-right:0">另一个好处是现在开发者可以通过编写 Taro 插件去支持任意的前端框架，而几乎不需要改动 Taro 的核心代码。</p> 
<h2><span>升级指南</span></h2> 
<h4 style="margin-left:auto; margin-right:auto"><span>1. 安装 <code>v3.4.0-beta</code> 的 CLI 工具：</span></h4> 
<pre><code>npm i -g @tarojs/cli@beta
</code></pre> 
<h4 style="margin-left:auto; margin-right:auto"><span>2. 更新项目依赖</span></h4> 
<blockquote> 
 <p style="color:#999999; margin-left:0; margin-right:0">如果安装失败或打开项目失败，可以删除 <strong style="color:hsl(216, 80%, 44%)">node_modules</strong>、<strong style="color:hsl(216, 80%, 44%)">yarn.lock</strong>、<strong style="color:hsl(216, 80%, 44%)">package-lock.json</strong> 后重新安装依赖再尝试。</p> 
</blockquote> 
<p style="color:#666666; margin-left:0; margin-right:0">修改 <code>package.json</code> 文件中 Taro 相关依赖的版本修改为 <code>~3.4.0-beta.0</code>，再重新安装依赖。</p> 
<h4 style="margin-left:auto; margin-right:auto"><span>3.【Breaking Changes】安装对应的框架适配插件</span></h4> 
<p style="color:#666666; margin-left:0; margin-right:0">因为 Taro v3.4 把各前端框架的适配逻辑拆分到对应的插件中，因此旧项目升级时需要安装对应框架的适配插件：</p> 
<ul style="list-style-type:disc"> 
 <li> <p>使用 React，请安装 <code>@tarojs/plugin-framework-react</code></p> </li> 
 <li> <p>使用 Vue2，请安装 <code>@tarojs/plugin-framework-vue2</code></p> </li> 
 <li> <p>使用 Vue3，请安装 <code>@tarojs/plugin-framework-vue3</code></p> </li> 
</ul> 
<h2><span>其他</span></h2> 
<h3><span>Breaking Changes</span></h3> 
<ul style="list-style-type:disc"> 
 <li> <p>百度小程序使用 <code>onInit</code> 代替 <code>onLoad</code> 生命周期，以优化首次启动时间。</p> </li> 
</ul> 
<h2><span>最后</span></h2> 
<p style="color:#666666; margin-left:0; margin-right:0">接下来 Taro 的重心将会放在编译系统升级（如升级 Webpack5）和优化 H5 能力（如输出 SSR 方案、优化路由系统等）上。</p> 
<h3><span>鸿蒙应用 && OpenHarmony</span></h3> 
<p style="color:#666666; margin-left:0; margin-right:0">Taro 迭代的另一条主线是对<strong style="color:hsl(216, 80%, 44%)">鸿蒙应用 && OpenHarmony</strong> 的适配，目前第一阶段的开发工作即将完成，12 月初会发布首个可用的体验版本。</p> 
<p style="color:#666666; margin-left:0; margin-right:0">相关咨询：</p> 
<ul style="list-style-type:disc"> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fdiscussions%2Fcategories%2F%25E9%25B8%25BF%25E8%2592%2599-openharmony-%25E9%2580%2582%25E9%2585%258D%25E5%25B0%258F%25E7%25BB%2584" target="_blank">鸿蒙 && OpenHarmony 适配小组</a></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fprojects%2F2" target="_blank">适配进度</a></p> </li> 
</ul> 
<p style="color:#666666; margin-left:0; margin-right:0">鸿蒙 & OpenHarmony 交流群：</p> 
<p><img alt src="https://cors.zfour.workers.dev/?http://storage.360buyimg.com/taro-jd-com/static/contact_taro_harmony_qr.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            