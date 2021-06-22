
---
title: '记录第一次用node + mysql做接口'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01f20122354c49eba961adc8dd54664d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 19:43:31 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01f20122354c49eba961adc8dd54664d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一. 使用navicat建数据库</h1>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01f20122354c49eba961adc8dd54664d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">1. 下载mysql</h2>
<ul>
<li>安装指南 <a href="https://zhuanlan.zhihu.com/p/37152572" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/37152572</a> ，这篇文章很详细</li>
<li>安装时，MySQL会提示输入<code>root</code>用户的口令，请务必记清楚。如果怕记不住，就把口令设置为<code>password</code>。</li>
<li>在<code>Windows</code>上，安装时请选择<code>UTF-8</code>编码，以便正确地处理中文。</li>
<li>配置<code>username</code>和<code>password</code>时最好记录下来，避免忘了。</li>
</ul>
<h2 data-id="heading-2">2. 下载navicat</h2>
<ul>
<li>安装 <a href="https://www.navicat.com.cn/products" target="_blank" rel="nofollow noopener noreferrer">Navicat Premium 15</a></li>
</ul>

<h2 data-id="heading-3">3. navicat连接mysql数据库</h2>
<ul>
<li>用管理员身份运行<code>cmd</code>，输入<code>net start 服务器名称</code>，启动数据库</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac9fec5f870c40d39a75125505683e7f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>启动成功</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c709e3b73c244d33b1914686ad925e72~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>打开<code>navicat</code>点击连接<code>mysql</code></li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/415376957f7649c5845c245adee3aa7e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>输入<code>net stop 服务器名称</code>，停止<code>mysql</code></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24cea319a3704862b7ccf76760a6df67~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">二. 使用node + mysql做接口</h1>
<h2 data-id="heading-5">1. 启动node服务器</h2>
<ul>
<li>随便找个地方运行命令<code>mkdir node-service && cd node-service</code>，新建<code>index.js</code>文件，简单用<code>express</code>就开启一个服务器了</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">"express"</span>);
<span class="hljs-keyword">const</span> app = express();
<span class="hljs-keyword">const</span> port = <span class="hljs-number">3002</span>;
app.listen(port, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`Example app listening at http://localhost:<span class="hljs-subst">$&#123;port&#125;</span>`</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">2. node连接本地数据库</h2>
<ul>
<li>引用<code>mysql</code>连接，这样就能连接上本地的数据库了，前提是数据库服务器有开启</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> mysql = <span class="hljs-built_in">require</span>(<span class="hljs-string">"mysql"</span>);
<span class="hljs-keyword">const</span> defconfig = &#123;
  <span class="hljs-attr">host</span>: <span class="hljs-string">"localhost"</span>,
  <span class="hljs-attr">user</span>: <span class="hljs-string">"root"</span>,
  <span class="hljs-attr">password</span>: <span class="hljs-string">"password"</span>,
  <span class="hljs-attr">database</span>: <span class="hljs-string">"test"</span>, <span class="hljs-comment">// 数据库名</span>
  <span class="hljs-attr">port</span>: <span class="hljs-string">"3306"</span>,
&#125;;
<span class="hljs-keyword">const</span> connection = mysql.createConnection(defconfig);
connection.connect(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (err) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"数据库连接失败"</span>);
    <span class="hljs-keyword">throw</span> err;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>操作数据库，简单查询一下数据库</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> querysql = <span class="hljs-string">"SELECT * FROM user"</span>;
connection.query(querysql, [], <span class="hljs-function">(<span class="hljs-params">res, fields</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"查询结果："</span>);
  <span class="hljs-built_in">console</span>.log(res);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"fields: "</span>, fields);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>再简单封装一下，就可以在调用接口的时候直接使用了。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// db.js</span>
<span class="hljs-keyword">const</span> query = <span class="hljs-function">(<span class="hljs-params">sql, params, callback</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> connection = mysql.createConnection(defconfig);
  connection.connect(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (err) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"数据库连接失败"</span>);
      <span class="hljs-keyword">throw</span> err;
    &#125;
  &#125;);
  <span class="hljs-keyword">const</span> fn = <span class="hljs-function">(<span class="hljs-params">err, res, fields</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (err) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"数据操作失败: "</span>, err.message);
      <span class="hljs-keyword">throw</span> err;
    &#125;
    <span class="hljs-comment">//将查询出来的数据返回给回调函数</span>
    callback && callback(res, fields);
    connection.end(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (err) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"关闭数据库连接失败！"</span>);
        <span class="hljs-keyword">throw</span> err;
      &#125;
    &#125;);
  &#125;;
  connection.query(sql, params, fn);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">3. 创建增删改查接口</h2>
<blockquote>
<p>注意：要拿到传过来的数据需要调用<code>app.use(express.json())</code>和<code>app.use(express.urlencoded())</code>，代替<code>body-parse</code>解析传入数据</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcaeb6e401e34a8c90dfbc4baf2290cd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85972bde50f04d2abc1aa57154d7af5e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">"express"</span>);
<span class="hljs-keyword">const</span> app = express();
app.use(express.json());
app.use(express.urlencoded());
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>数据库</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a46d6f0688024a4fb5b2dbd6ce8d4c95~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>创建查询接口，然后在前端调用接口</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">app.get(<span class="hljs-string">"/data"</span>, <span class="hljs-function">(<span class="hljs-params">req, resp</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> querysql = <span class="hljs-string">"SELECT * FROM todo_list"</span>;
  db.query(querysql, [], <span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    resp.json(res);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> http = <span class="hljs-keyword">new</span> XMLHttpRequest();
http.onreadystatechange =  <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">if</span> (http.status == <span class="hljs-number">200</span> && http.readyState == <span class="hljs-number">4</span>) &#123;
    <span class="hljs-comment">// 调用成功后</span>
  &#125;
&#125;;
<span class="hljs-comment">//发送请求</span>
http.open(<span class="hljs-string">"GET"</span>, <span class="hljs-string">"http://localhost:3000/data"</span>);
http.send();
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>创建插入接口</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">app.post(<span class="hljs-string">"/postdata"</span>, <span class="hljs-function">(<span class="hljs-params">req, resp</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"插入数据"</span>, req.body);
  <span class="hljs-keyword">const</span> target = req.body.target;
  <span class="hljs-keyword">const</span> querysql = <span class="hljs-string">"insert into todo_list(target, status) values(?,?)"</span>;
  db.query(querysql, [target, <span class="hljs-string">"false"</span>], <span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    resp.json(res);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> http = <span class="hljs-keyword">new</span> XMLHttpRequest();
<span class="hljs-keyword">var</span> &#123; value, name &#125; = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"name"</span>);
<span class="hljs-keyword">const</span> params = &#123; [name]: value &#125;;
http.open(<span class="hljs-string">"POST"</span>, <span class="hljs-string">"http://localhost:3000/postdata"</span>);
http.setRequestHeader(<span class="hljs-string">"Content-type"</span>, <span class="hljs-string">"application/json;charset=UTF-8"</span>);
http.send(<span class="hljs-built_in">JSON</span>.stringify(params));
<span class="hljs-built_in">document</span>.location.reload();
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>创建更新接口</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">app.put(<span class="hljs-string">"/putData"</span>, <span class="hljs-function">(<span class="hljs-params">req, resp</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"修改数据："</span>, req.body);
  <span class="hljs-keyword">const</span> target = req.body.target;
  <span class="hljs-keyword">const</span> status = req.body.status;
  <span class="hljs-keyword">let</span> data;
  <span class="hljs-keyword">if</span> (status === <span class="hljs-string">"false"</span>) data = <span class="hljs-literal">true</span>;
  <span class="hljs-keyword">if</span> (status === <span class="hljs-string">"true"</span>) data = <span class="hljs-literal">false</span>;
  <span class="hljs-keyword">const</span> sql = <span class="hljs-string">`update todo_list set status = "<span class="hljs-subst">$&#123;data&#125;</span>" where target = "<span class="hljs-subst">$&#123;target&#125;</span>"`</span>;
  db.query(sql, [], <span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    resp.json(res);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> http = <span class="hljs-keyword">new</span> XMLHttpRequest();
http.open(<span class="hljs-string">"PUT"</span>, <span class="hljs-string">`http://localhost:3000/putData`</span>);
<span class="hljs-comment">// 传body要设置请求头</span>
http.setRequestHeader(
<span class="hljs-string">"Content-type"</span>,
<span class="hljs-string">"application/json;charset=UTF-8"</span>
);
http.send(<span class="hljs-built_in">JSON</span>.stringify(data));
<span class="hljs-built_in">document</span>.location.reload();
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>删除接口</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">app.delete(<span class="hljs-string">"/deleteData"</span>, <span class="hljs-function">(<span class="hljs-params">req, resp</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"删除数据："</span>, req.query);
  <span class="hljs-keyword">const</span> target = req.query.target;
  <span class="hljs-keyword">const</span> querysql = <span class="hljs-string">`DELETE FROM todo_list WHERE target = "<span class="hljs-subst">$&#123;target&#125;</span>" `</span>;
  db.query(querysql, [], <span class="hljs-function">() =></span> &#123;
    resp.json(req.query);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> http = <span class="hljs-keyword">new</span> XMLHttpRequest();
http.open(<span class="hljs-string">"DELETE"</span>, <span class="hljs-string">`http://localhost:3000/deleteData?target=<span class="hljs-subst">$&#123;data.target&#125;</span>`</span>);
http.send();
<span class="hljs-built_in">document</span>.location.reload();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">4. 跨域问题</h2>
<ul>
<li>第一种方法，安装cors</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//yarn add cors</span>
<span class="hljs-keyword">const</span> cors = <span class="hljs-built_in">require</span>(<span class="hljs-string">"cors"</span>);
app.use(cors());
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第二种方法，手动实现</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">app.use(<span class="hljs-function">(<span class="hljs-params">req, res, next</span>) =></span> &#123;
res.header(<span class="hljs-string">'Access-Control-Allow-Origin'</span>, <span class="hljs-string">'*'</span>)
res.header(<span class="hljs-string">'Access-Control-Allow-Headers'</span>, <span class="hljs-string">'Authorization,X-API-KEY, Origin, X-Requested-With, Content-Type, Accept, Access-Control-Request-Method'</span> )
res.header(<span class="hljs-string">'Access-Control-Allow-Methods'</span>, <span class="hljs-string">'GET, POST, OPTIONS, PATCH, PUT, DELETE'</span>)
res.header(<span class="hljs-string">'Allow'</span>, <span class="hljs-string">'GET, POST, PATCH, OPTIONS, PUT, DELETE'</span>)
next();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            