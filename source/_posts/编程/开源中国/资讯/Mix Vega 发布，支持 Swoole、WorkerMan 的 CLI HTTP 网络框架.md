
---
title: 'Mix Vega 发布，支持 Swoole、WorkerMan 的 CLI HTTP 网络框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6952'
author: 开源中国
comments: false
date: Tue, 29 Jun 2021 18:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6952'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">Mix Vega 是一个用 PHP 编写的 CLI HTTP 网络框架，支持 Swoole、WorkerMan。</p> 
<h2 style="text-align:start">Overview</h2> 
<p style="text-align:start">Vega 是 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-php%2Fmix" target="_blank">MixPHP</a> <code>V3+</code> 内置的最核心的组件 (可独立使用)，参考 golang <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgin-gonic%2Fgin" target="_blank">gin</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorilla%2Fmux" target="_blank">mux</a> 开发，它包含 Web 应用处理的大量功能 (数据库处理除外) ，包括：路由、渲染、参数获取、中间件、文件上传处理等；具有 CLI 模式下强大的兼容性，同时支持 Swoole、WorkerMan, 并且支持 Swoole 的多种进程模型。</p> 
<h2 style="text-align:start">Installation</h2> 
<blockquote> 
 <p>需要先安装 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.swoole.com%2F%23%2Fenvironment" target="_blank">Swoole</a> 或者 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.workerman.net%2Finstall%2Frequirement.html" target="_blank">WorkerMan</a></p> 
</blockquote> 
<div style="text-align:start"> 
 <pre><code><span style="color:#6f42c1">composer</span> <span style="color:#032f62">require mix/vega</span>
</code></pre> 
</div> 
<h2 style="text-align:start">Quick start</h2> 
<p style="text-align:start">Swoole 多进程 (异步) 中使用</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#6a737d"><?php</span></span>
<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">require</span></span> <span style="color:#d73a49">__DIR__</span> . <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/vendor/autoload.php'</span></span>;

<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-variable)">Engine</span>();
<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">handleF</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/hello'</span></span>, <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">string</span>(<span style="color:var(--color-prettylights-syntax-constant)">200</span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'hello, world!'</span></span>);
&#125;)-><span style="color:var(--color-prettylights-syntax-entity)">methods</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'GET'</span></span>);

<span style="color:var(--color-prettylights-syntax-constant)">$</span>http = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Swoole</span>\<span style="color:var(--color-prettylights-syntax-variable)">Http</span>\<span style="color:var(--color-prettylights-syntax-variable)">Server</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'0.0.0.0'</span></span>, <span style="color:var(--color-prettylights-syntax-constant)">9501</span>);
<span style="color:var(--color-prettylights-syntax-constant)">$</span>http-><span style="color:var(--color-prettylights-syntax-entity)">on</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'Request'</span></span>, <span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">handler</span>());
<span style="color:var(--color-prettylights-syntax-constant)">$</span>http-><span style="color:var(--color-prettylights-syntax-entity)">start</span>();</pre> 
</div> 
<p style="text-align:start">Swoole 单进程 (协程) 中使用</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#6a737d"><?php</span></span>
<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">require</span></span> <span style="color:#d73a49">__DIR__</span> . <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/vendor/autoload.php'</span></span>;

<span style="color:var(--color-prettylights-syntax-entity)"><span style="color:var(--color-prettylights-syntax-variable)">Swoole</span>\<span style="color:var(--color-prettylights-syntax-variable)">Coroutine</span>\run</span>(<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> () &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>vega = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-variable)">Engine</span>();
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">handleF</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/hello'</span></span>, <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
        <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">string</span>(<span style="color:var(--color-prettylights-syntax-constant)">200</span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'hello, world!'</span></span>);
    &#125;)-><span style="color:var(--color-prettylights-syntax-entity)">methods</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'GET'</span></span>);
    
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>server = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Swoole</span>\<span style="color:var(--color-prettylights-syntax-variable)">Coroutine</span>\<span style="color:var(--color-prettylights-syntax-variable)">Http</span>\<span style="color:var(--color-prettylights-syntax-variable)">Server</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'127.0.0.1'</span></span>, <span style="color:var(--color-prettylights-syntax-constant)">9502</span>, <span style="color:var(--color-prettylights-syntax-constant)"><span style="color:#d73a49">false</span></span>);
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>server-><span style="color:var(--color-prettylights-syntax-entity)">handle</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/'</span></span>, <span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">handler</span>());
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>server-><span style="color:var(--color-prettylights-syntax-entity)">start</span>();
&#125;);</pre> 
</div> 
<p style="text-align:start">WorkerMan 中使用</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#6a737d"><?php</span></span>
<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">require</span></span> <span style="color:#d73a49">__DIR__</span> . <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/vendor/autoload.php'</span></span>;

