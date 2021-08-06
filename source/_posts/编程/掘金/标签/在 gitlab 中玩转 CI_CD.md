
---
title: '在 gitlab 中玩转 CI_CD'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97fb594699f04cb0be16305be8301684~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 23:05:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97fb594699f04cb0be16305be8301684~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style>
<h2 data-id="heading-0">什么是CI/CD</h2>
<p>持续集成（CI）和持续部署（CD）是DevOps中重要的两个环节，传统的软件开发和交付方式正在迅速变得过时，过去软件迭代与开发里，大多数公司的软件发布周期是每月、每季度甚至每年，较长的周期不利于产品的试错以及敏捷开发，而现在，DevOps 时代，每周、每天甚至每天多次都是常态。</p>
<p>开发团队通过编写软件交付流水线（Pipeline）代码实现版本构建，发布的自动化，以快速进行验证和缩短交付周期，更少的去关注部署以及发布的细节，而将更多的精力留在代码质量本身。</p>
<p>在实际使用中，g是开发者通过在itlab的CI/CD离预先配置的一系列<code>pipeline</code>参数，精心掌控触发时机，在代码提交、合并、或者打tag时，触发响应的自动构建流来完成构建到发布的动作。</p>
<h2 data-id="heading-1">GitLab CI/CD 是如何工作的</h2>
<p>为了使用GitLab CI/CD，你需要一个托管在GitLab上的应用程序代码库，并且在根目录中的<code>.gitlab-ci.yml</code>文件中指定构建、测试和部署的脚本。</p>
<p>在这个文件中，你可以定义要运行的脚本，定义包含的依赖项，选择要按顺序运行的命令和要并行运行的命令，定义要在何处部署应用程序，以及指定是否 要自动运行脚本或手动触发脚本。</p>
<p>为了可视化处理过程，假设添加到配置文件中的所有脚本与在计算机的终端上运行的命令相同。</p>
<p>一旦你已经添加了<code>.gitlab-ci.yml</code>到仓库中，GitLab将检测到该文件，并使用名为<code>GitLab Runner</code>的工具运行你的脚本。该工具的操作与终端类似。</p>
<p>这些脚本被分组到<code>jobs</code>，它们共同组成一个<code>pipeline</code>。一个最简单的<code>.gitlab-ci.yml</code>文件可能是这样的：</p>
<pre><code class="hljs language-yml copyable" lang="yml"><span class="hljs-attr">before_script:</span> 
  <span class="hljs-bullet">-</span> <span class="hljs-string">apt-get</span> <span class="hljs-string">install</span> <span class="hljs-string">rubygems</span> <span class="hljs-string">ruby-dev</span> <span class="hljs-string">-y</span> 

<span class="hljs-attr">run-test:</span> 
  <span class="hljs-attr">script:</span> 
    <span class="hljs-bullet">-</span> <span class="hljs-string">ruby</span> <span class="hljs-string">--version</span> <span class="hljs-number">6</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97fb594699f04cb0be16305be8301684~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="20210404014040" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">任务目标</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fab31db4624641ec98bf989a156d7c2b~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="20210330104247" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们的任务目标是搭建一个 gitlab + gitlab-runner 的CICD环境，在代码触发时，启动构建动作，构建完毕后将代码推送到应用服务器上进行部署</p>
