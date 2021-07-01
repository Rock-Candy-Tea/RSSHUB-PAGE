
---
title: '浅谈ES6的Proxy'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8922'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 21:53:02 GMT
thumbnail: 'https://picsum.photos/400/300?random=8922'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">创建一个简单的Proxy</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> target = &#123;&#125;
<span class="hljs-keyword">let</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, &#123;&#125;)

proxy.name = <span class="hljs-string">'proxy'</span>

<span class="hljs-built_in">console</span>.log(proxy.name) <span class="hljs-comment">// proxy</span>
<span class="hljs-built_in">console</span>.log(target.name) <span class="hljs-comment">// proxy</span>

target.name = <span class="hljs-string">'target'</span>

<span class="hljs-built_in">console</span>.log(proxy.name) <span class="hljs-comment">// target</span>
<span class="hljs-built_in">console</span>.log(target.name) <span class="hljs-comment">// target</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个实例将"proxy"赋值给proxy.name属性时会在目标上创建name,代理只是简单的将操作转发给目标，他不会储存这个属性。相当于proxy.name和target.name引用的都是target.name的值。</p>
<h2 data-id="heading-1">使用set陷阱验证属性</h2>
<p>set陷阱接收四个参数：</p>
<p>1.trapTarget：用于接收属性（代理的目标）的对象</p>
<p>2.key：要写入的属性键（字符串或者symbol）</p>
<p>3.value：被写入的属性值</p>
<p>4.receiver：操作发生的对象（通常是代理）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> target = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"target"</span>
&#125;

<span class="hljs-keyword">let</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, &#123;
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">trapTarget, key, value, receiver</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (!trapTarget.hasOwnProperty(key)) &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">isNaN</span>(value)) &#123;
                <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"属性必须时数字"</span>)
            &#125;
        &#125;

        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.set(trapTarget, key, value, receiver)
    &#125;
&#125;)

proxy.count = <span class="hljs-number">1</span>
<span class="hljs-built_in">console</span>.log(proxy.count) <span class="hljs-comment">//1</span>
<span class="hljs-built_in">console</span>.log(target.count) <span class="hljs-comment">//1</span>

proxy.name = <span class="hljs-string">"proxy"</span>

<span class="hljs-built_in">console</span>.log(proxy.name) <span class="hljs-comment">//proxy</span>
<span class="hljs-built_in">console</span>.log(target.name) <span class="hljs-comment">//proxy</span>

proxy.other = <span class="hljs-string">"other"</span> <span class="hljs-comment">// 这里会报错因为不数字</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个实例每次在外面改变proxy的值时就会出发set函数。</p>
<h2 data-id="heading-2">用get陷阱验证对象结构</h2>
<p>get接收3个参数</p>
<p>1.trapTarget：用于接收属性（代理的目标）的对象</p>
<p>2.key：要写入的属性键（字符串或者symbol）</p>
<p>3.receiver：操作发生的对象（通常是代理）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(&#123;&#125;, &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">trapTarget, key, receiver</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (!(key <span class="hljs-keyword">in</span> receiver)) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"属性"</span> + key + <span class="hljs-string">"不存在"</span>)
        &#125;

        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.get(trapTarget, key, receiver)
    &#125;
&#125;)

proxy.name = <span class="hljs-string">"proxy"</span>

<span class="hljs-built_in">console</span>.log(proxy.name) <span class="hljs-comment">//proxy</span>

<span class="hljs-built_in">console</span>.log(proxy.age) <span class="hljs-comment">// 属性不存在会抛出错误</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们访问proxy创建的对象属性时就会触发get方法</p>
<h2 data-id="heading-3">使用has陷阱因此已有属性</h2>
<p>has接收2个参数：</p>
<p>1.trapTarget：用于接收属性（代理的目标）的对象</p>
<p>2.key：要写入的属性键（字符串或者symbol）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> target = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"target"</span>,
    <span class="hljs-attr">value</span>: <span class="hljs-number">42</span>
&#125;

<span class="hljs-keyword">let</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, &#123;
    <span class="hljs-function"><span class="hljs-title">has</span>(<span class="hljs-params">trapTarget, key</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'value'</span>) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.has(trapTarget, key)
        &#125;
    &#125;
&#125;)


<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"value"</span> <span class="hljs-keyword">in</span> proxy) <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"name"</span> <span class="hljs-keyword">in</span> proxy) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"toString"</span> <span class="hljs-keyword">in</span> proxy) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每当我们判断proxy中是否含有属性时会出发has函数</p>
<h2 data-id="heading-4">用deleteProperty陷阱防止删除属性</h2>
<p>deleteProperty接收2个参数：</p>
<p>1.trapTarget：用于接收属性（代理的目标）的对象</p>
<p>2.key：要写入的属性键（字符串或者symbol）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> target = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"target"</span>,
    <span class="hljs-attr">value</span>: <span class="hljs-number">42</span>
