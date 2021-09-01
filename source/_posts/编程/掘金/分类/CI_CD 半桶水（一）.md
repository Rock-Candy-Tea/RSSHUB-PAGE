
---
title: 'CI_CD 半桶水（一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a51e31ff1f4542c99dee212182fe8474~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 17:03:59 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a51e31ff1f4542c99dee212182fe8474~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>专栏地址：<strong><a href="https://juejin.cn/column/7001336650957586445" target="_blank" title="https://juejin.cn/column/7001336650957586445">CI/CD 流水线</a></strong></li>
<li>系列文章：<strong><a href="https://juejin.cn/post/7002775438711865352" target="_blank" title="https://juejin.cn/post/7002775438711865352">CI/CD 半桶水（二）</a>、<a href="https://juejin.cn/post/7002776008570961956" target="_blank" title="https://juejin.cn/post/7002776008570961956">CI/CD 半桶水（三）</a></strong></li>
<li>本文作者：<strong><a href="https://juejin.cn/user/2576910985735070" target="_blank" title="https://juejin.cn/user/2576910985735070">Clfeng</a></strong></li>
</ul>
</blockquote>
<h2 data-id="heading-0">导学</h2>
<p>CICD 是持续集成（Continuous Integration）、持续交付（Continuous Delivery）与持续部署（Continuous Deployment）的简称。指在开发过程中自动执行一系列脚本来减低开发引入 bug 的概率，在新代码从开发到部署的过程中，尽量减少人工的介入。相信大伙在工作中也经常与其接触，但可能由于岗位性质的原因，虽是天天使用但对其并不了解，当 CI/CD 流水线出了问题之后也只能是对外求助。为了摆脱这般困境，让我们通过一些列的文章来深入的了解下 CI/CD 吧。</p>
<p>本章的内容会一步步的带着我们从最初的项目创建到 CI/CD 环境安装再到一个简单流水线的编写让我们体会如何搭建自己的 CI/CD。最后会再讲解其最基础的概念，并让我们能清晰的了解我们写的第一个流水线的内容。</p>
<h2 data-id="heading-1">创建 GitLab 项目</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a51e31ff1f4542c99dee212182fe8474~tplv-k3u1fbpfcp-watermark.image" alt="create_project.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">环境安装</h2>
<p><em>注：在企业基本都是使用 linux 环境作为 CI/CD 的 runner ，因此一下的环境安装使用的环境为 linux ；</em></p>
<p>操作系统信息:</p>
<pre><code class="hljs language-shell copyable" lang="shell">Linux version 3.10.0-1160.el7.x86_64 (mockbuild@kbuilder.bsys.centos.org) (gcc version 4.8.5 20150623 (Red Hat 4.8.5-44) (GCC) ) #1 SMP Mon Oct 19 16:18:59 UTC 2020

