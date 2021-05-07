
---
title: 'Mix XDI V1.1 - Golang DI、IoC 依赖注入容器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6897'
author: 开源中国
comments: false
date: Fri, 07 May 2021 10:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6897'
---

<div>   
<div class="content">
                                                                    
                                                        <blockquote> 
 <p>OpenMix 出品：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenmix.org%2Fmix-go" target="_blank">https://openmix.org</a></p> 
</blockquote> 
<h2 style="text-align:start">Mix XDI</h2> 
<p style="text-align:start"><span style="color:#000000">DI、IoC 容器</span></p> 
<p style="text-align:start"><span style="color:#000000">DI, IoC container</span></p> 
<h2 style="text-align:start">Overview</h2> 
<p style="text-align:start"><span style="color:#000000">一个创建对象以及处理对象依赖关系的库，该库可以实现统一管理依赖，全局对象管理，动态配置刷新等。</span></p> 
<h2 style="text-align:start">Installation</h2> 
<pre style="text-align:start"><code>go get github.com/mix-go/xdi
</code></pre> 
<h2 style="text-align:start">Quick start</h2> 
<p style="text-align:start"><span style="color:#000000">通过依赖配置实例化一个单例</span></p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xdi"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Foo</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">init</span>() &#123;
    obj <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span>xdi.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Object</span>&#123;
        <span style="color:var(--color-prettylights-syntax-constant)">Name</span>: <span style="color:var(--color-prettylights-syntax-string)">"foo"</span>,
        <span style="color:var(--color-prettylights-syntax-constant)">New</span>: <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() (<span style="color:var(--color-prettylights-syntax-keyword)">interface</span>&#123;&#125;, <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">error</span>) &#123;
            i <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Foo</span>&#123;&#125;
            <span style="color:var(--color-prettylights-syntax-keyword)">return</span> i, <span style="color:var(--color-prettylights-syntax-constant)">nil</span>
        &#125;,
    &#125;
    <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> xdi.<span style="color:var(--color-prettylights-syntax-entity)">Provide</span>(obj); err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
        <span style="color:var(--color-prettylights-syntax-entity)">panic</span>(err)
    &#125;
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
    <span style="color:var(--color-prettylights-syntax-keyword)">var</span> foo <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Foo</span>
    <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> xdi.<span style="color:var(--color-prettylights-syntax-entity)">Populate</span>(<span style="color:var(--color-prettylights-syntax-string)">"foo"</span>, <span style="color:var(--color-prettylights-syntax-constant)">&</span>foo); err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
        <span style="color:var(--color-prettylights-syntax-entity)">panic</span>(err)
    &#125;
    <span style="color:var(--color-prettylights-syntax-comment)">// use foo</span>
&#125;</pre> 
</div> 
<h2 style="text-align:start">Reference</h2> 
<p style="text-align:start"><span style="color:#000000">依赖配置中引用另一个依赖配置的实例</span></p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xdi"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Foo</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">Bar</span> <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Bar</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Bar</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">init</span>() &#123;
    objs <span style="color:var(--color-prettylights-syntax-constant)">:=</span> []<span style="color:var(--color-prettylights-syntax-constant)">*</span>xdi.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Object</span>&#123;
        &#123;
            <span style="color:var(--color-prettylights-syntax-constant)">Name</span>: <span style="color:var(--color-prettylights-syntax-string)">"foo"</span>,
            <span style="color:var(--color-prettylights-syntax-constant)">New</span>: <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() (<span style="color:var(--color-prettylights-syntax-keyword)">interface</span>&#123;&#125;, <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">error</span>) &#123;
                <span style="color:var(--color-prettylights-syntax-comment)">// reference bar</span>
                <span style="color:var(--color-prettylights-syntax-keyword)">var</span> bar <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Bar</span>
                <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> xdi.<span style="color:var(--color-prettylights-syntax-entity)">Populate</span>(<span style="color:var(--color-prettylights-syntax-string)">"bar"</span>, <span style="color:var(--color-prettylights-syntax-constant)">&</span>bar); err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
                    <span style="color:var(--color-prettylights-syntax-keyword)">return</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span>, err
                &#125;

                i <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Foo</span>&#123;
                    <span style="color:var(--color-prettylights-syntax-constant)">Bar</span>: bar,
                &#125;
                <span style="color:var(--color-prettylights-syntax-keyword)">return</span> i, <span style="color:var(--color-prettylights-syntax-constant)">nil</span>
            &#125;,
        &#125;,
        &#123;
            <span style="color:var(--color-prettylights-syntax-constant)">Name</span>: <span style="color:var(--color-prettylights-syntax-string)">"bar"</span>,
            <span style="color:var(--color-prettylights-syntax-constant)">New</span>: <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() (<span style="color:var(--color-prettylights-syntax-keyword)">interface</span>&#123;&#125;, <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">error</span>) &#123;
                i <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Bar</span>&#123;&#125;
                <span style="color:var(--color-prettylights-syntax-keyword)">return</span> i, <span style="color:var(--color-prettylights-syntax-constant)">nil</span>
            &#125;,
            <span style="color:var(--color-prettylights-syntax-constant)">NewEverytime</span>: <span style="color:var(--color-prettylights-syntax-constant)">true</span>,
        &#125;,
    &#125;
    <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> xdi.<span style="color:var(--color-prettylights-syntax-entity)">Provide</span>(objs<span style="color:var(--color-prettylights-syntax-constant)">...</span>); err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
        <span style="color:var(--color-prettylights-syntax-entity)">panic</span>(err)
    &#125;
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
    <span style="color:var(--color-prettylights-syntax-keyword)">var</span> foo <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Foo</span>
    <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> xdi.<span style="color:var(--color-prettylights-syntax-entity)">Populate</span>(<span style="color:var(--color-prettylights-syntax-string)">"foo"</span>, <span style="color:var(--color-prettylights-syntax-constant)">&</span>foo); err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
        <span style="color:var(--color-prettylights-syntax-entity)">panic</span>(err)
    &#125;
    <span style="color:var(--color-prettylights-syntax-comment)">// use foo</span>
&#125;</pre> 
</div> 
<h2 style="text-align:start">Refresh singleton</h2> 
<p style="text-align:start"><span style="color:#000000">程序执行中配置信息发生变化时，可以刷新单例的实例</span></p> 
<div style="text-align:start"> 
 <pre>obj, err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> xdi.<span style="color:var(--color-prettylights-syntax-entity)">Container</span>().<span style="color:var(--color-prettylights-syntax-entity)">Object</span>(<span style="color:var(--color-prettylights-syntax-string)">"foo"</span>)
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
    <span style="color:var(--color-prettylights-syntax-entity)">panic</span>(err)
&#125;
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> obj.<span style="color:var(--color-prettylights-syntax-entity)">Refresh</span>(); err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
    <span style="color:var(--color-prettylights-syntax-entity)">panic</span>(err)
&#125;</pre> 
</div> 
<h2 style="text-align:start">License</h2> 
<p style="text-align:start"><span style="color:#000000">Apache License Version 2.0, </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.apache.org%2Flicenses%2F" target="_blank"><span style="color:#000000">http://www.apache.org/licenses/</span></a></p>
                                        </div>
                                      
</div>
            