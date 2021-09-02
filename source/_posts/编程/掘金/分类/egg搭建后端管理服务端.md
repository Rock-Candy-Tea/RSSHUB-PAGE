
---
title: 'egg搭建后端管理服务端'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7965'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 00:09:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=7965'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.7;font-weight:400;font-size:16px;overflow-x:hidden;color:#212122&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:8px;padding-bottom:8px&#125;.markdown-body h1&#123;color:#a0a0a0;font-size:38px;margin-top:32px;padding-top:32px&#125;.markdown-body h2&#123;color:#fff;background-color:#212122;width:fit-content;border-bottom-right-radius:100px;margin-top:47px;margin-bottom:16px;padding:4px 48px 4px 8px;line-height:1.7;font-size:30px;transition:all .3s ease-out&#125;.markdown-body h2:hover&#123;border-bottom-right-radius:50px;transition:all .3s ease-out&#125;.markdown-body h3&#123;font-size:24px;padding-left:8px;margin-top:32px;border-bottom:2px solid #c6c4c4;line-height:1.7&#125;.markdown-body h4&#123;font-size:20px;padding-left:8px;margin-top:32px;border-bottom:1px solid #ddd&#125;.markdown-body h5&#123;font-size:16px;margin-top:24px&#125;.markdown-body h6&#123;margin-top:16px;line-height:1.1&#125;.markdown-body p&#123;font-size:16px;text-align:start;white-space:normal;text-size-adjust:auto;line-height:2;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%;margin:auto;padding-left:8px;padding-right:8px&#125;.markdown-body hr&#123;border:none;border-top:4px double #212122;margin-top:32px;margin-bottom:32px;text-align:center&#125;.markdown-body hr:after&#123;content:"♥";display:inline-block;position:relative;top:-15px;padding:0 10px;color:#212122;font-size:18px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;background-color:#f1f1f1;color:#ef7060;font-size:14px;padding:.065em 6px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;border-radius:2px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.7;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);margin:32px 16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-color:#212122;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);background-size:40px&#125;.markdown-body pre>code&#123;font-size:14px;padding:16px 8px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#fff;background:#272822&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:10px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;box-shadow:inset 0 0 6px rgba(0,0,0,.3);border-radius:3px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;border-radius:3px;box-shadow:inset 0 0 6px rgba(0,0,0,.3);background-color:#555&#125;.markdown-body a&#123;color:#ef7060;padding:2px;text-decoration:none;border-bottom:.125em solid #ef7060;border-radius:2px;box-shadow:inset 0 -.025em 0 #ef7060;transition:box-shadow .27s cubic-bezier(.77,0,.175,1),color .27s cubic-bezier(.77,0,.175,1)&#125;.markdown-body a:focus,.markdown-body a:hover&#123;outline:none;box-shadow:inset 0 -1.5em 0 #ef7060;color:#fff&#125;.markdown-body a:before&#123;content:"⇲ ";vertical-align:top;margin-left:2px;font-family:dart!important;font-size:12px;color:inherit;opacity:.7&#125;.markdown-body table&#123;background:#fbfbfb;border-radius:4px;border-collapse:collapse;margin:auto;padding:5px;width:95%;box-shadow:0 5px 10px rgba(0,0,0,.1);animation:float 5s infinite&#125;.markdown-body table th&#123;color:#fff;background:#212122;border-bottom:1px solid #9ea7af;border-right:1px solid #343a45;font-size:18px;padding:16px;text-align:left;vertical-align:middle&#125;.markdown-body table th:first-child&#123;border-top-left-radius:4px&#125;.markdown-body table th:last-child&#123;border-top-right-radius:4px;border-right:none&#125;.markdown-body table tr&#123;border-top:1px solid #c1c3d1;border-bottom:1px solid #c1c3d1;color:#666b85&#125;.markdown-body table tr:hover td&#123;background:#212122;color:#fff;border-top:1px solid #22262e&#125;.markdown-body table tr:first-child&#123;border-top:none&#125;.markdown-body table tr:last-child&#123;border-bottom:none&#125;.markdown-body table tr:nth-child(odd) td&#123;background:#f1f1f1&#125;.markdown-body table tr:nth-child(odd):hover td&#123;background:#212122&#125;.markdown-body table tr:last-child td:first-child&#123;border-bottom-left-radius:4px&#125;.markdown-body table tr:last-child td:last-child&#123;border-bottom-right-radius:4px&#125;.markdown-body table td&#123;background:#fbfbfb;padding:16px;text-align:left;vertical-align:middle;font-size:16px;border-right:1px solid #c1c3d1&#125;.markdown-body table td:last-child&#123;border-right:0&#125;.markdown-body blockquote&#123;color:#777;padding:1px 16px;margin:24px 0;border-left:4px solid #c6c4c4;background-color:#f1f1f1;transition:all .3s ease-out;border-radius:4px&#125;.markdown-body blockquote:hover&#123;border-left-color:#212122;background-color:#212122;color:#fff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:24px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:6px;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body span.math&#123;margin-left:32px;font-size:18px;font-weight:700&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:30.4px&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:19.2px&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:12.8px&#125;&#125;</style><h1 data-id="heading-0">egg搭建后端管理服务端</h1>
<h1 data-id="heading-1">快速初始化</h1>
<pre><code class="copyable">mkdir egg-example && cd egg-example
npm init egg --type=simple
yarn
<span class="copy-code-btn">复制代码</span></code></pre>
<p>启动项目:</p>
<pre><code class="copyable">yarn dev 
open http://localhost:7001
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">安装 <code>Sequelize</code></h1>
<p>1- 安装对应的插件 ：</p>
<pre><code class="copyable">yarn add egg-sequelize mysql2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2- 开启插件：</p>
<pre><code class="copyable">// config/plugin.js
module.exports = &#123;
  // had enabled by egg
  static: &#123;
    enable: true
  &#125;,
  // 数据库
  sequelize: &#123;
    enable: true,
    package: "egg-sequelize"
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3- 在 config/config.default.js 中编写 sequelize 配置</p>
<pre><code class="copyable">  // sequelize 配置
  config.sequelize = &#123;
    dialect: "mysql", // 数据路类型-我用的是mysql
    host: "127.0.0.1", // 数据库地址
    port: 3306, // 数据库端口号
    database: "egg-sequelize", // 数据库名称
    username: "root", // 用户名
    password: "123456", // 密码
    // 配置数据库时间为东八区北京时间
    timezone: "+08:00",
    define: &#123;
      freezeTableName: true // 强制表名称等于模型名称
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">安装 sequelize-cli</h3>
<pre><code class="copyable">yarn add sequelize-cli --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 egg 项目中，我们希望将所有数据库 Migrations 相关的内容都放在 <code>database</code> 目录下，所以我们在项目根目录下新建一个 <code>.sequelizerc</code> 配置文件：</p>
<pre><code class="copyable">'use strict';

