
---
title: 'Taro 正式发布 3.4 版本：全面支持 Preact & Vue 3.2'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4017'
author: 开源中国
comments: false
date: Thu, 20 Jan 2022 22:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4017'
---

<div>   
<div class="content">
                                                                                            <p style="color:#1c1e21; text-align:start">距 Taro v3.4 beta 版本的发布已有一段时间，期间我们完善了对 Preact 和 Vue3 的支持，加入了一些有趣的特性，更是对 H5 作了大幅度的优化与调整，并于近期发布了 v3.4 的正式版本。</p> 
<blockquote> 
 <p>上月我们还推出了支持开发鸿蒙应用的 v3.5.0 canary 版本，欢迎各位同学关注~</p> 
</blockquote> 
<h2 style="text-align:start"><strong>一、支持使用 Preact</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%23%25E4%25B8%2580%25E6%2594%25AF%25E6%258C%2581%25E4%25BD%25BF%25E7%2594%25A8-preact" target="_blank">​</a></h2> 
<p style="color:#1c1e21; text-align:start">开发小程序应用时我们经常会受到包体积的掣肘，大型应用常常为了“尺土寸金”的包体积开展瘦身行动。在此背景下 React 将近 100k 的体积则显得有点过于奢侈。因此 Taro v3.4 实现了对 Preact 的支持，仅需少量配置即可从 React 切换到 Preact，有效地降低了包体积。</p> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpreactjs.com%2F" target="_blank">Preact</a><span> </span>是一款体积超小的类 React 框架，提供和 React 几乎一致的 API，兼容 React 生态，而体积只有 5k 左右。</p> 
</blockquote> 
<p style="color:#1c1e21; text-align:start">适配思路与具体用法请参阅<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2021-11-24-Taro-3.4-beta%23%25E6%2594%25AF%25E6%258C%2581%25E4%25BD%25BF%25E7%2594%25A8-preact" target="_blank">《Taro v3.4 发布 beta 版本 —— 支持使用 Preact 进行开发》</a></p> 
<h2 style="text-align:start"><strong>二、更好地支持 Vue 3.2</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%23%25E4%25BA%258C%25E6%259B%25B4%25E5%25A5%25BD%25E5%259C%25B0%25E6%2594%25AF%25E6%258C%2581-vue-32" target="_blank">​</a></h2> 
<h3 style="text-align:start"><strong>1. 支持 Composition API 版本的小程序生命周期钩子</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%231-%25E6%2594%25AF%25E6%258C%2581-composition-api-%25E7%2589%2588%25E6%259C%25AC%25E7%259A%2584%25E5%25B0%258F%25E7%25A8%258B%25E5%25BA%258F%25E7%2594%259F%25E5%2591%25BD%25E5%2591%25A8%25E6%259C%259F%25E9%2592%25A9%25E5%25AD%2590" target="_blank">​</a></h3> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fdocs%2Fnext%2Fcomposition-api" target="_blank">文档地址</a></p> 
</blockquote> 
<p style="color:#1c1e21; text-align:start">Vue 3.2 正式推出了<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv3.vuejs.org%2Fapi%2Fsfc-script-setup.html%23basic-syntax" target="_blank">script setup</a><span> </span>语法，过去 Taro 的 Options 式小程序生命周期钩子难以配合 script setup 语法进行使用。因此 Taro v3.4 提供了 Composition API 版本的小程序生命周期钩子，方便开发者配合 setup 语法组织和复用代码逻辑。</p> 
<p style="color:#1c1e21; text-align:start">例子：</p> 
<div style="text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#393a34"><</span><span style="color:#00009f">script</span><span style="color:#00009f"> </span><span style="color:#00a4db">setup</span><span style="color:#393a34">></span>
</span><span style="color:#393a34"><span style="color:#00009f">import</span><span> </span><span style="color:#393a34">&#123;</span><span> useDidShow </span><span style="color:#393a34">&#125;</span><span> </span><span style="color:#00009f">from</span><span> </span><span style="color:#e3116c">'@tarojs/taro'</span>
</span>
<span style="color:#393a34"><span style="color:#d73a49">useDidShow</span><span style="color:#393a34">(</span><span style="color:#393a34">(</span><span style="color:#393a34">)</span><span> </span><span style="color:#393a34">=></span><span> </span><span>console</span><span style="color:#393a34">.</span><span style="color:#d73a49">log</span><span style="color:#393a34">(</span><span style="color:#e3116c">'onShow'</span><span style="color:#393a34">)</span><span style="color:#393a34">)</span>
</span><span style="color:#393a34"><span style="color:#393a34"></</span><span style="color:#00009f">script</span><span style="color:#393a34">></span></span></code></pre> 
</div> 
<h3 style="text-align:start"><strong>2. 支持<span> </span><code><style> v-bind</code><span> </span>语法</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%232-%25E6%2594%25AF%25E6%258C%2581-style-v-bind-%25E8%25AF%25AD%25E6%25B3%2595" target="_blank">​</a></h3> 
<p style="color:#1c1e21; text-align:start">Vue 3.2 的<span> </span><code><style> v-bind</code><span> </span>语法让我们可以对样式进行数据绑定。它的实现使用了 DOM 的 MutationObserver API，但之前 Taro DOM 没有模拟实现此 API，因此使用<span> </span><code><style> v-bind</code><span> </span>时会报错。</p> 
<p style="color:#1c1e21; text-align:start">感谢<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fb2nil" target="_blank">@b2nil</a><span> </span>同学，参照<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fampproject%2Fworker-dom" target="_blank">worker-dom</a><span> </span>为 Taro DOM 实现了<span> </span><code>MutationObserver</code><span> </span>API，让我们可以使用<span> </span><code><style> v-bind</code><span> </span>语法。</p> 
<blockquote> 
 <p>Taro DOM 只针对 Vue3 暴露了<span> </span><code>MutationObserver</code><span> </span>API，使用 React 或 Vue2 的同学不需要担心会增大代码体积。</p> 
