
---
title: '彻底掌握 Node.js 四大流，解决爆缓冲区的_背压_问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb73ee9d7eac4e9eb9734864fc089fc8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 05:39:41 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb73ee9d7eac4e9eb9734864fc089fc8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>把一个东西从 A 搬到 B 该怎么搬呢？</p>
<p>抬起来，移动到目的地，放下不就行了么。</p>
<p>那如果这个东西有一吨重呢？</p>
<p>那就一部分一部分的搬。</p>
<p>其实 IO 也就是搬东西，包括网络的 IO、文件的 IO，如果数据量少，那么直接传送全部内容就行了，但如果内容特别多，一次性加载到内存会崩溃，而且速度也慢，这时候就可以一部分一部分的处理，这就是流的思想。</p>
<p>各种语言基本都实现了 stream 的 api，Node.js 也是，stream api 是比较常用的，下面我们就来探究一下 stream。</p>
<p>本文会回答以下问题：</p>
<ul>
<li>Node.js 的 4 种 stream 是什么</li>
<li>生成器如何与 Readable Stream 结合</li>
<li>stream 的暂停和流动</li>
<li>什么是背压问题，如何解决</li>
</ul>
<h2 data-id="heading-0">Node.js 的 4种 stream</h2>
<h3 data-id="heading-1">流的直观感受</h3>
<p>从一个地方流到另一个地方，显然有流出的一方和流入的一方，流出的一方就是可读流(readable)，而流入的一方就是可写流(writable)。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb73ee9d7eac4e9eb9734864fc089fc8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然，也有的流既可以流入又可以流出，这种叫做双工流（duplex）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/875d6291c85e4300abc89fbca7e1e9a9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>既然可以流入又可以流出，那么是不是可以对流入的内容做下转换再流出呢，这种流叫做转换流（transform）</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd67c5d32e854ae4a2af47f1353bf0c2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>duplex 流的流入和流出内容不需要相关，而 transform 流的流入和流出是相关的，这是两者的区别。</p>
<h3 data-id="heading-2">流的 api</h3>
<p>Node.js 提供的 stream 就是上面介绍的那 4 种：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> stream = <span class="hljs-built_in">require</span>(<span class="hljs-string">'stream'</span>);

<span class="hljs-comment">// 可读流</span>
<span class="hljs-keyword">const</span> Readable = stream.Readable;
<span class="hljs-comment">// 可写流</span>
<span class="hljs-keyword">const</span> Writable = stream.Writable;
<span class="hljs-comment">// 双工流</span>
<span class="hljs-keyword">const</span> Duplex = stream.Duplex;
<span class="hljs-comment">// 转换流</span>
<span class="hljs-keyword">const</span> Transform = stream.Transform;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它们都有要实现的方法：</p>
<ul>
<li>Readable 需要实现 _read 方法来返回内容</li>
<li>Writable 需要实现 _write 方法来接受内容</li>
<li>Duplex 需要实现 _read 和 _write 方法来接受和返回内容</li>
<li>Transform 需要实现 _transform 方法来把接受的内容转换之后返回</li>
</ul>
<p>我们分别来看一下：</p>
<h4 data-id="heading-3">Readable</h4>
<p>Readable 要实现 _read 方法，通过 push 返回具体的数据。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Stream = <span class="hljs-built_in">require</span>(<span class="hljs-string">'stream'</span>);

<span class="hljs-keyword">const</span> readableStream = Stream.Readable();

readableStream._read = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.push(<span class="hljs-string">'阿门阿前一棵葡萄树，'</span>);
    <span class="hljs-built_in">this</span>.push(<span class="hljs-string">'阿东阿东绿的刚发芽，'</span>);
    <span class="hljs-built_in">this</span>.push(<span class="hljs-string">'阿东背着那重重的的壳呀，'</span>);
    <span class="hljs-built_in">this</span>.push(<span class="hljs-string">'一步一步地往上爬。'</span>)
    <span class="hljs-built_in">this</span>.push(<span class="hljs-literal">null</span>);
&#125;

