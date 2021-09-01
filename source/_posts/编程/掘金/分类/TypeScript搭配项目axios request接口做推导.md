
---
title: 'TypeScript搭配项目axios request接口做推导'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4e114819a5048b0b1c157414d0a87bb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 21:17:08 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4e114819a5048b0b1c157414d0a87bb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">简述</h1>
<p>随着前端技术的发展，TypeScript 已经逐渐取代Javascript，尤其在各大开源项目，或者是其他开源js项目，我们都可以看到ts的身影，例如我们熟知的vue3 就是用ts重构的；</p>
<ul>
<li>在使用ts的时候，最大的一个好处就是可以给js各种类型约束，使得Js能够完成静态代码分析，推断代码中存在的类型错误或者类型提示，不需要在运行时候才发现错误；</li>
<li>TS完成类型推导，需要事先知道变量的类型，所以我们得需要事先给变量定义好明确的类型，这可以让TS很好的完成类型推倒；</li>
</ul>
<p>首先我们需要简单了解一下ts：<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fts.xcatliu.com%2Fbasics%2Fdeclaration-files.html" target="_blank" rel="nofollow noopener noreferrer" title="https://ts.xcatliu.com/basics/declaration-files.html" ref="nofollow noopener noreferrer">什么是TypeScript</a></p>
<p>在这篇中学会ts的一些泛型，文件声明，接口（interface），type，一系列类型描述即可；<br>
个人觉得 学会ts的最快方式就是看一些开源代码； 可以了解到很懂泛型的使用；<br>
本篇文章只是浅度的使用到泛型；</p>
<h1 data-id="heading-1">正文</h1>
<h2 data-id="heading-2">封装一个axios，或者 request 请求函数；</h2>
<p>通常我们封装函数的格式</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// request.js</span>

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@description</span>: 请求函数
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> </span>path 路径
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;object&#125;</span> </span>params 携带参数
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;object&#125;</span></span>
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params">path, params</span>) </span>&#123;
    <span class="hljs-comment">// ...</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>页面中使用的情况大概如下；</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> [d, setData] = useState(&#123;&#125;); 
<span class="hljs-comment">// 这是一个List接口 我们需要使用上面的request方法</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getList</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> request(<span class="hljs-string">'v1/app/list'</span>, &#123;<span class="hljs-attr">search</span>: <span class="hljs-number">1</span>&#125;);
    <span class="hljs-keyword">if</span>(res.code === <span class="hljs-number">200</span>) &#123;
        setData(res.data)
    &#125;
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到我们上面封装函数一般都是 path params请求路径；
返回的是一个promise resolve结果；
结构一般是：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
 <span class="hljs-attr">code</span>: <span class="hljs-number">200</span>,
 <span class="hljs-attr">data</span>: &#123;&#125;,
 <span class="hljs-attr">errMsg</span>: <span class="hljs-string">'错误提示'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">ts接口书写</h2>
<p>ok 有了以上的信息，我们来简单做一下函数的封装；</p>
<p>首先我们先写一下 返回格式的描述；</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 服务端接口基本类型</span>
<span class="hljs-keyword">type</span> Server<T> = &#123;
    <span class="hljs-attr">errMsg</span>: <span class="hljs-built_in">string</span>;
    data: T;
    code: <span class="hljs-number">200</span> | <span class="hljs-number">1000</span> | <span class="hljs-number">1001</span> | <span class="hljs-number">404</span> | <span class="hljs-number">500</span> ...;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>学习完.d.ts, 以及interface后，我们知道interface 声明的接口会自动合并，而.d.ts中声明的可以在全局中任何地方去使用；</p>
<p>所以可以在.d.ts 中是声明我们所需要的接口名字，我们暂把它定死为API;</p>
<p>因为我们需要根据path 自动推导出来params参数，data等； 所以需要定义一种有关联意义的；</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// abc.d.ts</span>
<span class="hljs-keyword">interface</span> API &#123;
    <span class="hljs-string">'/v1/app/list'</span>: &#123;
        <span class="hljs-attr">params</span>: &#123;
            <span class="hljs-comment">/** 我是a参数 */</span>
            <span class="hljs-attr">a</span>: <span class="hljs-built_in">number</span>;
            <span class="hljs-comment">/** 我是b参数 */</span>
            b: <span class="hljs-built_in">string</span>;
        &#125;,
        <span class="hljs-attr">data</span>: &#123;
            <span class="hljs-comment">/** 数字类型的数组 */</span>
            <span class="hljs-attr">list</span>: <span class="hljs-built_in">number</span>[];
        &#125;
    &#125;
    <span class="hljs-string">'/v1/app/home'</span>: &#123;
        <span class="hljs-attr">params</span>: &#123;&#125;,
        <span class="hljs-attr">data</span>: &#123;&#125;
    &#125;
&#125;


<span class="hljs-keyword">interface</span> API &#123;
    <span class="hljs-string">'/v1/app/abc'</span>: &#123;
        <span class="hljs-attr">params</span>: &#123;&#125;,
        <span class="hljs-attr">data</span>: &#123;&#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以这样的去写， interface的结构； 可以看到 list home abc 三个接口都有自己的关联的params 与 data；</p>
<h2 data-id="heading-4">函数的写法</h2>
<p>接下来看函数的描述</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 请求方法参数约束</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Drequest</span><<span class="hljs-title">URL</span> <span class="hljs-title">extends</span> <span class="hljs-title">keyof</span> <span class="hljs-title">API</span>>(<span class="hljs-params">
path: URL,
params: API[URL][<span class="hljs-string">'params'</span>],
method?: <span class="hljs-string">'POST'</span>
</span>): <span class="hljs-title">Promise</span><<span class="hljs-title">Server</span><<span class="hljs-title">API</span>[<span class="hljs-title">URL</span>]['<span class="hljs-title">data</span>']>>

<span class="hljs-title">export</span> <span class="hljs-title">default</span> <span class="hljs-title">const</span> <span class="hljs-title">request</span>:<span class="hljs-title">typeof</span> <span class="hljs-title">Drequest</span> = (<span class="hljs-params">path, params, method = <span class="hljs-string">'POST'</span></span>) => </span>&#123;
   
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面有.d.ts中有相对应的 API接口了，可以使用推导；
这个函数是最后关键的组装；<br>
keyof 是把 interface 的key变成联合类型</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-string">'/v1/app/list'</span> | <span class="hljs-string">'/v1/app/home'</span> | <span class="hljs-string">'/v1/app/abc'</span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>extends 是看URL 是否可以是联合类型中的一种 <br>
看到最上面封装的函数有 path params ，这样子我们就可以与 path 一一对应起来了；</p>
<p>看一下页面使用情况吧：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4e114819a5048b0b1c157414d0a87bb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f5d4db0294145638072694f55295d82~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/832603038a254323975ee2f34898b5ec~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">总结</h1>
<p>经过上面这些ts 接口的封装可以自动校验 params 的参数类型，以及推导data字段类型；
不过这些 都需要自己去写接口字段data 以及用 /** */ 做注释；<br>
这样做会加占用前期的开发时间，不过对于之后的维护还是很有利的；
与服务端定好的字段更能严格一点，因为我们也会复制他们的类型等等；</p></div>  
</div>
            