&#125;

<span class="hljs-keyword">let</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(traget, &#123;
    <span class="hljs-function"><span class="hljs-title">deleteProperty</span>(<span class="hljs-params">trapTarget, key</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (key === <span class="hljs-string">"value"</span>) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.deleteProperty(trapTarget, key)
        &#125;
    &#125;
&#125;)


<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"value"</span> <span class="hljs-keyword">in</span> proxy) <span class="hljs-comment">// true</span>

<span class="hljs-keyword">let</span> result1 = <span class="hljs-keyword">delete</span> proxy.value

<span class="hljs-built_in">console</span>.log(result1) <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"value"</span> <span class="hljs-keyword">in</span> proxy) <span class="hljs-comment">// true</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"name"</span> <span class="hljs-keyword">in</span> proxy) <span class="hljs-comment">// true</span>

<span class="hljs-keyword">let</span> result2 = <span class="hljs-keyword">delete</span> proxy.name
<span class="hljs-built_in">console</span>.log(result2) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"name"</span> <span class="hljs-keyword">in</span> proxy) <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当外部要删除proxy的属性就会触发deleteProperty函数</p>
<h2 data-id="heading-5">原型代理陷阱(setProptotypeOf,getPrototypeOf)</h2>
<p>setProptotypeOf接收2个参数</p>
<p>1.trapTarget：用于接收属性（代理的目标）的对象</p>
<p>2.proto：作为原型使用的对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> target = &#123;&#125;

