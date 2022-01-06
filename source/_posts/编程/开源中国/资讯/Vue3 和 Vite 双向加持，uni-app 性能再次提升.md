
---
title: 'Vue3 和 Vite 双向加持，uni-app 性能再次提升'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9899'
author: 开源中国
comments: false
date: Thu, 06 Jan 2022 16:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9899'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span style="color:#24292e">uni-app 对 vue3 & Vite 的升级，是一个渐进式过程：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">2020年9月：小程序平台支持 vue3 开发，小程序平台编译器依然使用webpack；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">2021年5月：H5平台支持 vue3 开发，H5平台编译器升级为 Vite；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">2021年8月：App平台支持 vue3 开发，App平台编译器升级为 Vite；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">2021年11月：小程序平台编译器升级为 Vite；</p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">至此，uni-app 在全平台支持了 Vite 编译及Vue 3.x 运行。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"> </p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">so，这场持续一年之久的大版本升级，究竟给 uni-app 项目带来了哪些提升？</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">是时候总结（秀）一波了。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">新版 uni-app 框架主要做了三大改进：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">重写框架内核：基于 vue3 + ts 重写内置组件和API，实现更彻底、更高效的  tree-shaking；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增支持 Vite 构建工具，在H5平台实现秒开预览；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增支持 Vue3.x，实现更灵活的开发方式，及更高的运行性能；</p> </li> 
</ul> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">基于这三大改进，uni-app 项目获得了<span><strong><span style="color:#407600">多快好省</span></strong></span>四大收益：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">更多的语法支持，支持组合式API，业务聚焦，开发效率更高；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">更快的编译速度，H5平台十倍加速，小程序、App加速30%以上；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">更好的运行性能，用户端响应更快，体验更好；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">更小的代码体积，瘦身30%以上，更省体积、更省流量</p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span style="color:#407600">更多的语法支持</span></h2> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">新版 uni-app 支持Vue 3.x框架，支持组合式API，可实现更聚焦的业务开发。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">Vue 3.x的一些新增特性，uni-app 也已经完全支持，如：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">支持<code><script setup></code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持<code><style scoped></code>、<code><style module></code>、<code>State-Driven Dynamic CSS(v-bind)</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持<code>jsx</code>、<code>tsx</code>（h5,app 平台支持，小程序不支持）</p> </li> 
</ul> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">另外，在小程序平台，新版 uni-app 也扩展了更多的语法，如：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">更完善的模板语法支持（如 <code>class</code>、<code>style</code> 支持函数、变量等，不再局限数组、对象类型）</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">更完整的 <code>props</code> 支持（如传递函数）</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">更完善的 <code>slot</code> 支持（如作用域插槽）</p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span style="color:#407600">更快的编译速度</span></h2> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">开发者日常工作中，最无聊的就是等待编译构建。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">某乎上还有一个<em>”程序员在等待编译的时候都做什么？“</em>的讨论帖，可见编译时间对开发者而言，是一个多么尴尬无聊的碎片时间。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><span>uni-app 本次升级 vue3 & Vite </span><span>后，在编译时间上有多少改进？</span><span>带给开发者多少福利？</span><span>我们安排真实测试，以数据说话。</span></p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">测试环境说明：</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>硬件：RedmiBook 14 二代
处理器：Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz 
内存：16.0 GB
操作系统：Windows 11 专业版 64 位操作系统</code></pre> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">关于编译速度，我们做了两个维度的对比：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>纵向对比：</span><span>挑选 uni-app 常用项目模板，在H5、小程序、App平台，分别测试 vue 2.6 和 vue 3.x 的</span><span>编译时间</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">横向对比：使用业内优秀的其它跨端框架，创建默认项目模板，记录其编译时间，和 uni-app 的 vue 3.x 版本进行对比</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">uni-app 历史版本纵向对比</h3> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">我们选择<code>uni-app默认模板</code>、<code>uni-starter</code>、<code>hello-uniapp</code>三个项目模板，分别测试 <span style="color:#24292e">vue 2.6 和 vue 3.x  </span>的编译时间。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">uni-app项目编译时间的采集方式：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>vue 2.6 版编译时间 = webpack 的 stats.endTime - stats.startTime</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>vue 3.x 版</span><span style="color:#333333">编译时间 = 构建工具入口处记录 global.vite_start_time = performance.now()，构建工具编译完成时：</span><span style="color:#333333">performance.now() - global.vite_start_time</span></p> </li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">H5平台</h4> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">对<span style="color:#24292e"> uni-app </span>的三个项目模板分别运行到H5平台，进行多次编译测试，并求其均值后，获得如下数据：</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-7e8b5103081cd7154afa4782bb14b6c5617.png" referrerpolicy="no-referrer"></p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">由此，我们可以观察到：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">在 vue 2.6 环境下，随着项目复杂度的提升，H5首页预览所需编译时间会直线增加；这是因为在 vue 2.6 版本下，虽然仅预览首页，但依然会使用 <code>webpack</code> 编译整个项目资源；故项目越复杂，编译时间越长；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">在 vue 3.x 环境下，H5首页预览的编译时间跟项目复杂度也有关系，但增幅不大；这是因为在 vue 3.x 版本下，使用 Vite 进行构建，预览首页时仅编译首页及首页所依赖资源，不会编译其它页面资源。</p> </li> 
</ul> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">通过图表对比，我们可以直观得出结论：vue 3.x 环境下的首页编译时间，平均不到 vue 2.6 环境下的十分之一。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">换言之，<span style="color:#24292e"> vue 3.x </span>版本下的首页编译速度，相比<span style="color:#24292e"> </span><span style="color:#24292e">vue 2.6 </span>版本，有<span style="color:#407600">十倍效率提升</span>。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">这个十倍效率提升，主要得益于新版采用<code>Vite</code>作为构建工具，由此带来了两大好处：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">使用原生 ESM 文件，无需打包，实现极速的服务启动；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">预览（运行）使用<code>esbuild</code>作为打包工具，相比<span style="color:#24292e"> </span><span style="color:#24292e">vue 2.6 </span>环境下的<code>webpack</code>，构建速度快 10-100 倍（这不是我们夸大，详见<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesbuild.docschina.org%2F" target="_blank">esbuild</a>官网）</p> </li> 
</ul> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">本着这个<span>十倍效率提升</span>，小伙伴们还不赶紧上手试试？</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">小程序平台</h4> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">对<span style="color:#24292e"> uni-app </span>的三个模板项目运行到微信小程序平台，多次编译测试，并求其均值后，获得如下数据：</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-b8c87a9b1d6cff81b4085d7d427c3bd578d.png" referrerpolicy="no-referrer"></p> 
<p>从上图对比数据来看，我们可以得出结论：小程序平台，<span style="color:#24292e"> </span><span style="color:#24292e">vue 3.x </span>版本下的运行编译，相比<span style="color:#24292e"> </span><span style="color:#24292e">vue 2.6 </span>版本，编译性能至少提升30%；且项目越复杂，编译性能提升越明显，可以达到40% ~ 50%。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">App平台</h4> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">对<span style="color:#24292e"> uni-app </span>的三个项目模板继续运行到App平台，多次编译测试，并求其均值后，获得如下数据：</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-f100789362e36bb2e4129ce334ce01249bc.png" referrerpolicy="no-referrer"></p> 
<p>从上图对比数据来看，我们可以得出结论：App平台，<span style="color:#24292e"> </span><span style="color:#24292e">vue 3.x </span>版本下的运行编译，相比<span style="color:#24292e"> </span><span style="color:#24292e">vue 2.6 </span>版本，编译性能提升将近50%。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">虽没有H5平台的十倍效率提升那么刺激，但<span style="color:#407600">将近50%的速度提升</span>，经常开发小程序/App的小伙伴，还不心动？</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">业内优秀框架横向对比</h3> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">除了采用不同版本的<span style="color:#24292e"> uni-app </span>进行纵向对比外，我们还使用业内优秀的跨端框架<code>Taro</code>，创建空的项目模板，进行横向对比测试。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">具体测试方案：</p> 
<ol style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">安装<code>Taro</code>的最新cli，本文测试时使用的版本为"@tarojs/taro": "3.3.16"</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">使用<code>Taro init</code>命令，分别选择<code>react</code>、<code>vue</code>、<code>vue3</code>框架，创建三个默认项目模板，三个项目名称分别为<code>taro3-react</code>、<code>taro3-vue</code>、<code>taro3-vue3</code>，如下图： <br> <img alt src="https://oscimg.oschina.net/oscnet/up-160f6d6ea6ad7f50ef10cc5d637a05e74aa.png" referrerpolicy="no-referrer"></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">使用<code>npm run dev:h5</code>，运行到H5平台进行预览，记录每次预览编译时间，重复执行，求其均值</p> </li> 
</ol> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">关于<code>Taro</code>编译时间的计算方案：</p> 
<ol style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">开发一个<code>Taro</code>扩展插件，插件规范参考<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftaro-docs.jd.com%2FTaro%2Fdocs%2Fplugin%2F" target="_blank">Taro官网 - 插件功能</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">在<code>ctx.onBuildStart</code>中记录开始编译时间</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">在<code>ctx.onBuildFinish</code>中记录编译结束时间</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">两者的时间差，即为编译过程消耗时间</p> </li> 
</ol> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">然后使用<span style="color:#24292e"> uni-app </span>的<code>cli</code>命令行，创建基于<span style="color:#24292e"> </span><span style="color:#24292e">vue 3.x </span>的空项目模板，项目命名为<code>uni-app-vue3</code>。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">我们使用各自框架的命令行，将如上创建的5个项目分别编译到H5平台和小程序平台，多次测试，并求其均值。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">同框架版本在H5平台上的编译时间，结果如下：</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-dac87437358e25ef9ba996d8497eabb01b6.png" referrerpolicy="no-referrer"></p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">从图中可以看出，<span style="color:#24292e"> uni-app </span>的 vue3 版本，在H5平台上的首页编译预览性能是遥遥领先的。这个遥遥有多远呢？这么讲吧，你都编译20次了，友商第一次还没完呢。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">继续编译到微信小程序平台，多次测试，求其均值，结果如下：</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-81ac541733208c743578c1621561cf5c5b7.png" referrerpolicy="no-referrer"></p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">从图中可以看出，<span style="color:#24292e"> uni-app </span>的<span style="color:#24292e"> </span><span style="color:#24292e">vue 3.x </span>版本，在微信小程序平台上的编译性能也是遥遥领先的，这个遥遥也不近。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span style="color:#407600">更好的运行速度</span></h2> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">开发环节编译快了，那面向最终用户的软件，运行性能怎么样？</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">我们进入性能测试章节。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">测试方案：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">开发内容：开发一个仿微博小程序首页的复杂长列表，支持下拉刷新、上拉翻页、点赞。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">界面如下： <br> <img alt src="https://oscimg.oschina.net/oscnet/up-14ea9bc3ab753dc9f9937ea378da4d0d122.png" referrerpolicy="no-referrer"></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">测试机型：小米 Mi 10 pro、MIUI 12.5 (21.11.3 开发版) 、微信版本 8.0.16</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">准备工作：每次开始测试前，杀掉各App进程、清空内存，保证测试机环境基本一致；每次从本地读取静态数据，屏蔽网络差异。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">评测点：长列表中的某个组件，比如点赞组件，点击时是否能及时的修改未赞和已赞状态？</p> </li> 
</ul> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">测试计时方式：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">选中某微博，点击“点赞”按钮，实现点赞状态状态切换（已赞高亮、未赞灰色），</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">点赞按钮 onclick函数开头开始计时，setData回调函数开头结束计时；</p> </li> 
</ul> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">在小米手机上进行多次测试，求其平均值，结果如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img alt src="https://oscimg.oschina.net/oscnet/up-a3c9f9c50a8177995500673370c4e885b90.png" referrerpolicy="no-referrer"></p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">从表格中可以看出：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">随着页面记录的增加，<span style="color:#24292e"> </span><span style="color:#24292e">vue 2.6 </span>版本的<span style="color:#24292e"> uni-app </span>项目，点赞组件响应时间快速增加，响应越来越慢；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">基于<span style="color:#24292e"> </span><span style="color:#24292e">vue 3.x </span>的<span style="color:#24292e"> uni-app </span>项目，点赞组件的响应时间跟页面条数无关，一直保持极高的响应灵敏度，性能体验远高于<span style="color:#24292e"> </span><span style="color:#24292e">vue 2.6 </span>版本。</p> </li> 
</ul> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">从这个常见的长列表组件响应实验来看，<span style="color:#24292e"> </span><span style="color:#24292e">vue 3.x </span>的性能体验要远高于<span style="color:#24292e"> </span><span style="color:#24292e">vue 2.6 </span>版本。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span style="color:#407600">更小的代码体积</span></h2> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">项目发行后的代码体积，是一个很重要的考量指标：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">H5平台：更小的代码体积，可以帮助开发者节省服务端带宽及CDN流量，可实现更快的资源加载及页面渲染；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">小程序平台：更小的代码体积，可加速小程序包的下载（甚至可能免了分包加载的繁琐），帮助用户更快进入小程序业务界面；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">App平台：更小的代码体积，可实现更快的App启动，帮助用户更快进入App首页</p> </li> 
</ul> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">为了测试 vue 3.x 新版升级后，代码体积的变化，我们同样做了两个维度的测试：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">纵向对比：选择<span style="color:#24292e"> uni-app </span>常用项目模板，在H5、小程序、App平台，分别测试<span style="color:#24292e"> </span><span style="color:#24292e">vue 2.6 </span>和<span style="color:#24292e"> </span><span style="color:#24292e">vue 3.x </span>的编译包大小</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">横向对比：使用业内优秀的其它跨端框架，创建默认项目模板，记录其编译后的包体积大小，和 uni-app 版本进行对比</p> </li> 
</ul> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">Tips：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">开发阶段重在编译速度，对应<code>npm run dev</code>操作</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">发行阶段重在编译包大小，对应<code>npm run build</code>操作</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">uni-app 不同版本纵向对比</h3> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">我们复用之前创建的<code>uni-app默认模板</code>、<code>uni-starter</code>、<code>hello-uniapp</code>三个项目模板，分别测试<span style="color:#24292e"> </span><span style="color:#24292e">vue 2.6 </span>和<span style="color:#24292e"> </span><span style="color:#24292e">vue 3.x </span>的编译包体积。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292e"> uni-app </span>项目编译包体积的采集方式：编译到对应平台后，记录编译后文件夹的大小。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">H5平台</h4> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">H5平台编译后代码体积记录如下：</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-d42bd3115724d643f63e69a8f6c38e36d0d.png" referrerpolicy="no-referrer"></p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">从统计结果来看，<span style="color:#24292e"> uni-app </span>的<span style="color:#24292e"> </span><span style="color:#24292e">vue 3.x </span>版本，在H5平台上的编译包体积至少瘦身30%以上。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">H5平台的瘦身优化，主要得益于<span style="color:#24292e"> uni-app </span>框架的底层全面重构，实现了更彻底的摇树优化。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">小程序平台</h4> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">微信小程序平台编译后代码体积记录如下：</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-66f370cb4bd4091a681b0895a085ce58a0d.png" referrerpolicy="no-referrer"></p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">从统计结果来看，<span style="color:#24292e"> uni-app </span>的<span style="color:#24292e"> </span><span style="color:#24292e">vue 3.x </span>版本，在小程序平台上也有大幅瘦身。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">App平台</h4> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">App平台编译后代码体积记录如下： </p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-02981702206e250d6c8962a8bbb256ff276.png" referrerpolicy="no-referrer"></p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">从统计结果来看，<span style="color:#24292e"> uni-app </span>的<span style="color:#24292e"> </span><span style="color:#24292e">vue 3.x </span>版本，在App平台上根据项目不同，会有不同幅度的瘦身。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">从理论上来讲，项目中的页面模板越复杂，App平台的瘦身效果越明显。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">业内优秀框架横向对比</h3> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">关于编译后的代码体积，我们也和业内优秀的跨端框架<code>Taro</code>进行了对比，复用前面章节创建的三个<code>Taro</code>项目，分别编译到H5平台和小程序平台，计算其编译后的源码文件夹大小。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-dbe3f2172ffc5b47e1ce6555c2036a5e235.png" referrerpolicy="no-referrer"></p> 
<p>从图中可以看出，<span style="color:#24292e"> uni-app </span>的 vue3 版本，在H5平台上编译包体积是最小的，只有友商的十分之一左右。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">我们继续测试，不同版本框架发行到微信小程序平台，记录其编译包大小：</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-3fa52feb52fb73240aa68d7f1cdfaa29c6b.png" referrerpolicy="no-referrer"></p> 
<p>从图中可以看出，<span style="color:#24292e"> uni-app </span>的 vue3 版本，在小程序平台上编译包体积也是最小的。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start"><span>Tips：</span>细心的开发者会发现，所有框架版本编译到小程序上的代码包体积都远小于其在H5平台上的包体积，这是因为小程序由平台厂商提供内置组件及接口实现，而H5平台则需跨端框架自己实现内置组件及接口，故H5平台的代码包普遍要大一些。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span style="color:#407600">总结</span></h2> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">综上，我们以数字说话，阐述了基于 vue3 版本开发<span style="color:#24292e"> uni-app 项目</span>的诸多优势，再回顾一遍：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">更多的语法</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">更快的编译</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">更好的运行</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">更少的代码</p> </li> 
</ul> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">你还不赶紧升级新版 uni-app 来试试吗？</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">对文本测试过程及结果有疑问的同学，欢迎到github上提交<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdcloudio%2Funi-app" target="_blank">issue</a>，欢迎指正。</p>
                                        </div>
                                      
</div>
            