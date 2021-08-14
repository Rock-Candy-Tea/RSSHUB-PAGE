
---
title: '别人过七夕，我在搭网站 -- 腾讯云CentOS机器搭建 个人 网站'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4399b6865328415ba2da745bccbd3fa5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 18:46:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4399b6865328415ba2da745bccbd3fa5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第14天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<blockquote>
<p>早先参加鹅厂的活动白嫖了个腾讯的机器，尝试了下自己手动创建个人网站，有需求的小白们可以一步步操作搭建自己的个人网站。</p>
</blockquote>
<blockquote>
<p>文章发布这天恰好传统佳节--七夕节，祝各位看到文章的朋友们都有甜美的爱情！或基情！</p>
</blockquote>
<blockquote>
<p>更多文章在我的github及个人公众号【全栈道路】上，欢迎观赏<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fprogrammer-zhang%2Ffront-end" title="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fprogrammer-zhang%2Ffront-end" target="_blank">【前端知识点】</a>，如有受益，不要钱，小手点个Star</p>
</blockquote>
<h2 data-id="heading-0">阅读本文您将收获</h2>
<ul>
<li>使用腾讯云机器搭建网站环境</li>
</ul>
<h2 data-id="heading-1">运行环境</h2>
<h3 data-id="heading-2">本地环境</h3>
<ul>
<li>MacBook Pro</li>
<li>macOS Mojave 10.14.6</li>
</ul>
<h3 data-id="heading-3">腾讯云主机</h3>
<ul>
<li>CentOS 7.6 64位</li>
<li>1 核 1 GB 1 Mbps</li>
<li>高性能云硬盘</li>
</ul>
<h2 data-id="heading-4">准备工作</h2>
<ul>
<li>服务器实例正常启动</li>
<li>web端登录实例</li>
<li>畅通的网络</li>
</ul>
<h2 data-id="heading-5">服务器环境设置</h2>
<h3 data-id="heading-6">手动安装node</h3>
<ul>
<li>
<p>根据云主机系统选择node版本</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fen%2Fdownload%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/en/download/" ref="nofollow noopener noreferrer">NodeJS官方下载地址</a></li>
</ul>
</li>
<li>
<p>登录云主机 并 下载node安装包(记住安装路径，免得下载完找不到安装包)</p>
<ul>
<li>方式一：直接下载</li>
</ul>
<pre><code class="copyable">wget http://nodejs.org/dist/v8.9.4/node-v8.9.4-linux-x64.tar.gz
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>方式二：本地拷贝 拷贝到云主机地址下的文件夹</li>
</ul>
<pre><code class="copyable">scp /local/file/path  root@187.xxx.xxx.xxx:/test
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>解压安装包</p>
<ul>
<li>由于安装包是.gz格式的，我们首先需要先解压</li>
</ul>
<pre><code class="copyable">tar -zxvf node-v8.9.4-linux-x64.tar.gz
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>解压成功会在当前文件夹生成 node 包，包名过长过复杂可重命名</p>
<pre><code class="copyable">mv node-v8.9.4-linux-x64 node
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>全局设置 node 环境变量</p>
<ul>
<li>找到.bash_profile文件</li>
</ul>
<pre><code class="copyable">vim ~/.bash_profile
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>修改文件</li>
</ul>
<pre><code class="copyable">PATH=$PATH:$HOME/bin:/usr/local/src/node/bin
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>保存文件</li>
</ul>
<pre><code class="copyable">source ~/.bash_profile
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>检查 NodeJS 是否安装成功 <code>node -v</code></p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4399b6865328415ba2da745bccbd3fa5~tplv-k3u1fbpfcp-watermark.image" alt="node-success.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>检查 云服务 是否正常
<ul>
<li>在机器中创建server.js</li>
</ul>
<pre><code class="copyable">// 创建HTTP服务
var http = require('http');
http.createServer(function (req, res) &#123;
res.writeHead(200, &#123;'Content-Type': 'text/plain'&#125;);
res.end('Welcome Node.js');
&#125;).listen(8080, '0.0.0.0'); // 注意这里是监听 0.0.0.0 的端口
console.log('Server running at http://0.0.0.0:8080/');
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>启动 server 服务 <code>node server.js</code></li>
</ul>
</li>
<li>访问机器外网IP，访问成功即为云服务器搭建成功</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b74b7b1087e49d684b8092d48a0db70~tplv-k3u1fbpfcp-watermark.image" alt="server-success.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>访问机器外网IP，访问失败请按照腾讯云服务器自检文档进行自检
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcloud.tencent.com%2Fdocument%2Fproduct%2F213%2F14633" target="_blank" rel="nofollow noopener noreferrer" title="https://cloud.tencent.com/document/product/213/14633" ref="nofollow noopener noreferrer">自检文档地址</a></li>
</ul>
</li>
</ul>
<h3 data-id="heading-7">安装 Git</h3>
<ul>
<li>Git 安装</li>
</ul>
<pre><code class="copyable">sudo yum install git
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>检查 git 是否安装成功</li>
</ul>
<pre><code class="copyable">git --version
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">安装 Nginx</h3>
<ul>
<li>使用 yum 安装</li>
</ul>
<pre><code class="copyable">sudo yum install nginx
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>修改 Nginx 配置</li>
</ul>
<pre><code class="copyable">server &#123;
    listen  80;
    root /home/project/dist;
    server_name localhost; 

    location / &#123;
       try_files $uri $uri/ @router;
       index index.html;
    &#125;

    location @router &#123;
       rewrite ^.*$ /index.html last;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">项目本地创建与测试</h2>
<blockquote>
<p>本项目基于 Vue-cli 搭建, Vue 项目 的搭建想必熟悉前端开发的同学已经很熟悉，所有本文这部分一笔带过，不做过多赘述</p>
</blockquote>
<h3 data-id="heading-10">Vue项目本地创建</h3>
<ul>
<li>使用 NPM 安装 vue-cli</li>
</ul>
<pre><code class="copyable">npm install vue -g
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用 vuw-cli 创建本地初始项目</li>
</ul>
<pre><code class="copyable">vue init webpack <project-name>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">项目本地启动</h3>
<ul>
<li>安装 node 依赖</li>
</ul>
<pre><code class="copyable">npm install
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">本地 node 启动访问 (开发、测试、生产环境启动)</h5>
<ul>
<li>启动指令具体查看 package.json</li>
</ul>
<pre><code class="copyable">npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13">本地 nginx 访问静态包 (测试、生产环境)</h5>
<ul>
<li>项目打包成静态资源(打包指令具体查看 package.json)</li>
</ul>
<pre><code class="copyable">npm run build
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">git 关联并上传</h3>
<ul>
<li>git 创建远程分支</li>
<li>本地项目 git 初始化</li>
</ul>
<pre><code class="copyable">git init
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>关联远程分支</li>
</ul>
<pre><code class="copyable">git remote add < git 远程地址 >
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>将本地分支加入项目管理</li>
</ul>
<pre><code class="copyable">git add .
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>提交本地分支到远程分支并添加注释</li>
</ul>
<pre><code class="copyable">git commit -m "注释内容" 
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>推送到远程分支</li>
</ul>
<pre><code class="copyable">git push origin <feature>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">服务器手动部署项目</h2>
<h3 data-id="heading-16">服务器添加项目</h3>
<ul>
<li>使用 Git 进行 clone 项目</li>
</ul>
<pre><code class="copyable">git clone < 项目git地址 >
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">服务器启动项目</h3>
<ul>
<li>服务器安装 node 依赖</li>
</ul>
<pre><code class="copyable">npm install
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>若依赖安装失败可使用本地运行时的依赖(建议打包后移动) 或 修改 npm 源为国内源后重新操作</li>
</ul>
<pre><code class="copyable">scp /Personal/web-projects/xxx/node_modules.tar  root@182.254.xxx.xxx:/项目地址
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-18">进行 node 启动</h5>
<ul>
<li>服务器启动</li>
</ul>
<pre><code class="copyable">npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-19">nginx 访问静态包</h5>
<ul>
<li>将项目打包为静态包</li>
</ul>
<pre><code class="copyable">npm run build
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>nginx 配置 跳转</li>
</ul>
<h3 data-id="heading-20">访问网站</h3>
<ul>
<li>若能正常打开首页即为部署成功</li>
<li>若访问不到网站请检查云服务器80端口是否为打开状态</li>
</ul>
<h3 data-id="heading-21">查看监控信息</h3>
<ul>
<li>查看云平台控制台监控信息查看是否正常</li>
<li>使用 <code>PM2</code> 等 node 进程监控管理工具进行监控</li>
</ul>
<h3 data-id="heading-22">二次开发个人网站</h3>
<ul>
<li>首次部署成功后可进行二次开发</li>
<li>二次开发流程和部署流程和首次开发基本相同</li>
<li>也可酌情使用自动化构建工具 <code>jenkins</code> 进行构建</li>
</ul>
<h2 data-id="heading-23">写在最后</h2>
<p>如果你觉得这篇文章对你有益，烦请点赞以及分享给更多需要的人！</p>
<h5 data-id="heading-24">欢迎关注【全栈道路】及微信公众号【全栈道路】，获取更多好文及免费书籍！</h5>
<h5 data-id="heading-25">有需要【百度】&【字节跳动】&【京东】&【猿辅导】内推的也请留言哦，你将享受VIP级极速内推服务~</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79f601eff9e84ebe9c490a5f5833f93e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"> <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0fd9d5a090d42e3bf34593576582f8e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-26">往期好文</h2>
<p><a href="https://juejin.cn/post/6993980017227563021#heading-18" title="https://juejin.cn/post/6993980017227563021#heading-18" target="_blank">微信 JS API 支付的实现</a></p>
<p><a href="https://juejin.cn/post/6991424007069237262" title="https://juejin.cn/post/6991424007069237262" target="_blank">创建个性化的 Github 个人主页</a></p>
<p><a href="https://juejin.cn/post/6901104219995635725" title="https://juejin.cn/post/6901104219995635725" target="_blank">面试官问你<code><img></code>是什么元素时你怎么回答</a></p>
<p><a href="https://juejin.cn/post/6922727457212612621" title="https://juejin.cn/post/6922727457212612621" target="_blank">特殊的JS 浮点数的存储与计算</a></p>
<p><a href="https://juejin.cn/post/6844904116267778055" title="https://juejin.cn/post/6844904116267778055" target="_blank">[万字长文]百度和好未来面试经含答案 | 掘金技术征文</a></p>
<p><a href="https://juejin.cn/post/6879418373365563399" title="https://juejin.cn/post/6879418373365563399" target="_blank">前端实用正则表达式&小技巧，一股脑全丢给你🏆 掘金技术征文|双节特别篇</a></p>
<p><a href="https://juejin.cn/post/6888924266008412167" title="https://juejin.cn/post/6888924266008412167" target="_blank">冷门的 HTML tabindex 详解</a></p>
<p><a href="https://juejin.cn/post/6885952653075939335" title="https://juejin.cn/post/6885952653075939335" target="_blank">几行代码教你解决微信生成海报及二维码</a></p>
<p><a href="https://juejin.cn/post/6878097147649064974" title="https://juejin.cn/post/6878097147649064974" target="_blank">Vue3.0 响应式数据原理：ES6 Proxy</a></p>
<p><a href="https://juejin.cn/post/6844904078615511054" title="https://juejin.cn/post/6844904078615511054" target="_blank">[前端面试]前端缓存问题看这篇，让面试官爱上你</a></p>
<p><a href="https://juejin.cn/post/6992184390210027527" title="https://juejin.cn/post/6992184390210027527" target="_blank">如何优雅地画一条细线</a></p>
<p><a href="https://juejin.cn/post/6844904065688666119" title="https://juejin.cn/post/6844904065688666119" target="_blank">[三分钟小文]前端性能优化-HTML、CSS、JS部分</a></p>
<p><a href="https://juejin.cn/post/6844904065688682510" title="https://juejin.cn/post/6844904065688682510" target="_blank">[三分钟小文]前端性能优化-页面加载速度优化</a></p>
<p><a href="https://juejin.cn/post/6844904065692860424" title="https://juejin.cn/post/6844904065692860424" target="_blank">[三分钟小文]前端性能优化-网络传输层优化</a></p></div>  
</div>
            