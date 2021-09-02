
---
title: '【Docker】镜像打造指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1787096d59e43ecb4dd0627565bb1e2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 22:16:30 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1787096d59e43ecb4dd0627565bb1e2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Docker简介</h2>
<blockquote>
<p>Docker 是一个开放源代码软件，是一个开放平台，用于开发、交付和运行应用。 Docker允许用户将基础设施中的应用单独分割出来，形成更小的颗粒（容器），从而提高交付软件的速度。
Docker使用Go语言开发，利用Linux核心中的资源分离机制，如<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FCgroups" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/Cgroups" ref="nofollow noopener noreferrer">cgroups</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FLinux_namespaces" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Linux_namespaces" ref="nofollow noopener noreferrer">namespaces</a>等来创建独立的容器。Linux对namespace的支持完全隔离了工作环境中应用程序的视野，包括行程树、网络、用户ID与挂载文件系统，而核心的cgroup提供资源隔离，包括CPU、存储器、block I/O与网络。
—— Wikipedia</p>
</blockquote>
<p>本文旨在介绍打造Docker镜像的实战和优化，不对docker的原理和运行机制作过多的探讨，读者需对docker的镜像（image）、容器（container）、仓库（Repository）等概念有一定了解。</p>
<h2 data-id="heading-1">Docker镜像（Image）</h2>
<p>Docker本质上是一个运行在Linux操作系统上的应用，而Linux操作系统分为<code>内核</code>和<code>用户空间</code>，内核启动后，通过挂载root文件系统（Root FileSystem）来提供用户空间，Docker镜像就是一个Linux的<code>root文件系统</code>。</p>
<p>Docker镜像提供容器运行时所需的程序、库、资源、配置等文件，以及一些为运行时准备的配置参数（如匿名卷、环境变量、用户等）。</p>
<p>镜像有几个特征：<code>分层、无状态、只读</code>。</p>
<p>镜像不包含任何动态数据（无状态的），其内容在构建之后也不会被改变（只读）。</p>
<h3 data-id="heading-2">分层</h3>
<p>Docker镜像的分层基于<code>UnionFS（联合文件系统）</code>。UnionFS是一种分层、轻量级并且高性能的文件系统，它支持对文件系统的修改作为一次提交来一层层的叠加，同时可以将不同目录挂载到同一个虚拟文件系统下。</p>
<p>分层一个最大的好处是可以<code>共享资源</code>。例如本地有多个镜像都是基于一个基础镜像构建而成，那磁盘中就只需要保存一份基础镜像；并且镜像的某一层也可以被多个镜像共享。利用分层做缓存的会在下文的构建优化中详细介绍。</p>
<h2 data-id="heading-3">构建镜像实战</h2>
<p>尝试构建一个简单的基于express的node server镜像，代码库目录如下：</p>
<pre><code class="copyable">|--Dockerfile
|--src/
| |--index.js
|--package.json
|--yarn.lock
<span class="copy-code-btn">复制代码</span></code></pre>
<p>src/index.js：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>)

<span class="hljs-keyword">const</span> app = express()

<span class="hljs-keyword">const</span> port = <span class="hljs-number">8047</span>

