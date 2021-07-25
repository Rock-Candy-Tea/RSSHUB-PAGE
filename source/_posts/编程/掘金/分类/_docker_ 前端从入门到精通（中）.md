
---
title: '_docker_ 前端从入门到精通（中）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ddc718336de1482da5254c71efb22f1c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 24 Jul 2021 23:53:52 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ddc718336de1482da5254c71efb22f1c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ddc718336de1482da5254c71efb22f1c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://juejin.cn/post/6988513822818435080" target="_blank" title="https://juejin.cn/post/6988513822818435080">docker 前端从入门到精通(上)</a>中我们了解到了<code>docker</code>的基本常用命令，以及怎么使用<code>docker</code>，在下篇中着重讲解怎样使用进阶和高级使用。</p>
<h1 data-id="heading-0">docker 可视化工具</h1>
<p><code>Portainer</code> 是一个可视化的容器镜像的图形管理工具，利用Portainer可以轻松构建，管理和维护Docker环境。 而且完全免费，基于容器化的安装方式，方便高效部署。</p>
<pre><code class="hljs language-js copyable" lang="js"># 搜索
docker search portainer |head -n <span class="hljs-number">3</span>

#拉取镜像
docker pull docker.io/portainer/portainer

# 执行镜像获的容器
docker run -d -p <span class="hljs-number">8000</span>:<span class="hljs-number">8000</span> -p <span class="hljs-number">9000</span>:<span class="hljs-number">9000</span> --name=portainer --restart=always -v /<span class="hljs-keyword">var</span>/run/docker.sock:<span class="hljs-regexp">/var/</span>run/docker.sock -v portainer_data:<span class="hljs-regexp">/data portainer/</span>portainer

# 访问注册
<span class="hljs-attr">http</span>:<span class="hljs-comment">//localhost:9000/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dd35d81cdaf4e2c9cebb3cd82b474b2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">容器和数据卷</h1>
<p>目前理解到容器还有一个问题，就是如果整个容器被删除的话，所有的数据也会一起销毁掉，为了解决这个问题，可以使用数据卷把容器数据挂在的宿主机的磁盘上。</p>
<h3 data-id="heading-2">commit 镜像</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f4ef02ae1cc4be68ecd3e7084b78afb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>总结：<code>Docker</code> <strong>镜像都是只读的，当容器启动时，一个新的可写层被加到镜像的顶部。
这一层就是我们通常说的容器层，容器之下都是镜像层。</strong></p>
<p><code>docker commit</code> 命令除了学习之外，还有一些特殊的应用场合，比如被入侵后保存现场等。</p>
<p><code>docker commit</code> 命令，可以将容器的存储层保存下来成为镜像。换句话说，就是在原有镜像的基础上，再叠加上容器的存储层，并构成新的镜像。以后我们运行这个新镜像的时候，就会拥有原有容器最后的文件变化。</p>
<pre><code class="hljs language-js copyable" lang="js">docker commit  # 提交镜像 
docker commit -m=<span class="hljs-string">"提交者信息"</span> -a=<span class="hljs-string">"作者"</span>  容器id  镜像名称：[TAG]

# 根据上面的原理，我们在当前层提交了一层提交，完成整个镜像
[root@zhaosi ~]# docker commit -m=<span class="hljs-string">"cp weblist dir"</span> -a=<span class="hljs-string">"zhangsan"</span> c4b104964c2b zs_tomcat:<span class="hljs-number">1.0</span>
<span class="hljs-attr">sha256</span>:d81257471ca4836acba4ca2a5c160e92c75f99c12aa8494e69b397a45711ed0a
[root@zhaosi ~]# docker images 

