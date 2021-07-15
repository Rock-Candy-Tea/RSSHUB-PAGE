
---
title: 'axios拦截器的使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5719'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 07:49:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=5719'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ol>
<li>新建request.js文件,导入axios</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>创建一个axios的实例</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> request = axios.create(&#123;
  <span class="hljs-attr">baseURL</span>: xxx,
  <span class="hljs-comment">// baseURL: '项目基地址'</span>
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">5000</span> <span class="hljs-comment">// 设置5秒延时关闭请求</span>
&#125;) 
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>设置请求拦截器</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// request.interceptors.request.use() // 请求拦截器</span>
request.interceptors.request.use(<span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
  
  config.headers.Authorization = <span class="hljs-string">`Bearer <span class="hljs-subst">$&#123;token&#125;</span>`</span> <span class="hljs-comment">// 设置请求头携带token</span>
  <span class="hljs-keyword">return</span> config 
&#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(error) <span class="hljs-comment">// 发生错误打印</span>
  <span class="hljs-keyword">return</span> error
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>设置响应拦截器</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// request.interceptors.response.use() // 响应拦截器</span>
request.interceptors.response.use(<span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
  <span class="hljs-keyword">return</span> config <span class="hljs-comment">// 成功直接返回</span>
&#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (error.response.status === <span class="hljs-number">401</span>) &#123; <span class="hljs-comment">//如果发生错误,查看错误码是多少 401为权限不够,token过期</span>
    alert(<span class="hljs-string">'token请求超时!请重新登录!'</span>)
    <span class="hljs-comment">// 进行操作,如删除vuex中过期用户数据等一系列操作</span>
    router.push(<span class="hljs-string">'/login'</span>) <span class="hljs-comment">// 强行返回到登录页</span>
  &#125;
  <span class="hljs-keyword">return</span> error
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>导出axios实例</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> request
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            