<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>注：笔者的 linux 环境为在本地的 macOS 上通过虚拟机安装的 centos:7 系统</em></p>
<p><em>读者无需特意去买服务器，使用本地的主机通过虚拟机安装 linux 系统或者是将本地的 macOS 或者 window 作为 runner 都行，但不建议用 windows ，毕竟在写 CI 配置文件的时候会有很多的符号要注意</em></p>
<h3 data-id="heading-3">安装 docker</h3>
<p>后续我们使用的 runner 会以 docker 作为执行器（executor），因此我们先在系统上安装一下 docker 吧。</p>
<p>docker 的安装可按照官网教程进行安装 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.docker.com%2Fengine%2Finstall%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.docker.com/engine/install/" ref="nofollow noopener noreferrer">docs.docker.com/engine/inst…</a></p>
<p>安装的基本流程：</p>
<h4 data-id="heading-4">1. 移除旧版本的 docker</h4>
<pre><code class="hljs language-shell copyable" lang="shell">sudo yum remove docker \
                docker-client \
                docker-client-latest \
                docker-common \
                docker-latest \
                docker-latest-logrotate \
                docker-logrotate \
                docker-engine
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">2. 开始安装 docker</h4>
<pre><code class="hljs language-shell copyable" lang="shell">sudo yum install -y yum-utils
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
<span class="hljs-meta">
#</span><span class="bash"> 安装docker引擎</span>
sudo yum install docker-ce docker-ce-cli containerd.io
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">3. 启动 docker</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">sudo systemctl start docker
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">4. 安装成功</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/379c7589dc724146bc58f9c9811a3f22~tplv-k3u1fbpfcp-watermark.image" alt="install_docker_success.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">安装 runner</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.gitlab.com%2Frunner%2Finstall%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.gitlab.com/runner/install/" ref="nofollow noopener noreferrer">docs.gitlab.com/runner/inst…</a></p>
<h4 data-id="heading-9">1. 执行一下脚本进行 gitlab-runner 的安装</h4>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 1. 添加官方的GitLab仓库</span>
curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.rpm.sh" | sudo bash
<span class="hljs-meta">
#</span><span class="bash"> 2. 安装gitlab-runner</span>
sudo yum install gitlab-runner
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">2. 安装成功</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/866e750dbe644890835557bd831e617a~tplv-k3u1fbpfcp-watermark.image" alt="gitlab_runner_success.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">注册 runner</h3>
<h5 data-id="heading-12">进入项目仓库 CI/CD 页面查看相应的 url 与 token</h5>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dadefde15ab44869636664542ac32c3~tplv-k3u1fbpfcp-watermark.image" alt="register_runner_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-13">执行 <code>gitlab-runner register</code> 命令并根据提示注册 runner</h5>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94dc3eb383fd4c49b2cf988018f0b646~tplv-k3u1fbpfcp-watermark.image" alt="register_runner_2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-14">注册成功之后，查看可用 runner</h5>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7202525f7304890a8a3e1edc1eeb3dc~tplv-k3u1fbpfcp-watermark.image" alt="register_runner_3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到此我们便准备好学习 CI/CD 的基本环境啦～</p>
<p>接着我们尝试写一个简单流水线</p>
<p><em>注：暂时不用去理解 .gitlab-ci.yml 的内容，后续会逐步讲解</em></p>
<h2 data-id="heading-15">第一个流水线</h2>
<h3 data-id="heading-16">添加流水线配置文件</h3>
<p>在项目根目录下，添加 .gitlab-ci.yml 文件，并推送到远程分支，文件内容如下：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-comment"># .gitlab-ci.yml</span>
<span class="hljs-attr">stages:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">build</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">test</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">deploy</span>

<span class="hljs-attr">build_job:</span>
  <span class="hljs-attr">stage:</span> <span class="hljs-string">build</span> <span class="hljs-comment"># 指定job所属stage</span>
  <span class="hljs-attr">image:</span> <span class="hljs-string">centos:7</span> <span class="hljs-comment"># 指定执行job的所使用docker镜像</span>
  <span class="hljs-attr">tags:</span> 
    <span class="hljs-bullet">-</span> <span class="hljs-string">clf-centos-runner</span> <span class="hljs-comment"># 指定执行job的runner（即机器）</span>
  <span class="hljs-attr">script:</span> <span class="hljs-comment"># job执行时运行的脚本</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">echo</span> <span class="hljs-string">"build project"</span>

<span class="hljs-attr">test_job:</span>
  <span class="hljs-attr">stage:</span> <span class="hljs-string">test</span>
  <span class="hljs-attr">image:</span> <span class="hljs-string">centos:7</span>
  <span class="hljs-attr">tags:</span> 
    <span class="hljs-bullet">-</span> <span class="hljs-string">clf-centos-runner</span>
  <span class="hljs-attr">script:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">echo</span> <span class="hljs-string">"test project"</span>

