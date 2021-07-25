
---
title: '当CDN服务不可用时，前端有什么解决办法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9565'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 00:46:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=9565'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>现在前端主流的部署方式基本都是把静态资源打包上传至CDN服务器，可能还会引用一些在线公共资源库。这都可能会存在一种问题：如果CDN服务器挂了，就会导致页面访问不了。笔者在之前的工作中就遇到过第三方资源公共CDN服务器挂掉的问题，当时的临时解决方法是修改地址，重新发布，期间存在一定时间内不可用状态。对于中小型公司来说，系统少的还好，对于系统多的改起来可费劲了。</p>
<p>那么从前端角度来看，有没有什么比较好的解决思路呢？</p>
<p>其实思路很简单，就是在当前静态资源加载失败时自动换到另一个地方重新加载该资源。基于这种思路，我们可以把静态资源上传到多个CDN服务器上，一个作为主要使用，一个作为备份使用，让不同CDN服务，请求路径相同。这里以CDN A为主域名使用，以CDN B为备份域名使用为例。</p>
<p>当js、css资源加载失败时，会触发 <code>onerror</code> 事件，我们可以给所有的 <code>script</code> 和 <code>link</code> 标签加上一个 <code>onerror</code> 事件 <code>onCdnError</code> ，然后在 <code>window</code> 中定义全局的 <code>onCdnError</code> 事件，然后在自定义事件中获取当前资源失败的链接，替换成备用cdn地址，重新加载一次资源即可。</p>
<p>主要实现逻辑：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 静态资源对应的链接</span>
<span class="hljs-keyword">var</span> staticMap = &#123;
  <span class="hljs-attr">link</span>: <span class="hljs-string">"href"</span>,
  <span class="hljs-attr">script</span>: <span class="hljs-string">"src"</span>,
&#125;;
<span class="hljs-comment">// <link onerror="onCdnError(this)" href="https://cdn-a.com/index.css" rel="stylesheet"/></span>
<span class="hljs-comment">// <script onerror="onCdnError(this)" href="https://cdn-a.com/index.js"></script></span>
<span class="hljs-built_in">window</span>.onCdnError = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
  <span class="hljs-keyword">const</span> nodeName = e.nodeName.toLowerCase();
  <span class="hljs-keyword">const</span> srcName = staticMap[nodeName];
  <span class="hljs-keyword">if</span> (!srcName) &#123;
    <span class="hljs-keyword">return</span>;
  &#125;
  <span class="hljs-comment">// 获取当前加载失败的链接</span>
  <span class="hljs-keyword">let</span> link = e[srcName];
  <span class="hljs-keyword">if</span> (!link) <span class="hljs-keyword">return</span>;
  <span class="hljs-keyword">if</span> (link.includes(<span class="hljs-string">"cdn-a.com"</span>)) &#123;
    link = link.replace(<span class="hljs-string">"cdn-a.com"</span>, <span class="hljs-string">"cdn-b.com"</span>);

    <span class="hljs-comment">// 创建script或者link标签，插入到head中</span>
    <span class="hljs-keyword">const</span> head = <span class="hljs-built_in">document</span>.head || <span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">"head"</span>)[<span class="hljs-number">0</span>];
    <span class="hljs-keyword">const</span> el = <span class="hljs-built_in">document</span>.createElement(nodeName);
    <span class="hljs-keyword">if</span> (el === <span class="hljs-string">"link"</span>) &#123;
      el.rel = <span class="hljs-string">"stylesheet"</span>;
    &#125;
    el[srcName] = link;
    el.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">window</span>.onCdnError(el);
    &#125;;
    el.setAttribute(<span class="hljs-string">"crossorigin"</span>, <span class="hljs-string">"anonymous"</span>);
    head.appendChild(el);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 可能已经是cdn-b了，此时cdn b也已经挂了，可以做一些提示处理</span>
    <span class="hljs-comment">// ...do something</span>
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            