REPOSITORY            TAG       IMAGE ID       CREATED          SIZE
zs_tomcat             <span class="hljs-number">1.0</span>       d81257471ca4   <span class="hljs-number">10</span> seconds ago   672MB
yachtomcat            <span class="hljs-number">1.0</span>       3ca80e740f23   <span class="hljs-number">2</span> weeks ago      672MB
nginx                 latest    4cdc5dd7eaad   <span class="hljs-number">2</span> weeks ago      133MB
tomcat                latest    36ef696ea43d   <span class="hljs-number">3</span> weeks ago      667MB
mysql                 latest    5c62e459e087   <span class="hljs-number">4</span> weeks ago      556MB
portainer/portainer   latest    580c0e4e98b0   <span class="hljs-number">4</span> months ago     <span class="hljs-number">79.</span>1MB
centos                latest    300e315adb2f   <span class="hljs-number">7</span> months ago     209MB
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c119a309a4c446e2990787542864544f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>【警告】</strong> <code>docker commit</code> 意味着所有对镜像的操作都是黑箱操作，生成的镜像也被称为 黑箱镜像，换句话说，就是除了制作镜像的人知道执行过什么命令、怎么生成的镜像，别人根本无从得知。</p>
<h3 data-id="heading-3">dockfile</h3>
<p>从刚才的 <code>docker commit</code> 的学习中，我们可以了解到，镜像的定制实际上就是定制每一层所添加的配置、文件。如果我们可以把每一层修改、安装、构建、操作的命令都写入一个脚本，用这个脚本来构建、定制镜像，那么之前提及的无法重复的问题、镜像构建透明性的问题、体积的问题就都会解决。这个脚本就是 <code>Dockerfile</code>。</p>
<p><code>Dockerfile</code> 是一个文本文件，其内包含了一条条的 指令<code>(Instruction)</code>，每一条指令构建一层，因此每一条指令的内容，就是描述该层应当如何构建。</p>
<p>之前说过，<code>Dockerfile</code> 中每一个指令都会建立一层，<code>RUN</code>也不例外。每一个 <code>RUN</code> 的行为，就和刚才我们手工建立镜像的过程一样：新建立一层，在其上执行这些命令，执行结束后，<code>commit </code>这一层的修改，构成新的镜像。</p>
<h4 data-id="heading-4">案例1：使用nginx 简单构建一个镜像</h4>
<pre><code class="hljs language-js copyable" lang="js">touch mynginx && cd mynginx && touch Dockerfile

# vi写入以下爱内容
FROM nginx
RUN echo <span class="hljs-string">'<h1>Hello, Docker!</h1>'</span> > <span class="hljs-regexp">/usr/</span>share/nginx/html/index.html

# 在当前路径下，执行构建
# 也可以指定路径，不用移动到当前的路径
# docker build -f /path/to/a/Dockerfile
docker build -t nginx:v3 .


# 查看构建
docker images

REPOSITORY            TAG       IMAGE ID       CREATED         SIZE

nginx                 v4        1b03f171e7d4   <span class="hljs-number">7</span> minutes ago   133MB
zs_tomcat             <span class="hljs-number">1.0</span>       d81257471ca4   <span class="hljs-number">4</span> hours ago     672MB
yachtomcat            <span class="hljs-number">1.0</span>       3ca80e740f23   <span class="hljs-number">2</span> weeks ago     672MB
nginx                 latest    4cdc5dd7eaad   <span class="hljs-number">2</span> weeks ago     133MB
tomcat                latest    36ef696ea43d   <span class="hljs-number">3</span> weeks ago     667MB
mysql                 latest    5c62e459e087   <span class="hljs-number">4</span> weeks ago     556MB
portainer/portainer   latest    580c0e4e98b0   <span class="hljs-number">4</span> months ago    <span class="hljs-number">79.</span>1MB
centos                latest    300e315adb2f   <span class="hljs-number">7</span> months ago    209MB
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">案例2：构建centos上传docker-pub</h4>
<p>实现两个功能：可以使用 <code>vim</code> 和 <code>ifconfig</code> 两个功能，完整实现<code>dockerfile</code>并且发布到<code>docker-pub</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"># <span class="hljs-number">1</span> 建立文件
mkdir -p mycentos && cd mycentos && touch mycentosDockfile-centos

# <span class="hljs-number">2</span> 编辑 vi mycentosDockfile-centos
FROM centos
MAINTAINER zhangsan<qiuyanlong2016@gmail.com>


ENV MYPATH /usr/local
WORKDIR $MYPATH

RUN yum -y install vim 
RUN yum -y install net-tools

EXPOSE <span class="hljs-number">8080</span>

CMD echo $MYPATH
CMD echo <span class="hljs-string">"================end================="</span>
CMD /bin/bash

# <span class="hljs-number">3</span>: 构建 zhangsan 是docker-pub账号
docker build -f ./mycentosDockfile-centos -t zhangsan/dircentos:<span class="hljs-number">1.0</span> .

# <span class="hljs-number">4</span>：如果<span class="hljs-number">3</span>步忘记添加在即的账号作为spacename 则需要单独打一个tag 
docker tag  dircentos:<span class="hljs-number">1.0</span>  zhangsan/dircentos:<span class="hljs-number">1.0</span>

