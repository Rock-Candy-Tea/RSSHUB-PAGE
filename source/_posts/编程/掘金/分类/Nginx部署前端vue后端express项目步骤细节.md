
---
title: 'Nginx部署前端vue后端express项目步骤细节'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2929767a49904020b1d334e175ae2ec0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 02 Sep 2021 20:41:47 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2929767a49904020b1d334e175ae2ec0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>项目前端使用vue画页面、后端使用express写接口。部署项目之前，要做好准备工作。要把前端的vue项目<code>npm run build</code>打包生成一个<code>dist</code>文件夹，同时也要把nginx安装好。我们接着往下阅读步骤：</p>
</blockquote>
<h2 data-id="heading-0">第一步</h2>
<p>首先找到nginx安装的目录，然后修改nginx的服务配置文件，是在nginx安装目录里的<code>conf</code>文件夹中的<code>nginx.conf</code>这个文件，我们使用vscode打开，并加上一个<code>serve&#123;&#125;</code>配置我们所需要的反向代理，接下来就是写对应nginx配置代码了</p>
<h2 data-id="heading-1">第二步</h2>
<p>我们比较喜欢 <code>5678</code>这个数字，于是我们就把自己电脑上的 <code>5678</code>这个端口开放给用户使用。即：我们使用nginx这个工具（哨兵）监听本机的<code>5678</code>这个端口，当有用户来访问这个端口的时候，我们就给到相应的反馈。</p>
<p>所以对应nginx代码：<code>listen 5678</code></p>
<h2 data-id="heading-2">第三步</h2>
<p>假设我们电脑的<code>ip</code>是<code>10.9.26.121</code>，因为我们用自己的电脑当做服务器部署项目。</p>
<p>所以对应nginx代码： <code>server_name 10.9.26.121</code></p>
<h2 data-id="heading-3">第四步</h2>
<p>当用户访问我们的ip端口时，即：用户访问：<code>10.9.26.121:5678</code>的时候，因为哨兵工具nginx在时时刻刻监听监视这个ip端口。所以nginx收到ip端口的访问请求时，就会把请求转发到，或者说定位location到我们前端vue项目打包好的dist文件中去。dist文件夹中的存放的是我们写好的前端页面代码，代码解析执行，用户即可看到前端页面。因为程序执行需要找到对应的文件代码位置，所以root就是对应前端打包代码dist存放的位置。至于dist入口，肯定是index.html不需赘述。对应nginx代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">location / &#123; 
    root D:<span class="hljs-regexp">/nginx-1.18.0/</span>html/personManage/dist; 
    index index.html; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如上述的root是，我把vue打包的dist文件放在电脑D磁盘中的这个目录位置<code>D:/nginx-1.18.0/html/personManage/dist</code> 但是注意，这里有一个坑：如果我们直接在文件地址栏复制dist文件地址位置，复制的结果是不对的。如下图这样的错误操作：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2929767a49904020b1d334e175ae2ec0~tplv-k3u1fbpfcp-watermark.image" alt="1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>我们最终复制到的是这样的地址：<code>D:\nginx-1.18.0\html\personManage</code>，如果我们直接把这个地址放在root后面，运行nginx以后，会显示<code>500 Internal Server Error</code>，因为这里是去文件夹里面找程序代码，所以需要用正斜杠<code>/</code>，这样的话nginx才能识别，即，解决方案为：</p>
<p>修改成：<code>D:/nginx-1.18.0/html/personManage/dist</code>（毕竟windows喜欢用反斜杠<code>\</code>，但是Nginx只使用正斜杠<code>/</code>）</p>
</blockquote>
<h2 data-id="heading-4">第五步</h2>
<p>又因为，前端vue项目中ajax交互跨域解决方案使用的是vue.config.js中的devServer中proxy代理，所以nginx中还需要一个location去处理，前端跨域请求转发的问题，所以proxy中的跨域转发前缀要和nginx中的跨域转发前缀保持一致，页面接口交互才能正常实现。图示如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32fabfbe870c405fa15a43097fbbd88d~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">最终nginx代码</h3>
<pre><code class="hljs language-js copyable" lang="js"># personManage项目 history路由模式
server &#123;
    listen<span class="hljs-number">5678</span>; # 给用户使用<span class="hljs-number">5678</span>端口并监听
    server_name<span class="hljs-number">10.9</span><span class="hljs-number">.26</span><span class="hljs-number">.121</span>; # 本机服务器ip地址为：<span class="hljs-number">10.9</span><span class="hljs-number">.26</span><span class="hljs-number">.121</span>
    client_max_body_size 100m; # 上传大文件的配置，nginx默认20M容量，想要上传更大文件，就要额外设置
    location / &#123; # 定位具体的文件入口
        try_files $uri $uri/ /index.html; # 解决vue中history路由模式，部署后刷新页面<span class="hljs-number">404</span>问题，hash路由模式则不需要
        root D:<span class="hljs-regexp">/nginx-1.18.0/</span>html/personManage/dist; # 前端代码dist文件所在磁盘目录位置
        index index.html; # dist文件夹中的入口文件index.html
    &#125;
    location /api/ &#123; # 处理前端跨域转发请求
        # 我们后端express服务启用的端口是<span class="hljs-number">9999</span>，所以这里就转发到这个地址
        proxy_pass http:<span class="hljs-comment">//10.9.26.121:9999/;</span>
        # 下面三句话是用来获取用户访问的ip的
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $remote_addr;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>后端express启用的是9999端口，代码：</p>
<p><code>app.listen(9999, (req,res) => &#123; console.log('后端服务端口地址为：localhost://9999') &#125; )</code></p>
</blockquote>
<h2 data-id="heading-6">第六步</h2>
<p>因为后端我们使用的是node中的express框架，不是java中的springboot框架什么的，不需要打一个jav包，我们只需要在express中使用pm2插件去管理我们的后端项目即可。</p>
<h3 data-id="heading-7">6.1 全局安装pm2</h3>
<p><code>npm install -g pm2</code></p>
<h3 data-id="heading-8">6.2 使用pm2启动express项目</h3>
<p>之前我们启动express项目使用的命令是<code>node app.js</code>，但是有局限，所以我们使用pm2这个插件去管理后端的express项目。pm2功能挺强大的，包括开机自启动项目、停止项目、进程管理、负载均衡、日志查看等功能，而node app.js只能启动项目，所以还是要使用pm2更加方便管理。</p>
<p>全局安装好pm2以后，我们执行<code>pm2 -v</code>命令能查看到版本号，就说明我们已经安装成功了，然后执行<code>pm2 start app.js</code>启动项目。出现下图，就说明我们服务启动好了，然后用户就可以正常访问了</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a116d9c487f43cc95c5c06a26e33def~tplv-k3u1fbpfcp-watermark.image" alt="333.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">总结</h2>
<p>上述就是nginx部署一个vue+express项目的流程步骤。如果大家想进一步了解pm2插件的使用细节，可以去pm2官网看看。附上传送门:<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpm2.keymetrics.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://pm2.keymetrics.io/" ref="nofollow noopener noreferrer">pm2.keymetrics.io/</a></p></div>  
</div>
            