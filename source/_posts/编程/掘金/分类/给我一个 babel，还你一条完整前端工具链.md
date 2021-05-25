
---
title: '给我一个 babel，还你一条完整前端工具链'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e54afca544cb442d96640a0a519aab4d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 24 May 2021 04:16:36 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e54afca544cb442d96640a0a519aab4d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">你不知道的 babel</h2>
<p>提到 babel，你会想到什么？</p>
<ul>
<li>可以把项目中的 es6、es7 等代码转成目标环境支持的代码</li>
<li>可以自动 polyfill 目标环境不支持的 api</li>
<li>taro （小程序转译工具）是基于 babel 实现的</li>
<li>babel 的插件很丰富</li>
<li>我们公司现在用 babel 来编译 typescript，不用 tsc 了</li>
<li>我基于 babel 做过自动埋点的功能，得到了领导的夸奖</li>
<li>...</li>
</ul>
<p>其实 babel 能做的不只是这些，它能做 3 类事情：</p>
<h3 data-id="heading-1">转译 esnext、typescript、flow 等到目标环境支持的 js</h3>
<p>这个是最常用的功能，用来把代码中的 esnext 的新的语法、typescript 和 flow 的语法转成基于目标环境支持的语法的实现。并且还可以把目标环境不支持的 api 进行 polyfill。</p>
<p>babel7 支持了 preset-env，可以指定 targets 来进行按需转换，转换更加的精准，产物更小。</p>
<h3 data-id="heading-2">一些特定用途的代码转换</h3>
<p>babel 是一个转译器，暴露了很多 api，用这些 api 可以完成代码到 AST 的 parse，AST 的转换，以及目标代码的生成。</p>
<p>开发者可以用它来来完成一些特定用途的转换，比如函数插桩（函数中自动插入一些代码，例如埋点代码）、自动国际化、default import 转 named import 等。</p>
<p>现在比较流行的小程序转译工具 taro，就是基于 babel 的 api 来实现的。</p>
<h3 data-id="heading-3">代码的静态分析</h3>
<p>对代码进行 parse 之后，能够进行转换，是因为通过 AST 的结构能够理解代码。理解了代码之后，除了进行转换然后生成目标代码之外，也同样可以用于分析代码的信息，进行一些检查。</p>
<h4 data-id="heading-4">babel 还能做什么？</h4>
<p>babel 是前端业务开发和工具链开发中必不可少的工具，我们每天都在用，可是你有想过这些问题么：</p>
<ul>
<li>怎么写一个 babel 插件来做自定义的代码转换？</li>
<li>业务开发中有哪些地方可以用 babel 来做自动化？</li>
<li>babel 是怎么实现的？</li>
</ul>
<p>还有</p>
<ul>
<li>linter 是怎么实现的？</li>
<li>typescript 类型检查是怎么实现的？</li>
<li>压缩混淆工具的原理是什么？</li>
<li>打包工具是如何分析代码依赖关系的？</li>
<li>api 文档如何自动生成？</li>
</ul>
<p>上面这些都可以用 babel 来实现，或许你并没有想过 babel 有这么大的能量，<strong>学会了 babel，绝对能让你提升一个段位</strong>。</p>
<h2 data-id="heading-5">基于 babel 实现完整工具链</h2>
<p>我们来理一下这些工具的实现思路（所有下面列的工具都有<a href="https://github.com/QuarkGluonPlasma/babel-plugin-exercize" target="_blank" rel="nofollow noopener noreferrer">实现代码</a>放在 github）</p>
<h3 data-id="heading-6">自动国际化</h3>
<p>国际化是把写死的字符串字面量换成从资源包取值的方式，babel 可以分析出代码中的字符串字面量，把它替换成一个函数调用语句，然后自动引入资源包。基于 babel，我们完全可以做到自动国际化。</p>
<h3 data-id="heading-7">自动生成 api 文档</h3>
<p>我们在写 api 的时候，会在上方添加注释，那么是不是能把这些注释内容还有关联的函数、class 的信息提取出来，用一定的模版来生成 api 文档呢？ 没错，babel 可以做到。</p>
<h3 data-id="heading-8">linter</h3>
<p>我们整天用 eslint、stylelint 来做代码规范的检查，其实他们不过就是对 AST 做了校验，这些我们用 babel 完全可以做到。可以基于 babel 实现 eslint。</p>
<h3 data-id="heading-9">type checker</h3>
<p>typescript 是给代码添加了静态的类型信息，可以在编译期间进行类型检查，也可以辅助做代码的智能提示，现在基本是前端必备技能了。可是你有想过 typescript 怎么实现的么？在小册中<strong>我们会手写一个 ts type checker，让你真正理解 typescript！</strong></p>
<h3 data-id="heading-10">压缩混淆</h3>
<p>前端代码上生产肯定要做压缩，做混淆，这个我们整天都在用，可是你知道他的实现原理么，我们能不能用 babel 来实现一下。答案是肯定的，在<a href="https://sourl.co/ijmTn3" target="_blank" rel="nofollow noopener noreferrer">小册</a>中<strong>我们会实现压缩混淆的功能</strong>。</p>
<h3 data-id="heading-11">js 解释器</h3>
<p>v8 引擎的实现原理是什么，解释型语言都是怎么解释代码的。我们能不能实现一个 js 解释器，是可以的，<a href="https://sourl.co/ijmTn3" target="_blank" rel="nofollow noopener noreferrer">《babel 插件通关秘籍》</a>小册中我们会基于 babel parser 实现一个 js 解释器。</p>
<h2 data-id="heading-12">手写 babel</h2>
<p>可能你会问，上面的这些都是基于 babel，那如果没有 babel 呢？</p>
<p>没有 babel 我们就实现一个 babel，<a href="https://sourl.co/ijmTn3" target="_blank" rel="nofollow noopener noreferrer">小册</a>最后<strong>我们会实现一个简易但可用的 babel，让你真正理解 babel 的原理，真正掌握 babel</strong>。</p>
<p>上面的解释器和类型检查的内容，<a href="https://www.yinwang.org/blog-cn/2021/02/15/cs3?utm_source=wechat_session&utm_medium=social&utm_oi=861330616749281280" target="_blank" rel="nofollow noopener noreferrer">王垠卖 12000</a>，见下图，所以这本小册绝对超值。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e54afca544cb442d96640a0a519aab4d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/191ae08bb75c407984abe95243004b59~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">大纲</h2>
<p>上面说了很多小册的内容，下面是小册的完整目录：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56d6c82fc259474aa210592a7ba15a79~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">不只是 babel</h2>
<p>虽然上面的实战都是基于 babel 的，可是你学到的只是 babel 么？</p>
<p>不是的，上面的实战案例涉及到完整的工具链，从文档生成、lint、type check、压缩混淆到 js 解释器等等，这几乎是前端开发的闭环了。<strong>以此为抓手，学到的是整条工具链的实现思路</strong>。</p>
<p>上面的工具还是集中在前端领域，但其中转译器、解释器的实现思路确是通用的，编译原理主要就是学编译器、转译器、解释器三部分，<strong>学完整本小册，相信也能帮助你入门编译原理</strong>。</p>
<h2 data-id="heading-15">总结</h2>
<p>babel 是前端领域几乎是必备的工具，基于它可以完成很多功能，甚至是打造整条工具链，我们在<a href="https://sourl.co/ijmTn3" target="_blank" rel="nofollow noopener noreferrer">小册</a>中会实现 linter、type cheker、压缩混淆、api 文档自动生成、js 解释器等等一系列功能。其中解释器和类型检查的功能在王垠那里能卖 12000，对比之下，这本小册内容和价格绝对很良心了。</p>
<p>如果说 babel api 是术，那么基于 babel 学到的编译原理、工具链实现思路就是道了。掌握了 babel、掌握了工具链，入门编译原理，绝对能让你提升一个段位。</p></div>  
</div>
            