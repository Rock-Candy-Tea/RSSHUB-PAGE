
---
title: '【酷库】如何获取到 HTML 元素指纹（CSS Selector）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ed873ca97914d809e672b31ec019b2f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 15:34:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ed873ca97914d809e672b31ec019b2f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>最近在做一个项目，要求获取到一个 <code>HTML</code> 元素指纹。比如，我点击一个元素，就能返回一个该元素的 <code>CSS selectors</code> 或者 <code>xpath</code>。找了一下，业内还蛮多这种 npm 库，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffczbkk%2Fcss-selector-generator-benchmark" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/fczbkk/css-selector-generator-benchmark" ref="nofollow noopener noreferrer">点击这里查看详情</a>。</p>
<p>本文就 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fautarc%2Foptimal-select" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/autarc/optimal-select" ref="nofollow noopener noreferrer">optimal-select</a> 讲一下是如何实现的？选择 <code>optimal-select</code> 的原因如下：</p>
<ul>
<li><code>CSS Selector</code> 相比 <code>xpath</code> 具有更优的性能和可读性.</li>
<li><code>optimal-select</code> 支持选择多个元素</li>
<li>支持配置匹配优先级（<code>priority</code>），忽略（<code>ignore</code>）等自定义匹配规则</li>
</ul>
<p>当然，也有它的一个不足之处，这个库看起来有 5 年没有更新了，不过看起来它目前的情况是最符合我们的场景了。</p>
<h2 data-id="heading-1">optimal select 的简单使用</h2>
<p>首先，安装使用如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install --save optimal-select
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单的使用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; select, getMultiSelector, getSingleSelector, getCommonProperties, common &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'optimal-select'</span> <span class="hljs-comment">// global: 'OptimalSelect'</span>
<span class="hljs-keyword">const</span> multiElements = [];
<span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> element = e.target;
  multiElements.push(e.target);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'多个元素标识'</span>, getMultiSelector(multiElements));
  <span class="hljs-comment">// 单个元素的标识</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'单个元素标识，默认：'</span>, select(element, &#123;
    <span class="hljs-comment">// default reference</span>
    <span class="hljs-attr">root</span>: <span class="hljs-built_in">document</span>,
    skip (traverseNode) &#123;
      <span class="hljs-comment">// ignore select information of the direct parent</span>
      <span class="hljs-comment">// 忽略直接父节点的选择信息</span>
      <span class="hljs-keyword">return</span> traverseNode === element.parentNode
    &#125;,
    <span class="hljs-comment">// define order of attribute processing</span>
    <span class="hljs-comment">// 定义优先级</span>
    <span class="hljs-attr">priority</span>: [<span class="hljs-string">'id'</span>, <span class="hljs-string">'class'</span>, <span class="hljs-string">'href'</span>, <span class="hljs-string">'src'</span>],
    <span class="hljs-comment">// define patterns which should't be included</span>
    <span class="hljs-comment">// 定义忽略规则</span>
    <span class="hljs-attr">ignore</span>: &#123;
      <span class="hljs-class"><span class="hljs-keyword">class</span> (<span class="hljs-title">className</span>) </span>&#123;
        <span class="hljs-comment">// disregard short classnames</span>
        <span class="hljs-keyword">return</span> className.length < <span class="hljs-number">5</span>
      &#125;,
      attribute (name, value, defaultPredicate) &#123;
        <span class="hljs-comment">// exclude HTML5 data attributes</span>
        <span class="hljs-keyword">return</span> (<span class="hljs-regexp">/data-*/</span>).test(name) || defaultPredicate(name, value)
      &#125;,
      <span class="hljs-comment">// tag: 'div'</span>
    &#125;
  &#125;));
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>演示结果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ed873ca97914d809e672b31ec019b2f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到它有两个核心功能：</p>
<ul>
<li>可以生成单个元素和多个元素公共的 <code>CSS Selector</code></li>
<li>允许配置跳过匹配规则、优先级规则和忽略模式规则等自定义选项。比如 <code>priority: ['id', 'class', 'href', 'src']</code> 就会有优先采取 id 匹配，再到 class 匹配，最后才是 href 和 src</li>
</ul>
<h2 data-id="heading-2">整体结构</h2>
<p>整体文件就 7 个，相关功能如下：</p>
<pre><code class="copyable">├── adapt.js 
├── common.js # 公共的函数，getCommonAncestor 获取到公共祖先元素。getCommonProperties 获取到公共的 属性
├── index.js  # 入口文件
├── match.js  # 单个元素的匹配
├── optimize.js # 优化
├── select.js   # 选择
└── utilities.js # 工具函数
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">获取单个元素的 CSS Selector</h2>
<p>从入口文件出发：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> select, &#123; getSingleSelector, getMultiSelector &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./select'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看 <code>select.js</code> 文件中的 <code>getSingleSelector</code> 函数。首先对 <code>Node Type </code>进行一些判断处理。<code>Node Type</code> 相关，可以参考——<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FNode%2FnodeType" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Node/nodeType" ref="nofollow noopener noreferrer">MDN</a>。</p>
<ul>
<li>假如是3（TEXT_NODE）——文字类型，则取其父元素</li>
<li>假如不是一个元素 节点，例如 <p> 和 <div>，则报错</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 假如是3（TEXT_NODE）——Element 或者 Attr 中实际的文字，则取其父元素</span>
<span class="hljs-keyword">if</span> (element.nodeType === <span class="hljs-number">3</span>) &#123;
  element = element.parentNode