<span class="hljs-attr">deploy_job:</span>
  <span class="hljs-attr">stage:</span> <span class="hljs-string">deploy</span>
  <span class="hljs-attr">image:</span> <span class="hljs-string">centos:7</span>
  <span class="hljs-attr">tags:</span> 
    <span class="hljs-bullet">-</span> <span class="hljs-string">clf-centos-runner</span>
  <span class="hljs-attr">script:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">echo</span> <span class="hljs-string">"deploy project"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">查看流水线执行情况</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43642e7555f044d5b54cc07feb22d85f~tplv-k3u1fbpfcp-watermark.image" alt="simple_pipeline_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a084d45857e04718aca3720fa4f8f43c~tplv-k3u1fbpfcp-watermark.image" alt="simple_pipeline_2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-18">理解基本概念</h2>
<p>在《第一个流水线》章节，我们新增了 .gitlab-ci.yml 并且写了一堆的配置。然后提交文件推送到 GitLab 上之后便可看到有流水线在执行了。那么我们前面在 .gitlab-ci.yml 文件中写的的配置是什么意思？流水线的配置又该怎么写？</p>
<p>为了能写出一个基本的流水线配置，我们需要来学习一下下面的内容：</p>
<ul>
<li>yaml 语法</li>
<li>什么是 CI/CD</li>
<li>CI/CD 的关键概念
<ul>
<li>pipeline</li>
<li>stage</li>
<li>job</li>
</ul>
</li>
</ul>
<h3 data-id="heading-19">yaml 语法</h3>
<p>CI/CD 流水线的配置文件使用的便是 yaml 语法写的，因此需要先理解一下相关的语法。这里推荐通过阮一峰老师的文章进行学习：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2016%2F07%2Fyaml.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.ruanyifeng.com/blog/2016/07/yaml.html" ref="nofollow noopener noreferrer">www.ruanyifeng.com/blog/2016/0…</a></p>
<h3 data-id="heading-20">什么是 CI/CD</h3>
<p>CI/CD 可拆解为 CI 和 CD，其中 CI 为持续集成，CD 为持续交付与持续部署。CI/CD 是一种通过在应用开发阶段引入<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.redhat.com%2Fzh%2Ftopics%2Fautomation%2Fwhats-it-automation" target="_blank" rel="nofollow noopener noreferrer" title="https://www.redhat.com/zh/topics/automation/whats-it-automation" ref="nofollow noopener noreferrer">自动化</a>来频繁向客户交付应用的方法。</p>
<ul>
<li>Continuous Integration (CI) 【持续集成】</li>
<li>Continuous Delivery (CD) 【持续交付】</li>
<li>Continuous Deployment (CD)【持续部署】</li>
</ul>
<p>当然这么介绍可能还是简单了点，所以摘录了以下更为详细的介绍，感兴趣的可以稍微看看</p>
<hr>
<h4 data-id="heading-21">持续集成</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.redhat.com%2Fzh%2Fsolutions%2Fcloud-native-development" target="_blank" rel="nofollow noopener noreferrer" title="https://www.redhat.com/zh/solutions/cloud-native-development" ref="nofollow noopener noreferrer">现代应用开发</a>的目标是让多位开发人员同时处理同一应用的不同功能。但是，如果企业安排在一天内将所有分支源代码合并在一起（称为“<a href="https://link.juejin.cn/?target=https%3A%2F%2Fthedailywtf.com%2Farticles%2FHappy_Merge_Day!" target="_blank" rel="nofollow noopener noreferrer" title="https://thedailywtf.com/articles/Happy_Merge_Day!" ref="nofollow noopener noreferrer">合并日</a>”），最终可能造成工作繁琐、耗时，而且需要手动完成。这是因为当一位独立工作的开发人员对应用进行更改时，有可能会与其他开发人员同时进行的更改发生冲突。如果每个开发人员都自定义自己的本地<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.redhat.com%2Fzh%2Ftopics%2Fmiddleware%2Fwhat-is-ide" target="_blank" rel="nofollow noopener noreferrer" title="https://www.redhat.com/zh/topics/middleware/what-is-ide" ref="nofollow noopener noreferrer">集成开发环境（IDE）</a>，而不是让团队就一个基于云的 IDE 达成一致，那么就会让问题更加雪上加霜。</p>
<p>持续集成（CI）可以帮助开发人员更加频繁地（有时甚至每天）将代码更改合并到共享分支或“主干”中。一旦开发人员对应用所做的更改被合并，系统就会通过自动构建应用并运行不同级别的自动化测试（通常是单元测试和集成测试）来验证这些更改，确保这些更改没有对应用造成破坏。这意味着测试内容涵盖了从类和函数到构成整个应用的不同模块。如果自动化测试发现新代码和现有代码之间存在冲突，CI 可以更加轻松地快速修复这些错误。</p>
<h4 data-id="heading-22">持续交付</h4>
<p>完成 CI 中构建及单元测试和集成测试的自动化流程后，持续交付可自动将已验证的代码发布到存储库。为了实现高效的持续交付流程，务必要确保 CI 已内置于开发管道。持续交付的目标是拥有一个可随时部署到生产环境的代码库。</p>
<p>在持续交付中，每个阶段（从代码更改的合并，到生产就绪型构建版本的交付）都涉及测试自动化和代码发布自动化。在流程结束时，运维团队可以快速、轻松地将应用部署到生产环境中。</p>
<h4 data-id="heading-23">持续部署</h4>
<p>对于一个成熟的 CI/CD 管道来说，最后的阶段是持续部署。作为持续交付——自动将生产就绪型构建版本发布到代码存储库——的延伸，持续部署可以自动将应用发布到生产环境。由于在生产之前的管道阶段没有手动门控，因此持续部署在很大程度上都得依赖精心设计的测试自动化。</p>
<p>实际上，持续部署意味着开发人员对应用的更改在编写后的几分钟内就能生效（假设它通过了自动化测试）。这更加便于持续接收和整合用户反馈。总而言之，所有这些 CI/CD 的关联步骤都有助于降低应用的部署风险，因此更便于以小件的方式（而非一次性）发布对应用的更改。不过，由于还需要编写自动化测试以适应 CI/CD 管道中的各种测试和发布阶段，因此前期投资还是会很大。</p>
<p><strong>个人小结：</strong></p>
<p>持续集成: 高频率的将代码合入主干，在合入之前触发单测和集成测试等去验证代码的改动，确保改动不会对应用造成破坏</p>
<p>持续交付：将代码合入到代码仓库。其目标是拥有一个可随时部署到生产环境的代码库</p>
<p>持续部署：在流程结束时，运维团队可以快速、轻松地将应用部署到生产环境中</p>
<hr>
<h3 data-id="heading-24">CI/CD 的关键概念</h3>
<p>来自官网的解释：</p>
<p>Pipelines are the top-level component of continuous integration, delivery, and deployment.</p>
<ul>
<li>Jobs, which define <em>what</em> to do. For example, jobs that compile or test code.</li>
<li>Stages, which define <em>when</em> to run the jobs. For example, stages that run tests after stages that compile the code.</li>
</ul>
<p>In general, pipelines are executed automatically and require no intervention once created. However, there are also times when you can manually interact with a pipeline.</p>
<p>译文：</p>
<p>Pipelines 是持续集成、交付和部署的顶级组件。</p>
<ul>
<li>Job ，定义<em>做什么</em>。 例如，编译或测试代码的作业。</li>
<li>Stages ，定义<em>何时</em>运行作业。 例如，在编译代码的阶段之后运行测试的阶段。</li>
</ul>
<p>一般来说，管道是自动执行的，一旦创建就不需要干预。 但是，有时您也可以手动与管道进行交互。</p>
<p><strong>理解</strong></p>
<p>Pipelines 是 CI/CD 的顶级组件，一个 pipeline 创建之后便会自动执行一系列的任务，<strong>无需人工干预</strong>。而在 pipeline 组件的下面又会有几个子组件 job 和 stages ；其中 stages 定义的是整个 pipeline 有的多少个阶段（环节），这些阶段（环节）的执行顺序是怎样的。而 job 则是每个环节中的具体任务【一个阶段（环节）中可以多个任务】，在定义任务的时候，我们要描述清楚这个任务什么情况下执行以及做什么事情。</p>
<p>接下来我们来理解下《第一个流水线》中的配置：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">stages:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">build</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">test</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">deploy</span>

