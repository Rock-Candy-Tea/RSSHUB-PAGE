
---
title: 'docker'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/11531502-b471cf28abce8c70.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/11531502-b471cf28abce8c70.png'
---

<div>   
<h1>一、docker简介</h1>
<p><strong>1、为什么会出现docker？</strong><br>
一般情况下是开发人员开发好代码，本地测试通过后，打成jar包或者war包，交给运维人员，部署到服务器上。就是这么个过程，经常会出现如下场景：</p>
<ul>
<li>运维：哥们，你这代码不行啊，跑不起来；</li>
<li>开发：怎么可能，你看我本地是可以的；</li>
<li>运维：你过来看啊，服务器上就是不行；</li>
<li>开发：我的代码怎么可能有问题，你会不会玩？<br>
……</li>
</ul>
<p>一样的代码，本地可以跑，服务器上就不行，那这就是环境的问题和配置的问题了。而且，一个产品从开发到上线，往往有开发环境，测试环境，仿真环境和生产环境，每个环境我们都需要安装一遍mysql、redis、nginx，activemq等，运维的工作量也挺大，而且都是重复的工作。为了解决这些痛点，docker就出现了。</p>
<hr>
<p>欢迎大家关注我的公众号 <strong>javawebkf</strong>，目前正在慢慢地将简书文章搬到公众号，以后简书和公众号文章将同步更新，且简书上的付费文章在公众号上将免费。</p>
<hr>
<p><strong>2、是什么？</strong></p>
<ul>
<li>官网：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.docker.com" target="_blank">https://www.docker.com</a>
</li>
</ul>
<p>docker就是一个容器，一次构建，处处运行。也就是说，我开发环境安装了mysql、redis，我可以直接将这两个镜像搬到测试环境，开箱即用，而不用重新去配置。</p>
<p><strong>3、虚拟机技术和容器技术：</strong></p>
<ul>
<li>虚拟机：相当于一台电脑，模拟了一整套完整的操作系统。缺点是启动慢，冗余步骤多，占用资源多。</li>
<li>容器技术(docker)：不是模拟完整的操作系统，而是对进程进行隔离，对可以公用的不进行模拟。因此系统变得轻量，启动也是秒级的。</li>
</ul>
<p><strong>4、docker的核心概念：</strong></p>
<ul>
<li><p>容器：就是docker的logo鲸鱼背上那一个个地集装箱。一个集装箱就是一个容器，比如你在docker上要安装redis、mysql、jdk，那么就需要三个集装箱，也就是三个容器。</p></li>
<li><p>镜像：用来生成容器实例的东西</p></li>
<li><p>仓库：存放镜像的地方。有个叫docker hub的网站，它就是仓库。不过国内访问docker hub特别慢，国内一般用阿里云和网易云的仓库。</p></li>
</ul>
<h1>二、docker的安装</h1>
<p><strong>1、安装前提：</strong></p>
<ul>
<li>centos 6.5或者更高版本</li>
<li>如果是centos 6.5，要求系统64位，内核版本2.6.32-431或更高</li>
<li>如果是centos 7，要求系统64，内核版本3.10或者更高</li>
<li>查看系统版本命令：<code>cat /etc/redhat-release</code>
</li>
<li>查看系统内核版本的命令：<code>uname -r</code>
</li>
</ul>
<p><strong>2、docker的安装：</strong></p>
<p>centos 6安装docker：</p>
<ul>
<li><code>yum install -y epel-release</code></li>
<li><code>yum install -y docker-io</code></li>
<li>安装后的配置文件：<code>/etc/sysconfig/docker</code>
</li>
<li>启动docker服务：<code>service docker start</code>
</li>
<li>验证版本信息：<code>docker version</code>，出现版本信息说明安装成功。</li>
</ul>
<p>centos 7安装docker:</p>
<ul>
<li>官网文档：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdocs.docker.com%2Fengine%2Finstall%2Fcentos%2F" target="_blank">https://docs.docker.com/engine/install/centos/</a>
</li>
<li>安装gcc相关：<code>yum install -y gcc</code>，<code>yum install -y gcc-c++</code>，安装完执行<code>gcc -v</code>有版本信息就安装成功。</li>
<li>卸载旧版本docker：</li>
</ul>
<pre><code>yum remove docker \
           docker-client \
           docker-client-latest \
           docker-common \
           docker-latest \
           docker-latest-logrotate \
           docker-logrotate \
           docker-engine
