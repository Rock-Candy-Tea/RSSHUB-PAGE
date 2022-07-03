
---
title: 'trzsz-go 发布 v0.1.8 可以用 apt、yum 和 brew 安装啦'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3173'
author: 开源中国
comments: false
date: Sat, 02 Jul 2022 13:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3173'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftrzsz%2Ftrzsz" target="_blank">trzsz</a> ( trz / tsz ) <span style="background-color:#ffffff; color:#000000">是一个兼容 tmux 的文件传输工具，和 lrzsz ( rz /sz ) 类似，并且有进度条和支持目录传输，还支持拖目录或文件上传。</span></p> 
<hr> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftrzsz%2Ftrzsz-go" target="_blank">trzsz-go</a> v0.1.8 版本修复了一些小 bug，以及做了一些优化，重点是发布到了各大软件分发平台：</p> 
<p>1 、在 Ubuntu 用 apt 安装，Debian 也可以用 ppa:trzsz/ppa 这个源，详情可参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.desdelinux.net%2Fen%2Fcomo-agregar-repositorios-ppa-en-debian%2F" target="_blank">How to add PPA repositories in Debian</a></p> 
<p>sudo apt update && sudo apt install software-properties-common<br> sudo add-apt-repository ppa:trzsz/ppa && sudo apt update<br> sudo apt install trzsz</p> 
<hr> 
<p>2 、在 Fedora 、CentOS 或 RHEL 用 yum 安装</p> 
<p>echo '[trzsz]<br> name=Trzsz Repo<br> baseurl=https://yum.fury.io/trzsz/<br> enabled=1<br> gpgcheck=0' | sudo tee /etc/yum.repos.d/trzsz.repo</p> 
<p>sudo yum install trzsz</p> 
<hr> 
<p>3 、在 macOS 用 brew 安装</p> 
<p>brew update<br> brew install trzsz-go</p> 
<p><br> 其实，在 Linux 下也以用 Homebrew 的。</p> 
<hr> 
<p>4 、用法：</p> 
<p>4.1 、客户端和服务端都安装好 trzsz</p> 
<p>4.2 、在客户端使用 trzsz ssh xxx 登录</p> 
<p>4.3 、在服务端使用 trz 上传，使用 tsz xxx 下载</p> 
<p> </p>
                                        </div>
                                      
</div>
            