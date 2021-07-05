
---
title: 'Docker基本使用命令'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=43'
author: Dockone
comments: false
date: 2021-07-05 07:06:23
thumbnail: 'https://picsum.photos/400/300?random=43'
---

<div>   
<br><h3>前言</h3>刚看别人使用Docker的时候有很多不解，为什么要用Docker，Docker怎么用？Docker配置为什么这么难？为什么网络访问不通？等等因素阻碍了笔者学习Docker？其实笔者也很笨，有很多思考不清晰的点。顺便也分享下。<br>
<br>学时疑惑：<br>
<br>Q：我一套服务为什么不放在一个容器里面（Java、MySQL、Nginx、Redis等）？<br>
A：因为既要维护容器内网络，又要维护端口等等之类的东西，Docker就是为了快速搭建环境而生的，而且Docker最好也是一个服务一个容器，这样好打理。<br>
<br>Q：Docker能放到生产环境吗？<br>
A：在公司没有专门的运维团队情况下，不建议使用Docker部署的环境作为生产环境，因为不仅仅要维护项目和中间件，Docker或者Kubernetes出现问题后，还要解决这些问题，也就是还要解决Docker的问题。如果在没有专门运维团队的情况下，最好使用某里云的服务，例如RDS，SLB等，最起码别人还会帮你维护你的数据库和服务。<br>
<h3>基本命令</h3><h4>下载镜像</h4><pre class="prettyprint"># 以Redis为例子<br>
docker pull redis<br>
</pre><br>
<h4>运行镜像</h4><pre class="prettyprint">docker run \<br>
-d \ # 后台运行<br>
--name redis6 \ # 自定义名字<br>
-p 6379:6379 \ # 端口映射<br>
redis # 镜像名称<br>
docker run -d --name redis6 -p 6379:6379 redis redis-server --appendonly yes --requirepass "123456" # 完整命令<br>
</pre><br>
<h4>进入容器</h4>第一种（不推荐，当退出容器使用exit命令时，会停止这个容器）：<br>
<pre class="prettyprint">docker attach 容器id<br>
</pre><br>
第二种：<br>
<pre class="prettyprint">docker exec -it 容器id /bin/bash<br>
</pre><br>
<h4>暂停容器</h4><pre class="prettyprint">docker stop 容器id<br>
</pre><br>
<h4>启动容器</h4><pre class="prettyprint">docker start 容器id<br>
</pre><br>
<h4>查询容器列表</h4><pre class="prettyprint">docker ps -a # 查看所有容器<br>
docker ps # 查看运行中的容器<br>
</pre><br>
run和start的区别：<br>
<ul><li>run是创建一个新的容器</li><li>start是把已经创建好的容器启动</li></ul><br>
<br><h4>查看容器信息</h4><pre class="prettyprint">docker inspect 容器id<br>
</pre><br>
<h3>挂载</h3><h4>挂载介绍</h4>容器里面的文件都是在容器内部，而跟你当前电脑是没有关系的，如果删除了容器怎么办？但是资料又想保存就像MySQL一样，我只是换一台电脑就要把整个容器复制过去，太麻烦了！所以需要把容器的文件跟当前主机文件作为一个<strong>映射</strong>。<br>
<h4>命令教程</h4>参数-v宿主机路径:容器路径<br>
<pre class="prettyprint"># 以MySQL为例子<br>
docker run -d --name mysql8 -p 3306:3306 -v /data/mysql8/config:/etc/mysql/conf.d -v /data/mysql8/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 mysql<br>
# 以上的命令可以参考：https://hub.docker.com/_/mysql，里面有详细介绍<br>
</pre><br>
<h4>为什么要知道这么多路径或者参数</h4>每个中间件或者一个数据库容器，他可能需要有很多配置，例如密码，持久化文件的路径等等。那我们怎么知道路径是什么：<br>
<ol><li>可以进hub.docker.com找到自己需要的容器然后看文档</li><li>进容器找了（这个方法有点笨，笔者一开始就是这么找到的。）</li></ol><br>
<br><h3>网络</h3><h4>容器之间怎么进行通讯</h4>容器虽然是能相互通讯的，但是容器每次重启ip都跟上一次不一样，所以这样通讯会很复杂。<br>
<h4>示范</h4><pre class="prettyprint"># 先拉个CentOS镜像下来<br>
docker pull centos<br>
# 创建个容器<br>
docker run -d -it --name centos1 centos<br>
docker run -d -it --name centos2 centos<br>
<br>
docker inspect centos1_id<br>
</pre><br>
截取一些容器信息下来：<br>
<pre class="prettyprint">[<br>
&#123;<br>
    "NetworkSettings": &#123;<br>
        "Networks": &#123;<br>
            "bridge": &#123;<br>
                "IPAMConfig": null,<br>
                "Links": null,<br>
                "Aliases": null,<br>
                "NetworkID": "9e7ed6d29ca3474de04409833e39b7c7965c7c63d3a1f509886a7a998e4825f8",<br>
                "EndpointID": "41230bf523fac8fa4933989d98baaaa7655fba5c5dadd14e63839ffe868ed3f8",<br>
                "Gateway": "172.17.0.1",<br>
                "IPAddress": "172.17.0.4",<br>
                "IPPrefixLen": 16,<br>
                "IPv6Gateway": "",<br>
                "GlobalIPv6Address": "",<br>
                "GlobalIPv6PrefixLen": 0,<br>
                "MacAddress": "02:42:ac:11:00:04",<br>
                "DriverOpts": null<br>
            &#125;<br>
        &#125;<br>
    &#125;<br>
&#125;<br>
] <br>
</pre><br>
<pre class="prettyprint">docker inspect centos2_id<br>
</pre><br>
<pre class="prettyprint">[<br>
&#123;<br>
    "NetworkSettings": &#123;<br>
        "Networks": &#123;<br>
            "bridge": &#123;<br>
                "IPAMConfig": null,<br>
                "Links": null,<br>
                "Aliases": null,<br>
                "NetworkID": "9e7ed6d29ca3474de04409833e39b7c7965c7c63d3a1f509886a7a998e4825f8",<br>
                "EndpointID": "8ae77d46887c795983ee7a8fb96951d05e236b4ca4b4caa5d5964f892e18a476",<br>
                "Gateway": "172.17.0.1",<br>
                "IPAddress": "172.17.0.5",<br>
                "IPPrefixLen": 16,<br>
                "IPv6Gateway": "",<br>
                "GlobalIPv6Address": "",<br>
                "GlobalIPv6PrefixLen": 0,<br>
                "MacAddress": "02:42:ac:11:00:05",<br>
                "DriverOpts": null<br>
            &#125;<br>
        &#125;<br>
    &#125;<br>
&#125;<br>
] <br>
</pre><br>
<ul><li>以上centos1 ip为<strong>172.17.0.4</strong></li><li>以上centos2 ip为<strong>172.17.0.5</strong></li></ul><br>
<br><h4>解决问题</h4><pre class="prettyprint">docker network create centos-network<br>
docker run -d -it --network centos-network --name centos3 centos<br>
docker run -d -it --network centos-network --name centos4 centos<br>
docker exec -it centos3_id /bin/bash<br>
ping centos4 <br>
# 所以当创建了一个network后 容器都能加入到这个网络里面，很方便<br>
</pre><br>
这样就可以解决每次容器重启后ip不一致问题。<br>
<h3>小结</h3>其实在刚使用容器的时候会很麻烦：<br>
<ol><li>不知道Docker的命令和容器需要的参数</li><li>每次都要上官网找下有什么参数或者百度，但相比每次下载文件下来，进去配置省很多力气，并且配置一次保存好用过的命令，以后都可以用了，不需要再重复去改很多东西  </li><li>其实在一些小型公司，没有专业的运维的话尽量不要在生产环境上使用Docker，不然真的出现问题的话会很头疼，不仅仅要维护项目，还要维护Docker</li></ol><br>
<br>原文链接：<a href="https://juejin.cn/post/6974427129748389902" rel="nofollow" target="_blank">https://juejin.cn/post/6974427129748389902</a>，作者：Kakki
                                
                                                              
</div>
            