
---
title: 'Promise.all()实现根据传入url顺序, 返回按序结果'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8869'
author: 掘金
comments: false
date: Thu, 15 Apr 2021 23:21:03 GMT
thumbnail: 'https://picsum.photos/400/300?random=8869'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">问题描述:</h3>
<ul>
<li>网络请求是异步的, 如果使用<code>for</code>循环, 进行好多的数据请求, 返回的数据, 很可能不是按照用户输入的顺序返回的.</li>
</ul>
<h4 data-id="heading-1">解决方法:</h4>
<ul>
<li>这里可以使用<code>Promise.all()</code>方法实现, 异步网络请求, 返回的数据也是按序的.</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-title">functionlaodFiles</span>(<span class="hljs-params">dataFiles</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>((<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-comment">// promise.all保证了, 输出的顺序和输入的是一致的</span>
        <span class="hljs-built_in">Promise</span>.all(dataFiles.map(<span class="hljs-function"><span class="hljs-params">dataFile</span> =></span> &#123;
            axios.get(dataFile.url).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> (&#123;<span class="hljs-attr">date</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(res), <span class="hljs-attr">data</span>: res&#125;))
        &#125;)).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
            resolve(data)
        &#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
            reject(err)
        &#125;)
    &#125;))
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">实现原理</h3>
<ul>
<li><code>Promise.all</code>内部是怎么实现按序的呢, 下面我们就来扒一扒<code>Promise.all</code>内部的秘密</li>
<li>首先贴上, 手写的<code>Promise.all() </code></li>
</ul>
<h3 data-id="heading-3">正确写法:</h3>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">PromiseAll</span>(<span class="hljs-params">promises</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.isArray(promises)) &#123;
            <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'传入的参数必须得是数组格式'</span>))
        &#125;
        <span class="hljs-keyword">let</span> res = []
        <span class="hljs-keyword">let</span> count;
        promises.forEach(<span class="hljs-function">(<span class="hljs-params">promise, index</span>) =></span> &#123;
        <span class="hljs-comment">// 这里其实需要判断一下, 当前遍历的promise是否是Promise类型, 但是, 这里没有判断, 想想是因为什么原因. </span>
            <span class="hljs-built_in">Promise</span>.resolve(promise).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
            <span class="hljs-comment">// 注意点1: index用来保证按序存储</span>
                res[index]  = data
                count++
                <span class="hljs-comment">// 注意点2: count用来保证获取到了想要的所有数据</span>
                <span class="hljs-keyword">if</span>(count === promises.length) &#123;
                    resolve(res)
                &#125;
            &#125;, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
            &#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
                <span class="hljs-keyword">return</span> reject(err)
            &#125;)
        &#125;)
    &#125;)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">不正确的写法一:</h3>
<ul>
<li>上面代码的<code>forEach</code>方法中, 第一个参数<code>promise</code>遍历的当前对象, 后一个<code>index</code>是关键, 可能会有人在处理结果的时候, 像下面这样书写:</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">let</span> count =<span class="hljs-number">0</span>
<span class="hljs-keyword">let</span> res = []
<span class="hljs-keyword">let</span> length= promises.length
promises.forEach(<span class="hljs-function"><span class="hljs-params">promise</span> =></span> &#123;
    <span class="hljs-built_in">Promise</span>.resolve(promise).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
        res.push(data)
        <span class="hljs-comment">// 直接判断判断当前的结果数组长度是否是传入的数组长度</span>
        <span class="hljs-keyword">if</span>(res.length === length) resolve(res)
    &#125;)
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>但是像这样直接用返回结果长度会有一个问题, 那就是, 里面的结果数据不是按序的, 只要结果返回就往里面<code>push</code>,可能第一个返回的结果, 并不是第一个传入参数对应的, 可能是第三个或者任何一个.</p>
</li>
</ul>
<h3 data-id="heading-5">不正确的写法二:</h3>
<ul>
<li>
<ul>
<li>上面代码的<code>forEach</code>方法中, 第一个参数<code>promise</code>遍历的当前对象, 后一个<code>index</code>是关键, 那你说<code>index</code>是关键, 那我就带上就好了 , 然后,可能会有人在处理结果的时候, 像下面这样书写:</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">let</span> count =<span class="hljs-number">0</span>
<span class="hljs-keyword">let</span> res = []
<span class="hljs-keyword">let</span> length= promises.length
promises.forEach(<span class="hljs-function">(<span class="hljs-params">promise, index</span>) =></span> &#123;
    <span class="hljs-built_in">Promise</span>.resolve(promise).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-comment">// 1.根据返回的结果, 将数据按照对应的index放进数组, 就可以保证按序了</span>
        res[index] = data
        <span class="hljs-comment">// 2.直接判断判断当前的结果数组长度是否是传入的数组长度(这里有坑</span>
        <span class="hljs-keyword">if</span>(res.length === length) resolve(res)
    &#125;)
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>那你可能会说, 我带了<code>inded</code>也按序了, 我这样写就没问题了吧! 但是! 你想想看, 如果, 第一个返回的就是, 最后一个<code>index</code>, 那直接把数组装满了, 结果为: <code>[undefined,undefined,undefined,undefined,......, data]</code>. 这样肯定是错误的, 那之前的数据都是空的了.</li>
</ul>
<h3 data-id="heading-6">总结</h3>
<ul>
<li>在使用前人, 前辈创造出来的好工具的时候, 也想想里面的原理, 这样, 才能从前辈那里学到一些知识和技能.</li>
<li>这里需要注意的是两个点:</li>
</ul>
<ol>
<li>需要对遍历的当前对象判断是否为<code>Promise</code>类型, 但是, 可以使用<code>Promise.resolve()</code>这样可以保证当前的对象是<code>Promise</code>类型.</li>
<li>需要使用<code>index</code>来进行返回数据的顺序问题.  res[index] = data</li>
<li>需要定一个<code>count</code>用来判断是否将所有的数据获取完毕了.</li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            