<span class="hljs-attr">build_job:</span>
  <span class="hljs-attr">stage:</span> <span class="hljs-string">build</span> <span class="hljs-comment"># 指定job所属stage</span>
  <span class="hljs-attr">image:</span> <span class="hljs-string">centos:7</span> <span class="hljs-comment"># 指定执行job的所使用docker镜像</span>
  <span class="hljs-attr">tags:</span> 
    <span class="hljs-bullet">-</span> <span class="hljs-string">clf-centos-runner</span> <span class="hljs-comment"># 指定执行job的runner（即机器）</span>
  <span class="hljs-attr">script:</span> <span class="hljs-comment"># job执行时运行的脚本</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">echo</span> <span class="hljs-string">"build project"</span>

<span class="hljs-attr">test_job:</span>
  <span class="hljs-attr">stage:</span> <span class="hljs-string">test</span>
  <span class="hljs-attr">image:</span> <span class="hljs-string">centos:7</span>
  <span class="hljs-attr">tags:</span> 
    <span class="hljs-bullet">-</span> <span class="hljs-string">clf-centos-runner</span>
  <span class="hljs-attr">script:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">echo</span> <span class="hljs-string">"test project"</span>

<span class="hljs-attr">deploy_job:</span>
  <span class="hljs-attr">stage:</span> <span class="hljs-string">deploy</span>
  <span class="hljs-attr">image:</span> <span class="hljs-string">centos:7</span>
  <span class="hljs-attr">tags:</span> 
    <span class="hljs-bullet">-</span> <span class="hljs-string">clf-centos-runner</span>
  <span class="hljs-attr">script:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">echo</span> <span class="hljs-string">"deploy project"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上的配置便是一个完整 pipeline 的配置，那么 pipeline 的 stages 和 job 在这份配置中是如何体现的呢？</p>
