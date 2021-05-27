
---
title: '90%的人都不知道的Node.js 依赖关系管理（上）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0431009806f486c982002ab4cbe9b18~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 26 May 2021 19:37:06 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0431009806f486c982002ab4cbe9b18~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>转载请注明出处：葡萄城官网，葡萄城为开发者提供专业的开发工具、解决方案和服务，赋能开发者。</p>
</blockquote>
<h1 data-id="heading-0">引言</h1>
<p>Node.js中的一个重要概念是依赖关系管理。本文就将带大家了解依赖管理的各种模式以及Node.js如何加载依赖。
Node.js编写模块化代码非常简单，我们可以使用单个js文件非模块化的编写所有应用程序的内容。
在这里你可能会问，模块（module）是什么，它又有什么作用。
大型项目的实施之中，会有很多分工协作，为了可以让分工更加方便和顺利，我们可以将编写好的代码封装起来，重复使用或者提供给第三方使用。在项目封装阶段将所有模块组织编译成一个完整程序。
总而言之，模块是代码为了便于在开发中共享和重用，而进行的分组。这些模块使我们可以将复杂的应用程序分解。以便让我们更好地理解代码，发现并修复Bug。基于CommonJS，Node.js中使用require这个关键字来获取一个JavaScript文件。</p>
<h1 data-id="heading-1">开始</h1>
<p>我们给项目创建一个目录，用npm init 进行初始化，创建了app.js和appMsg.js两个JavaScript文件。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0431009806f486c982002ab4cbe9b18~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer">
此时两个.js文件都是空的，我们来继续更新appMsgs.js文件</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd2805a76d9046bf9895ef746ada80b8~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此处可以看到module.exports的用法，该方法公开给定文件（appMsgs.js）中的属性或对象，这些属性或对象可以在另一个文件中使用。本例中该文件是app.js
在这个系统中每个文件都可以访问module.exports，所以appMsgs.js文件中的一些项就被公开了，下面是具体使用这些内容的展示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6aff3aa321e2486eaaf4bb9e2160fdcc~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用require关键字引用文件，使用的时候它将返回一个表示模块化代码段的对象。我们将其分配给变量appMsgs variable，然后在console.log语句中使用属性。得到以下输出：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42973e7e3d8340bc9749dbeb7da32125~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer">
执行JavaScript，构造一个返回对象。这个对象可以是一个类构造函数，也可以是一个包含许多元素或一些简单属性的对象。
因此，通过管理require和module.exports，我们可以创建这些模块化应用程序。
所需的功能加载代码并只加载一次。如果其他人通过require请求这个对象，只会得到这个对象的缓存版本。</p>
<p>接下来看看其他方法</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/035375a3c47c4d8e96d9a441df6db0d0~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对代码进行修改，不再公开一个对象，而是导出整个函数。每次函数调用都会执行此代码
下面是它如何在app.js文件中使用</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/037ad094335e4b8da85abbfd428c958a~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不需要调用属性，只需要像执行函数一样。与函数执行不同的是每次执行这个代码，函数中的代码都会被重新执行
下面是运行结果</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1ca447e37064d69a770dabb0d161c28~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上是module.exports的两种模式及其差异，另一个常见模式中我们需要知道如何使用它作为构造函数</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/beae9860863f49789002058226864a06~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面是更新后的app.js文件</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee567f593782479d893cc91070db133f~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本质上来说这样与在JavaScript中创建伪类并允许创建伪类的实例时是一样的，下面是更改之后的输出</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6daade274ea946edb998c7b1da2afd96~tplv-k3u1fbpfcp-watermark.image" alt="10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以下是该模式的另一个例子
我们创建一个名为userRepo.js的新文件</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/985051ad0bec4c5e96d31639ed3c9b51~tplv-k3u1fbpfcp-watermark.image" alt="11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面是app.js和此更改的执行结果</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68c894e476ad461382154c6eedcbde2f~tplv-k3u1fbpfcp-watermark.image" alt="12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/255920a29378489f8e4cf4a08fc34a14~tplv-k3u1fbpfcp-watermark.image" alt="13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>单个文件使用require很常见，但别忘了另一种模式：文件夹的之间的依赖关系</p>
<h1 data-id="heading-2">文件夹相关性</h1>
<p>在正式介绍文件夹相关性之前，我们先来了解Nodejs如何查找依赖项，不要忽略前面例子中的这一内容：</p>
<pre><code class="copyable">var appMsgs = require("./appMsgs")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Node.js会查找appMsgs.js文件，也会将appMsgs作为目录查找，无论它首先找到哪个都会进行记录。
接着我们创建一个名为logger的文件夹，在该文件夹中创建一个index.js文件</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e71e3a303124e6da791468eca286e83~tplv-k3u1fbpfcp-watermark.image" alt="14.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>app.js文件，它用require调用这个模块</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41439e3ed4b0427f8de560ccdd13aace~tplv-k3u1fbpfcp-watermark.image" alt="15.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在这个例子中值得注意的是：</p>
<pre><code class="copyable">var logger = require("./logger/index.js")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该内容完全正确，但如果改成一下内容：</p>
<pre><code class="copyable">var logger = require("./logger")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为项目中没有logger.js，所以在有一个logger目录时，默认情况下会加载index.js作为logger的起点。这就是我们命名index.js的原因，这段代码的结果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/485ba3681a2949cc862c7cb543144574~tplv-k3u1fbpfcp-watermark.image" alt="16.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看到这里，你可能会疑惑为什么还要费心去完成创建文件夹和inex.js的额外步骤呢？
原因是，我们可能正在组合一个复杂的依赖项，这个依赖项可能还有其他依赖项。而记录器的调用者不需要知道还有很多其他依赖项存在。
这是一种封装形式，当我们构建更复杂的内容时，我们可以用多个文件构建它们，而在用户端使用单个文件。文件夹是一种管理这些依赖关系的好方法。</p>
<h1 data-id="heading-3">Node Package Manager (NPM)</h1>
<p>再次要介绍的另一个内容是NPM，你一定了解它的功能，带来了很多便利。使用的方法也很简单。
我们可以使用npm安装依赖项</p>
<p><code>npm install underscore;</code></p>
<p>然后可以在app.js中简单地require</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8dfaa11fd13a4da1b35074fcedc6dd41~tplv-k3u1fbpfcp-watermark.image" alt="17.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以看到标红位置如何使用下划线包提供的功能。除此之外，当我们需要使用这个模块时，并不指定文件路径，只需要使用它的名称，Node.js将从应用程序中的node\u modules文件夹加载这个模块</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d102f88a8ab4d688d7e24b0366b8fdf~tplv-k3u1fbpfcp-watermark.image" alt="18.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面是它的输出</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15af770418e24a15a841ad4562d132e3~tplv-k3u1fbpfcp-watermark.image" alt="19.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">总结</h1>
<p>本文介绍了Nodejs如何管理它的依赖关系，并且在我们的应用程序中看到了一些可以使用的模式。希望可以对各位的开发学习带来帮助。</p>
<h1 data-id="heading-5">拓展阅读</h1>
<p>如果您已经对Node.js的内容很熟悉，还可以了解<a href="https://www.grapecity.com.cn/blogs/spread-table-performance-optimization-practice" target="_blank" rel="nofollow noopener noreferrer">web系统中对表格性能进行优化</a>。</p></div>  
</div>
            