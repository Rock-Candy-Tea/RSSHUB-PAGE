
---
title: '前后端联调解决cookie回写'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc961affef9945cb84179dc6a5f31093~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 28 Mar 2021 01:11:49 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc961affef9945cb84179dc6a5f31093~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>故事背景</strong><br>
在日常开发中，当我们需要和后端联调时候，发送接口请求的时候，后端会校验接口是否带上了<code>cookie</code>,如果没有，后端会返回一个<code>redirectUrl</code>,这个<code>redirectUrl</code>是线上的一个登录地址，
因此普遍的做法是登陆一下线上的系统，复制一下<code>cookie</code>，写入本地<code>webpack</code>的<code>cookie</code>,再次重启<code>webpack</code>。</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-regexp">/api/</span>: &#123;
        <span class="hljs-attr">headers</span>: &#123;
           <span class="hljs-attr">cookie</span>: <span class="hljs-string">'刚才登录拿到的线上的cookie'</span> 
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p><strong>产生的问题</strong></p>
<ol>
<li>当前调试的<code>cookie</code>如果失效，就需要重新登录，然后复制<code>cookie</code>，最后重启整个项目</li>
<li>每次提交代码时，都需要清空<code>cookie</code> 【因为<code>cookie</code>每次都不一样】</li>
<li>耗费了许多时间在这个复制<code>cookie</code>上</li>
</ol>
<hr>
<p><strong>原因分析</strong></p>
<ol>
<li>后端在进行接口调用的时候是每次都需要进行<code>cookie</code>校验</li>
<li><code>cookie</code>失效<code>redirectUrl</code>是写死的线上地址，不是根据<code>refere</code>判断的</li>
</ol>
<hr>
<p><strong>方案调研</strong></p>
<ol>
<li><code>cookie</code>不做失效校验</li>
<li><code>redirectUrl</code>根据<code>refere</code>来判断</li>
<li>前端通过<code>webpack</code>代理实现<code>cookie</code>的自动回写</li>
</ol>
<hr>
<p><strong>结果</strong></p>
<ul>
<li><code>cookie</code>和<code>redirectUrl</code>的这两个方案，对后端来说，改动量非常大，所以行不通</li>
<li>使用<code>webpack</code>自动回写</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> cookie = <span class="hljs-string">''</span>;
...
&#123;
    <span class="hljs-regexp">/api/</span>: &#123;
        <span class="hljs-comment">// 这个代表你要自定义处理返回的数据</span>
        <span class="hljs-attr">selfHandleResponse</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-function"><span class="hljs-title">onProxyReq</span>(<span class="hljs-params">proxyReq, req, res</span>)</span> &#123;
            <span class="hljs-comment">//每次请求之前设置一下 cookie</span>
            proxyReq.setHeader(<span class="hljs-string">'cookie'</span>, cookie);
        &#125;,
        <span class="hljs-function"><span class="hljs-title">onProxyRes</span>(<span class="hljs-params">proxyRes, req, res</span>)</span> &#123;
            <span class="hljs-keyword">if</span> (proxyRes.headers[<span class="hljs-string">'set-cookie'</span>]) &#123;
              <span class="hljs-comment">// 获取后端系统返回的 cookie</span>
              cookie = proxyRes.headers[<span class="hljs-string">'set-cookie'</span>].join(<span class="hljs-string">';'</span>);
            &#125;
            <span class="hljs-keyword">var</span> body = [];
            proxyRes.on(<span class="hljs-string">'data'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">chunk</span>) </span>&#123;
                body.push(chunk);
            &#125;);
            proxyRes.on(<span class="hljs-string">'end'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                body = <span class="hljs-built_in">JSON</span>.parse(Buffer.concat(body).toString());
                <span class="hljs-keyword">if</span> (!body.success && body.code === <span class="hljs-number">302</span>) &#123;
                  body.message.redirect = <span class="hljs-string">'http://localhost:3000'</span>;
                &#125;
                res.end(Buffer.from(<span class="hljs-built_in">JSON</span>.stringify(body)));
            &#125;);
      &#125;
    &#125;
&#125;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p><strong>讨论</strong><br>
这种方案只是对于点对点的系统有效果</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc961affef9945cb84179dc6a5f31093~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
如果是下面这种系统这个方案将会是无效的</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a073120ae4a4c6c99555be5e3be9589~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>那么这种该怎么解决呢？</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            