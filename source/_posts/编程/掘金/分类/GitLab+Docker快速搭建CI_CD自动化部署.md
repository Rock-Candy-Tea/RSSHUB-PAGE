
---
title: 'GitLab+Docker快速搭建CI_CD自动化部署'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4aa481b1a84c429c99023e9b21379ee5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 29 May 2021 22:52:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4aa481b1a84c429c99023e9b21379ee5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">什么是持续集成(Continuous integration)?</h2>
<h3 data-id="heading-1">CI</h3>
<p>在持续集成环境中，开发人员将会频繁得提交代码到主干。这些新提交在最终合并到主线之前，都需要通过编译和自动化测试进行验证。这样做是基于之前持续集成过程中很重视自动化测试验证结果，以保障所有得提交在合并主干之后得质量问题，对可能出现得一些问题进行预计。</p>
<h3 data-id="heading-2">持续交付(Continuous Delivery)</h3>
<p>持续交付就是讲我们得应用发布出去的过程。这个过程可以确保我们尽量可能快的实现交付。这就意味着除了自动化测试，我们还需要有自动化的发布流，以及通过一个按键就可以随时随地实现应用的部署上线</p>
<p>通过持续交付，可以决定每天，每周，每两周发布一次，这完全可以根据自己的业务进行设置。</p>
<p>但是，如果你真的希望体验持续交付的优势，就需要先进行小批量发布，尽快部署到生产线，以便在出现问题时方便进行故障排除。</p>
<h3 data-id="heading-3">持续部署(Continuous Deployment)</h3>
<p>如果我们想更加深入一步的话，就是持续部署了。通过这个方式，任何修改通过了所有已有的工作流就会直接和客户见面。没有人为干预(没有一键部署按钮)，只有当一个修改在工作流中构建失败才能阻止它部署到产品线。</p>
<p>持续部署是一个很优秀的方式，可以加速与客户的反馈循环，但是会给团队带来压力，因为不再有"发布日"了。开发人员可以专注于构建软件，他们看到他们修改在他们完成工作后几分钟就上线了。基本上，当开发人员在主分支合并一个提交时，这个分支将被构建，测试，如果一切顺利，则部署到生产环境中。</p>
<h3 data-id="heading-4">持续集成需求</h3>
<ul>
<li>持续集成是通过平台串联各个开发环节，实现和沉淀工作自动化的方法。</li>
<li>线上代码和代码仓库不同步，影响迭代和团队协作。</li>
<li>静态资源发布依赖人工，浪费开发人力。</li>
<li>缺少自动化测试，产品质量得不到保障</li>
<li>文案简单修改上线，需要技术介入。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4aa481b1a84c429c99023e9b21379ee5~tplv-k3u1fbpfcp-watermark.image" alt="1609680100306.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">Gitlab</h2>
<p>Gitlab是一个开源的版本管理系统，实现一个自托管的Git项目仓库，可通过Web界面进行访问公开的或者私人项目。它拥有与Github类似的功能，能够浏览源码，管理缺陷和注释，可以管理团队对仓库的访问，它非常易于浏览提交的版本并提供一个文件历史库。团队成员可以利用内置的简单的聊天程序进行交流。它还提供一个代码片段收集功能可以实现代码复用。</p>
<p>GitLab对于系统性能有要求，所以我们需要将克隆出来的虚拟机的内存提高到至少2G以上。</p>
<h3 data-id="heading-6">Gitlab安装</h3>
<p>方法一:</p>
<pre><code class="hljs language-js copyable" lang="js">sudo docker run --detach \
  --hostname localhost \
  --publish <span class="hljs-number">443</span>:<span class="hljs-number">443</span> --publish <span class="hljs-number">8084</span>:<span class="hljs-number">8084</span> --publish <span class="hljs-number">222</span>:<span class="hljs-number">22</span> \
  --name gitlab \
  --restart always \
  --volume /home/docker/gitlab/config:<span class="hljs-regexp">/etc/gi</span>tlab \
  --volume /home/docker/gitlab/logs:<span class="hljs-regexp">/var/</span>log/gitlab \
  --volume /home/docker/gitlab/data:<span class="hljs-regexp">/var/</span>opt/gitlab \
  gitlab/gitlab-ce:latest
