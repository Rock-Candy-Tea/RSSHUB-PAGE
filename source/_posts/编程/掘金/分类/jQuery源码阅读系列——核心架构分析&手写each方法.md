
---
title: 'jQuery源码阅读系列——核心架构分析&手写each方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/708cd52619d946dabff53cf126c9f64d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 17 Apr 2021 19:39:24 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/708cd52619d946dabff53cf126c9f64d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前几篇文章记录了导出问题和其中一点的数据类型判断的封装问题。</p>
<p>这次对jQuery核心架构简单分析，以此学习面向对象和插件封装的知识。</p>
<h2 data-id="heading-0">使用其他原型上的方法</h2>
<p>我们想使用其他类原型上的方法，例如数组 <code>push</code> ，有两种方式，：</p>
<ul>
<li>类似 <code>[].push.call(实例)</code> ，使用 <code>call</code> 改变内部 <code>this</code> 指向</li>
<li>或者 <code>jQuery.prototype.push = arr.push</code></li>
</ul>
<p>jQuery就是这样，取到数组原型上的对应方法，然后放到自己的原型上，这样就可以使用别的原型上提供的公用方法。</p>
<p>这样实例通过原型链找到所属类原型上为其提供的公共属性和方法的时候，就可以使用到别的类的方法，我们把这种借用的方式称作鸭子类型，如下：</p>
<pre><code class="hljs language-js copyable" lang="js">
(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-meta">    "use strict"</span>;
    <span class="hljs-keyword">var</span> arr = [];
    <span class="hljs-keyword">var</span> slice = arr.slice;<span class="hljs-comment">//取到数组原型上的对应方法</span>
    <span class="hljs-keyword">var</span> push = arr.push;
    <span class="hljs-keyword">var</span> indexOf = arr.indexOf;

    <span class="hljs-comment">// =======</span>
    <span class="hljs-keyword">var</span> version = <span class="hljs-string">"3.5.1"</span>,
        jQuery = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">jQuery</span>(<span class="hljs-params">selector, context</span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> jQuery.fn.init(selector, context);
        &#125;;
    jQuery.fn = jQuery.prototype = &#123;
        <span class="hljs-attr">constructor</span>: jQuery,<span class="hljs-comment">//原型重定向,防止没有constructor</span>
        <span class="hljs-attr">jquery</span>: version,
        <span class="hljs-attr">length</span>: <span class="hljs-number">0</span>,
        <span class="hljs-comment">// 鸭子类型把数组原型上的这些方法放到jQuery的原型上,这样就可以使用别的原型上提供的方法,</span>
        <span class="hljs-comment">//类似[].slice.call(实例),或者像下面这种方法jQuery.push = arr.push ,这样也可以用</span>
        <span class="hljs-attr">push</span>: push,
        <span class="hljs-attr">sort</span>: arr.sort,
        <span class="hljs-attr">splice</span>: arr.splice,
       
    <span class="hljs-built_in">window</span>.jQuery = <span class="hljs-built_in">window</span>.$ = jQuery;
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">面向对象</h2>
<p>jQuery在使用的时候，基本都是 <code>$('.box)</code> 这样使用，那么他是如何将构造函数当做普通函数执行，却又返回了其实例对象的呢？我们来分析一下</p>
<p>代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-meta">    "use strict"</span>;
    <span class="hljs-keyword">var</span> version = <span class="hljs-string">"3.5.1"</span>,
        jQuery = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">jQuery</span>(<span class="hljs-params">selector, context</span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> jQuery.fn.init(selector, context);
        &#125;;
    jQuery.fn = jQuery.prototype = &#123;
        <span class="hljs-attr">constructor</span>: jQuery,
        <span class="hljs-attr">jquery</span>: version,
        <span class="hljs-attr">length</span>: <span class="hljs-number">0</span>,
    &#125;;
    
    <span class="hljs-keyword">var</span> init = jQuery.fn.init = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">init</span>(<span class="hljs-params">selector, context, root</span>) </span>&#123;
        <span class="hljs-comment">//...</span>
        &#125;;
    init.prototype = jQuery.fn;
    <span class="hljs-comment">//...</span>
    <span class="hljs-built_in">window</span>.jQuery = <span class="hljs-built_in">window</span>.$ = jQuery;
&#125;)();

<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>$([selector])</code> 方法，过程如下</p>
<ol>
<li>相当于执行 <code>new jQuery.fn.init(selector, context);</code> ，返回的是 <code>init</code>  方法（类）的实例，假设这个实例是 <code>A</code></li>
<li>那么： 可以得出 <code>A.__proto__===init.prototype</code></li>
<li>又由代码可以得知 <code>init.prototype</code>  =>  <code>jQuery.fn</code>  =>  <code>jQuery.prototype</code> ，让 <code>init</code> 的原型重定向为jQuery的原型，所以最终执行 <code>new init</code> 相当于执行了 <code>new jQuery</code></li>
<li>所以 <code>A.__proto__===jQuery.prototype</code></li>
</ol>
<p>总结：基于JQ选择器 <code>$(...)</code> 、 <code>jQuery(...)</code> 获取的是 <code>jQuery</code> 类的实例</p>
<ul>
<li>目的：让用户使用的时候把 <code>jQuery</code> /  <code>$</code> 当做普通函数执行，但是最后的结果是创造其类的一个实例，用户使用起来方便</li>
<li>这种处理模式的思想其实就是<strong>工厂设计模式</strong></li>
</ul>
<p><img alt="image。png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/708cd52619d946dabff53cf126c9f64d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>有一个面试题：不使用 <code>new</code> 操作符，是否可以创造当前函数的实例？上面就是例子，核心原理就是使用 <code>jQuery.fn</code> 做一个原型的中转</p>
<p>额外补充另外一种不基于 <code>new</code> 执行函数，也可以创在构造函数实例的情况：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
fn.prototype.x = <span class="hljs-number">100</span>;
<span class="hljs-keyword">let</span> f = fn();
<span class="hljs-comment">// f.__proto__===fn.prototype  f也是fn的一个实例（这也是另外一种不基于new执行函数，也可以创在构造函数实例的情况） </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2"><code>init</code> 构造函数中的逻辑</h2>
<p>函数 <code>init</code> 传入三个参数，其中 <code>selector</code> 可以传入不同的参数种类，我们分类讨论</p>
<p><code>jQuery.fn.init</code> 中传入了 <code>selector</code> ，  <code>context</code> 两个参数，对应着jQuery的用法</p>
<ul>
<li><code>$('.box')</code>   在整个文档中找到拥有 <code>'box'</code> 样式类的</li>
<li><code>$('#commHead .box')</code>  在ID为 <code>'commHead'</code> 的容器中，找到拥有box样式类的（后代查找）</li>
<li><code>$('.box',document.getElementById('commHead'))</code>  和上面一个意思</li>
</ul>
<h3 data-id="heading-3">如果传入的是DOM</h3>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-meta">    "use strict"</span>;
    <span class="hljs-comment">//...</span>

    <span class="hljs-keyword">var</span> version = <span class="hljs-string">"3.5.1"</span>,
        jQuery = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">jQuery</span>(<span class="hljs-params">selector, context</span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> jQuery.fn.init(selector, context);
        &#125;;
    jQuery.fn = jQuery.prototype = &#123;
       <span class="hljs-comment">//...</span>
        <span class="hljs-attr">length</span>: <span class="hljs-number">0</span>,
    &#125;;
    <span class="hljs-keyword">var</span> rootjQuery = jQuery(<span class="hljs-built_in">document</span>),
        init = jQuery.fn.init = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">init</span>(<span class="hljs-params">selector, context, root</span>) </span>&#123;
            <span class="hljs-keyword">var</span> match, elem;
            <span class="hljs-comment">// 处理: $(""), $(null), $(undefined), $(false)  返回空的JQ对象</span>
            <span class="hljs-keyword">if</span> (!selector) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
            root = root || rootjQuery;
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> selector === <span class="hljs-string">"string"</span>) &#123;
               <span class="hljs-comment">//...</span>
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (selector.nodeType) &#123;
                <span class="hljs-comment">// 传递的是一个原生的DOM/JS对象：把DOM对象转换为JQ对象“这样就可以使用JQ原型上提供的方法”</span>
                <span class="hljs-built_in">this</span>[<span class="hljs-number">0</span>] = selector;
                <span class="hljs-built_in">this</span>.length = <span class="hljs-number">1</span>;
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isFunction(selector)) &#123;
             <span class="hljs-comment">//...</span>
            &#125;
        &#125;;
    init.prototype = jQuery.fn;

    <span class="hljs-built_in">window</span>.jQuery = <span class="hljs-built_in">window</span>.$ = jQuery;
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>
<p><code>if (!selector) return this;</code> 处理为： <code>$("")</code> ， <code>$(null)</code> ，  <code>$(undefined)</code> ，  <code>$(false)</code>   返回空的JQ对象，仅有 <code>__proto__</code> 上有公共方法</p>
</li>
<li>
<p><code>typeof selector === "string"</code> 是一种关于传入字符串选择器的处理，这里逻辑比较复杂，先跳过这一块</p>
</li>
<li>
<p><code>selector.nodeType</code> 处理：当传入的是DOM对象时，把DOM对象放到属性 <code>[0]</code> 上，相当于在DOM对象上包裹一层，并返回一个jQ对象的伪数组，每一个数字属性，就是一个DOM对象。</p>
<p><img alt="image。png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8d181a546c9480889f3a51545298098~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ol>
<p>这里区分一下“JQ对象” 和 “DOM对象”
“JQ对象” ：JQ实例对象“也就是基于选择器获取的结果”  ，一般返回的是一个类数组集合，拥有索引和 <code>length</code> 等属性，
“DOM/JS对象”： 基于浏览器内置的方法获取的元素对象“他们是浏览器内置类的相关实例对象”</p>
<ul>
<li>“DOM对象”转化为“JQ对象” ：  <code>$(“DOM对象”)</code></li>
<li>“JQ对象”获取“DOM对象” ： 使用 <code>JQ对象[索引]</code>  或  <code>JQ对象.get(索引)</code>   使用内置类原型上的方法</li>
</ul>
<h3 data-id="heading-4">原型上方法   <code>get</code>  VS  <code>eq</code></h3>
<p><code>get</code> 是拿到其DOM对象， <code>eq</code> 返回的是jQuery对象</p>
<p><code>get</code> 原理是，如果什么都不传，先把“JQ对象”类数组集合转化为数组集合（ <code>slice.call(this)</code> ），然后如果传了索引就根据索引获取其DOM值，具体逻辑可以看代码的注视</p>
<p><code>eq</code> 也是基于索引查找JQ对象集合中的某一项，但是最后返回的不是“DOM对象”，而是一个新的“JQ对象”具体如下，一点点分析</p>
<ol>
<li>先执行 <code>eq()</code> ，支持负数索引</li>
<li>eq返回 <code>pushStack()</code> 的执行结果，这个执行结果是空的JQ对象，并把 <code>eq()</code> 函数传入的索引的那个DOM对象作为0属性，相当于重新返回一个新的jq对象，仅包含eq的索引那个DOM值</li>
<li><code>pushStack()</code> 具体实现是基于 <code>merge</code> 方法，拼接伪数组，将空的JQ对象（ <code>length</code> 为0）和长度为1的DOM对象组合在一起然后返回</li>
<li><code>merge</code> 要注意的是，他传递两个集合，把第二个集合中的每一项全部放置到第一个集合的末尾，既合并两个集合，返回的是第一个集合。类似于数组的 <code>concat</code> ，但是 <code>concat</code> 只能数组使用， <code>merge</code> 方法可以支持类数组集合的处理</li>
<li>注意 <code>pushStack</code> 还返回了 <code>prevObject</code> 属性，代码中可以看到，这是使用eq后，原来的根JQ对象，在链式调用中，可以快速回到原始操作的JQ对象。例如 <code>$('body').prev().addClass('xxx').prevObject.addClass('clearfix')</code></li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-meta">    "use strict"</span>;
    <span class="hljs-keyword">var</span> arr = [];
    <span class="hljs-keyword">var</span> slice = arr.slice;<span class="hljs-comment">//取到数组原型上的对应方法</span>
    <span class="hljs-keyword">var</span> push = arr.push;

    <span class="hljs-comment">// =======</span>
    <span class="hljs-keyword">var</span> version = <span class="hljs-string">"3.5.1"</span>,
        jQuery = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">jQuery</span>(<span class="hljs-params">selector, context</span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> jQuery.fn.init(selector, context);
        &#125;;
    jQuery.fn = jQuery.prototype = &#123;
        <span class="hljs-attr">constructor</span>: jQuery,
        <span class="hljs-attr">jquery</span>: version,
        <span class="hljs-attr">length</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">push</span>: push,
        <span class="hljs-comment">// 基于索引把“JQ对象”转换为“DOM对象”</span>
        <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">num</span>) </span>&#123;
            <span class="hljs-comment">// 把“JQ对象”类数组集合转化为数组集合</span>
            <span class="hljs-keyword">if</span> (num == <span class="hljs-literal">null</span>) <span class="hljs-keyword">return</span> slice.call(<span class="hljs-built_in">this</span>);
            <span class="hljs-comment">// 支持负数作为索引</span>
            <span class="hljs-keyword">return</span> num < <span class="hljs-number">0</span> ? <span class="hljs-built_in">this</span>[num + <span class="hljs-built_in">this</span>.length] : <span class="hljs-built_in">this</span>[num];
        &#125;,
        <span class="hljs-comment">// 也是基于索引查找JQ对象集合中的某一项，但是最后返回的不是“DOM对象”，而是一个新的“JQ对象”</span>
        <span class="hljs-attr">eq</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">i</span>) </span>&#123;
            <span class="hljs-comment">// 支持负数作为索引</span>
            <span class="hljs-keyword">var</span> len = <span class="hljs-built_in">this</span>.length,
                j = +i + (i < <span class="hljs-number">0</span> ? len : <span class="hljs-number">0</span>);
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.pushStack(j >= <span class="hljs-number">0</span> && j < len ? [<span class="hljs-built_in">this</span>[j]] : []);
        &#125;,
        <span class="hljs-attr">pushStack</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">elems</span>) </span>&#123;
            <span class="hljs-comment">// this.constructor->jQuery => jQuery() => 空的JQ对象</span>
            <span class="hljs-keyword">var</span> ret = jQuery.merge(<span class="hljs-built_in">this</span>.constructor(), elems);
            <span class="hljs-comment">// prevObject:在链式调用中，可以快速回到原始操作的JQ对象（根JQ对象）</span>
            ret.prevObject = <span class="hljs-built_in">this</span>;
            <span class="hljs-keyword">return</span> ret;
        &#125;,
    &#125;;
    
    <span class="hljs-comment">// 传递两个集合，把第二个集合中的每一项全部放置到第一个集合的末尾“合并两个集合”，返回的是第一个集合</span>
    <span class="hljs-comment">//   + 类似于数组的concat，但是这个只能数组使用</span>
    <span class="hljs-comment">//   + merge方法可以支持类数组集合的处理</span>
    jQuery.merge = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">merge</span>(<span class="hljs-params">first, second</span>) </span>&#123;
        <span class="hljs-keyword">var</span> len = +second.length,
            j = <span class="hljs-number">0</span>,
            i = first.length;
        <span class="hljs-keyword">for</span> (; j < len; j++) &#123;
            first[i++] = second[j];
        &#125;
        first.length = i;
        <span class="hljs-keyword">return</span> first;
    &#125;;

    <span class="hljs-comment">// =======</span>
      <span class="hljs-keyword">var</span>  init = jQuery.fn.init = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">init</span>(<span class="hljs-params">selector, context, root</span>) </span>&#123;
            <span class="hljs-keyword">var</span> match, elem;
            <span class="hljs-comment">// 处理: $(""), $(null), $(undefined), $(false)  返回空的JQ对象</span>
            <span class="hljs-keyword">if</span> (!selector) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> selector === <span class="hljs-string">"string"</span>) &#123;
               /...
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (selector.nodeType) &#123;
                <span class="hljs-comment">// 传递的是一个原生的DOM/JS对象：把DOM对象转换为JQ对象“这样就可以使用JQ原型上提供的方法”</span>
                <span class="hljs-built_in">this</span>[<span class="hljs-number">0</span>] = selector;
                <span class="hljs-built_in">this</span>.length = <span class="hljs-number">1</span>;
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isFunction(selector)) &#123;
              <span class="hljs-comment">//...</span>
            &#125;
            <span class="hljs-comment">//...</span>
        &#125;;
    init.prototype = jQuery.fn;
    <span class="hljs-built_in">window</span>.jQuery = <span class="hljs-built_in">window</span>.$ = jQuery;
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image。png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40bb2f77e493488b8eb1af5a8d6bb7d5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">如果传入的是函数</h3>
<p>如果传入函数，即 <code>$(function ()&#123;&#125;)</code> ，通过以下代码可以看出</p>
<p><code>var rootjQuery = jQuery(document)</code> => <code>root = root || rootjQuery;</code>
再到下面返回值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">return</span> root.ready !== <span class="hljs-literal">undefined</span> ?
                    root.ready(selector) :
                    selector(jQuery);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>即
<code>$(function ()&#123;&#125;)</code> 相当于执行了 <code>$(document).ready(function ()&#123;&#125;)</code></p>
<p><code>ready</code> 函数操作为： <code>readyList</code> 返回一个 <code>promise</code> ， <code>resolve</code> 之后，才执行传进去的函数</p>
<p><code>readyList</code> 做了什么呢？因为这部分代码过于分散和跳跃，就不粘贴了，说一下原理：</p>
<p><code>readyList</code> 里，监听 <code>'DOMContentLoaded'</code> 事件，在此事件触发时， <code>resolve</code> promise。</p>
<p><code>'DOMContentLoaded'</code> 是等待页面中的<strong>DOM结构全部都加载完成</strong>，就会会触发的事件，触发后会执行回调函数</p>
<p>注意区别与 <code>window.addEventListener('load',function()&#123;&#125;)</code>  。  <code>load</code> 事件指的是等待页面中的所有资源都加载完成，含DOM结构加载完成 与其他资源加载完成。</p>
<p>上面的原理正对应着我们日常使用 <code>$(function ()&#123;&#125;)</code> 和 <code>$(document).ready(function ()&#123;&#125;)</code></p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-meta">    "use strict"</span>;
    <span class="hljs-keyword">var</span> version = <span class="hljs-string">"3.5.1"</span>,
        jQuery = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">jQuery</span>(<span class="hljs-params">selector, context</span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> jQuery.fn.init(selector, context);
        &#125;;
    jQuery.fn = jQuery.prototype = &#123;&#125;;
    <span class="hljs-keyword">var</span> rootjQuery = jQuery(<span class="hljs-built_in">document</span>),
        init = jQuery.fn.init = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">init</span>(<span class="hljs-params">selector, context, root</span>) </span>&#123;
            <span class="hljs-keyword">var</span> match, elem;
            <span class="hljs-keyword">if</span> (!selector) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
            root = root || rootjQuery;
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> selector === <span class="hljs-string">"string"</span>) &#123;
              <span class="hljs-comment">//...</span>
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (selector.nodeType) &#123;
              <span class="hljs-comment">//...</span>
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isFunction(selector)) &#123;
                <span class="hljs-keyword">return</span> root.ready !== <span class="hljs-literal">undefined</span> ?
                    root.ready(selector) :
                    selector(jQuery);
            &#125;
            <span class="hljs-comment">//...</span>
        &#125;;
    init.prototype = jQuery.fn;
    <span class="hljs-comment">// =======</span>
    <span class="hljs-keyword">var</span> readyList = jQuery.Deferred();
    jQuery.fn.ready = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">fn</span>) </span>&#123;
        readyList
            .then(fn)
            .catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
                jQuery.readyException(error);
            &#125;);
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
    &#125;;
    <span class="hljs-built_in">window</span>.jQuery = <span class="hljs-built_in">window</span>.$ = jQuery;
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">如果传入的是字符串</h3>
<p>根据判断，分为 <code>$('.box')</code> 选择器类型和 <code>$('<div>xxx</div>')</code> html字符串类型处理，然后根据不同逻辑，使用不同的正则分支判断分别去处理，这里代码过多，就不仔细分析了</p>
<h3 data-id="heading-7">如果传入其他</h3>
<p>例如传入一个数组</p>
<p><img alt="image。png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bfc646ef57c41ec9c2ebba398bfc5e4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
我们可以看到jQ将数组的每一项变为了伪数组的</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-meta">    "use strict"</span>;
    <span class="hljs-keyword">var</span> push = arr.push;
    <span class="hljs-keyword">var</span> version = <span class="hljs-string">"3.5.1"</span>,
        jQuery = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">jQuery</span>(<span class="hljs-params">selector, context</span>) </span>&#123; <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> jQuery.fn.init(selector, context);&#125;;
    jQuery.fn = jQuery.prototype = &#123;
        <span class="hljs-attr">jquery</span>: version,
        <span class="hljs-attr">length</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">push</span>: push
    &#125;;
    jQuery.merge = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">merge</span>(<span class="hljs-params">first, second</span>) </span>&#123;
        <span class="hljs-keyword">var</span> len = +second.length,
            j = <span class="hljs-number">0</span>,
            i = first.length;
        <span class="hljs-keyword">for</span> (; j < len; j++) &#123;
            first[i++] = second[j];
        &#125;
        first.length = i;
        <span class="hljs-keyword">return</span> first;
    &#125;;
    <span class="hljs-keyword">var</span> init = jQuery.fn.init = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">init</span>(<span class="hljs-params">selector, context, root</span>) </span>&#123;
            <span class="hljs-keyword">var</span> match, elem;
            <span class="hljs-keyword">if</span> (!selector) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
            root = root || rootjQuery;
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> selector === <span class="hljs-string">"string"</span>) &#123;...&#125; 
            <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (selector.nodeType) &#123;...&#125; 
            <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isFunction(selector)) &#123;...&#125;
            <span class="hljs-keyword">return</span> jQuery.makeArray(selector, <span class="hljs-built_in">this</span>);
        &#125;;
    init.prototype = jQuery.fn;
    jQuery.makeArray = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeArray</span>(<span class="hljs-params">arr, results</span>) </span>&#123;
        <span class="hljs-keyword">var</span> ret = results || [];
        <span class="hljs-keyword">if</span> (arr != <span class="hljs-literal">null</span>) &#123;
            <span class="hljs-keyword">if</span> (isArrayLike(<span class="hljs-built_in">Object</span>(arr))) &#123;
                jQuery.merge(ret,
                    <span class="hljs-keyword">typeof</span> arr === <span class="hljs-string">"string"</span> ? [arr] : arr
                );
            &#125; <span class="hljs-keyword">else</span> &#123;
                push.call(ret, arr);
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> ret;
    &#125;;
    <span class="hljs-built_in">window</span>.jQuery = <span class="hljs-built_in">window</span>.$ = jQuery;
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到 <code>return jQuery.makeArray(selector, this);</code> ，如果传入数组，jquery对象，就经过 <code>isArrayLike</code> 的检测，然后使用 <code>merge</code> 将空的jQ对象和数组合并。如果是其他类型的值，就调用 <code>push</code> ，将其放在jQ对象的伪数组的第一个，然后最终返回的还是jQuery对象</p>
<h2 data-id="heading-8">手写更强的each方法</h2>
<p>jquery中的 <code>each</code> 方法可以遍历数组/类数组/对象，我们在它源码的基础上再进行更高要求的封装：</p>
<p>要求：支持回调函数返回值处理：传入的回调函数返回 <code>false</code> 则结束循环。 这是内置方法 <code>forEach</code> / <code>map</code> 不具备的</p>
<p>在其中加入传入参数检测的逻辑和结束循环的逻辑</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 遍历数组/类数组/对象「支持回调函数返回值处理：返回false则结束循环，这是内置方法forEach/map不具备的」</span>
    <span class="hljs-keyword">var</span> each = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">each</span>(<span class="hljs-params">obj, callback</span>) </span>&#123;
        <span class="hljs-comment">//'Function.prototype'返回一个匿名空函数,什么都不做,为了兼容下面传入的不是函数的情况</span>
        <span class="hljs-keyword">typeof</span> callback !== <span class="hljs-string">"function"</span> ? callback = <span class="hljs-built_in">Function</span>.prototype : <span class="hljs-literal">null</span>;
        <span class="hljs-keyword">var</span> length,
            i = <span class="hljs-number">0</span>,
            keys = [];
        <span class="hljs-keyword">if</span> (isArrayLike(obj)) &#123;
            <span class="hljs-comment">// 数组或者类数组</span>
            length = obj.length;
            <span class="hljs-keyword">for</span> (; i < length; i++) &#123;
                <span class="hljs-keyword">var</span> item = obj[i],
                <span class="hljs-comment">//让其中的this指向元素本身,(和forEach一样)</span>
                    result = callback.call(item, item, i);
                    <span class="hljs-comment">//回调函数返回false,结合素循环</span>
                <span class="hljs-keyword">if</span> (result === <span class="hljs-literal">false</span>) <span class="hljs-keyword">break</span>
            &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 对象</span>
            <span class="hljs-comment">//为了避免for in循环的问题,我们这里用keys+循环来遍历对象</span>
            keys = <span class="hljs-built_in">Object</span>.keys(obj);
            <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span> !== <span class="hljs-string">"undefined"</span> ? keys = keys.concat(<span class="hljs-built_in">Object</span>.getOwnPropertySymbols(obj)) : <span class="hljs-literal">null</span>;<span class="hljs-comment">//包含Symbol属性</span>
            i = <span class="hljs-number">0</span>;
            length = keys.length;
            <span class="hljs-keyword">for</span> (; i < length; i++) &#123;
                <span class="hljs-keyword">var</span> key = keys[i],
                    value = obj[key];
                    <span class="hljs-comment">//这样既执行了,又返回了结果</span>
                <span class="hljs-keyword">if</span> (callback.call(value, value, key) === <span class="hljs-literal">false</span>) <span class="hljs-keyword">break</span>;
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> obj;
    &#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            