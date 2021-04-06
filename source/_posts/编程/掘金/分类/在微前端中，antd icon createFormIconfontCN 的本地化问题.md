
---
title: '在微前端中，antd icon createFormIconfontCN 的本地化问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/853dd0b1b1fd4e0ca0c5fe96fe33816a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 19:29:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/853dd0b1b1fd4e0ca0c5fe96fe33816a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>首发于 <a href="https://www.yuque.com/blueju" target="_blank" rel="nofollow noopener noreferrer">语雀文档</a></p>
</blockquote>
<p><a name="user-content-tCbT2" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-0">前言</h2>
<p>用过 antd icon 的朋友们可能知道，其中介绍的用法是：</p>
<blockquote>
<p><a href="https://ant.design/components/icon-cn/#components-icon-demo-iconfont" target="_blank" rel="nofollow noopener noreferrer">ant.design/components/…</a></p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createFromIconfontCN &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@ant-design/icons'</span>;

<span class="hljs-keyword">const</span> IconFont = createFromIconfontCN(&#123;
  <span class="hljs-attr">scriptUrl</span>: <span class="hljs-string">'//at.alicdn.com/t/font_8d5l8fzk5b87iudi.js'</span>,
&#125;);

ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"icons-list"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">IconFont</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"icon-tuichu"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">IconFont</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"icon-facebook"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">IconFont</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"icon-twitter"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>,
  mountNode,
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br>可以看出，提供的是：（相对路径引入 / 外链引入）的方式，<br>但对于一些内网开发者和微前端应用开发者，仍不太完全满足需求。<br></p>
<p><a name="user-content-XXLpa" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-1">对于内网开发者</h2>
<p>对于内网开发者，无法连接外网，使用相对路径引入的方式，能较好地解决图标资源本地化的问题。<br></p>
<p><a name="user-content-EjpKQ" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-2">对于微前端应用开发者</h2>
<p>但对于微前端应用开发者（比如说我们），相对路径引入的方式，仍无法满足我们解决图标资源本地化的问题。因为子应用一旦嵌入基座，由于浏览器中的 IP 域名就不再是子应用的 IP 域名，若请求未明确指定 IP 域名的情况下，请求会默认取浏览器中的 IP 域名（虽然大多是 umi+qiankun，会帮我处理绝大多数请求，让请求仍指向子应用的静态资源服务），如图：<br><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/853dd0b1b1fd4e0ca0c5fe96fe33816a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>font 的正确路径应该是：<a href="http://%E5%AD%90%E5%BA%94%E7%94%A8IP:%E5%AD%90%E5%BA%94%E7%94%A8%E7%AB%AF%E5%8F%A3/font.js%EF%BC%8C" target="_blank" rel="nofollow noopener noreferrer">http://子应用IP:子应用端口/font.js，</a>
但由于子应用在基座（即：主应用）中运行，此时使用的是相对路径，可以发现发出的资源请求 URL 变成了：<a href="http://%E4%B8%BB%E5%BA%94%E7%94%A8IP:%E4%B8%BB%E5%BA%94%E7%94%A8%E7%AB%AF%E5%8F%A3/font.js%EF%BC%8C%E8%BF%99%E6%98%8E%E6%98%BE%E4%B8%8D%E5%AF%B9%EF%BC%8C%E6%8A%A5%E4%BA%86" target="_blank" rel="nofollow noopener noreferrer">http://主应用IP:主应用端口/font.js，这明显不对，报了</a> 404 错误。</p>
</blockquote>
<p><a name="user-content-Z5DPK" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-3">我的解决方案</h2>
<blockquote>
<p>说实话，这并不难理解，只是当时一下子没想到，害我自己还去写了根据应用名获取对应应用地址，将其与图标资源文件进行路径拼接的方法。😂😂😂</p>
</blockquote>
<p>我在网上搜了不少，只找到相对路径引入的方式来解决图标资源本地化，但没看到有如下的解决方式。<br>在我看来，在没有更多时间去研究 umi 配置的情况下去解决图标资源本地化，这是最快的解决方案。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> IconFont = Icon.createFromIconfontCN(&#123;
  <span class="hljs-attr">scriptUrl</span>: <span class="hljs-built_in">require</span>(<span class="hljs-string">'../assets/js/font_8d5l8fzk.js'</span>),
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br>当然，还有一种办法，那就是：CDN / OSS</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            