
---
title: 'vue3.0中的响应式钩子是如何实现的'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2764'
author: 掘金
comments: false
date: Thu, 29 Apr 2021 02:24:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=2764'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">先来聊聊<code>Vue3.0</code>的变化</h3>
<p>Vue3.0相比Vue2.0发生了翻天覆地的变化，从设计理念，到架构模式都发生了变化，笔者列入最核心的变化</p>
<ul>
<li>diff设计变化，将dom渲染做到极致</li>
<li>优化静态变量提升，提高无效的dom渲染</li>
<li>监听缓存机制，让重复的数据流操作消失</li>
<li>组合式的API，然代码的耦合度更低</li>
<li>重写object.defineproperty()的数据双向绑定,使用Proxy代理重写</li>
</ul>
<blockquote>
<p>划重点，今天我们聊的只是基于Proxy实现的响应式代理</p>
</blockquote>
<p>默认大家已经明白<code>Proxy</code>的原理是什么，如果大家还不太了解Proxy的原理先请大家移步<a href="https://es6.ruanyifeng.com/#docs/proxy" target="_blank" rel="nofollow noopener noreferrer">阮一峰Proxy讲解</a></p>
<h3 data-id="heading-1">shallowReactive实现</h3>
<p>首先我们先看看shallowReactive到底是个什么<code>创建一个响应式代理，它跟踪其自身 property 的响应性，但不执行嵌套对象的深层响应式转换 (暴露原始值)。(官网原话)</code>。由此我们能得到这个hooks实现的只会代理第一层。</p>
<p>代码实现</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">shallowReactive</span>(<span class="hljs-params">obj</span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">obj, key</span>)</span>&#123;
            <span class="hljs-keyword">return</span> obj[key]
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">obj, key, val</span>)</span>&#123;
            obj[key] = val
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"更新UI界面"</span>)
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        &#125;
    &#125;)
&#125;
<span class="hljs-comment">// 测试</span>

