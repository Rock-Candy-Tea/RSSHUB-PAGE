
---
title: '掌握源码阅读的技巧 - Webpack 篇'
categories: 
 - 编程
 - 掘金
 - — 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/637c07e3a8f44808bd479cfc31834e4f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 10 Mar 2021 21:00:26 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/637c07e3a8f44808bd479cfc31834e4f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>高级前端面试中经常有这么几道题：</p>
<ol>
<li>说一说 loader和 plugin 的区别</li>
<li>webpack 构建流程是怎样的</li>
<li>编写 webpack loader 的思路</li>
<li>编写 webpack plugin 的思路</li>
</ol>
<p>网上能搜到一些答案，但是这些答案我一一看过了，要么过于肤浅留于表面，要么冗长繁杂难以卒读。</p>
<p>如果面试岗位的工资是 20k 以上，面试官必定会追问到更深层次。</p>
<p>因此，我花了一个星期把 Webpack 5 的源码逐行扫了一遍，理出了主要脉络。整个阅读过程我录制成了视频，总时长不到 3 小时，但把 Webpack 的整体架构、打包思路、loader 实现思路、plugin 实现思路、parser 运行流程等都讲到了，最重要的是，通过视频你会掌握「阅读源码的技巧」。</p>
<p>接下来是文字教程：</p>
<hr>
<p><img alt="webpack 流程分析.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/637c07e3a8f44808bd479cfc31834e4f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">webpack-cli 是如何调用 wepack 的</h1>
<pre><code class="copyable">webpack = require('webpack')
compiler = webpack(options, callback)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">hooks.xxx.call 是什么</h1>
<p>Tapable 是 webpack 团队为了写 Webpack 而写的一个事件/钩子库</p>
<p>用法</p>
<pre><code class="copyable">定义一个事件/钩子
this.hooks.eventName = new SyncHook(["arg1", "arg2"]);
监听一个事件/钩子
this.hooks.eventName.tap('监听理由', fn)
触发一个事件/钩子
this.hooks.eventName.call('arg1', 'arg2')
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">Webpack 的整体流程是怎样的</h1>
<p>至少有 env init run beforeCompile compile compilation make finishMake seal optimize afterCompile emit 等钩子</p>
<h1 data-id="heading-3">读取 index.js 并分析和收集依赖是在哪个阶段？</h1>
<p>make - finishMake 阶段</p>
<h1 data-id="heading-4">make - finishMake 之间，做了什么</h1>
<ul>
<li>搜索 make.tap，发现很多地方监听了 make 事件</li>
<li>凭借我们的直觉，我们直接打开 EntryPlugin</li>
<li>EntryPlugin 的 addEntry 函数就是 make 阶段最重要的事情之一</li>
</ul>
<h1 data-id="heading-5">factory.create 中的 factory 是什么东西？</h1>
<blockquote>
<p>这个 factory 是哪里来的？</p>
</blockquote>
<p>是从 factorizeModule(options 的 options.factory 来的。</p>
<blockquote>
<p>这个 options.factory 是哪里来的？</p>
</blockquote>
<p>是从 moduleFactory 来的。</p>
<blockquote>
<p>moduleFactory 哪里来的？</p>
</blockquote>
<p>是用 this.dependencyFactories.get(Dep) 得到的。</p>
<blockquote>
<p>this.dependencyFactories.get(Dep) 是个啥？</p>
</blockquote>
<p>你搜 compilation.tap 就知道，它是 normalModuleFactory，简称 nmf</p>
<blockquote>
<p>老师，你 TM 怎么知道要搜这个？</p>
</blockquote>
<p>我把所有钩子都搜了，搜了半个小时，能不知道吗？</p>
<p>结论：factory 就是 nmf，所以 factory.create 就是 nmf.craete</p>
<h1 data-id="heading-6">nmf.create 做了什么？</h1>
<ul>
<li>nmf.create 得到了一个 module 对象</li>
<li>后续操作是 addModule 和 buildModule</li>
</ul>
<h1 data-id="heading-7">addModule 做了什么？</h1>
<ul>
<li>跟前面课程的思路类似，把 module 添加到 compilation.modules 里</li>
<li>而且还通过检查 id 防止重复添加</li>
</ul>
<h1 data-id="heading-8">buildModule 做了什么？</h1>
<ul>
<li>看名字就知道是重要操作，它调用了 module.build()</li>
<li>来到 NormalModule.js 看 build 源码，发现了 runLoaders</li>
<li>然后来到 processResult()，发现了 _source = ... 和 _ast = null</li>
<li>这是要做什么？显然是要把 _source 变成 _ast 了！</li>
<li>来到 doBuild 的回调，发现了 this.parser.parse() ！</li>
<li>parse 就是把 code 变成 ast</li>
<li>问题来了，parser 是什么，parse() 的源码在哪？</li>
<li>继续跟代码会发现 parser 来自于 acorn 库，需要编译原理知识，不跟进了</li>
<li>如果你想要学习编译原理知识，可以购买我的科班课程</li>
</ul>
<h1 data-id="heading-9">Webpack 如何知道 index.js 依赖了哪些文件</h1>
<ul>
<li>blockPreWalkStatement() 对 ImportDeclaration 进行了检查</li>
<li>一旦发现 import 'xxx'，就会触发钩子，对应的监听函数会处理依赖</li>
<li>其中 walkStatements() 对 ImportExpression 进行了检查</li>
<li>一旦发现 import('xxx')，就会触发钩子，对应的监听函数也会处理依赖</li>
<li>这里不讨论 require，大家有兴趣可以自己研究</li>
</ul>
<h1 data-id="heading-10">Webpack 是怎么把 modules 合并成一个文件的？</h1>
<ul>
<li>看 compilation.seal()，该函数会创建 chunks、 为每个 chunk 进行 codeGeneration，然后为每个 chunk 创建 asset</li>
<li>seal() 之后，emitAssets()、emitFiles() 会创建文件（emit 就是射）</li>
<li>最终得到 dist/main.js 和其他 chunk 文件</li>
</ul>
<hr>
<p>今年，我将研读更多前端项目源码并做成新的视频课程，敬请期待。</p>
<p>如果有什么开源项目的源码是你想了解的，欢迎留言。</p>
<p>完。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            