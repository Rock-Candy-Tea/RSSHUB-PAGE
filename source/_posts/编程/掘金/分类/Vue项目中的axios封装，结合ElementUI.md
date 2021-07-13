
---
title: 'Vue项目中的axios封装，结合ElementUI'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7505'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 00:59:31 GMT
thumbnail: 'https://picsum.photos/400/300?random=7505'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>日常生活中开发Vue的项目总是免不了要封装axios，今天得空索性写个完完整整的axios封装，结合ElementUI组件库的提示功能，实用性还是不错的。</p>
<p>废话少说，代码贴出如下，如有不正确的地方，欢迎指正：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>

<span class="hljs-comment">// 这里的Message是按需导入的，和VantUI的类似，根据自己的需要决定</span>
<span class="hljs-keyword">import</span> &#123; Message &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'element-ui'</span>

<span class="hljs-comment">// 错误代码消息提示框</span>
<span class="hljs-keyword">const</span> tip = <span class="hljs-function"><span class="hljs-params">message</span> =></span> &#123;
  Message(&#123;
    message,
    <span class="hljs-attr">duration</span>: <span class="hljs-number">1000</span>,
    <span class="hljs-attr">type</span>: <span class="hljs-string">'error'</span>
  &#125;)
&#125;

<span class="hljs-comment">// 错误代码捕获</span>
<span class="hljs-keyword">const</span> errorHandler = <span class="hljs-function">(<span class="hljs-params">status</span>) =></span> &#123;
  <span class="hljs-keyword">switch</span> (status) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-number">302</span>:
      tip(<span class="hljs-string">'接口重定向'</span>)
      <span class="hljs-keyword">break</span>

    <span class="hljs-keyword">case</span> <span class="hljs-number">400</span>:
      tip(<span class="hljs-string">'请求错误'</span>)
      <span class="hljs-keyword">break</span>

    <span class="hljs-keyword">case</span> <span class="hljs-number">401</span>:
      tip(<span class="hljs-string">'未授权，请重新登陆'</span>)
      <span class="hljs-keyword">break</span>

    <span class="hljs-keyword">case</span> <span class="hljs-number">403</span>:
      tip(<span class="hljs-string">'没有操作权限'</span>)
      <span class="hljs-keyword">break</span>

    <span class="hljs-keyword">case</span> <span class="hljs-number">404</span>:
      tip(<span class="hljs-string">'请求地址出错'</span>)
      <span class="hljs-keyword">break</span>

    <span class="hljs-keyword">case</span> <span class="hljs-number">405</span>:
      tip(<span class="hljs-string">'请求方法不被允许'</span>)
      <span class="hljs-keyword">break</span>

    <span class="hljs-keyword">case</span> <span class="hljs-number">408</span>:
      tip(<span class="hljs-string">'请求超时'</span>)
      <span class="hljs-keyword">break</span>

    <span class="hljs-keyword">case</span> <span class="hljs-number">500</span>:
      tip(<span class="hljs-string">'服务器错误'</span>)
      <span class="hljs-keyword">break</span>

    <span class="hljs-keyword">case</span> <span class="hljs-number">501</span>:
      tip(<span class="hljs-string">'服务未实现'</span>)
      <span class="hljs-keyword">break</span>

    <span class="hljs-keyword">case</span> <span class="hljs-number">502</span>:
      tip(<span class="hljs-string">'网关错误'</span>)
      <span class="hljs-keyword">break</span>

    <span class="hljs-keyword">case</span> <span class="hljs-number">503</span>:
      tip(<span class="hljs-string">'服务不可用'</span>)
      <span class="hljs-keyword">break</span>

    <span class="hljs-keyword">case</span> <span class="hljs-number">504</span>:
      tip(<span class="hljs-string">'服务暂时无法访问，请稍后再试'</span>)
      <span class="hljs-keyword">break</span>

    <span class="hljs-keyword">case</span> <span class="hljs-number">505</span>:
      tip(<span class="hljs-string">'HTTP版本不受支持'</span>)
      <span class="hljs-keyword">break</span>

    <span class="hljs-attr">default</span>:
      tip(<span class="hljs-string">'系统错误，请稍候重试'</span>)
      <span class="hljs-keyword">break</span>
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HttpRequest</span> </span>&#123;
  <span class="hljs-comment">// 设置基准路径</span>
  <span class="hljs-title">constructor</span> (<span class="hljs-params">baseURL</span>) &#123;
    <span class="hljs-comment">// baseURL表示的是基准的URL地址，例如;https://www.cghbh.com/api/v1/</span>
    <span class="hljs-comment">// 请求中的url表示的是api的路由，例如http.get('/users')</span>
    <span class="hljs-comment">// 上面的两段就合并成了这样的请求:https://www.cghbh.com/api/v1/users</span>
    <span class="hljs-built_in">this</span>.baseURL = baseURL
  &#125;

  <span class="hljs-comment">// 设置axios的实例配置</span>
  getInstanceConfig () &#123;
    <span class="hljs-keyword">const</span> config = &#123;
      <span class="hljs-attr">timeout</span>: <span class="hljs-number">10000</span>,
      <span class="hljs-attr">baseURL</span>: <span class="hljs-built_in">this</span>.baseURL,
      <span class="hljs-attr">headers</span>: &#123;
        <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'application/json;charset=utf-8'</span>
      &#125;
    &#125;
    <span class="hljs-keyword">return</span> config
  &#125;

  <span class="hljs-comment">// 设置拦截器</span>
  interceptors (instance) &#123;
    <span class="hljs-comment">// 请求拦截器</span>
    instance.interceptors.request.use(<span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
      <span class="hljs-comment">// 这里的token是用户登陆之后获取的，现在暂时乱写</span>
      <span class="hljs-keyword">const</span> token = <span class="hljs-string">'jxnwejjwsnwjswswxwxdw'</span>
      token && (config.headers.Authorization = <span class="hljs-string">`Bear <span class="hljs-subst">$&#123;token&#125;</span>`</span>)
      <span class="hljs-keyword">return</span> config
    &#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
      <span class="hljs-built_in">Promise</span>.reject(error)
    &#125;)

    <span class="hljs-comment">// 响应拦截器</span>
    instance.interceptors.response.use(<span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(result.data)
    &#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
      <span class="hljs-keyword">const</span> &#123; response &#125; = error
      <span class="hljs-keyword">if</span> (response) &#123;
        errorHandler(response.status)
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(response)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.navigator.onLine) &#123;
          tip(<span class="hljs-string">'断网了'</span>)
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error)
        &#125;
      &#125;
    &#125;)
  &#125;

  <span class="hljs-comment">// 创建请求的实例，也可以发DELETE和PUT等请求</span>
  request (options) &#123;
    <span class="hljs-keyword">const</span> instance = axios.create()
    <span class="hljs-keyword">const</span> newOptions = <span class="hljs-built_in">Object</span>.assign(<span class="hljs-built_in">this</span>.getInstanceConfig(), options)
    <span class="hljs-comment">// 拦截器操作</span>
    <span class="hljs-built_in">this</span>.interceptors(instance)
    <span class="hljs-keyword">return</span> instance(newOptions)
  &#125;

  <span class="hljs-comment">// get请求</span>
  get (url, config) &#123;
    <span class="hljs-keyword">const</span> options = <span class="hljs-built_in">Object</span>.assign(&#123;
      <span class="hljs-attr">method</span>: <span class="hljs-string">'GET'</span>,
      <span class="hljs-attr">url</span>: url
    &#125;, config)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.request(options)
  &#125;

  post (url, data) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.request(&#123;
      url,
      <span class="hljs-attr">method</span>: <span class="hljs-string">'POST'</span>,
      data
    &#125;)
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> HttpRequest
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            