
---
title: '利用gitHub的webhooks实现前端项目自动化部署---个人摸索的一次学习总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/588c479f83fb46738802742c04e26973~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 20 Jul 2021 02:52:51 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/588c479f83fb46738802742c04e26973~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作为一个前端，买了腾讯云服务器后，一直想尝试项目自动化打包部署，奈何jenkins体量太大，穷人买的低配服务器还玩不起来，还有gitHub的webhooks，于是自己摸索用node.js结合webhooks跑通了自动部署的流程。</p>
<p>前期准备：一个服务器（自己搭好node环境, 安装好git）, 一个托管在github、部署在服务器上的前端项目。</p>
<ul>
<li><strong>在服务器上创建一个服务（我用node.js），用于监听gitHub的webhooks触发的post请求，</strong></li>
</ul>
<p>请求所带的数据大概如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/588c479f83fb46738802742c04e26973~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>由此可区分出触发的事件(仅识别push触发)和分支(仅对master分支做了识别并自动部署)，之后执行部署脚本。</p>
<p>服务代码deploy.js如下：</p>
<pre><code class="copyable">var http = require('http')

var createHandler = require('github-webhook-handler')

var handler = createHandler(&#123; path: '/', secret: '1qazxsw2' &#125;) 

// 上面的 path 即是github中填写的url的path部分

// 上面的 secret 保持和 GitHub 后台设置的一致 
function run_cmd(cmd, args, callback) &#123;

  var spawn = require('child_process').spawn;  var child = spawn(cmd, args);

  var resp = "";   
  child.stdout.on('data', function(buffer) &#123; resp += buffer.toString(); &#125;);

  child.stdout.on('end', function() &#123; callback (resp) &#125;);

&#125;
 http.createServer(function (req, res) &#123;

  handler(req, res, function (err) &#123;

    res.statusCode = 404

    res.end('no such location')

  &#125;)

&#125;).listen(7777)

// listen(7777)指监听7777端口,可以根据实际情况改成你自己的

handler.on('error', function (err) &#123;

  console.error('Error:', err.message)

&#125;)// push事件触发

handler.on('push', function (event) &#123;

  var name=event.payload.repository.name;

  console.log('Received a push event for %s to %s',    event.payload.repository.name,    event.payload.ref);

  // 判断master分支变动时执行，可根据payload.ref区分分支

  if (event.payload.ref === 'refs/heads/master') &#123;   
     run_cmd('sh', ['./deploy.sh',name], function(text)&#123; console.log(text) &#125;);

  &#125;

&#125;)
//这里为了实现不同仓库的自动部署,传了仓库名给shell脚本 

handler.on('issues', function (event) &#123;

  console.log('Received an issue event for % action=%s: #%d %s',    event.payload.repository.name,    event.payload.action,    event.payload.issue.number,    event.payload.issue.title)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>部署脚本所做的工作：服务器拉取并更新代码库（服务器要配置好git，生成公钥，并在gihub项目上添加公钥），打包生成dist，移动到对应的目录替换发版文件。</p>
<p>部署脚本代码deploy.sh如下</p>
<pre><code class="copyable">#!/bin/bash

WEB_NAME="$1"# 服务器上的项目代码库路径

PROJECT_PATH="/root/project/$&#123;WEB_NAME&#125;/"


# 项目发布的地址，我用的nginx的静态目录DEPLOY_PATH="/usr/share/nginx/html/$&#123;WEB_NAME&#125;/"

cd $PROJECT_PATH

MD5=`md5sum package.json | cut -d' ' -f1`

rm -rf dist

git pull

NEW_MD5=`md5sum package.json | cut -d' ' -f1`

# 利用前后package.json文件MD5值是否变化来决定是否重新npm install

if [ $MD5 == $NEW_MD5 ]; then

    echo '未检测到依赖项改变'else

    echo "change install"

    npm installfi

npm run build

if [[ ! -d "dist" ]]; then

    echo "build error"    exit 1fi

rm -rf $DEPLOY_PATH*

cp -rf dist/* $DEPLOY_PATH 

echo "build success $WEB_NAME"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以用pm2管理此服务，此外，我根据package.json文件MD5值是否变化来选择是否重新安装依赖 npm install。</p>
<h3 data-id="heading-0">在github项目配置url和secert</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2b9dcd2e911421d9043c267f10dd8de~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">测试，修改项目代码，提交、push。查看是否触发，gitHub面板会有触发记录，redeliver按钮也可以方便调试，不用每次都自己push触发。</h3>
<p>如此实现了前端自动部署项目的流程，但是实际生产中，还是jenkin等有界面的ci系统更为可靠。</p></div>  
</div>
            