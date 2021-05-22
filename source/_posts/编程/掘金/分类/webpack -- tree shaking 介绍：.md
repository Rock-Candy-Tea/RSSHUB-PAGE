
---
title: 'webpack -- tree shaking 介绍：'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7728'
author: 掘金
comments: false
date: Fri, 21 May 2021 19:31:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=7728'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><strong>tree shaking</strong> 的作用：</h2>
<p>在我们使用webpack进行打包的时候，我们现在有一个有一个模块A.js;我们在index.js中引入A模块的部分代码；tree shaking会帮我们吧我们<strong>不需要的其他代码</strong>删除掉；只打包我们<strong>已经使用的代码</strong>；</p>
<ol>
<li>一个模块引用了没有被使用；</li>
<li>一个模块中可能有很多方法，但实际使用中可能没有被全部使用到；</li>
<li>代码中Dead code 死代码；</li>
</ol>
<h6 data-id="heading-1">就像这样：</h6>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// A.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> a = <span class="hljs-string">'a'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> b = <span class="hljs-string">'b'</span>;    <span class="hljs-comment">// 不导出，删除</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> c = <span class="hljs-string">'c'</span>;    <span class="hljs-comment">// 导出不引用，删除</span>

<span class="hljs-comment">// index.js </span>
<span class="hljs-keyword">import</span> &#123; a, c &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.js'</span>; 
<span class="hljs-built_in">console</span>.log(a);
<span class="hljs-keyword">if</span>(<span class="hljs-literal">false</span>) &#123;             <span class="hljs-comment">// 不会执行的代码，删除</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'去除我'</span>);  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">使用：</h3>
<p>在mode：production的模式下 tree shaking自动启用；不需要我们手动开启；
<strong>必须使用ES6语法，不支持CJS</strong>，因为import和require的引入方式是不同的；
因为 tree shaking只能对<strong>静态的代码</strong>进行分析；import引入属于静态引入，而require属于动态引入；</p>
<h3 data-id="heading-3">注意</h3>
<p>在我们使用的过程中；我发现tree shaking并不能对我们的一些<strong>副作用代码</strong>进行优化；
像class中一些方法，和一些副作用函数之类的；
副作用：副作用可以理解成某个模块执行时除了导出成员之外所作的事情；详细就不累述了；</p>
<h3 data-id="heading-4">tree shaking优化：sideEffects：true/false/数组</h3>
<h4 data-id="heading-5">前提：webpack 的版本号要大于等于 4</h4>
<h4 data-id="heading-6">解释：</h4>
<p>false ：告诉 webpack 我这个 npm 包里的所有文件代码都是没有副作用的；
数组：数组则表示告诉 webpack 我这个 npm 包里指定文件代码是没有副作用的</p>
<h4 data-id="heading-7">使用</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// package.json</span>
&#123;
    <span class="hljs-string">"sideEffects"</span>: <span class="hljs-literal">false</span>
&#125;
<span class="hljs-comment">// antd package.json</span>
&#123;
  <span class="hljs-string">"sideEffects"</span>: [
    <span class="hljs-string">"dist/*"</span>,
    <span class="hljs-string">"es/**/style/*"</span>,
    <span class="hljs-string">"lib/**/style/*"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还可以对webpack 的配置文件中配置：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.jsx?$/</span>,
        exclude: <span class="hljs-regexp">/(node_modules|bower_components)/</span>,
        use: &#123;
          <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
        &#125;,
        <span class="hljs-attr">sideEffects</span>: <span class="hljs-literal">false</span> || []
      &#125;
    ]
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就会对我们的整个项目生效了；我们就可以愉快的吧我们的不需要的副作用代码优化掉！</p></div>  
</div>
            