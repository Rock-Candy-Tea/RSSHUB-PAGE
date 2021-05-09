
---
title: 'Swift - PropertyWrapper'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=7913'
author: 掘金
comments: false
date: Wed, 21 Apr 2021 08:29:31 GMT
thumbnail: 'https://picsum.photos/400/300?random=7913'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、知识点</h2>
<blockquote>
<p>Property Wrapper，即属性包装器，其作用是将属性的 <code>定义代码</code> 与属性的<code>存储方式代码</code> 进行分离，抽取的<code>管理的存储代码</code>只需要编写一次，即可将功能应用于其它属性上。</p>
</blockquote>
<h3 data-id="heading-1">1、基础用法</h3>
<p>功能需求：确保值始终小于或等于12</p>
<p>这里我们直接使用 <code>property wrapper</code> 进行封装演示</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">@propertyWrapper</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">TwelveOrLess</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> number: <span class="hljs-type">Int</span>
    
    <span class="hljs-comment">// wrappedValue变量的名字是固定的</span>
    <span class="hljs-keyword">var</span> wrappedValue: <span class="hljs-type">Int</span> &#123;
        <span class="hljs-keyword">get</span> &#123; <span class="hljs-keyword">return</span> number &#125;
        <span class="hljs-keyword">set</span> &#123; number <span class="hljs-operator">=</span> <span class="hljs-built_in">min</span>(newValue, <span class="hljs-number">12</span>) &#125;
    &#125;
    
    <span class="hljs-function"><span class="hljs-keyword">init</span>()</span> &#123;
        <span class="hljs-keyword">self</span>.number <span class="hljs-operator">=</span> <span class="hljs-number">0</span>
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">SmallRectangle</span> </span>&#123;
    <span class="hljs-meta">@TwelveOrLess</span> <span class="hljs-keyword">var</span> height: <span class="hljs-type">Int</span>
    <span class="hljs-meta">@TwelveOrLess</span> <span class="hljs-keyword">var</span> width: <span class="hljs-type">Int</span>
&#125;

<span class="hljs-keyword">var</span> rectangle <span class="hljs-operator">=</span> <span class="hljs-type">SmallRectangle</span>()
<span class="hljs-built_in">print</span>(rectangle.height) <span class="hljs-comment">// 0</span>

rectangle.height <span class="hljs-operator">=</span> <span class="hljs-number">10</span>
<span class="hljs-built_in">print</span>(rectangle.height) <span class="hljs-comment">// 10</span>

