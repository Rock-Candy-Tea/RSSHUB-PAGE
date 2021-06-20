
---
title: 'Node系列学习之Redis(二)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9269'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 07:56:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=9269'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第19天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h3 data-id="heading-0">工具函数封装</h3>
<blockquote>
<p>在上一篇文章中封装了node中使用redis的工具函数,再简单看一下:</p>
</blockquote>
<p><code>src/conf/db.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> env = process.env.NODE_ENV <span class="hljs-comment">// 获取环境参数</span>
<span class="hljs-comment">// 配置</span>
<span class="hljs-keyword">let</span> MYSQL_CONF
<span class="hljs-keyword">let</span> REDIS_CONF

<span class="hljs-keyword">if</span> (env == <span class="hljs-string">'dev'</span>) &#123;
  <span class="hljs-comment">// mysql</span>
  MYSQL_CONF = &#123;
    <span class="hljs-attr">host</span>: <span class="hljs-string">'localhost'</span>,
    <span class="hljs-attr">user</span>: <span class="hljs-string">'root'</span>,
    <span class="hljs-attr">password</span>: <span class="hljs-string">'wyf666...'</span>,
    <span class="hljs-attr">port</span>: <span class="hljs-string">'3306'</span>,
    <span class="hljs-attr">database</span>: <span class="hljs-string">'myblog'</span>
  &#125;
  <span class="hljs-comment">// redis</span>
  REDIS_CONF = &#123;
    <span class="hljs-attr">port</span>: <span class="hljs-number">6379</span>,
    <span class="hljs-attr">host</span>: <span class="hljs-string">'127.0.0.1'</span>
  &#125;
&#125;
<span class="hljs-keyword">if</span> (env == <span class="hljs-string">'production'</span>) &#123;
  MYSQL_CONF = &#123;
    <span class="hljs-attr">host</span>: <span class="hljs-string">'localhost'</span>,
    <span class="hljs-attr">user</span>: <span class="hljs-string">'root'</span>,
    <span class="hljs-attr">password</span>: <span class="hljs-string">'wyf666...'</span>,
    <span class="hljs-attr">port</span>: <span class="hljs-string">'3306'</span>,
    <span class="hljs-attr">database</span>: <span class="hljs-string">'myblog'</span>
  &#125;,
  <span class="hljs-comment">// redis</span>
  REDIS_CONF = &#123;
    <span class="hljs-attr">port</span>: <span class="hljs-number">6379</span>,
    <span class="hljs-attr">host</span>: <span class="hljs-string">'127.0.0.1'</span>
  &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = &#123;
  MYSQL_CONF,
  REDIS_CONF
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>db/redis.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> redis = <span class="hljs-built_in">require</span>(<span class="hljs-string">'redis'</span>)
<span class="hljs-keyword">const</span> &#123; REDIS_CONF &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../conf/db'</span>)