<p>应用服务是是一个具备nginx的服务，他暴露了80端口允许你访问端口，应用我们选择前端的 <code>hexo</code> 博客系统，开箱即用</p>
<h2 data-id="heading-3">准备</h2>
<p>为了实现本文档的目标任务，需要做一下软件的前期准备</p>
<ul>
<li>安装docker</li>
<li>了解docker常用操作</li>
<li>apt 软件安装操作</li>
</ul>
<p>为了加快实践操作，你可能还会需要</p>
<ol>
<li>安装docker WSL2</li>
<li>配置镜像加速源（可以自己申请阿里的一个镜像服务，免费的，或者直接使用下面的配置）</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b61b5204ad54cd8a93aab412c30354f~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="20210404013450" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">&#123;
  "registry-mirrors": [
    "https://gk9l8m3a.mirror.aliyuncs.com"
  ],
  "insecure-registries": [],
  "debug": false,
  "experimental": false,
  "features": &#123;
    "buildkit": true
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>apt update/ install 都会比较耗时，可以尝试安装镜像源</li>
</ol>
<h2 data-id="heading-4">相关材料</h2>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.gitlab.com%2Fomnibus%2Fdocker%2Fsunsky2017" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.gitlab.com/omnibus/docker/sunsky2017" ref="nofollow noopener noreferrer">docker安装gitlab</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fma726518972%2Farticle%2Fdetails%2F108146218" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/ma726518972/article/details/108146218" ref="nofollow noopener noreferrer">docker四种网络模式，容器localhost访问宿主机端口</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fnodejs%2Fnodejs-install-setup.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/nodejs/nodejs-install-setup.html" ref="nofollow noopener noreferrer">linux 安装 nodejs</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Flinux%2Flinux-comm-ln.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/linux/linux-comm-ln.html" ref="nofollow noopener noreferrer">linux软连接</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.gitlab.com%2Frunner%2Finstall%2Fdocker.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.gitlab.com/runner/install/docker.html" ref="nofollow noopener noreferrer">安装 gilab-runner</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.gitlab.com%2Fee%2Fci%2Fpipelines%2Fjob_artifacts.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.gitlab.com/ee/ci/pipelines/job_artifacts.html" ref="nofollow noopener noreferrer">Job artifacts</a></li>
</ol>
<h2 data-id="heading-5">环境准备</h2>
<h3 data-id="heading-6">从安装一个 gitlab 开始</h3>
<p>首先我们在docker安装一个gitlab用来做本次实验</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 下载镜像</span>
docker pull gitlab/gitlab-ee

<span class="hljs-comment"># 启动</span>
docker run -d \
  --hostname localhost \
  -p 80:80 \
  --name gitlab \
  gitlab/gitlab-ee:latest

<span class="hljs-comment"># 查看日志</span>
docker logs -f gitlab
<span class="copy-code-btn">复制代码</span></code></pre>
<p>启动阶段要做较多的初始化工作，需要耐心等待。完成后可以通过 <code>80</code> 端口看到gilab。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5f3a60ca3b54374b5ed5cd1e288ed55~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="20210330151758" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>首次登陆需要重置密码，重置密码后即可进入系统</li>
</ul>
<h3 data-id="heading-7">安装并注册 git runner</h3>
<p>安装好 gitlab 后还要安装 gitlab-runner 并注册，gitlab-runner 主要用于响应 gitlab CI/CD，CI/CD里面的script脚本将会被 gitlab-runner 所执行</p>
<pre><code class="hljs language-bash copyable" lang="bash">docker pull gitlab/gitlab-runner

<span class="hljs-comment"># --network host 共享主机网络保证gitrunner能够正确的访问gitlab</span>
docker run -d \
    --name gitlab-runner \
    --network host \
    gitlab/gitlab-runner:latest

<span class="hljs-comment"># 命令模式进入容器</span>
docker <span class="hljs-built_in">exec</span> -it gitlab-runner bash
<span class="copy-code-btn">复制代码</span></code></pre>
<p>进入容器控制台，输入如下命令进行注册</p>
<pre><code class="copyable">gitlab-ci-multi-runner register
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注册时需要一个token参数，可以访问 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%2Fadmin%2Frunners" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost/admin/runners" ref="nofollow noopener noreferrer">http://localhost/admin/runners</a> 这个页面去获取</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fda9f9cbf2e409786f66dcd00dcd1ee~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="20210328171907" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-bash copyable" lang="bash">> gitlab-ci-multi-runner register

Runtime platform arch=amd64 os=linux pid=63 revision=943fc252 version=13.7.0
Running <span class="hljs-keyword">in</span> system-mode.