&#125;
<span class="hljs-comment">// 假如不是一个元素 节点，例如 <p> 和 <div>。</span>
<span class="hljs-keyword">if</span> (element.nodeType !== <span class="hljs-number">1</span>) &#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Invalid input - only HTMLElements or representations of them are supported! (not "<span class="hljs-subst">$&#123;<span class="hljs-keyword">typeof</span> element&#125;</span>")`</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来是最主要的 <code>match</code> 方法，主要是定义在 match.js 中，用来匹配单个元素的 <code>CSS Selector</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 返回匹配到的 selector</span>
<span class="hljs-keyword">const</span> selector = match(element, options)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">默认的匹配规则</h4>
<p>解构赋值中，可以看到 <code>priority</code> 默认为 <code>['id', 'class', 'href', 'src']</code>，这个也是我们常用的编码技巧：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123;
  root = <span class="hljs-built_in">document</span>,
  skip = <span class="hljs-literal">null</span>,
  priority = [<span class="hljs-string">'id'</span>, <span class="hljs-string">'class'</span>, <span class="hljs-string">'href'</span>, <span class="hljs-string">'src'</span>],
  ignore = &#123;&#125;
&#125; = options
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">跳过（skip）的逻辑</h4>
<p>从当前元素开始遍历，直到根元素为止，<code>ignore</code> 也是一样的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 往上遍历查找匹配</span>
<span class="hljs-keyword">while</span> (element !== root) &#123;
  <span class="hljs-keyword">if</span> (skipChecks(element) !== <span class="hljs-literal">true</span>) &#123;
    <span class="hljs-comment">// ...</span>
  &#125;
  element = element.parentNode
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假如存在一个条件满足，就可以 skip：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> skipChecks = <span class="hljs-function">(<span class="hljs-params">element</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> skip && skipCompare.some(<span class="hljs-function">(<span class="hljs-params">compare</span>) =></span> compare(element)) <span class="hljs-comment">// 调用 skipCompare 看是否满足条件</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>skip 可以设置一个 node 值，function 或者是一个 node 数组。最后都处理成函数规则，以便 <code>skipChecks</code> 调用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> skipCompare = skip && (<span class="hljs-built_in">Array</span>.isArray(skip) ? skip : [skip]).map(<span class="hljs-function">(<span class="hljs-params">entry</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> entry !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">element</span>) =></span> element === entry <span class="hljs-comment">// 满足条件就跳过</span>
  &#125;
  <span class="hljs-keyword">return</span> entry
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">ignore 的逻辑</h4>
<p>ignore 的代码逻辑跟 skip 是类似的，首先是统一规则。因为配置可以是 function. number string boolean。统计处理成函数校验的方式，方便后面调用。其中 <code>ignore</code> 就是一个对象，<code>key</code> 为相应的属性名称，值为规则函数，这样方便后面的调用校验：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 可以是 function. number string boolean。统计处理成函数校验的方式</span>
<span class="hljs-built_in">Object</span>.keys(ignore).forEach(<span class="hljs-function">(<span class="hljs-params">type</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (type === <span class="hljs-string">'class'</span>) &#123;
    ignoreClass = <span class="hljs-literal">true</span>
  &#125;
  <span class="hljs-keyword">var</span> predicate = ignore[type]
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> predicate === <span class="hljs-string">'function'</span>) <span class="hljs-keyword">return</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> predicate === <span class="hljs-string">'number'</span>) &#123;
    predicate = predicate.toString()
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> predicate === <span class="hljs-string">'string'</span>) &#123;
    predicate = <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(escapeValue(predicate).replace(<span class="hljs-regexp">/\\/g</span>, <span class="hljs-string">'\\\\'</span>))
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> predicate === <span class="hljs-string">'boolean'</span>) &#123;
    predicate = predicate ? <span class="hljs-regexp">/(?:)/</span> : <span class="hljs-regexp">/.^/</span>
  &#125;
  ignore[type] = <span class="hljs-function">(<span class="hljs-params">name, value</span>) =></span> predicate.test(value)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后调用 <code>checkAttributes</code> 或者 <code>checkTag</code> 进行检查是否匹配一致，接下来说一下 <code>checkAttributes</code> 是如何检查属性的，其中调用 <code>findAttributesPattern</code> 找到元素的标识。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkAttributes</span> (<span class="hljs-params">priority, element, ignore, path, parent = element.parentNode</span>) </span>&#123;
  <span class="hljs-comment">// 找到该元素目前的标识</span>
  <span class="hljs-keyword">const</span> pattern = findAttributesPattern(priority, element, ignore)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后调用的是 <code>checkIgnore</code>，其中调用以上的规则，就可以知道是否是要忽略的了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> currentIgnore = ignore[attributeName] || ignore.attribute <span class="hljs-comment">// 获取到 check 函数的规则</span>
