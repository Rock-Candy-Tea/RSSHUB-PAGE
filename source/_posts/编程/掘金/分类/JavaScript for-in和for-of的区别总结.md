
---
title: 'JavaScript for-in和for-of的区别总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2973'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 15:30:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=2973'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">for-in</h1>
<p><code>for...in</code>语句以<strong>任意顺序</strong>遍历一个对象的除<code>Symbol</code>以外的<strong>可枚举</strong>属性。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">for</span> (variable <span class="hljs-keyword">in</span> object)&#123;
...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>variable</code>：在每次迭代时，<code>variable</code>会被赋值为不同的<code>key</code>，即<strong>属性名</strong>。</li>
<li><code>object</code>：非<code>Symbol</code>类型的<strong>可枚举</strong>属性被迭代的对象。</li>
</ul>
<p><code>for ... in</code>更适合遍历对象，不建议与<strong>数组</strong>一起使用，因为遍历顺序有可能不是按照实际数组的索引顺序。</p>
<p><code>for ... in</code>会遍历所有的可枚举属性，包括<strong>原型</strong>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">c</span>: <span class="hljs-number">3</span> &#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myObj</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'Jack'</span>;
&#125;

myObj.prototype = obj;

<span class="hljs-keyword">const</span> user = <span class="hljs-keyword">new</span> myObj();

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> prop <span class="hljs-keyword">in</span> user) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`user.<span class="hljs-subst">$&#123;prop&#125;</span> = <span class="hljs-subst">$&#123;user[prop]&#125;</span>`</span>);
&#125;
<span class="hljs-comment">// user.name = Jack</span>
<span class="hljs-comment">// user.a = 1</span>
<span class="hljs-comment">// user.b = 2</span>
<span class="hljs-comment">// user.c = 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果想仅迭代自身的属性，需要使用<code>hasOwnProperty()</code>方法判断某个属性是否是该对象的实例属性：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">c</span>: <span class="hljs-number">3</span> &#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myObj</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'Jack'</span>;
&#125;

myObj.prototype = obj;

<span class="hljs-keyword">const</span> user = <span class="hljs-keyword">new</span> myObj();

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> prop <span class="hljs-keyword">in</span> user) &#123;
    <span class="hljs-keyword">if</span> (user.hasOwnProperty(prop)) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`user.<span class="hljs-subst">$&#123;prop&#125;</span> = <span class="hljs-subst">$&#123;user[prop]&#125;</span>`</span>);
    &#125;
&#125;
<span class="hljs-comment">// user.name = Jack</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">for-of</h1>
<p><code>for...of</code>语句在<strong>可迭代对象</strong>（包括 <code>Array</code>，<code>Map</code>，<code>Set</code>，<code>String</code>，<code>TypedArray</code>，<code>arguments</code>对象等 ）上创建一个迭代循环，并为每个<strong>不同属性的值</strong>执行语句。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">for</span> (variable <span class="hljs-keyword">of</span> iterable) &#123;
...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>variable</code>：在每次迭代中，将不同属性的<strong>值</strong>分配给<code>variable</code>。</li>
<li><code>iterable</code>：被迭代枚举其属性的对象。</li>
</ul>
<blockquote>
<p>与<code>forEach()</code>不同的是，它可以正确响应<code>break</code>、<code>continue</code>和<code>return</code>语句。</p>
</blockquote>
<p>迭代<strong>数组</strong>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">10</span>, <span class="hljs-number">20</span>, <span class="hljs-number">30</span>];

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> value <span class="hljs-keyword">of</span> arr) &#123;
    <span class="hljs-built_in">console</span>.log(value);
&#125;
<span class="hljs-comment">// 10</span>
<span class="hljs-comment">// 20</span>
<span class="hljs-comment">// 30</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>迭代<code>Map</code>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([
    [<span class="hljs-string">'a'</span>, <span class="hljs-number">1</span>],
    [<span class="hljs-string">'b'</span>, <span class="hljs-number">2</span>],
    [<span class="hljs-string">'c'</span>, <span class="hljs-number">3</span>],
]);

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> entry <span class="hljs-keyword">of</span> map) &#123;
    <span class="hljs-built_in">console</span>.log(entry);
&#125;
<span class="hljs-comment">// ["a", 1]</span>
<span class="hljs-comment">// ["b", 2]</span>
<span class="hljs-comment">// ["c", 3]</span>

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> [key, value] <span class="hljs-keyword">of</span> map) &#123;
    <span class="hljs-built_in">console</span>.log(value);
&#125;
<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// 2</span>
<span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>迭代<code>arguments</code>对象：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> argument <span class="hljs-keyword">of</span> <span class="hljs-built_in">arguments</span>) &#123;
        <span class="hljs-built_in">console</span>.log(argument);
    &#125;
&#125;)(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>);

<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// 2</span>
<span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">总结</h1>
<ul>
<li><code>for...in</code>语句以<strong>任意顺序</strong>迭代对象的<strong>键</strong>，包括<strong>原型</strong>。不建议与<strong>数组</strong>一起使用。</li>
<li><code>for...of</code> 语句遍历<strong>可迭代对象</strong>的<strong>值</strong>。</li>
</ul></div>  
</div>
            