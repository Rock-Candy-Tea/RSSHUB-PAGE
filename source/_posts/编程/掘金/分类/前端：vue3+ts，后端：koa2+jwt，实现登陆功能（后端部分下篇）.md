
---
title: '前端：vue3+ts，后端：koa2+jwt，实现登陆功能（后端部分下篇）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2474'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 17:03:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=2474'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第17天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p><a href="https://juejin.cn/post/6996804771222913055#heading-0" target="_blank" title="https://juejin.cn/post/6996804771222913055#heading-0"># 前端：vue3+ts，后端：koa2+jwt，实现登陆功能（后端部分上篇）</a></p>
<h2 data-id="heading-0">1. 在routes里面，创建一个user.js文件，用作登陆的后端文件</h2>
<pre><code class="copyable">/**
 * 用户管理模块
 */
const router = require('koa-router')()  // koa路由文件
const User = require('../models/userSchema')  // schema文件 定义user用户的字段的
const util = require('../utils/util')  // 引入请求成功与否的封装
const jwt = require('jsonwebtoken')  // 引入jsonwebtoken做token的加密

// 二级路由前缀定义
router.prefix('/users')

// 用户的登录
router.post('/login', async (ctx) => &#123;
  try &#123;
      // get请求是ctx.request.query
      // post请求是ctx.request.body
      const &#123; username, password &#125; = ctx.request.body
      /**
       * 返回数据库指定字段， 有三种方式
       * 1. 'userId username userEmail state role deptId roleList'    // 选择只返回的字段
       * 2. &#123; userId: 1, _id: 0 &#125;                                     // 选择只返回的字段， 1是展示， 0是不展示
       * 3. selec('userId')                                           // 查找userId
       */
      const res = await User.findOne(&#123;
          username,
          password
        &#125;, 'userId userame userEmail state role deptId roleList')
      const data = res._doc##

      // 利用jsonwebtoken生成基于密钥xiaohe的token
      const token = jwt.sign(&#123;
        data,
      &#125;, 'xiaohe', &#123; expiresIn: '2d' &#125;)
      
      // 当查找到数据的时候，返回token和成功
      if(res) &#123;
        data.token = token
        ctx.body = util.success(data)
      &#125; else &#123;
        ctx.body = util.fail('账号或密码不正确')
      &#125;
  &#125; catch (error) &#123;
    //   console.log(error)
      ctx.body = util.fail(error.msg)
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2. 挂载一下到app.js里面</h2>
<pre><code class="copyable">const Koa = require('koa')
const app = new Koa()
const views = require('koa-views')
const json = require('koa-json')
const onerror = require('koa-onerror')
const bodyparser = require('koa-bodyparser')
const logger = require('koa-logger')
const koajwt = require('koa-jwt')    // 引入koa-jwt，用于解密
const users = require('./routes/users') // 引入users文件
const log4js = require('./utils/log4j') // 引入日志系统
const router = require('koa-router')() // 引入路由跳转
const util = require('./utils/util')  // 引入状态吗

// error handler
onerror(app)

// 使用db连接数据库
require('./config/db')

// middlewares
app.use(bodyparser(&#123;
  enableTypes:['json', 'form', 'text']
&#125;))
app.use(json())
app.use(logger())
app.use(require('koa-static')(__dirname + '/public'))

app.use(views(__dirname + '/views', &#123;
  extension: 'pug'
&#125;))

// logger   中间件
app.use(async (ctx, next) => &#123;
  log4js.info(`get: $&#123; JSON.stringify(ctx.request.query) &#125;`)
  log4js.info(`params: $&#123; JSON.stringify(ctx.request.body) &#125;`)
  // 当状态码是401的时候，改成200，并展示token认证失败
  await next().catch(err => &#123;
    if(err.status == '401') &#123;
      ctx.status = 200
      ctx.body = util.fail('Token认证失败', util.CODE.AUTH_ERROR)
    &#125; else throw err
  &#125;)
&#125;)

// koa的jwt校验， secret: 密钥   unless： 过滤掉不需要校验的api
app.use(koajwt(&#123; secret: 'xiaohe' &#125;).unless(&#123;
  path: [/^\/api\/users\/login/]
&#125;))  // 密钥校验，jwt校验

router.prefix('/api')  // api前缀

// 挂载users上路由
router.use(users.routes(), users.allowedMethods())

// routes
app.use(router.routes(), router.allowedMethods())

// error-handling
app.on('error', (err, ctx) => &#123;
  // console.error('server error', err, ctx)
  log4js.error(`$&#123; err.stack &#125;`)
&#125;);

module.exports = app
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">最后</h2>
<blockquote>
<p>公众号：小何成长，佛系更文，都是自己曾经踩过的坑或者是学到的东西</p>
<p>有兴趣的小伙伴欢迎关注我哦，我是：<code>何小玍</code>。大家一起进步鸭</p>
<p>需要源码的，欢迎添加公众号，然后跟我要源码吧。</p>
<p>最近有点忙，文章可能有点水，有问题大家可以关注我公众号，一起交流</p>
<p>注释都写到代码里面了，望见谅</p>
</blockquote></div>  
</div>
            