<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-variable)">Engine</span>();
<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">handleF</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/hello'</span></span>, <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">string</span>(<span style="color:var(--color-prettylights-syntax-constant)">200</span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'hello, world!'</span></span>);
&#125;)-><span style="color:var(--color-prettylights-syntax-entity)">methods</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'GET'</span></span>);

<span style="color:var(--color-prettylights-syntax-constant)">$</span>http_worker = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Workerman</span>\<span style="color:var(--color-prettylights-syntax-variable)">Worker</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"http://0.0.0.0:2345"</span></span>);
<span style="color:var(--color-prettylights-syntax-constant)">$</span>http_worker-><span style="color:var(--color-prettylights-syntax-constant)">onMessage</span> = <span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">handler</span>();
<span style="color:var(--color-prettylights-syntax-constant)">$</span>http_worker-><span style="color:var(--color-prettylights-syntax-constant)">count</span> = <span style="color:var(--color-prettylights-syntax-constant)">4</span>;
<span style="color:var(--color-prettylights-syntax-variable)">Workerman</span>\<span style="color:var(--color-prettylights-syntax-variable)">Worker</span>::<span style="color:var(--color-prettylights-syntax-entity)">runAll</span>();</pre> 
</div> 
<p style="text-align:start">访问测试</p> 
<div style="text-align:start"> 
 <pre><code>% curl http:<span style="color:#6a737d">//0.0.0.0:9501/hello</span>
hello, world!
</code></pre> 
</div> 
<h2 style="text-align:start">路由配置</h2> 
<p style="text-align:start">配置 <code>Closure</code> 闭包路由</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-constant)">$</span>vega = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-variable)">Engine</span>();
<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">handleF</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/hello'</span></span>, <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">string</span>(<span style="color:var(--color-prettylights-syntax-constant)">200</span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'hello, world!'</span></span>);
&#125;)-><span style="color:var(--color-prettylights-syntax-entity)">methods</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'GET'</span></span>);</pre> 
</div> 
<p style="text-align:start">配置 <code>callable</code> 路由</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">class</span></span> <span style="color:var(--color-prettylights-syntax-variable)"><span style="color:#6f42c1">Hello</span></span> &#123;
    <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">public</span></span> <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> <span style="color:var(--color-prettylights-syntax-entity)"><span style="color:#6f42c1">index</span></span>(<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
        <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">string</span>(<span style="color:var(--color-prettylights-syntax-constant)">200</span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'hello, world!'</span></span>);
    &#125;
&#125;
<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-variable)">Engine</span>();
<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">handleC</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/hello'</span></span>, [<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Hello</span>(), <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'index'</span></span>])-><span style="color:var(--color-prettylights-syntax-entity)">methods</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'GET'</span></span>);</pre> 
</div> 
<p style="text-align:start">配置路由变量</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-constant)">$</span>vega = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-variable)">Engine</span>();
<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">handleF</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/users/&#123;id&#125;'</span></span>, <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>id = <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">param</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'id'</span></span>);
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">string</span>(<span style="color:var(--color-prettylights-syntax-constant)">200</span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'hello, world!'</span></span>);
&#125;)-><span style="color:var(--color-prettylights-syntax-entity)">methods</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'GET'</span></span>);</pre> 
</div> 
<p style="text-align:start">配置多个 <code>method</code></p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-constant)">$</span>vega = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-variable)">Engine</span>();
<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">handleF</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'hello'</span></span>, <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">string</span>(<span style="color:var(--color-prettylights-syntax-constant)">200</span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'hello, world!'</span></span>);
&#125;)-><span style="color:var(--color-prettylights-syntax-entity)">methods</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'GET'</span></span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'POST'</span></span>);</pre> 
</div> 
<h2 style="text-align:start">路由前缀 (分组)</h2> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-constant)">$</span>vega = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-variable)">Engine</span>();
<span style="color:var(--color-prettylights-syntax-constant)">$</span>subrouter = <span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">pathPrefix</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/foo'</span></span>);
<span style="color:var(--color-prettylights-syntax-constant)">$</span>subrouter-><span style="color:var(--color-prettylights-syntax-entity)">handleF</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/bar1'</span></span>, <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">string</span>(<span style="color:var(--color-prettylights-syntax-constant)">200</span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'hello, world!'</span></span>);
&#125;)-><span style="color:var(--color-prettylights-syntax-entity)">methods</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'GET'</span></span>);
<span style="color:var(--color-prettylights-syntax-constant)">$</span>subrouter-><span style="color:var(--color-prettylights-syntax-entity)">handleF</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/bar2'</span></span>, <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">string</span>(<span style="color:var(--color-prettylights-syntax-constant)">200</span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'hello1, world!'</span></span>);
&#125;)-><span style="color:var(--color-prettylights-syntax-entity)">methods</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'GET'</span></span>);</pre> 
</div> 
<h2 style="text-align:start">参数获取</h2> 
<h3 style="text-align:start">请求参数</h3> 
<table cellspacing="0" style="width:max-content"> 
 <thead> 
  <tr> 
   <th>方法名称</th> 
   <th>描述</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->param(string $key): string</td> 
   <td style="border-color:#dddddd">获取路由参数</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->query(string $key): string</td> 
   <td style="border-color:#dddddd">获取url参数，包含路由参数</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->defaultQuery(string $key, string $default): string</td> 
   <td style="border-color:#dddddd">获取url参数，可配置默认值</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->getQuery(string $key): string or null</td> 
   <td style="border-color:#dddddd">获取url参数, 可判断是否存在</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->postForm(string $key): string</td> 
   <td style="border-color:#dddddd">获取post参数</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->defaultPostForm(string $key, string $default): string</td> 
   <td style="border-color:#dddddd">获取post参数，可配置默认值</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->getPostForm(string $key): string or null</td> 
   <td style="border-color:#dddddd">获取post参数，可判断是否存在</td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="text-align:start">Headers, Cookies, Uri ...</h3> 
