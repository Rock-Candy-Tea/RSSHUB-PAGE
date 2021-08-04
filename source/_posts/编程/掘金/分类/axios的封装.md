
---
title: 'axios的封装'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7046'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 21:53:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=7046'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在main.js中引入：
import axios from '@/assets/js/http.js'
Vue.use(axios);</p>
<p>在项目中使用：
this.$post(url, param).then((res) => &#123;
&#125;);</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//http.js</span>


<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">"axios"</span>



<span class="hljs-keyword">const</span> Axios = axios.create(&#123;
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">30000</span>,
  <span class="hljs-comment">//responseType:"json",</span>
  <span class="hljs-attr">withCredentials</span>:<span class="hljs-literal">false</span>,
&#125;);


<span class="hljs-comment">/**
  axios访问前的拦截，增加配置信息
  baseURL=反向代理的URL地址，配置在nginx、apache下有效,tomcat下请配置为/
  data=将json转换为字符发送
  headers = 设置HTTP头文件，其中token是登陆时从服务器获取的
  withCredentials = 提交时是否携带cookie
*/</span>

Axios.interceptors.request.use(

  <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;

    <span class="hljs-keyword">var</span> token = sessionStorage.getItem(<span class="hljs-string">"account.token"</span>) || <span class="hljs-string">""</span>;
    <span class="hljs-keyword">if</span> (token && token != <span class="hljs-string">""</span>) &#123;
      config.headers = &#123;
        <span class="hljs-string">"Authorization"</span>: <span class="hljs-string">'Bearer '</span> + token,
        <span class="hljs-string">'Content-Type'</span>:<span class="hljs-string">'application/json; charset=utf-8'</span>,  
      &#125;
    &#125;<span class="hljs-keyword">else</span>&#123;
      config.headers = &#123;
        <span class="hljs-string">'Content-Type'</span>:<span class="hljs-string">'application/x-www-form-urlencoded; charset=utf-8'</span>,  
      &#125;  
      config.data = Vue.prototype.qs.stringify(config.data)
    &#125;

    <span class="hljs-keyword">return</span> config;
  &#125;,
  <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error);
  &#125;

);



<span class="hljs-comment">/**
  axios响应时拦截处理
*/</span>
httpService.interceptors.response.use(
    <span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
        <span class="hljs-keyword">let</span> msg = <span class="hljs-string">""</span>
        <span class="hljs-keyword">if</span> (response.status == <span class="hljs-number">200</span>) &#123;
            <span class="hljs-keyword">switch</span> (response.data.code) &#123;
                <span class="hljs-keyword">case</span> <span class="hljs-number">1000</span>:
                    msg = response.data.msg
                    <span class="hljs-comment">// Message['success'](&#123;</span>
                    <span class="hljs-comment">//     background: true,</span>
                    <span class="hljs-comment">//     content: msg,</span>
                    <span class="hljs-comment">//     duration: 3</span>
                    <span class="hljs-comment">// &#125;)</span>
                    <span class="hljs-keyword">break</span>;
                <span class="hljs-keyword">default</span>:
                    msg = response.data.msg
                    Message[<span class="hljs-string">'error'</span>](&#123;
                        <span class="hljs-attr">background</span>: <span class="hljs-literal">true</span>,
                        <span class="hljs-attr">content</span>: msg,
                        <span class="hljs-attr">duration</span>: <span class="hljs-number">10</span>,
                        <span class="hljs-attr">closable</span>: <span class="hljs-literal">true</span>
                    &#125;)
                    
            &#125;
            <span class="hljs-comment">// 统一处理状态</span>
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(response.data.data)
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(response)
        &#125;
    &#125;,
    <span class="hljs-comment">// 处理处理</span>
    <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (error && error.response) &#123;
            <span class="hljs-keyword">switch</span> (error.response.status) &#123;
                <span class="hljs-keyword">case</span> <span class="hljs-number">400</span>:
                    error.message = <span class="hljs-string">'错误请求'</span>;                 
                    <span class="hljs-keyword">break</span>;
                <span class="hljs-keyword">case</span> <span class="hljs-number">401</span>:
                    error.message = <span class="hljs-string">'未授权，请重新登录'</span>;
                    <span class="hljs-keyword">break</span>;
                <span class="hljs-keyword">case</span> <span class="hljs-number">403</span>:
                    error.message = <span class="hljs-string">'拒绝访问'</span>;
                    <span class="hljs-keyword">break</span>;
                <span class="hljs-keyword">case</span> <span class="hljs-number">404</span>:
                    error.message = <span class="hljs-string">'请求错误,未找到该资源'</span>;
                    <span class="hljs-keyword">break</span>;
                <span class="hljs-keyword">case</span> <span class="hljs-number">500</span>:
                    error.message = <span class="hljs-string">'服务器端出错'</span>;
                    <span class="hljs-keyword">break</span>;
                <span class="hljs-keyword">default</span>:
                    error.message = <span class="hljs-string">`未知错误<span class="hljs-subst">$&#123;error.response.status&#125;</span>`</span>;
            &#125;
            Message[<span class="hljs-string">'error'</span>](&#123;
                <span class="hljs-attr">background</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">content</span>: error.message,
                <span class="hljs-attr">duration</span>: <span class="hljs-number">10</span>,
                <span class="hljs-attr">closable</span>: <span class="hljs-literal">true</span>
            &#125;)
        &#125; <span class="hljs-keyword">else</span> &#123;
            error.message = <span class="hljs-string">"连接到服务器失败"</span>;
            Message[<span class="hljs-string">'error'</span>](&#123;
                <span class="hljs-attr">background</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">content</span>: error.message,
                <span class="hljs-attr">duration</span>: <span class="hljs-number">10</span>,
                <span class="hljs-attr">closable</span>: <span class="hljs-literal">true</span>
            &#125;)
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error);
    &#125;
)

<span class="hljs-comment">/**
 * 封装get方法
 * <span class="hljs-doctag">@param <span class="hljs-variable">url</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-variable">data</span></span>
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Promise&#125;</span></span>
 */</span>

<span class="hljs-keyword">const</span> get = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">url, param = &#123;&#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    Axios.get(url, &#123;
        <span class="hljs-attr">params</span>: <span class="hljs-built_in">JSON</span>.stringify(param),
      &#125;)
      .then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
        resolve(response.data);
      &#125;)
      .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        resolve(&#123;
          <span class="hljs-attr">code</span>: <span class="hljs-string">"no"</span>,
          <span class="hljs-attr">msg</span>: err.err
        &#125;);
        <span class="hljs-comment">//reject(err)</span>
      &#125;)
  &#125;) 
&#125;

<span class="hljs-keyword">const</span> post = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">url, param = &#123;&#125;, bURL=Vue.prototype.config.proxy</span>) </span>&#123;
  <span class="hljs-keyword">let</span> config = &#123;
    <span class="hljs-attr">baseURL</span>:bURL
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;    
    Axios.post(url, param, config).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
        resolve(response.data);

    &#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123; 
      <span class="hljs-keyword">var</span> t = err.err.response.data
      resolve(t);
    &#125;)
  &#125;)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">install</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">Vue, Option</span>) </span>&#123;
    <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">"$http"</span>, &#123;
      <span class="hljs-attr">value</span>: Axios
    &#125;);
    <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">"$get"</span>, &#123;
      <span class="hljs-attr">value</span>: get
    &#125;);
    <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">"$post"</span>, &#123;
      <span class="hljs-attr">value</span>: post
    &#125;);
  &#125;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            