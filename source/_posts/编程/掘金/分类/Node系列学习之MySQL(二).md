
---
title: 'Node系列学习之MySQL(二)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2691'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 07:56:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=2691'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第11天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">封装SQL函数</h2>
<h3 data-id="heading-1">配置文件</h3>
<p>在 <code>src</code> 下新建 <code>conf</code> 文件夹,并在其下新建 <code>db.js</code></p>
<p><code>src/conf/db.js</code></p>
<pre><code class="hljs language-sjs copyable" lang="sjs">const env = process.env.NODE_ENV // 获取环境参数

let MYSQL_CONF

if (env == 'dev') &#123;
  MYSQL_CONF = &#123;
    host: 'localhost',
    user: 'root',
    password: '看不到看不到',
    port: '3306',
    database: 'myblog'
  &#125;
&#125;
if (env == 'production') &#123;
  MYSQL_CONF = &#123;
    host: 'localhost',
    user: 'root',
    password: '看不到看不到',
    port: '3306',
    database: 'myblog'
  &#125;
&#125;

module.exports = &#123;
  MYSQL_CONF
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>OK, <code>sql</code> 的配置完成.</p>
<h3 data-id="heading-2">函数封装</h3>
<p>在 <code>src</code> 下新建 <code>db</code> 文件夹, 并在其下新建 <code>mysql.js</code></p>
<p><code>src/db/mysql.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> mysql = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mysql'</span>)
<span class="hljs-keyword">const</span> &#123; MYSQL_CONF &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../conf/db'</span>)
<span class="hljs-comment">// 创建链接对象</span>
<span class="hljs-keyword">const</span> con = mysql.createConnection(MYSQL_CONF)

<span class="hljs-comment">// 开始连接</span>
con.connect()

<span class="hljs-comment">// 同意执行 sql 的函数</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">exec</span>(<span class="hljs-params">sql</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    con.query(sql, <span class="hljs-function">(<span class="hljs-params">err, result</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (err) &#123;
        reject(err)
        <span class="hljs-keyword">return</span>
      &#125;
      resolve(result)
    &#125;)
  &#125;)
&#125;
<span class="hljs-built_in">module</span>.exports = &#123;
  exec
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>OK,简单的一个SQL执行函数封装完成~</p>
<h2 data-id="heading-3">路由优化</h2>
<h3 data-id="heading-4">获取博客列表</h3>
<p><code>controller/blog.js</code></p>
<pre><code class="hljs language-js copyable" lang="js">...
<span class="hljs-keyword">const</span> getList = <span class="hljs-function">(<span class="hljs-params">author, keyword</span>) =></span> &#123;
  
  <span class="hljs-keyword">let</span> sql = <span class="hljs-string">`
    select * from blogs where 1=1 
  `</span>
  <span class="hljs-keyword">if</span> (author) &#123;
    sql += <span class="hljs-string">`and author='<span class="hljs-subst">$&#123;author&#125;</span>' `</span>
  &#125;
  <span class="hljs-keyword">if</span>(keyword) &#123;
    sql += <span class="hljs-string">`and title like '%<span class="hljs-subst">$&#123;keyword&#125;</span>%' `</span>
  &#125;
  sql += <span class="hljs-string">`order by createtime desc;`</span>
  <span class="hljs-comment">// 返回的是个Promise</span>
  <span class="hljs-keyword">return</span> exec(sql)
  