<span class="hljs-keyword">let</span> obj = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-string">'a'</span>,
    <span class="hljs-attr">gf</span>: &#123;
        <span class="hljs-attr">b</span>: <span class="hljs-string">'b'</span>,
        <span class="hljs-attr">f</span>: &#123;
            <span class="hljs-attr">c</span>: <span class="hljs-string">'c'</span>,
            <span class="hljs-attr">s</span>: &#123;
                <span class="hljs-attr">d</span>: <span class="hljs-string">'d'</span>
            &#125;
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">let</span> state = shallowReactive(obj)
state.a = <span class="hljs-string">'1'</span>
state.gf.b = <span class="hljs-string">'2'</span>
state.gf.f.c = <span class="hljs-string">'3'</span>
state.gf.f.s.d = <span class="hljs-string">'4'</span>
<span class="hljs-comment">// 只会代理第一层 所以只会出发一次更新ui操作</span>
<span class="hljs-built_in">console</span>.log(state) 
<span class="hljs-comment">/*
更新UI界面
&#123; a: '1', gf: &#123; b: '2', f: &#123; c: '3', s: [Object] &#125; &#125; &#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">shallowRef</h3>
<blockquote>
<p>概念 ：创建一个跟踪自身 <code>.value</code> 变化的 ref，但不会使其值也变成响应式的。</p>
</blockquote>
<p>从官网的话中能够明白，实际上shallowRef与shallowReactive之间的区别就在于被value包裹了一层</p>
<p>代码实现:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">shallowRef</span>(<span class="hljs-params">val</span>)</span>&#123;
    <span class="hljs-comment">// 实现代码只需要shallowReactive拿过来那代理一次就可</span>
    <span class="hljs-keyword">return</span> shallowReactive(&#123;<span class="hljs-attr">value</span>: val&#125;)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">shallowReactive</span>(<span class="hljs-params">obj</span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">obj, key</span>)</span>&#123;
            <span class="hljs-keyword">return</span> obj[key]
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">obj, key, val</span>)</span>&#123;
            obj[key] = val
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"更新UI界面"</span>)
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        &#125;
    &#125;)
&#125;
<span class="hljs-keyword">let</span> obj = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-string">'a'</span>,
    <span class="hljs-attr">gf</span>: &#123;
        <span class="hljs-attr">b</span>: <span class="hljs-string">'b'</span>,
        <span class="hljs-attr">f</span>: &#123;
            <span class="hljs-attr">c</span>: <span class="hljs-string">'c'</span>,
            <span class="hljs-attr">s</span>: &#123;
                <span class="hljs-attr">d</span>: <span class="hljs-string">'d'</span>
            &#125;
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">let</span> state = shallowRef(obj)
<span class="hljs-comment">// state.value.a = '1'</span>
<span class="hljs-comment">// state.value.gf.b = '2'</span>
<span class="hljs-comment">// state.value.gf.f.c = '3'</span>
<span class="hljs-comment">// state.value.gf.f.s.d = '4'</span>
<span class="hljs-comment">// 修改里面的值不会发生改变只能监听第一层</span>
state.value = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-string">'1'</span>,
    <span class="hljs-attr">gf</span>: &#123;
        <span class="hljs-attr">b</span>: <span class="hljs-string">'2'</span>,
        <span class="hljs-attr">f</span>: &#123;
            <span class="hljs-attr">c</span>: <span class="hljs-string">'3'</span>,
            <span class="hljs-attr">s</span>: &#123;
                <span class="hljs-attr">d</span>: <span class="hljs-string">'4'</span>
            &#125;
        &#125;
    &#125;
&#125;
<span class="hljs-built_in">console</span>.log(state)
<span class="hljs-comment">/*
更新UI界面
&#123; value: &#123; a: '1', gf: &#123; b: '2', f: [Object] &#125; &#125; &#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">shallowReadonly</h3>
<blockquote>
<p>概念：创建一个 proxy，使其自身的 property 为只读，但不执行嵌套对象的深度只读转换 (暴露原始值)。</p>
</blockquote>
<p>大致的意思就是只会做底层代理，同时这一层代理是不能够操作的, 其他层次的值可以修改但是不会被proxy代理</p>
<p>代码实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// shallowReadonly只需要set函数中不要设置值</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">shallowReadonly</span>(<span class="hljs-params">obj</span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">obj, key</span>)</span>&#123;
            <span class="hljs-keyword">return</span> obj[key]
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">obj, key, val</span>)</span>&#123;
            <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">`<span class="hljs-subst">$&#123;key&#125;</span> 只读，不能赋值`</span>)
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        &#125;
    &#125;)
&#125;
<span class="hljs-keyword">let</span> obj = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-string">'a'</span>,
    <span class="hljs-attr">gf</span>: &#123;
        <span class="hljs-attr">b</span>: <span class="hljs-string">'b'</span>,
        <span class="hljs-attr">f</span>: &#123;
            <span class="hljs-attr">c</span>: <span class="hljs-string">'c'</span>,
            <span class="hljs-attr">s</span>: &#123;
                <span class="hljs-attr">d</span>: <span class="hljs-string">'d'</span>
            &#125;
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">let</span> state = shallowReadonly(obj)
state.a = <span class="hljs-string">'1'</span>
state.gf.b = <span class="hljs-string">'2'</span>
state.gf.f.c = <span class="hljs-string">'3'</span>
state.gf.f.s.d = <span class="hljs-string">'4'</span>
<span class="hljs-comment">// 只会代理第一层 所以只会出发一次更新ui操作</span>
<span class="hljs-built_in">console</span>.log(state)
<span class="hljs-comment">/*
a 只读，不能赋值
&#123; a: 'a', gf: &#123; b: '2', f: &#123; c: '3', s: [Object] &#125; &#125; &#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">reactive</h3>
<blockquote>
<p>概念：返回对象的响应式副本</p>
</blockquote>
<p>和shallowReactive的区别是在于reactive是需要把所有的对象进行代理</p>
<p>代码实现:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 产生递归监听</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span>(<span class="hljs-params">obj</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> obj === <span class="hljs-string">"object"</span>)&#123;
        <span class="hljs-keyword">if</span>(obj <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>)&#123;
            <span class="hljs-comment">// 如果是一个数组，取出数组中的每一元素，判断每一个元素是否又是一个对象</span>
            <span class="hljs-comment">// 如果又是一个对象需要包装成一个proxy</span>
            obj.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
                <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> item === <span class="hljs-string">"object"</span>)&#123;
                    obj[index] = reactive(item)
                &#125;
            &#125;)
        &#125;<span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 如果是一个对象取出对象属性的一个去吃没判断对象属性的取值也需要包装成Proxy</span>
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> obj) &#123;
                <span class="hljs-keyword">let</span> item = obj[key]
                <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> item === <span class="hljs-string">"object"</span>)&#123;
                    obj[key] = reactive(item)
                &#125;
            &#125;
        &#125;
    &#125;<span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">`<span class="hljs-subst">$&#123;obj&#125;</span> is not object`</span>)
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">obj, key</span>)</span>&#123;
            <span class="hljs-keyword">return</span> obj[key]
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">obj, key, value</span>)</span>&#123;
            obj[key] = value
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"更新UI界面"</span>)
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        &#125;
    &#125;)
&#125;
<span class="hljs-comment">// 测试</span>
<span class="hljs-keyword">let</span> obj = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-string">'a'</span>,
    <span class="hljs-attr">gf</span>: &#123;
        <span class="hljs-attr">b</span>: <span class="hljs-string">'b'</span>,
        <span class="hljs-attr">f</span>: &#123;
            <span class="hljs-attr">c</span>: <span class="hljs-string">'c'</span>,
            <span class="hljs-attr">s</span>: &#123;
                <span class="hljs-attr">d</span>: <span class="hljs-string">'d'</span>
            &#125;
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">let</span> state = reactive(obj)
state.a = <span class="hljs-string">'1'</span>
state.gf.b = <span class="hljs-string">'2'</span>
state.gf.f.c = <span class="hljs-string">'3'</span>
state.gf.f.s.d = <span class="hljs-string">'4'</span>
<span class="hljs-built_in">console</span>.log(state)
<span class="hljs-comment">/*
更新UI界面
更新UI界面
更新UI界面
更新UI界面
&#123; a: '1', gf: &#123; b: '2', f: &#123; c: '3', s: [Object] &#125; &#125; &#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">ref</h3>
<blockquote>
<p>概念: 接受一个内部值并返回一个响应式且可变的 ref 对象。ref 对象具有指向内部值的单个 property <code>.value</code>。</p>
</blockquote>
<p>基于<code>reactive</code>就可以实现</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ref</span>(<span class="hljs-params">obj</span>)</span>&#123;
    <span class="hljs-keyword">return</span> reactive(&#123;
        <span class="hljs-attr">value</span>: obj
    &#125;)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span>(<span class="hljs-params">obj</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> obj === <span class="hljs-string">"object"</span>)&#123;
        <span class="hljs-keyword">if</span>(obj <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>)&#123;
            <span class="hljs-comment">// 如果是一个数组，取出数组中的每一元素，判断每一个元素是否又是一个对象</span>
            <span class="hljs-comment">// 如果又是一个对象需要包装成一个proxy</span>
            obj.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
                <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> item === <span class="hljs-string">"object"</span>)&#123;
                    obj[index] = reactive(item)
                &#125;
            &#125;)
        &#125;<span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 如果是一个对象取出对象属性的一个去吃没判断对象属性的取值也需要包装成Proxy</span>
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> obj) &#123;
                <span class="hljs-keyword">let</span> item = obj[key]
                <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> item === <span class="hljs-string">"object"</span>)&#123;
                    obj[key] = reactive(item)
                &#125;
            &#125;
        &#125;
    &#125;<span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">`<span class="hljs-subst">$&#123;obj&#125;</span> is not object`</span>)
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">obj, key</span>)</span>&#123;
            <span class="hljs-keyword">return</span> obj[key]
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">obj, key, value</span>)</span>&#123;
            obj[key] = value
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"更新UI界面"</span>)
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        &#125;
    &#125;)
&#125;
<span class="hljs-comment">// 测试</span>
<span class="hljs-keyword">let</span> obj = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-string">'a'</span>,
    <span class="hljs-attr">gf</span>: &#123;
        <span class="hljs-attr">b</span>: <span class="hljs-string">'b'</span>,
        <span class="hljs-attr">f</span>: &#123;
            <span class="hljs-attr">c</span>: <span class="hljs-string">'c'</span>,
            <span class="hljs-attr">s</span>: &#123;
                <span class="hljs-attr">d</span>: <span class="hljs-string">'d'</span>
            &#125;
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">let</span> state = ref(obj)
state.value.a = <span class="hljs-string">'1'</span>
state.value.gf.b = <span class="hljs-string">'2'</span>
state.value.gf.f.c = <span class="hljs-string">'3'</span>
state.value.gf.f.s.d = <span class="hljs-string">'4'</span>
<span class="hljs-built_in">console</span>.log(state)
<span class="hljs-comment">/*
更新UI界面
更新UI界面
更新UI界面
更新UI界面
&#123; value: &#123; a: '1', gf: &#123; b: '2', f: [Object] &#125; &#125; &#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">readonly</h3>
<blockquote>
<p>概念：接受一个对象 (响应式或纯对象) 或 <a href="https://v3.cn.vuejs.org/api/refs-api.html#ref" target="_blank" rel="nofollow noopener noreferrer">ref</a> 并返回原始对象的只读代理。只读代理是深层的：任何被访问的嵌套 property 也是只读的。</p>
</blockquote>
<p>其实想要设置只读操作很简单，我们只需要在Proxy的set方法不去设置值即可</p>
<p>代码实现:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">readonly</span>(<span class="hljs-params">obj</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> obj === <span class="hljs-string">"object"</span>)&#123;
        <span class="hljs-keyword">if</span>(obj <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>)&#123;
            <span class="hljs-comment">// 如果是一个数组，取出数组中的每一元素，判断每一个元素是否又是一个对象</span>
            <span class="hljs-comment">// 如果又是一个对象需要包装成一个proxy</span>
            obj.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
                <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> item === <span class="hljs-string">"object"</span>)&#123;
                    obj[index] = readonly(item)
                &#125;
            &#125;)
        &#125;<span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 如果是一个对象取出对象属性的一个去吃没判断对象属性的取值也需要包装成Proxy</span>
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> obj) &#123;
                <span class="hljs-keyword">let</span> item = obj[key]
                <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> item === <span class="hljs-string">"object"</span>)&#123;
                    obj[key] = readonly(item)
                &#125;
            &#125;
        &#125;
    &#125;<span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">`<span class="hljs-subst">$&#123;obj&#125;</span> is not object`</span>)
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">obj, key</span>)</span>&#123;
            <span class="hljs-keyword">return</span> obj[key]
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">obj, key, value</span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;key&#125;</span> 只读， 不能赋值`</span>)
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        &#125;
    &#125;)
&#125;
<span class="hljs-comment">// 测试</span>
<span class="hljs-keyword">let</span> obj = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-string">'a'</span>,
    <span class="hljs-attr">gf</span>: &#123;
        <span class="hljs-attr">b</span>: <span class="hljs-string">'b'</span>,
        <span class="hljs-attr">f</span>: &#123;
            <span class="hljs-attr">c</span>: <span class="hljs-string">'c'</span>,
            <span class="hljs-attr">s</span>: &#123;
                <span class="hljs-attr">d</span>: <span class="hljs-string">'d'</span>
            &#125;
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">let</span> state = readonly(obj)
state.a = <span class="hljs-string">'1'</span>
state.gf.b = <span class="hljs-string">'2'</span>
state.gf.f.c = <span class="hljs-string">'3'</span>
state.gf.f.s.d = <span class="hljs-string">'4'</span>
<span class="hljs-built_in">console</span>.log(state)
<span class="hljs-comment">/*
a 只读， 不能赋值
b 只读， 不能赋值
c 只读， 不能赋值
d 只读， 不能赋值
&#123; a: 'a', gf: &#123; b: 'b', f: &#123; c: 'c', s: [Object] &#125; &#125; &#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面所述基本就是Vue3.0响应式hooks基本的实现原理，具体Vue3.0是如何完成数据双向绑定，dom渲染算法，请移步 <a href="https://github.com/vuejs/vue-next" target="_blank" rel="nofollow noopener noreferrer">Vue3.0</a></p>
<p>响应式的对象创建已经完成了，那么如何判断这个响应式对象的是那种类型创建的？</p>
<p>Vue3.0也提供了<code>isRef, isReadonly,isReactive，isProxy</code>这些判断函数</p>
<p>我们也来简单的实现一下，实现这个钩子可能我们需要重写一下上面实现的reactive和ref</p>
<h3 data-id="heading-7">isRef</h3>
<blockquote>
<p>概念：检查值是否为一个 ref 对象。</p>
</blockquote>
<p>代码实现</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ref</span>(<span class="hljs-params">target</span>)</span>&#123;
    target = reactive(target);
  <span class="hljs-comment">// 这里我们需要重写对象的get，set方法，设置value的key</span>
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-comment">// 标识当前对象时ref对象</span>
        <span class="hljs-attr">_is_ref</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 保存target数据保存起来</span>
        <span class="hljs-attr">_value</span>: target,
        <span class="hljs-keyword">get</span> <span class="hljs-title">value</span>() &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'劫持得到了读取数据'</span>);
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._value
        &#125;,
        <span class="hljs-keyword">set</span> <span class="hljs-title">value</span>(<span class="hljs-params">value</span>) &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"劫持到了修改数据，"</span>,
                value);
            <span class="hljs-built_in">this</span>._value = value;
        &#125;
    &#125;

&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span>(<span class="hljs-params">obj</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> obj === <span class="hljs-string">"object"</span>)&#123;
        <span class="hljs-keyword">if</span>(obj <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>)&#123;
            <span class="hljs-comment">// 如果是一个数组，取出数组中的每一元素，判断每一个元素是否又是一个对象</span>
            <span class="hljs-comment">// 如果又是一个对象需要包装成一个proxy</span>
            obj.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
                <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> item === <span class="hljs-string">"object"</span>)&#123;
                    obj[index] = reactive(item)
                &#125;
            &#125;)
        &#125;<span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 如果是一个对象取出对象属性的一个去吃没判断对象属性的取值也需要包装成Proxy</span>
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> obj) &#123;
                <span class="hljs-keyword">let</span> item = obj[key]
                <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> item === <span class="hljs-string">"object"</span>)&#123;
                    obj[key] = reactive(item)
                &#125;
            &#125;
        &#125;
    &#125;<span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">`<span class="hljs-subst">$&#123;obj&#125;</span> is not object`</span>)
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">obj, key</span>)</span>&#123;
            <span class="hljs-keyword">return</span> obj[key]
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">obj, key, value</span>)</span>&#123;
            obj[key] = value
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"更新UI界面"</span>)
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        &#125;
    &#125;)
&#125;
<span class="hljs-comment">/**
 * 
 * 判断是否为ref
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>target 
 * <span class="hljs-doctag">@returns </span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isRef</span>(<span class="hljs-params">target</span>)</span>&#123;
    <span class="hljs-keyword">return</span> target && target._is_ref
&#125;
<span class="hljs-comment">// 测试</span>
<span class="hljs-keyword">let</span> obj = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-string">'a'</span>,
    <span class="hljs-attr">gf</span>: &#123;
        <span class="hljs-attr">b</span>: <span class="hljs-string">'b'</span>,
        <span class="hljs-attr">f</span>: &#123;
            <span class="hljs-attr">c</span>: <span class="hljs-string">'c'</span>,
            <span class="hljs-attr">s</span>: &#123;
                <span class="hljs-attr">d</span>: <span class="hljs-string">'d'</span>
            &#125;
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">let</span> state = ref(obj)
state.value.a = <span class="hljs-string">'1'</span>
state.value.gf.b = <span class="hljs-string">'2'</span>
state.value.gf.f.c = <span class="hljs-string">'3'</span>
state.value.gf.f.s.d = <span class="hljs-string">'4'</span>
<span class="hljs-built_in">console</span>.log(isRef(state))
<span class="hljs-comment">/*
劫持得到了读取数据
更新UI界面
劫持得到了读取数据
更新UI界面
劫持得到了读取数据
更新UI界面
劫持得到了读取数据
更新UI界面
true
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">isReadonly</h3>
<blockquote>
<p>概念：检查对象是否是由 <a href="https://v3.cn.vuejs.org/api/basic-reactivity.html#readonly" target="_blank" rel="nofollow noopener noreferrer"><code>readonly</code></a></p>
</blockquote>
<p>代码实现</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">readonly</span>(<span class="hljs-params">obj</span>)</span>&#123;
    <span class="hljs-comment">// obj._is_readonly = true 第一种方法</span>
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> obj === <span class="hljs-string">"object"</span>)&#123;
        <span class="hljs-keyword">if</span>(obj <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>)&#123;
            <span class="hljs-comment">// 如果是一个数组，取出数组中的每一元素，判断每一个元素是否又是一个对象</span>
            <span class="hljs-comment">// 如果又是一个对象需要包装成一个proxy</span>
            obj.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
                <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> item === <span class="hljs-string">"object"</span>)&#123;
                    obj[index] = readonly(item)
                &#125;
            &#125;)
        &#125;<span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 如果是一个对象取出对象属性的一个去吃没判断对象属性的取值也需要包装成Proxy</span>
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> obj) &#123;
                <span class="hljs-keyword">let</span> item = obj[key]
                <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> item === <span class="hljs-string">"object"</span>)&#123;
                    obj[key] = readonly(item)
                &#125;
            &#125;
        &#125;
    &#125;<span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">`<span class="hljs-subst">$&#123;obj&#125;</span> is not object`</span>)
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">obj, key</span>)</span>&#123;
            <span class="hljs-comment">// 第二种处理方式</span>
            <span class="hljs-keyword">if</span>(key === <span class="hljs-string">"_is_readonly"</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
            <span class="hljs-keyword">return</span> obj[key]
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">obj, key, value</span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;key&#125;</span> 只读`</span>)
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        &#125;
    &#125;)
&#125;
<span class="hljs-comment">/**
 * 
 * 判断是否为readonly
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>target 
 * <span class="hljs-doctag">@returns </span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isReadonly</span>(<span class="hljs-params">target</span>)</span>&#123;
    <span class="hljs-keyword">return</span> target && target._is_readonly
&#125;
<span class="hljs-comment">// 测试</span>
<span class="hljs-keyword">let</span> obj = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-string">'a'</span>,
    <span class="hljs-attr">gf</span>: &#123;
        <span class="hljs-attr">b</span>: <span class="hljs-string">'b'</span>,
        <span class="hljs-attr">f</span>: &#123;
            <span class="hljs-attr">c</span>: <span class="hljs-string">'c'</span>,
            <span class="hljs-attr">s</span>: &#123;
                <span class="hljs-attr">d</span>: <span class="hljs-string">'d'</span>
            &#125;
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">let</span> state = readonly(obj)
state.a = <span class="hljs-string">'1'</span>
state.gf.b = <span class="hljs-string">'2'</span>
state.gf.f.c = <span class="hljs-string">'3'</span>
state.gf.f.s.d = <span class="hljs-string">'4'</span>
<span class="hljs-built_in">console</span>.log(state)
<span class="hljs-built_in">console</span>.log(isReadonly(state.gf))
<span class="hljs-comment">/*
a 只读
b 只读
c 只读
d 只读
&#123; a: 'a', gf: &#123; b: 'b', f: &#123; c: 'c', s: [Object] &#125; &#125; &#125;
true
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">isReactive</h3>
<blockquote>
<p>概念：检查对象是否是由 <a href="https://v3.cn.vuejs.org/api/basic-reactivity.html#reactive" target="_blank" rel="nofollow noopener noreferrer"><code>reactive</code></a></p>
</blockquote>
<p>代码实现</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span>(<span class="hljs-params">obj</span>)</span>&#123;    <span class="hljs-comment">// obj._is_reactive = true 这是一种方法    if(typeof obj === "object")&#123;        if(obj instanceof Array)&#123;            // 如果是一个数组，取出数组中的每一元素，判断每一个元素是否又是一个对象            // 如果又是一个对象需要包装成一个proxy            obj.forEach((item, index) => &#123;                if(typeof item === "object")&#123;                    obj[index] = reactive(item)                &#125;            &#125;)        &#125;else &#123;            // 如果是一个对象取出对象属性的一个去吃没判断对象属性的取值也需要包装成Proxy            for (const key in obj) &#123;                let item = obj[key]                if(typeof item === "object")&#123;                    obj[key] = reactive(item)                &#125;            &#125;        &#125;    &#125;else &#123;        console.warn(`$&#123;obj&#125; is not object`)    &#125;    return new Proxy(obj, &#123;        get(obj, key)&#123;            // 这种第二种方法            if(key === "_is_reactive") return true            return obj[key]        &#125;,        set(obj, key, value)&#123;            obj[key] = value            console.log("更新UI界面")            return true        &#125;    &#125;)&#125;/** *  * 判断是否为reactive * @param &#123;*&#125; target  * @returns  */function isReactive(target)&#123;    return target && target._is_reactive&#125;// 测试let obj = &#123;    a: 'a',    gf: &#123;        b: 'b',        f: &#123;            c: 'c',            s: &#123;                d: 'd'            &#125;        &#125;    &#125;&#125;let state = reactive(obj)state.a = '1'state.gf.b = '2'state.gf.f.c = '3'state.gf.f.s.d = '4'console.log(isReactive(state.gf))/*更新UI界面更新UI界面更新UI界面更新UI界面true*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">isProxy</h3>
<blockquote>
<p>概念：检查对象是否是由 <a href="https://v3.cn.vuejs.org/api/basic-reactivity.html#reactive" target="_blank" rel="nofollow noopener noreferrer"><code>reactive</code></a> 或 <a href="https://v3.cn.vuejs.org/api/basic-reactivity.html#readonly" target="_blank" rel="nofollow noopener noreferrer"><code>readonly</code></a> 创建的 proxy。</p>
</blockquote>
<p>代码实现</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span>(<span class="hljs-params">obj</span>)</span>&#123;    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> obj === <span class="hljs-string">"object"</span>)&#123;        <span class="hljs-keyword">if</span>(obj <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>)&#123;            <span class="hljs-comment">// 如果是一个数组，取出数组中的每一元素，判断每一个元素是否又是一个对象            // 如果又是一个对象需要包装成一个proxy            obj.forEach((item, index) => &#123;                if(typeof item === "object")&#123;                    obj[index] = reactive(item)                &#125;            &#125;)        &#125;else &#123;            // 如果是一个对象取出对象属性的一个去吃没判断对象属性的取值也需要包装成Proxy            for (const key in obj) &#123;                let item = obj[key]                if(typeof item === "object")&#123;                    obj[key] = reactive(item)                &#125;            &#125;        &#125;    &#125;else &#123;        console.warn(`$&#123;obj&#125; is not object`)    &#125;    obj._is_reactive = true    return new Proxy(obj, &#123;        get(obj, key)&#123;            return obj[key]        &#125;,        set(obj, key, value)&#123;            obj[key] = value            console.log("更新UI界面")            return true        &#125;    &#125;)&#125;/** *  * 判断是否为reactive * @param &#123;*&#125; target  * @returns  */function isReactive(target)&#123;    return target && target._is_reactive&#125;/** *  * 判断是否为readonly * @param &#123;*&#125; target  * @returns  */ function isReadonly(target)&#123;    return target && target._is_readonly&#125;function readonly(obj)&#123;    if(typeof obj === "object")&#123;        if(obj instanceof Array)&#123;            // 如果是一个数组，取出数组中的每一元素，判断每一个元素是否又是一个对象            // 如果又是一个对象需要包装成一个proxy            obj.forEach((item, index) => &#123;                if(typeof item === "object")&#123;                    obj[index] = reactive(item)                &#125;            &#125;)        &#125;else &#123;            // 如果是一个对象取出对象属性的一个去吃没判断对象属性的取值也需要包装成Proxy            for (const key in obj) &#123;                let item = obj[key]                if(typeof item === "object")&#123;                    obj[key] = reactive(item)                &#125;            &#125;        &#125;    &#125;else &#123;        console.warn(`$&#123;obj&#125; is not object`)    &#125;    return new Proxy(obj, &#123;        get(obj, key)&#123;            if(key === "_is_readonly") return true            return obj[key]        &#125;,        set(obj, key, value)&#123;            console.log(`$&#123;key&#125; 只读， 不能赋值`)            return true        &#125;    &#125;)&#125;function isProxy(target)&#123;    return isReactive(target) || isReadonly(target)&#125;// 测试let obj = &#123;    a: 'a',    gf: &#123;        b: 'b',        f: &#123;            c: 'c',            s: &#123;                d: 'd'            &#125;        &#125;    &#125;&#125;let state = readonly(obj)state.a = '1'state.gf.b = '2'state.gf.f.c = '3'state.gf.f.s.d = '4'console.log(isProxy(state.gf))</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就是Vue3.0核心响应式对象创建和判断的方法了，关于Raw相关实现，比较简单就是保留了一份原始对象数据，具体实现后续会更新哈:face_with_thermometer:</p>
<blockquote>
<p>总结：听完VueConf大会尤大神对Vue3.0的解析，我才觉得自己对Vue3.0的理解还是比较浅薄的，关于上面代码实现基本结合尤大神的思想和Proxy的原理从零实现，也会完成自己手动封装一个类Vue的框架</p>
</blockquote></div>  
</div>
            