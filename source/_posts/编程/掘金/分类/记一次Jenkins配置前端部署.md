
---
title: '记一次Jenkins配置前端部署'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6376'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 22:52:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=6376'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>jenkins已经部署在对应服务器上，前端的部署需要自己来新建任务，做一些配置。</p>
<h6 data-id="heading-0">首先：</h6>
<pre><code class="copyable">登陆jenkins图形化界面，插件安装略过，系统管理-插件管理中，NodeJs plugin和git。  
插件安装好之后，去首页的系统配置中找到全局工具配置，在其中找到nodejs，新增安装，这里我选择的是node 14。  
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-1">第二步：</h6>
<pre><code class="copyable">基础条件具备，之后跳转到首页，在对应视图下新建任务，也就是我们的项目部署任务，选择自由风格软件项目。  
【如有可以复制的配置项目，则可以填写被复制的任务名称】  
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-2">第三步：</h6>
<pre><code class="copyable"> 在项目配置中，将描述，源码配置，构建环境（这里去选择之前安装的node版本）填写好。  
 构建模块，选择执行shell，代码如下：  
 
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">#!<span class="hljs-regexp">/bin/</span>bash
echo $PATH <span class="hljs-comment">// 更新环境变量</span>

node -v <span class="hljs-comment">// 输出node版本</span>

npm -v <span class="hljs-comment">// 输出npm版本</span>

npm config set registry https:<span class="hljs-comment">//registry.npm.taobao.org // 修改npm源</span>

npm install <span class="hljs-comment">// 执行安装依赖</span>

npm install -D node-sass@<span class="hljs-number">4.14</span><span class="hljs-number">.1</span> <span class="hljs-comment">// 每次下载都失败，干脆单独执行一次</span>

npm run build <span class="hljs-comment">// 执行打包</span>

cd dist <span class="hljs-comment">// 进入打包文件</span>

rm -rf test.tar.gz <span class="hljs-comment">// 删除上一次的压缩文件</span>

tar -zcvf test.tar.gz * <span class="hljs-comment">// 将打包文件中的所有内容压缩</span>

echo <span class="hljs-string">"完成压缩"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">构建后的操作：   
source file要写dist/test.tar.gz，前缀分别写dist和服务器上前端目录对应的文件名。  
构建后，需要将压缩好的文件传到服务器，并解压覆盖，Exec command如下。  
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">#!<span class="hljs-regexp">/bin/</span>bash
source /etc/profile
cd ...这里写前端代码在服务器上的的文件目录地址例如 /usr/main/html/project
tar -zxvf test.tar.gz
rm -rf test.tar.gz
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-3">第四步</h6>
<pre><code class="copyable">准备工作完成，需要在nginx配置对应的端口号，并指向对应目录的入口文件，例如我们的index.html  
这里我用的是Xshell  
登陆服务器，找到nginx.conf文件，执行vim nginx.conf  
将我们所需要的端口文件目录及代理信息填写完毕。  
执行nginx -s reload，刷新nginx。
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-4">最后</h6>
<pre><code class="copyable">至此，配置完成了，点击任务开始部署，可以在控制台查看具体进度。
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            