&#125;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>router/blog.js</code></p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// 获取博客列表</span>
  <span class="hljs-keyword">if</span> (method == <span class="hljs-string">'GET'</span> && req.path == <span class="hljs-string">'/api/blog/list'</span>) &#123;
    <span class="hljs-keyword">const</span> author = req.query.author || <span class="hljs-string">''</span>
    <span class="hljs-keyword">const</span> keyword = req.query.keyword || <span class="hljs-string">''</span>
    <span class="hljs-comment">// const listData = getList(author, keyword)</span>
    <span class="hljs-comment">// return new SuccessModel(listData)</span>
    <span class="hljs-keyword">const</span> result = getList(author,keyword)
    <span class="hljs-keyword">return</span> result.then(<span class="hljs-function"><span class="hljs-params">listData</span> =></span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> SuccessModel(listData)
    &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">获取博客详情</h3>
<p><code>controller/blog.js</code></p>
<pre><code class="hljs language-js copyable" lang="js">...
<span class="hljs-comment">// 博客详情</span>
<span class="hljs-keyword">const</span> getDetail = <span class="hljs-function"><span class="hljs-params">id</span> =></span> &#123;
  <span class="hljs-keyword">const</span> sql = <span class="hljs-string">`select * from blogs where id='<span class="hljs-subst">$&#123;id&#125;</span>' `</span>
  <span class="hljs-keyword">return</span> exec(sql).then(<span class="hljs-function"><span class="hljs-params">rows</span> =></span> &#123;
    <span class="hljs-keyword">return</span> rows[<span class="hljs-number">0</span>]
  &#125;)
&#125;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>router/blog.js</code></p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// 获取博客详情</span>
  <span class="hljs-keyword">if</span> (method == <span class="hljs-string">'GET'</span> && req.path == <span class="hljs-string">'/api/blog/detail'</span>) &#123;
    <span class="hljs-comment">// const data = getDetail(id)</span>
    <span class="hljs-comment">// return new SuccessModel(data)</span>
    <span class="hljs-keyword">const</span> result = getDetail(id)
    <span class="hljs-keyword">return</span> result.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> SuccessModel(data)
    &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">新建博客文章</h3>
<p><code>controller/blog.js</code></p>
<pre><code class="hljs language-js copyable" lang="js">...
<span class="hljs-comment">// 新建博客</span>
<span class="hljs-keyword">const</span> newBlog = <span class="hljs-function">(<span class="hljs-params">blogData = &#123;&#125;</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> title = blogData.title
  <span class="hljs-keyword">const</span> content = blogData.content
  <span class="hljs-keyword">const</span> author = blogData.author
  <span class="hljs-keyword">const</span> createTime = <span class="hljs-built_in">Date</span>.now()
  <span class="hljs-keyword">const</span> sql = <span class="hljs-string">`
    insert into blogs (title,content,createtime,author) values ('<span class="hljs-subst">$&#123;title&#125;</span>','<span class="hljs-subst">$&#123;content&#125;</span>',<span class="hljs-subst">$&#123;createTime&#125;</span>, '<span class="hljs-subst">$&#123;author&#125;</span>');
  `</span>
  <span class="hljs-keyword">return</span> exec(sql).then(<span class="hljs-function"><span class="hljs-params">insertData</span> =></span> &#123;
    <span class="hljs-comment">// console.log('insertData',insertData);</span>
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">id</span>: insertData.insertId
    &#125;
  &#125;)
&#125;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>router/blog.js</code></p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// 新建一篇博客</span>
  <span class="hljs-keyword">if</span> (method == <span class="hljs-string">'POST'</span> && req.path == <span class="hljs-string">'/api/blog/new'</span>) &#123;
    <span class="hljs-comment">// const data = newBlog(req.body)</span>
    <span class="hljs-comment">// return new SuccessModel(data)</span>
    req.body.author = <span class="hljs-string">'tmier'</span> <span class="hljs-comment">// 待开发登录完成后再改成真实数据</span>
    <span class="hljs-keyword">const</span> result = newBlog(req.body)
    <span class="hljs-keyword">return</span> result.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> SuccessModel(data)
    &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面改完之后,相应的<code>app.js</code> 也需要修改一下</p>
<p><code>app.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> querystring = <span class="hljs-built_in">require</span>(<span class="hljs-string">'querystring'</span>)
<span class="hljs-keyword">const</span> handleBlogRouter = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./src/router/blog.js'</span>)
<span class="hljs-keyword">const</span> handleUserRouter = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./src/router/user.js'</span>)

<span class="hljs-comment">// 用于处理 postData</span>
<span class="hljs-keyword">const</span> getPostData = <span class="hljs-function"><span class="hljs-params">req</span> =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (req.method !== <span class="hljs-string">'POST'</span>) &#123;
      resolve(&#123;&#125;)
      <span class="hljs-keyword">return</span>
    &#125;
    <span class="hljs-comment">// 非json数据类型,忽略并返回&#123;&#125;</span>
    <span class="hljs-keyword">if</span> (req.headers[<span class="hljs-string">'content-type'</span> !== <span class="hljs-string">'application/json'</span>]) &#123;
      resolve(&#123;&#125;)
      <span class="hljs-keyword">return</span>
    &#125;
    <span class="hljs-comment">// 正确的</span>
    <span class="hljs-keyword">let</span> postData = <span class="hljs-string">''</span>
    req.on(<span class="hljs-string">'data'</span>, <span class="hljs-function"><span class="hljs-params">chunk</span> =></span> &#123;
      postData += chunk.toString()
    &#125;)
    req.on(<span class="hljs-string">'end'</span>, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (!postData) &#123;
        resolve(&#123;&#125;)
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-comment">// 成功返回</span>
      resolve(<span class="hljs-built_in">JSON</span>.parse(postData))
    &#125;)
  &#125;)
&#125;

<span class="hljs-keyword">const</span> serverHandle = <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  res.setHeader(<span class="hljs-string">'Content-Type'</span>, <span class="hljs-string">'application/json'</span>)

  <span class="hljs-comment">// 获取path</span>
  <span class="hljs-keyword">const</span> url = req.url
  req.path = url.split(<span class="hljs-string">'?'</span>)[<span class="hljs-number">0</span>]

  <span class="hljs-comment">// 解析 query</span>
  req.query = querystring.parse(url.split(<span class="hljs-string">'?'</span>)[<span class="hljs-number">1</span>])

  <span class="hljs-comment">// 处理 postData</span>
  getPostData(req).then(<span class="hljs-function"><span class="hljs-params">postData</span> =></span> &#123;
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
        res.end(<span class="hljs-built_in">JSON</span>.stringify(blogData))
      &#125;)
      <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-comment">// 处理 user 路由</span>
    <span class="hljs-keyword">const</span> userData = handleUserRouter(req, res)
    <span class="hljs-keyword">if</span> (userData) &#123;
      res.end(<span class="hljs-built_in">JSON</span>.stringify(userData))
      <span class="hljs-keyword">return</span>
    &#125;
    <span class="hljs-comment">// 未命中路由, 返回404</span>
    res.writeHead(<span class="hljs-number">404</span>, &#123; <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'text/plain'</span> &#125;)
    res.write(<span class="hljs-string">'404 Not Found\n'</span>)
    res.end()
  &#125;)
&#125;
<span class="hljs-built_in">module</span>.exports = serverHandle
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>​     OK,今天的文章就更新到这里了, 已经完成了从数据库获取数据,现在接口请求的的数据已经是从数据库里拿到的, 而不是自己在<code>js</code>文件里<code>mock</code>的, 技术上可能没有很大的突破,但对我来讲确实是一个值得纪念的时刻~</p>
</blockquote></div>  
</div>
            