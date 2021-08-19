
---
title: '跨域-Vue-Cli配置代理转发'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3782'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 02:00:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=3782'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">跨域-Vue-Cli配置代理转发</h2>
<h3 data-id="heading-1">目标</h3>
<p>通过配置vue-cli请求代理解决开发环境下的跨域问题</p>
<h3 data-id="heading-2">vue-cli中集成的跨域解决方案</h3>
<p>具体有两步：</p>
<ol>
<li>在vue.config.js中配置devServer</li>
<li>确保基地址指向本地服务</li>
</ol>
<h3 data-id="heading-3">vue-cli解决跨域配置说明</h3>
<p>在<code>vue.config.js</code>配置文件中，有一项是devServer，它就是我们下边要操作的主角。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-comment">// 代理配置</span>
    <span class="hljs-attr">proxy</span>: &#123;
    <span class="hljs-comment">// 'http://localhost:3000' // 接口服务器</span>
      <span class="hljs-string">'/api'</span>: &#123;
        <span class="hljs-comment">// /api/users 的请求会将请求代理到 http://localhost:3000/api/users</span>
        <span class="hljs-attr">target</span>: <span class="hljs-string">'http://localhost:3000'</span> 
        <span class="hljs-comment">// 如果不希望传递/api，则需要重写路径</span>
        <span class="hljs-attr">pathRewrite</span>: &#123; <span class="hljs-string">'^/api'</span>: <span class="hljs-string">''</span> &#125;,
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">确保基地址指向本地服务</h3>
<p><code>.env.development</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 开发环境下的基地址</span>
VUE_APP_BASE_API = <span class="hljs-string">'/api'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>api/user.js</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">login</span>(<span class="hljs-params">formData</span>) </span>&#123;
  <span class="hljs-keyword">return</span> request(&#123;
<span class="hljs-comment">//  url: 'api/sys/login',</span>
+   url: <span class="hljs-string">'/sys/login'</span>, <span class="hljs-comment">// 前面的api就省略了</span>
    <span class="hljs-attr">method</span>: <span class="hljs-string">'POST'</span>,
    <span class="hljs-attr">data</span>: formData
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：</strong></p>
<ol>
<li>vue-cli集成了跨域代理功能------ <strong>只能用在开发阶段</strong>。</li>
<li>vue.config.js文件中，在devServe下按指定格式配置了proxy，再<strong>重启项目</strong>即可。</li>
<li>ajax的基地址baseUrl必须是相对地址，而不能是绝对地址</li>
</ol></div>  
</div>
            