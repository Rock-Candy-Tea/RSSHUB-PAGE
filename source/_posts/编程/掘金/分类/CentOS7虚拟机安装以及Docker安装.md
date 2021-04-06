
---
title: 'CentOS7虚拟机安装以及Docker安装'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb6b01c7b4494f6b9f431ee44319cbef~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 19:57:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb6b01c7b4494f6b9f431ee44319cbef~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>step1: 进入下载页，选择阿里云站点进行下载</p>
<p>阿里云站点：<a href="http://mirrors.aliyun.com/centos/7/isos/x86_64/" target="_blank" rel="nofollow noopener noreferrer">mirrors.aliyun.com/centos/7/is…</a></p>
<p>每个链接都包括了镜像文件的地址、类型及版本号等信息</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb6b01c7b4494f6b9f431ee44319cbef~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>各个版本的ISO镜像文件说明：</p>
<p>CentOS-7-x86_64-DVD-1708.iso               标准安装版（推荐）</p>
<p>CentOS-7-x86_64-Everything-1708.iso        完整版，集成所有软件（以用来补充系统的软件或者填充本地镜像）</p>
<p>CentOS-7-x86_64-LiveGNOME-1708.iso         GNOME桌面版  </p>
<p>CentOS-7-x86_64-LiveKDE-1708.iso           KDE桌面版  </p>
<p>CentOS-7-x86_64-Minimal-1708.iso           精简版，自带的软件最少</p>
<p>CentOS-7-x86_64-NetInstall-1708.iso        网络安装版（从网络安装或者救援系统）</p>
<p><strong>在virtual box上安装虚拟机的过程,大家可以百度</strong></p>
<p>我是虚拟机装的Centos7，linux 3.10 内核，docker官方说至少3.8以上，建议3.10以上（ubuntu下要linux内核3.8以上， RHEL/Centos 的内核修补过， centos6.5的版本就可以——这个可以试试）</p>
<p>1，root账户登录，查看内核版本如下
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0aecf1b129234a8f9a210539611e1333~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>2，把yum包更新到最新（温馨提示：新环境或测试环境可随意操作，生产环境酌情慎重更新）</p>
<pre><code class="hljs language-bash copyable" lang="bash">[root@localhost ~]<span class="hljs-comment"># yum update</span>
已加载插件：fastestmirror
Loading mirror speeds from cached hostfile
 * base: centos.ustc.edu.cn
 * extras: mirrors.aliyun.com
 * updates: mirrors.cn99.com
base                                                                                                  | 3.6 kB  00:00:00     
extras                                                                                                | 3.4 kB  00:00:00     
updates                                                                                               | 3.4 kB  00:00:00     
正在解决依赖关系
--> 正在检查事务
---> 软件包 NetworkManager.x86_64.1.1.12.0-6.el7 将被 升级
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（期间要选择确认，输入 y 即可）</p>
<p>3，安装需要的软件包， yum-util 提供yum-config-manager功能，另外两个是devicemapper驱动依赖的</p>
<pre><code class="hljs language-bash copyable" lang="bash">[root@localhost /]<span class="hljs-comment"># yum install -y yum-utils device-mapper-persistent-data lvm2</span>
已加载插件：fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.tuna.tsinghua.edu.cn
 * extras: mirrors.tuna.tsinghua.edu.cn
 * updates: mirrors.tuna.tsinghua.edu.cn
软件包 device-mapper-persistent-data-0.8.5-3.el7_9.2.x86_64 已安装并且是最新版本
软件包 7:lvm2-2.02.187-6.el7_9.4.x86_64 已安装并且是最新版本
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4，设置yum源（选择其中一个）</p>
<p><code>yum-config-manager --add-repo http://download.docker.com/linux/centos/docker-ce.repo</code>（中央仓库）</p>
<p><code>yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo</code>（阿里仓库）</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0761108432544c79b66b4d42c3822acc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>5，可以查看所有仓库中所有docker版本，并选择特定版本安装</p>
<pre><code class="hljs language-bash copyable" lang="bash">[root@localhost /]<span class="hljs-comment"># yum list docker-ce --showduplicates | sort -r</span>
已加载插件：fastestmirror
可安装的软件包
 * updates: mirrors.tuna.tsinghua.edu.cn
Loading mirror speeds from cached hostfile
 * extras: mirrors.tuna.tsinghua.edu.cn