<table cellspacing="0" style="width:max-content"> 
 <thead> 
  <tr> 
   <th>方法名称</th> 
   <th>描述</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->contentType(): string</td> 
   <td style="border-color:#dddddd">请求类型</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->header(string $key): string</td> 
   <td style="border-color:#dddddd">请求头</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->cookie(string $name): string</td> 
   <td style="border-color:#dddddd">cookies</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->uri(): UriInterface</td> 
   <td style="border-color:#dddddd">完整uri</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->rawData(): string</td> 
   <td style="border-color:#dddddd">原始包数据</td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="text-align:start">客户端IP</h3> 
<table cellspacing="0" style="width:max-content"> 
 <thead> 
  <tr> 
   <th>方法名称</th> 
   <th>描述</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->clientIP(): string</td> 
   <td style="border-color:#dddddd">从反向代理获取用户真实IP</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->remoteIP(): string</td> 
   <td style="border-color:#dddddd">获取远程IP</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:start">上传文件处理</h2> 
<table cellspacing="0" style="width:max-content"> 
 <thead> 
  <tr> 
   <th>方法名称</th> 
   <th>描述</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->formFile(string $name): UploadedFileInterface</td> 
   <td style="border-color:#dddddd">获取上传的第一个文件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->multipartForm(): UploadedFileInterface[]</td> 
   <td style="border-color:#dddddd">获取上传的全部文件</td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:start">文件保存</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-constant)">$</span>file = <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">formFile</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'img'</span></span>);
<span style="color:var(--color-prettylights-syntax-constant)">$</span>targetPath = <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/data/uploads/'</span></span> . <span style="color:var(--color-prettylights-syntax-constant)">$</span>file-><span style="color:var(--color-prettylights-syntax-entity)">getClientFilename</span>();
<span style="color:var(--color-prettylights-syntax-constant)">$</span>file-><span style="color:var(--color-prettylights-syntax-entity)">moveTo</span>(<span style="color:var(--color-prettylights-syntax-constant)">$</span>targetPath);</pre> 
</div> 
<h2 style="text-align:start">请求上下文</h2> 
<p style="text-align:start">请求当中需要保存一些信息，比如：会话、JWT载荷等。</p> 
<table cellspacing="0" style="width:max-content"> 
 <thead> 
  <tr> 
   <th>方法名称</th> 
   <th>描述</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->set(string $key, $value): void</td> 
   <td style="border-color:#dddddd">设置值</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->get(string $key): mixed or null</td> 
   <td style="border-color:#dddddd">获取值</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->mustGet(string $key): mixed or throws</td> 
   <td style="border-color:#dddddd">获取值或抛出异常</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:start">中断执行</h2> 