</code></pre>
<ul>
<li>安装需要的软件包：<code>yum install -y yum-utils</code>
</li>
<li>设置stable镜像仓库(推荐用阿里云的库)：</li>
</ul>
<pre><code>yum-config-manager \
   --add-repo \
   http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
</code></pre>
<ul>
<li>更新yum软件包索引：<code>yum makecache fast</code>
</li>
<li>安装docker ce：<code>yum install -y docker-ce</code>
</li>
<li>启动docker：<code>systemctl start docker</code>
</li>
<li>测试：<code>docker -v</code>，有版本信息则安装成功，再执行<code>docker run hello-world</code>，会有 hello from docker的信息。</li>
<li>镜像加速配置：</li>
</ul>
<pre><code>mkdir -p /etc/docker
vim /etc/docker/daemon.json
systemctl daemon-reload
systemctl restart docker
</code></pre>
<p>daemon.json的内容如下：</p>
<pre><code># 网易云
&#123;"registry-mirrors":["http://hub-mirror.c.163.com"]&#125;
# 阿里云
&#123;"registry-mirrors":["你阿里云的镜像加速链接"]&#125;
</code></pre>
<p>获取阿里云加速镜像链接的方法：<br>
登陆<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fcr.console.aliyun.com" target="_blank">https://cr.console.aliyun.com</a>，然后点击左下角的“镜像加速器”即可。</p>
<ul>
<li>卸载：</li>
</ul>
<pre><code>systemctl stop docker
yum -y remove docker-ce
rm -rf /var/lib/docker
</code></pre>
<p><strong>3、hello world：</strong><br>
上面说过执行<code>docker run hello-world</code>会打印出相关信息，执行这条命令过程如下：</p>
<ul>
<li>首先会查找本机是否有该镜像</li>
<li>如果有，直接以本机的那个镜像为模板生成容器实例运行</li>
<li>如果没有，去docker hub上查找</li>
<li>找到了，下载到本地，然后生成实例运行，找不到就返回错误信息</li>
</ul>
<h1>三、docker常用命令</h1>
<p><strong>1、帮助命令：</strong></p>
<ul>
<li>查看版本信息：<code>docker -v</code>
</li>
<li>查看docker信息：<code>docker info</code>
</li>
<li>查看帮助命令：<code>docker --help</code>，类似linux的<code>man</code>命令</li>
</ul>
<p><strong>2、镜像命令：</strong><br>
回顾一下docker的logo，海上有一头鲸鱼，鲸鱼背上有一个个的集装箱。对应关系如下：</p>
<ul>
<li>海 ------ 电脑主机</li>
<li>鲸鱼 ------ docker</li>
<li>集装箱 ------ 容器实例，来自镜像模板</li>
</ul>
<p>常用镜像命令如下：</p>
<ul>
<li>列出主机上的镜像：<code>docker images</code>
</li>
<li>列出全部镜像(包括中间镜像)：<code>docker images -a</code>
</li>
<li>只列出镜像的id：<code>docker images -q</code>
</li>
<li>列出全部镜像的id：<code>docker images -qa</code>
</li>
<li>显示镜像的摘要信息：<code>docker images --digests</code>
</li>
<li>显示完整的镜像信息：<code>docker images --no-trunc</code>
</li>
<li>从docker hub上查找xxx镜像：<code>docker search xxx</code>
</li>
<li>从docker hub上查找点赞数超过30的xxx镜像：<code>docker search -s 30 xxx</code>
</li>
<li>从docker hub上查找xxx镜像，并显示摘要信息：<code>docker search -s 30 --no-trunc xxx</code>
</li>
<li>从docker hub上查找能自动构建的xxx镜像：<code>docker search --automated xxx</code>
</li>
<li>从docker hub上拉取(下载)最新版的xxx镜像：<code>docker pull xxx</code>
</li>
<li>删除xxx(可以是镜像名，也可以是id)镜像：<code>docker rmi xxx</code>
</li>
<li>强制删除xxx镜像：<code>docker rmi -f xxx</code>
</li>
<li>删除多个镜像：<code>docker rmi -f xxx yyy</code>
</li>
<li>删除全部镜像：<code>docker rmi -f $(docker images -qa)</code>
</li>
</ul>
<p><strong>3、容器命令：</strong><br>
首先我们执行<code>docker pull centos</code>拉取一个centos的镜像，下面所说的容器都是指centos(都可以是名字或者id)。</p>
<ul>
<li>新建并启动容器：<code>docker run -it centos</code>
</li>
<li>启动容器可选的参数有：<code>--name</code>：为容器指定名字；<code>-d</code>：后台运行容器；<code>-P</code>：随机端口映射；<code>-p</code>：指定端口映射；<code>-i</code>：以交互模式运行容器；<code>-t</code>：为容器重新分配一个伪输入终端，常与<code>-i</code>一起使用</li>
<li>列出当前正在运行的容器：<code>docker ps</code>
</li>
<li>列出运行的容器可选参数有：<code>-a</code>：列出当前运行和历史上运行过的容器；<code>-l</code>：显示最近创建的容器；<code>-n</code>：显示最近创建的n个容器；<code>-q</code>：静默模式，只显示容器编号；<code>--no-trunc</code>：显示完整摘要信息</li>
<li>退出容器：<code>exit</code>：容器停止退出；<code>ctrl + p + q</code>：容器不停止退出</li>
<li>启动容器：<code>docker start centos</code>
</li>
<li>重启容器：<code>docker restart centos</code>
</li>
<li>停止容器：<code>docker stop centos</code>
</li>
<li>强制停止容器：<code>docker kill centos</code>
</li>
<li>删除容器：<code>docker rm -f centos</code>
</li>
<li>一次性删除多个容器：<code>docker rm -f $(docker ps -a -q</code>或者<code>docker ps -a -q | xargs docker rm</code>
</li>
<li>后台运行容器：<code>docker run -d centos</code>，启动后，再<code>docker ps</code>，发现根本就没有正在运行的容器，但是刚刚确实启动成功了，因为启动后返回了一个id。这是docker的机制造成的，后台启动docker容器，前台没有交互，docker会认为它没事可做，就杀死了。</li>
<li>查看容器倒数n行日志：<code>docker logs -f -t --tail n 容器id</code>
</li>
<li>查看容器内运行的进程：<code>docker top 容器id</code>
</li>
<li>查看容器内部细节(返回一个json串)：<code>docker inspect 容器id</code>
</li>
<li>进入正在运行的容器(ctrl + p + q退出后重新进入)：<code>docker attach 容器id</code>
</li>
<li>不进入容器但对容器执行相关命令：<code>docker exec -t 容器id 命令</code>；比如不进入docker上运行的centos直接执行<code>ls /</code>命令：<code>docker exec -t centos的id ls /</code>
</li>
<li>将容器内的数据拷贝到主机：<code>docker cp 容器id:容器内路径 主机路径</code>
</li>
</ul>
<h1>四、docker镜像</h1>
<p><strong>1、什么是镜像？</strong><br>
镜像是一种轻量级的可执行的独立软件包。用来打包软件运行环境和基于运行环境开发的软件，包括代码、运行时、库、环境变量和配置文件。docker底层是一个unionFS(联合文件系统)，即是一层一层的文件系统组成。</p>
<p><strong>2、镜像为什么那么大？</strong><br>
执行<code>docker pull tomcat</code>命令，下载一个tomcat镜像，然后执行<code>docker images</code>，发现一个tomcat就600多兆，为什么那么大？因为刚才说的，镜像是一个联合文件系统，tomcat镜像不仅仅包含tomcat，还包含tomcat运行的各种环境，一个镜像包含了很多层，分层镜像如下：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="665" data-height="389"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-b471cf28abce8c70.png" data-original-width="665" data-original-height="389" data-original-format="image/png" data-original-filesize="16411" src="https://upload-images.jianshu.io/upload_images/11531502-b471cf28abce8c70.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">tomcat镜像</div>
</div>
<p><strong>3、docker为什么采用分层镜像？</strong><br>
最大的好处就是共享资源。比如多个镜像都需要jdk，那么宿主机上其实只要保存一份jdk就可以了，内存中也只需要加载一份。镜像的每一层都是可以共享的。</p>
<p><strong>4、docker commit命令：</strong><br>
首先我们运行<code>docker run -it -p 8888:8080 tomcat</code>，这里表示docker内部将tomcat运行在8080端口，对外暴露8888端口，即执行完这条命令，我们要用8888端口才能访问到tomcat。如果你访问到的是404，不要方，这是因为你下载的这个版本的tomcat，webapps目录是空的，资源都在webapps-dist目录下，可以执行如下操作：</p>
<ul>
<li>进入tomcat目录：<code>docker exec -it tomcat容器的id /bin/bash</code>
</li>
<li>列出tomcat目录下的文件：<code>ls -l</code>
</li>
<li>给webapps重命名：<code>mv webapps webapps2</code>
</li>
<li>将webapps-dist改名为webapps：<code>mv webapps.dist webapps</code>
</li>
</ul>
<p>刷新页面，就可以看到熟悉的tomcat首页了。<br>
上面是指定对外暴露8888端口，还可以执行<code>docker run -it -P tomcat</code>，大写的P表示随机分配端口，不自己指定。用这个命令启动后，执行<code>docker ps</code>，就可以看到随机分配的端口是什么。</p>
<p>上面我们对tomcat做了一些修改，把访问会报404的tomcat改成了一个正常的tomcat，我们就可以使用commit命令以我们改好的tomcat为模板，生成一个启动就能直接访问的新的tomcat镜像。执行如下命令：<br>
<code>docker commit -a="zhusl" -m="normal tomcat" 容器id newtomcat:1.0</code></p>
<ul>
<li>-a是作者，-m是备注信息，newtomcat是新镜像的名字，1.0是版本号</li>
</ul>
<h1>五、容器数据卷</h1>
<p><strong>1、是什么？</strong><br>
我们在docker上运行容器实例，运行时产生的数据，当docker关闭了就没了。但是我们希望有些数据可以持久化保存下来，这个保存的地方的就是容器数据卷，并且保存下来的数据可以共享。</p>
<p><strong>2、容器数据卷的特点：</strong></p>
<ul>
<li>数据卷可在容器之间共享或重用数据</li>
<li>卷中的更改可直接生效</li>
<li>数据卷中的更改不会包含在镜像的更新中</li>
<li>数据卷的生命周期一直持续到没有容器使用它为止</li>
</ul>
<p><strong>3、添加数据卷的方法：</strong><br>
添加数据卷有两种方法，一种是命令添加，一种是用dockerfile。<br>
<strong><em>命令添加：</em></strong></p>
<ul>
<li><p>添加数据卷命令：<code>docker run -it -v /宿主机绝对路径目录:/容器内目录 镜像名</code><br>
比如执行<code>docker run -it -v /mydatadir:/dockerdatadir centos</code>，就表示让centos这个镜像和主机之间建立数据卷，主机根目录下的<code>mydatadir</code>和centos镜像根目录下的<code>dockerdatadir</code>目录建立连接，进行数据共享。目录不存会自动新建目录。执行了以上命令后，先查看主机根目录下是否有mydatadir目录，然后再执行<code>docker run -it centos /bin/bash</code>，ls查看一下centos镜像的根目录下是否有dockerdatadir目录。</p></li>
<li>
<p>查看数据卷是否挂载成功：<code>docker inspect 容器id</code>。如果你看到两个目录都成功新建了还是不放心，可以用这条命令查看，如果在返回的内容中看到了如下信息则挂载成功。<br>
</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="733" data-height="178"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-8b9b7d2dfafad492.png" data-original-width="733" data-original-height="178" data-original-format="image/png" data-original-filesize="10160" src="https://upload-images.jianshu.io/upload_images/11531502-8b9b7d2dfafad492.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">数据卷挂载成功</div>
</div>
<p></p>
</li>
<li><p>验证通过数据卷可实现数据共享：首先在主机的mydatadir目录下新建一个test.txt文件，然后发现centos的镜像的dockerdatadir目录也有test.txt文件。然后再centos镜像中往test.txt文件些内容，回到主机再次查看test.txt文件，发现也是有内容的。并且容器推出后，在主机上的mydatadir目录下做的任何操作，在容器重启后，都会被同步到dockerdatadir目录下。</p></li>
<li><p>以只读方式添加数据卷：<code>docker run -it -v /宿主机绝对路径目录:/容器内目录:ro 镜像名</code>，加上ro，表示read only，容器只能读数据，不能进行写操作。</p></li>
</ul>
<p><strong><em>dockerFile添加：</em></strong></p>
<ul>
<li>主机根目录下新建<code>mydocker</code>文件夹；</li>
<li>进入<code>mydocker</code>目录，新建dockerfile文件：<code>vim dockerfile</code>，文件内容如下：</li>
</ul>
<pre><code>FROM centos
VOLUME ["/dockerdatadir1","/dockerdatadir2"]
CMD echo "finished,---------success"
CMD /bin/bash
</code></pre>
<ul>
<li>然后执行build命令生成新的镜像，镜像名叫zhusl/centos：<code>docker build -f /mydocker/dockerfile -t zhusl/centos .</code>
</li>
<li>查看镜像：<code>docker images</code>，发现已经有zhusl/centos这个镜像了。这个镜像就是，我们以centos镜像为来源，添加了数据卷，新生成的一个centos。</li>
<li>运行新生成的这个镜像，就可以发现在zhusl/centos的根目录下有两个数据卷，dockerdatadir1和dockerdatadir2。那么这两个数据卷对应宿主机的哪个目录呢？还是执行<code>docker inspect 容器id</code>，就可以看到了，如下图：<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1087" data-height="217"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-4482b477889c9074.png" data-original-width="1087" data-original-height="217" data-original-format="image/png" data-original-filesize="20475" src="https://upload-images.jianshu.io/upload_images/11531502-4482b477889c9074.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">数据卷</div>
</div>
</li>
</ul>
<p><strong>4、数据卷容器：</strong><br>
上面说了数据卷，数据卷容器其实就是数据卷之间的传递性。比如还是以zhusl/centos镜像为例，先执行<code>docker run -it --name dc01 zhusl/centos</code>，运行一个名为dc01的实例，然后再执行<code>docker run -it --name doc02 --volumes-from dc02 zhusl/centos</code>，以dc01为父容器，运行一个dc02。因为zhusl/centos是添加了数据卷的，所以运行的dc01是挂载了数据卷的，然后dc02又是from dc01，所以dc02也挂载了数据卷。如果还有一个dc03也是继承自dc01，当dc01挂了，dc02和dc03之间也是可以进行数据共享的。</p>
<h1>六、dockerFile</h1>
<p><strong>1、是什么？</strong><br>
就是一个写命令的文件，然后通过这个文件，就可以构建镜像。</p>
<p><strong>2、构建的三个步骤：</strong></p>
<ul>
<li>编写dockerfile文件</li>
<li>docker build</li>
<li>docker run</li>
</ul>
<p>登陆docker hub，然后随便搜索一个镜像，就以centos为例，选择版本然后进入，就可以看到它的dockerfile文件内容。如下就是centos7的dockerfile文件内容：</p>
<pre><code>FROM scratch
ADD centos-7-x86_64-docker.tar.xz /

LABEL \
    org.label-schema.schema-version="1.0" \
    org.label-schema.name="CentOS Base Image" \
    org.label-schema.vendor="CentOS" \
    org.label-schema.license="GPLv2" \
    org.label-schema.build-date="20200504" \
    org.opencontainers.image.title="CentOS Base Image" \
    org.opencontainers.image.vendor="CentOS" \
    org.opencontainers.image.licenses="GPL-2.0-only" \
    org.opencontainers.image.created="2020-05-04 00:00:00+01:00"

CMD ["/bin/bash"]
</code></pre>
<ul>
<li>FROM scratch：相当于java的Object类。所以镜像的基础镜像，即源镜像。</li>
<li>ADD：后面的是要添加的东西</li>
<li>LABEL：一些标签信息</li>
<li>CMD：要执行的命令</li>
</ul>
<p><strong>3、dockerfile内容基础知识：</strong></p>
<ul>
<li>保留字(就是上面那些FROM、ADD等关键字)都必须为大写字母并且后面要跟随至少一个参数</li>
<li>指令从上到下按顺序执行</li>
<li>#表示注释</li>
<li>每条指令都会创建一个新的镜像层，并对镜像进行提交</li>
</ul>
<p><strong>4、dockerfile的执行流程：</strong></p>
<ul>
<li>docker从基础镜像中运行一个容器</li>
<li>执行一条指令并对容器做出修改</li>
<li>执行类似docker commit的操作提交一个新的镜像层</li>
<li>docker再基于刚提交的镜像运行一个新的容器</li>
<li>执行dockerfile中的下一条指令直到所有指令都执行完成</li>
</ul>
<p><strong>5、dockerfile的保留字：</strong></p>
<ul>
<li>FROM：表示当前要构建的新镜像是基于哪个镜像的</li>
<li>MAINTAINER：作者 + 邮箱</li>
<li>RUN：容器构建时需要运行的命令</li>
<li>EXPOSE：服务的端口号</li>
<li>WORKDIR：指定在创建容器后，终端默认登陆进来的工作目录</li>
<li>ENV：设置环境变量用的</li>
<li>ADD：要添加进镜像并解压缩的东西</li>
<li>COPY：要拷贝进镜像的东西</li>
<li>VOLUME：数据容器卷，用于持久化</li>
<li>CMD：指定一个容器启动时要运行的命令，一个dockerfile中可以有多个CMD，但最终只有最后一个生效，CMD会被docker run后面的参数替换</li>
<li>ENTRYPOINT：指定一个容器启动时要运行的命令，docker run后面的参数不会替换这个，而是在后面追加</li>
<li>ONBUILD：触发器。就是另一个镜像基于自己构建时，当另一个镜像启动时自己要做的事</li>
</ul>
<p><strong>6、dockerfile构建镜像实操：</strong></p>
<ul>
<li>案例1：基础命令的使用：就以构建centos为例，我们从docker hub上拉下来的centos，默认路径是/，没有vim编辑器，也没有ifconfig命令。这个centos要实现登陆后默认路径的~，要有vim编辑器，要有ifconfig命令。下面开始编写dockerfile文件：</li>
</ul>
<pre><code># 基于docker hub上拉下来的centos进行构建
FROM centos
# 容器启动后工作目录
WORKDIR ~
# 安装vim
RUN yum -y install vim
# 安装网络工具，使其能用ifconfig命令
RUN yum -y install net-tools
# 端口号
EXPOSE 80
CMD /bin/bash
</code></pre>
<p>新建一个dockerfile2文件，内容就是上面那段，然后执行<code>docker build -f /mydocker/dockerfile2 -t mycentos:1.0 .</code>进行构建。-f后面的是dockerfile2文件的路径，mycentos是镜像名字，1.0是版本号，.代表当前路径。</p>
<p>执行完后，<code>docker images</code>就会发现有一个新镜像，名字叫mycentos。然后运行该镜像，就会发现这个mycentos可以使用vim和ifconfig的。再回溯一个问题，镜像那么大，是因为它包含了它运行所需的所有环境，那么是不是很浪费空间？就比如这个，我原本有一个centos镜像，只不过没有vim编辑器，现在我构建一个新的有vim的mycentos，docker images 显示centos 600M，mycentos 620M，那这两个是不是就要占用1个G？其实并不是，因为镜像是可以共享的，mycentos 是form centos的，也就是说这600其实是共用的，最后这两个镜像其实占空间就是620M。</p>
<p>执行<code>docker history 镜像id</code>，就可以列出镜像的历史，即这个镜像有多少层。</p>
<ul>
<li><p>案例2：CMD指令的使用：执行<code>docker run -it -p 7777:8080 tomcat ls -l</code>，就是在启动命令后追加<code>ls -l</code>参数，列出登陆后的目录。然后发现tomcat根本就没有启动，只是列出了tomcat的目录。因为dockerfile的CMD命令只有最后一行生效，<code>ls -l</code>这个命令把启动tomcat的CMD覆盖了，所以没启动。</p></li>
<li><p>案例3：ENTRYPOINT的使用：新建一个dockerfile3，内容如下：</p></li>
</ul>
<pre><code>FROM centos
RUN yum install -y curl
CMD ["curl","-s","http://ip.cn"]
</code></pre>
<p>意思就是制作一个镜像，一启动，就可以查出本机的IP。执行<code>docker build -f /mydocker/dockerfile3 -t myip .</code>进行构建。然后运行该容器，就可以打印出ip信息。如果过执行的时候想加参数，比如<code>docker run -it myip -i</code>，实际上就是想执行curl的时候加上<code>-i</code>参数，打印请求头信息，那么抱歉，<code>-i</code>会覆盖之前的命令，即覆盖<code>CMD ["curl","-s","http://ip.cn"]</code>这一样，然后<code>-i</code>根本就不是一个可执行命令，所以执行报错。要实现上面的需求，即加个<code>-i</code>，让它真正执行的是<code>curl -s -i https://ip.cn</code>，只需要把<code>CMD</code>换成<code>ENTRYPOINT</code>，然后启动容器时用<code>docker run -it myip -i</code>即可。</p>
<ul>
<li>案例4：<code>ONBUILD</code>的使用：修改dockerfile3，在后面加上如下的命令：</li>
</ul>
<pre><code>ONBUILD RUN echo "我被触发了"
</code></pre>
<p>然后，新建dockerfile4，FROM myip，build的时候会打印出 "我被触发了" 这一句话。</p>
<ul>
<li>案例5：<code>COPY</code>和<code>ADD</code>的使用。首先在opt目录下先搞两个tar.gz包和一个copy.txt文件，一个jdk8，一个tomcat9。编写dockerfile，内容如下：</li>
</ul>
<pre><code>FROM   centos
# 复制文件
COPY copy.txt /usr/local/cincontainer.txt
# 添加并解压jdk
ADD jdk-8u171-linux-x64.tar.gz /usr/local
# 添加并解压tomcat9
ADD apache-tomcat-9.0.8.tar.gz /usr/local
# 安装vim
RUN yum install -y install vim
# 设置登陆落脚点
ENV MYPATH /usr/local
WORKDIR $MYPATH
# 配置jdk和tomcat环境变量
ENV JAVA_HOME /usr/local/jdk1.8.0_171
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
ENV CATALINA_HOME /usr/local/apache-tomcat-9.0.8
ENV CATALINA_BASE /usr/local/apache-tomcat-9.0.8
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/lib:CATALINA_HOME/bin
# 指定容器运行端口
EXPOSE 8080
# 启动命令
CMD /usr/lcoal/apache-tomcat-9.0.8/bin/startup.sh && tail -F /usr/local/apache-tomat-9.0.8/bin/logs/catalina.out
</code></pre>
<h1>七、常用镜像安装</h1>
<p><strong>1、MySQL：</strong></p>
<ul>
<li>拉取镜像：<code>docker pull mysql:5.7</code>
</li>
<li>启动并添加数据卷：<code>docker run -p 3306:3306 --name mysql -v /zhusl/mysql/conf:/etc/mysql/conf.d -v /zhusl/mysql/logs:/logs -v /zhusl/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7</code>
</li>
<li>进入容器：<code>docker exec -it 容器id /bin/bash</code>
</li>
<li>使用mysql：<code>mysql -u root -p</code>
</li>
</ul>
<p><strong>2、redis:</strong></p>
<ul>
<li>搜索镜像：<code>docker search redis</code>
</li>
<li>拉取镜像：<code>docker pull redis</code>
</li>
<li>启动redis镜像：<code>docker run -p 6379:6379 -v /zhusl/redis/data:/data -v /zhusl/redis/conf/redis.conf:/usr/local/etc/redis/redis.conf -d redis redis-server /usr/local/etc/redis/redis.conf --appendonly yes</code><br>
appendonly yes表示开启aof。</li>
<li>连接redis：<code>docker exec -it redis容器id redis-cli</code>
</li>
</ul>
<h1>八、本地镜像推送到阿里云</h1>
<ul>
<li>登陆阿里云开发者平台：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdev.aliyun.com%2Fsearch.html" target="_blank">https://dev.aliyun.com/search.html</a>
</li>
<li>创建镜像仓库</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1912" data-height="544"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-47009ebfb9279b46.png" data-original-width="1912" data-original-height="544" data-original-format="image/png" data-original-filesize="96903" src="https://upload-images.jianshu.io/upload_images/11531502-47009ebfb9279b46.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">创建镜像仓库</div>
</div>
<ul>
<li>将本地镜像推送到阿里云：</li>
</ul>
<pre><code>docker login --username= registry.cn-hangzhou.aliyuncs.com
# 执行完上一条命令会要你输入用户名和密码
docker tag 镜像id registry.cn-hangzhou.aliyuncs.com/zhushulin/redis:镜像版本号
docker push registry.cn-hangzhou.aliyuncs.com/zhushulin/redis:镜像版本号
</code></pre>
  
</div>
            