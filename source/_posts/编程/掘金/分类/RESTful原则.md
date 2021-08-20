
---
title: 'RESTful原则'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9135'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 01:51:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=9135'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">RESTful 六大原则</h1>
<h2 data-id="heading-1">1. C-S 架构</h2>
<p>数据的存储在Server端，Client端只需使用就行。两端彻底分离的好处使client端代码的可移植性变强，Server端的拓展性变强。两端单独开发，互不干扰。</p>
<h2 data-id="heading-2">2. 无状态</h2>
<p>http请求本身就是无状态的，基于C-S架构，客户端的每一次请求带有充分的信息能够让服务端识别。请求所需的一些信息都包含在URL的查询参数、header、body，服务端能够根据请求的各种参数，无需保存客户端的状态，将响应正确返回给客户端。无状态的特征大大提高的服务端的健壮性和可拓展性。</p>
<p>当然这总无状态性的约束也是有缺点的，客户端的每一次请求都必须带上相同重复的信息确定自己的身份和状态（这也是必须的），造成传输数据的冗余性，但这种确定对于性能和使用来说，几乎是忽略不计的。</p>
<h2 data-id="heading-3">3. 统一的接口</h2>
<p>这个才是<strong>REST架构的核心</strong>，统一的接口对于RESTful服务非常重要。客户端只需要关注实现接口就可以，接口的可读性加强，使用人员方便调用。</p>
<h2 data-id="heading-4">4. 一致的数据格式</h2>
<p>服务端返回的数据格式要么是XML，要么是Json（获取数据），或者直接返回状态码。</p>
<p>系统分层：客户端通常无法表明自己是直接还是间接与端服务器进行连接，分层时同样要考虑安全策略。</p>
<h2 data-id="heading-5">5. 可缓存</h2>
<p>在万维网上，客户端可以缓存页面的响应内容。因此响应都应隐式或显式的定义为可缓存的，若不可缓存则要避免客户端在多次请求后用旧数据或脏数据来响应。管理得当的缓存会部分地或完全地除去客户端和服务端之间的交互，进一步改善性能和延展性。</p>
<h2 data-id="heading-6">6. 按需编码、可定制代码（可选）</h2>
<h2 data-id="heading-7">实践</h2>
<h3 data-id="heading-8">1. 版本</h3>
<pre><code class="copyable">https://example.com/api/v1/
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">2. 参数命名规范</h3>
<p>例如：驼峰命名法，下划线命名法</p>
<h3 data-id="heading-10">3. url命名规范</h3>
<pre><code class="copyable">https://example.com/api/getallUsers GET 获取所有用户
https://example.com/api/getuser/1 GET 获取标识为1用户信息
https://example.com/api/user/delete/1 GET/POST 删除标识为1用户信息
https://example.com/api/updateUser/1 POST 更新标识为1用户信息
https://example.com/api/User/add POST 添加新的用户
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">4. 统一返回数据格式</h3>
<p>例如json格式：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">//成功的响应</span>
&#123;
  <span class="hljs-attr">"code"</span>: <span class="hljs-number">200</span>,
  <span class="hljs-attr">"message"</span>: <span class="hljs-string">"success"</span>,
  <span class="hljs-attr">"data"</span>: &#123;
    <span class="hljs-attr">"userName"</span>: <span class="hljs-string">"123456"</span>,
    <span class="hljs-attr">"age"</span>: <span class="hljs-number">16</span>,
    <span class="hljs-attr">"address"</span>: <span class="hljs-string">"beijing"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">//失败的响应</span>
&#123;
  <span class="hljs-attr">"code"</span>: <span class="hljs-number">401</span>,
  <span class="hljs-attr">"message"</span>: <span class="hljs-string">"error  message"</span>,
  <span class="hljs-attr">"data"</span>: <span class="hljs-literal">null</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            