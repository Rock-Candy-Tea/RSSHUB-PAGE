
---
title: 'vue3 沙箱机制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3036'
author: 掘金
comments: false
date: Wed, 14 Apr 2021 03:18:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=3036'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">vue3 沙箱机制</h3>
<h3 data-id="heading-1">前言</h3>
<p>vue3 沙箱主要分两种</p>
<ol>
<li>浏览器编译版本，浏览器版本是使用<code>with</code>语法加上<code>proxy</code>代理拦截</li>
<li>本地预编译版本，通过在模版预编译阶段转换阶段，使用转换插件<code>transformExpression</code>将非白名单标识符挂在在组件代理对象下</li>
</ol>
<h3 data-id="heading-2">浏览器编译版本</h3>
<p>render 函数编译结果</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123;test&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123;Math.floor(1)&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>to</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> _Vue = Vue;

<span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">_ctx, _cache, $props, $setup, $data, $options</span>) </span>&#123;
  <span class="hljs-keyword">with</span> (_ctx) &#123;
    <span class="hljs-keyword">const</span> &#123;
      <span class="hljs-attr">toDisplayString</span>: _toDisplayString,
      <span class="hljs-attr">createVNode</span>: _createVNode,
      <span class="hljs-attr">Fragment</span>: _Fragment,
      <span class="hljs-attr">openBlock</span>: _openBlock,
      <span class="hljs-attr">createBlock</span>: _createBlock,
    &#125; = _Vue;

    <span class="hljs-keyword">return</span> (
      _openBlock(),
      _createBlock(
        _Fragment,
        <span class="hljs-literal">null</span>,
        [
          _createVNode(<span class="hljs-string">"div"</span>, <span class="hljs-literal">null</span>, _toDisplayString(test), <span class="hljs-number">1</span> <span class="hljs-comment">/* TEXT */</span>),
          _createVNode(
            <span class="hljs-string">"div"</span>,
            <span class="hljs-literal">null</span>,
            _toDisplayString(<span class="hljs-built_in">Math</span>.floor(<span class="hljs-number">1</span>)),
            <span class="hljs-number">1</span> <span class="hljs-comment">/* TEXT */</span>
          ),
        ],
        <span class="hljs-number">64</span> <span class="hljs-comment">/* STABLE_FRAGMENT */</span>
      )
    );
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码，我们能发现，变量标识符没有增加前缀，只是用<code>with</code>语法包裹了一下，延长作用域链，那么是如何做到 js 沙箱拦截的呢？例如变量<code>test</code>，
理论上说，当前作用域链没有<code>test</code>变量，变量会从上一层作用域查找，直到查找到全局作用域，但是，实际上只会在<code>_ctx</code>上查找，
原理很简单，<code>_ctx</code>是一个代理对象，那么我们如何使用<code>Proxy</code>做拦截，示例代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> GLOBALS_WHITE_LISTED =
  <span class="hljs-string">"Infinity,undefined,NaN,isFinite,isNaN,parseFloat,parseInt,decodeURI,"</span> +
  <span class="hljs-string">"decodeURIComponent,encodeURI,encodeURIComponent,Math,Number,Date,Array,"</span> +
  <span class="hljs-string">"Object,Boolean,String,RegExp,Map,Set,JSON,Intl,BigInt"</span>;

<span class="hljs-keyword">const</span> isGloballyWhitelisted = <span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> GLOBALS_WHITE_LISTED.split(<span class="hljs-string">","</span>).includes(key);
&#125;;

