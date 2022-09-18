
---
title: 'axios二次封装和请求发送'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f52aeaf4b594372803ab93cd3f3454a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 18:17:23 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f52aeaf4b594372803ab93cd3f3454a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">axios二次封装和请求发送</h2>
<p>我使用的例子是登录注册发请求的例子</p>
<p>1.axios二次封装</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>  <span class="hljs-comment">//导入axios</span>

<span class="hljs-comment">//创建axios对象</span>
<span class="hljs-keyword">const</span> request = axios.<span class="hljs-title function_">create</span>(&#123;   

  <span class="hljs-attr">baseURL</span>: <span class="hljs-string">'http://toutiao.itheima.net'</span> <span class="hljs-comment">//接口基准路径</span>

&#125;)


<span class="hljs-comment">// 请求拦截器  1，可以在这里添加token</span>

request.<span class="hljs-property">interceptors</span>.<span class="hljs-property">request</span>.<span class="hljs-title function_">use</span>(<span class="hljs-keyword">function</span> (<span class="hljs-params">config</span>) &#123;

  <span class="hljs-comment">// 在发送请求之前做些什么</span>

  <span class="hljs-keyword">const</span> &#123; user&#125; = store.<span class="hljs-property">state</span>

  <span class="hljs-keyword">if</span> (user && user.<span class="hljs-property">token</span>) &#123;

    config.<span class="hljs-property">headers</span>.<span class="hljs-property">Authorization</span> = <span class="hljs-string">`Bearer <span class="hljs-subst">$&#123;store.state.user.token&#125;</span>`</span>

  &#125;

  <span class="hljs-keyword">return</span> config;

&#125;, <span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) &#123;

  <span class="hljs-comment">// 对请求错误做些什么</span>

  <span class="hljs-keyword">return</span> <span class="hljs-title class_">Promise</span>.<span class="hljs-title function_">reject</span>(error);

&#125;);

<span class="hljs-comment">// 添加响应拦截器</span>

 request.<span class="hljs-property">interceptors</span>.<span class="hljs-property">response</span>.<span class="hljs-title function_">use</span>(<span class="hljs-keyword">function</span> (<span class="hljs-params">response</span>) &#123;

<span class="hljs-comment">//   // 2xx 范围内的状态码都会触发该函数。</span>

<span class="hljs-comment">//   // 对响应数据做点什么</span>

  <span class="hljs-keyword">return</span> response;

 &#125;, <span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) &#123;

<span class="hljs-comment">//   // 超出 2xx 范围的状态码都会触发该函数。</span>

<span class="hljs-comment">//   // 对响应错误做点什么</span>
   <span class="hljs-keyword">return</span> <span class="hljs-title class_">Promise</span>.<span class="hljs-title function_">reject</span>(error);

  &#125;);

<span class="hljs-comment">//最后导出request</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> request
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.创建api文件夹，用来管理请求，在这里我们就可以创建 ./src/api/user.js用来管理登录页面的请求</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 用户登录请求模块 user.js</span>

<span class="hljs-keyword">import</span> request <span class="hljs-keyword">from</span> <span class="hljs-string">"@/utils/request"</span>; <span class="hljs-comment">//导入axios实例对象，待会会使用这个对象去发请求</span>

<span class="hljs-comment">//axios是在原地返回得到promise对象,then（）/catch()拿到成功或者失败的内容,这两个是promise原生带的方法</span>
<span class="hljs-keyword">export</span>  <span class="hljs-keyword">const</span> <span class="hljs-title function_">login</span> = (<span class="hljs-params">data</span>) => &#123;     <span class="hljs-comment">//data是参数，里面传入登录信息</span>

 <span class="hljs-keyword">return</span> <span class="hljs-title function_">request</span>(&#123;  

  <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,   <span class="hljs-comment">//请求方法，get post </span>

  <span class="hljs-attr">url</span>: <span class="hljs-string">'/v1_0/authorizations'</span>,

  data

 &#125;)

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.在组件中，调用发请求，我采用的是Async/Await 调用，这种比较优雅的调用方式（强烈推荐）</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">//表单提交事件触发onSubmit（）</span>
<span class="hljs-attr">methods</span>: &#123;

  <span class="hljs-comment">// 验证表单函数</span>

  <span class="hljs-keyword">async</span> <span class="hljs-title function_">onSubmit</span>(<span class="hljs-params">values</span>) &#123;

   <span class="hljs-comment">// 获取表单验证</span>

   <span class="hljs-keyword">const</span> user = <span class="hljs-variable language_">this</span>.<span class="hljs-property">user</span>;

   <span class="hljs-keyword">try</span> &#123;

​    <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> <span class="hljs-title function_">login</span>(user)  <span class="hljs-comment">//在这里我们调用刚才在user.js中封装的login请求，会在原地得到promise对象,</span>
                                       <span class="hljs-comment">//使用res来接收我们请求回来的信息</span>

​    <span class="hljs-comment">// 存储token</span>

​    <span class="hljs-variable language_">this</span>.<span class="hljs-property">$store</span>.<span class="hljs-title function_">commit</span>(<span class="hljs-string">'setUser'</span>, res.<span class="hljs-property">data</span>.<span class="hljs-property">data</span>)

​    <span class="hljs-comment">// 为了数据刷新还在，采用本地存储，然后store重本地存储里面获取</span>

​    <span class="hljs-comment">// 根据请求响应结果处理后续操作</span>

​    <span class="hljs-variable language_">this</span>.<span class="hljs-property">$toast</span>.<span class="hljs-title function_">success</span>(<span class="hljs-string">'登录成功'</span>)  <span class="hljs-comment">//执行到这个地方的时候，会把前面的窗口关闭</span>

​    <span class="hljs-variable language_">this</span>.<span class="hljs-property">$router</span>.<span class="hljs-title function_">back</span>()

   &#125; <span class="hljs-keyword">catch</span> (error) &#123;
       <span class="hljs-comment">//在这里处理错误信息</span>

  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">接口调用： async/await 处理异步操作</h2>
<p><code>async/await</code> 是ES7 引入的新语法，可以更加方便的进行异步操作</p>
<ol>
<li><code>async</code> 作为一个关键字放到<strong>函数前面</strong></li>
<li>任何一个 async 函数都会隐式返回一个 promise**</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">await</span><span class="hljs-string">` 关键字只能在使用 `</span><span class="hljs-keyword">async</span> 定义的函数中使用
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>await后面可以直接跟一个 <strong>Promise实例对象</strong></li>
<li>await函数不能单独使用</li>
</ol>
<p>具体的async/await可以前往MDN详细了解</p>
<p>最后向各位掘友求个关注点赞</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f52aeaf4b594372803ab93cd3f3454a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="09DD7F96.gif" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            