rectangle.height <span class="hljs-operator">=</span> <span class="hljs-number">24</span>
<span class="hljs-built_in">print</span>(rectangle.height) <span class="hljs-comment">// 12</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里可以注意到，在创建 <code>SmallRectangle</code> 实例时，并不需要初始化 <code>height</code> 和 <code>width</code></p>
<p>原因：
被 <code>property wrapper</code> 声明的属性，实际上在存储时的类型是 <code>TwelveOrLess</code>，只不过编译器施了一些魔法，让它对外暴露的类型依然是被包装的原来的类型。
上面的 <code>SmallRectangle</code>  结构体，等同于下方这种写法</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">SmallRectangle</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> _height <span class="hljs-operator">=</span> <span class="hljs-type">TwelveOrLess</span>()
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> _width <span class="hljs-operator">=</span> <span class="hljs-type">TwelveOrLess</span>()
    <span class="hljs-keyword">var</span> height: <span class="hljs-type">Int</span> &#123;
        <span class="hljs-keyword">get</span> &#123; <span class="hljs-keyword">return</span> _height.wrappedValue &#125;
        <span class="hljs-keyword">set</span> &#123; _height.wrappedValue <span class="hljs-operator">=</span> newValue &#125;
    &#125;
    <span class="hljs-keyword">var</span> width: <span class="hljs-type">Int</span> &#123;
        <span class="hljs-keyword">get</span> &#123; <span class="hljs-keyword">return</span> _width.wrappedValue &#125;
        <span class="hljs-keyword">set</span> &#123; _width.wrappedValue <span class="hljs-operator">=</span> newValue &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">2、设置初始值</h3>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">@propertyWrapper</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">SmallNumber</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> maximum: <span class="hljs-type">Int</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> number: <span class="hljs-type">Int</span>
    
    <span class="hljs-keyword">var</span> wrappedValue: <span class="hljs-type">Int</span> &#123;
        <span class="hljs-keyword">get</span> &#123; <span class="hljs-keyword">return</span> number &#125;
        <span class="hljs-keyword">set</span> &#123; number <span class="hljs-operator">=</span> <span class="hljs-built_in">min</span>(newValue, maximum) &#125;
    &#125;
    
    <span class="hljs-function"><span class="hljs-keyword">init</span>()</span> &#123;
        maximum <span class="hljs-operator">=</span> <span class="hljs-number">12</span>
        number <span class="hljs-operator">=</span> <span class="hljs-number">0</span>
    &#125;
    
    <span class="hljs-function"><span class="hljs-keyword">init</span>(<span class="hljs-params">wrappedValue</span>: <span class="hljs-type">Int</span>)</span> &#123;
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"init(wrappedValue:)"</span>)
        maximum <span class="hljs-operator">=</span> <span class="hljs-number">12</span>
        number <span class="hljs-operator">=</span> <span class="hljs-built_in">min</span>(wrappedValue, maximum)
    &#125;
    
    <span class="hljs-function"><span class="hljs-keyword">init</span>(<span class="hljs-params">wrappedValue</span>: <span class="hljs-type">Int</span>, <span class="hljs-params">maximum</span>: <span class="hljs-type">Int</span>)</span> &#123;
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"init(wrappedValue:maximum:)"</span>)
        <span class="hljs-keyword">self</span>.maximum <span class="hljs-operator">=</span> maximum
        number <span class="hljs-operator">=</span> <span class="hljs-built_in">min</span>(wrappedValue, maximum)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用了 <code>@SmallNumber</code> 但没有指定初始化值</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">ZeroRectangle</span> </span>&#123;
    <span class="hljs-meta">@SmallNumber</span> <span class="hljs-keyword">var</span> height: <span class="hljs-type">Int</span>
    <span class="hljs-meta">@SmallNumber</span> <span class="hljs-keyword">var</span> width: <span class="hljs-type">Int</span>
&#125;

<span class="hljs-keyword">var</span> zeroRectangle <span class="hljs-operator">=</span> <span class="hljs-type">ZeroRectangle</span>()
<span class="hljs-built_in">print</span>(zeroRectangle.height, zeroRectangle.width) <span class="hljs-comment">// 0 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用了 <code>@SmallNumber</code> ，并指定初始化值</p>
<p>这里会调用 <code>init(wrappedValue:)</code> 方法 </p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">UnitRectangle</span> </span>&#123;
    <span class="hljs-meta">@SmallNumber</span> <span class="hljs-keyword">var</span> height: <span class="hljs-type">Int</span> <span class="hljs-operator">=</span> <span class="hljs-number">1</span>
    <span class="hljs-meta">@SmallNumber</span> <span class="hljs-keyword">var</span> width: <span class="hljs-type">Int</span> <span class="hljs-operator">=</span> <span class="hljs-number">1</span>
&#125;

<span class="hljs-keyword">var</span> unitRectangle <span class="hljs-operator">=</span> <span class="hljs-type">UnitRectangle</span>()
<span class="hljs-built_in">print</span>(unitRectangle.height, unitRectangle.width) <span class="hljs-comment">// 1 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用@SmallNumber，并传参进行初始化</p>
<p>这里会调用 <code>init(wrappedValue:maximum:)</code> 方法 </p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">NarrowRectangle</span> </span>&#123;
    <span class="hljs-comment">// 报错：Extra argument 'wrappedValue' in call</span>
    <span class="hljs-comment">// @SmallNumber(wrappedValue: 2, maximum: 5) var height: Int = 1</span>
    <span class="hljs-comment">// 这种初始化是可以的，调用 init(wrappedValue:maximum:) 方法</span>
    <span class="hljs-comment">// @SmallNumber(maximum: 9) var height: Int = 2</span>
    <span class="hljs-meta">@SmallNumber</span>(wrappedValue: <span class="hljs-number">2</span>, maximum: <span class="hljs-number">5</span>) <span class="hljs-keyword">var</span> height: <span class="hljs-type">Int</span>
    <span class="hljs-meta">@SmallNumber</span>(wrappedValue: <span class="hljs-number">3</span>, maximum: <span class="hljs-number">4</span>) <span class="hljs-keyword">var</span> width: <span class="hljs-type">Int</span>
