
---
title: 'webpack深入开发之--Loader'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91aa3f65b9c34f32b77b48b49829d5bb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 02:26:31 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91aa3f65b9c34f32b77b48b49829d5bb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. loader 开发场景</h2>
<p>当在项目中需要对我们的文件进行处理，但是现有loader无法满足要求的时候， 那么自己开发一个loader，就显得比较重要了。比如，我们在开发组件库中，要想使用markdown组成网站的一个个功能介绍页面。在我们的markdown文件中，需要新创建一个自定义标签，用于国际化，比如必须使用一个<code><chn></code>标签, 但这个标签，实际上现有的markdown loader是不支持的， 那么就需要新加一个loader，来进行标签的解析。</p>
<h2 data-id="heading-1">2. 本文的讨论深度</h2>
<p>本文并不是介绍webpack loader的源码实现， 重点放在我们怎么开发一个可正常运行的loader。 所以下面开始对loader进行一些分析。</p>
<h2 data-id="heading-2">3. webpack中loader的分类</h2>
<p>在webpack的loader中，其实是分为这几类的：</p>
<ul>
<li>pre 前置, 会优先执行</li>
<li>post 后置， 会最后执行</li>
<li>normal 普通</li>
<li>inline 行内</li>
</ul>
<p>涉及的是loader的执行顺序。 比如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.less$/</span>,
        use: <span class="hljs-string">'style-loader'</span>
      &#125;,
     &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.less$/</span>,
        use: <span class="hljs-string">'css-loader'</span>
      &#125;,
     &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.less$/</span>,
        use: <span class="hljs-string">'less-loader'</span>
      &#125;
    ]
  &#125;,

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是我们经常会用的loader， 它的执行顺序其实是<code>自下往上</code>(或者说从右向左)。 所以执行的顺序是:</p>
<blockquote>
<p>less-loader -> css-loader -> style-loader</p>
</blockquote>
<p>如果我们设置 <code>enforce</code>, 则会明确自定义的执行顺序， 比如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.less$/</span>,
        use: <span class="hljs-string">'less-loader'</span>,
        <span class="hljs-attr">enforce</span>: <span class="hljs-string">'pre'</span>
      &#125;,
     &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.less$/</span>,
        use: <span class="hljs-string">'css-loader'</span>
      &#125;,
     &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.less$/</span>,
        use: <span class="hljs-string">'style-loader'</span>,
        <span class="hljs-attr">enforce</span>: <span class="hljs-string">'post'</span>
      &#125;
    ]
  &#125;,

<span class="copy-code-btn">复制代码</span></code></pre>
<p>像上面这种写法，则手动确定执行顺序：</p>
<blockquote>
<p>less-loader -> css-loader -> style-loader</p>
</blockquote>
<p><strong><code>normal</code> 是我们正常在rules中引用loader</strong></p>
<p>而 <code>inline</code> 是另外一种写法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> style-loader!css-loader!stylus-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然目前大家用inline的场景有限，因为很多时候对loader要传入各种参数。</p>
<p>好， 基础用法和不常用的<code>enforce</code>讲完， 下面，拿<code>normal</code>出来，进行重点讲解</p>
<h2 data-id="heading-3">4. Normal Loader 和 Pitching Loader</h2>
<h3 data-id="heading-4">4.1 Loader的执行总结构</h3>
<p>Loader的总体结构是将一个函数 exports出去，供webpack的 <code>runtime(我自己抽象的)</code>使用。</p>
<h3 data-id="heading-5">4.2 Normal Loader的开发方式和执行</h3>
<p>先把最基础的展示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// vue-pre-loader.js</span>

<span class="hljs-keyword">const</span> vuePreLoader = <span class="hljs-function">(<span class="hljs-params">content, map, meta</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'vue PreLoader获取的'</span>)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'vue PreLoader逻辑执行'</span>);
    <span class="hljs-keyword">return</span> content;
&#125;
<span class="hljs-built_in">module</span>.exports = vuePreLoader;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在webpack中的使用：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123;resolve&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-comment">// ....</span>
rules: [
    &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.vue$/</span>,
        use: [
                &#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">'vue-loader'</span>
                &#125;,
                &#123;
                    <span class="hljs-attr">loader</span>: resolve(__dirname, <span class="hljs-string">'./loader/vue-pre-loader.js'</span>)
                &#125;
        ]
    &#125;,
]

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在编译<code>.vue</code>文件的时候, 就会先执行我们自己写的loader， 而且会把<code>content</code>打印出来。 这个content是字符串，我们可以对数据进行二次处理。</p>
<p>好了，现在我们再开发一个loader, 用于 vue-loader执行后。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// vue-after-loader.js</span>

