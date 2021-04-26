
---
title: 'Mix XWP V1.1 - Go 通用动态协程池 WorkerPool'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3686'
author: 开源中国
comments: false
date: Mon, 26 Apr 2021 07:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3686'
---

<div>   
<div class="content">
                                                                    
                                                        <blockquote> 
 <p>OpenMix 出品：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenmix.org%2Fmix-go" target="_blank">https://openmix.org</a></p> 
</blockquote> 
<h2 style="text-align:start">Mix XWP</h2> 
<p style="text-align:start"><span style="color:#000000">通用的工作池</span></p> 
<p style="text-align:start"><span style="color:#000000">A common worker pool</span></p> 
<h2 style="text-align:start">Installation</h2> 
<pre style="text-align:start"><code>go get github.com/mix-go/xwp
</code></pre> 
<h2 style="text-align:start">Usage</h2> 
<p style="text-align:start"><span style="color:#000000">先创建一个结构体用来处理任务，使用类型断言转换任务数据类型，例如：<code>i := data.(int)</code></span></p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Foo</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> (t <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Foo</span>) <span style="color:var(--color-prettylights-syntax-entity)">Do</span>(data <span style="color:var(--color-prettylights-syntax-keyword)">interface</span>&#123;&#125;) &#123;
    <span style="color:var(--color-prettylights-syntax-comment)">// do something</span>
&#125;</pre> 
</div> 
<p style="text-align:start"><span style="color:#000000">调度任务</span></p> 
<ul> 
 <li>也可以使用 <code>RunF</code> 采用闭包来处理任务</li> 
 <li>如果不想阻塞执行，可以使用 <code>p.Start()</code> 启动</li> 
</ul> 
<div style="text-align:start"> 
 <pre>jobQueue <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-entity)">make</span>(<span style="color:var(--color-prettylights-syntax-keyword)">chan</span> <span style="color:var(--color-prettylights-syntax-keyword)">interface</span>&#123;&#125;, <span style="color:var(--color-prettylights-syntax-constant)">200</span>)

p <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span>xwp.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WorkerPool</span>&#123;
    <span style="color:var(--color-prettylights-syntax-constant)">JobQueue</span>:       jobQueue,
    <span style="color:var(--color-prettylights-syntax-constant)">MaxWorkers</span>:     <span style="color:var(--color-prettylights-syntax-constant)">1000</span>,
    <span style="color:var(--color-prettylights-syntax-constant)">InitWorkers</span>:    <span style="color:var(--color-prettylights-syntax-constant)">100</span>,
    <span style="color:var(--color-prettylights-syntax-constant)">MaxIdleWorkers</span>: <span style="color:var(--color-prettylights-syntax-constant)">100</span>,
    <span style="color:var(--color-prettylights-syntax-constant)">RunI</span>:           <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Foo</span>&#123;&#125;,
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">go</span> <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
    <span style="color:var(--color-prettylights-syntax-comment)">// 投放任务</span>
    <span style="color:var(--color-prettylights-syntax-keyword)">for</span> i <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">0</span>; i <span style="color:var(--color-prettylights-syntax-constant)"><</span> <span style="color:var(--color-prettylights-syntax-constant)">10000</span>; i<span style="color:var(--color-prettylights-syntax-constant)">++</span> &#123;
        jobQueue <span style="color:var(--color-prettylights-syntax-constant)"><-</span> i
    &#125;

    <span style="color:var(--color-prettylights-syntax-comment)">// 投放完停止调度</span>
    p.<span style="color:var(--color-prettylights-syntax-entity)">Stop</span>()
&#125;()

p.<span style="color:var(--color-prettylights-syntax-entity)">Run</span>() <span style="color:var(--color-prettylights-syntax-comment)">// 阻塞等待</span></pre> 
</div> 
<p style="text-align:start"><span style="color:#000000">异常处理：<code>Do</code> 方法中执行的代码，可能会出现 <code>panic</code> 异常，我们可以通过 <code>recover</code> 获取异常信息记录到日志或者执行其他处理</span></p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">func</span> (t <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Foo</span>) <span style="color:var(--color-prettylights-syntax-entity)">Do</span>(data <span style="color:var(--color-prettylights-syntax-keyword)">interface</span>&#123;&#125;) &#123;
    <span style="color:var(--color-prettylights-syntax-keyword)">defer</span> <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
        <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-entity)">recover</span>(); err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
            <span style="color:var(--color-prettylights-syntax-comment)">// handle error</span>
        &#125;
    &#125;()
    <span style="color:var(--color-prettylights-syntax-comment)">// do something</span>
&#125;</pre> 
</div> 
<p style="text-align:start"><span style="color:#000000">查看 <code>Workers</code> 的执行状态：通常可以使用一个定时器，定时打印或者告警处理</span></p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">go</span> <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
    ticker <span style="color:var(--color-prettylights-syntax-constant)">:=</span> time.<span style="color:var(--color-prettylights-syntax-entity)">NewTicker</span>(<span style="color:var(--color-prettylights-syntax-constant)">1000</span> <span style="color:var(--color-prettylights-syntax-constant)">*</span> time.<span style="color:var(--color-prettylights-syntax-constant)">Millisecond</span>)
    <span style="color:var(--color-prettylights-syntax-keyword)">for</span> &#123;
        <span style="color:var(--color-prettylights-syntax-constant)"><-</span>ticker.<span style="color:var(--color-prettylights-syntax-constant)">C</span>
        log.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%+v"</span>, p.<span style="color:var(--color-prettylights-syntax-entity)">Stat</span>()) <span style="color:var(--color-prettylights-syntax-comment)">// 2021/04/26 14:32:53 &&#123;Active:5 Idle:95 Total:100&#125;</span>
    &#125;
&#125;()</pre> 
</div> 
<h2 style="text-align:start">License</h2> 
<p style="text-align:start"><span style="color:#000000">Apache License Version 2.0, </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.apache.org%2Flicenses%2F" target="_blank"><span style="color:#000000">http://www.apache.org/licenses/</span></a></p>
                                        </div>
                                      
</div>
            