docker-ce.x86_64            3:20.10.5-3.el7                     docker-ce-stable
docker-ce.x86_64            3:20.10.4-3.el7                     docker-ce-stable
docker-ce.x86_64            3:20.10.3-3.el7                     docker-ce-stable
docker-ce.x86_64            3:20.10.2-3.el7                     docker-ce-stable
docker-ce.x86_64            3:20.10.1-3.el7                     docker-ce-stable
docker-ce.x86_64            3:20.10.0-3.el7                     docker-ce-stable
docker-ce.x86_64            3:19.03.9-3.el7                     docker-ce-stable
docker-ce.x86_64            3:19.03.8-3.el7                     docker-ce-stable
docker-ce.x86_64            3:19.03.7-3.el7                     docker-ce-stable
docker-ce.x86_64            3:19.03.6-3.el7                     docker-ce-stable
docker-ce.x86_64            3:19.03.5-3.el7                     docker-ce-stable
docker-ce.x86_64            3:19.03.4-3.el7                     docker-ce-stable
docker-ce.x86_64            3:19.03.3-3.el7                     docker-ce-stable
docker-ce.x86_64            3:19.03.2-3.el7                     docker-ce-stable
docker-ce.x86_64            3:19.03.15-3.el7                    docker-ce-stable
docker-ce.x86_64            3:19.03.14-3.el7                    docker-ce-stable
docker-ce.x86_64            3:19.03.1-3.el7                     docker-ce-stable
docker-ce.x86_64            3:19.03.13-3.el7                    docker-ce-stable
docker-ce.x86_64            3:19.03.12-3.el7                    docker-ce-stable
docker-ce.x86_64            3:19.03.11-3.el7                    docker-ce-stable
docker-ce.x86_64            3:19.03.10-3.el7                    docker-ce-stable
docker-ce.x86_64            3:19.03.0-3.el7                     docker-ce-stable
docker-ce.x86_64            3:18.09.9-3.el7                     docker-ce-stable
docker-ce.x86_64            3:18.09.8-3.el7                     docker-ce-stable
docker-ce.x86_64            3:18.09.7-3.el7                     docker-ce-stable
docker-ce.x86_64            3:18.09.6-3.el7                     docker-ce-stable
docker-ce.x86_64            3:18.09.5-3.el7                     docker-ce-stable
docker-ce.x86_64            3:18.09.4-3.el7                     docker-ce-stable
docker-ce.x86_64            3:18.09.3-3.el7                     docker-ce-stable
docker-ce.x86_64            3:18.09.2-3.el7                     docker-ce-stable
docker-ce.x86_64            3:18.09.1-3.el7                     docker-ce-stable
docker-ce.x86_64            3:18.09.0-3.el7                     docker-ce-stable
docker-ce.x86_64            18.06.3.ce-3.el7                    docker-ce-stable
docker-ce.x86_64            18.06.2.ce-3.el7                    docker-ce-stable
docker-ce.x86_64            18.06.1.ce-3.el7                    docker-ce-stable
docker-ce.x86_64            18.06.0.ce-3.el7                    docker-ce-stable
docker-ce.x86_64            18.03.1.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            18.03.0.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.12.1.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.12.0.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.09.1.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.09.0.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.06.2.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.06.1.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.06.0.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.03.3.ce-1.el7                    docker-ce-stable
docker-ce.x86_64            17.03.2.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.03.1.ce-1.el7.centos             docker-ce-stable
docker-ce.x86_64            17.03.0.ce-1.el7.centos             docker-ce-stable
 * base: mirrors.tuna.tsinghua.edu.cn
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6，安装Docker，命令：yum install docker-ce-版本号，我选的是docker-ce-18.03.1.ce，如下</p>
<pre><code class="hljs language-bash copyable" lang="bash">[root@localhost /]<span class="hljs-comment"># yum install docker-ce-18.03.1.ce</span>
已加载插件：fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.tuna.tsinghua.edu.cn
 * extras: mirrors.tuna.tsinghua.edu.cn
 * updates: mirrors.tuna.tsinghua.edu.cn
正在解决依赖关系
--> 正在检查事务
---> 软件包 docker-ce.x86_64.0.18.03.1.ce-1.el7.centos 将被 安装
--> 正在处理依赖关系 container-selinux >= 2.9，它被软件包 docker-ce-18.03.1.ce-1.el7.centos.x86_64 需要
--> 正在处理依赖关系 pigz，它被软件包 docker-ce-18.03.1.ce-1.el7.centos.x86_64 需要
--> 正在处理依赖关系 libcgroup，它被软件包 docker-ce-18.03.1.ce-1.el7.centos.x86_64 需要
--> 正在处理依赖关系 libltdl.so.7()(64bit)，它被软件包 docker-ce-18.03.1.ce-1.el7.centos.x86_64 需要
--> 正在检查事务
---> 软件包 container-selinux.noarch.2.2.119.2-1.911c772.el7_8 将被 安装
<span class="copy-code-btn">复制代码</span></code></pre>
<p>7， 启动Docker，命令：systemctl start docker，然后加入开机启动，如下</p>
<pre><code class="hljs language-bash copyable" lang="bash">[root@localhost /]<span class="hljs-comment"># systemctl start docker</span>
[root@localhost /]<span class="hljs-comment"># docker -v</span>
Docker version 18.03.1-ce, build 9ee9f40

[root@localhost /]<span class="hljs-comment"># systemctl enable docker</span>
Created symlink from /etc/systemd/system/multi-user.target.wants/docker.service to /usr/lib/systemd/system/docker.service.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此<code>docker</code>已经成功安装到了<code>Centos7</code>上了</p>
<p>我是南飞雁，你可以叫我飞雁，我是一名奋斗者，在实现财富自由的路上……</p>
<p>我喜欢分享，也喜欢思考；我有自己的人生规划和梦想；但有时也很迷茫……</p>
<p>我从事IT行业，研究的技术领域相对比较多而杂： PHP、MySQL、Linux、JavaScript、Node.js、NoSQL、PhotoShop、音视频处理、架构集群、网络通信、生活技巧、人生三观、做人做事读书……</p>
<p>我总是会在自己的公众号和掘金上写下自己的所思所想和近期要做的事，希望你关注我，我是一个奋斗者，我叫南飞雁</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            