</blockquote> 
<h3 style="text-align:start"><strong>3. 暴露 VueLoader 的配置</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%233-%25E6%259A%25B4%25E9%259C%25B2-vueloader-%25E7%259A%2584%25E9%2585%258D%25E7%25BD%25AE" target="_blank">​</a></h3> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fdocs%2Fnext%2Fvue3%23compileroptions" target="_blank">文档地址</a></p> 
</blockquote> 
<p style="color:#1c1e21; text-align:start">开发者有时需要修改 VueLoader 的配置，例如使用小程序原生组件时需要配置<span> </span><code>compilerOptions.isCustomElement</code>。以往开发者只能通过<span> </span><code>WebpackChain</code><span> </span>去修改，Taro v3.4 暴露了 VueLoader 的配置，让开发者可以更方便地进行修改。</p> 
<h2 style="text-align:start"><strong>三、H5</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%23%25E4%25B8%2589h5" target="_blank">​</a></h2> 
<h3 style="text-align:start"><strong>1. 自定义多路由配置</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%231-%25E8%2587%25AA%25E5%25AE%259A%25E4%25B9%2589%25E5%25A4%259A%25E8%25B7%25AF%25E7%2594%25B1%25E9%2585%258D%25E7%25BD%25AE" target="_blank">​</a></h3> 
<p style="color:#1c1e21; text-align:start">Taro-H5 过去并不支持多路由访问同一个页面实例的操作，即便通过自定义路由配置也并不能在多个路由中访问同一个页面。</p> 
<p style="color:#1c1e21; text-align:start">因此 Taro-H5 提供了自定义多路由配置的参数，供开发者根据需求自行配置。</p> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fdocs%2Fnext%2Fconfig-detail%23h5routercustomroutes" target="_blank">文档地址</a></p> 
</blockquote> 
<div style="text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span>module</span><span style="color:#393a34">.</span><span>exports </span><span style="color:#393a34">=</span><span> </span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>  </span><em>// ...</em>
</span><span style="color:#393a34"><span>  h5</span><span style="color:#393a34">:</span><span> </span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>    </span><em>// ...</em>
</span><span style="color:#393a34"><span>    router</span><span style="color:#393a34">:</span><span> </span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>      customRoutes</span><span style="color:#393a34">:</span><span> </span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>        </span><em>// "页面路径": "自定义路由"</em>
</span><span style="color:#393a34"><span>        </span><span style="color:#e3116c">'/pages/index/index'</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">'/index'</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span>        </span><span style="color:#e3116c">'/pages/detail/index'</span><span style="color:#393a34">:</span><span> </span><span style="color:#393a34">[</span><span style="color:#e3116c">'/detail'</span><span style="color:#393a34">]</span><span> </span><em>// 可以通过数组为页面配置多个自定义路由</em>
</span><span style="color:#393a34"><span>      </span><span style="color:#393a34">&#125;</span>
</span><span style="color:#393a34"><span>    </span><span style="color:#393a34">&#125;</span>
</span><span style="color:#393a34"><span>  </span><span style="color:#393a34">&#125;</span>
</span><span style="color:#393a34"><span style="color:#393a34">&#125;</span></span></code></pre> 
</div> 
<h3 style="text-align:start"><strong>2. 路由动画 by<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FShaoGongBra" target="_blank">@ShaoGongBra</a></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%232-%25E8%25B7%25AF%25E7%2594%25B1%25E5%258A%25A8%25E7%2594%25BB-by-shaogongbra" target="_blank">​</a></h3> 
<p style="color:#1c1e21; text-align:start">Taro-H5 支持了路由动画，开发者可以通过配置<span> </span><code>app.config.js</code><span> </span>来控制页面的动画效果，也可以通过覆盖 CSS 样式来调整动画。当然一些场景下，比如页面需要使用<span> </span><code>position: fixed;</code><span> </span>会因为<span> </span><code>translate3d</code><span> </span>影响实际效果，可以将动画禁用。</p> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fdocs%2Fnext%2Fapp-config%23animation" target="_blank">文档地址</a></p> 
</blockquote> 
<div style="text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#00009f">export</span><span> </span><span style="color:#00009f">default</span><span> </span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>  </span><em>// ...</em>
</span><span style="color:#393a34"><span>  animation</span><span style="color:#393a34">:</span><span> </span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>    </span><em>// 动画切换时间，单位毫秒</em>
</span><span style="color:#393a34"><span>    duration</span><span style="color:#393a34">:</span><span> </span><span style="color:#36acaa">300</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span>    </span><em>// 动画切换时间，单位毫秒</em>
</span><span style="color:#393a34"><span>    delay</span><span style="color:#393a34">:</span><span> </span><span style="color:#36acaa">50</span>
</span><span style="color:#393a34"><span>  </span><span style="color:#393a34">&#125;</span>
</span><span style="color:#393a34"><span>  </span><em>// ...</em>
</span><span style="color:#393a34"><span style="color:#393a34">&#125;</span></span></code></pre> 
</div> 
<h3 style="text-align:start"><strong>3. dynamic-import-node</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%233-dynamic-import-node" target="_blank">​</a></h3> 
<p style="color:#1c1e21; text-align:start">Taro-H5 打包时会将页面和组件拆分成独立的文件按需加载，但这么做会导致没有用到的页面和组件依旧会被打包，导致编译体积变大，在一些特殊场景中（比如 PWA 等需要严格限制包体大小时）会因此受到不小的困扰。</p> 
<p style="color:#1c1e21; text-align:start">所以我们通过 babel 插件提供了移除懒加载的方法：</p> 
<div style="text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span>module</span><span style="color:#393a34">.</span><span>exports </span><span style="color:#393a34">=</span><span> </span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>  presets</span><span style="color:#393a34">:</span><span> </span><span style="color:#393a34">[</span>
</span><span style="color:#393a34"><span>    </span><span style="color:#393a34">[</span><span style="color:#e3116c">'taro'</span><span style="color:#393a34">,</span><span> </span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>      framework</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">'react'</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span>      hot</span><span style="color:#393a34">:</span><span> </span><span style="color:#36acaa">false</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span>      </span><span style="color:#e3116c">'dynamic-import-node'</span><span style="color:#393a34">:</span><span> </span><span style="color:#36acaa">true</span>
</span><span style="color:#393a34"><span>    </span><span style="color:#393a34">&#125;</span><span style="color:#393a34">]</span>
</span><span style="color:#393a34"><span>  </span><span style="color:#393a34">]</span>
</span><span style="color:#393a34"><span style="color:#393a34">&#125;</span></span></code></pre> 
</div> 
<h2 style="text-align:start"><strong>四、新增 defineAppConfig 与 definePageConfig 编译宏</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%23%25E5%259B%259B%25E6%2596%25B0%25E5%25A2%259E-defineappconfig-%25E4%25B8%258E-definepageconfig-%25E7%25BC%2596%25E8%25AF%2591%25E5%25AE%258F" target="_blank">​</a></h2> 
<blockquote> 
 <p>再次感谢<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fb2nil" target="_blank">@b2nil</a><span> </span>同学为 Taro 新增了此特性。 文档地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fdocs%2Fnext%2Fapp-config%23defineappconfig-%25E5%25AE%258F%25E5%2587%25BD%25E6%2595%25B0" target="_blank">defineAppConfig</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fdocs%2Fnext%2Fpage-config%23definepageconfig-%25E5%25AE%258F%25E5%2587%25BD%25E6%2595%25B0" target="_blank">definePageConfig</a></p> 
