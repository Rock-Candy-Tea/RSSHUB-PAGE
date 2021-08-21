
---
title: 'JavaScript中到底什么是异步'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a13c309c48240c897295d1e73955329~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 22:59:16 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a13c309c48240c897295d1e73955329~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第20天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h1 data-id="heading-0">实例</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
&#125;,<span class="hljs-number">0</span>)
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里问大家一个问题，这个函数的执行顺序是什么样的？按照常理来说，延迟0秒执行，不就是不延迟吗，所以应该是： 0 1吧；
但实际是：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a13c309c48240c897295d1e73955329~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为setTimeout就是个<strong>异步函数</strong><br>
异步：不死等耗时较长的事情完成，先同时干别的事情，耗时较长的事情完成了，控制权交给回调函数<br>
同步：就是异步的反面，死等那个耗时较长的事情完成，然后做别的事情\</p>
<h1 data-id="heading-1">什么是异步</h1>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f113661f3c9f48c08df8fe23b1a7707a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>js中常见的异步函数：
1） setInterval、setTimeout
2） 所有的事件监听可以看做异步
3） Ajax（实际上也是onreadystatechange事件）</p>
<h1 data-id="heading-2">其他的一些异步和同步</h1>
<p>Node.js全是异步
PHP读取数据库，是同步的，死等读取完成：</p>
<pre><code class="hljs language-php copyable" lang="php"><span class="hljs-comment">//php是同步读取数据库，I/O时间非常长，仍然死等，I/O驱动程序开始工作，CPU计算进程被阻塞。</span>
<span class="hljs-variable">$result</span> = Mysql_query(<span class="hljs-string">"SELECT * FROM table1"</span>);
mysql_fetch_array(<span class="hljs-variable">$result</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// node.js和php相反，是异步的：</span>
db.read(&#123;<span class="hljs-string">"student"</span>:<span class="hljs-string">"all"</span>&#125;,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(data.username);
&#125;);
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>+<span class="hljs-number">2</span>+<span class="hljs-number">3</span>);    
<span class="hljs-comment">//会先打印6 再打印IO查出的数据</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">Ajax异步的细节：</h2>
<p>● 浏览器执行到Ajax代码这行语句，发出了一个HTTP请求，欲请求服务器上的数据。服务器的此时开始I/O，所谓的I/O就是磁盘读取，需要花一些时间，所以不会立即产生下行HTTP报文。<br>
● 由于Ajax是异步的，所以本地的JavaScript程序不会停止运行，页面不会假死，不会傻等下行HTTP报文的出现。后面的JavaScript语句将继续运行。进程不阻塞。<br>
● 服务器I/O结束，将下行HTTP报文发送到本地。此时，回调函数将执行。回调函数中，将使用DOM更改页面内容。</p></div>  
</div>
            