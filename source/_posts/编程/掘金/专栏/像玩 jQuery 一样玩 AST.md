
---
title: '像玩 jQuery 一样玩 AST'
categories: 
    - 编程
    - 掘金
    - 专栏

author: 掘金
comments: false
date: Sun, 31 Jan 2021 06:50:16 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0efd039239b4d668c8f1b7402153294~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文来自飞猪前端的 @呦嘿 同学，萌妹子手把手教你使用 AST，这篇文章写得很不错值得一读。</p>
</blockquote>
<blockquote>
<p>这篇文章适合在原理性知识不通的情况下，仍然对ast蠢蠢欲动的开发者们，文章不具备任何专业性以及严谨性，它除了实用，可能一无是处。</p>
</blockquote>
<p>关于AST的介绍，网上已经一大堆了，不仅生涩难懂，还自带一秒劝退属性。其实我们可以很（hao）接（bu）地（yan）气（jin）的去了解一个看上去高端大气的东西，比如，AST是一个将代码解构成一棵可以千变万化的树的黑魔法。所以，只要我们知道咒语怎么念，世界的大门就打开了。有趣的是，魔法咒语长得像jQuery～</p>
<h2 data-id="heading-0">欢迎你，魔法师</h2>
<p>在成为一名魔法师之前，我们需要准备四样东西：<strong>趁手的工具、<strong>又简短又常用的</strong>使用技巧</strong>，即使看不懂也不影响使用的<strong>权威api</strong>、 以及天马行空的<strong>想象力。</strong></p>
<h3 data-id="heading-1">🍭 魔法棒 之 趁手的工具</h3>
<h4 data-id="heading-2">🔗 <a href="https://astexplorer.net/" target="_blank" rel="nofollow noopener noreferrer">AST exporer</a></h4>
<blockquote>
<p>这是一个ast在线调试工具，有了它，我们可以非常直观的看到ast生成前后以及代码转换，它分五个区域。我们接下来都依赖这个工具进行代码操作。</p>
</blockquote>
<p><img alt="20210119160723.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0efd039239b4d668c8f1b7402153294~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">🔗  <a href="https://github.com/facebook/jscodeshift" target="_blank" rel="nofollow noopener noreferrer">jscodeshift</a></h4>
<blockquote>
<p>它是一个ast转换器，我们通过它来将原始代码转译成ast语法树，并借用其开放的api操作ast，最终转换成我们想要的代码。</p>
</blockquote>
<p>jscodeshift的api基于recast封装，语法十分接近jquery。recast是对babel/travers & babel/types的封装，它提供简易的ast操作，而travers是babel中用于操作ast的工具，types我们可以粗浅的理解为字典，它用于描述结构树类型。</p>
<p>同时，jscodeshift还提供额外的功能，使得开发者们能够在项目工程阶段、亦或开发阶段皆可投入使用，同时无需感知babel转译前后的过程，只专注于如何操作或改变树，并得到结果。</p>
<p>尽管jscodeshift缺少中文文档，但其源码可读性非常高，这也是为什么推荐使用jscodeshift的重要原因之一。关于其api操作技巧，将在实践中为大家揭晓。</p>
<h3 data-id="heading-4">📖 魔法书 之 权威api</h3>
<h4 data-id="heading-5">🔗 <a href="https://babeljs.io/docs/en/babel-types" target="_blank" rel="nofollow noopener noreferrer">babel-types</a></h4>
<blockquote>
<p>ast语法字典，方便我们快速查阅结构树的类型，它是我们想要通过ast生成某行代码时的重要工具之一。</p>
</blockquote>
<h2 data-id="heading-6">认识AST</h2>
<h3 data-id="heading-7">我以为的AST</h3>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbc7047f269044449c82fd830bcd3cc8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">实际中的AST</h3>
<p>假如我们有这样一份代码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们将其转化为AST，以JSON格式展示如下</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Program"</span>,
  <span class="hljs-attr">"sourceType"</span>: <span class="hljs-string">"script"</span>,
  <span class="hljs-attr">"body"</span>: [
    &#123;
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"VariableDeclaration"</span>,
      <span class="hljs-attr">"kind"</span>: <span class="hljs-string">"var"</span>,
      <span class="hljs-attr">"declarations"</span>: [
        &#123;
          <span class="hljs-attr">"type"</span>: <span class="hljs-string">"VariableDeclarator"</span>,
          <span class="hljs-attr">"id"</span>: &#123;
            <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
            <span class="hljs-attr">"name"</span>: <span class="hljs-string">"a"</span>
          &#125;,
          <span class="hljs-attr">"init"</span>: &#123;
            <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Literal"</span>,
            <span class="hljs-attr">"value"</span>: <span class="hljs-number">1</span>
          &#125;
        &#125;
      ]
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我操作对象init中value的值 1 改为 2 时，对应的js也会跟着改变为 var a = 2
当我操作对象id中的name的值a 改为 b 时， 对应的js也会跟着改变为 var b = 2</p>
<p>看到这里，突然发现，操作AST无非就是<strong>操作一组有规则的JSON</strong>，发现新大陆有木有？？
那么只要明白规则，是不是很快就可以掌握一个世界了有！木！有！</p>
<h3 data-id="heading-9">了解AST节点</h3>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0f48c22710843079edc87c7d29a3c8f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">探索AST节点类型</h3>
<p>常用节点含义对照表
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0870a372ff146a2b6298b25dedef1e2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
看了规则后瞬间明白ast的json中那些看不懂的type是个什么玩意了(详细可对照<a href="https://babeljs.io/docs/en/babel-types" target="_blank" rel="nofollow noopener noreferrer">babel-types</a>），真的就是描述语法的词汇罢了！
原来掌握一个世界竟然可以这么简！单！</p>
<h2 data-id="heading-11">jscodeshift 简易操作</h2>
<h3 data-id="heading-12">查找</h3>



































<table><thead><tr><th>api</th><th>类型</th><th>接收参数</th><th>描述</th></tr></thead><tbody><tr><td>find</td><td>fn</td><td>type： ast类型</td><td></td></tr><tr><td>找到所有符合筛选条件的ast类型的ast节点，并返回一个array。</td><td></td><td></td><td></td></tr><tr><td>filter</td><td>fn</td><td>callback：接受一个回调，默认传递被调用的ast节点</td><td>筛选指定条件的ast节点，并返回一个array</td></tr><tr><td>forEach</td><td>fn</td><td>callback：接受一个回调，默认传递被调用的ast节点</td><td>遍历ast节点，同js的forEach函数</td></tr></tbody></table>
<p>除此之外， 还有<strong>some、every、closest</strong>等用法基本一致。</p>
<h3 data-id="heading-13"></h3>
<h3 data-id="heading-14">删除</h3>























<table><thead><tr><th>api</th><th>类型</th><th>接收参数</th><th>描述</th></tr></thead><tbody><tr><td>remove</td><td>fn</td><td>type： ast类型</td><td></td></tr><tr><td>filter：筛选条件</td><td>找到所有符合筛选条件的ast类型的ast节点，并返回一个array。</td><td></td><td></td></tr></tbody></table>
<h3 data-id="heading-15"></h3>
<h3 data-id="heading-16">添加 & 修改</h3>



































<table><thead><tr><th>api</th><th>类型</th><th>接收参数</th><th>描述</th></tr></thead><tbody><tr><td>replaceWith</td><td>fn</td><td>nodes：ast节点</td><td>替换ast节点，如果为空则表示删除</td></tr><tr><td>insertBefore</td><td>fn</td><td>fn</td><td>nodes：ast节点</td></tr><tr><td>insertAfter</td><td>fn</td><td>fn</td><td>nodes：ast节点</td></tr><tr><td>toSource</td><td>fn</td><td>options: 配置项</td><td>ast节点转译，返回js</td></tr></tbody></table>
<p>除此之外， 还有<strong>some、every、closest</strong>等用法基本一致。</p>
<h3 data-id="heading-17"></h3>
<h3 data-id="heading-18">其它</h3>
<p>子节点相关操作如getAST()、nodes() 等。
指定ast节点的查找，如：findJSXElements()、hasAttributes()、hasChildren()等。</p>
<blockquote>
<p>更多可通过ast explore 在操作区console查看、或直接查看<a href="https://github.com/facebook/jscodeshift/tree/master/src/collections" target="_blank" rel="nofollow noopener noreferrer">jscodeshift/collections</a></p>
</blockquote>
<h3 data-id="heading-19"></h3>
<h3 data-id="heading-20">命令</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// -t 转换文件的文件路径 可以是本地或者url </span>
<span class="hljs-comment">// myTransforms ast执行文件</span>
<span class="hljs-comment">// fileA fileB 待操作的文件</span>
<span class="hljs-comment">// --params=options 用于执行文件接收的参数</span>
jscodeshift -t myTransforms fileA fileB --params=options
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多命令查看 🔗 <a href="https://github.com/facebook/jscodeshift" target="_blank" rel="nofollow noopener noreferrer">jscodeshift</a></p>
<h2 data-id="heading-21"></h2>
<h2 data-id="heading-22">实践</h2>
<blockquote>
<p>接下来，我将在实践中传递技巧。</p>
</blockquote>
<h3 data-id="heading-23">简单的例子</h3>
<p>我们先来看一个例子，假设有如下代码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> styles <span class="hljs-keyword">from</span> <span class="hljs-string">'./index.module.scss'</span>;
<span class="hljs-keyword">import</span> &#123; Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@alifd/next"</span>;


<span class="hljs-keyword">const</span> Button = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>转译前<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"normal"</span>></span>Normal<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>></span>Prirmary<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"secondary"</span>></span>Secondary<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
        

        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"normal"</span> <span class="hljs-attr">text</span>></span>Normal<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> <span class="hljs-attr">text</span>></span>Primary<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"secondary"</span> <span class="hljs-attr">text</span>></span>Secondary<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
        

        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"normal"</span> <span class="hljs-attr">warning</span>></span>Normal<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Button;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行文件（通过jscodeshift进行操作）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">file, api</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> j = api.jscodeshift;
    <span class="hljs-keyword">const</span> root = j(file.source);
    root
        .find(j.ImportDeclaration, &#123; <span class="hljs-attr">source</span>: &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">"@alifd/next"</span> &#125; &#125;)
        .forEach(<span class="hljs-function">(<span class="hljs-params">path</span>) =></span> &#123;
            path.node.source.value = <span class="hljs-string">"antd"</span>;
        &#125;)
    root
    .find(j.JSXElement, &#123;<span class="hljs-attr">openingElement</span>: &#123; <span class="hljs-attr">name</span>: &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'h2'</span> &#125; &#125;&#125;)
  .forEach(<span class="hljs-function">(<span class="hljs-params">path</span>) =></span> &#123;
        path.node.children = [j.jsxText(<span class="hljs-string">'转译后'</span>)]
        &#125;)
    root
        .find(j.JSXOpeningElement, &#123; <span class="hljs-attr">name</span>: &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Button'</span> &#125; &#125;)
        .find(j.JSXAttribute)
        .forEach(<span class="hljs-function">(<span class="hljs-params">path</span>) =></span> &#123;
            <span class="hljs-keyword">const</span> attr = path.node.name
            <span class="hljs-keyword">const</span> attrVal = ((path.node.value || &#123;&#125;).expression || &#123;&#125;).value ? path.node.value.expression : path.node.value

            <span class="hljs-keyword">if</span> (attr.name === <span class="hljs-string">"type"</span>) &#123;
                <span class="hljs-keyword">if</span> (attrVal.value === <span class="hljs-string">'normal'</span>) &#123;
                    attrVal.value = <span class="hljs-string">'default'</span>
                &#125;
            &#125;

            <span class="hljs-keyword">if</span> (attr.name === <span class="hljs-string">"size"</span>) &#123;
                <span class="hljs-keyword">if</span> (attrVal.value === <span class="hljs-string">'medium'</span>) &#123;
                    attrVal.value = <span class="hljs-string">'middle'</span>
                &#125;
            &#125;

            <span class="hljs-keyword">if</span> (attr.name === <span class="hljs-string">"warning"</span>) &#123;
                attr.name = <span class="hljs-string">'danger'</span>
            &#125;

            <span class="hljs-keyword">if</span> (attr.name === <span class="hljs-string">"text"</span>) &#123;
                <span class="hljs-keyword">const</span> attrType = path.parentPath.value.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.name.name === <span class="hljs-string">'type'</span>)
                attr.name = <span class="hljs-string">'type'</span>
                <span class="hljs-keyword">if</span> (attrType.length) &#123;
                    attrType[<span class="hljs-number">0</span>].value.value = <span class="hljs-string">'link'</span>
                    j(path).replaceWith(<span class="hljs-string">''</span>)
                &#125; <span class="hljs-keyword">else</span> &#123;
                    path.node.value = j.stringLiteral(<span class="hljs-string">'link'</span>)
                &#125;

            &#125;
        &#125;);

    <span class="hljs-keyword">return</span> root.toSource();
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>该例代码大致解读如下</p>
<ol>
<li>将js转换为ast</li>
<li>遍历代码中所有包含@alifd/next的引用模块，并做如下操作
<ol>
<li>改变该模块名为antd。</li>
</ol>
</li>
<li>找到代码中标签名为h2的代码块，并修改该标签内的文案。</li>
<li>遍历代码中所有Button标签，并做如下操作
<ol>
<li>改变标签中type和size属性的值</li>
<li>改变标签中text属性变为 type = "link"</li>
<li>改变标签中warning属性为danger</li>
</ol>
</li>
<li>返回由ast转换后的js。</li>
</ol>
<p>最终输出结果</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> styles <span class="hljs-keyword">from</span> <span class="hljs-string">'./index.module.scss'</span>;
<span class="hljs-keyword">import</span> &#123; Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"antd"</span>;


<span class="hljs-keyword">const</span> Button = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>转译后<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"default"</span>></span>Normal<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>></span>Prirmary<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"secondary"</span>></span>Secondary<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
        

        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"link"</span> ></span>Normal<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"link"</span> ></span>Primary<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"link"</span> ></span>Secondary<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
        

        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"default"</span> <span class="hljs-attr">danger</span>></span>Normal<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Button;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">逐句解读</h3>
<h4 data-id="heading-25">获取必要的数据</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 获取操作ast用的api，获取待编译的文件主体内容,并转换为AST结构。</span>
<span class="hljs-keyword">const</span> j = api.jscodeshift;
<span class="hljs-keyword">const</span> root = j(file.source);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行jscodeshift命令后，执行文件接收 <strong>3</strong> 个参数</p>
<h5 data-id="heading-26">file</h5>

















<table><thead><tr><th>属性</th><th>描述</th></tr></thead><tbody><tr><td>path</td><td>文件路径</td></tr><tr><td>source</td><td>待操作的文件主体，我们主要用到这个。</td></tr></tbody></table>
<h5 data-id="heading-27">api</h5>





















<table><thead><tr><th>属性</th><th>描述</th></tr></thead><tbody><tr><td>jscodeshift</td><td>对jscodeshift库的引用，我们主要用到这个。</td></tr><tr><td>stats</td><td> <code>--dry</code> 运行期间收集统计信息的功能</td></tr><tr><td>report</td><td>将传递的字符串打印到stdout</td></tr></tbody></table>
<h5 data-id="heading-28">options</h5>
<p>执行jscodeshift命令时，接收额外传入的参数，目前用不到，不做额外赘述。</p>
<h4 data-id="heading-29">代码转换</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// root: 被转换后的ast跟节点  </span>
root
<span class="hljs-comment">// ImportDeclaration 对应 import 句式</span>
  .find(j.ImportDeclaration, &#123; <span class="hljs-attr">source</span>: &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">"@alifd/next"</span> &#125; &#125;)
  .forEach(<span class="hljs-function">(<span class="hljs-params">path</span>) =></span> &#123;
  <span class="hljs-comment">// path.node 为import句式对应的ast节点</span>
  path.node.source.value = <span class="hljs-string">"antd"</span>;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解读：</p>
<ul>
<li>遍历代码中所有包含@alifd/next的引用模块，并做如下操作
<ol>
<li>改变该模块名为antd。</li>
</ol>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">root
<span class="hljs-comment">// JSXElement 对应 element 完整句式，如 <h2 ...> ... </h2></span>
<span class="hljs-comment">// openingElement 对应 element 的 开放标签句式， 如 <h2 ...></span>
  .find(j.JSXElement, &#123;<span class="hljs-attr">openingElement</span>: &#123; <span class="hljs-attr">name</span>: &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'h2'</span> &#125; &#125;&#125;)
  .forEach(<span class="hljs-function">(<span class="hljs-params">path</span>) =></span> &#123;
  <span class="hljs-comment">// jsxText 对应 text</span>
  path.node.children = [j.jsxText(<span class="hljs-string">'转译后'</span>)]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解读：</p>
<ul>
<li>筛选标签为h2的html，更改该标签的内容的text为“转译后”</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    root
    <span class="hljs-comment">// 筛选Button的 element开放句式</span>
        .find(j.JSXOpeningElement, &#123; <span class="hljs-attr">name</span>: &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Button'</span> &#125; &#125;)
<span class="hljs-comment">// JSXAttribute 对应 element 的 attribute 句式， 如 type="normal" ...</span>
        .find(j.JSXAttribute)
        .forEach(<span class="hljs-function">(<span class="hljs-params">path</span>) =></span> &#123;
            <span class="hljs-keyword">const</span> attr = path.node.name
            <span class="hljs-keyword">const</span> attrVal = ((path.node.value || &#123;&#125;).expression || &#123;&#125;).value ? path.node.value.expression : path.node.value

            <span class="hljs-keyword">if</span> (attr.name === <span class="hljs-string">"type"</span>) &#123;
                <span class="hljs-keyword">if</span> (attrVal.value === <span class="hljs-string">'normal'</span>) &#123;
                    attrVal.value = <span class="hljs-string">'default'</span>
                &#125;
            &#125;

            <span class="hljs-keyword">if</span> (attr.name === <span class="hljs-string">"size"</span>) &#123;
                <span class="hljs-keyword">if</span> (attrVal.value === <span class="hljs-string">'medium'</span>) &#123;
                    attrVal.value = <span class="hljs-string">'middle'</span>
                &#125;
            &#125;

            <span class="hljs-keyword">if</span> (attr.name === <span class="hljs-string">"warning"</span>) &#123;
                attr.name = <span class="hljs-string">'danger'</span>
            &#125;

            <span class="hljs-keyword">if</span> (attr.name === <span class="hljs-string">"text"</span>) &#123;
              <span class="hljs-comment">// 判断该ast节点的兄弟节点是否存在 type，</span>
                <span class="hljs-comment">// 如果有，则修改type的值为link，如果没有则改变当前节点为type=“link”</span>
                <span class="hljs-keyword">const</span> attrType = path.parentPath.value.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.name.name === <span class="hljs-string">'type'</span>)
                attr.name = <span class="hljs-string">'type'</span>
                <span class="hljs-keyword">if</span> (attrType.length) &#123;
                    attrType[<span class="hljs-number">0</span>].value.value = <span class="hljs-string">'link'</span>
                    j(path).replaceWith(<span class="hljs-string">''</span>)
                &#125; <span class="hljs-keyword">else</span> &#123;
                  <span class="hljs-comment">// stringLiteral 对应 string类型字段值</span>
                    path.node.value = j.stringLiteral(<span class="hljs-string">'link'</span>)
                &#125;

            &#125;
        &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解读：</p>
<ul>
<li>遍历代码中所有Button标签，并做如下操作
<ol>
<li>改变标签中type和size属性的值</li>
<li>改变标签中text属性变为 type = "link"</li>
<li>改变标签中warning属性为danger</li>
</ol>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">return</span> root.toSource();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解读：</p>
<ul>
<li>返回由ast转换后的js。</li>
</ul>
<h4 data-id="heading-30"></h4>
<h4 data-id="heading-31">天马行空的想象力来自于“懒”</h4>
<p>假如我们想插入一大段代码，按照ast的写法就得使用大量的type生成大量的节点对象，如此繁琐，大可不必，万事总有暴力解决法 🌝。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> formRef = j(<span class="hljs-string">'const formRef = React.createRef();'</span>).nodes()[<span class="hljs-number">0</span>].program.body[<span class="hljs-number">0</span>]
path.insertAfter(formRef)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假如我们想句式转换，比如element的text句式转attr标签。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> getStringEle = <span class="hljs-function">(<span class="hljs-params">source</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(source)) &#123;
        <span class="hljs-keyword">let</span> arr = []
        source.forEach(<span class="hljs-function">(<span class="hljs-params">item, i, items</span>) =></span> &#123;
            <span class="hljs-keyword">if</span> (!item.replace(<span class="hljs-regexp">/\s+|\n/g</span>, <span class="hljs-string">''</span>).length && i!==<span class="hljs-number">0</span> && i!== (items.length - <span class="hljs-number">1</span> ))&#123;
                arr.push(<span class="hljs-string">'<></>'</span>)
            &#125;
            arr.push(item)
        &#125;)
        <span class="hljs-keyword">return</span> arr.join(<span class="hljs-string">''</span>)
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> source
    &#125;
&#125;

...
.find(j.JSXAttribute)
.forEach(<span class="hljs-function"><span class="hljs-params">path</span> =></span> &#123;
  <span class="hljs-keyword">const</span> attrVal = ((path.node.value || &#123;&#125;).expression || &#123;&#125;).value ? path.node.value.expression : path.node.value
<span class="hljs-keyword">const</span> childrenEleStr = getStringEle(j(path).toSource())
  
  j(path).replaceWith(j.jsxIdentifier(
    <span class="hljs-string">`attr=&#123;[<span class="hljs-subst">$&#123;childrenEleStr.replace(<span class="hljs-regexp">/<><\/>/g</span>, <span class="hljs-string">','</span>)&#125;</span>]&#125;`</span>
  ))
  
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>掌握更多的链式写法，就能玩出更多的花样～ 这点和jQuery如出一辙。</p>
<h3 data-id="heading-32"></h3>
<h3 data-id="heading-33">让文件结合工程run起来</h3>
<p>以上我们都基于ast exporer，并不能实用于项目场景，或者满足工程需要。
真实的工程化场景，并不满足于一份文件，如果想让ast工程化，真正的落实在项目中，利用ast重构业务代码，解放重复的劳动力，以下是一个很好的解决思路。</p>
<p>以下基于node，我推荐两个工具</p>
<h4 data-id="heading-34">npx & execa</h4>
<p>利用npx实现一个复杂命令，来创建一个简易cli。通过execa批量执行jscodeshift。</p>
<p>关键代码如下</p>
<h5 data-id="heading-35">package.json</h5>
<pre><code class="hljs language-json copyable" lang="json">  <span class="hljs-string">"bin"</span>: &#123;
    <span class="hljs-attr">"ast-cli"</span>: <span class="hljs-string">"bin/index.js"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-36">index.js</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">#! /usr/bin/env node</span>
<span class="hljs-built_in">require</span>(<span class="hljs-string">'./cli'</span>).main()
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-37">main()</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript">...

<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> execa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'execa'</span>);
<span class="hljs-keyword">const</span> jscodeshiftBin = <span class="hljs-built_in">require</span>.resolve(<span class="hljs-string">'.bin/jscodeshift'</span>);

<span class="hljs-built_in">module</span>.exports.main = <span class="hljs-keyword">async</span> () => &#123;
...
  <span class="hljs-keyword">const</span> astFilesPath = ...
  astFilesPath.forEach(<span class="hljs-keyword">async</span> (transferPath, i) => &#123;
    <span class="hljs-keyword">const</span> outdrr = <span class="hljs-keyword">await</span> execa.sync(jscodeshiftBin, [<span class="hljs-string">'-t'</span>, transferPath, src])
    <span class="hljs-keyword">if</span> (outdrr.failed) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`编译出错： <span class="hljs-subst">$&#123;outdrr&#125;</span>`</span>)
    &#125;
  &#125;)
  ...
&#125;

...

<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            