const path = require('path');

module.exports = &#123;
   config: path.join(__dirname, 'database/config.json'),
   'migrations-path': path.join(__dirname, 'database/migrations'),
   'seeders-path': path.join(__dirname, 'database/seeders'),
   'models-path': path.join(__dirname, 'app/model'),
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始化 Migrations 配置文件和目录</p>
<pre><code class="copyable">npx sequelize init:config
npx sequelize init:migrations
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行完后会生成 <code>database/config.json</code> 文件和 <code>database/migrations</code> 目录，我们修改一下 <code>database/config.json</code> 中的内容，将其改成我们项目中使用的数据库配置：</p>
<pre><code class="copyable">&#123;
  "development": &#123;
    "username": "root",
    "password": null,
    "database": "database_development",
    "host": "127.0.0.1",
    "dialect": "mysql"
  &#125;,
  "test": &#123;
    "username": "root",
    "password": null,
    "database": "database_test",
    "host": "127.0.0.1",
    "dialect": "mysql"
  &#125;,
  "production": &#123;
    "username": "root",
    "password": null,
    "database": "database_production",
    "host": "127.0.0.1",
    "dialect": "mysql"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时 sequelize-cli 和相关的配置也都初始化好了，我们可以开始编写项目的第一个 Migration 文件来创建我们的一个 users 表了。</p>
