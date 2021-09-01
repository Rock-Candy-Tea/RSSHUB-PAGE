
---
title: '聊聊Promise的值穿透和异常穿透。'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b2ae406f0f647daa3a5280a0addbadb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 05:53:24 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b2ae406f0f647daa3a5280a0addbadb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">值穿透</h2>
<p>值穿透指的是，链式调用的参数不是函数时，会发生值穿透，就传入的非函数值忽略，传入的是之前的函数参数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">1</span>)
    .then(<span class="hljs-number">2</span>)
    .then(<span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">3</span>))
    .then(<span class="hljs-built_in">console</span>.log)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b2ae406f0f647daa3a5280a0addbadb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
传入2或者promise的fulfilled状态都会发生值穿透。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">1</span>)
    .then(<span class="hljs-function">() =></span> &#123; <span class="hljs-keyword">return</span> <span class="hljs-number">2</span> &#125;)
    .then(<span class="hljs-function">() =></span> &#123; <span class="hljs-keyword">return</span> <span class="hljs-number">3</span> &#125;)
    .then(<span class="hljs-built_in">console</span>.log)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f8b399c94ff4b44b6b28b48db397b47~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">1</span>)
    .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">2</span>
    &#125;)
    .then(<span class="hljs-function">() =></span> &#123; <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">3</span>) &#125;)
    .then(<span class="hljs-built_in">console</span>.log)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/281df78645064370baa0bee46b5c82f8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
只有传入的是函数才会传递给下一个链式调用。</p>
<h2 data-id="heading-1">异常穿透</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.reject(<span class="hljs-number">1</span>)
    .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(res);
    &#125;)
    .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123; <span class="hljs-built_in">console</span>.log(res) &#125;,
        <span class="hljs-function"><span class="hljs-params">rej</span> =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`rej****<span class="hljs-subst">$&#123;rej&#125;</span>`</span>);
        &#125;)
    .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`err****<span class="hljs-subst">$&#123;err&#125;</span>`</span>);
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9541a66c95424bdc99293043f9f0c169~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
当在then中传入了第二个函数，就不会被catch捕获到错误了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.reject(<span class="hljs-number">1</span>)
    .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(res);
    &#125;)
    .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123; <span class="hljs-built_in">console</span>.log(res) &#125;,
        <span class="hljs-function"><span class="hljs-params">rej</span> =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`rej****<span class="hljs-subst">$&#123;rej&#125;</span>`</span>);
        &#125;)
    .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`res****<span class="hljs-subst">$&#123;res&#125;</span>`</span>);
    &#125;, <span class="hljs-function"><span class="hljs-params">rej</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`rej****<span class="hljs-subst">$&#123;rej&#125;</span>`</span>);
    &#125;)
    .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`err<span class="hljs-subst">$&#123;err&#125;</span>`</span>);
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/536550842278420cb9c2896f54ea2d79~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
被then捕获的错误也会传给下一个链式调用成功的状态，虽然为undefined。</p>
<p><strong>记录记录！</strong></p></div>  
</div>
            