# <span class="hljs-number">5</span>: 登陆
docker login -u zhangsan

# <span class="hljs-number">6</span>: push
docker push zhangsan/dircentos:<span class="hljs-number">1.0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般<code>dockfile</code>包含<strong>基础镜像信息</strong>、<strong>维护者信息</strong>、<strong>镜像操作指令</strong>和<strong>容器启动时执行指令</strong>。</p>
<p><code>docker</code> 以从上到下的顺序运行<code>Dockerfile</code>的指令。为了指定基本映像，第一条指令必须是<code>FROM</code>。一个声明以＃字符开头则被视为注释。可以在<code>Docker</code>文件中使用<code>RUN</code>，<code>CMD</code>，<code>FROM</code>，<code>EXPOSE</code>，<code>ENV</code>等指令。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c19fa2edfb7a4448a72a054dd970b3fa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9348fc408e6c4d2ea2961240d333dba2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">卷挂载使用</h3>
<pre><code class="hljs language-js copyable" lang="js"> docker run -it -v 主机目录:容器目录 
 
 # 把容器的data挂在到宿主的home下面
 docker run -it -v /home/data:<span class="hljs-regexp">/home centos /</span>bin/bash 
 
 #查看这个容器的所有详细信息
 docker inspect 容器的ID
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e06318a3fa44478bd44d89ed310a4aa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">具名挂载和匿名挂载</h3>
<p><code>-v</code> 容器内路径 不写宿主机器的路径就是<strong>匿名挂载</strong></p>
<pre><code class="hljs language-js copyable" lang="js"># 匿名挂载
docker run -d -p  --name nginx_01 -v /etc/nginx nginx 

# 查看挂在卷列表
docker volume ls

local     0bd0439abb6511c914de41975ca4f9d2e07eaab969d92981277092d4673bd6d7
local     0fe72108880078fa40e4060e8695a56e1518402069a6c0f559092ad9b5aadbb7
local     8f4456ba8f2288e680fdc466b4b35853ee134700e8d21d79911e91163a6e3c60
local     08f05b86ac17558c8b32b36ff7ac01907e115e4c6e9c0bba0d5c91b1dc5d2cc3

# 查看某个容器卷挂载具体情况
docker volume inspect 容器id

# 具名挂载
docker run -d -P  --name nginx_01 -v  test-nginx : <span class="hljs-regexp">/etc/</span>nginx nginx 

# 再次查看
docker volume ls

local     0bd0439abb6511c914de41975ca4f9d2e07eaab969d92981277092d4673bd6d7
local     0fe72108880078fa40e4060e8695a56e1518402069a6c0f559092ad9b5aadbb7
local     8f4456ba8f2288e680fdc466b4b35853ee134700e8d21d79911e91163a6e3c60
local     08f05b86ac17558c8b32b36ff7ac01907e115e4c6e9c0bba0d5c91b1dc5d2cc3
local     test-nginx
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/231cd57e47904186adc6647fa2b0b566~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">练习：挂在mysql 数据</h3>
<pre><code class="hljs language-js copyable" lang="js"># -p 端口映射
# -v 卷挂在
# -e 环境配置
# --name 容器名称

docker run -d 
-p <span class="hljs-number">3301</span>:<span class="hljs-number">3306</span>\ 
-v /home/mysql/conf:<span class="hljs-regexp">/etc/my</span>sql/conf.d\ 
-v /home/mysql/data:<span class="hljs-regexp">/var/</span>lib/mysql\ 
-e MYSQL_ROOT_PASSWORD=<span class="hljs-number">123456</span>\ 
--name mysql_01 mysql

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76602db15320479cbe6f51f48112f830~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>网络相关的 <code>docker componse</code> 和 <code>docker swam</code>集群等相关见[docker] 前端从入门到精通（下）。</p>
</blockquote>
<h1 data-id="heading-9">参考文章</h1>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fthe-undeveloped-procedural-ape%2Farticles%2F14203848.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/the-undeveloped-procedural-ape/articles/14203848.html" ref="nofollow noopener noreferrer">Portainer 点击 connect 报错：Failure Cannot connect to the Docker daemon at unix:///var/run/docker.sock.</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fyeasy.gitbook.io%2Fdocker_practice%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://yeasy.gitbook.io/docker_practice/" ref="nofollow noopener noreferrer">yeasy.gitbook.io/docker_prac…</a></p>
</li>
</ul></div>  
</div>
            