<p style="text-align:start"><code>abort</code> 执行后，会停止执行后面的全部代码，包括中间件。</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-constant)">$</span>vega = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-variable)">Engine</span>();
<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">handleF</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/users/&#123;id&#125;'</span></span>, <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">if</span></span> (<span style="color:var(--color-prettylights-syntax-constant)"><span style="color:#d73a49">true</span></span>) &#123;
        <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">string</span>(<span style="color:var(--color-prettylights-syntax-constant)">401</span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'Unauthorized'</span></span>);
        <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">abort</span>();
    &#125;
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">string</span>(<span style="color:var(--color-prettylights-syntax-constant)">200</span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'hello, world!'</span></span>);
&#125;)-><span style="color:var(--color-prettylights-syntax-entity)">methods</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'GET'</span></span>);</pre> 
</div> 
<h2 style="text-align:start">响应处理</h2> 
<table cellspacing="0" style="width:max-content"> 
 <thead> 
  <tr> 
   <th>方法名称</th> 
   <th>描述</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->status(int $code): void</td> 
   <td style="border-color:#dddddd">设置状态码</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->setHeader(string $key, string $value): void</td> 
   <td style="border-color:#dddddd">设置header</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->setCookie(string $name, string $value, int $expire = 0, ...): void</td> 
   <td style="border-color:#dddddd">设置cookie</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">$ctx->redirect(string $location, int $code = 302): void</td> 
   <td style="border-color:#dddddd">重定向</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:start">JSON 请求与输出</h2> 
<p style="text-align:start">获取 JSON 请求数据</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-constant)">$</span>vega = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-variable)">Engine</span>();
<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">handleF</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/users'</span></span>, <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>obj = <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">getJSON</span>();
    <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">if</span></span> (!<span style="color:var(--color-prettylights-syntax-constant)">$</span>obj) &#123;
        <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">throw</span></span> <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> \<span style="color:var(--color-prettylights-syntax-variable)"><span style="color:#d73a49">Exception</span></span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'Parameter error'</span></span>);
    &#125;
    <span style="color:var(--color-prettylights-syntax-entity)">var_dump</span>(<span style="color:var(--color-prettylights-syntax-constant)">$</span>obj);
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">JSON</span>(<span style="color:var(--color-prettylights-syntax-constant)">200</span>, [
        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'code'</span></span> => <span style="color:var(--color-prettylights-syntax-constant)">0</span>,
        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'message'</span></span> => <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'ok'</span></span>
    ]);
&#125;)-><span style="color:var(--color-prettylights-syntax-entity)">methods</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'POST'</span></span>);</pre> 
</div> 
<p style="text-align:start"><code>mustGetJSON</code> 自带有效性检查，以下代码等同于上面</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-constant)">$</span>vega = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-variable)">Engine</span>();
<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">handleF</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/users'</span></span>, <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>obj = <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">mustGetJSON</span>();
    <span style="color:var(--color-prettylights-syntax-entity)">var_dump</span>(<span style="color:var(--color-prettylights-syntax-constant)">$</span>obj);
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">JSON</span>(<span style="color:var(--color-prettylights-syntax-constant)">200</span>, [
        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'code'</span></span> => <span style="color:var(--color-prettylights-syntax-constant)">0</span>,
        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'message'</span></span> => <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'ok'</span></span>
    ]);
&#125;)-><span style="color:var(--color-prettylights-syntax-entity)">methods</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'POST'</span></span>);</pre> 
</div> 
<h3 style="text-align:start">JSONP 处理</h3> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-constant)">$</span>vega = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-variable)">Engine</span>();
<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">handleF</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/jsonp'</span></span>, <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">JSONP</span>(<span style="color:var(--color-prettylights-syntax-constant)">200</span>, [
        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'code'</span></span> => <span style="color:var(--color-prettylights-syntax-constant)">0</span>,
        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'message'</span></span> => <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'ok'</span></span>
    ]);
&#125;)-><span style="color:var(--color-prettylights-syntax-entity)">methods</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'GET'</span></span>);</pre> 
</div> 
<h2 style="text-align:start">设置中间件</h2> 
<p style="text-align:start">给某个路由配置中间件，可配置多个</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-constant)">$</span>vega = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-variable)">Engine</span>();
<span style="color:var(--color-prettylights-syntax-constant)">$</span>func = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// do something</span></span>
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">next</span>();
&#125;;
<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">handleF</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/hello'</span></span>, <span style="color:var(--color-prettylights-syntax-constant)">$</span>func, <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">string</span>(<span style="color:var(--color-prettylights-syntax-constant)">200</span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'hello, world!'</span></span>);
&#125;)-><span style="color:var(--color-prettylights-syntax-entity)">methods</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'GET'</span></span>);</pre> 
</div> 
<p style="text-align:start">配置全局中间件，即便没有匹配到路由也会执行</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-constant)">$</span>vega = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-variable)">Engine</span>();
<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">use</span>(<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">next</span>();
&#125;);</pre> 
</div> 
<p style="text-align:start">前置中间件</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">use</span>(<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// do something</span></span>
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">next</span>();
&#125;);</pre> 
</div> 
<p style="text-align:start">后置中间件</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">use</span>(<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">next</span>();
    <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// do something</span></span>
