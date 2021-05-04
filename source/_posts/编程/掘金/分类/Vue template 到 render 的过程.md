
---
title: 'Vue template 到 render 的过程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2355'
author: 掘金
comments: false
date: Mon, 03 May 2021 03:32:50 GMT
thumbnail: 'https://picsum.photos/400/300?random=2355'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">过程分析</h2>
<p>Vue的模版编译过程主要如下：<code>template->ast->render函数</code>。</p>
<p>Vue在模版编译中会执行<code>compileToFunctions</code>将<code>template</code>转化为<code>render函数</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 将模版编译为render函数</span>
<span class="hljs-keyword">const</span> &#123; render, staticRenderFns &#125; = compileToFunctions(template, options, <span class="hljs-built_in">this</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">1.调用parse方法将template转化为ast（抽象语法树）</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ast = parse(template.trim(), options)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>parse的目标：</code>是把template转化为AST，它是一种用JavaScript对象形式来描述整个模版的语法结构。</p>
<p><code>解析过程：</code>利用正则表达式来解析模版，当解析到开始标签、闭合标签、文本的时候都会分别执行对应的回调函数，来达到构造AST树的目的。</p>
<p>AST元素节点总共三种类型：type为1表示普通元素、2为表达式、3为纯文本。</p>
<h3 data-id="heading-2">2.对静态节点做优化</h3>
<pre><code class="hljs language-js copyable" lang="js">optimize(ast, options)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个过程主要分析出哪些是静态节点，给其打一个标记，为后续更新渲染可以直接跳过静态节点做优化。</p>
<p><code>深度遍历AST：</code>查看每个子树的节点元素是否为静态节点或者静态节点根。如果为静态节点，他们生成的DOM永远不会改变，这对运行时的模版更新起到了极大的优化作用。</p>
<h3 data-id="heading-3">3.生成代码</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> code = generate(ast, options)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>generate将ast抽象语法树编译成<code>render字符串</code>并将静态部分放到<code>staticRenderFns</code>中，最后通过<code>new Function(render)</code>生成render函数。</p></div>  
</div>
            