<span class="hljs-comment">// 创建客户端</span>
<span class="hljs-keyword">const</span> redisClient = redis.createClient(REDIS_CONF.port, REDIS_CONF.host)
redisClient.on(<span class="hljs-string">'error'</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.error(err)
&#125;)
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">set</span>(<span class="hljs-params">key, val</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> val == <span class="hljs-string">'object'</span>) &#123;
    val = <span class="hljs-built_in">JSON</span>.stringify(val)
  &#125;
  redisClient.set(key, val, redis.print)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">get</span>(<span class="hljs-params">key</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    redisClient.get(key, <span class="hljs-function">(<span class="hljs-params">err, val</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (err) &#123;
        reject(err)
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-keyword">if</span>(val == <span class="hljs-literal">null</span>) &#123;
        resolve(<span class="hljs-literal">null</span>)
        <span class="hljs-keyword">return</span> 
      &#125;
      <span class="hljs-keyword">try</span> &#123;
        resolve(<span class="hljs-built_in">JSON</span>.parse(val))
      &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        resolve(val)
      &#125;
    &#125;)
  &#125;)
&#125;
<span class="hljs-built_in">module</span>.exports = &#123;
  set,
  get
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>工具函数暴露了两个方法, get() 和 set, 分别设置和取出 redis中的数据</p>
</blockquote>
<h3 data-id="heading-1">redis的使用</h3>
<pre><code class="hljs language-js copyable" lang="js">...
<span class="hljs-comment">// 引入工具函数方法</span>
<span class="hljs-keyword">const</span> &#123; get, set &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./src/db/redis'</span>)
...
  <span class="hljs-comment">// 解析session, 使用redis</span>
  <span class="hljs-keyword">let</span> needSetCookie = <span class="hljs-literal">false</span> <span class="hljs-comment">// 是否设置Set-Cookie, 默认为false</span>
  <span class="hljs-keyword">let</span> userId = req.cookie.userId <span class="hljs-comment">// 在req中获取userId</span>
  <span class="hljs-comment">// 对是否存在userId分别进行处理</span>
  <span class="hljs-keyword">if</span> (!userId) &#123;
    needSetCookie = <span class="hljs-literal">true</span> <span class="hljs-comment">// 打开需要服务端设置Cookie开关</span>
    userId = <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">Date</span>.now()&#125;</span>_<span class="hljs-subst">$&#123;<span class="hljs-built_in">Math</span>.random()&#125;</span>`</span> <span class="hljs-comment">// 随机生成userId</span>
    <span class="hljs-comment">// 初始化 redis 中的 session 值</span>
    set(userId, &#123;&#125;)
  &#125;
  <span class="hljs-comment">// 获取session</span>
  req.sessionId = userId <span class="hljs-comment">// 设置req.sessionId</span>
  get(req.sessionId)
    .then(<span class="hljs-function"><span class="hljs-params">sessionData</span> =></span> &#123;
      <span class="hljs-comment">// redis中的sessionData为null时</span>
      <span class="hljs-keyword">if</span> (sessionData == <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-comment">// 初始化 redis 中的 session 值</span>
        set(req.sessionId, &#123;&#125;)
        <span class="hljs-comment">// 设置session</span>
        req.session = &#123;&#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        req.session = sessionData
      &#125;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'req.session: '</span>, req.session)
      <span class="hljs-comment">// 处理 postData</span>
      <span class="hljs-keyword">return</span> getPostData(req)
    &#125;)
    .then(<span class="hljs-function"><span class="hljs-params">postData</span> =></span> &#123;...&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>src/router/user.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; login &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../controller/user'</span>)
<span class="hljs-keyword">const</span> &#123; SuccessModel, ErrorModel &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../model/resModel'</span>)
<span class="hljs-keyword">const</span> &#123;set&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../db/redis'</span>)

<span class="hljs-keyword">const</span> handleUserRouter = <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> method = req.method

  <span class="hljs-comment">// 登录</span>
  <span class="hljs-keyword">if</span> (method == <span class="hljs-string">'POST'</span> && req.path == <span class="hljs-string">'/api/user/login'</span>) &#123;
    <span class="hljs-keyword">const</span> &#123; username, password &#125; = req.body
    <span class="hljs-keyword">const</span> result = login(username,password)
    <span class="hljs-keyword">return</span> result.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
      <span class="hljs-keyword">if</span>(data.username) &#123;
        <span class="hljs-comment">// 设置session</span>
        req.session.username = data.username
        req.session.realname = data.realname
        <span class="hljs-comment">// 同步到 redis</span>
        set(req.sessionId, req.session)
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> SuccessModel()
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> ErrorModel(<span class="hljs-string">'登录失败~'</span>)
    &#125;)
  &#125;

  <span class="hljs-comment">// 登录验证的测试</span>
  <span class="hljs-keyword">if</span>(method == <span class="hljs-string">'GET'</span> && req.path == <span class="hljs-string">'/api/user/login-test'</span>) &#123;
    <span class="hljs-keyword">if</span>(req.session.username) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-keyword">new</span> SuccessModel(&#123;
        <span class="hljs-attr">session</span>: req.session
      &#125;))
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-keyword">new</span> ErrorModel(<span class="hljs-string">'尚未登录~'</span>))
  &#125;
&#125;
<span class="hljs-built_in">module</span>.exports = handleUserRouter
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>在登录接口中将session中的数据同步到redis中</p>
</blockquote>
<p>今天就先到这了, redis的使用基本就是这样了, 回头再简单的在每个接口中稍微改动下, 将redis的get,set使用一下, 基本上登录就没问题了~</p></div>  
</div>
            