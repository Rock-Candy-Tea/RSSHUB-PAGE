
---
title: '【重磅官宣】KMRE 升级版发布，支持自定义安装安卓软件！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://imcn.me/wp-content/uploads/2021/09/1630895367893267.png'
author: 开源中国
comments: false
date: Mon, 06 Sep 2021 03:10:00 GMT
thumbnail: 'https://imcn.me/wp-content/uploads/2021/09/1630895367893267.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start">Linux 桌面操作系统下的应用生态短板一直都是比较严峻的问题，麒麟移动运行环境（KMRE）的上线使得优麒麟的应用生态不再局限于桌面端。此前，为了保证用户体验，KMRE 下的所有安卓软件只能通过软件商店和软件源进行统一管理。</p> 
<p style="text-align:start">现在，万众瞩目的 Kmre Apk 安装器 终于诞生了！不仅支持<strong>双击安装本地 Apk 包</strong>，还支持<strong>拖拽和选择文件进行安装</strong>，从此实现 Linux 系统下 Apk 包安装自由！</p> 
<p style="text-align:start">先看结论（以开心消消乐为例）：</p> 
<p><img alt="优麒麟（Ubuntu Kylin）" height="720" src="https://imcn.me/wp-content/uploads/2021/09/1630895367893267.png" style="margin-left:auto; margin-right:auto" width="1280" referrerpolicy="no-referrer"><img alt="优麒麟（Ubuntu Kylin）" height="720" src="https://imcn.me/wp-content/uploads/2021/09/1630895435883524.png" style="margin-left:auto; margin-right:auto" width="1280" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p><img alt="优麒麟（Ubuntu Kylin）" height="720" src="https://imcn.me/wp-content/uploads/2021/09/1630895389163810.png" style="margin-left:auto; margin-right:auto" width="1280" referrerpolicy="no-referrer"></p> 
<p><img alt="优麒麟（Ubuntu Kylin）" height="720" src="https://imcn.me/wp-content/uploads/2021/09/1630895410321384.png" style="margin-left:auto; margin-right:auto" width="1280" referrerpolicy="no-referrer"></p> 
<p>别急别急，安装方式在此：</p> 
<p><strong>安装方式</strong></p> 
<p style="text-align:start">一、万变不离其宗，让我们先更新系统：</p> 
<p style="text-align:start">1. 未安装优麒麟的用户请先前往官网下载镜像文件；</p> 
<p style="text-align:start">2. 已安装 20.04 和 20.04 Pro 正式版的用户通过以下方式进行源更新和系统升级：</p> 
<blockquote> 
 <p>$ sudo apt update $ sudo apt full-upgrade</p> 
</blockquote> 
<p style="text-align:start"> </p> 
<p style="text-align:start">二、安装麒麟移动运行环境：</p> 
<p style="text-align:start">（1）下载 deb 包并安装，从而添加 software 软件源（已经添加过的忽略此步骤）：</p> 
<blockquote> 
 <p>$ wget http://archive.ubuntukylin.com/ubuntukylin/pool/main/k/kylin-software-keyring/kylin-software-keyring_2021.04.21_all.deb</p> 
 <p>$ sudo dpkg -i kylin-software-keyring_2021.04.21_all.deb</p> 
 <p> </p> 
</blockquote> 
<p style="text-align:start">（2） 安装内核头文件包、KMRE 环境、Apk 安装器并重启：</p> 
<blockquote> 
 <p>$ sudo apt install linux-headers-`uname -r`</p> 
 <p>$ sudo apt install kmre kmre-apk-installer</p> 
 <p>$ reboot</p> 
</blockquote> 
<p style="text-align:start"> </p> 
<p style="text-align:start"><strong>使用须知</strong></p> 
<ol> 
 <li>关于 CPU 型号支持：目前支持 Intel、AMD、海光、兆芯四款型号的 CPU。</li> 
 <li>关于 GPU 型号支持：目前在大部分 Intel 集成显卡，AMD，NVIDIA 显卡上支持运行，且稳定性较好，硬件加速效率也高，部分老旧显卡可能不支持默认的渲染模式，用户可以自己根据显卡型号配置对应的渲染模式。</li> 
 <li>关于内核：目前在 5.4、5.8、5.10 内核上支持较好，切换内核后，请务必安装相应的头文件包。</li> 
</ol> 
<p style="text-align:start"> </p> 
<p style="text-align:start">欢迎大家多多反馈使用 Kmre Apk 安装器中遇到的问题，可能你的宝藏应用还没有被小优发现，请你不要吝啬地大声说出来~</p>
                                        </div>
                                      
</div>
            