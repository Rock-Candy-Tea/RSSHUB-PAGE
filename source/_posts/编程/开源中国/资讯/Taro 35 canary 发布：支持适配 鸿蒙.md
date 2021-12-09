
---
title: 'Taro 3.5 canary 发布：支持适配 鸿蒙'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img11.360buyimg.com/imagetools/jfs/t1/207457/5/11670/466511/61b05b41E43730965/de2d1029083cc60d.png'
author: 开源中国
comments: false
date: Thu, 09 Dec 2021 20:20:00 GMT
thumbnail: 'https://img11.360buyimg.com/imagetools/jfs/t1/207457/5/11670/466511/61b05b41E43730965/de2d1029083cc60d.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:start">一、背景<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2021-12-08-Taro-3.5-canary%23%25E4%25B8%2580%25E8%2583%258C%25E6%2599%25AF" target="_blank">​</a></h2> 
<p style="color:#1c1e21; text-align:start">鸿蒙作为华为自研开发的一款可以实现万物互联的操作系统，一经推出就受到了很大的关注，被国人寄予了厚望。而鸿蒙也没让人失望，今年 Harmony2.0 正式推出供用户进行升级之后，在短短的三个月内实现了 1.2 亿的装机量，并且在前不久的华为开发者大会上，华为宣布 Harmony2.0 的装机量已经突破了 1.5 亿。</p> 
<p style="color:#1c1e21; text-align:start">众多应用厂商都逐步推出了适配的鸿蒙应用，Taro 作为一个开放式的 跨端跨框架 解决方案，不少开发者期待将小程序的能力移植到鸿蒙 OS 上，可以使用 Taro 开发鸿蒙 && OpenHarmony 应用。</p> 
<p style="color:#1c1e21; text-align:start">鸿蒙的方舟开发框架提供类 Web 范式编程，支持使用 JS 开发 UI 层，其语法与小程序相接近。经过前期调研，可以沿用 Taro 现有的架构适配鸿蒙</p> 
<p style="color:#1c1e21; text-align:start">今年 6 月份我们新建了支持鸿蒙的提案，希望能达成三大目标：</p> 
<ul> 
 <li>开发者可以使用 Taro 开发鸿蒙应用。</li> 
 <li>开发者可以把现有的 Taro 应用适配到鸿蒙平台。</li> 
 <li>开发者可以使用 Taro 的反向转换工具，把原生开发的小程序转换为 Taro 应用，再适配到鸿蒙平台。</li> 
</ul> 
<p style="color:#1c1e21; text-align:start">目前 Taro 和 OpenHarmony 建立了官方合作关系，并成立了<a href="https://gitee.com/NervJS/community/blob/master/sig/sig-crossplatformui/sig_crossplatformui_cn.md" target="_blank">跨平台 UI 兴趣小组</a>，同时 Taro 与华为保持着内部沟通与分享，Taro 拥有的海量开发者和优秀案例，能有效补充鸿蒙生态。</p> 
<h2 style="text-align:start">二、实现细节<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2021-12-08-Taro-3.5-canary%23%25E4%25BA%258C%25E5%25AE%259E%25E7%258E%25B0%25E7%25BB%2586%25E8%258A%2582" target="_blank">​</a></h2> 
<p style="color:#1c1e21; text-align:start">鸿蒙的 JS UI 语法与小程序类似，但毕竟两者底层原理不一样，不可避免地存在许多差异。接下来将简单介绍鸿蒙与小程序的主要差异，和 Taro 又是如何处理这些差异的。</p> 
<h3 style="text-align:start">1. 鸿蒙与小程序的异同<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2021-12-08-Taro-3.5-canary%231-%25E9%25B8%25BF%25E8%2592%2599%25E4%25B8%258E%25E5%25B0%258F%25E7%25A8%258B%25E5%25BA%258F%25E7%259A%2584%25E5%25BC%2582%25E5%2590%258C" target="_blank">​</a></h3> 
<h4 style="text-align:start">1.1 项目组织<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2021-12-08-Taro-3.5-canary%2311-%25E9%25A1%25B9%25E7%259B%25AE%25E7%25BB%2584%25E7%25BB%2587" target="_blank">​</a></h4> 
<p style="color:#1c1e21; text-align:start">鸿蒙的项目组织和小程序类似，有入口文件<span> </span><code>app.js</code><span> </span>、页面、自定义组件。</p> 
<p style="color:#1c1e21; text-align:start">其中页面、自定义组件均由三类文件组成：</p> 
<ul> 
 <li><code>.hml</code><span> </span>用来描述布局结构。与小程序的模板文件相比，语法、支持的能力有少许区别。</li> 
 <li><code>.css</code><span> </span>用来描述页面样式。</li> 
 <li><code>.js</code><span> </span>用于处理页面和用户的交互，默认支持 ES6 语法。</li> 
