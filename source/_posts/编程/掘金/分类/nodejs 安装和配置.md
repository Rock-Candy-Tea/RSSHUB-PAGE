
---
title: 'nodejs 安装和配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/863ca86877b8404c80d92fe5d9b96e19~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 07:57:35 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/863ca86877b8404c80d92fe5d9b96e19~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">nodejs的安装以及配置</h1>
<p>window安装，下一步下一步就行了，接下来是配置</p>
<p>创建好文件夹之后打开cmd 输入：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm config <span class="hljs-built_in">set</span> prefix <span class="hljs-string">"D:\nodejs\node_global"</span> 注意：这里的路径要改成你自己创建的文件夹的路径

npm config <span class="hljs-built_in">set</span> cache <span class="hljs-string">"D:\nodejs\node_cache"</span>　　注意：这里的路径要改成你自己创建的文件夹的路径
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/863ca86877b8404c80d92fe5d9b96e19~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>进入环境变量对话框，在【系统变量】下新建【NODE_PATH】，</p>
</li>
<li>
<p>输入【D:\nodejs\node_global\node_modules】，</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/704bf4646b364c8e80f2d5e702421053~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>将【用户变量】下的【Path】修改为【D:\nodejs\node_global】</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdd04c4791b344a3b24bf6250fa01665~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3660579edcac4bd397c9ecdb4c13812c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04c0284cb1f34308b56bde88fd8e1430~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>配置完后，安装个module测试下，我们就安装最常用的express模块，打开cmd窗口，</p>
</li>
<li>
<p>输入如下命令进行模块的全局安装：npm install express -g 　　注 -g是全局安装的意思</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90238b6f31244ed188470b58ea24247a~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">nodejs 换源</h1>
<ul>
<li>解决npm install安装慢的问题</li>
<li>国外镜像会很慢</li>
<li>可用 get命令查看registry</li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash">npm config get registry
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>原版结果为</li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash">http://registry.npmjs.org
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>用set命令换成阿里的镜像就可以了</li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash">npm config <span class="hljs-built_in">set</span> registry https://registry.npm.taobao.org
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>再执行命令</li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash">npm install
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>或者直接执行</li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash">npm install --registry=https://registry.npm.taobao.org
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">装cnpm</h1>
<pre><code class="hljs language-bash copyable" lang="bash">npm install -g cnpm --registry=https://registry.npm.taobao.org
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后配置环境变量</p>
<h1 data-id="heading-3">node-sass问题</h1>
<pre><code class="hljs language-bash copyable" lang="bash">cnpm install node-sass@latest
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者</p>
<p>所以用</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install -g cnpm --registry=https://registry.npm.taobao.org 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>，从淘宝镜像那下载，然后cnpm下载成功。</p>
<p>最后输入</p>
<pre><code class="hljs language-bash copyable" lang="bash">cnpm install node-sass --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>npm run dev终于能跑起来了！！！</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i node-sass -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">nodejs 运行命令</h1>
<p>在IDEA命令行中运行命令：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下载相关依赖;</p>
<p>在IDEA命令行中运行命令：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行项目;</p>
<h1 data-id="heading-5">yum命令彻底删除nodejs，重新安装</h1>
<ul>
<li>第一步 用自带的包管理先删除一次</li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash">yum remove nodejs npm -y
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>手动删除残留</p>
</li>
<li>
<p>进入 /usr/local/lib 删除所有 node 和 node_modules文件夹</p>
</li>
<li>
<p>进入 /usr/local/include 删除所有 node 和 node_modules 文件夹</p>
</li>
<li>
<p>进入 /usr/local/bin 删除 node 的可执行文件</p>
</li>
<li>
<p>安装nodejs官网最新的xz包</p>
</li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 下载</span>
    wget https://nodejs.org/dist/v10.13.0/node-v10.13.0-linux-x64.tar.xz
    
<span class="hljs-comment"># 解压</span>
    xz -d node-v9.8.0-linux-x64.tar.xz
    tar -xvf node-v9.8.0-linux-x64.tar
    
<span class="hljs-comment"># 进入目录</span>
    <span class="hljs-built_in">cd</span> node-v10.13.0-linux-x64/
    
<span class="hljs-comment"># 创建软连接</span>
    ln -s /opt/nodejs/node-v10.13.0-linux-x64/bin/node /usr/<span class="hljs-built_in">local</span>/bin/node
    ln -s /opt/nodejs/node-v10.13.0-linux-x64/bin/npm /usr/<span class="hljs-built_in">local</span>/bin/npm
    
<span class="hljs-comment"># 测试</span>
    node -v
    npm -v
    
 <span class="hljs-comment"># 配置taobao镜像</span>
    npm config <span class="hljs-built_in">set</span> registry https://registry.npm.taobao.org
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            