<span class="hljs-keyword">const</span> hasOwn = <span class="hljs-function">(<span class="hljs-params">obj, key</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype.hasOwnProperty.call(obj, key);
&#125;;

<span class="hljs-keyword">const</span> origin = &#123;&#125;;
<span class="hljs-keyword">const</span> _ctx = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(origin, &#123;
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, key, reciever</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (hasOwn(target, key)) &#123;
      <span class="hljs-built_in">Reflect</span>.get(target, key, reciever);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">console</span>.warn(
        <span class="hljs-string">`Property <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(key)&#125;</span> was accessed during render `</span> +
          <span class="hljs-string">`but is not defined on instance.`</span>
      );
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">has</span>(<span class="hljs-params">target, key</span>)</span> &#123;
    <span class="hljs-comment">// 如果是 全局对象 返回false，不触发get 拦截，从上一层作用域查找变量</span>
    <span class="hljs-comment">// 如果不是 全局对象 返回true，触发get 拦截</span>
    <span class="hljs-keyword">return</span> !isGloballyWhitelisted(key);
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码很简单，为什么这么简单的代码就能做到拦截？
因为 <code>with</code> 语句会触发 <code>has</code> 拦截，当 <code>has</code> 返回 <code>true</code>，就会 触发代理对象 <code>get</code> 拦截，如果返回 <code>false</code>， 则代理对象 <code>get</code> 拦截不会触发，变量不在当前代理对象查找，直接查找更上一层作用域</p>
<h3 data-id="heading-3">本地预编译版本</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123;test&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123;Math.floor(1)&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>to</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;
  toDisplayString <span class="hljs-keyword">as</span> _toDisplayString,
  createVNode <span class="hljs-keyword">as</span> _createVNode,
  Fragment <span class="hljs-keyword">as</span> _Fragment,
  openBlock <span class="hljs-keyword">as</span> _openBlock,
  createBlock <span class="hljs-keyword">as</span> _createBlock,
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">_ctx, _cache, $props, $setup, $data, $options</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    _openBlock(),
    _createBlock(
      _Fragment,
      <span class="hljs-literal">null</span>,
      [
        _createVNode(<span class="hljs-string">"div"</span>, <span class="hljs-literal">null</span>, _toDisplayString(_ctx.a), <span class="hljs-number">1</span> <span class="hljs-comment">/* TEXT */</span>),
        _createVNode(
          <span class="hljs-string">"div"</span>,
          <span class="hljs-literal">null</span>,
          _toDisplayString(<span class="hljs-built_in">Math</span>.floor(<span class="hljs-number">1</span>)),
          <span class="hljs-number">1</span> <span class="hljs-comment">/* TEXT */</span>
        ),
      ],
      <span class="hljs-number">64</span> <span class="hljs-comment">/* STABLE_FRAGMENT */</span>
    )
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码我们可以发现，非白名单标识符都添加了<code>_ctx</code> 变量前缀，那么是如何做到的呢？当本地编译 template 时，处于转换阶段时会对 变量表达式节点<code>NodeTypes.SIMPLE_EXPRESSION</code>进行添加前缀处理，示例代码如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> GLOBALS_WHITE_LISTED =
  <span class="hljs-string">"Infinity,undefined,NaN,isFinite,isNaN,parseFloat,parseInt,decodeURI,"</span> +
  <span class="hljs-string">"decodeURIComponent,encodeURI,encodeURIComponent,Math,Number,Date,Array,"</span> +
  <span class="hljs-string">"Object,Boolean,String,RegExp,Map,Set,JSON,Intl,BigInt"</span>;

<span class="hljs-keyword">const</span> isGloballyWhitelisted = <span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> GLOBALS_WHITE_LISTED.split(<span class="hljs-string">","</span>).includes(key);
&#125;;
<span class="hljs-keyword">const</span> isLiteralWhitelisted = <span class="hljs-function">(<span class="hljs-params">key</span>)=></span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">'true,false,null,this'</span>.split(<span class="hljs-string">','</span>).includes(key)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processExpression</span>(<span class="hljs-params">
  node
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> rewriteIdentifier = <span class="hljs-function">(<span class="hljs-params">raw</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`_ctx.<span class="hljs-subst">$&#123;raw&#125;</span>`</span>
  &#125;
  <span class="hljs-keyword">const</span> rawExp = node.content
  <span class="hljs-keyword">if</span> (isSimpleIdentifier(rawExp)) &#123;
    <span class="hljs-keyword">const</span> isAllowedGlobal = isGloballyWhitelisted(rawExp)
    <span class="hljs-keyword">const</span> isLiteral = isLiteralWhitelisted(rawExp)
    <span class="hljs-keyword">if</span> (!isAllowedGlobal && !isLiteral) &#123;
      node.content = rewriteIdentifier(rawExp)
    &#125;
    <span class="hljs-keyword">return</span> node
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然上面的代码只是简化版本，原版插件还做了精确到了<code>__props</code> <code>$setup</code>，减短变量查询路径，提高性能，还有通过<code>babel</code>编译复杂表达式比如：箭头函数。</p>
<h3 data-id="heading-4">总结</h3>
<p>整个 vue3 js 沙箱机制就解释结束了，当初浏览器编译版本困扰了我很久，因为不知道 <code>has</code> 可以拦截 <code>with</code> 语句变量查询</p>
<h3 data-id="heading-5">参考</h3>
<ol>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/has" target="_blank" rel="nofollow noopener noreferrer">Proxy handler.has</a></li>
<li><a href="https://juejin.cn/post/6844903954074058760#heading-3" target="_blank">说说 JS 中的沙箱</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/58602800" target="_blank" rel="nofollow noopener noreferrer">动手写 js 沙箱</a></li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            