<span class="copy-code-btn">复制代码</span></code></pre>
<p>localhost:主机名,即虚拟机的ip,8084可以自己定义端口号,restart重启方式,volume目录挂载,gitlab/gitlab-ce:latest镜像名。</p>
<p>方法二:</p>
<pre><code class="hljs language-js copyable" lang="js">docker pull twang2218/gitlab-ce-zh
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等待其拉取，然后在 /home下新建docker目录，再在其下新建gitlab目录，进入gitlab目录，在当前目录下新建docker-compose.yml配置文件，编写内容如下。</p>
<pre><code class="hljs language-js copyable" lang="js">version: <span class="hljs-string">'3'</span>
<span class="hljs-attr">services</span>:
   web:
     image: <span class="hljs-string">'twang2218/gitlab-ce-zh'</span>   #gitlab镜像
     <span class="hljs-attr">restart</span>: always
     <span class="hljs-attr">privileged</span>: <span class="hljs-literal">true</span>  #权限
     <span class="hljs-attr">hostname</span>: <span class="hljs-string">''</span>       #主机名,即虚拟机的ip
     <span class="hljs-attr">environment</span>:
        TZ: <span class="hljs-string">'Asia/Shanghai'</span>
        <span class="hljs-attr">GITLAB_OMNIBUS_CONFIG</span>: |
            external_url <span class="hljs-string">''</span> #主机名,即虚拟机的ip
            gitlab_rails[<span class="hljs-string">'gitlab_shell_ssh_port'</span>] = <span class="hljs-number">2222</span>
            unicorn[<span class="hljs-string">'port'</span>] = <span class="hljs-number">8888</span>
            nginx[<span class="hljs-string">'listen_port'</span>] = <span class="hljs-number">8084</span>
     <span class="hljs-attr">ports</span>:
        - <span class="hljs-string">'8084:8084'</span>
        - <span class="hljs-string">'8443:443'</span>
        - <span class="hljs-string">'2222:22'</span>
     <span class="hljs-attr">volumes</span>:
        - <span class="hljs-string">'./config:/etc/gitlab'</span>
        - <span class="hljs-string">'./logs:/var/log/gitlab'</span>
        - <span class="hljs-string">'./data:/var/opt/gitlab'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行<code>docker-compose up</code>，然后进入等待时间，等它下好了去通过自己设置的虚拟机的ip和端口号访问。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55850e0afd5d4bf7b737502dff0d8e32~tplv-k3u1fbpfcp-watermark.image" alt="1622287438766.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果安装过程中有报错权限问题，那么加上<code>privileged: true</code></p>
<p>查看方式:</p>
<pre><code class="hljs language-js copyable" lang="js">root@iZm5ebvlfc3n55vzckl9ifZ:# docker ps
CONTAINER ID        IMAGE                         COMMAND                  CREATED             STATUS                 PORTS                                                                         NAMES
ddc7d0e214ef        twang2218/gitlab-ce-zh        <span class="hljs-string">"/assets/wrapper"</span>        <span class="hljs-number">30</span> hours ago        Up <span class="hljs-number">6</span> hours (healthy)   <span class="hljs-number">80</span>/tcp, <span class="hljs-number">0.0</span><span class="hljs-number">.0</span><span class="hljs-number">.0</span>:<span class="hljs-number">8084</span>-><span class="hljs-number">8084</span>/tcp, <span class="hljs-number">0.0</span><span class="hljs-number">.0</span><span class="hljs-number">.0</span>:<span class="hljs-number">2222</span>-><span class="hljs-number">22</span>/tcp, <span class="hljs-number">0.0</span><span class="hljs-number">.0</span><span class="hljs-number">.0</span>:<span class="hljs-number">8443</span>-><span class="hljs-number">443</span>/tcp   gitlab_web_1

