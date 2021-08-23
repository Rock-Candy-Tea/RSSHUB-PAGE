
---
title: '深入浅出Map、WeakMap、Set、WeakSet'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6804'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 08:19:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=6804'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">深入浅出Map、WeakMap、Set、WeakSet</h1>
<h2 data-id="heading-1">Map</h2>
<p>在ES6之前，键值对存储通过一个<code>Object</code>对象来实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj = &#123;
    <span class="hljs-attr">key</span>: <span class="hljs-string">"val"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ES6实现了一个真正的键值对存储：<code>Map</code></p>
<h3 data-id="heading-2">基本API</h3>
<ol>
<li>实例化：<code>new Map()</code></li>
</ol>
<p>我们可以通过<code>new</code>实例化一个<code>Map</code>对象：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，如果想要在实例化的时候就去添加数据，那我们可以添加一个<strong>可迭代的对象</strong>(iterable object)，比如一个array对象：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([
    [<span class="hljs-string">'k1'</span>, <span class="hljs-string">'v1'</span>],
    [<span class="hljs-string">'k2'</span>, <span class="hljs-string">'v2'</span>],
    [<span class="hljs-string">'k3'</span>, <span class="hljs-string">'v3'</span>]
])

<span class="hljs-built_in">console</span>.log(m.size) <span class="hljs-comment">//> 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(&#123;
    [<span class="hljs-built_in">Symbol</span>.iterator]: <span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">yield</span> [<span class="hljs-string">'k1'</span>, <span class="hljs-string">'v1'</span>]
        <span class="hljs-keyword">yield</span> [<span class="hljs-string">'k2'</span>, <span class="hljs-string">'v2'</span>]
        <span class="hljs-keyword">yield</span> [<span class="hljs-string">'k3'</span>, <span class="hljs-string">'v3'</span>]
    &#125;
&#125;)

<span class="hljs-built_in">console</span>.log(m.size) <span class="hljs-comment">//> 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><code>set(k, v)</code>，添加一对新的键值对，如果键已存在，则用新值覆盖其旧值</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
m.set(<span class="hljs-string">'k1'</span>, <span class="hljs-string">'v1'</span>)

