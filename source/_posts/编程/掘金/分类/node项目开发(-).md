
---
title: 'node项目开发(-)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6316'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 01:10:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=6316'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与掘金创作者训练营第三期「话题写作」赛道，详情查看：<a href="https://juejin.cn/post/6994417198164869133" title="https://juejin.cn/post/6994417198164869133" target="_blank">掘力计划｜创作者训练营第三期正在进行，「写」出个人影响力</a>。</p>
<h1 data-id="heading-0">NodeJS 项目</h1>
<h4 data-id="heading-1">0.  初始化</h4>
<p>1.1 创建项目</p>
<ol>
<li>新建 api_server 文件夹作为项目根目录，并在项目根目录中运行如下的命令，初始化包管理配置文件：</li>
</ol>
<p><code>npm init -y</code></p>
<ol start="2">
<li>运行如下的命令，安装特定版本的 express：</li>
</ol>
<p><code>npm i express@4.17.1</code></p>
<ol start="3">
<li>在项目根目录中新建 app.js 作为整个项目的入口文件，并初始化如下的代码：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 导入 express 模块</span>

<span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>)

<span class="hljs-comment">// 创建 express 的服务器实例</span>

<span class="hljs-keyword">const</span> app = express()

<span class="hljs-comment">// write your code here...</span>
<span class="hljs-comment">// 调用 app.listen 方法，指定端口号并启动web服务器</span>