<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过虚拟主机的ip+端口访问，此时需要设置管理员密码，账号为root，密码最少为8位。</p>
<p>登录成功后，如下:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22cc81a6ecb044058e312365627f0ef8~tplv-k3u1fbpfcp-watermark.image" alt="1622288085865.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">项目创建</h3>
<p>点击 <code>+</code> 号 --> <code>新建项目</code></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b65fd8ad83c4f3f8e6983c13728e206~tplv-k3u1fbpfcp-watermark.image" alt="7986413-d97bf80a83e45895.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>输入项目名称及描述信息，设置可见等级：私有，内部，公开。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3568b97352d4e058b1929a4f4507ab8~tplv-k3u1fbpfcp-watermark.image" alt="1622288467482.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">初始化项目</h4>
<p>我们可以选择通过增加一个README的方式来初始化项目,如下:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f53bc637eec34d5da59dca4b5b9a874a~tplv-k3u1fbpfcp-watermark.image" alt="1622288978567.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e02bc270715744fbac0962cba5597afa~tplv-k3u1fbpfcp-watermark.image" alt="7986413-38bb77b9e693be70.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建项目的时候有一个问题，在自己最开始定义了端口号，创建项目的时候会没有端口号，这时候clone项目的时候会访问不了，这时候我们在最开始安装定义目录里面config目录下找到<code>gitlab.rb</code>,编辑它，搜索<code>external_url</code>，没有就添加<code>external_url:主机ip+端口号</code>，有就修改就行了。这时候我们就可以去克隆项目了。当然我们也可以通过下面方法去把项目推送到gitlab上面:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12af7ed1a5054b1680c365ea1b610431~tplv-k3u1fbpfcp-watermark.image" alt="1622298003116.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2156b28e85d4cd5b18306d871c1a294~tplv-k3u1fbpfcp-watermark.image" alt="1622289009680.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">Gitlab-Runner</h2>
<h3 data-id="heading-10">安装</h3>
<pre><code class="hljs language-js copyable" lang="js">sudo docker run -d --name gitlab-runner --restart always \
  -v /home/gitlab-runner/config:<span class="hljs-regexp">/etc/gi</span>tlab-runner \
  -v /<span class="hljs-keyword">var</span>/run/docker.sock:<span class="hljs-regexp">/var/</span>run/docker.sock \
  gitlab/gitlab-runner:latest
<span class="copy-code-btn">复制代码</span></code></pre>
<p>映射<code>/var/run/docker.sock</code>这个文件是为了让容器可以通过<code>/var/run/docker.sock</code>与<code>Docker</code>守护进程通信，管理其他<code>Docker</code>容器
<code>-v /home/gitlab-runner/config:/etc/gitlab-runner</code>是将runner的配置文件映射到宿主机<code>/home/gitlab-runner/config</code>方便调整和查看配置</p>
<p>安装完成我们需要去注册Gitlab-Runner。</p>
<p>运行<code>docker ps</code>查看:</p>
<pre><code class="hljs language-js copyable" lang="js">root@iZm5ebvlfc3n55vzckl9ifZ:<span class="hljs-regexp">/home/</span>docker/gitlab# docker ps
CONTAINER ID        IMAGE                         COMMAND                  CREATED             STATUS                 PORTS                                                                         NAMES
ed6c7a038263        gitlab/gitlab-runner:latest   <span class="hljs-string">"/usr/bin/dumb-init …"</span>   <span class="hljs-number">24</span> hours ago        Up <span class="hljs-number">24</span> hours                                                                                          gitlab-runner
ddc7d0e214ef        twang2218/gitlab-ce-zh        <span class="hljs-string">"/assets/wrapper"</span>        <span class="hljs-number">30</span> hours ago        Up <span class="hljs-number">6</span> hours (healthy)   <span class="hljs-number">80</span>/tcp, <span class="hljs-number">0.0</span><span class="hljs-number">.0</span><span class="hljs-number">.0</span>:<span class="hljs-number">8084</span>-><span class="hljs-number">8084</span>/tcp, <span class="hljs-number">0.0</span><span class="hljs-number">.0</span><span class="hljs-number">.0</span>:<span class="hljs-number">2222</span>-><span class="hljs-number">22</span>/tcp, <span class="hljs-number">0.0</span><span class="hljs-number">.0</span><span class="hljs-number">.0</span>:<span class="hljs-number">8443</span>-><span class="hljs-number">443</span>/tcp   gitlab_web_1

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">注册</h3>
<pre><code class="hljs language-js copyable" lang="js">docker run --rm -v /srv/gitlab-runner/config:<span class="hljs-regexp">/etc/gi</span>tlab-runner gitlab/gitlab-runner register \
  --non-interactive \
  --executor <span class="hljs-string">"docker"</span> \
  --docker-image alpine:latest \
  --url <span class="hljs-string">""</span> \
  --registration-token <span class="hljs-string">""</span> \
  --description <span class="hljs-string">"first-register-runner"</span> \
  --tag-list <span class="hljs-string">"vue3-app"</span> \
  --run-untagged=<span class="hljs-string">"true"</span> \
  --locked=<span class="hljs-string">"false"</span> \
  --access-level=<span class="hljs-string">"not_protected"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注册需要输出url，token，描述，tag，执行器等，url和token怎么来的呢?在设置->CI/CD->Runner里面，我这里面注册了一个专用的和共享的Runner，正常情况我们用专用Runner就可以了。共享版Runner是登录root账户在头部小扳手图片里面的Runner得到url和token，然后去注册。这里面的tag值会在编写<code>.gitlab-ci.yml</code>时用到。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48aa4207085340219d226ba9a035c783~tplv-k3u1fbpfcp-watermark.image" alt="1622298841818.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">运行流水线</h3>