<p>**</p>
<pre><code class="copyable">npx sequelize migration:generate --name=init-users
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行完后会在 <code>database/migrations</code> 目录下生成一个 migration 文件(<code>$&#123;timestamp&#125;-init-users.js</code>)，我们修改它来处理初始化 <code>users</code> 表：</p>
<p>**</p>
<pre><code class="copyable">'use strict';

module.exports = &#123;
   // 在执行数据库升级时调用的函数，创建 users 表
   up: async (queryInterface, Sequelize) => &#123;
      const &#123; INTEGER, DATE, STRING &#125; = Sequelize;
      await queryInterface.createTable('users', &#123;
         id: &#123; type: INTEGER, primaryKey: true, autoIncrement: true &#125;,
         name: STRING(30),
         age: INTEGER,
         created_at: DATE,
         updated_at: DATE,
      &#125;);
   &#125;,
   // 在执行数据库降级时调用的函数，删除 users 表
   down: async queryInterface => &#123;
      await queryInterface.dropTable('users');
   &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 migrate 进行数据库变更</p>
<p>**</p>
<pre><code class="copyable"># 升级数据库
# npx sequelize db:migrate
# 如果有问题需要回滚，可以通过 `db:migrate:undo` 回退一个变更
# npx sequelize db:migrate:undo
# 可以通过 `db:migrate:undo:all` 回退到初始状态
# npx sequelize db:migrate:undo:all
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行之后，我们的数据库初始化就完成了。</p>
<h3 data-id="heading-4">编写代码</h3>
<p>现在终于可以开始编写代码实现业务逻辑了，首先我们来在 <code>app/model/</code> 目录下编写 user 这个 Model：</p>
<p>**</p>
<pre><code class="copyable">'use strict';

module.exports = app => &#123;
   const &#123; STRING, INTEGER, DATE &#125; = app.Sequelize;

   const User = app.model.define('user', &#123;
      id: &#123; type: INTEGER, primaryKey: true, autoIncrement: true &#125;,
      name: STRING(30),
      age: INTEGER,
      created_at: DATE,
      updated_at: DATE,
   &#125;);

   return User;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个 Model 就可以在 Controller 和 Service 中通过 <code>app.model.User</code> 或者 <code>ctx.model.User</code> 访问到了，例如我们编写 <code>app/controller/users.js</code>：</p>
<p>**</p>
<pre><code class="copyable">// app/controller/users.js
const Controller = require('egg').Controller;

function toInt(str) &#123;
   if (typeof str === 'number') return str;
   if (!str) return str;
   return parseInt(str, 10) || 0;
&#125;

class UserController extends Controller &#123;
   async index() &#123;
      const ctx = this.ctx;
      const query = &#123; limit: toInt(ctx.query.limit), offset: toInt(ctx.query.offset) &#125;;
      ctx.body = await ctx.model.User.findAll(query);
   &#125;

   async show() &#123;
      const ctx = this.ctx;
      ctx.body = await ctx.model.User.findByPk(toInt(ctx.params.id));
   &#125;

   async create() &#123;
      const ctx = this.ctx;
      const &#123; name, age &#125; = ctx.request.body;
      const user = await ctx.model.User.create(&#123; name, age &#125;);
      ctx.status = 201;
      ctx.body = user;
   &#125;

   async update() &#123;
      const ctx = this.ctx;
      const id = toInt(ctx.params.id);
      const user = await ctx.model.User.findByPk(id);
      if (!user) &#123;
         ctx.status = 404;
         return;
      &#125;

      const &#123; name, age &#125; = ctx.request.body;
      await user.update(&#123; name, age &#125;);
      ctx.body = user;
   &#125;

   async destroy() &#123;
      const ctx = this.ctx;
      const id = toInt(ctx.params.id);
      const user = await ctx.model.User.findByPk(id);
      if (!user) &#123;
         ctx.status = 404;
         return;
      &#125;

      await user.destroy();
      ctx.status = 200;
   &#125;
&#125;

module.exports = UserController;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们将这个 controller 挂载到路由上：</p>
<p>**</p>
<pre><code class="copyable">// app/router.js
module.exports = app => &#123;
   const &#123; router, controller &#125; = app;
   router.resources('users', '/users', controller.users);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">自动生成 model 文件</h3>
<p><code>yarn add  egg-sequelize-auto --dev</code></p>
<p>在 package.json 的 script 里面添加把数据库生成 model 的命令（ -o 表示生成 models 的路径，-h 表示主机，-p 表示端口，-d 表示数据库， -u 表示用户名，-x 表示密码）</p>
<p>**</p>
<pre><code class="copyable">"scripts": &#123;
   "dbload": "egg-sequelize-auto -o ./app/model -h localhost -p 3306 -d database -u username -x password"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-6">待更新2021-09-01</h2></div>  
</div>
            