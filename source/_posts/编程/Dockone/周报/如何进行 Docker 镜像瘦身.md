
---
title: '如何进行 Docker 镜像瘦身'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/766e4e43592badd4ef804b5b51f54d91.png'
author: Dockone
comments: false
date: 2021-09-06 11:06:21
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/766e4e43592badd4ef804b5b51f54d91.png'
---

<div>   
<br><h3>简介</h3>容器镜像类似于虚拟机镜像，封装了程序的运行环境，保证了运行环境的一致性，使得我们可以一次创建任意场景部署运行。镜像构建的方式有两种，一种是通过 docker build 执行 Dockerfile 里的指令来构建镜像，另一种是通过 docker commit 将存在的容器打包成镜像，通常我们都是使用第一种方式来构建容器镜像。  <br>
<br>在构建 Docker 容器时，我们一般希望尽量减小镜像，以便加快镜像的分发；但是不恰当的镜像构建方式，很容易导致镜像过大，造成带宽和磁盘资源浪费，尤其是遇到 DaemonSet 这种需要在每台机器上拉取镜像的服务，会造成大量资源浪费；而且镜像过大还会影响服务的启动速度，尤其是处理紧急线上镜像变更时，直接影响变更的速度。如果不是刻意控制镜像大小、注意镜像瘦身，一般的业务系统中可能 90% 以上的大镜像都存在镜像空间浪费的现象（不信可以尝试检测看看）。因此我们非常有必要了解镜像瘦身方法，减小容器镜像。<br>
<h3>如何判断镜像是否需要瘦身</h3>通常，我们可能都是在容器镜像过大，明显影响到镜像上传/拉取速度时，才会考虑到分析镜像，尝试镜像瘦身。此时采用的多是 docker image history 等 Docker 自带的镜像分析命令，以查看镜像构建历史、镜像大小在各层的分布等。然后根据经验判断是否存在空间浪费，但是这种判断方式起点较高、没有量化，不方便自动化判断。当前，社区中也有很多镜像分析工具，其中比较流行的 <a href="http://weekly.dockone.io/_https://github.com/wagoodman/dive_">dive</a> 分析工具，就可以量化给出容器镜像有效率、镜像空间浪费率等指标，如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/766e4e43592badd4ef804b5b51f54d91.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/766e4e43592badd4ef804b5b51f54d91.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
采用 dive 对一个 MySQL 镜像进行效率分析，发现镜像有效率只有 41%，镜像空间浪费率高达 59%，显然需要瘦身。<br>
<h3>如何进行镜像瘦身</h3>当判断一个镜像需要瘦身后，我们就需要知道如何进行镜像瘦身，下面将结合具体案例讲解一些典型的镜像瘦身方法。<br><br>
<h4>多阶段构建</h4>所谓多阶段构建，实际上是允许在一个 Dockerfile 中出现多个 FROM 指令。最后生成的镜像，以最后一条 FROM 构建阶段为准，之前的 FROM 构建阶段会被抛弃。通过多阶段构建，后一个阶段的构建过程可以直接利用前一阶段的构建缓存，有效降低镜像大小。一个典型的场景是将编译环境和运行环境分离，以一个 Go 项目镜像构建过程为例：<br><br>
<pre class="prettyprint"># Go 语言编译环境基础镜像<br>
FROM golang:1.16-alpine<br>
<br>
# 拷贝源码到镜像<br>
COPY server.go /build/<br>
<br>
# 指定工作目录<br>
WORKDIR /build<br>
<br>
# 编译镜像时，运行 go build 编译生成 server 程序<br>
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 GOARM=6 go build -ldflags '-w -s' -o server<br>
<br>
# 指定容器运行时入口程序<br>
ENTRYPOINT ["/build/server"]<br>
</pre><br>
这种传统的构建方式有以下缺点：<br>
<ul><li>基础镜像为支持编译环境，包含大量 Go 语言的工具/库，而运行时并不需要。</li><li>COPY 源码，增加了镜像分层，同时有源码泄漏风险。</li></ul><br>
<br>采用多阶段构建方式，可以将上述传统的构建方式修改如下：<br>
<pre class="prettyprint">## 1 编译构建阶段<br>
#  Go 语言编译环境基础镜像<br>
FROM golang:1.16-alpine AS build<br>
<br>
# 拷贝源码到镜像<br>
COPY server.go /build/<br>
<br>
# 指定工作目录<br>
WORKDIR /build<br>
<br>
# 编译镜像时，运行 go build 编译生成 server 程序<br>
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 GOARM=6 go build -ldflags '-w -s' -o server<br>
<br>
## 2 运行构建阶段<br>
#  采用更小的运行时基础镜像<br>
FROM scratch<br>
<br>
# 从编译阶段仅拷贝所需的编译结果到当前镜像中<br>
COPY --from=build /build/server /build/server<br>
<br>
# 指定容器运行时入口程序<br>
ENTRYPOINT ["/build/server"]<br>
</pre><br>
可以看到，使用多阶段构建，可以获取如下好处：<br>
<ul><li>最终镜像只关心运行时，采用了更小的基础镜像。</li><li>直接拷贝上一个编译阶段的编译结果，减少了镜像分层，还避免了源码泄漏。</li></ul><br>
<br><h4>减少镜像分层</h4>镜像的层就像 Git 的提交（commit）一样，用于保存镜像的当前版本与上一版本之间的差异，但是镜像层会占用空间，拥有的层越多，最终的镜像就越大。在构建镜像时，RUN，ADD，COPY 指令对应的层会增加镜像大小，其他命令并不会增加最终的镜像大小。下面以实际工作中的一个案例讲解如何减少镜像分层，以减小镜像大小。<br>
<br><strong>背景</strong><br>
<br>测试项目 MySQL 镜像时，遇到了容器创建比较慢的情况，我们发现主要是因为容器镜像较大，拉取镜像时间较长，所以就打算看看 MySQL 镜像为什么这么大，是否可以减小容器镜像。  <br>
<br><strong>镜像大小分析</strong><br>
<br>通过 docker image history 查看镜像构建历史及各层大小：<strong>镜像大小 - 2.9GB</strong>。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/77a6d36756fd3b381e334c854d336a5a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/77a6d36756fd3b381e334c854d336a5a.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
其相应 Dockerfile 如下：<br>
<pre class="prettyprint">##<br>
## MySQL 5.7<br>
<h1>#</h1>FROM centos:7<br>
...<br>
<br>
RUN yum -y install crontabs<br>
RUN groupadd -g $&#123;MY_GID&#125; -r $&#123;MY_GROUP&#125; && \<br>
adduser $&#123;MY_USER&#125; -u $&#123;MY_UID&#125; -M -s /sbin/nologin -g $&#123;MY_GROUP&#125;<br>
<br>
# RUN wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.29-1.el7.x86_64.rpm-bundle.tar<br>
COPY mysql-5.7.29-1.el7.x86_64.rpm-bundle.tar  /<br>
RUN tar -vxf /mysql-5.7.29-1.el7.x86_64.rpm-bundle.tar<br>
RUN rm /mysql-5.7.29-1.el7.x86_64.rpm-bundle.tar<br>
RUN yum clean all<br>
RUN yum -y install libaio<br>
RUN yum -y install numactl<br>
RUN yum -y install net-tools<br>
RUN yum -y install perl<br>
<br>
# RUN rpm -e --nodeps mariadb-libs-1:5.5.52-1.el7.x86_64<br>
RUN rpm -ivh mysql-community-common-5.7.29-1.el7.x86_64.rpm<br>
RUN rpm -ivh mysql-community-libs-5.7.29-1.el7.x86_64.rpm<br>
RUN rpm -ivh mysql-community-client-5.7.29-1.el7.x86_64.rpm<br>
RUN rpm -ivh mysql-community-server-5.7.29-1.el7.x86_64.rpm<br>
RUN rm -rf mysql-community-*<br>
RUN yum clean all<br>
<h1>#</h1> ## Entrypoint<br>
<h1>#</h1>ENTRYPOINT ["/bin/bash","/docker-entrypoint.sh"]<br>
</pre><br>
可以发现：Dockerfile 中存在过多分散的 RUN/COPY 指令，而且还是大文件相关操作，导致了过多的镜像分层，使得镜像过大，可以尝试合并相关指令，以减小镜像分层。<br>
<br><strong>合并 RUN 指令</strong><br>
<br>该 Dockerfile 中 RUN 指令较多，可以将 RUN 指令合并到同一层：<br>
<pre class="prettyprint">RUN yum -y install crontabs && \<br>
mv /tmp/dumb-init_1.2.5_x86_64 /usr/bin/dumb-init && \<br>
chmod +x /usr/bin/dumb-init && \<br>
groupadd -g $&#123;MY_GID&#125; -r $&#123;MY_GROUP&#125; && \<br>
adduser $&#123;MY_USER&#125; -u $&#123;MY_UID&#125; -M -s /sbin/nologin -g $&#123;MY_GROUP&#125; && \<br>
tar -vxf /tmp/mysql-5.7.29-1.el7.x86_64.rpm-bundle.tar && \<br>
yum clean all && \<br>
yum -y install libaio numactl net-tools perl && \<br>
rpm -ivh mysql-community-common-5.7.29-1.el7.x86_64.rpm && \<br>
rpm -ivh mysql-community-libs-5.7.29-1.el7.x86_64.rpm && \<br>
rpm -ivh mysql-community-client-5.7.29-1.el7.x86_64.rpm && \<br>
rpm -ivh mysql-community-server-5.7.29-1.el7.x86_64.rpm && \<br>
rm -rf mysql-community-* && \<br>
rm -rf /tmp/mysql-5.7.29-1.el7.x86_64.rpm-bundle.tar<br>
</pre><br>
编译后镜像大小显著下降：<strong>镜像大小 - 1.92GB</strong>。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/0d3babfe8d204a783fcff998f492723d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/0d3babfe8d204a783fcff998f492723d.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>COPY 指令转换合并到 RUN 指令</strong><br>
<br>从上图中可以看到，一个较大的镜像层是 COPY 指令导致的，拷贝的文件较大，所以我们考虑将 COPY 指令转换合并到 RUN 指令；具体做法是将文件上传到 oss，在 RUN 指令中下载。当然也可以发现之前还有一个 RUN 指令漏掉没有合并，需要继续合并到已有 RUN 指令中。<br>
<pre class="prettyprint">RUN curl -o /tmp/mysql-5.7.29-1.el7.x86_64.rpm-bundle.tar http://xxx.oss.aliyuncs.com/addon-pkgs/mysql-5.7.29-1.el7.x86_64.rpm-bundle.tar && \<br>
tar -vxf /tmp/mysql-5.7.29-1.el7.x86_64.rpm-bundle.tar && \<br>
...<br>
</pre><br>
编译后镜像大小显著下降：<strong>镜像大小 - 1.27GB</strong>。<br>
<br><strong>注意</strong>：此处主要是因为 COPY 指令操作的相关文件较大，对应层占用空间较多，才会将 COPY 指令转换合并到 RUN 指令；如果其对应层占用空间较小，则只需分别合并 COPY 指令、RUN 指令，会更加清晰，而没必要将两者转换合并到一层。<br>
<h4>减少容器中不必要的包</h4>还是以上述 MySQL 镜像为例，我们发现下载的包 mysql-5.7.29-1.el7.x86_64.rpm-bundle.tar 包含如下 rpm 包：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/a043788a36f99b3846433a3edf1620f3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/a043788a36f99b3846433a3edf1620f3.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
而安装所需的 rmp 包只有：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/1003b805810236226400b4844656ef63.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/1003b805810236226400b4844656ef63.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
删除不必要的包，用最新的最小 rpm 压缩包替换 mysql-5.7.29-1.el7.x86_64.rpm-bundle.tar 后重新编译镜像：<strong>镜像大小 - 1.19GB</strong>。<br>
<h3>镜像分析工具</h3>前面我们通过 Docker 自带的 docker image history 命令分析镜像，本节主要讲解镜像分析工具 dive 的使用，其主要特征如下：<br>
<ul><li>按层显示 Docker 镜像内容</li><li>指出每一层的变化</li><li>评估 “镜像的效率”，浪费的空间</li><li>快速的构建/分析周期</li><li>和 CI 集成，方便自动化检测镜像效率是否合格</li></ul><br>
<br><h4>镜像效率分析</h4>之前是通过 docker image history 分析镜像体积分布，并进行镜像瘦身，此处将采用 dive 分析镜像有效率。<br>
<br>使用方法：dive <image_name>。<br>
<br><strong>优化前</strong><br>
<br>原始镜像有效率: 41%，大部分镜像体积都是浪费的。<br>
<br>如下所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/1d0b6a5d9916ff6a07a4722d4b6c756e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/1d0b6a5d9916ff6a07a4722d4b6c756e.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>优化后</strong><br>
<br>优化后镜像有效率：97%。<br>
<br><strong>注意</strong>：优化后，镜像分层明显减少，镜像有效率显著提高；但是此时的镜像效率提升主要是依靠减少浪费空间获取的，如果要继续优化镜像体积，需要结合镜像体积瓶颈点评估下一步优化方向。一个通常的继续优化点是：减小基础镜像体积和不必要的包。<br>
<br>如下所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/dd77c53d0eb89b8d76cea6b40f6ae2ac.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/dd77c53d0eb89b8d76cea6b40f6ae2ac.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>通过镜像恢复 Dockerfile</h4>前面主要通过镜像分析工具分析镜像体积分布，发现浪费空间，优化镜像大小。镜像分析工具的另一个典型应用场景是：当只有容器镜像时如何通过镜像恢复 Dockerfile？  <br>
<br><strong>镜像构建历史查看</strong><br>
<br>一般，我们可以通过 docker image history 查看镜像构建历史、镜像层及对应的构建指令，从而还原出对应 Dockerfile。<br>
<br><strong>注意</strong>：docker image history 查看对应的构建命令可能显示不全，需要带上 --no-trunc 选项。<br>
<br>这种方法有如下缺陷：<br>
<ul><li>一些指令信息提取不完整、不易读，如 COPY/ADD 指令，对应的操作文件用 id 表示，如下图所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/23407f88eb8dc78617b0491292650aff.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/23407f88eb8dc78617b0491292650aff.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
</li><li>对于一些镜像层，不是通过 Dockerfile 指令构建出来的，而是直接通过修改容器内容，然后 docker commit 生成，不方便查看该层变更的文件。</li></ul><br>
<br><strong>借助 dive 分析工具还原</strong><br>
<br>借助 dive 分析工具还原 Dockerfile，主要是因为 dive 可以指出每一层的变化，如下：<br><br>
<ul><li>可以根据 COPY 层变化内容（右侧），直观判断拷贝的文件。</li><li>因为可以查看每一层的变化，所以对于 docker commit 也更容易分析相关操作对应的变动范围。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/b5e92880e4503dd3409f3dceeffd69dc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/b5e92880e4503dd3409f3dceeffd69dc.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>思考</h3><h4>镜像变胖的原因</h4>镜像变胖的原因很多，如：<br>
<ul><li>无用文件，比如编译过程中的依赖文件对编译或运行无关的指令被引入到镜像</li><li>系统镜像冗余文件多</li><li>各种日志文件，缓存文件</li><li>重复编译中间文件</li><li>重复拷贝资源文件</li><li>运行无依赖文件</li></ul><br>
<br>但是一般情况是，用户可能对少量的镜像空间浪费不那么敏感；但是在操作大文件时，一些不当的指令（RUN/COPY/ADD）使用方式却很容易造成大量的空间浪费，此时尤其要注意镜像分析与镜像瘦身。<br>
<h4>镜像瘦身难吗？</h4>对于基础镜像的减小、系统包的减小，将镜像体积从 200M 减小到 190M 等可能相对难些，此时需要对程序镜像非常熟悉，并结合专门的分析工具具体分析。但是一般场景下，镜像的浪费很可能仅仅是因为镜像构建命令的使用姿势不佳。此时结合本文的镜像瘦身方法，和 Dockerfile 最佳实践，一般都能实现镜像瘦身。<br><br>
<h4>如何评价瘦身效果？</h4>如果可以评价镜像的空间使用效率，一方面可以比较直观的判断哪些镜像空降浪费严重，需要瘦身；另一方面也可以对瘦身的效果进行评价。上文介绍的，镜像分析工具 dive 即可满足要求。<br><br>
<h4>CI 集成</h4>如果需要对大量镜像的体积使用效率进行把关，就必须将效率检测作为自动化流程的一环，而  dive 就比较容易集成到 CI 中，只需执行如下指令：<br><br>
<pre class="prettyprint">CI=true dive <image-name><br>
</pre><br>
优化前 MySQL 镜像执行结果：由上文可知，优化前实际效率值为 41%，由于默认效率阈值为 90%，所以执行失败。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/3c63d56697bad1e81ba1ab88956048c9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/3c63d56697bad1e81ba1ab88956048c9.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
优化后镜像执行结果：效率值为 97%，由于默认效率阈值为 90%，所以执行通过。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/a06b55b2b8375ec878a42c7db6f6090a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/a06b55b2b8375ec878a42c7db6f6090a.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
同时项目也可以根据其对镜像大小的敏感度，将镜像大小最为一个检测条件，如只有镜像大小超过 1G 时，才进行镜像效率检测，这就可以避免大量小镜像的检测，加快 CI 流程。<br>
<h4>如何自动化检测 Docerfile？</h4>结合上文，ADD/COPY/RUN 指令对应层会增加最终镜像大小，而一般镜像的构建过程包含：文件准备、文件操作等。文件准备阶段在 ADD/COPY/RUN 指令中都有可能出现；文件操作阶段主要由 RUN 指令实现，如果指令过于分散，文件操作阶段会根据<strong>写时复制</strong>原则，拷贝一份到当前镜像层，造成空间浪费，尤其是在涉及大文件操作时。更严重的情况是，假如对文件的操作分散在不同的 RUN 指令中，不就造成了多次文件拷贝浪费了。试想一下，如果拷贝和操作在同一层进行，不就可以避免这些文件跨层拷贝了吗。  <br>
<br>所以有以下一些通用的优化检测方法和建议：<br>
<ul><li>检测 RUN 指令是否过于分散，建议合并。</li><li>检测 COPY/ADD 指令是否有拷贝大文件，且在 RUN 指令中有对文件进行操作，则建议将 COPY/ADD 指令转换合并到 RUN 指令中。当然此种检测方法，仅仅只有 Dockerfile 还是不够的，还需要有上下文，才能检测相关文件的大小。</li></ul><br>
<br>当然还有很多其他的检测方向和优化建议，有待进一步完善，欢迎留言讨论。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/hn8Env3e5PztLgOCAYZamA" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/hn8Env3e5PztLgOCAYZamA</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            