<p>在项目根目录里面创建一个<code>.gitlab-ci.yml</code>，编写代码如下:</p>
<pre><code class="hljs language-js copyable" lang="js">image: node:alpine

<span class="hljs-attr">stages</span>: # 分段
  - install
  - eslint
  - build
  - deploy

<span class="hljs-attr">cache</span>: # 缓存
  <span class="hljs-attr">paths</span>:
    - node_modules

<span class="hljs-attr">job_install</span>:
  tags:
    - vue3-app
  <span class="hljs-attr">stage</span>: install
  <span class="hljs-attr">script</span>:
    - npm install

<span class="hljs-attr">job_build</span>:
  tags:
    - vue3-app
  <span class="hljs-attr">stage</span>: build
  <span class="hljs-attr">script</span>:
    - npm run build
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数说明:</p>
<ul>
<li>stages:pipeline的阶段列表，定义整个pipeline阶段</li>
<li>stage:定义某个job的所在阶段</li>
<li>image:指定一个基础Docker进行作为基础运行环境，比如:node,python,java</li>
<li>tags:用于指定Runner，tags的取值范围是在该项目可惜可见的runner tags中，也就是前面我们设置的那个tag</li>
<li>only/except:知道当前任务条件</li>
<li>when:实现在发生故障时仍能运行的作业</li>
<li>cache:讲当前工作环境目录中的一些文件，文件夹存储起来，用于在各个任务初始化的时候恢复</li>
<li>environment:指定部署相关任务的环境，并非真实环境，是对要部署到某环境的任务的归类。方便在gitlab上聚合以便进行回滚和重新部署操作</li>
<li>artifacts:保留文档。在每次 job 之前runner会清除未被 git 跟踪的文件。为了让编译或其他操作后的产物可以留存到后续使用，添加该参数并设置保留的目录，保留时间等。被保留的文件将被上传到gitlab以备后续使用。</li>
<li>dependencies:任务依赖。指定job的前置job。添加该参数后，可以获取到前置job的artifacts。注意如果前置 job 执行失败，导致没能生成artifacts，则 job 也会直接失败。</li>
</ul>
<p>编写好上面代码后推送到gitlab后就会自己执行里面的语句:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b9c8bdab36745eea02ff8bcaf9feefd~tplv-k3u1fbpfcp-watermark.image" alt="1622299460821.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">部署</h3>
<p>在项目中创建一个<code>Dockerfile</code>，代码如下:</p>
<pre><code class="hljs language-js copyable" lang="js">FROM node:latest <span class="hljs-keyword">as</span> builder
WORKDIR /app
COPY  package.json
RUN npm install --registry=http:<span class="hljs-comment">//registry.npm.taobao.org</span>
COPY ..
RUN npm run build