</ul> 
<h4 style="text-align:start">1.2 配置文件<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2021-12-08-Taro-3.5-canary%2312-%25E9%2585%258D%25E7%25BD%25AE%25E6%2596%2587%25E4%25BB%25B6" target="_blank">​</a></h4> 
<p style="color:#1c1e21; text-align:start">和小程序规定的入口文件、页面文件、自定义组件各自对应一份配置文件不一样，鸿蒙 JS UI 的配置文件只有一份。</p> 
<p style="color:#1c1e21; text-align:start">鸿蒙的<strong>路由</strong>和小程序一样是配置式的，需要在 JS UI 的配置文件中进行配置。</p> 
<h4 style="text-align:start">1.3 样式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2021-12-08-Taro-3.5-canary%2313-%25E6%25A0%25B7%25E5%25BC%258F" target="_blank">​</a></h4> 
<p style="color:#1c1e21; text-align:start">CSS 方面，鸿蒙和 RN 一样有着诸多限制。例如不支持盒子模型、各组件只支持部分 CSS 属性等。</p> 
<h4 style="text-align:start">1.4 组件 & API<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2021-12-08-Taro-3.5-canary%2314-%25E7%25BB%2584%25E4%25BB%25B6--api" target="_blank">​</a></h4> 
<p style="color:#1c1e21; text-align:start">鸿蒙提供了一系列功能丰富的组件，与小程序的组件相比，命名、功能上略有差别。</p> 
<p style="color:#1c1e21; text-align:start">API 也是一样的，两者的 API 集合有部分交集，用法、功能上有差别。</p> 
<h3 style="text-align:start">2. 兼容细节<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2021-12-08-Taro-3.5-canary%232-%25E5%2585%25BC%25E5%25AE%25B9%25E7%25BB%2586%25E8%258A%2582" target="_blank">​</a></h3> 
<h4 style="text-align:start">2.1 Taro 可以解决什么？<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2021-12-08-Taro-3.5-canary%2321-taro-%25E5%258F%25AF%25E4%25BB%25A5%25E8%25A7%25A3%25E5%2586%25B3%25E4%25BB%2580%25E4%25B9%2588" target="_blank">​</a></h4> 
<p style="color:#1c1e21; text-align:start">Taro 适配鸿蒙致力于尽可能地抹平差异，但作为一个框架，注定有它能够解决和不能解决的问题。</p> 
<p style="color:#1c1e21; text-align:start">语法差异可以通过编写运行时框架去处理；使用鸿蒙的组件、API 去尽可能地实现微信小程序规范的组件和 API，以抹平两者之间的使用差别。</p> 
<p style="color:#1c1e21; text-align:start">而 CSS 的差异、组件和 API 能力上的差异等依赖着鸿蒙底层实现，Taro 是无法解决的。</p> 
<p style="color:#1c1e21; text-align:start"><img alt="适配方案" src="https://img11.360buyimg.com/imagetools/jfs/t1/207457/5/11670/466511/61b05b41E43730965/de2d1029083cc60d.png" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:start">2.2 鸿蒙插件<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2021-12-08-Taro-3.5-canary%2322-%25E9%25B8%25BF%25E8%2592%2599%25E6%258F%2592%25E4%25BB%25B6" target="_blank">​</a></h4> 
<p style="color:#1c1e21; text-align:start">Taro 在鸿蒙方面的兼容工作主要由<span> </span><code>@tarojs/plugin-platform-harmony</code><span> </span>插件来完成，开发者引入该插件即可编译为鸿蒙应用。它主要做了这些适配工作：</p> 
<p style="color:#1c1e21; text-align:start"><strong>a) 模板</strong></p> 
<p style="color:#1c1e21; text-align:start">熟悉 Taro 的同学都应该清楚，Taro 在小程序端利用<span> </span><code><template></code><span> </span>标签的递归来渲染页面动态的 DOM 树。而鸿蒙中并没有<span> </span><code><template></code><span> </span>，因此我们使用自定义组件进行递归。</p> 
<p style="color:#1c1e21; text-align:start"><strong>b) 运行时</strong></p> 
<p style="color:#1c1e21; text-align:start">运行时主要在鸿蒙端兼容了小程序的生命周期和数据更新方法<span> </span><code>setData</code><span> </span>。</p> 
<p style="color:#1c1e21; text-align:start"><strong>c) 组件 & API</strong></p> 
<p style="color:#1c1e21; text-align:start">我们使用鸿蒙的原生语法封装了符合微信小程序规范的组件库和 API 库。在兼容微信小程序的属性的同时，也保留了鸿蒙独有的支持属性。</p> 
<p style="color:#1c1e21; text-align:start">目前共适配了 29 个组件，16 类API。组件示例库可参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro-components-sample%2Ftree%2Fharmony" target="_blank">taro-components-sample</a></p> 
<p style="color:#1c1e21; text-align:start"><img alt="组件示例图" src="https://img14.360buyimg.com/imagetools/jfs/t1/137976/7/22742/2461697/61b17384Ebbb815c0/4949c696d9a49283.jpg" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">3. 架构图<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2021-12-08-Taro-3.5-canary%233-%25E6%259E%25B6%25E6%259E%2584%25E5%259B%25BE" target="_blank">​</a></h3> 
<p style="color:#1c1e21; text-align:start"><img alt="架构图" src="https://img14.360buyimg.com/imagetools/jfs/t1/215443/28/7034/1135729/61b05b42E21c6230a/5e8fc76941f98920.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">三、使用方法<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2021-12-08-Taro-3.5-canary%23%25E4%25B8%2589%25E4%25BD%25BF%25E7%2594%25A8%25E6%2596%25B9%25E6%25B3%2595" target="_blank">​</a></h2> 
<p style="color:#1c1e21; text-align:start">如您是新项目， 升级 Taro 选择鸿蒙模板即可；</p> 
<p style="color:#1c1e21; text-align:start">旧项目需要按照如下方法进行手动配置：</p> 
<h3 style="text-align:start">1. 把 Taro 升级到 v3.5.0-canary.0 版本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2021-12-08-Taro-3.5-canary%231-%25E6%258A%258A-taro-%25E5%258D%2587%25E7%25BA%25A7%25E5%2588%25B0-v350-canary0-%25E7%2589%2588%25E6%259C%25AC" target="_blank">​</a></h3> 
<p style="color:#1c1e21; text-align:start">首先需要安装<span> </span><code>v3.5.0-canary.0</code><span> </span>的 CLI 工具</p> 
<div style="text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span>npm i </span><span style="color:#393a34">-</span><span>g @tarojs</span><span style="color:#393a34">/</span><span>cli@canary</span>
</span></code></pre> 
</div> 
<p style="color:#1c1e21; text-align:start">然后更新项目本地的 Taro 相关依赖：把 <code>package.json</code> 文件中 Taro 相关依赖的版本修改为 <code>~3.5.0-canary.0</code>，再重新安装依赖。</p> 
<blockquote> 
 <p>如果安装失败或打开项目失败，可以删除 <strong>node_modules</strong>、<strong>yarn.lock</strong>、<strong>package-lock.json</strong> 后重新安装依赖再尝试。</p> 
