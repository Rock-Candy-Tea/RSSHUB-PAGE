
---
title: '前端业务常量的快捷使用方案：消除恶心的find与魔法值'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=778'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 03:58:14 GMT
thumbnail: 'https://picsum.photos/400/300?random=778'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">在前端开发时，经常会使用到业务常量</h3>
<p>如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fieldType = [
  &#123; <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">label</span>: <span class="hljs-string">'文本'</span> &#125;,
  &#123; <span class="hljs-attr">value</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">label</span>: <span class="hljs-string">'数字'</span> &#125;,
  &#123; <span class="hljs-attr">value</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">label</span>: <span class="hljs-string">'视频'</span> &#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用它的场景大致有三类：</p>
<h4 data-id="heading-1">1. 当做表单输入的可选项被遍历</h4>
<blockquote>
<p>作为select、radio、checkbox等的选项值</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">el-select</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"type"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">el-option</span>
    <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in fieldType"</span>
    <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.value"</span>
    <span class="hljs-attr">:label</span>=<span class="hljs-string">"item.label"</span>
    <span class="hljs-attr">:value</span>=<span class="hljs-string">"item.value"</span>
  ></span>
  <span class="hljs-tag"></<span class="hljs-name">el-option</span>></span>
<span class="hljs-tag"></<span class="hljs-name">el-select</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是常量最普遍被使用的方式，所以大多数常量都被存储为数组，并且包含<code>value</code>、<code>label</code>两个字段</p>
<h4 data-id="heading-2">2. 把<code>value</code>转为<code>label</code>显示</h4>
<p>有时后端提供的数据的是<code>value</code>，那么前端显示时<strong>需要把数字转化为文字</strong>。这个过程在实践中，是很重复、繁琐的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">enumsFilter</span>(<span class="hljs-params">value</span>)</span> &#123;
  <span class="hljs-keyword">if</span> (!value) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
  &#125;
  <span class="hljs-keyword">const</span> item = fieldType.find(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.value === value)
  <span class="hljs-keyword">return</span> item ? item.label : <span class="hljs-string">''</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述逻辑大概率会在<code>filter</code>中实现（vue3已取消filter功能），也可能出现在其他函数中。</p>
<h5 data-id="heading-3">NOTE：最重要的是，<strong>这段逻辑无处不在，很恶心。</strong></h5>
<h4 data-id="heading-4">3. 用英文名获取<code>value</code>，消除<a href="https://baike.baidu.com/item/%E9%AD%94%E6%95%B0" target="_blank" rel="nofollow noopener noreferrer">魔法值</a></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span>(typeValue === <span class="hljs-number">1</span>)&#123;
<span class="hljs-comment">// do something</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>魔法值的问题很明显：<strong>没有语义，不易于维护。</strong></p>
<p>于是就出现了<strong>使用英文名字来获取<code>value</code>的方式，使代码语义化</strong>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span>(typeValue === fieldTypeEnum.TEXT)&#123;
    <span class="hljs-comment">// do something</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么就需要数据原来维护，英文名和<code>value</code>的对应关系</p>
<pre><code class="hljs language-js copyable" lang="js">fieldTypeEnum = &#123;
    <span class="hljs-attr">TEXT</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">NUMBER</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">VIDEO</span>: <span class="hljs-number">3</span>,
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5"><strong>NOTE：一个常量，需要维护两份数据。因为耗费精力，偷懒就造成魔法值泛滥。</strong></h5>
<p>上述的后两种使用场景，都有各自的问题。于是我尝试简化这两个场景的代码。</p>
<h3 data-id="heading-6">网上的解决方案：</h3>
<p>对于上述常量使用场景的相应问题，网上也有一些解决方案：</p>
<p>数据源维护<code>value、label、name</code>三个字段，并使用<code>createEnum</code>处理数据源：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> fieldType = createEnum([
  &#123; <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">label</span>: <span class="hljs-string">'文本'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'TEXT'</span> &#125;,
  &#123; <span class="hljs-attr">value</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">label</span>: <span class="hljs-string">'数字'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'NUMBER'</span> &#125;,
  &#123; <span class="hljs-attr">value</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">label</span>: <span class="hljs-string">'视频'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'VIDEO'</span> &#125;
])
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>createEnum</code>返回值为数组，会携带两个方法<code>getLableByValue</code>、<code>getValueByName</code>，来覆盖上述的后两种场景：<code>value => label</code>，<code>name => value</code>，使用示例:</p>
<pre><code class="copyable">fieldType  // list

fieldType.getLableByValue(1) // '文本'

fieldType.getValueByName('TEXT')  // 1
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">我的优化：</h3>
<p>我的纠结点在于：有没有另一种方式，能把函数调用省略掉，一是因为<strong>写函数名也很麻烦</strong>，二是因为<strong>使用调用，代码就会有<code>ReferenceError</code>报错的概率</strong>。</p>
<p>尝试了很多种方式，终于找到了完美的方式，覆盖三种常量的使用场景，并且使用更简洁：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> fieldType = createEnum([
  &#123; <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">label</span>: <span class="hljs-string">'文本'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'TEXT'</span> &#125;,
  &#123; <span class="hljs-attr">value</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">label</span>: <span class="hljs-string">'数字'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'NUMBER'</span> &#125;,
  &#123; <span class="hljs-attr">value</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">label</span>: <span class="hljs-string">'视频'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'VIDEO'</span> &#125;
])


fieldType()  <span class="hljs-comment">// list</span>

fieldType(<span class="hljs-number">1</span>)  <span class="hljs-comment">// '文本'</span>
fieldType(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>)  <span class="hljs-comment">// '文本、数组、视频'  代码未实现</span>

fieldType(<span class="hljs-string">'TEXT'</span>)  <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>createEnum</code>返回的是函数，通过传参来获取不同的数据，类似于枚举的效果。</p>
<h4 data-id="heading-8">优势：</h4>
<ol>
<li>省略了<code>value ==> label</code>过程中，恶心、重复的<code>find</code>过程；</li>
<li>三种场景的使用方式都是函数调用，一致且简洁；</li>
</ol>
<h4 data-id="heading-9">代码实现很简单：</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 业务常量的使用方式扩展
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Array&#125;</span> </span>source 
    [
      &#123; value: 1,label: '空间站',name: 'SPACE' &#125;,
      &#123; value: 2, label: '实践任务', name: 'PRACTICE' &#125;,
      &#123; value: 3, label: '其他系统', name: 'OTHERS' &#125;
    ]
  <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Function&#125;</span> <span class="hljs-variable">fn</span></span>
    fn() ===> source
    fn(value) ===> label
    fn(name) ===> value
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createEnum</span>(<span class="hljs-params">source</span>) </span>&#123;
  <span class="hljs-keyword">const</span> sourceMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
  source.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    sourceMap.set(item.name, item.value)
    sourceMap.set(item.value, item.label)
  &#125;)

  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">key</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (key) &#123;
      <span class="hljs-keyword">return</span> sourceMap.get(key)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span> source
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>考虑到不是所有的常量都会有第三种使用场景(name=>value)，所以<code>name</code>是可选的。你可以碰到此场景时，再回来定义name，以避免多余的工作量，毕竟起英文名也很费精力。</p>
</blockquote>
<p>当时想了很多种方式，把<code>source</code>数组和<code>sourceMap</code>结合在一起，代理<code>proxy</code>、迭代器<code>iterator</code>、原型<code>prototype</code>等等，最后选用了函数调用的方式，简单、有效。</p>
<h3 data-id="heading-10">懒人提效系列：</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6967098818957410318" target="_blank">面对重复的代码、逻辑，如何提高开发效率</a></p>
<p><a href="https://juejin.cn/post/6940062321007919111" target="_blank">使用类名，高效快捷的进行flex布局</a></p>
<p><a href="https://juejin.cn/post/6920160545962197006" target="_blank">element-ui 弹窗组件封装 极简方案</a></p>
</blockquote></div>  
</div>
            