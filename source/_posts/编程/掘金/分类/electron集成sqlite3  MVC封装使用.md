
---
title: 'electron集成sqlite3  MVC封装使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://juejin.cn/post/undefined'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 00:38:43 GMT
thumbnail: 'https://juejin.cn/post/undefined'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>​</p>
<p>一：添加依赖 配置环境（注意target electron版本）</p>
<pre><code class="copyable">1: yarn add sqlite3@latest --build-from-source --runtime=electron --target=8.5.2 --dist-url=https://atom.io/download/electron
2: yarn add electron-rebuild    node > 12.19.0 需要升级最新node版本
3: yarn add aws-sdk             需要先安装aws-sdk  不然 rebuild失败
4: package.json 增加命令    "rebuild:sql": "electron-rebuild -f -w sqlite3"
5: yarn rebuild:sql    验证 可用性 可行
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<p>二：封装sql方法 主进程下创建 sqlite.js</p>
<pre><code class="copyable">// import sqlite3 from 'sqlite3'
const sqlite3 = require('sqlite3');
const sqlite = sqlite3.verbose();
class Sqlite &#123;
  constructor () &#123;
    this.sqlInstance = null;
    this.db = null;
  &#125;

  // 连接数据库
  connect (path) &#123;
    return new Promise((resolve, reject) => &#123;
      this.db = new sqlite.Database(path, (err) => &#123;
        if (err) &#123;
          reject(err);
        &#125; else &#123;
          resolve(1);
        &#125;
      &#125;);
    &#125;);
  &#125;

  // 运行sql
  run (sql, params) &#123;
    return new Promise((resolve, reject) => &#123;
      this.db.run(sql, params, (err) => &#123;
        if (err) &#123;
          reject(err);
        &#125; else &#123;
          resolve(1);
        &#125;
      &#125;);
    &#125;);
  &#125;

  // 运行多条sql
  exec (sql) &#123;
    return new Promise((resolve, reject) => &#123;
      this.db.exec(sql, (err) => &#123;
        if (err) &#123;
          reject(err);
        &#125; else &#123;
          resolve(1);
        &#125;
      &#125;);
    &#125;);
  &#125;

  // 查询一条数据
  get (sql, params) &#123;
    return new Promise((resolve, reject) => &#123;
      this.db.get(sql, params, (err, data) => &#123;
        if (err) &#123;
          reject(err);
        &#125; else &#123;
          resolve(data);
        &#125;
      &#125;);
    &#125;);
  &#125;

  // 查询所有数据
  all (sql, params) &#123;
    return new Promise((resolve, reject) => &#123;
      this.db.all(sql, params, (err, data) => &#123;
        if (err) &#123;
          reject(err);
        &#125; else &#123;
          resolve(data);
        &#125;
      &#125;);
    &#125;);
  &#125;

  // 关闭数据库
  close () &#123;
    this.db.close();
  &#125;

  // 单例
  static getInstance () &#123;
    this.sqlInstance = this.sqlInstance ? this.sqlInstance : new Sqlite();
    return this.sqlInstance;
  &#125;
&#125;

export default Sqlite;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<p>三：主进程注册 Sqlite 服务</p>
<pre><code class="copyable">// 数据库服务
import Sqlite from './utils/sqlite';

const sqlite = new Sqlite();
context.sqlite = sqlite;     //context 定义为全局上下文
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<p>四：以User数据 创建 UserListTable 数据模型 UserListTable.js</p>
<pre><code class="copyable">class UserListTable &#123;
  constructor (context) &#123;
    this.mContext = context;
  &#125;
  insertAllContacts (args, userInfo) &#123;
    const list = args.data;
    let sql = ‘’
    return this.mContext.sqlite.exec(sql);
  &#125;
  searchUserList (params) &#123;
    params = &#123;userId: 123&#125;;
    return this.mContext.sqlite.all('SELECT * FROM test');
  &#125;
&#125;
export default UserListTable;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<p>五：创建User 控制器 userListCorl.js 调用</p>
<pre><code class="copyable">import BaseClass from './baseClass';
class UserListCorl extends BaseClass &#123;
  async insertAllContacts (args, userInfo) &#123;
    return this.userListTable.insertAllContacts(args, userInfo);
  &#125;
&#125;
export default UserListCorl;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<p>补充</p>
<p>baseClass.js</p>
<pre><code class="copyable">// 所有的models 都在base注册 在其他class 消费
import InitDB from '../models/initDB';
import UserListTable from '../models/userListTable';
class BaseClass &#123;
  constructor (context) &#123;
    this.mContext = context;
    this.mInitDB = new InitDB(context);
    this.userListTable = new UserListTable(context);
  &#125;
&#125;
export default BaseClass;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">InitDB.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">class InitDB &#123;
  constructor (content) &#123;
    this.mContext = content;
  &#125;
  connectDB (path) &#123;
    return this.mContext.sqlite.connect(path);
  &#125;
  createTable () &#123;
    // 创建表
    return this.mContext.sqlite.exec(sql);
    // 还需创建 多张表
  &#125;
  insertTestData (params) &#123;
    return this.mContext.sqlite.run(sql);
  &#125;
&#125;
export default InitDB;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<p>​</p></div>  
</div>
            