</blockquote> 
<h3 style="text-align:start"><strong>defineAppConfig</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%23defineappconfig" target="_blank">​</a></h3> 
<p style="color:#1c1e21; text-align:start">开发者可以使用<span> </span><code>defineAppConfig</code><span> </span>包裹 App 配置对象，以获得全局配置的<strong>类型提示</strong>和<strong>自动补全</strong>，如：</p> 
<div style="text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><em>// app.config.ts</em>
</span><span style="color:#393a34"><span style="color:#00009f">export</span><span> </span><span style="color:#00009f">default</span><span> </span><span style="color:#d73a49">defineAppConfig</span><span style="color:#393a34">(</span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>  pages</span><span style="color:#393a34">:</span><span> </span><span style="color:#393a34">[</span><span style="color:#e3116c">'pages/index/index'</span><span style="color:#393a34">]</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span>  </span><span style="color:#36acaa">window</span><span style="color:#393a34">:</span><span> </span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>    navigationBarTitleText</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">'WeChat'</span>
</span><span style="color:#393a34"><span>  </span><span style="color:#393a34">&#125;</span>
</span><span style="color:#393a34"><span style="color:#393a34">&#125;</span><span style="color:#393a34">)</span></span></code></pre> 
</div> 
<h3 style="text-align:start"><strong>definePageConfig</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%23definepageconfig" target="_blank">​</a></h3> 
<p style="color:#1c1e21; text-align:start">使用<span> </span><code>definePageConfig</code><span> </span>包裹 Page 配置对象，同样可以获得页面配置的<strong>类型提示</strong>和<strong>自动补全</strong>，如：</p> 
<div style="text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><em>// page.config.ts</em>
</span><span style="color:#393a34"><span style="color:#00009f">export</span><span> </span><span style="color:#00009f">default</span><span> </span><span style="color:#d73a49">definePageConfig</span><span style="color:#393a34">(</span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>  navigationBarTitleText</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">'首页'</span>
</span><span style="color:#393a34"><span style="color:#393a34">&#125;</span><span style="color:#393a34">)</span></span></code></pre> 
</div> 
<p style="color:#1c1e21; text-align:start">除此之外，<strong>开发者可以不提供页面的配置文件，直接在页面逻辑文件中使用<span> </span><code>definePageConfig</code><span> </span>定义页面配置</strong>。</p> 
<p style="color:#1c1e21; text-align:start">如在 React 中：</p> 
<div style="text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><em>// page.tsx</em>
</span><span style="color:#393a34"><span style="color:#d73a49">definePageConfig</span><span style="color:#393a34">(</span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>  navigationBarTitleText</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">'首页'</span>
</span><span style="color:#393a34"><span style="color:#393a34">&#125;</span><span style="color:#393a34">)</span>
</span>
<span style="color:#393a34"><span style="color:#00009f">export</span><span> </span><span style="color:#00009f">default</span><span> </span><span style="color:#00009f">function</span><span> </span><span style="color:#d73a49">Index</span><span> </span><span style="color:#393a34">(</span><span style="color:#393a34">)</span><span> </span><span style="color:#393a34">&#123;</span><span style="color:#393a34">&#125;</span></span></code></pre> 
</div> 
<p style="color:#1c1e21; text-align:start">在 Vue 中：</p> 
<div style="text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#393a34"><</span><span style="color:#00009f">script</span><span style="color:#393a34">></span>
</span><span style="color:#393a34"><span style="color:#d73a49">definePageConfig</span><span style="color:#393a34">(</span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>  navigationBarTitleText</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">'首页'</span>
</span><span style="color:#393a34"><span style="color:#393a34">&#125;</span><span style="color:#393a34">)</span>
</span>
<span style="color:#393a34"><span style="color:#00009f">export</span><span> </span><span style="color:#00009f">default</span><span> </span><span style="color:#393a34">&#123;</span><span style="color:#393a34">&#125;</span>
</span><span style="color:#393a34"><span style="color:#393a34"></</span><span style="color:#00009f">script</span><span style="color:#393a34">></span></span></code></pre> 
</div> 
<h2 style="text-align:start"><strong>五、其它重要特性与优化</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%23%25E4%25BA%2594%25E5%2585%25B6%25E5%25AE%2583%25E9%2587%258D%25E8%25A6%2581%25E7%2589%25B9%25E6%2580%25A7%25E4%25B8%258E%25E4%25BC%2598%25E5%258C%2596" target="_blank">​</a></h2> 
<h3 style="text-align:start"><strong>性能</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%23%25E6%2580%25A7%25E8%2583%25BD" target="_blank">​</a></h3> 
<ul> 
 <li>修复<span> </span><code>eventSource</code><span> </span>导致的内存泄漏的问题，相关<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fcommit%2F41c7cef9b0832306e096121b84a26947b896416e" target="_blank">commit</a>。</li> 
 <li>修复<span> </span><code>CustomWrapper</code><span> </span>嵌套使用后失效的问题，感谢<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCS-Tao" target="_blank">@CS-Tao</a><span> </span>的贡献。</li> 
 <li>运行时体积优化，相比 Taro v3.3 版本大约减少了<span> </span><strong>30k</strong><span> </span>空间。</li> 
</ul> 
<h3 style="text-align:start"><strong>特性</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%23%25E7%2589%25B9%25E6%2580%25A7" target="_blank">​</a></h3> 
<ul> 
 <li>支持微信小程序开发者工具的<strong>热重载</strong>功能，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fdocs%2Fnext%2Fmini-troubleshooting%23%25E7%2583%25AD%25E9%2587%258D%25E8%25BD%25BD" target="_blank">文档地址</a>。</li> 
 <li>支持支付宝小程序<span> </span><strong>2.0 构建</strong>。</li> 
 <li>H5 端支持配置渲染页面的容器 id，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fdocs%2Fnext%2Fapp-config%23appid" target="_blank">文档地址</a></li> 
 <li>H5 端路由规则调整，Query 参数不再添加到<span> </span><code>pageId</code><span> </span>中，同时<span> </span><code>TabBar</code><span> </span>页面不会重新创建重复节点。</li> 
 <li>H5 端支持<span> </span><code>entryPagePath</code><span> </span>参数，by<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fliuchuzhang" target="_blank">@liuchuzhang</a></li> 
 <li>H5 端支持<span> </span><code>CoverView</code><span> </span>&<span> </span><code>CoverImage</code><span> </span>组件，by<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjiaozitang" target="_blank">@jiaozitang</a></li> 
 <li>H5 端支持<span> </span><code>NodesRef.context</code><span> </span>&<span> </span><code>NodesRef.node</code><span> </span>方法</li> 
 <li>H5 端支持通过<span> </span><code>useResize</code><span> </span>方法监听<span> </span><code>resize</code><span> </span>事件</li> 
</ul> 
<h3 style="text-align:start"><strong>修复</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%23%25E4%25BF%25AE%25E5%25A4%258D" target="_blank">​</a></h3> 
<ul> 
 <li>修复预渲染失败的问题。</li> 
 <li>修复多个页面使用同一个组件时，因为组件定义了<span> </span><code>id</code><span> </span>而导致事件触发失效的问题。</li> 
 <li>修复 H5 端多页面滚动事件偶发性触发错误问题。</li> 
 <li>修复 3.x 中 H5 端 API 失效的 Shaking 能力。</li> 
</ul> 
<h2 style="text-align:start"><strong>六、Breaking Changes</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%23%25E5%2585%25ADbreaking-changes" target="_blank">​</a></h2> 
<ul> 
 <li>旧项目升级到 Taro v3.4 需要安装对应的<strong>框架适配插件</strong>，详情浏览升级指南。</li> 
 <li>百度小程序使用<span> </span><code>onInit</code><span> </span>代替<span> </span><code>onLoad</code><span> </span>生命周期，以优化首次启动时间。</li> 
 <li>H5 端调整了 showModal 返回的 errMsg 参数，和小程序接口对齐，如果项目内针对这个差异做过适配，可以在升级后移除。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11040" target="_blank">#11040</a></li> 
</ul> 
<h2 style="text-align:start"><strong>升级指南</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%23%25E5%258D%2587%25E7%25BA%25A7%25E6%258C%2587%25E5%258D%2597" target="_blank">​</a></h2> 
<h3 style="text-align:start"><strong>1. 把 Taro CLI 更新到<span> </span><code>v3.4.0</code>：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%231-%25E6%258A%258A-taro-cli-%25E6%259B%25B4%25E6%2596%25B0%25E5%2588%25B0-v340" target="_blank">​</a></h3> 
<div style="text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#d73a49">npm</span><span> i -g @tarojs/cli</span></span></code></pre> 
</div> 
<h3 style="text-align:start"><strong>2. 更新项目依赖</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%232-%25E6%259B%25B4%25E6%2596%25B0%25E9%25A1%25B9%25E7%259B%25AE%25E4%25BE%259D%25E8%25B5%2596" target="_blank">​</a></h3> 
<blockquote> 
 <p>如果安装失败或打开项目失败，可以删除<span> </span><strong>node_modules</strong>、<strong>yarn.lock</strong>、<strong>package-lock.json</strong><span> </span>后重新安装依赖再尝试。</p> 
</blockquote> 
<p style="color:#1c1e21; text-align:start">修改<span> </span><code>package.json</code><span> </span>文件中 Taro 相关依赖的版本修改为<span> </span><code>3.4.0</code>，再重新安装依赖。</p> 
<h3 style="text-align:start"><strong>3.【Breaking Changes】安装对应的框架适配插件</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%233breaking-changes%25E5%25AE%2589%25E8%25A3%2585%25E5%25AF%25B9%25E5%25BA%2594%25E7%259A%2584%25E6%25A1%2586%25E6%259E%25B6%25E9%2580%2582%25E9%2585%258D%25E6%258F%2592%25E4%25BB%25B6" target="_blank">​</a></h3> 
<p style="color:#1c1e21; text-align:start">因为 Taro v3.4 把各前端框架的适配逻辑拆分到对应的插件中，因此旧项目升级时需要安装对应框架的适配插件：</p> 
<ul> 
 <li>使用 React，请安装<span> </span><code>@tarojs/plugin-framework-react</code></li> 
 <li>使用 Vue2，请安装<span> </span><code>@tarojs/plugin-framework-vue2</code></li> 
 <li>使用 Vue3，请安装<span> </span><code>@tarojs/plugin-framework-vue3</code></li> 
</ul> 
<h2 style="text-align:start"><strong>最后</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022-01-20-Taro-3.4%23%25E6%259C%2580%25E5%2590%258E" target="_blank">​</a></h2> 
<p style="color:#1c1e21; text-align:start">接下来 Taro v3.6 的工作重心将会放在小程序性能优化、编译系统升级（如升级 Webpack5）和优化 H5 能力（如输出 SSR 方案、优化路由系统等）上。</p> 
<p style="color:#1c1e21; text-align:start">Taro 迭代的另一条主线是对<span> </span><strong>鸿蒙应用 && OpenHarmony</strong><span> </span>的适配，Taro 与 OpenHarmony 团队成立了<a href="https://gitee.com/NervJS/community/blob/master/sig/sig-crossplatformui/sig_crossplatformui_cn.md" target="_blank">跨平台 UI 兴趣组</a>，将联合社区共同展开适配工作。目前第一阶段的开发工作已完成，并发布了 Taro v3.5-canary 版本。</p> 
<p style="color:#1c1e21; text-align:start">相关咨询：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fdiscussions%2Fcategories%2F%25E9%25B8%25BF%25E8%2592%2599-openharmony-%25E9%2580%2582%25E9%2585%258D%25E5%25B0%258F%25E7%25BB%2584" target="_blank">鸿蒙 && OpenHarmony 适配小组</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fprojects%2F2" target="_blank">适配进度</a></li> 
</ul> 
<p style="color:#1c1e21; text-align:start">鸿蒙 & OpenHarmony 交流群：</p> 
<p style="color:#1c1e21; text-align:start"><img alt="Taro X Harmony 交流群" src="http://storage.360buyimg.com/taro-jd-com/static/contact_taro_harmony_qr.png" referrerpolicy="no-referrer"></p> 
<p style="color:#1c1e21; text-align:start">最后，衷心感谢参与了 Taro 开源共建的各位同学，也欢迎更多的同学参与进来！</p>
                                        </div>
                                      
</div>
            