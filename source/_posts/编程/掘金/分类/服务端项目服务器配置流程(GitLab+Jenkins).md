
---
title: '服务端项目服务器配置流程(GitLab+Jenkins)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5105'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 01:55:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=5105'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">服务端项目服务器配置流程(GitLab+Jenkins)</h1>
<ol>
<li>阿里云域名配置指向到服务器地址</li>
<li>本地通过xshell测试域名是否联通指向服务器<code>ping test.page.com</code></li>
</ol>

<ol start="3">
<li>增加nginx代理</li>
</ol>
<pre><code class="copyable">server &#123;
  listen:80;  # 监听本机所有 ip 上的 80 端口
  server_name test.page.com; # 域名：www.example.com 这里 "_" 代表获取匹配所有
  root /storage/nginx/www/page;  # 此处page代表文件夹名称，匹配所有名字发现为test.page.com 时访问代理的文件夹
  location / &#123;
    index index.htm index.html index.php;
    try_files $uri $uri/ /index.html;
  &#125; #默认访问根目录进入index主页
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>重启 nginx服务</li>
</ol>
<pre><code class="copyable">systemctl stop nginx
systemctl start nginx
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>检查 访问 test.page.com 是否出现502/404提示</li>
<li><code>cd /storge/node</code> 进入node文件配置</li>
</ol>

<ol start="7">
<li>前端项目配置脚本</li>
</ol>
<h5 data-id="heading-1">新增oss配置</h5>
<pre><code class="copyable">const OSS = require('ali-oss');
const util = require('util');
const fs = require('fs');
const path = require('path');

const readdir = util.promisify(fs.readdir);
const stat = util.promisify(fs.stat);

class OssClient &#123;
  constructor() &#123;
    this.client = new OSS(&#123;
      region: 'xxxxxxxxxxx',
      accessKeyId: 'xxxxxxxxxxx', // process.env.ACCESSKEYID,
      accessKeySecret: 'xxxxxxxxxxx', // process.env.ACCESSKEYSECRET,
      bucket: process.env.NODE_ENV === 'production' ? 'xxxxxxxxxxx' : 'xxxxxxxxxxx', // process.env.BUCKET,
    &#125;);
  &#125;

  async putStream(dir, ossDir = '/', fileName) &#123;
    try &#123;
      const stream = fs.createReadStream(path.resolve(dir, fileName));
      return await this.client.putStream(ossDir + fileName, stream);
    &#125; catch (e) &#123;
      console.log(e);
    &#125;
  &#125;

  async putDir(dir, ossDir) &#123;
    let files;
    try &#123;
      files = await readdir(dir);
    &#125; catch (e) &#123;
      console.log(`【当前目录不存在】 -- $&#123;dir&#125; --`);
      return undefined;
    &#125;

    for (const i in files) &#123;
      const state = await stat(`$&#123;dir&#125;/$&#123;files[i]&#125;`);
      if (state.isDirectory()) &#123;
        await this.putDir(`$&#123;dir&#125;/$&#123;files[i]&#125;`, `$&#123;ossDir&#125;/$&#123;files[i]&#125;`);
      &#125; else &#123;
        await this.putStream(dir, `$&#123;ossDir&#125;/`, files[i]);
      &#125;
    &#125;
  &#125;

  async upload() &#123;
    try &#123;
      await this.putDir(path.resolve(__dirname, 'dist'), 'sass-erp-page');
    &#125; catch (e) &#123;
      console.log('【上传异常请重试】', e);
    &#125;
  &#125;
&#125;

new OssClient().upload()
  .then(() => &#123;
    console.log('上传成功')
  &#125;)
  .catch((error) => &#123;
    console.log('上传异常', error);
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-2">根目录下新增build-test.sh</h5>
<pre><code class="copyable">#!/usr/bin/env bash

echo "编译开始..."

git pull

yarn

npm run build:test

npm run oss:test

echo "编译完成..."

echo "复制文件到nginx 静态目录..."

rm -rf  /storage/nginx/www/page/*

\cp -rf dist/index.html  /storage/nginx/www/page

echo "发布完成..."
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">在package.json中增加执行脚本</h5>
<pre><code class="copyable">&#123;
  ...
  "build:test":"cross-env ENV_NODE=test umi build",
  "oss:test":"cross-env ENV_NODE=test node oss.client.js"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>\</p>
<ol start="8">
<li>拉取线上代码，切换分支，执行脚本</li>
</ol>
<pre><code class="copyable">git clone ... # 项目git路径
cd /storge/node/page # 进入项目目录
git checkout develop # 切换分支 
git pull# 拉取代码
sh build-test.sh #执行脚本
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">以上前端项目服务器环境配置完成</h5>
<h5 data-id="heading-5">自动化ci/cd配置</h5>
<ol>
<li>在Jenkins新建项目</li>
</ol>

<ol>
<li>添加项目描述</li>
<li>源代码管理选择Git</li>
</ol>

<ol>
<li>Repositories 地址为GitLab项目地址</li>
<li>指定分支（为空时代表any）</li>
</ol>

<ol start="3">
<li>构建触发器 选择Generic Webhook Trigger</li>
<li>设置token （可选令牌。如果已指定，则只有在调用<strong>http://JENKINS_URL/generic-webhook-trigger/invoke</strong>时提供了该令牌，才能触发此作业）</li>
</ol>

<ol start="5">
<li>构建=》Execute shell</li>
</ol>
<pre><code class="copyable">cd /storage/node/page
sh build-test.sh
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>保存</li>
</ol>

<ol start="2">
<li>打开GitLab当前项目的设置</li>
</ol>

<ol>
<li>点击集成</li>
<li>url：<strong>http://JENKINS_URL/generic-webhook-trigger/invoke (</strong> <strong>JENKINS_URL本地集成环境；有token携带token</strong> <strong>)</strong></li>
</ol>

<ol start="3">
<li>保存当前设置</li>
</ol>
<p>\</p>
<p><strong>自动化ci/cd配置配置完成</strong></p>
<p>\</p>
<p>\</p>
<p>\</p></div>  
</div>
            