&#125;

<span class="hljs-keyword">var</span> narrowRectangle <span class="hljs-operator">=</span> <span class="hljs-type">NarrowRectangle</span>()
<span class="hljs-built_in">print</span>(narrowRectangle.height, narrowRectangle.width) <span class="hljs-comment">// 2 3</span>

narrowRectangle.height <span class="hljs-operator">=</span> <span class="hljs-number">100</span>
narrowRectangle.width <span class="hljs-operator">=</span> <span class="hljs-number">100</span>
<span class="hljs-built_in">print</span>(narrowRectangle.height, narrowRectangle.width) <span class="hljs-comment">// 5 4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">3、projectedValue</h3>
<blockquote>
<p><code>projectedValue</code>为 <code>property wrapper</code> 提供了额外的功能（如：标志某个状态，或者记录 <code>property wrapper</code> 内部的变化等）</p>
<p>两者都是通过实例的属性名进行访问，唯一不同的地方在于，<code>projectedValue</code> 需要在属性名前加上 <code>$</code> 才可以访问</p>
<ul>
<li><code>wrappedValue</code>: <code>实例.属性名</code></li>
<li><code>projectedValue</code>: <code>实例.$属性名</code></li>
</ul>
</blockquote>
<p>下面的代码将一个 <code>projectedValue</code> 属性添加到 <code>SmallNumber</code> 结构中，以在存储该新值之前跟踪该属性包装器是否调整了该属性的新值。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">@propertyWrapper</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">SmallNumber1</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> number: <span class="hljs-type">Int</span>
    <span class="hljs-keyword">var</span> projectedValue: <span class="hljs-type">Bool</span>
    <span class="hljs-function"><span class="hljs-keyword">init</span>()</span> &#123;
        <span class="hljs-keyword">self</span>.number <span class="hljs-operator">=</span> <span class="hljs-number">0</span>
        <span class="hljs-keyword">self</span>.projectedValue <span class="hljs-operator">=</span> <span class="hljs-literal">false</span>
    &#125;
    <span class="hljs-keyword">var</span> wrappedValue: <span class="hljs-type">Int</span> &#123;
        <span class="hljs-keyword">get</span> &#123; <span class="hljs-keyword">return</span> number &#125;
        <span class="hljs-keyword">set</span> &#123;
            <span class="hljs-keyword">if</span> newValue <span class="hljs-operator">></span> <span class="hljs-number">12</span> &#123;
                number <span class="hljs-operator">=</span> <span class="hljs-number">12</span>
                projectedValue <span class="hljs-operator">=</span> <span class="hljs-literal">true</span>
            &#125; <span class="hljs-keyword">else</span> &#123;
                number <span class="hljs-operator">=</span> newValue
                projectedValue <span class="hljs-operator">=</span> <span class="hljs-literal">false</span>
            &#125;
        &#125;
    &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">SomeStructure</span> </span>&#123;
    <span class="hljs-meta">@SmallNumber1</span> <span class="hljs-keyword">var</span> someNumber: <span class="hljs-type">Int</span>
&#125;
<span class="hljs-keyword">var</span> someStructure <span class="hljs-operator">=</span> <span class="hljs-type">SomeStructure</span>()

someStructure.someNumber <span class="hljs-operator">=</span> <span class="hljs-number">4</span>
<span class="hljs-built_in">print</span>(someStructure.<span class="hljs-variable">$someNumber</span>) <span class="hljs-comment">// false</span>