readableStream.on(<span class="hljs-string">'data'</span>, <span class="hljs-function">(<span class="hljs-params">data</span>)=></span> &#123;
    <span class="hljs-built_in">console</span>.log(data.toString())
&#125;);

readableStream.on(<span class="hljs-string">'end'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'done~'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 push 一个 null 时，就代表结束流。</p>
<p>执行效果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae8656a154a546d2a20efb059408d022~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建 Readable 也可以通过继承的方式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Stream = <span class="hljs-built_in">require</span>(<span class="hljs-string">'stream'</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ReadableDong</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Stream</span>.<span class="hljs-title">Readable</span> </span>&#123;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">super</span>();
    &#125;

    <span class="hljs-function"><span class="hljs-title">_read</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.push(<span class="hljs-string">'阿门阿前一棵葡萄树，'</span>);
        <span class="hljs-built_in">this</span>.push(<span class="hljs-string">'阿东阿东绿的刚发芽，'</span>);
        <span class="hljs-built_in">this</span>.push(<span class="hljs-string">'阿东背着那重重的的壳呀，'</span>);
        <span class="hljs-built_in">this</span>.push(<span class="hljs-string">'一步一步地往上爬。'</span>)
        <span class="hljs-built_in">this</span>.push(<span class="hljs-literal">null</span>);
    &#125;

&#125;

<span class="hljs-keyword">const</span> readableStream = <span class="hljs-keyword">new</span> ReadableDong();

readableStream.on(<span class="hljs-string">'data'</span>, <span class="hljs-function">(<span class="hljs-params">data</span>)=></span> &#123;
    <span class="hljs-built_in">console</span>.log(data.toString())
&#125;);

readableStream.on(<span class="hljs-string">'end'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'done~'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可读流是生成内容的，那么很自然可以和生成器结合：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Stream = <span class="hljs-built_in">require</span>(<span class="hljs-string">'stream'</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ReadableDong</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Stream</span>.<span class="hljs-title">Readable</span> </span>&#123;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">iterator</span>)</span> &#123;
        <span class="hljs-built_in">super</span>();
        <span class="hljs-built_in">this</span>.iterator = iterator;
    &#125;

    <span class="hljs-function"><span class="hljs-title">_read</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> next = <span class="hljs-built_in">this</span>.iterator.next();
        <span class="hljs-keyword">if</span>(next.done) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.push(<span class="hljs-literal">null</span>);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">this</span>.push(next.value)
        &#125;
    &#125;

&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> *<span class="hljs-title">songGenerator</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">yield</span> <span class="hljs-string">'阿门阿前一棵葡萄树，'</span>;
    <span class="hljs-keyword">yield</span> <span class="hljs-string">'阿东阿东绿的刚发芽，'</span>;
    <span class="hljs-keyword">yield</span> <span class="hljs-string">'阿东背着那重重的的壳呀，'</span>;
    <span class="hljs-keyword">yield</span> <span class="hljs-string">'一步一步地往上爬。'</span>;
&#125;

<span class="hljs-keyword">const</span> songIterator = songGenerator();

<span class="hljs-keyword">const</span> readableStream = <span class="hljs-keyword">new</span> ReadableDong(songIterator);

readableStream.on(<span class="hljs-string">'data'</span>, <span class="hljs-function">(<span class="hljs-params">data</span>)=></span> &#123;
    <span class="hljs-built_in">console</span>.log(data.toString())
&#125;);

readableStream.on(<span class="hljs-string">'end'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'done~'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就是可读流，通过实现 _read 方法来返回内容。</p>
<h4 data-id="heading-4">Writable</h4>
<p>Writable 要实现 _write 方法，接收写入的内容。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Stream = <span class="hljs-built_in">require</span>(<span class="hljs-string">'stream'</span>);

<span class="hljs-keyword">const</span> writableStream = Stream.Writable();

writableStream._write = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data, enc, next</span>) </span>&#123;
   <span class="hljs-built_in">console</span>.log(data.toString());
   <span class="hljs-comment">// 每秒写一次</span>
   <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
       next();
   &#125;, <span class="hljs-number">1000</span>);
&#125;

writableStream.on(<span class="hljs-string">'finish'</span>, <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'done~'</span>));

writableStream.write(<span class="hljs-string">'阿门阿前一棵葡萄树，'</span>);
writableStream.write(<span class="hljs-string">'阿东阿东绿的刚发芽，'</span>);
writableStream.write(<span class="hljs-string">'阿东背着那重重的的壳呀，'</span>);
writableStream.write(<span class="hljs-string">'一步一步地往上爬。'</span>);
writableStream.end();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接收写入的内容，打印出来，并且调用 next 来处理下一个写入的内容，这里调用 next 是异步的，可以控制频率。</p>
<p>跑了一下，确实可以正常的处理写入的内容：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae8656a154a546d2a20efb059408d022~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这就是可写流，通过实现 _write 方法来处理写入的内容。</p>
<h4 data-id="heading-5">Duplex</h4>
<p>Duplex 是可读可写，同时实现 _read 和 _write 就可以了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Stream = <span class="hljs-built_in">require</span>(<span class="hljs-string">'stream'</span>);

<span class="hljs-keyword">var</span> duplexStream = Stream.Duplex();

duplexStream._read = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.push(<span class="hljs-string">'阿门阿前一棵葡萄树，'</span>);
    <span class="hljs-built_in">this</span>.push(<span class="hljs-string">'阿东阿东绿的刚发芽，'</span>);
    <span class="hljs-built_in">this</span>.push(<span class="hljs-string">'阿东背着那重重的的壳呀，'</span>);
    <span class="hljs-built_in">this</span>.push(<span class="hljs-string">'一步一步地往上爬。'</span>)
    <span class="hljs-built_in">this</span>.push(<span class="hljs-literal">null</span>);
&#125;

duplexStream._write = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data, enc, next</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(data.toString());
    next();
&#125;

duplexStream.on(<span class="hljs-string">'data'</span>, <span class="hljs-function"><span class="hljs-params">data</span> =></span> <span class="hljs-built_in">console</span>.log(data.toString()));
duplexStream.on(<span class="hljs-string">'end'</span>, <span class="hljs-function"><span class="hljs-params">data</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'read done~'</span>));

duplexStream.write(<span class="hljs-string">'阿门阿前一棵葡萄树，'</span>);
duplexStream.write(<span class="hljs-string">'阿东阿东绿的刚发芽，'</span>);
duplexStream.write(<span class="hljs-string">'阿东背着那重重的的壳呀，'</span>);
duplexStream.write(<span class="hljs-string">'一步一步地往上爬。'</span>);
duplexStream.end();

duplexStream.on(<span class="hljs-string">'finish'</span>, <span class="hljs-function"><span class="hljs-params">data</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'write done~'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>整合了 Readable 流和 Writable 流的功能，这就是双工流 Duplex。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58f7e80ba2494feb9dbf48cc0d648f4d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">Transform</h4>
<p>Duplex 流虽然可读可写，但是两者之间没啥关联，而有的时候需要对流入的内容做转换之后流出，这时候就需要转换流 Transform。</p>
<p>Transform 流要实现 _transform 的 api，我们实现下对内容做反转的转换流：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Stream = <span class="hljs-built_in">require</span>(<span class="hljs-string">'stream'</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TransformReverse</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Stream</span>.<span class="hljs-title">Transform</span> </span>&#123;

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">super</span>()
  &#125;

  <span class="hljs-function"><span class="hljs-title">_transform</span>(<span class="hljs-params">buf, enc, next</span>)</span> &#123;
    <span class="hljs-keyword">const</span> res = buf.toString().split(<span class="hljs-string">''</span>).reverse().join(<span class="hljs-string">''</span>);
    <span class="hljs-built_in">this</span>.push(res)
    next()
  &#125;
&#125;

<span class="hljs-keyword">var</span> transformStream = <span class="hljs-keyword">new</span> TransformReverse();

transformStream.on(<span class="hljs-string">'data'</span>, <span class="hljs-function"><span class="hljs-params">data</span> =></span> <span class="hljs-built_in">console</span>.log(data.toString()))
transformStream.on(<span class="hljs-string">'end'</span>, <span class="hljs-function"><span class="hljs-params">data</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'read done~'</span>));

transformStream.write(<span class="hljs-string">'阿门阿前一棵葡萄树'</span>);
transformStream.write(<span class="hljs-string">'阿东阿东绿的刚发芽'</span>);
transformStream.write(<span class="hljs-string">'阿东背着那重重的的壳呀'</span>);
transformStream.write(<span class="hljs-string">'一步一步地往上爬'</span>);
transformStream.end()

transformStream.on(<span class="hljs-string">'finish'</span>, <span class="hljs-function"><span class="hljs-params">data</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'write done~'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>跑了一下，效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b50adb48a8946c1bf307adf7a2c66d8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">流的暂停和流动</h2>
<p>我们从 Readable 流中获取内容，然后流入 Writable 流，两边分别做 _read 和 _write 的实现，就实现了流动。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54bf9c2915b343cb83152daaabd9ac8c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">背压</h3>
<p>但是 read 和 write 都是异步的，如果两者速率不一致呢？</p>
<p>如果 Readable 读入数据的速率大于 Writable 写入速度的速率，这样就会积累一些数据在缓冲区，如果缓冲的数据过多，就会爆掉，会丢失数据。</p>
<p>而如果  Readable 读入数据的速率小于 Writable 写入速度的速率呢？那没关系，最多就是中间有段空闲时期。</p>
<p>这种读入速率大于写入速率的现象叫做<code>“背压”</code>，或者<code>“负压”</code>。也很好理解，写入段压力比较大，写不进去了，会爆缓冲区，导致数据丢失。</p>
<p>这个缓冲区大小可以通过 readableHighWaterMark 和 writableHightWaterMark 来查看，是 16k。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0cc89bf6120a4db38d67c8edd982be85~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">解决背压</h3>
<p>怎么解决这种读写速率不一致的问题呢？</p>
<p>当没写完的时候，暂停读就行了。这样就不会读入的数据越来越多，驻留在缓冲区。</p>
<p>readable stream 有个 readableFlowing 的属性，代表是否自动读入数据，默认为 true，也就是自动读入数据，然后监听 data 事件就可以拿到了。</p>
<p>当 readableFlowing 设置为 false 就不会自动读了，需要手动通过 read 来读入。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">readableStream.readableFlowing = <span class="hljs-literal">false</span>;

<span class="hljs-keyword">let</span> data;
<span class="hljs-keyword">while</span>((data = readableStream.read()) != <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-built_in">console</span>.log(data.toString());
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但自己手动 read 比较麻烦，我们依然可以用自动流入的方式，调用 pause 和 resume 来暂停和恢复就行了。</p>
<p>当调用 writable stream 的 write 方法的时候会返回一个 boolean 值代表是写入了目标还是放在了缓冲区：</p>
<ul>
<li>true: 数据已经写入目标</li>
<li>false：目标不可写入，暂时放在缓冲区</li>
</ul>
<p>我们可以判断返回 false 的时候就 pause，然后等缓冲区清空了就 resume：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> rs = fs.createReadStream(src);
<span class="hljs-keyword">const</span> ws = fs.createWriteStream(dst);

rs.on(<span class="hljs-string">'data'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">chunk</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (ws.write(chunk) === <span class="hljs-literal">false</span>) &#123;
        rs.pause();
    &#125;
&#125;);

rs.on(<span class="hljs-string">'end'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    ws.end();
&#125;);

ws.on(<span class="hljs-string">'drain'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    rs.resume();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就能达到根据写入速率暂停和恢复读入速率的功能，解决了背压问题。</p>
<h3 data-id="heading-10">pipe 有背压问题么？</h3>
<p>平时我们经常会用 pipe 来直接把 Readable 流对接到 Writable 流，但是好像也没遇到过背压问题，其实是 pipe 内部已经做了读入速率的动态调节了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> rs = fs.createReadStream(src);
<span class="hljs-keyword">const</span> ws = fs.createWriteStream(dst);

rs.pipe(ws);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">总结</h2>
<p>流是传输数据时常见的思想，就是一部分一部分的传输内容，是文件读写、网络通信的基础概念。</p>
<p>Node.js 也提供了 stream 的 api，包括 Readable 可读流、Writable 可写流、Duplex 双工流、Transform 转换流。它们分别实现 _read、_write、_read + _write、_transform 方法，来做数据的返回和处理。</p>
<p>创建 Readable 对象既可以直接调用 Readable api 创建，然后重写 _read 方法，也可以继承 Readable 实现一个子类，之后实例化。其他流同理。（Readable 可以很容易的和 generator 结合）</p>
<p>当读入的速率大于写入速率的时候就会出现“背压”现象，会爆缓冲区导致数据丢失，解决的方式是根据 write 的速率来动态 pause 和 resume 可读流的速率。pipe 就没有这个问题，因为内部做了处理。</p>
<p>流是掌握 IO 绕不过去的一个概念，而背压问题也是流很常见的问题，遇到了数据丢失可以考虑是否发生了背压。希望这篇文章能够帮大家理清思路，真正掌握 stream！</p></div>  
</div>
            