<span class="hljs-comment">// set()方法返回当前Map对象，所以可以链式调用</span>
m.set(<span class="hljs-string">'k2'</span>, <span class="hljs-string">'v2'</span>)
    .set(<span class="hljs-string">'k3'</span>, <span class="hljs-string">'v3'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li><code>get(k)</code>，根据键得到它对应的值</li>
<li><code>has(k)</code>，判断是否存在该键</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
m.set(<span class="hljs-string">'k1'</span>, <span class="hljs-string">'v1'</span>)
    .set(<span class="hljs-string">'k2'</span>, <span class="hljs-string">'v2'</span>)
    .set(<span class="hljs-string">'k3'</span>, <span class="hljs-string">'v3'</span>)

<span class="hljs-built_in">console</span>.log(m.has(<span class="hljs-string">'k1'</span>)) <span class="hljs-comment">//> true</span>
<span class="hljs-built_in">console</span>.log(m.get(<span class="hljs-string">'k1'</span>)) <span class="hljs-comment">//> v1</span>
<span class="hljs-built_in">console</span>.log(m.get(<span class="hljs-string">'k4'</span>)) <span class="hljs-comment">//> undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li><code>size</code>，得到当前<code>Map</code>对象的键值对个数</li>
<li><code>delete(k)</code>：删除指定的键值对</li>
<li><code>clear()</code>：清空<code>map</code>对象的所有键值对</li>
</ol>
<h3 data-id="heading-3">遍历</h3>
<p><code>Map</code>维护了插入顺序，会根据这个顺序进行遍历</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
m.set(<span class="hljs-string">'k1'</span>, <span class="hljs-string">'v1'</span>)
    .set(<span class="hljs-string">'k2'</span>, <span class="hljs-string">'v2'</span>)
    .set(<span class="hljs-string">'k3'</span>, <span class="hljs-string">'v3'</span>)
<span class="hljs-comment">// 方式一：</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> e <span class="hljs-keyword">of</span> m) &#123;
    <span class="hljs-built_in">console</span>.log(e)
&#125;
<span class="hljs-comment">//> [ 'k1', 'v1' ]</span>
<span class="hljs-comment">//> [ 'k2', 'v2' ]</span>
<span class="hljs-comment">//> [ 'k3', 'v3' ]</span>

<span class="hljs-comment">// 方式二：</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> e <span class="hljs-keyword">of</span> m.entries()) &#123;
    <span class="hljs-built_in">console</span>.log(e)
&#125;
<span class="hljs-comment">//> [ 'k1', 'v1' ]</span>
<span class="hljs-comment">//> [ 'k2', 'v2' ]</span>
<span class="hljs-comment">//> [ 'k3', 'v3' ]</span>

<span class="hljs-comment">// 方式三：</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> e <span class="hljs-keyword">of</span> m[<span class="hljs-built_in">Symbol</span>.iterator]()) &#123;
    <span class="hljs-built_in">console</span>.log(e)
&#125;
<span class="hljs-comment">//> [ 'k1', 'v1' ]</span>
<span class="hljs-comment">//> [ 'k2', 'v2' ]</span>
<span class="hljs-comment">//> [ 'k3', 'v3' ]</span>

<span class="hljs-comment">// 实际上方式二和方式三调用同一个方法</span>
<span class="hljs-built_in">console</span>.log(m.entries === m[<span class="hljs-built_in">Symbol</span>.iterator])
<span class="hljs-comment">//> true</span>

<span class="hljs-comment">// 方式四：</span>
m.forEach(<span class="hljs-function">(<span class="hljs-params">v, k</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log([k, v])
&#125;)
<span class="hljs-comment">//> [ 'k1', 'v1' ]</span>
<span class="hljs-comment">//> [ 'k2', 'v2' ]</span>
<span class="hljs-comment">//> [ 'k3', 'v3' ]</span>

<span class="hljs-comment">// 方式五：只遍历键</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> k <span class="hljs-keyword">of</span> m.keys()) &#123;
    <span class="hljs-built_in">console</span>.log(k)
&#125;
<span class="hljs-comment">//> k1</span>
<span class="hljs-comment">//> k2</span>
<span class="hljs-comment">//> k3</span>


<span class="hljs-comment">// 方式六：只遍历值</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> v <span class="hljs-keyword">of</span> m.values()) &#123;
    <span class="hljs-built_in">console</span>.log(v)
&#125;
<span class="hljs-comment">//> v1</span>
<span class="hljs-comment">//> v2</span>
<span class="hljs-comment">//> v3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">选择Map还是Object</h3>
<p>Map和Object都是用于键值对存储，我们需要了解它们之间的区别，方便在开发的时候进行选择</p>
<ol>
<li>内存开销：在引擎层面上，<code>Map</code>和<code>Object</code>的实现区别很大，一般来说，键值对存储的内存开销是随着键值对数量线性增长的。不过对于大部分浏览器来说，<code>Map</code>在内存开销上还是略胜一筹，粗略计算，<code>Map</code>比<code>Object</code>减少50%的内存开销，也就是说，同样的内存，<code>Map</code>可以存储更多键值对。</li>
<li>插入性能：对于<code>Map</code>和<code>Object</code>，一个插入操作不会被键值对数量所影响，但<code>Map</code>的速度会稍微快于<code>Object</code>，如果你的代码有大量插入操作，建议选择<code>Map</code>。</li>
<li>查询性能：某些情况下，浏览器会优化<code>Object</code>的存放位置（比如，有连续的整数属性），而在Map中这是不可能的，因此，如果你有大量查询，建议使用<code>Object</code>。</li>
<li>删除性能：删除操作是一件很可怕的事情，如果有删除需要，建议使用伪删除(pseudo-deleting)——将该属性赋值为<code>undefined</code>或者<code>null</code>。如果真的有删除需要，<code>Map</code>的删除性能会更快一些。</li>
</ol>
<h2 data-id="heading-5">WeakMap</h2>
<h3 data-id="heading-6">基本API</h3>
<ol>
<li>实例化</li>
</ol>
<p><code>WeakMap</code>对象的key只能是**<code>Object</code>实例化的对象或者派生类的对象**，如果不是的话，则会报错；<code>WeakMap</code>对象的value可以是任意类型：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1. Object实例化的对象</span>
<span class="hljs-keyword">const</span> k1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>()

<span class="hljs-comment">// 2. 使用字面量对象，字面量对象实际上也是Object实例化的对象</span>
<span class="hljs-keyword">const</span> k2 = &#123;&#125;

<span class="hljs-comment">// 3. Object派生类的对象</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Other</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Object</span></span>&#123;&#125;
<span class="hljs-keyword">const</span> k3 = <span class="hljs-keyword">new</span> Other()

<span class="hljs-comment">// WeakMap的value可以是任意的基本类型或者引用对象</span>
<span class="hljs-keyword">const</span> wm = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>([
    [k1, <span class="hljs-number">10086</span>],
    [k2, <span class="hljs-string">"I am China Moblie"</span>],
    [k3, <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-string">"Interesting"</span>)]
])

<span class="hljs-comment">// 如果key不符合规范则会报错</span>
<span class="hljs-keyword">const</span> badWM = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>([
    [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>],
    [<span class="hljs-string">"Yoo"</span>, <span class="hljs-string">"Ugh"</span>]
])
<span class="hljs-comment">//> TypeError: Invalid value used as weak map key</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>WeakMap</code>的其他API基本和<code>Map</code>对象是一样的，但注意，并没有<code>size</code>属性和<code>clear()</code>方法</p>
<ol start="2">
<li><code>set(k, v)</code>，添加一对新的键值对，如果键已存在，则用新值覆盖其旧值</li>
<li><code>get(k)</code>，根据键得到它对应的值</li>
<li><code>has(k)</code>，判断是否存在该键</li>
<li><code>delete(k)</code>：删除指定的键值对</li>
</ol>
<h3 data-id="heading-7">弱键</h3>
<p><code>WeakMap</code>的key只能是Object实例化对象或者派生类对象的目的是，让这个key被<strong>弱持有</strong>。</p>
<p>假设我们有一个场景，我们需要存储DOM节点的属性以及它的值，我们可能会用到<code>Object</code>或者<code>Map</code>，假设使用<code>Map</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
<span class="hljs-comment">// 假设我们需要保存一个登录按钮的属性值</span>
<span class="hljs-keyword">const</span> loginButton = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#login"</span>)
m.set(loginButton, &#123;<span class="hljs-attr">disabled</span>: <span class="hljs-literal">true</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样会产生一个问题：当用户登录之后，跑到另外一个页面，登录按钮被移除了，正常来说，这个登录DOM节点应该也应该被垃圾回收器清除，但它被<code>loginButton</code>变量引用，而<code>loginButton</code>作为key被<code>map</code>引用，所以登录DOM节点会保留在内存中，白白占用空间。</p>
<p>这时候解决方法是手动解除引用，要么使用<code>delete</code>方法删除该键值对，要么等<code>Map</code>对象被销毁。</p>
<p>如果我们使用<code>WeakMap</code>对象进行同样的储存：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> wm = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>()
<span class="hljs-keyword">const</span> loginButton = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#login"</span>)
wm.set(loginButton, &#123;<span class="hljs-attr">disabled</span>: <span class="hljs-literal">true</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>作为<code>WeakMap</code>对象key的<code>loginButton</code>不会被算成<strong>正式的引用</strong>(formal reference)，也就是说<code>loginButton</code>变量相当于不会被<code>wm</code>引用，这时垃圾回收器就可以把这个<code>loginButton</code>变量和登录DOM节点都给干掉，释放内存空间。</p>
<p>这样就起到了自动清理的效果，这也是<code>WeakMap</code><strong>弱持有</strong>的目的所在。</p>
<h3 data-id="heading-8">不可迭代键</h3>
<p><code>WeakMap</code>的key是不算正式引用，随时可能会被回收清除掉，因此<code>WeakMap</code>不提供迭代的功能。</p>
<blockquote>
<p>对于<code>size</code>属性和<code>clear()</code>方法，由于它们需要先迭代遍历所有的key才能计算得到，所以同样无法使用。</p>
</blockquote>
<h2 data-id="heading-9">Set</h2>
<p>ECAMScript6引入了<code>Set</code>类型，它同我们高中学到的集合概念是一直的——确定性、互异性、无序性。</p>
<blockquote>
<p>可能<code>Set</code>和<code>Map</code>的<code>set()</code>方法有点混，<code>Set</code>意思是<strong>集合</strong>，名词；而<code>Map.set()</code>是<strong>设置</strong>，动词来着，注意区分。</p>
</blockquote>
<h3 data-id="heading-10">基本API</h3>
<ol>
<li>实例化。同<code>Map</code>一样在构造器中添加一个可迭代对象作为初始化数据。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> set1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()

<span class="hljs-keyword">const</span> set2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-string">'v1'</span>, <span class="hljs-string">'v2'</span>, <span class="hljs-string">'v3'</span>])

<span class="hljs-built_in">console</span>.log(set2.size)
<span class="hljs-comment">//> 3</span>

<span class="hljs-keyword">const</span> set3 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(
    &#123;
        [<span class="hljs-built_in">Symbol</span>.iterator]: <span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">yield</span> <span class="hljs-string">'v1'</span>
            <span class="hljs-keyword">yield</span> <span class="hljs-string">'v2'</span>
            <span class="hljs-keyword">yield</span> <span class="hljs-string">'v3'</span>
        &#125;
    &#125;
)
<span class="hljs-built_in">console</span>.log(set3.size)
<span class="hljs-comment">//> 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>
<p><code>add()</code>，添加数据</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()
<span class="hljs-comment">// add()返回当前Set对象，因此可以链式调用</span>
s.add(<span class="hljs-string">'h'</span>).add(<span class="hljs-string">'e'</span>).add(<span class="hljs-string">'l'</span>).add(<span class="hljs-string">'l'</span>).add(<span class="hljs-string">'o'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>has(v)</code>，判断是否存在该<code>value</code></p>
</li>
<li>
<p><code>delete(v)</code>，删除该<code>value</code></p>
</li>
<li>
<p><code>clear()</code>，删除Set对象中的所有<code>value</code></p>
</li>
<li>
<p><code>size</code>，返回当前<code>Set</code>中<code>value</code>的个数</p>
</li>
</ol>
<h3 data-id="heading-11">遍历</h3>
<p>和<code>Map</code>一样，<code>Set</code>也维护了插入顺序，会根据这个顺序进行遍历。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()
s.add(<span class="hljs-string">'h'</span>).add(<span class="hljs-string">'e'</span>).add(<span class="hljs-string">'l'</span>).add(<span class="hljs-string">'l'</span>).add(<span class="hljs-string">'o'</span>)

<span class="hljs-comment">// 方式一：</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> v <span class="hljs-keyword">of</span> s) &#123;
    <span class="hljs-built_in">console</span>.log(v)
&#125;
<span class="hljs-comment">//> h</span>
<span class="hljs-comment">//> e</span>
<span class="hljs-comment">//> l //! 注意这里只有一个l，这是由于集合的互异性，每个元素都是不一样的</span>
<span class="hljs-comment">//> o</span>

<span class="hljs-comment">// 方式二：</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> v <span class="hljs-keyword">of</span> s.values()) &#123;
    <span class="hljs-built_in">console</span>.log(v)
&#125;
<span class="hljs-comment">// 或者</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> v <span class="hljs-keyword">of</span> s.keys()) &#123;
    <span class="hljs-built_in">console</span>.log(v)
&#125;
<span class="hljs-comment">//> h</span>
<span class="hljs-comment">//> e</span>
<span class="hljs-comment">//> l </span>
<span class="hljs-comment">//> o</span>

<span class="hljs-comment">// 方式三：</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> v <span class="hljs-keyword">of</span> s[<span class="hljs-built_in">Symbol</span>.iterator]()) &#123;
    <span class="hljs-built_in">console</span>.log(v)
&#125;
<span class="hljs-comment">//> h</span>
<span class="hljs-comment">//> e</span>
<span class="hljs-comment">//> l </span>
<span class="hljs-comment">//> o</span>

<span class="hljs-comment">//! 以上三种方式其实都调用同一个方法</span>
<span class="hljs-built_in">console</span>.log(s.values === s[<span class="hljs-built_in">Symbol</span>.iterator])
<span class="hljs-built_in">console</span>.log(s.keys === s[<span class="hljs-built_in">Symbol</span>.iterator])

<span class="hljs-comment">// 方式四：</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> pair <span class="hljs-keyword">of</span> s.entries()) &#123;
    <span class="hljs-built_in">console</span>.log(pair)
&#125;
<span class="hljs-comment">//> [ 'h', 'h' ] //! 键和值都是相等的</span>
<span class="hljs-comment">//> [ 'e', 'e' ]</span>
<span class="hljs-comment">//> [ 'l', 'l' ]</span>
<span class="hljs-comment">//> [ 'o', 'o' ]</span>

<span class="hljs-comment">// 方式五：</span>
s.forEach(<span class="hljs-function">(<span class="hljs-params">val, sameVal</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`[ '<span class="hljs-subst">$&#123;val&#125;</span>', '<span class="hljs-subst">$&#123;sameVal&#125;</span>' ]`</span>)
&#125;)
<span class="hljs-comment">//> [ 'h', 'h' ]</span>
<span class="hljs-comment">//> [ 'e', 'e' ]</span>
<span class="hljs-comment">//> [ 'l', 'l' ]</span>
<span class="hljs-comment">//> [ 'o', 'o' ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">WeakSet</h2>
<p><code>WeakSet</code>和<code>WeakMap</code>基本相同，存放的<code>value</code>只能是**<code>Object</code>实例化的对象或者派生类的对象**，并且不能迭代， 也没有<code>clear()</code>方法、<code>size</code>属性。</p></div>  
</div>
            