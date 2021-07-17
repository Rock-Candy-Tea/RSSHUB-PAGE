
---
title: '【axios】不可不知的axios无感刷新token'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4401'
author: 掘金
comments: false
date: Fri, 16 Jul 2021 01:36:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=4401'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">背景</h4>
<p>最近项目用户登录页面处于安全考虑，登录之后的<code>access_token</code>并非永久有效而是有实效性了，因此
需要在用户登录之后<code>token</code>失效的情况下进行<code>access_token</code>的无感知刷新，也既是需要前端在<code>access_token</code>失效时调用一次<code>refresh API</code>使得<code>access_token</code>再次有效，而不影响用户的使用体验。</p>
<h4 data-id="heading-1">需求拆解</h4>
<p>用户登录成功之后<code>API</code>会将<code>&#123; access_token: '', refresh_token: '', expired: '' &#125;</code>返回，那就可以在用户发起一个请求时，判断<code>access_token</code>是否过期，过期就刷新<code>access_token</code>。首先判断<code>access_token</code>过期可以在请求之前根据<code>expired</code>判断，也可以在请求结果回来之后判断，问题的难点其实是指如何在多个请求进来时将这些请求暂存下来，然后在<code>refresh</code>之后在做请求场景还原。</p>
<h4 data-id="heading-2">实现思路</h4>
<p>针对需求拆解主要需要解决两个问题，一是失效判断，二是多个请求还原，具体解法如下：</p>
<ol>
<li>失效判断：（1）请求前根据<code>expired</code>的过期时间进行判断，但这种操作是不可靠的，因为时间是可修改的，所以不采用该方法；（2）根据请求结果判断<code>access_token</code>过期，然后进行刷新操作，然后在进行一次请求。</li>
<li>多请求的场景还原：当同时有多个过期请求进来时，需要避免多次<code>refresh</code>的请求，设置一个标志位，当已经有<code>refresh</code>的操作在进行时，再进来的请求进行挂起（此时可以利用<code>Promise</code>的<code>pending</code>状态做文章），等待<code>refresh</code>成功之后在进行请求。</li>
</ol>
<h4 data-id="heading-3">伪代码实现如下</h4>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> axios, &#123; AxiosRequestConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>;

<span class="hljs-keyword">interface</span> IRequestConfig &#123;
   <span class="hljs-attr">tokenInfoKey</span>: <span class="hljs-built_in">string</span>; <span class="hljs-comment">// 由于登录之后的 token 数据时存在 localstorage 需要键值</span>
   onRefreshError: VoidFunction;
&#125;

<span class="hljs-keyword">interface</span> ITokenInfo &#123;
    <span class="hljs-attr">access_token</span>: <span class="hljs-built_in">string</span>;
    refresh_token: <span class="hljs-built_in">string</span>;
    expired: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Request</span> </span>&#123;
  <span class="hljs-keyword">private</span> config: IRequestConfig = &#123;&#125;;
  <span class="hljs-keyword">private</span> tokenInfo: ITokenInfo | <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span>;
  <span class="hljs-keyword">private</span> isRefreshing: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>;
  <span class="hljs-keyword">private</span> needRetryRequest = [];
  <span class="hljs-title">constructor</span> (<span class="hljs-params">config: IRequestConfig</span>) &#123;
     <span class="hljs-keyword">const</span> &#123; tokenInfoKey &#125; = config;
     <span class="hljs-built_in">this</span>.tokenInfo = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">localStorage</span>.getItem(tokenInfoKey));
     <span class="hljs-built_in">this</span>.config = config;
  &#125;
  
  refreshAccessToken (onSuccess: VoidFunction) &#123;
      <span class="hljs-keyword">return</span> axios.request<ITokenInfo>(&#123;
          <span class="hljs-attr">url</span>: <span class="hljs-string">''</span>,
          <span class="hljs-attr">method</span>: <span class="hljs-string">''</span>,
      &#125;)
          .then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
              <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-built_in">this</span>.config.tokenInfoKey, res.data);
              onSuccess();
          &#125;)
          .catch(<span class="hljs-function">() =></span> &#123;
              <span class="hljs-built_in">this</span>.needRetryRequest = [];
          &#125;);
  &#125;
  
  request (config: AxiosRequestConfig) &#123;
     <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isRefreshing) &#123;
         <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
             <span class="hljs-built_in">this</span>.needRetryRequest.push(<span class="hljs-keyword">async</span> () => <span class="hljs-keyword">await</span> resolve(axios));
         &#125;);
     &#125;
     <span class="hljs-keyword">return</span> axios
       .request(config)
       .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
           <span class="hljs-keyword">return</span> res.data;
       &#125;)
       .catch(<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
           <span class="hljs-comment">// 假设 401401 定义需要 refresh</span>
           <span class="hljs-keyword">const</span> code = <span class="hljs-number">401401</span>;
           <span class="hljs-keyword">const</span> &#123; status &#125; = e.response;
           <span class="hljs-keyword">if</span> (status === code) &#123;
               <span class="hljs-built_in">this</span>.isRefreshing = <span class="hljs-literal">true</span>;
               <span class="hljs-built_in">this</span>.refreshAccessToken(<span class="hljs-function">() =></span> &#123;
                   <span class="hljs-built_in">Promise</span>.all([<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.request(config), ...this.needRetryRequest].map(<span class="hljs-function"><span class="hljs-params">cb</span> =></span> cb()));
               &#125;);
           &#125;
       &#125;)
       .finally(<span class="hljs-function">() =></span> &#123;
           <span class="hljs-built_in">this</span>.isRefreshing = <span class="hljs-literal">false</span>;
       &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            