</blockquote> 
<h3 style="text-align:start">2. 安装 taro 适配鸿蒙插件<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2021-12-08-Taro-3.5-canary%232-%25E5%25AE%2589%25E8%25A3%2585-taro-%25E9%2580%2582%25E9%2585%258D%25E9%25B8%25BF%25E8%2592%2599%25E6%258F%2592%25E4%25BB%25B6" target="_blank">​</a></h3> 
<p style="color:#1c1e21; text-align:start">（1）Taro 项目中安装鸿蒙插件<span> </span><code>@tarojs/plugin-platform-harmony</code></p> 
<div style="text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span>$ yarn add </span><span style="color:#393a34">--</span><span>dev @tarojs</span><span style="color:#393a34">/</span><span>plugin</span><span style="color:#393a34">-</span><span>platform</span><span style="color:#393a34">-</span><span>harmony</span>
</span></code></pre> 
</div> 
<p style="color:#1c1e21; text-align:start">（2）在 config/index.js 中增加编译配置</p> 
<div style="text-align:start"> 
 <div>
  config/index.js
 </div> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span>config </span><span style="color:#393a34">=</span><span> </span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>  </span><em>// 配置使用插件</em>
</span><span style="color:#393a34"><span>  plugins</span><span style="color:#393a34">:</span><span> </span><span style="color:#393a34">[</span><span style="color:#e3116c">'@tarojs/plugin-platform-harmony'</span><span style="color:#393a34">]</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span>  mini</span><span style="color:#393a34">:</span><span> </span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>    </span><em>// 如果使用开发者工具的预览器（previewer）进行预览的话，需要使用 development 版本的 react-reconciler。</em>
</span><span style="color:#393a34"><span>    </span><em>// 因为 previewer 对长串的压缩文本解析有问题。（真机/远程真机没有此问题）</em>
</span><span style="color:#393a34"><span>    debugReact</span><span style="color:#393a34">:</span><span> </span><span style="color:#36acaa">true</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span>    </span><em>// 如果需要真机断点调试，需要关闭 sourcemap 的生成</em>
</span><span style="color:#393a34"><span>    enableSourceMap</span><span style="color:#393a34">:</span><span> </span><span style="color:#36acaa">false</span>
</span><span style="color:#393a34"><span>  </span><span style="color:#393a34">&#125;</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span>  </span><em>// harmony 相关配置</em>
</span><span style="color:#393a34"><span>  harmony</span><span style="color:#393a34">:</span><span> </span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>    </span><em>// 【必填】鸿蒙应用的绝对路径</em>
</span><span style="color:#393a34"><span>    projectPath</span><span style="color:#393a34">:</span><span> path</span><span style="color:#393a34">.</span><span style="color:#d73a49">resolve</span><span style="color:#393a34">(</span><span>process</span><span style="color:#393a34">.</span><span style="color:#d73a49">cwd</span><span style="color:#393a34">(</span><span style="color:#393a34">)</span><span style="color:#393a34">,</span><span> </span><span style="color:#e3116c">'../MyApplication'</span><span style="color:#393a34">)</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span>    </span><em>// 【可选】HAP 的名称，默认为 'entry'</em>
</span><span style="color:#393a34"><span>    hapName</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">'entry'</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span>    </span><em>// 【可选】JS FA 的名称，默认为 'default'</em>
</span><span style="color:#393a34"><span>    jsFAName</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">'default'</span>
</span><span style="color:#393a34"><span>  </span><span style="color:#393a34">&#125;</span>
</span><span style="color:#393a34"><span style="color:#393a34">&#125;</span>
</span></code></pre> 
 </div> 
