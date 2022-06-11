
---
title: 'trzsz-go v0.1.6 实现_拖文件自动上传到远程服务器_'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ba03f80af455778dd8987f15a14c3fa1f33.gif'
author: 开源中国
comments: false
date: Sat, 11 Jun 2022 12:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ba03f80af455778dd8987f15a14c3fa1f33.gif'
---

<div>   
<div class="content">
                                                                                            <p>trzsz-go v0.1.6 实现“拖文件自动上传到远程服务器”，用法如下：</p> 
<p>1、在本地使用 trzsz -d ssh x.x.x.x 登录服务器。加 -d 是开启拖文件上传功能，默认是不开启的。</p> 
<p>2、将 trz 和 tsz 放到服务器某个 PATH 目录下，要有可执行权限。执行命令 trz -v 不会报错即可。</p> 
<p>在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftrzsz%2Ftrzsz-go%2Freleases" target="_blank">Release</a> 中下载的 zip 里就是三个 trzsz、trz、tsz 可执行程序，也可以自己 clone 下来 make 编译。</p> 
<hr> 
<p>在 Mac 上拖文件的效果如图（ 非拖文件的效果请参考软件介绍）：</p> 
<p><img height="500" src="https://oscimg.oschina.net/oscnet/up-ba03f80af455778dd8987f15a14c3fa1f33.gif" width="800" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p>踩坑指南（特别是 Windows ）：</p> 
<p>1 、trzsz ssh 时记得加上 -d 或 --dragfile，如 trzsz -d ssh x.x.x.x。</p> 
<p>2 、记得将 trz 放到远程服务器某个 PATH 目录下，要有可执行权限。</p> 
<p>3 、在 Windows 的 cmd 、PowerShell 、Terminal 上，标题不要有“管理员”，即不要“以管理员身份运行”它们，要不然可能拖不了文件。在我的电脑上 Terminal 总是以管理员运行，后来设置一下 UAC 重启电脑就好了。</p> 
<p>4 、在 Windows 的 cmd 、PowerShell 中，拖多个文件进去，也只有一个文件生效的（ 鼠标指向那个 ）。</p> 
<p>5 、在 Windows 的 Terminal 中，要拖文件到左上角，出现“粘贴文件路径”时再放开鼠标，要不然没用。</p>
                                        </div>
                                      
</div>
            