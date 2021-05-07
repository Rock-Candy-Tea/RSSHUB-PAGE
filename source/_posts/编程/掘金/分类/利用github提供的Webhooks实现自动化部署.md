
---
title: '利用github提供的Webhooks实现自动化部署'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/145c1f5cc2be45a898f8851a7186d931~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 06 May 2021 22:22:58 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/145c1f5cc2be45a898f8851a7186d931~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/145c1f5cc2be45a898f8851a7186d931~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>

<blockquote>
<p>实现自动部署的关键就是利用github的webhooks，我们在github建立一个项目之后，在项目主页点击Settings，看到Webhooks点击打开可以添加一个链接，这里的意思是，github可以帮你监听一些项目发生的事件，当指定事件发生时，会向你指定的链接发一个post请求，然后你就可以知道自己的哪个项目发生了什么事情，再去做一些具体的操作，那么这时就可以利用shell脚本实现项目自动pull并且重新部署，最后实现的效果就是在本地push代码，一段时间过后，效果就展示在了网站上面。</p>
</blockquote>
<h2 data-id="heading-0">1.配置git SSH 公钥和私钥</h2>
<p>可自行Google(最简单的基本操作)：配置成功之后，服务就能拉取github的代码了</p>
<h2 data-id="heading-1">2.配置Webhooks</h2>
<p>新建项目=>Settings=>Webhooks=>add hooks
配置项如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash">
Payload URL // hook触发的接口地址
Content <span class="hljs-built_in">type</span> // request类型(这里以application/json为例)
Secret // 加密的秘钥
Which events would you like to trigger this webhook // 想要触发的时间，默认选择第一个(push事件)
Active // 是否提供详细信息

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be43d38be4b848e29f2b10c4c8531653~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">3.创建自动化部署Shell脚本(也可以是其他脚本或手段，这里以Shell为例)</h2>
<pre><code class="hljs language-bash copyable" lang="bash">
<span class="hljs-comment">#!/bin/bash</span>
<span class="hljs-built_in">cd</span> /opt/...
git pull
...
启动命令

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4.编写调用自动化部署Shell的接口(这里以node服务koa2为例，也可以是其他语言服务)</h2>
<h4 data-id="heading-4">将创建Webhooks时填写的Secret存出在服务器环境变量中(这里以contos7为例)</h4>
<p>临时生效：</p>
<pre><code class="hljs language-bash copyable" lang="bash">
<span class="hljs-built_in">export</span> SECRET_TOKEN=创建Webhooks时填写的Secret

<span class="hljs-built_in">echo</span> <span class="hljs-variable">$SECRET_TOKEN</span> // 验证是否成功

<span class="copy-code-btn">复制代码</span></code></pre>
<p>永久生效：</p>
<pre><code class="hljs language-bash copyable" lang="bash">
vim /etc/profile

在最后，添加:

SECRET_TOKEN=创建Webhooks时填写的Secret
<span class="hljs-built_in">export</span> SECRET_TOKEN

保存，退出

<span class="hljs-built_in">source</span> /etc/profile

<span class="hljs-built_in">echo</span> <span class="hljs-variable">$SECRET_TOKEN</span> // 验证是否成功

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">创建koa2项目并编写调用自动化部署Shell的接口</h4>
<p>创建koa2项目，对项目进行常规配置(此处省略500字，这里不属于本文重点介绍的内容，有兴趣请自行Google)</p>
<p>关键代码性代码：</p>
<pre><code class="hljs language-bash copyable" lang="bash">
const router = require(<span class="hljs-string">'koa-router'</span>)()
const childProcess = require(<span class="hljs-string">'child_process'</span>) // 创建子进程
const crypto = require(<span class="hljs-string">'crypto'</span>) // 加密解密工具

router.post(<span class="hljs-string">'/url'</span>, <span class="hljs-keyword">function</span> (ctx, next) &#123; // 这里的/url必须与配置Webhooks时填写的接口路径相同
  const hubSignatureKV=ctx.header[<span class="hljs-string">'x-hub-signature'</span>]
  <span class="hljs-keyword">if</span>(hubSignatureKV)&#123;
    // 获取github签名
    const hubSignature=hubSignatureKV.slice(5)
    // 获取系统环境变量SECRET_TOKEN
    const secret=process.env.SECRET_TOKEN
    // 创建一个hmac对象(必须是sha1算法，secret作为加密秘钥)
    const hmac = crypto.createHmac(<span class="hljs-string">'sha1'</span>, secret)
    // 往hmac对象中添加摘要内容(必须是请求主体，因为Content <span class="hljs-built_in">type</span>配置为application/json，所有此处需要转为json字符串)
    const up = hmac.update(JSON.stringify(ctx.request.body))
    // 使用 digest 方法生成加密内容(必须是hex格式)
    const signature = up.digest(<span class="hljs-string">'hex'</span>)
    <span class="hljs-keyword">if</span>(hubSignature===signature)&#123; // 相同则验证成功
      childProcess.exec(<span class="hljs-string">'/opt/shell/hexo.sh'</span>,<span class="hljs-keyword">function</span>(err)&#123; // 利用子进程执行系统命令
        console.log(err)      //当成功是error是null 
      &#125;)
      ctx.body = <span class="hljs-string">'执行成功'</span>
    &#125;<span class="hljs-keyword">else</span>&#123;
      ctx.body = <span class="hljs-string">'服务器已积极拒绝你的请求'</span>
    &#125;
  &#125;<span class="hljs-keyword">else</span>&#123;
    ctx.body = <span class="hljs-string">'服务器已积极拒绝你的请求'</span>
  &#125;

&#125;)

module.exports = router

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">5.部署接口服务并验证</h2>
<p>将服务部署到服务器(这里案例为node服务，推荐使用pm2守护进程部署)
部署成功之后推送代码验证即可</p>
<p>快让你的github运转起来吧!</p>
<p><strong>作者：自如大前端研发中心-客端研发组-李会鑫</strong></p>
<h2 data-id="heading-7">招聘信息</h2>
<p>自如大前端研发中心招募新同学！FE/IOS/Android工程师
公司福利有：</p>
<ul>
<li>全额五险一金，并额外购买商业保险</li>
<li>免费健身房+年度体检</li>
<li>公司附近租房9折优惠</li>
<li>晚间打车报销</li>
<li>每年2次晋升机会</li>
</ul>
<p>欢迎对技术有执着热爱的你加入我们！简历请投递 <a href="mailto:zhangxl122@ziroom.com">zhangxl122@ziroom.com</a>, 或加微信 v-nice-v 详聊！</p></div>  
</div>
            