<span class="hljs-keyword">const</span> vueAfterLoader = <span class="hljs-function">(<span class="hljs-params">content, map, meta</span>) =></span> &#123;
    <span class="hljs-comment">// 比如可以把content中的html注释部分给删除掉</span>
    <span class="hljs-keyword">const</span> regExp = <span class="hljs-regexp">/<!--((\s|\r|\n)*((?!-->).)*\s|\r|\n)*-->/</span>;
    <span class="hljs-keyword">if</span>(regExp.test(content)) &#123;
        content = content.replace(content.match(regExp)[<span class="hljs-number">0</span>], <span class="hljs-string">''</span>);
    &#125;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'vueAfterLoader 逻辑执行'</span>);
    <span class="hljs-keyword">return</span> content;
&#125;

<span class="hljs-built_in">module</span>.exports = vueAfterLoader;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样，更新webpack中的配置：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123;resolve&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-comment">// ....</span>
rules: [
    &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.vue$/</span>,
        use: [
                &#123;
                    <span class="hljs-attr">loader</span>: resolve(__dirname, <span class="hljs-string">'./loader/vue-after-loader.js'</span>)
                &#125;,
                &#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">'vue-loader'</span>
                &#125;,
                &#123;
                    <span class="hljs-attr">loader</span>: resolve(__dirname, <span class="hljs-string">'./loader/vue-pre-loader.js'</span>)
                &#125;
        ]
    &#125;,
]

<span class="copy-code-btn">复制代码</span></code></pre>
<p>重新执行的时候，注意以下两点：</p>
<ul>
<li>content 的内容可以进行处理，处理成我们想要的</li>
<li>执行顺序： 先执行vue-pre-loader, 再执行vue-arger-loader</li>
</ul>
<h3 data-id="heading-6">4.3 Pitching Loader是什么</h3>
<p>这个概念在我处理的很多项目中并没有用到， 所以，更需要研究一下。 经过研究发现，这个<code>pitching</code>其实是跟<code>熔断</code>相关的。</p>
<p>首先加上这个<code>pitch</code>试试</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// vue-pre-loader.js</span>

<span class="hljs-keyword">const</span> vuePreLoader = <span class="hljs-function">(<span class="hljs-params">content, map, meta</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'vue PreLoader逻辑执行'</span>);
    <span class="hljs-keyword">return</span> content;
&#125;
vuePreLoader.pitch = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">remainingRequest, precedingRequest, data</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行vuePreLoader pitching'</span>);
&#125;

<span class="hljs-built_in">module</span>.exports = vuePreLoader;


<span class="hljs-comment">// vue-after-loader.js</span>

<span class="hljs-keyword">const</span> vueAfterLoader = <span class="hljs-function">(<span class="hljs-params">content, map, meta</span>) =></span> &#123;
    <span class="hljs-comment">// 比如可以把content中的html注释部分给删除掉</span>
    <span class="hljs-keyword">const</span> regExp = <span class="hljs-regexp">/<!--((\s|\r|\n)*((?!-->).)*\s|\r|\n)*-->/</span>;
    <span class="hljs-keyword">if</span>(regExp.test(content)) &#123;
        content = content.replace(content.match(regExp)[<span class="hljs-number">0</span>], <span class="hljs-string">''</span>);
    &#125;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'vueAfterLoader 逻辑执行'</span>);
    <span class="hljs-keyword">return</span> content;
&#125;

vueAfterLoader.pitch = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">remainingRequest, precedingRequest, data</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行vueAfterLoader pitching'</span>);
&#125;

<span class="hljs-built_in">module</span>.exports = vueAfterLoader;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次执行， 我们会发现，执行顺序是这样的：</p>
<blockquote>
<p>执行vueAfterLoader pitching -> 执行vuePreLoader pitching -> vue PreLoader逻辑执行 -> vueAfterLoader 逻辑执行</p>
</blockquote>
<p><strong>也就是说: <code>pitch的执行是从前向后， pitch执行完毕后，再从后向前执行loader</code></strong></p>
<p>那么这个pitching 的应用是什么呢？一个重要功能就是前面说的<code>熔断</code>。 当pitch 返回非undefined, 那么就会阻断之前的进程。 比如， 我在vue-pre-loader.js 中做一个return操作</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">vuePreLoader.pitch = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">remainingRequest, precedingRequest, data</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行vuePreLoader pitching'</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-string">'熔断流程'</span>;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么再看执行结果：</p>
<blockquote>
<p>执行vueAfterLoader pitching -> 执行vuePreLoader pitching -> vueAfterLoader 逻辑执行</p>
</blockquote>
<p>看到了吧？ 它把后面的流程给熔断了， 所以 <code>vue PreLoader逻辑执行</code>这个逻辑就没有执行，就返回到了 vue-after-loader</p>
<p>整体流程是这样的：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91aa3f65b9c34f32b77b48b49829d5bb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>画的不是很好，但是尽量体现他们之间的关系。希望对大家有那么一点点启发。</p>
<p>上面是今天我要表达的全部内容， 在分享给大家的同时，自己对其中的一些原理也有了更深一些的认识， 希望对大家有用。喜欢的话别忘了点个赞喔~~</p></div>  
</div>
            