</div> 
<h3 style="text-align:start">3. 准备鸿蒙运行环境<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2021-12-08-Taro-3.5-canary%233-%25E5%2587%2586%25E5%25A4%2587%25E9%25B8%25BF%25E8%2592%2599%25E8%25BF%2590%25E8%25A1%258C%25E7%258E%25AF%25E5%25A2%2583" target="_blank">​</a></h3> 
<blockquote> 
 <p>开发鸿蒙软件需要用到 HUAWEI DevEco Studio，它提供了模板创建、开发、编译、调试、发布等服务。</p> 
</blockquote> 
<p style="color:#1c1e21; text-align:start">主要包括以下内容：</p> 
<p style="color:#1c1e21; text-align:start">（1）注册开发者账号</p> 
<p style="color:#1c1e21; text-align:start">（2）下载 DevEco Studio 安装包</p> 
<p style="color:#1c1e21; text-align:start">（3）启动 DevEco Studio，根据工具引导下载 HarmonyOS SDK</p> 
<p style="color:#1c1e21; text-align:start">（4）新建 MyApplication JS项目</p> 
<p style="color:#1c1e21; text-align:start">（5）使用预览器或真机查看应用效果</p> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuejin.cn%2Fpost%2F6972109475347955749" target="_blank">《初窥鸿蒙》</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.harmonyos.com%2Fcn%2Fdevelop%2Fdeveco-studio" target="_blank">《华为开发者工具》</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.harmonyos.com%2Fcn%2Fdocumentation" target="_blank">《鸿蒙开发文档》</a></p> 
</blockquote> 
<h3 style="text-align:start">4. 项目运行<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2021-12-08-Taro-3.5-canary%234-%25E9%25A1%25B9%25E7%259B%25AE%25E8%25BF%2590%25E8%25A1%258C" target="_blank">​</a></h3> 
<p style="color:#1c1e21; text-align:start">运行命令</p> 
<div style="text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span>$ taro build —type harmony —watch</span></span></code></pre> 
</div> 
<p style="color:#1c1e21; text-align:start">若您在步骤 2(2) 设置好了打包输出到鸿蒙项目的路径，即可查看 Taro 适配鸿蒙的应用效果。</p> 
<blockquote> 
 <p>testHarmony 为您通过 DevEco Studio 创建的 JS 项目。</p> 