<p>首先我们定义一个 pipeline 需要考虑这个 pipeline 有多少个阶段以及阶段的顺序是怎样的？以《第一个流水线》这个 pipeline 为例：</p>
<p>一共是三个阶段：build、test、deploy；这三个阶段合在一起描述了代码上库之后的需要进行的处理，分别是代码构建、测试、部署。</p>
<p>体现在配置上便是：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">stages:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">build</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">test</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">deploy</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>顺序则是数组每项的顺序：build（构建）=> test（测试）=> deploy（部署）。</p>
<p>在定义了每个阶段之后我们便需要进一步为每个阶段定义相应的 job（任务），以 build 阶段为例：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">stages:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">build</span>

<span class="hljs-attr">build_job:</span> <span class="hljs-comment"># 这是job的名称</span>
  <span class="hljs-attr">stage:</span> <span class="hljs-string">build</span> <span class="hljs-comment"># 指定job所属stage</span>
  <span class="hljs-attr">image:</span> <span class="hljs-string">centos:7</span> <span class="hljs-comment"># 指定执行job的所使用docker镜像</span>
  <span class="hljs-attr">tags:</span> 
    <span class="hljs-bullet">-</span> <span class="hljs-string">clf-centos-runner</span> <span class="hljs-comment"># 指定执行job的runner（即机器）</span>
  <span class="hljs-attr">script:</span> <span class="hljs-comment"># job 做什么</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">echo</span> <span class="hljs-string">"build project"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>前面提到我们需要给每个阶段定义相应的 job（任务）。那么 job 怎么对应到对应的阶段呢？通过 stage 关键字来对应的：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">stages:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">build</span>