FROM nginx:latest
COPY --<span class="hljs-keyword">from</span>=builder /app/dist /usr/share/nginx/html
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>.gitlab-ci.yml</code>修改如下:</p>
<pre><code class="hljs language-js copyable" lang="js">image: node:alpine

<span class="hljs-attr">stages</span>: # 分段
  - install
  - eslint
  - build
  - deploy

<span class="hljs-attr">cache</span>: # 缓存
  <span class="hljs-attr">paths</span>:
    - node_modules

<span class="hljs-attr">job_install</span>:
  tags:
    - vue3-app
  <span class="hljs-attr">stage</span>: install
  <span class="hljs-attr">script</span>:
    - npm install

<span class="hljs-attr">job_build</span>:
  tags:
    - vue3-app
  <span class="hljs-attr">stage</span>: build
  <span class="hljs-attr">script</span>:
    - npm run build

<span class="hljs-attr">job_deploy</span>:
    image: docker
    <span class="hljs-attr">stage</span>: deploy
    <span class="hljs-attr">script</span>:
      - docker build -t appimages
      - <span class="hljs-keyword">if</span> [ $(docker ps -aq --filter name=app-container) ]; then docker rm -f app-container;fi
      - docker run -d -p <span class="hljs-number">8082</span>:<span class="hljs-number">80</span> --name app-container appimages
<span class="copy-code-btn">复制代码</span></code></pre>
<p>if语句判断:使用docker命令去搜索docker容器里面是否有一个name为<code>app-container</code>的容器，如果有就销毁掉,销毁掉是为了使用新的容器重新运行。</p>
<p>这里<code>image:docker</code>不写的话会报错:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce3239e40f114319b442cadf14b35e8d~tplv-k3u1fbpfcp-watermark.image" alt="1622301667720.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码推送后，流水线工作，到第三步就会出下报错:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30bba06f67824e93b35a66d10b7c6ae2~tplv-k3u1fbpfcp-watermark.image" alt="1622301866992.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e636e14a0b24187a7fe19c137f1210b~tplv-k3u1fbpfcp-watermark.image" alt="1622301814039.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>解决办法,在runner配置文件中配置docker命令:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"/usr/bin/docker:/usr/bin/docker"</span>, <span class="hljs-string">"/var/run/docker.sock:/var/run/docker.sock"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在gitlab-runner->config-vim config.toml，找到注册runner所对应的token，在volumes数组里面加入上面命令:</p>
<pre><code class="hljs language-js copyable" lang="js">concurrent = <span class="hljs-number">1</span>
check_interval = <span class="hljs-number">0</span>

[session_server]
  session_timeout = <span class="hljs-number">1800</span>
  
[[runners]]
  name = <span class="hljs-string">"first-register-runner"</span>
  url = <span class="hljs-string">""</span>
  token = <span class="hljs-string">""</span>
  executor = <span class="hljs-string">"docker"</span>
  [runners.custom_build_dir]
  [runners.cache]
    [runners.cache.s3]
    [runners.cache.gcs]
    [runners.cache.azure]
  [runners.docker]
    tls_verify = <span class="hljs-literal">false</span>
    image = <span class="hljs-string">"alpine:latest"</span>
    privileged = <span class="hljs-literal">false</span>
    disable_entrypoint_overwrite = <span class="hljs-literal">false</span>
    oom_kill_disable = <span class="hljs-literal">false</span>
    disable_cache = <span class="hljs-literal">false</span>
    volumes = [<span class="hljs-string">"/cache"</span>,<span class="hljs-string">"/usr/bin/docker:/usr/bin/docker"</span>, <span class="hljs-string">"/var/run/docker.sock:/var/run/docker.sock"</span>]
    shm_size = <span class="hljs-number">0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在去重新运行失败的Jobs，这时候发现成功了:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cdc58b9c2e7a4c85a7064bb2be7d7d6c~tplv-k3u1fbpfcp-watermark.image" alt="1622302501014.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后通过前面注册的端口号去访问，可以正常访问项目。</p></div>  
</div>
            