</blockquote> 
<p style="color:#1c1e21; text-align:start"><img alt="运行效果图" src="https://img13.360buyimg.com/imagetools/jfs/t1/218013/26/7034/2593615/61b05b43Ec927d51c/f2990eef38343eca.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">四、最后<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2021-12-08-Taro-3.5-canary%23%25E5%259B%259B%25E6%259C%2580%25E5%2590%258E" target="_blank">​</a></h2> 
<p style="color:#1c1e21; text-align:start">接下来我们会继续完善对鸿蒙的适配工作，预计会在 2022 年 Q1 发布 v3.5 正式版。</p> 
<p style="color:#1c1e21; text-align:start">同时也希望社区有更多的开发者参与共建，无论是提出 Issues、在论坛发帖、提交 PR 还是帮助建设周边生态等，对我们来说都是宝贵的财富，让我们一起把 Taro 建设的更强。</p> 
<p style="color:#1c1e21; text-align:start">Taro 团队衷心感谢一路走来大家对我们的支持，正是因为大家的期待、信赖敦促我们走向更好。</p> 
<p style="color:#1c1e21; text-align:start">最后，该版本鸿蒙的适配由京东内鸿蒙共建小组共同完成，感谢以下同学：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAdvancedCat" target="_blank">@AdvancedCat</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjiaozitang" target="_blank">@jiaozitang</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhuozhongyi123" target="_blank">@huozhongyi123</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftroy-sxj" target="_blank">@troy-sxj</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJSZabc" target="_blank">@JSZabc</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrazyonebyone" target="_blank">@crazyonebyone</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FevernoteHW" target="_blank">@evernoteHW</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsoulhat" target="_blank">@soulhat</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxueshuai" target="_blank">@xueshuai</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLuMeiling" target="_blank">@LuMeiling</a></p> 
<p style="color:#1c1e21; text-align:start"> </p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"><span style="color:#000000">最后的最后，如果您有任何疑问，可以扫描下方二维码添加我们的 Harmony 小助手进行反馈，感谢您的支持！</span></p> 
<p><img height="354" src="https://oscimg.oschina.net/oscnet/up-7b56ebf2ee4946cbd93185bae2c7a775797.png" width="362" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            