<span class="hljs-keyword">if</span> (checkIgnore(currentIgnore, attributeName, attributeValue, currentDefaultIgnore)) &#123;
  <span class="hljs-keyword">continue</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkIgnore</span> (<span class="hljs-params">predicate, name, value, defaultPredicate</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!value) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
  &#125;
  <span class="hljs-keyword">const</span> check = predicate || defaultPredicate
  <span class="hljs-keyword">if</span> (!check) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
  &#125;
  <span class="hljs-keyword">return</span> check(name, value, defaultPredicate)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">优先级的处理</h4>
<p>在 <code>findAttributesPattern</code> 中，通过配置的规则的前后顺序，对优先级进行排序，利用的就是 <code>JavaScript sort</code> 的语法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 根据优先级前后对属性进行进行排序</span>
<span class="hljs-keyword">const</span> sortedKeys = <span class="hljs-built_in">Object</span>.keys(attributes).sort(<span class="hljs-function">(<span class="hljs-params">curr, next</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> currPos = priority.indexOf(attributes[curr].name)
  <span class="hljs-keyword">const</span> nextPos = priority.indexOf(attributes[next].name)
  <span class="hljs-keyword">if</span> (nextPos === -<span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">if</span> (currPos === -<span class="hljs-number">1</span>) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
    &#125;
    <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>
  &#125;
  <span class="hljs-keyword">return</span> currPos - nextPos
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">检测唯一性</h4>
<p>以上我们可以拿到相关的规则了，但是众所众知，CSS Selector 可能不仅仅选中一个元素，这里通过 <code>querySelectorAll</code> 判断是否唯一，这种判断在这个库中多次运用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (pattern) &#123;
  <span class="hljs-comment">// 检查是否唯一。是的话，就加入到 path 前面</span>
  <span class="hljs-keyword">const</span> matches = parent.querySelectorAll(pattern)
  <span class="hljs-keyword">if</span> (matches.length === <span class="hljs-number">1</span>) &#123;
    path.unshift(pattern)
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，就完成了一个元素的<code> CSS Selector</code> 的唯一性匹配了。</p>
<h2 data-id="heading-9">获取多个元素的 CSS Selector</h2>
<p>其实在 <code>select.js</code> 中，有个 <code>getQuerySelector</code> 的方法，会根据传入的值进行不同的方法的调用，假如是传入的是多个 Node 的时候，就会自动调用 <code>getMultiSelector</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getQuerySelector</span> (<span class="hljs-params">input, options = &#123;&#125;</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (input.length && !input.name) &#123;
    <span class="hljs-keyword">return</span> getMultiSelector(input, options)
  &#125;
  <span class="hljs-keyword">return</span> getSingleSelector(input, options)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>getMultiSelector</code> 的实现原理也很简单：</p>
<ul>
<li><code>getCommonAncestor</code> 获取元素中公共的祖先，并使用 <code>getSingleSelector</code> 获取到公共祖先的唯一标识</li>
<li><code>getCommonSelectors</code> 获取到该元素所有的公共 <code>CSS Selector</code></li>
<li>拼接返回</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 获取元素中公共的祖先</span>
<span class="hljs-keyword">const</span> ancestor = getCommonAncestor(elements, options)
<span class="hljs-comment">// 获取到公共祖先的唯一标识</span>
<span class="hljs-keyword">const</span> ancestorSelector = getSingleSelector(ancestor, options)
<span class="hljs-comment">// 获取到该元素所有的公共 CSS Selector</span>
<span class="hljs-keyword">const</span> commonSelectors = getCommonSelectors(elements, options)
<span class="hljs-keyword">const</span> descendantSelector = commonSelectors[<span class="hljs-number">0</span>]
<span class="hljs-keyword">const</span> selector = optimize(<span class="hljs-string">`<span class="hljs-subst">$&#123;ancestorSelector&#125;</span> <span class="hljs-subst">$&#123;descendantSelector&#125;</span>`</span>, elements, options)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面提到的两个核心的方法，都在 common.js 中，我们来看下：</p>
<h3 data-id="heading-10">getCommonAncestor</h3>
<p>通过 <code>ancestors</code> 记录所有元素的可能性祖先元素：</p>
<pre><code class="hljs language-js copyable" lang="js">elements.forEach(<span class="hljs-function">(<span class="hljs-params">element, index</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> parents = []
  <span class="hljs-keyword">while</span> (element !== root) &#123;
    element = element.parentNode
    parents.unshift(element)
  &#125;
  ancestors[index] = parents
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了更加方便获取，直接取最短的祖先元素和其他的比较，这样也是一种优化处理：</p>
<pre><code class="hljs language-js copyable" lang="js">ancestors.sort(<span class="hljs-function">(<span class="hljs-params">curr, next</span>) =></span> curr.length - next.length)
<span class="hljs-keyword">const</span> shallowAncestor = ancestors.shift()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>遍历这个最短的祖先元素中的各个可能，看其他的祖先元素是否都包含该规则，假如都包含，则符合要求。否则 break</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>, l = shallowAncestor.length; i < l; i++) &#123;
  <span class="hljs-keyword">const</span> parent = shallowAncestor[i]
  <span class="hljs-keyword">const</span> missing = ancestors.some(<span class="hljs-function">(<span class="hljs-params">otherParents</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> !otherParents.some(<span class="hljs-function">(<span class="hljs-params">otherParent</span>) =></span> otherParent === parent)
  &#125;)
  <span class="hljs-keyword">if</span> (missing) &#123;
    <span class="hljs-keyword">break</span>
  &#125;
  ancestor = parent
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">getCommonSelectors</h3>
<p>获取公共属性的方式都差不多，假如没有公共属性，则直接写入。假如有公共的属性，判断当前的属性是否等于已有的公共属性，假如不等于，则删除。以下使用 tag 为例（最简单的判断）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ~ tag</span>
<span class="hljs-keyword">if</span> (commonTag !== <span class="hljs-literal">undefined</span>) &#123;
  <span class="hljs-keyword">const</span> tag = element.tagName.toLowerCase()
  <span class="hljs-keyword">if</span> (!commonTag) &#123;
    commonProperties.tag = tag
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (tag !== commonTag) &#123;
    <span class="hljs-keyword">delete</span> commonProperties.tag
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>获取多个元素的 CSS Selector 有一个比较大的问题，<strong>公共属性的获取，并不支持自定义配置忽略的规则等</strong>。所以我们可能要手动处理类似项 <code>data-v-3333</code> 这样的属性。</p>
<h2 data-id="heading-12">总结</h2>
<p><code>optimal select</code>  其实是一个比较简单的工具库，它值得我们学习的一些点如下：</p>
<ul>
<li>自定义规则配置的处理，将多种类型的配置，统一处理成函数，方便统一处理</li>
<li>一些 JavaScript 技巧的运用，比如使用 sort 对优先级进行排序</li>
<li>通过从当前元素开始往上遍历到 root 结束去确定一个元素唯一的 CSS Selector 的。其中会做一些优化（见 <code>optimize.js</code> 文件），优化后会使用 <code>querySelectorAll</code> 方法，确定其正确性</li>
<li>通过先获取到元素列表公共祖先元素的 CSS Selector，并获取到元素列表的公共属性，最后拼接成能够获取到多个元素的 CSS  Selector</li>
</ul></div>  
</div>
            