&#125;);</pre> 
</div> 
<h3 style="text-align:start">404 自定义</h3> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-constant)">$</span>vega = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-variable)">Engine</span>();
<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">use</span>(<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">try</span></span>&#123;
        <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">next</span>();
    &#125; <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">catch</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-variable)"><span style="color:#d73a49">Exception</span></span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">NotFoundException</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ex) &#123;
        <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">string</span>(<span style="color:var(--color-prettylights-syntax-constant)">404</span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'New 404 response'</span></span>);
        <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">abort</span>();
    &#125;
&#125;);</pre> 
</div> 
<h3 style="text-align:start">500 全局异常捕获</h3> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-constant)">$</span>vega = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-variable)">Engine</span>();
<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">use</span>(<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">try</span></span>&#123;
        <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">next</span>();
    &#125; <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">catch</span></span> (\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Throwable</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ex) &#123;
        <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">string</span>(<span style="color:var(--color-prettylights-syntax-constant)">500</span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'New 500 response'</span></span>);
        <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">abort</span>();
    &#125;
&#125;);</pre> 
</div> 
<h2 style="text-align:start">HTML 视图渲染</h2> 
<p style="text-align:start">创建视图文件 <code>foo.php</code></p> 
<div style="text-align:start"> 
 <pre><span style="color:#333333"><<span style="color:#22863a">p</span>></span>id: <span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#6a737d"><?</span>=</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>id <span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#6a737d">?></span></span>, name: <span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#6a737d"><?</span>=</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>name <span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#6a737d">?></span></span><span style="color:#333333"></<span style="color:#22863a">p</span>></span>
<span style="color:#333333"><</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">p</span></span></span><span style="color:#333333">></span>friends:<span style="color:#333333"></</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">p</span></span></span><span style="color:#333333">></span>
<span style="color:#333333"><</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">ul</span></span></span><span style="color:#333333">></span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#6a737d"><?php</span></span> <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">foreach</span></span>(<span style="color:var(--color-prettylights-syntax-constant)">$</span>friends <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">as</span></span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>name): <span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#6a737d">?></span></span>
        <span style="color:#333333"><</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">li</span></span></span><span style="color:#333333">></span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#6a737d"><?</span>=</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>name <span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#6a737d">?></span></span><span style="color:#333333"></</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">li</span></span></span><span style="color:#333333">></span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#6a737d"><?php</span></span> <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">endforeach</span></span>; <span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#6a737d">?></span></span>
<span style="color:#333333"></</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">ul</span></span></span><span style="color:#333333">></span></pre> 
 <div>
   
 </div> 
</div> 
<p style="text-align:start">配置视图路径，并响应html</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-constant)">$</span>vega = <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">new</span></span> <span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-variable)">Engine</span>();
<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">withHTMLRoot</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/data/project/views'</span></span>);
<span style="color:var(--color-prettylights-syntax-constant)">$</span>vega-><span style="color:var(--color-prettylights-syntax-entity)">handleF</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'/html'</span></span>, <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">function</span></span> (<span style="color:var(--color-prettylights-syntax-variable)">Mix</span>\<span style="color:var(--color-prettylights-syntax-variable)">Vega</span>\<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span> <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx) &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">$</span>ctx-><span style="color:var(--color-prettylights-syntax-entity)">HTML</span>(<span style="color:var(--color-prettylights-syntax-constant)">200</span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'foo'</span></span>, [
        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'id'</span></span> => <span style="color:var(--color-prettylights-syntax-constant)">1000</span>,
        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'name'</span></span> => <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'小明'</span></span>,
        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'friends'</span></span> => [
            <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'小花'</span></span>,
            <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'小红'</span></span>
        ]
    ]);
&#125;)-><span style="color:var(--color-prettylights-syntax-entity)">methods</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'GET'</span></span>);</pre> 
</div> 
<h2 style="text-align:start">License</h2> 
<p style="text-align:start">Apache License Version 2.0, <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.apache.org%2Flicenses%2F" target="_blank">http://www.apache.org/licenses/</a></p>
                                        </div>
                                      
</div>
            