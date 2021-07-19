
---
title: 'Vue3项目转原生小程序插件（一）初始化项目'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c72e324e7be48638b61fe4c98dc255d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 22:22:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c72e324e7be48638b61fe4c98dc255d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,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")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本篇为系列文章的第一篇。讲述如何把现有的 Vue3 项目以最低的成本迁移到微信小程序插件内（后来发现成本并不低）</p>
<p>注：是微信小程序插件，不是微信小程序。如果有不太明白的同学，可以看官方对于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fminiprogram%2Fdev%2Fframework%2Fplugin%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.weixin.qq.com/miniprogram/dev/framework/plugin/" ref="nofollow noopener noreferrer">插件</a> 的介绍。</p>
</blockquote>
<h1 data-id="heading-0"><del>非正规</del>. 引言</h1>
<p>先说一下为什么非要蹚这滩浑水 ~ （下面是与产品经理的一段<code>友好</code>会晤）</p>
<ul>
<li>🐵 产品：我们要做一个插件给微信小程序用。</li>
<li>👨‍💻‍ 我：插件？不是微信小程序？好吧，我了解一下吧...</li>
<li>👨‍💻‍ 我：Emmm，既然做小程序了，那是否考虑支付宝小程序？抖音小程序？等等？</li>
<li>🐵 产品：暂时不考虑，但后期也不是没有可能</li>
<li>👨‍💻‍ 我：啊这？（...文明用语...）知道了</li>
</ul>
<p>我司现有一个 <code>智能在线客服访客端</code> 的项目，是基于 <code>Vue3</code> + <code>Vuex</code> + <code>Typescript</code> + <code>stylus</code> 的，已开发 <code>8</code> 个多月迭代至 <code>V3.3</code> 版本。客户仅需在自己网站的 <code>script</code> 标签中嵌入我们的 <code>SDK</code> 代码，即可为自己的网站提供我司的智能在线客服服务，并且已经支持 <code>pc</code> 端和 <code>h5</code> 端。由于上层要求，某大客户想要将其在自己的小程序内使用，并且明令拒绝使用 <code>webview</code> 嵌入的方式（在后期的尝试中刚好发现，小程序插件根本就不支持使用 <code>webview</code> 标签）。</p>
<p>于是，我被迫走上了这条不归路...</p>
<h1 data-id="heading-1">壹。 各种尝试</h1>
<p>因为我们已经有了现有的 <code>Vue3</code> 项目，而且市场上已经有那么多可以把 <code>vue</code> 项目转化为小程序的编译框架，所以我们初期探索的思路很明确：<strong>使用市场上现有的小程序编译框架将现有的 <code>Vue3</code> 项目以最小的修改成本转换为微信小程序的代码</strong>。于是开始我们的探索之旅。</p>
<blockquote>
<p>在每一小节后面用 <code>×</code> 和 <code>√</code> 已经表明哪种方式是可以正常初始化项目的，不想看中间爬坑内容的朋友，可以只看 <code>本章 1.1 小节</code> 即可。</p>
</blockquote>
<h2 data-id="heading-2">1.1 官方提供的原生小程序插件Demo（√）</h2>
<p>在我们进行各框架采坑之前，我们首先要确保一下 <code>小程序插件</code> 这个东西真实是存在并且现在还是可用的。于是我们去微信公众平台官网找到了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fminiprogram%2Fdev%2Fframework%2Fplugin%2Fdevelopment.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.weixin.qq.com/miniprogram/dev/framework/plugin/development.html" ref="nofollow noopener noreferrer">开发插件</a>的章节，下载了一个所谓<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fs%2FNrPCBmmT7B1B" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.weixin.qq.com/s/NrPCBmmT7B1B" ref="nofollow noopener noreferrer">可以直接在微信开发者工具中查看的完整插件示例</a>。在微信开发者工具中打开，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c72e324e7be48638b61fe4c98dc255d~tplv-k3u1fbpfcp-zoom-1.image" alt="微信小程序插件目录结构" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以发现目录结构跟普通小程序是有一些差异的。</p>
<ul>
<li><code>miniprogram</code> 文件夹：这里面就是普通的微信小程序代码，是用来引入插件并对插件进行测试的（当你上传插件时，审核者会通过这个Demo去审核你插件的功能，所以尽可能完善你的测试页）。</li>
<li><code>plugin</code>文件夹：所有插件的内容都放在了这里面，除了 <code>pages</code>、<code>components</code>、<code>index.js</code> 等基础文件以外，多出了一个 <code>plugin.json</code> 文件，这里面放的就是你要导出的公共组件、页面、以及你插件的入口。</li>
<li><code>project.config.json</code> 文件：该文件的内容同正常小程序的配置文件，就是你插件的配置信息。但有一点区别是，里面多了一个 <code>"compileType": "plugin"</code> 的字段，表明你这个小程序当前是 <code>插件模式</code>。</li>
</ul>
<p>在经过一番尝试之后，基本上已经确定了插件的目录结构与各自功能。只要把你的普通小程序代码，放到 <code>plugin</code> 文件夹下，能够正常的运行起来，并且导出你相应的事件、页面与组件，就完成了小程序插件的开发。</p>
<p>所以，我们接下来的任务就是：如何把现有的 <code>Vue3</code> 项目，转换为 <code>普通小程序</code> 的语法，并且放到 <code>plugin</code> 文件夹内能正常跑起来。</p>
<h2 data-id="heading-3">1.2 Uni-App 框架（×）</h2>
<p>明确了目标，经过初步考虑之后，我们决定使用 <code>DCloud</code> 提供的 <code>Uni-App</code> 框架进行转换。即可以使用 <code>Vue.js</code> 的语法，又能同时编译成 <code>H5</code>、<code>App</code> 和 <code>小程序</code> 等多端平台。而且还有 那(不) 么(算) 庞 大 的插件市场，应该也能对后期的开发提供一些帮助。（简直是不要太符合需求）于是，就开始了...</p>
<p>根据文档中的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Funiapp.dcloud.io%2Fquickstart-hx" target="_blank" rel="nofollow noopener noreferrer" title="https://uniapp.dcloud.io/quickstart-hx" ref="nofollow noopener noreferrer">创建 uni-app 项目</a> 步骤初始化，并启动项目，在微信开发者工具中 <code>完美运行</code>。</p>
<p><img src="https://juejin.cn/post/6986519096623890440" alt="uni-app 项目 运行图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>于是将此项目发布为 <code>微信小程序</code>，将打包后的代码全部复制到 <code>plugin</code> 目录下，<strong>完美报错</strong>！</p>
<pre><code class="copyable">(global["webpackJsonp"]=global["webpackJsonp"]||[]).push([["pages/index/index"]&#123;......&#125;,[["df45","common/runtime","common/vendor"]]]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Emmm...</p>
<p>可能是通过 <code>HBuilderX</code> 创建的项目有问题，那我们通过命令行创建 <code>Uni-App</code> 项目：</p>
<pre><code class="copyable">vue create -p dcloudio/uni-preset-vue#vue3 vue3_uni_app
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样，在微信开发者工具中完美运行，但将代码复制到 <code>plugin</code> 文件夹中，<strong>完美报错</strong>！</p>
<p><strong>弃之。</strong></p>
<h2 data-id="heading-4">1.3 Taro 框架（×）</h2>
<p>后来了解到 <code>tarojs/cli</code> 脚手架可以初始化一个微信小程序插件的模板，于是按照官网给出的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftaro-docs.jd.com%2Ftaro%2Fdocs%2FGETTING-STARTED" target="_blank" rel="nofollow noopener noreferrer" title="https://taro-docs.jd.com/taro/docs/GETTING-STARTED" ref="nofollow noopener noreferrer">安装与使用</a> 安装了脚手架，并根据官网给出的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftaro-docs.jd.com%2Ftaro%2Fdocs%2Fminiprogram-plugin" target="_blank" rel="nofollow noopener noreferrer" title="https://taro-docs.jd.com/taro/docs/miniprogram-plugin" ref="nofollow noopener noreferrer">小程序插件开发</a> 指南初始化了 <code>vue3</code> + <code>typescript</code> + <code>stylus</code> 的插件项目。（简直不要太完美~）</p>
<p>发现项目的目录与 <code>1.1</code> 中官网下载的目录结构很相似，也有 <code>plugin</code> 文件夹</p>
<pre><code class="copyable">├── config 配置目录
├── src 源码目录
| ├── pages 调试页面目录，用于调试插件
| | └── index
| ├── plugin 插件目录
| | ├── doc 插件文档目录
| | ├── components 组件插件目录
| | ├── pages 页面插件目录
| | ├── index.js 接口插件文件
| | └── plugin.json 插件配置文件
| ├── app.css 项目总通用样式
| └── app.js 项目入口文件
└── package.json
└── package.config.json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过明令完美的编译项目。</p>
<pre><code class="copyable">taro build --plugin weapp --watch
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用微信开发者工具打开编译后的 <code>../root/dist/</code> 目录，<strong>完美报错</strong>！</p>
<pre><code class="copyable">(wx["webpackJsonp"]=wx["webpackJsonp"]||[]).push([[7]&#123;......&#125;Page(Object(o["createPageConfig"])(w,"pages/index/index",&#123;root:&#123;cn:[]&#125;&#125;,j||&#123;&#125;))&#125;&#125;,[[40,0,1,2]]]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并尝试只将该 <code>taro</code> 项目打包后的 <code>plugin</code> 文件夹的内容，复制到官网下载的插件项目的 <code>plugin</code> 文件夹下，同样，<strong>完美报错</strong>！</p>
<p><strong>弃之。</strong></p>
<blockquote>
<p>注：使用 <code>tarojs/cli</code> 创建的 <code>react</code> 模板的插件项目是可以跑起来的，但后期开发的坑也贼多，比如各种taro及微信原生的api找不到、修改render就报错、插件安装或使用报错等等，如果有兴趣的可以去尝试，由于跟我的技术栈不匹配，在此就不多赘述了。</p>
</blockquote>
<h2 data-id="heading-5">1.4 mp-vue 框架（×）</h2>
<p>根据 <code>mpvue</code> 官网给出的 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fmpvue.com%2Fmpvue%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://mpvue.com/mpvue/" ref="nofollow noopener noreferrer">使用手册</a> 安装脚手架并初始化了项目，编译后没有报错，将编译后的代码复制到 <code>plugin</code> 文件夹中，同样，<strong>完美报错</strong>！</p>
<p><strong>弃之。</strong></p>
<h2 data-id="heading-6">1.5 WePY（×）</h2>
<p>同样，根据官网给出的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwepyjs.github.io%2Fwepy-docs%2F2.x%2F%23%2Fbase%2Fgetstart" target="_blank" rel="nofollow noopener noreferrer" title="https://wepyjs.github.io/wepy-docs/2.x/#/base/getstart" ref="nofollow noopener noreferrer">安装步骤</a> 安装脚手架并初始化了项目，编译后没有报错，将编译后的代码复制到 <code>plugin</code> 文件夹中，同样，<strong>完美报错</strong>！</p>
<p><strong>弃之。</strong></p>
<h1 data-id="heading-7">总结</h1>
<p>最终，我们 <del>无奈</del> 选择 <code>微信公众平台官网</code> 给出的 <code>插件Demo</code>，并使用微信原生语法进行开发。</p>
<p>一篇踩坑教程到此结束~</p>
<p>谢谢大家~</p>
<p>拜~</p>
<h1 data-id="heading-8">系列文章</h1>
<blockquote>
<p>除了第一篇文章，其他的题目可能还没想好，后期会继续进行完善</p>
</blockquote>
<ul>
<li>
<p><a href="https://juejin.cn/user/2189882894323975/posts" target="_blank" title="https://juejin.cn/user/2189882894323975/posts">Vue3项目转原生小程序插件（一）初始化项目</a></p>
</li>
<li>
<p><a href="https://juejin.cn/user/2189882894323975/posts" target="_blank" title="https://juejin.cn/user/2189882894323975/posts">Vue3项目转原生小程序插件（二）Vue模板拆分成wx模板</a></p>
</li>
<li>
<p><a href="https://juejin.cn/user/2189882894323975/posts" target="_blank" title="https://juejin.cn/user/2189882894323975/posts">Vue3项目转原生小程序插件（三）使用 Mobx 替换 Vuex</a></p>
</li>
<li>
<p><a href="https://juejin.cn/user/2189882894323975/posts" target="_blank" title="https://juejin.cn/user/2189882894323975/posts">Vue3项目转原生小程序插件（四）小程序与插件的事件交互</a></p>
</li>
<li>
<p><a href="https://juejin.cn/user/2189882894323975/posts" target="_blank" title="https://juejin.cn/user/2189882894323975/posts">Vue3项目转原生小程序插件（五）在插件内使用 Http 与 Websocket</a></p>
</li>
<li>
<p>更多...</p>
</li>
</ul></div>  
</div>
            