Enter the GitLab instance URL (<span class="hljs-keyword">for</span> example, https://gitlab.com/):
> http://localhost/

Enter the registration token:
> Q1L_vwDETgx8Fx-Yypfp

Enter a description <span class="hljs-keyword">for</span> the runner:
[23229cabbaf2]: demo
Enter tags <span class="hljs-keyword">for</span> the runner (comma-separated):

Registering runner... succeeded                     runner=Q1L_vwDE
Enter an executor: docker-ssh, virtualbox, kubernetes, docker-ssh+machine, custom, docker, parallels, shell, ssh, docker+machine:
> shell
Runner registered successfully. Feel free to start it, but <span class="hljs-keyword">if</span> it<span class="hljs-string">'s running already the config should be automatically reloaded! 
</span><span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>URL 填写 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost/" ref="nofollow noopener noreferrer">http://localhost/</a></li>
<li>token 从 gitlab 获取</li>
<li>name 随意</li>
<li>不要为 runner 指定 tag， 否则他将会被绑定了 tag 的 job 所使用</li>
<li>executor 填 shell, 其他的不在本次实践范围</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f926e5fab32e4828ad6767abea4222af~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="20210330163620" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后点击编辑，将 lock 那一项给点掉</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ff247a2ff964c24b79001c1de7b730c~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="20210330163658" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后返回列表你会看到</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a7a05a3052b4534bdeaf08d920592b6~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="20210330161142" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了能运行nodejs项目，还需要继续安装 <code>nodejs</code></p>
<pre><code class="hljs language-bash copyable" lang="bash">apt update

<span class="hljs-comment"># 安装解压工具</span>
apt install xz-utils bzip2 -y

<span class="hljs-comment"># 下载</span>
wget https://nodejs.org/dist/v10.9.0/node-v10.9.0-linux-x64.tar.xz  

<span class="hljs-comment"># 解压wget </span>
tar -xf node-v10.9.0-linux-x64.tar.xz

<span class="hljs-comment"># 建立软连接，让npm和node可以在全局调用</span>
ln -b -s /node-v10.9.0-linux-x64/bin/npm /bin/npm
ln -b -s /node-v10.9.0-linux-x64/bin/node /bin/node

<span class="hljs-comment"># 查看node版本</span>
node -v
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">安装一台用于部署的服务器</h3>
<p>至此，我们还需要一台用于部署应用的服务器，我们使用 <code>nginx</code> 镜像</p>
<pre><code class="hljs language-bash copyable" lang="bash">docker pull nginx
docker run -d --name nginx \
    -p 8080:80 \
    nginx:latest 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>启动完毕后，8080端口就可以直接访问了 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A8080%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:8080/" ref="nofollow noopener noreferrer">http://localhost:8080/</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c643b61f1860464690f816d5210a690f~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="20210404014242" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">搭建代码仓库和cicd</h2>
<h3 data-id="heading-10">新建一个仓库</h3>
<p>至此，runner 的执行环境基本做完了，接下来我们需要新建一个代码仓库，然后配置 CI/CD 的相关内容。</p>
<p>我们需要先创建一个仓库</p>
<p>访问 gitlab <a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost/" ref="nofollow noopener noreferrer">http://localhost/</a>, 在 <code>project</code> 里面找到 <code>New Project</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3751323f1a604a4eab16ca13c9401c90~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="20210404014416" loading="lazy" referrerpolicy="no-referrer"></p>
<p>选择从一个模板中新建</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05850fc2958c47dc9cc23066a95fb9b1~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="20210330141010" loading="lazy" referrerpolicy="no-referrer"></p>
<p>找到 hexo 模板（一个静态化的博客系统）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bcb15f4ee654c2aac8db77fd50ac162~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="20210330141031" loading="lazy" referrerpolicy="no-referrer"></p>
<p>新建</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9885c09518144dd6988b1fb32b5a09bb~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="20210330141103" loading="lazy" referrerpolicy="no-referrer"></p>
<p>新建完毕后，可以在根目录下面找到 <code>.gitlab-ci.yml</code> 文件</p>
<h2 data-id="heading-11">测试CI/CD</h2>
<p>模板默认已经配好了CICD，可以直接运行</p>
<h3 data-id="heading-12">配置cicd</h3>
<p>找到 <code>.gitlab-ci.yml</code> 文件，点开编辑</p>
<pre><code class="hljs language-yml copyable" lang="yml"><span class="hljs-attr">image:</span> <span class="hljs-string">node:10.15.3</span>

<span class="hljs-attr">cache:</span>
  <span class="hljs-attr">paths:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">node_modules/</span>

<span class="hljs-attr">before_script:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">test</span> <span class="hljs-string">-e</span> <span class="hljs-string">package.json</span> <span class="hljs-string">&&</span> <span class="hljs-string">npm</span> <span class="hljs-string">install</span>

<span class="hljs-attr">pages:</span>
  <span class="hljs-attr">script:</span>
    <span class="hljs-comment"># hexo构建命令用仓库自身的而不用全局命令</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">./node_modules/hexo/bin/hexo</span> <span class="hljs-string">generate</span>
    <span class="hljs-comment"># scp需要进行进行ssh相关的配置才可以使用，未完成</span>
    <span class="hljs-comment"># - scp -r public root@localhost:/usr/share/nginx/html</span>
  <span class="hljs-attr">artifacts:</span>
    <span class="hljs-attr">paths:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">public</span>
  <span class="hljs-attr">only:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">master</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>保存完毕后，CI/CD 就开始执行</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ed26109801844448bfbc10760bc7bac~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="20210331134531" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">发布程序</h3>
<p>CI/CD 执行完毕后，由于我们配置了 <code>artifacts</code> 参数，可以在 CI/CD 面板中下载构建产物</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ac671481e5745a3bb684216bb9a949b~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="20210331172338" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以直接在应用服务器上面下载这个产物 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.gitlab.com%2Fee%2Fci%2Fpipelines%2Fjob_artifacts.html%23access-the-latest-job-artifacts-by-url" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.gitlab.com/ee/ci/pipelines/job_artifacts.html#access-the-latest-job-artifacts-by-url" ref="nofollow noopener noreferrer">细节看此链接</a></p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 访问ngx应用服务器</span>
docker <span class="hljs-built_in">exec</span> -it nginx bash
<span class="hljs-comment"># 到ngx的目录</span>
<span class="hljs-built_in">cd</span> /usr/share/nginx/
<span class="hljs-comment"># 下载最后一个在master上面构建的包</span>
curl --output artifacts.zip --header <span class="hljs-string">"PRIVATE-TOKEN: s8Y9J1g5Azof89zfhEhN"</span> <span class="hljs-string">"http://192.168.0.157/api/v4/projects/root%2Fblog/jobs/artifacts/master/download?job=pages"</span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>命令中的 Ip 请修改成自己的IP，不要使用localhost, <code>root%2Fblog</code> 是项目路径 <code>root/blog</code> encode之后的，<code>PRIVATE-TOKEN</code> 需要在仓库的 <code>Setting -> access token</code> 获得</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/743551043ff94c03999d85237bc147f7~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="20210331174424" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下载完毕后可以使用 <code>ls</code> 查看</p>
<pre><code class="hljs language-bash copyable" lang="bash">root@d77810f38ca5:/usr/share/nginx<span class="hljs-comment"># ls</span>
artifacts.zip  html
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们将其解压</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 更新软件源</span>
apt update 

<span class="hljs-comment"># 安装解压软件</span>
apt install unzip 

unzip artifacts.zip

<span class="hljs-comment"># 删除旧文件</span>
rm -rf html 

<span class="hljs-comment"># 将目录移到ngx配置目录</span>
mv public html 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a0a9c212b2e4b6e8e78031ea929b2a9~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="20210331180401" loading="lazy" referrerpolicy="no-referrer"></p>
<p>就可以看到结果了（样式问题是工程自己的问题）</p>
<h3 data-id="heading-14">使用 <code>SCP</code> 直接在 <code>CI/CD</code> 中发布</h3>
<p>未完待续</p>

</div>  
</div>
            