<span class="hljs-attr">build_job:</span> <span class="hljs-comment"># 这是job的名称</span>
  <span class="hljs-attr">stage:</span> <span class="hljs-string">build</span> <span class="hljs-comment"># 指定job所属stage</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>stage 的值 build 这和我们前面定义的在 stages 数组下的其中一个值 build 对应，这便说明了 build_job 是 build 阶段的一个任务。</p>
<p>我们还提到了 job 是用来定义做什么的，那么 build_job 这个 job 做了什么呢？看看 script 关键字：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">stages:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">build</span>

<span class="hljs-attr">build_job:</span> <span class="hljs-comment"># 这是job的名称</span>
  <span class="hljs-attr">stage:</span> <span class="hljs-string">build</span> <span class="hljs-comment"># 指定job所属stage</span>
  <span class="hljs-attr">script:</span> <span class="hljs-comment"># job 做什么</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">echo</span> <span class="hljs-string">"build project"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>emmm，就简单了输入了下 “build project”。</p>
<p>在前面的配置中还出现了几个其他的配置，我们也顺便来看看其相应的的作用</p>
<p>tags：该字段指定执行该 job 使用的 runner（机器），我们指定的是前面注册的 runner，名称是 clf-centos-runner</p>
<p>image：我们的 job 的执行器（executor）使用的是 docker，这个字段指定的是 docker 所使用的镜像</p>
<p>到这里相信我们已经可以大致理解《第一个流水线》的配置了；<strong>整体如下：</strong></p>
<p>整个 pipeline 共有三个阶段 build => test => deploy；我们为每个阶段都定义了一个任务。每个任务都指定了执行任务所使用的机器（runner），并指定了执行器（executor）所使用的镜像 centos:7。目前每个 job 的执行任务都非常简单就是输出对应的文本。</p>
<p>稍微等等，似乎还少了点什么东西。为什么我们刚编写完 .gitlab-ci.yml 文件提交并推送之后便可以看到流水线呢？gitlab 是怎么知道这个时候要执行流水线的？是不是只有改 .gitlab-ci.yml 文件才会触发流水线？那我现在已经写好了以后不会再去修改 .gitlab-ci 文件了，流水线还能触发吗？</p>
<p>这便涉及到了流水线的触发机制，一般来说只要有代码推送都会触发流水线。当代码推送到远程的 GibLab 仓库时，GibLab 会看有没有流水线的配置文件 .gitlab-ci.yml，如果有的话便会触发流水线（当然我们可能在配置进行了特定的配置使得流水线不创建）。除了代码推送，我们还有其他的方式可以触发流水线。如：定时任务、手动触发、通过调用 GibLab 的 api 的方式触发等。</p>
<h2 data-id="heading-25">结语</h2>
<p>通过前面的内容我们已经创建了测试用的项目，安装好了相应的环境，并写了自己的第一个流水线也理解了 CI/CD 的基本概念。相信大家对 CI/CD 已经有了一个比较完整的认知了。后面的章节我们将进一深入 CI/CD 核心概念的学习。</p>
<h2 data-id="heading-26">参考链接</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.gitlab.com%2Fee%2Fci%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.gitlab.com/ee/ci/index.html" ref="nofollow noopener noreferrer">docs.gitlab.com/ee/ci/index…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.redhat.com%2Fzh%2Ftopics%2Fdevops%2Fwhat-is-ci-cd" target="_blank" rel="nofollow noopener noreferrer" title="https://www.redhat.com/zh/topics/devops/what-is-ci-cd" ref="nofollow noopener noreferrer">www.redhat.com/zh/topics/d…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2016%2F07%2Fyaml.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.ruanyifeng.com/blog/2016/07/yaml.html" ref="nofollow noopener noreferrer">www.ruanyifeng.com/blog/2016/0…</a></p></div>  
</div>
            