app.get(<span class="hljs-string">'/'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    res.send(<span class="hljs-string">'Hello World!'</span>)
&#125;)

app.listen(port, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`Example app listening at http://localhost:<span class="hljs-subst">$&#123;port&#125;</span>`</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">Dockerfile</h3>
<p>Dockerfile是如何构建镜像的描述文件，下面是一个简单的例子：</p>
<pre><code class="hljs language-Dockerfile copyable" lang="Dockerfile"><span class="hljs-keyword">FROM</span> node:<span class="hljs-number">12.10</span>.<span class="hljs-number">0</span>

<span class="hljs-comment"># 设置环境变量</span>
<span class="hljs-keyword">ENV</span> SERVER_PATH=/server

<span class="hljs-comment"># 设置工作目录</span>
<span class="hljs-keyword">WORKDIR</span><span class="bash"> <span class="hljs-variable">$SERVER_PATH</span></span>

<span class="hljs-comment"># 安装pm2，使用pm2作为进程守护工具启动node服务</span>
<span class="hljs-keyword">RUN</span><span class="bash"> yarn global add pm2</span>

<span class="hljs-comment"># 把当前目录下的所有文件拷贝到镜像的工作目录下</span>
<span class="hljs-keyword">COPY</span><span class="bash"> . <span class="hljs-variable">$SERVER_PATH</span></span>

<span class="hljs-comment"># 安装依赖</span>
<span class="hljs-keyword">RUN</span><span class="bash"> yarn</span>

<span class="hljs-comment"># 暴露端口</span>
<span class="hljs-keyword">EXPOSE</span> <span class="hljs-number">8047</span>

<span class="hljs-comment"># 镜像运行后执行的node服务启动命令</span>
<span class="hljs-keyword">CMD</span><span class="bash"> [<span class="hljs-string">"pm2"</span>, <span class="hljs-string">"start"</span>, <span class="hljs-string">"src/index.js"</span>, <span class="hljs-string">"--no-daemon"</span>]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意点：</p>
<ul>
<li>pm2启动服务时默认在后台运行，但是docker运行时需保持一个进程在前台，所以要加上<code>--no-daemon</code>参数</li>
</ul>
<h3 data-id="heading-5">构建镜像</h3>
<p>代码准备完成后，运行docker build命令即可构建镜像，格式如下：</p>
<p><code>docker build [OPTIONS] PATH | URL | -</code></p>
<p>如：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 最后的 . 是指基于当前目录下的dockerfile构建镜像</span>
docker build -t server-template:latest .

<span class="hljs-comment"># 运行镜像</span>
docker run -p 8047:8047 server-template:latest
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">镜像优化</h3>
<h4 data-id="heading-7">使用更小的基础镜像版本</h4>
<p>运行<code>docker images</code>查看已有镜像：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1787096d59e43ecb4dd0627565bb1e2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，上述步骤中构建的镜像大小为972MB，明明是一个非常简单的项目，镜像体积却接近1G，问题出在哪里呢？</p>
<p>绝大部分原因是基础镜像的体积太大，我们Dockerfile的第一行是：</p>
<pre><code class="hljs language-Dockerfile copyable" lang="Dockerfile"><span class="hljs-keyword">FROM</span> node:<span class="hljs-number">12.10</span>.<span class="hljs-number">0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>意为基于官方提供的<a href="https://link.juejin.cn/?target=mailto%3Anode%4012.10.0" target="_blank" title="mailto:node@12.10.0" ref="nofollow noopener noreferrer">node@12.10.0</a>版本镜像构建，但官方提供了更纯净的<code>Alpine</code>版本，我们将第一行改为：</p>
<pre><code class="hljs language-Dockerfile copyable" lang="Dockerfile"><span class="hljs-keyword">FROM</span> node:<span class="hljs-number">12.10</span>.<span class="hljs-number">0</span>-alpine
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再重新构建一次，可以看到镜像大小变成了144M：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/332114ca31774a668e58fdd3ff101403~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>官方提供了三种类型node镜像的选择：</p>
<ul>
<li>
<p><code>node:<version></code>：官方默认镜像，基于debian构建，此类镜像的优点是安装的依赖很全，例如curl、wget，缺点是体积过大。</p>
</li>
<li>
<p><code>node:<version>-slim</code>：删除冗余依赖后的精简版本镜像，同样是基于 debian 构建，体积上比默认镜像小很多，删除了很多公共的软件包，只保留了最基本的 node 运行环境。</p>
</li>
<li>
<p><code>node:<version>-alpine</code>：基于 alpine 镜像构建，比 debian 的 slim 版本还要小。 Alpine 使用 musl 代替 glibc，一些 c/c++ 环境的软件可能不兼容，因此项目如果没使用 C++ 拓展的话，基本都能用该镜像跑起来</p>
</li>
</ul>
<p>镜像的选择不是绝对的，可以根据自身需求来决定。</p>
<p>选择官方版本虽然体积更大，但是功能较为齐全，不用担心以后的拓展问题，而且基于镜像的分层特性，基础镜像下载一次之后可以被多个镜像共享。选择alpine镜像则可以显著提升第一次构建的速度，以及在不同机器上拉取或者构建镜像的速度。</p>
<h4 data-id="heading-8">减少层数</h4>
<p>前面提到过docker镜像的分层特性，实际上，dockerfile里每执行一个指令，就会创建一个镜像层，通过减少层数，也可以减小镜像体积和优化构建速度。</p>
<p>我们可以通过<strong>合并多个指令</strong>来减少层数，例如：</p>
<pre><code class="hljs language-Dockerfile copyable" lang="Dockerfile"><span class="hljs-keyword">FROM</span> node:<span class="hljs-number">12.10</span>.<span class="hljs-number">0</span>-alpine

<span class="hljs-keyword">ADD</span><span class="bash"> . /app</span>

<span class="hljs-keyword">ENV</span> SERVER_PATH=/server

<span class="hljs-keyword">ENV</span> APP_PATH=/app

<span class="hljs-keyword">RUN</span><span class="bash"> <span class="hljs-built_in">cd</span> /app</span>

<span class="hljs-keyword">RUN</span><span class="bash"> yarn</span>

<span class="hljs-keyword">RUN</span><span class="bash"> yarn build</span>

<span class="hljs-keyword">CMD</span><span class="bash"> yarn start</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以合并成：</p>
<pre><code class="hljs language-Dockerfile copyable" lang="Dockerfile"><span class="hljs-keyword">FROM</span> node:<span class="hljs-number">12.10</span>.<span class="hljs-number">0</span>-alpine

<span class="hljs-keyword">ADD</span><span class="bash"> . /app</span>

<span class="hljs-comment"># 设置多个环境变量</span>
<span class="hljs-keyword">ENV</span> SERVER_PATH=/server \

APP_PATH=/app

<span class="hljs-comment"># 一次执行多条命令</span>
<span class="hljs-keyword">RUN</span><span class="bash"> <span class="hljs-built_in">cd</span> /app \
</span>
&& yarn \

&& yarn build

<span class="hljs-keyword">CMD</span><span class="bash"> yarn start</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">前置不常变动的命令，充分利用缓存</h4>
<p>我们应该把变化最少的指令放在 Dockerfile 前面，这样可以充分利用镜像缓存。</p>
<p>例如常见的npm包依赖缓存，原Dockerfile：</p>
<pre><code class="hljs language-Dockerfile copyable" lang="Dockerfile"><span class="hljs-keyword">FROM</span> node:<span class="hljs-number">12.10</span>.<span class="hljs-number">0</span>-alpine

<span class="hljs-keyword">EXPOSE</span> <span class="hljs-number">8047</span>

<span class="hljs-keyword">WORKDIR</span><span class="bash"> /server</span>

<span class="hljs-comment"># 将当前目录的所有文件复制到工作区</span>
<span class="hljs-keyword">COPY</span><span class="bash"> . .</span>

<span class="hljs-comment"># 安装依赖</span>
<span class="hljs-keyword">RUN</span><span class="bash"> yarn</span>

<span class="hljs-keyword">CMD</span><span class="bash"> yarn start</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子中，我们先将项目的源码都复制到了工作区，然后执行安装依赖的命令。但是由于源码经常变化，导致每次构建镜像时都会重新安装依赖。</p>
<p>因此我们可以先复制package.json和yarn.lock，然后安装依赖，最后再复制其他的源码，这样只要package.json和yarn.lock不变，即使源码发生变动也能复用前面安装了依赖的层的缓存。</p>
<p>使用下面的写法：</p>
<pre><code class="hljs language-Dockerfile copyable" lang="Dockerfile"><span class="hljs-keyword">FROM</span> node:<span class="hljs-number">12.10</span>.<span class="hljs-number">0</span>-alpine

<span class="hljs-keyword">EXPOSE</span> <span class="hljs-number">8047</span>

<span class="hljs-keyword">WORKDIR</span><span class="bash"> /server</span>

<span class="hljs-comment"># 先将package.json和yarn.lock复制到工作区安装依赖</span>
<span class="hljs-keyword">COPY</span><span class="bash"> package.json yarn.lock ./</span>

<span class="hljs-keyword">RUN</span><span class="bash"> yarn</span>

<span class="hljs-keyword">COPY</span><span class="bash"> . .</span>

<span class="hljs-keyword">CMD</span><span class="bash"> yarn start</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">每个 RUN 指令后删除多余文件</h4>
<p>镜像构建时，会一层层构建。前一层是后一层的基础。每一层构建完就不会再发生改变，后一层上的任何改变只发生在当前这一层。</p>
<p>比如，删除前一层文件的操作，实际不是真的删除前一层的文件，而是仅在当前层标记为该文件已删除。最终容器运行的时候该文件其实依然存在。</p>
<p>因此，在构建镜像的时候，每一层应该尽量只包含该层需要添加的东西，任何额外的东西应该在该层构建结束前清理掉。</p>
<p>例如我们的node项目在启动前会使用rollup等构建工具进行ts和babel的转译，则构建完成后之后最好只保留打包之后的代码。</p>
<h4 data-id="heading-11">使用多阶段构建（multistage builds）</h4>
<p>Docker v17.05 开始支持多阶段构建，可以解决镜像层数过多、体积过大的问题，同时可以让dockerfile可读性更好、层次更清晰。</p>
<p>以下面的构建为例：</p>
<pre><code class="hljs language-Dockerfile copyable" lang="Dockerfile"><span class="hljs-keyword">FROM</span> node:<span class="hljs-number">12.10</span>.<span class="hljs-number">0</span>-alpine

<span class="hljs-comment"># 设置环境变量</span>
<span class="hljs-keyword">ENV</span> SERVER_PATH=/server

<span class="hljs-comment"># 暴露端口</span>
<span class="hljs-keyword">EXPOSE</span> <span class="hljs-number">8047</span>

<span class="hljs-comment"># 设置工作目录</span>
<span class="hljs-keyword">WORKDIR</span><span class="bash"> <span class="hljs-variable">$SERVER_PATH</span></span>

<span class="hljs-comment"># 安装pm2</span>
<span class="hljs-keyword">RUN</span><span class="bash"> yarn global add pm2</span>

<span class="hljs-keyword">COPY</span><span class="bash"> package.json yarn.lock ./</span>

<span class="hljs-keyword">RUN</span><span class="bash"> yarn</span>

<span class="hljs-comment"># 把当前目录下的所有文件拷贝到镜像的工作目录下</span>
<span class="hljs-keyword">COPY</span><span class="bash"> . .</span>

<span class="hljs-comment"># 镜像运行后执行的node服务启动命令</span>
<span class="hljs-keyword">CMD</span><span class="bash"> [<span class="hljs-string">"pm2"</span>, <span class="hljs-string">"start"</span>, <span class="hljs-string">"src/index.js"</span>, <span class="hljs-string">"--no-daemon"</span>]</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用多阶段构建改造将其改造：</p>
<pre><code class="hljs language-Dockerfile copyable" lang="Dockerfile"><span class="hljs-comment"># 基础镜像</span>
<span class="hljs-keyword">FROM</span> node:<span class="hljs-number">12.10</span>.<span class="hljs-number">0</span>-alpine AS base

<span class="hljs-keyword">ENV</span> SERVER_PATH=/server

<span class="hljs-keyword">EXPOSE</span> <span class="hljs-number">8047</span>

<span class="hljs-keyword">WORKDIR</span><span class="bash"> <span class="hljs-variable">$SERVER_PATH</span></span>

<span class="hljs-keyword">RUN</span><span class="bash"> yarn global add pm2</span>

<span class="hljs-comment"># 基于base镜像 安装依赖阶段</span>
<span class="hljs-keyword">FROM</span> base AS install

<span class="hljs-keyword">COPY</span><span class="bash"> package.json yarn.lock ./</span>

<span class="hljs-keyword">RUN</span><span class="bash"> yarn</span>

<span class="hljs-comment"># 回到基础镜像</span>
<span class="hljs-keyword">FROM</span> base

<span class="hljs-comment"># 将安装依赖阶段中生成的node_modules目录复制到工作目录</span>
<span class="hljs-keyword">COPY</span><span class="bash"> --from=install <span class="hljs-variable">$SERVER_PATH</span>/node_modules ./node_modules</span>

<span class="hljs-keyword">COPY</span><span class="bash"> . .</span>

<span class="hljs-keyword">CMD</span><span class="bash"> [<span class="hljs-string">"pm2"</span>, <span class="hljs-string">"start"</span>, <span class="hljs-string">"src/index.js"</span>, <span class="hljs-string">"--no-daemon"</span>]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">添加HEALTHCHECK</h4>
<p>在没有 HEALTHCHECK 指令前，Docker 引擎只可以通过容器内主进程是否退出来判断容器是否状态异常。很多情况下这没问题，但是如果程序进入死锁状态，或者死循环状态，应用进程并不退出，但是该容器已经无法提供服务了。</p>
<p>Docker 1.12 版本之后，提供了 HEALTHCHECK 指令，通过该指令指定一行命令，用这行命令来判断容器主进程的服务状态是否还正常，从而比较真实的反应容器实际状态。写法如下：</p>
<pre><code class="hljs language-Dockerfile copyable" lang="Dockerfile"><span class="hljs-keyword">HEALTHCHECK</span><span class="bash"> CMD curl --fail http://localhost:<span class="hljs-variable">$APP_PORT</span> || <span class="hljs-built_in">exit</span> 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上命令会默认每隔30秒向容器的服务发起一个请求，连续失败三次则会终止容器。结合docker的运行参数 <code>--restart always</code> 可以让无法再提供服务的容器自动重启。</p>
<h2 data-id="heading-13">镜像仓库</h2>
<p>在本地构建好镜像后，可以将镜像推送到远端仓库，这样就可以在任何机器上拉取镜像并运行了。</p>
<p>首先在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fhub.docker.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://hub.docker.com/" ref="nofollow noopener noreferrer">Docker Hub</a>注册一个账号，再创建一个<code>Repository</code>，例如我的仓库<a href="https://link.juejin.cn/?target=https%3A%2F%2Fhub.docker.com%2Frepository%2Fdocker%2Fdeland7%2Fserver" target="_blank" rel="nofollow noopener noreferrer" title="https://hub.docker.com/repository/docker/deland7/server" ref="nofollow noopener noreferrer">deland7/server</a>。</p>
<p>然后将本地的镜像重命名和远端仓库一致，我本地的镜像：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2cfe992184843858989e6f43142410b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>重新打tag，推送到远端：</p>
<pre><code class="hljs language-bash copyable" lang="bash">docker tag server-template:latest deland7/server:latest

docker push deland7/server:latest
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后就可以在仓库看到自己的镜像了。</p>
<h2 data-id="heading-14">参考文档</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.docker.com%2Fdevelop%2Fdevelop-images%2Fdockerfile_best-practices%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.docker.com/develop/develop-images/dockerfile_best-practices/" ref="nofollow noopener noreferrer">Best practices for writing Dockerfiles</a></li>
<li><a href="https://juejin.cn/post/6991689670027542564" target="_blank" title="https://juejin.cn/post/6991689670027542564">如何优化 node 项目的 docker 镜像（像老板压榨员工一样压榨镜像）</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fyeasy.gitbook.io%2Fdocker_practice%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://yeasy.gitbook.io/docker_practice/" ref="nofollow noopener noreferrer">Docker —— 从入门到实践</a></li>
</ul></div>  
</div>
            