<span class="hljs-keyword">let</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, &#123;

    <span class="hljs-comment">// 访问时调用</span>
    <span class="hljs-function"><span class="hljs-title">getPrototypeOf</span>(<span class="hljs-params">trapTarget</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
    &#125;,
    <span class="hljs-comment">// 改变时调用</span>
    <span class="hljs-function"><span class="hljs-title">setPrototypeOf</span>(<span class="hljs-params">trapTarget, proto</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    &#125;

&#125;)

<span class="hljs-keyword">let</span> targetProto = <span class="hljs-built_in">Object</span>.getPrototypeOf(target)
<span class="hljs-keyword">let</span> proxyProto = <span class="hljs-built_in">Object</span>.getPrototypeOf(proxy)

<span class="hljs-built_in">console</span>.log(targetProto === <span class="hljs-built_in">Object</span>.prototype) <span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(proxyProto === <span class="hljs-built_in">Object</span>.prototype) <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(proxyProto) <span class="hljs-comment">// null</span>

<span class="hljs-built_in">Object</span>.setPrototypeOf(target, &#123;&#125;) <span class="hljs-comment">// 成功</span>

<span class="hljs-built_in">Object</span>.setPrototypeOf(proxy, &#123;&#125;) <span class="hljs-comment">// 抛出错误</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果正常实现</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> target = &#123;&#125;

<span class="hljs-keyword">let</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, &#123;

    <span class="hljs-comment">// 访问时调用</span>
    <span class="hljs-function"><span class="hljs-title">getPrototypeOf</span>(<span class="hljs-params">trapTarget</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.getPrototypeOf(trapTarget)
    &#125;,
    <span class="hljs-comment">// 改变时调用</span>
    <span class="hljs-function"><span class="hljs-title">setPrototypeOf</span>(<span class="hljs-params">trapTarget, proto</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.setPrototypeOf(trapTarget, proto)
    &#125;

&#125;)

<span class="hljs-keyword">let</span> targetProto = <span class="hljs-built_in">Object</span>.getPrototypeOf(target)
<span class="hljs-keyword">let</span> proxyProto = <span class="hljs-built_in">Object</span>.getPrototypeOf(proxy)

<span class="hljs-built_in">console</span>.log(targetProto === <span class="hljs-built_in">Object</span>.prototype) <span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(proxyProto === <span class="hljs-built_in">Object</span>.prototype) <span class="hljs-comment">// true</span>

<span class="hljs-built_in">Object</span>.setPrototypeOf(target, &#123;&#125;) <span class="hljs-comment">// 成功</span>

<span class="hljs-built_in">Object</span>.setPrototypeOf(proxy, &#123;&#125;) <span class="hljs-comment">// 成功</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">属性描述符陷阱</h2>
<p>defineProperty接收三个参数：</p>
<p>1.trapTarget：用于接收属性（代理的目标）的对象</p>
<p>2.key：要写入的属性键（字符串或者symbol）</p>
<p>3.descriptor：属性的描述对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(&#123;&#125;, &#123;
    <span class="hljs-function"><span class="hljs-title">defineProperty</span>(<span class="hljs-params">trapTarget, key, descriptor</span>)</span> &#123; <span class="hljs-comment">// descriptor 只能接收enumerable, configurable, value, writeable, get, set </span>
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> key === <span class="hljs-string">"symbol"</span>) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.defineProperty(trapTarget, key, descriptor)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">getOwnPropertyDescriptor</span>(<span class="hljs-params">trapTarget, key</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.getOwnPropertyDescriptor(trapTarget, key)
    &#125;
&#125;)

<span class="hljs-built_in">Object</span>.defineProperty(proxy, <span class="hljs-string">"name"</span>, &#123;
    <span class="hljs-attr">value</span>: <span class="hljs-string">"proxy"</span>
&#125;)

<span class="hljs-built_in">console</span>.log(proxy.name) <span class="hljs-comment">//proxy</span>

<span class="hljs-keyword">let</span> nameSymbol = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"name"</span>)

<span class="hljs-built_in">Object</span>.defineProperty(proxy, nameSymbol, &#123;
    <span class="hljs-attr">value</span>: <span class="hljs-string">"proxy"</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在外部调用defineProperty | getOwnPropertyDescriptor时会触发内部definenProperty | getOwnPropertyDescriptor方法。</p>
<h2 data-id="heading-7">ownKeys陷阱</h2>
<p>ownKeys陷阱会拦截外部的Object.keys()，Object.getOwnPropertyName(),Object.getOwnPropertySymbols()和Object.assign()四个方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(&#123;&#125;, &#123;
    <span class="hljs-function"><span class="hljs-title">ownKeys</span>(<span class="hljs-params">trapTarget</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.ownKeys(trapTarget).filter(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> key !== <span class="hljs-string">"string"</span> || key[<span class="hljs-number">0</span>] !== <span class="hljs-string">'_'</span>
        &#125;)
    &#125;
&#125;)

<span class="hljs-keyword">let</span> nameSymbol = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"name"</span>)

proxy.name = <span class="hljs-string">"proxy"</span>

proxy._name = <span class="hljs-string">"private"</span>

proxy[nameSymbol] = <span class="hljs-string">"symbol"</span>

<span class="hljs-keyword">let</span> names = <span class="hljs-built_in">Object</span>.getOwnPropertyNames(proxy),
    keys = <span class="hljs-built_in">Object</span>.keys(proxy),
    symbols = <span class="hljs-built_in">Object</span>.getOwnPropertySymbols(proxy)

<span class="hljs-built_in">console</span>.log(names.length) <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(names) <span class="hljs-comment">// name</span>

<span class="hljs-built_in">console</span>.log(keys.length) <span class="hljs-comment">//1</span>
<span class="hljs-built_in">console</span>.log(keys[<span class="hljs-number">0</span>]) <span class="hljs-comment">// name</span>

<span class="hljs-built_in">console</span>.log(symbols.length) <span class="hljs-comment">//1</span>
<span class="hljs-built_in">console</span>.log(symbols[<span class="hljs-number">0</span>]) <span class="hljs-comment">// symbol(name)</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            