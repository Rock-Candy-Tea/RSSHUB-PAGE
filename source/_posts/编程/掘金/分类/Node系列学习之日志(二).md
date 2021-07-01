
---
title: 'Node系列学习之日志(二)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6827'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 07:56:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=6827'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第30天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h3 data-id="heading-0">写日志</h3>
<p>新建<code>src/logs</code> 文件夹, 并新建<code>access.log</code>, <code>error.log</code>, <code>event.log</code> 三个日志文件</p>
<p>新建 <code>utils/log.js</code> 写封装的日志方法</p>
<p><code>utils/log.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-comment">// 写日志</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">writeLog</span>(<span class="hljs-params">writeStream, log</span>) </span>&#123;
  writeStream.write(log + <span class="hljs-string">'\n'</span>)
&#125;

<span class="hljs-comment">// 生成 write Stream</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createWriteStream</span>(<span class="hljs-params">fileName</span>) </span>&#123;
  <span class="hljs-keyword">const</span> fullFileName = path.join(__dirname, <span class="hljs-string">'../'</span>, <span class="hljs-string">'logs'</span>, fileName)
  <span class="hljs-keyword">const</span> writeStream = fs.createWriteStream(fullFileName, &#123;
    <span class="hljs-attr">flogs</span>: <span class="hljs-string">'a'</span>
  &#125;)
  <span class="hljs-keyword">return</span> writeStream
&#125;

<span class="hljs-comment">// 写访问日志</span>
<span class="hljs-keyword">const</span> accessWriteStream = createWriteStream(<span class="hljs-string">'access.log'</span>)
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">access</span>(<span class="hljs-params">log</span>) </span>&#123;
  writeLog(accessWriteStream, log)
&#125;
<span class="hljs-built_in">module</span>.exports = &#123;
  access
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后引入使用</p>
<p><code>app.js</code></p>
<pre><code class="hljs language-js copyable" lang="js">...
<span class="hljs-keyword">const</span> &#123;access&#125;  = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./src/utils/log'</span>)
...
<span class="hljs-keyword">const</span> serverHandle = <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  <span class="hljs-comment">// 记录 access log</span>
  access(<span class="hljs-string">`<span class="hljs-subst">$&#123;req.method&#125;</span> -- <span class="hljs-subst">$&#123;req.url&#125;</span> -- <span class="hljs-subst">$&#123;req.headers[<span class="hljs-string">'user-agent'</span>]&#125;</span> -- <span class="hljs-subst">$&#123;<span class="hljs-built_in">Date</span>.now()&#125;</span>`</span>)
  <span class="hljs-comment">// 设置返回格式</span>
  res.setHeader(<span class="hljs-string">'Content-Type'</span>, <span class="hljs-string">'application/json'</span>)

  <span class="hljs-comment">// 获取path</span>
  <span class="hljs-keyword">const</span> url = req.url
  req.path = url.split(<span class="hljs-string">'?'</span>)[<span class="hljs-number">0</span>]

  <span class="hljs-comment">// 解析 query</span>
  req.query = querystring.parse(url.split(<span class="hljs-string">'?'</span>)[<span class="hljs-number">1</span>])

  <span class="hljs-comment">// 解析cookie</span>
  req.cookie = &#123;&#125;
  <span class="hljs-keyword">const</span> cookieStr = req.headers.cookie || <span class="hljs-string">''</span>
  cookieStr.split(<span class="hljs-string">';'</span>).forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (!item) &#123;
      <span class="hljs-keyword">return</span>
    &#125;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'item: '</span>, item);
    <span class="hljs-keyword">const</span> arr = item.split(<span class="hljs-string">'='</span>)
    <span class="hljs-keyword">const</span> key = arr[<span class="hljs-number">0</span>].trim()
    <span class="hljs-keyword">const</span> val = arr[<span class="hljs-number">1</span>].trim()
    req.cookie[key] = val
  &#125;)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'req.cookie'</span>, req.cookie);
  <span class="hljs-comment">// 解析session, 使用redis</span>
  <span class="hljs-keyword">let</span> needSetCookie = <span class="hljs-literal">false</span> <span class="hljs-comment">// 是否设置Set-Cookie, 默认为false</span>
  <span class="hljs-keyword">let</span> userId = req.cookie.userId <span class="hljs-comment">// 在req中获取userId</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'userId'</span>, req.cookie.userId);
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
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'sessionData'</span>,sessionData);
      <span class="hljs-comment">// debugger</span>
      <span class="hljs-comment">// redis中的sessionData为null时</span>
      <span class="hljs-keyword">if</span> (sessionData == <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-comment">// 初始化 redis 中的 session 值</span>
        set(req.sessionId, &#123;&#125;)
        <span class="hljs-comment">// 设置session</span>
        req.session = &#123;&#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        req.session = sessionData
      &#125;
      <span class="hljs-comment">// 处理 postData</span>
      <span class="hljs-keyword">return</span> getPostData(req)
    &#125;)
    .then(<span class="hljs-function"><span class="hljs-params">postData</span> =></span> &#123;
      req.body = postData
      <span class="hljs-comment">// 处理 blog 路由 旧</span>

      <span class="hljs-comment">// const blogData = handleBlogRouter(req, res)</span>
      <span class="hljs-comment">// if (blogData) &#123;</span>
      <span class="hljs-comment">//   res.end(JSON.stringify(blogData))</span>
      <span class="hljs-comment">//   return</span>
      <span class="hljs-comment">// &#125;</span>

      <span class="hljs-comment">// 处理 blog 路由 新</span>
      <span class="hljs-keyword">const</span> blogResult = handleBlogRouter(req, res)
      <span class="hljs-keyword">if</span> (blogResult) &#123;
        blogResult.then(<span class="hljs-function"><span class="hljs-params">blogData</span> =></span> &#123;
          <span class="hljs-comment">// 路由处理完成后, 如果needSetCookie为true时,设置Set-Cookie</span>
          <span class="hljs-keyword">if</span> (needSetCookie) &#123;
            res.setHeader(<span class="hljs-string">'Set-Cookie'</span>, <span class="hljs-string">`userId=<span class="hljs-subst">$&#123;userId&#125;</span>; path=/; httponly; expires=<span class="hljs-subst">$&#123;getCookieExpires()&#125;</span>`</span>)
            needSetCookie = <span class="hljs-literal">false</span>
          &#125;
          res.end(<span class="hljs-built_in">JSON</span>.stringify(blogData))
        &#125;)
        <span class="hljs-keyword">return</span>
      &#125;

      <span class="hljs-comment">// 处理 user 路由</span>
      <span class="hljs-comment">// const userData = handleUserRouter(req, res)</span>
      <span class="hljs-comment">// if (userData) &#123;</span>
      <span class="hljs-comment">//   res.end(JSON.stringify(userData))</span>
      <span class="hljs-comment">//   return</span>
      <span class="hljs-comment">// &#125;</span>
      <span class="hljs-keyword">const</span> userResult = handleUserRouter(req, res)
      <span class="hljs-keyword">if</span> (userResult) &#123;
        userResult.then(<span class="hljs-function"><span class="hljs-params">userData</span> =></span> &#123;
          <span class="hljs-comment">// 路由处理完成后, 如果needSetCookie为true时,设置Set-Cookie</span>
          <span class="hljs-keyword">if</span> (needSetCookie) &#123;
            res.setHeader(<span class="hljs-string">'Set-Cookie'</span>, <span class="hljs-string">`userId=<span class="hljs-subst">$&#123;userId&#125;</span>; path=/; httponly; expires=<span class="hljs-subst">$&#123;getCookieExpires()&#125;</span>`</span>)
            needSetCookie = <span class="hljs-literal">false</span>
          &#125;
          res.end(<span class="hljs-built_in">JSON</span>.stringify(userData))
        &#125;)
        <span class="hljs-keyword">return</span>
      &#125;

      <span class="hljs-comment">// 未命中路由, 返回404</span>
      res.writeHead(<span class="hljs-number">404</span>, &#123; <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'text/plain'</span> &#125;)
      res.write(<span class="hljs-string">'404 Not Found\n'</span>)
      res.end()
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后刷新一下接口, 发现 <code>access.log</code> 中写入记录</p>
<pre><code class="hljs language-txt copyable" lang="txt">GET -- /api/blog/list?isadmin=1 -- Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 -- 1625066885837
GET -- /api/blog/list?isadmin=1 -- Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 -- 1625066886470
GET -- /api/blog/list?isadmin=1 -- Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 -- 1625066887164
GET -- /api/blog/detail?id=17 -- Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 -- 1625066917923
GET -- /api/blog/detail?id=17 -- Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 -- 1625066919531
GET -- /api/blog/list?isadmin=1 -- Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 -- 1625066920573
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">日志拆分</h3>
<p>在<code>utils</code> 下新建 <code>copy.sh</code></p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash">!/bin/sh</span>
cd D:/GithubPro/node-blog/src/logs
cp access.log $(date +%Y-%m-%d).access.log
echo "" > access.log
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在执行命令的时候会将当前日志备份, 并以时间戳重命名, 完成后清空当前日志内容~</p></div>  
</div>
            