someStructure.someNumber <span class="hljs-operator">=</span> <span class="hljs-number">55</span>
<span class="hljs-built_in">print</span>(someStructure.<span class="hljs-variable">$someNumber</span>) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 <code>someStructure.$someNumber</code> 访问的是 <code>projectedValue</code></p>
<h3 data-id="heading-4">4、使用限制</h3>
<ul>
<li>不能在协议里的属性使用</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">protocol</span> <span class="hljs-title">SomeProtocol</span> </span>&#123;
    <span class="hljs-comment">// Property 'sp' declared inside a protocol cannot have a wrapper</span>
    <span class="hljs-meta">@SmallNumber1</span> <span class="hljs-keyword">var</span> sp: <span class="hljs-type">Bool</span> &#123; <span class="hljs-keyword">get</span> <span class="hljs-keyword">set</span> &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>不能在 extension 内使用</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">SomeStructure</span> </span>&#123;
    <span class="hljs-comment">// Extensions must not contain stored properties</span>
    <span class="hljs-meta">@SmallNumber1</span> <span class="hljs-keyword">var</span> someProperty2: <span class="hljs-type">Int</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>不能在 <code>enum</code> 内使用</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">SomeEnum</span> </span>&#123;
    <span class="hljs-comment">// Property wrapper attribute 'SmallNumber1' can only be applied to a property</span>
    <span class="hljs-meta">@SmallNumber1</span> <span class="hljs-keyword">case</span> a
    <span class="hljs-keyword">case</span> b
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>class</code> 里的 <code>wrapper property</code> 不能覆盖其他的 property</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AClass</span> </span>&#123;
    <span class="hljs-meta">@SmallNumber1</span> <span class="hljs-keyword">var</span> aProperty: <span class="hljs-type">Int</span>
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BClass</span>: <span class="hljs-title">AClass</span> </span>&#123;
    <span class="hljs-comment">// Cannot override with a stored property 'aProperty'</span>
    <span class="hljs-keyword">override</span> <span class="hljs-keyword">var</span> aProperty: <span class="hljs-type">Int</span> <span class="hljs-operator">=</span> <span class="hljs-number">1</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>wrapper</code> 属性不能定义 <code>getter</code> 或 <code>setter</code> 方法</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">SomeStructure2</span> </span>&#123;
    <span class="hljs-comment">// Property wrapper cannot be applied to a computed property</span>
    <span class="hljs-meta">@SmallNumber1</span> <span class="hljs-keyword">var</span> someNumber: <span class="hljs-type">Int</span> &#123;
        <span class="hljs-keyword">get</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>wrapper</code> 属性不能被 <code>lazy</code>、 <code>@NSCopying</code>、 <code>@NSManaged</code>、 <code>weak</code>、 或者 <code>unowned</code> 修饰 </li>
</ul>
<h2 data-id="heading-5">二、实际应用</h2>
<blockquote>
<p><a href="https://github.com/jessesquires/Foil" target="_blank" rel="nofollow noopener noreferrer">Foil</a> -- 对UserDefaults进行了轻量级的属性包装第三方库</p>
<p>这部分我们主要简单的看下该第三方库的核心实现与使用</p>
</blockquote>
<h3 data-id="heading-6">1、使用</h3>
<ul>
<li>声明</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">// 声明使用的key为flagEnabled，默认值为true</span>
<span class="hljs-meta">@WrappedDefault</span>(key: <span class="hljs-string">"flagEnabled"</span>, defaultValue: <span class="hljs-literal">true</span>)
<span class="hljs-keyword">var</span> flagEnabled: <span class="hljs-type">Bool</span>

