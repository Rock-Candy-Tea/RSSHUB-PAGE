
---
title: 'docker 基础(5) 第一个 dockerfile'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/8207483-202c082eb371986c.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/8207483-202c082eb371986c.png'
---

<div>   
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="610" data-height="305"><img data-original-src="//upload-images.jianshu.io/upload_images/8207483-202c082eb371986c.png" data-original-width="610" data-original-height="305" data-original-format="image/png" data-original-filesize="44384" src="https://upload-images.jianshu.io/upload_images/8207483-202c082eb371986c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">docker</div>
</div>
<h2>dockerfile</h2>
<p>dockerfile 可以理解如何创建镜像文件</p>
<ul>
<li>手动编写 dockerfile 文件，必须符合 file 的规范</li>
<li>用 docker build 执行，获得一个自定义的镜像</li>
<li>用 run 命令运行</li>
</ul>
<pre><code>FROM scratch
</code></pre>
<p>这是就是最基础镜像，一切镜像都基于 scratch</p>
<pre><code>CMD ["/bin/bash"]
</code></pre>
<p>dockerfile</p>
<ul>
<li>每条保留字指令都必须为大写字母且后面要至少跟随一个参数<code>FROM</code> 这样指令后必须有内容</li>
<li>指令执行顺序是之上而下执行</li>
<li>
<h1>表示注释</h1>
</li>
<li>每条指令都会创建一个新的镜像层，并对镜像进行提交</li>
</ul>
<p>镜像、容器和 dockerfile 的关系</p>
<ul>
<li>dockerfile 镜像的图纸</li>
<li>docker 镜像是模板</li>
<li>docker 容器镜像的一个一个实例</li>
</ul>
<h3>dockerfile 体系结构</h3>
<ul>
<li>FROM 基础镜像，指定创建镜像是基于哪一个镜像</li>
<li>MAINTAINER 镜像维护人的信息，邮箱和名称</li>
<li>RUN 容器构建时需要执行的命令</li>
<li>EXPOSE 暴露出镜像的实例服务端口号</li>
<li>WORDDIR 指定创建容器后，终端默认登录进来后的工作目录，如果没有指定默认工作目录是根目录</li>
<li>ENV 用来在构建镜像过程中设置环境变量</li>
<li>ADD 相对于 COPY ，不但复制而且并进行加压，将宿主机目录下文件 copy 进镜像并自动处理 url 和解压 tar 压缩包</li>
<li>COPY 直接复制，类似 ADD copy文件和目录到镜像中。将从构建上下文目录中<源路径>的文件/目录复制到新的一层的镜像内的<目标路径>位置</li>
<li>VOLUME 容器数据卷，用于数据保存和持久化</li>
<li>CMD 指定一个容器启动时要运行的命令，但是 ENTRYPOINT 的区别是在 dockerfile 可以有多个 CMD 命令，CMD 会被 docker run 之后的参数替换</li>
<li>ENTRYPOINT 指定一个容器启动时要运行的命令，</li>
<li>ONBUILD 当构建一个被继承的 dockerfile 时运行命令，父镜像在被子继承后父镜像的 onbuild 被触发</li>
</ul>
<pre><code>docker rm -f $(docker ps -q)
</code></pre>
<p>创建一个 Ubuntu</p>
<ul>
<li>登录后默认路径</li>
<li>vim 编辑器</li>
<li>查看网络配置ifconfig支持</li>
</ul>
<pre><code>FROM centos
MAINTAINER zidea

ENV mpath=/tmp
WORKDIR $&#123;mpath&#125;

RUN yum -y install vim
RUN yum -y install net-tools

EXPOSE 80
CMD [ "/bin/bash" ]
</code></pre>
<pre><code>docker build -f Dockerfile -t mycentos:1.0 .
</code></pre>
<pre><code>Successfully built xxxxxx
Successfully tagged mycentos:1.0
</code></pre>
<pre><code>xxx        4 minutes ago       /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B                  
xxx        4 minutes ago       /bin/sh -c #(nop)  EXPOSE 80                    0B                  
xxx        4 minutes ago       /bin/sh -c yum -y install net-tools             24.1MB              
xxx        4 minutes ago       /bin/sh -c yum -y install vim                   59.8MB              
xxx        5 minutes ago       /bin/sh -c #(nop) WORKDIR /tmp                  0B                  
xxx        5 minutes ago       /bin/sh -c #(nop)  ENV mpath=/tmp               0B                  
xxx        5 minutes ago       /bin/sh -c #(nop)  MAINTAINER zidea             0B                  
xxx        3 months ago        /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B                  
<missing>           3 months ago        /bin/sh -c #(nop)  LABEL org.label-schema.sc…   0B                  
<missing>           3 months ago        /bin/sh -c #(nop) ADD file:aa54047c80ba30064…   237MB
</code></pre>
  
</div>
            