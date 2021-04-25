
---
title: '学习--初识AST'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ee2a1df88fc44a29341c5a5014a9dc0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 24 Apr 2021 22:23:13 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ee2a1df88fc44a29341c5a5014a9dc0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">探索AST</h2>
<h3 data-id="heading-1">AST是什么？</h3>
<p>AST全称是Abstract Syntax Tree，翻译过来是抽象语法树的意思。</p>
<blockquote>
<p>AST是<strong>源代码</strong>语法结构的一种<strong>抽象</strong>表示。它以树状的形式表现编程语言的语法结构，树上的每个节点都表示源代码中的一种结构。 <a href="https://www.hk.wiiaa.top/baike-%E6%8A%BD%E8%B1%A1%E8%AA%9E%E6%B3%95%E6%A8%B9" target="_blank" rel="nofollow noopener noreferrer">AST维基百科</a></p>
</blockquote>
<h3 data-id="heading-2">AST结构是什么样的？</h3>
<p>从上面的解释中我们知道了AST是从源代码中分析出来的，那么我们现在可以以一小段代码为例子，看一下AST结构是什么样子的，我们可以打开这个网站 <a href="https://astexplorer.net/" target="_blank" rel="nofollow noopener noreferrer">AST在线预览</a> ，来帮助我们查看一下这段代码具体的AST结构。这里选择了@babel/parser对代码进行了解析。</p>
<h4 data-id="heading-3">🌰栗子：简单的console.log</h4>
<p><code>console.log('hello world');</code></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ee2a1df88fc44a29341c5a5014a9dc0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">🌰分析：console.log的AST</h4>
<p>我们可以看到，console.log解析出来的AST其实是一个对象，我们把这个对象一层层展开后，神奇地在
<code>body -> ExpressionStatement -> expression -> callee</code>
里面发现了object（console）和property（log）这两个属性节点。
简单树图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/593828cae97747dbb9cbe4bf57d4627a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个对象上还包含了其他很多的属性，其他属性的意思也可以参照下 <a href="https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/Parser_API#Node_objects" target="_blank" rel="nofollow noopener noreferrer">AST对象文档</a> 上的解释。</p>
<h3 data-id="heading-5">AST能做什么？</h3>
<p>那如果AST是对象的话，是不是可以通过对象解构的形式把console和log提取出来呢？那既然都可以获取到节点了，是不是也可以给源码加上一些其他操作？
<strong>所以可以利用AST来写一个webpack loader或plugin来对源代码做一些预处理。</strong></p>
<p>常见的AST场景就比如通过bable对代码进行转换遍历，<code>删除代码中未被使用过的变量</code>，<code>删除console.log</code>，<code>antd的组件按需加载(babel-plugin-import)</code>，<code>语法高亮</code>等等，实际这背后都是是在对JavaScript的抽象语法树进行遍历操作，再返回操作后生成的新的AST树。</p>
<h2 data-id="heading-6">补充：源代码执行过程</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75234512ad284f9aa035d117408a7e57~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">词法分析（token）</h3>
<p>因为JS引擎执行代码是从上到下，从左往右扫码执行代码的，<strong>编译的第一个阶段是扫描源代码文本，scanner会从左到右扫描文本，把文本拆成一些单词</strong>。然后，这些单词传入分词器，经过一系列的识别器（关键字识别器、标识符识别器、常量识别器、操作符识别器等），确定这些单词的词性，这一过程的产物是token序列。token序列用<type, value>来表示，type表示一个单词种类，value为属性值。</p>
<p><a href="https://esprima.org/demo/parse.html#" target="_blank" rel="nofollow noopener noreferrer">词法分析预览</a></p>
<p>console.log('hello world')的词法分析token如下：<br></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab16106fd28a4cbd82eb9a7f2881fbb5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">语法分析（AST）</h3>
<p>语法分析个人理解就是在收集了词法分析的基础上，对JS的文法规则<code>(rules of grammar)</code>输出AST抽象解析树，《<a href="https://developer.mozilla.org/zh-CN/docs/Mozilla/Projects/SpiderMonkey/Parser_API" target="_blank" rel="nofollow noopener noreferrer">语法命名规则参考</a>》，
另外这棵树是可以任意遍历和增删改查的，因为这棵树是生成在编译成计算机识别的代码之前的。</p>
<h2 data-id="heading-9">总结</h2>
<p>现在对源代码的解析到运行有了一些基本理解，那么我们可以尝试着写一个简单的webpack loader或plugin实践下，理解源码的执行或直接对其中做一些特定的干预过程：</p>
<p><code>parser（解析） -> traverse（遍历/增删改查） -> generate（生成） </code></p></div>  
</div>
            