<span class="hljs-comment">// 声明使用的key为timestamp</span>
<span class="hljs-meta">@WrappedDefaultOptional</span>(key: <span class="hljs-string">"timestamp"</span>)
<span class="hljs-keyword">var</span> timestamp: <span class="hljs-type">Date</span>?
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>获取</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">// 获取变量在UserDefault中对应存储的值</span>
<span class="hljs-keyword">self</span>.flagEnabled
<span class="hljs-keyword">self</span>.timestamp
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>赋值</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">// 设置UserDefault中对应存储的值</span>
<span class="hljs-keyword">self</span>.flagEnabled <span class="hljs-operator">=</span> <span class="hljs-literal">false</span>
<span class="hljs-keyword">self</span>.timestamp <span class="hljs-operator">=</span> <span class="hljs-type">Date</span>()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">2、核心代码</h3>
<p><code>WrappedDefault.swift</code> 文件</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">@propertyWrapper</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">WrappedDefault</span><<span class="hljs-title">T</span>: <span class="hljs-title">UserDefaultsSerializable</span>> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">let</span> _userDefaults: <span class="hljs-type">UserDefaults</span>

    <span class="hljs-comment">/// 使用UserDefaults是所使用的key</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">let</span> key: <span class="hljs-type">String</span>

    <span class="hljs-comment">/// 从UserDefaults中获取到的值</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">var</span> wrappedValue: <span class="hljs-type">T</span> &#123;
        <span class="hljs-keyword">get</span> &#123;
            <span class="hljs-keyword">self</span>._userDefaults.fetch(<span class="hljs-keyword">self</span>.key)
        &#125;
        <span class="hljs-keyword">set</span> &#123;
            <span class="hljs-keyword">self</span>._userDefaults.save(newValue, for: <span class="hljs-keyword">self</span>.key)
        &#125;
    &#125;

    <span class="hljs-comment">// 初始化方法</span>
    <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-keyword">init</span>(
        <span class="hljs-params">keyName</span>: <span class="hljs-type">String</span>,        
        <span class="hljs-params">defaultValue</span>: <span class="hljs-type">T</span>,
        <span class="hljs-params">userDefaults</span>: <span class="hljs-type">UserDefaults</span> <span class="hljs-operator">=</span> .standard
    )</span> &#123;
        <span class="hljs-keyword">self</span>.key <span class="hljs-operator">=</span> keyName
        <span class="hljs-keyword">self</span>._userDefaults <span class="hljs-operator">=</span> userDefaults
        
        <span class="hljs-comment">// 对key所对应的值进行初始化（已有值则跳过，没有则进行初始化）</span>
        userDefaults.registerDefault(value: defaultValue, key: keyName)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>WrappedDefaultOptional.swift</code> 文件</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">@propertyWrapper</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">WrappedDefaultOptional</span><<span class="hljs-title">T</span>: <span class="hljs-title">UserDefaultsSerializable</span>> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">let</span> _userDefaults: <span class="hljs-type">UserDefaults</span>

    <span class="hljs-keyword">public</span> <span class="hljs-keyword">let</span> key: <span class="hljs-type">String</span>

    <span class="hljs-comment">/// 从UserDefaults中获取到的值，无则返回nil</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">var</span> wrappedValue: <span class="hljs-type">T</span>? &#123;
        <span class="hljs-keyword">get</span> &#123;
            <span class="hljs-keyword">self</span>._userDefaults.fetchOptional(<span class="hljs-keyword">self</span>.key)
        &#125;
        <span class="hljs-keyword">set</span> &#123;
            <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> newValue <span class="hljs-operator">=</span> newValue &#123;
                <span class="hljs-comment">// 更新值</span>
                <span class="hljs-keyword">self</span>._userDefaults.save(newValue, for: <span class="hljs-keyword">self</span>.key)
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-comment">// 删除值</span>
                <span class="hljs-keyword">self</span>._userDefaults.delete(for: <span class="hljs-keyword">self</span>.key)
            &#125;
        &#125;
    &#125;

    <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-keyword">init</span>(<span class="hljs-params">keyName</span>: <span class="hljs-type">String</span>,
                <span class="hljs-params">userDefaults</span>: <span class="hljs-type">UserDefaults</span> <span class="hljs-operator">=</span> .standard)</span> &#123;
        <span class="hljs-keyword">self</span>.key <span class="hljs-operator">=</span> keyName
        <span class="hljs-keyword">self</span>._userDefaults <span class="hljs-operator">=</span> userDefaults
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">三、资料</h2>
<p><a href="https://docs.swift.org/swift-book/LanguageGuide/Properties.html#ID617" target="_blank" rel="nofollow noopener noreferrer">Swift官方文档</a></p>
<p><a href="https://github.com/apple/swift-evolution/blob/master/proposals/0258-property-wrappers.md" target="_blank" rel="nofollow noopener noreferrer">apple / swift-evolution</a></p></div>  
</div>
            