app.listen(<span class="hljs-number">3007</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'api server running at [http://127.0.0.1:3007'</span>](http:<span class="hljs-comment">//127.0.0.1:3007%27/))</span>

&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.1 配置 cors 跨域</p>
<p>1、运行如下的命令，安装 cors 中间件：</p>
<p><code>npm i cors@2.8.5</code></p>
<p>2、在 app.js 中导入并配置 cors 中间件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 导入 cors 中间件</span>

<span class="hljs-keyword">const</span> cors = <span class="hljs-built_in">require</span>(<span class="hljs-string">'cors'</span>)

<span class="hljs-comment">// 将 cors 注册为全局中间件</span>

app.use(cors())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1.3 配置解析表单数据的中间件</p>
<p>1 通过如下的代码，配置解析 application/x-www-form-urlencoded 格式的表单数据的中间件：</p>
<p><code>app.use(express.urlencoded(&#123; extended: false &#125;))</code></p>
<p>1.4 初始化路由相关的文件夹</p>
<p>1在项目根目录中，新建 router 文件夹，用来存放所有的路由模块</p>
<p>路由模块中，只存放客户端的请求与处理函数之间的映射关系</p>
<p>1在项目根目录中，新建 router_handler 文件夹，用来存放所有的 路由处理函数模块</p>
<p>路由处理函数模块中，专门负责存放每个路由对应的处理函数</p>
<p>1.5 初始化用户路由模块</p>
<p>1在 router 文件夹中，新建 user.js 文件，作为用户的路由模块，并初始化代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>)

<span class="hljs-comment">// 创建路由对象</span>

<span class="hljs-keyword">const</span> router = express.Router()

<span class="hljs-comment">// 注册新用户</span>

router.post(<span class="hljs-string">'/reguser'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;

res.send(<span class="hljs-string">'reguser OK'</span>)

&#125;)

<span class="hljs-comment">// 登录</span>

router.post(<span class="hljs-string">'/login'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;

res.send(<span class="hljs-string">'login OK'</span>)

&#125;)

<span class="hljs-comment">// 将路由对象共享出去</span>

<span class="hljs-built_in">module</span>.exports = router
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2在 app.js 中，导入并使用 用户路由模块 ：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 导入并注册用户路由模块</span>

<span class="hljs-keyword">const</span> userRouter = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./router/user'</span>)

app.use(<span class="hljs-string">'/api'</span>, userRouter)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1.6 抽离用户路由模块中的处理函数</p>
<p>目的：为了保证 路由模块 的纯粹性，所有的 路由处理函数，必须抽离到对应的 路由处理函数模块 中</p>
<p>1在 /router_handler/user.js 中，使用 exports 对象，分别向外共享如下两个 路由处理函数 ：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**

* 在这里定义和用户相关的路由处理函数，供 /router/user.js 模块进行调用

*/</span>

<span class="hljs-comment">// 注册用户的处理函数</span>

<span class="hljs-built_in">exports</span>.regUser = <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;

res.send(<span class="hljs-string">'reguser OK'</span>)

&#125;

<span class="hljs-comment">// 登录的处理函数</span>

<span class="hljs-built_in">exports</span>.login = <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;

res.send(<span class="hljs-string">'login OK'</span>)

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2将 /router/user.js 中的代码修改为如下结构：</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>)

<span class="hljs-keyword">const</span> router = express.Router()

<span class="hljs-comment">// 导入用户路由处理函数模块</span>

<span class="hljs-keyword">const</span> userHandler = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../router_handler/user'</span>)

<span class="hljs-comment">// 注册新用户</span>

router.post(<span class="hljs-string">'/reguser'</span>, userHandler.regUser)

<span class="hljs-comment">// 登录</span>

router.post(<span class="hljs-string">'/login'</span>, userHandler.login)

<span class="hljs-built_in">module</span>.exports = router
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>登录注册</li>
</ol>
<p>2.1 新建 ev_users 表</p>
<p>1在 my_db_01 数据库中，新建 ev_users 表如下：</p>
<p>2.2 安装并配置 mysql 模块</p>
<p>在 API 接口项目中，需要安装并配置 mysql 这个第三方模块，来连接和操作 MySQL 数据库</p>
<p>1运行如下命令，安装 mysql 模块：</p>
<p>npm i <a href="https://link.juejin.cn/?target=mailto%3Amysql%402.18.1" target="_blank" title="mailto:mysql@2.18.1" ref="nofollow noopener noreferrer">mysql@2.18.1</a></p>
<p>2在项目根目录中新建 /db/index.js 文件，在此自定义模块中创建数据库的连接对象：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 导入 mysql 模块</span>

<span class="hljs-keyword">const</span> mysql = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mysql'</span>)

<span class="hljs-comment">// 创建数据库连接对象</span>

<span class="hljs-keyword">const</span> db = mysql.createPool(&#123;

<span class="hljs-attr">host</span>: <span class="hljs-string">'127.0.0.1'</span>,

<span class="hljs-attr">user</span>: <span class="hljs-string">'root'</span>,

<span class="hljs-attr">password</span>: <span class="hljs-string">'admin123'</span>,

<span class="hljs-attr">database</span>: <span class="hljs-string">'my_db_01'</span>,

&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>// 向外共享 db 数据库连接对象</p>
<p><code>module.exports = db</code></p>
<p>2.3 注册 2.3.0 实现步骤</p>
<p>1检测表单数据是否合法</p>
<p>2检测用户名是否被占用</p>
<p>3对密码进行加密处理</p>
<p>4插入新用户</p>
<p>2.3.1 检测表单数据是否合法</p>
<p>1判断用户名和密码是否为空</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 接收表单数据</span>

<span class="hljs-keyword">const</span> userinfo = req.body

<span class="hljs-comment">// 判断数据是否合法</span>

<span class="hljs-keyword">if</span> (!userinfo.username || !userinfo.password) &#123;

<span class="hljs-keyword">return</span> res.send(&#123; <span class="hljs-attr">status</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'用户名或密码不能为空！'</span> &#125;)

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.3.2 检测用户名是否被占用</p>
<p>1导入数据库操作模块：</p>
<p><code>const db = require('../db/index')</code></p>
<p>2定义 SQL 语句：</p>
<p><code>const sql = </code>select * from ev_users where username=?``</p>
<p>3执行 SQL 语句并根据结果判断用户名是否被占用：</p>
<pre><code class="hljs language-js copyable" lang="js">db.query(sql, [userinfo.username], <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err, results</span>) </span>&#123;

<span class="hljs-comment">// 执行 SQL 语句失败</span>

<span class="hljs-keyword">if</span> (err) &#123;

<span class="hljs-keyword">return</span> res.send(&#123; <span class="hljs-attr">status</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">message</span>: err.message &#125;)

&#125;

<span class="hljs-comment">// 用户名被占用</span>

<span class="hljs-keyword">if</span> (results.length > <span class="hljs-number">0</span>) &#123;

<span class="hljs-keyword">return</span> res.send(&#123; <span class="hljs-attr">status</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'用户名被占用，请更换其他用户名！'</span> &#125;)

&#125;

<span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> 用户名可用，继续后续流程...</span>

&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.3.3 对密码进行加密处理</p>
<p>为了保证密码的安全性，不建议在数据库以 明文 的形式保存用户密码，推荐对密码进行 加密存储</p>
<p>在当前项目中，使用 bcryptjs 对用户密码进行加密，优点：</p>
<p>●加密之后的密码，无法被逆向破解</p>
<p>●同一明文密码多次加密，得到的加密结果各不相同，保证了安全性</p>
<p>1运行如下命令，安装指定版本的 bcryptjs ：</p>
<p><code>npm i bcryptjs@2.4.3</code></p>
<p>2在 /router_handler/user.js 中，导入 bcryptjs ：</p>
<p><code>const bcrypt = require('bcryptjs')</code></p>
<p>3 在注册用户的处理函数中，确认用户名可用之后，调用 bcrypt.hashSync(明文密码, 随机盐的长度) 方法，对用户的密码进行加密处理：</p>
<p>// 对用户的密码,进行 bcrype 加密，返回值是加密之后的密码字符串</p>
<p><code>userinfo.password = bcrypt.hashSync(userinfo.password, 10)</code></p>
<p>2.3.4 插入新用户</p>
<p>1定义插入用户的 SQL 语句：</p>
<p>const sql = 'insert into ev_users set ?'</p>
<p>2调用 db.query() 执行 SQL 语句，插入新用户：</p>
<pre><code class="hljs language-js copyable" lang="js">db.query(sql, &#123; <span class="hljs-attr">username</span>: userinfo.username, <span class="hljs-attr">password</span>: userinfo.password &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err, results</span>) </span>&#123;

<span class="hljs-comment">// 执行 SQL 语句失败</span>

<span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">return</span> res.send(&#123; <span class="hljs-attr">status</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">message</span>: err.message &#125;)

<span class="hljs-comment">// SQL 语句执行成功，但影响行数不为 1</span>

<span class="hljs-keyword">if</span> (results.affectedRows !== <span class="hljs-number">1</span>) &#123;

<span class="hljs-keyword">return</span> res.send(&#123; <span class="hljs-attr">status</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'注册用户失败，请稍后再试！'</span> &#125;)

&#125;

<span class="hljs-comment">// 注册成功</span>

res.send(&#123; <span class="hljs-attr">status</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'注册成功！'</span> &#125;)

&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.4 优化 res.send() 代码</p>
<p>在处理函数中，需要多次调用 res.send() 向客户端响应 处理失败 的结果，为了简化代码，可以手动封装一个 res.cc() 函数</p>
<p>1在 app.js 中，所有路由之前，声明一个全局中间件，为 res 对象挂载一个 res.cc() 函数 ：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 响应数据的中间件</span>

app.use(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">req, res, next</span>) </span>&#123;

<span class="hljs-comment">// status = 0 为成功； status = 1 为失败； 默认将 status 的值设置为 1，方便处理失败的情况</span>

res.cc = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err, status = <span class="hljs-number">1</span></span>) </span>&#123;

res.send(&#123;

<span class="hljs-comment">// 状态</span>

status,

<span class="hljs-comment">// 状态描述，判断 err 是 错误对象 还是 字符串</span>

<span class="hljs-attr">message</span>: err <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Error</span> ? err.message : err,

&#125;)

&#125;

next()

&#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            