
---
title: 'Windows 11最新开发版右键点击开始菜单会崩溃 但可以用隐藏方法修复'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0226/971df78e5f9b654.png'
author: cnBeta
comments: false
date: Sat, 26 Feb 2022 05:34:12 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0226/971df78e5f9b654.png'
---

<div>   
在昨天推出的 Windows 11 Dev Build 22563 版中，微软并没有注意到任务栏用于判断平板模式的值设置有问题。所以在已知问题列表里微软没有提到资源管理器会崩溃，只不过这个问题太容易发现不知道为何测试时没注意到。当用户右键点击开始菜单时会瞬间卡死，然后资源管理器会被自动重启，蓝点网升级后测试发现触发率是 100%。<br>
 <p><strong>问题发生在哪：</strong></p><p>目前<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>已经知晓此问题不过暂时也没法直接修复，至少也要等到下周发布新的开发版时才能解决错误值的问题。测试发现该问题说起来其实非常简单，在新开发版中微软为平板电脑增加新的任务栏模式支持展开和自动隐藏。</p><p>而当用户右键点击开始菜单或使用 Win+X 触发时，系统会首先判断是否处于平板模式再根据设置显示不同样式，但微软在任务栏里预留的某个值是空的，于是系统引用该值时会报错，然后导致资源管理器直接崩溃再自动重启。</p><p>这也是为什么右键点击开始能百分百触发问题，有趣的是微软其实还在新版本里为开始按钮右键菜单设置新样式。蓝点网猜测微软工程师应该都使用的是新右键菜单样式，因为这个新样式并没有崩溃，所以微软没有注意到这个如此明显的 BUG。</p><p><strong>新右键菜单样式是这样的：</strong></p><p><a href="https://img.lancdn.com/landian/2022/02/92750-1.png"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0226/971df78e5f9b654.png"><img data-original="https://static.cnbetacdn.com/article/2022/0226/971df78e5f9b654.png" src="https://static.cnbetacdn.com/thumb/article/2022/0226/971df78e5f9b654.png" referrerpolicy="no-referrer"></a></p><p><strong>用ViveTool开启新样式：</strong></p><p>如果你从未使用过ViveTool请先点击这里下载：<a href="https://www.landian.vip/archives/92272.html">[图文</a><a data-link="1" href="https://c.duomai.com/track.php?k=iRyUSQzUycwRHdo1Ddm0DZpVXZmkDN2ITPklWYmYDO5IDNy0DZp9VZ0l2cmUmchdHdm92cGJTJjZkMl42Yu02bj5SZy9GdzRnZvN3byNWat5yd3dnRyU" target="_blank">教程</a>] <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11开发版必备神器 ViveTool 到底怎么用？ 下载解压后打开管理员模式的命令提示符执行以下命令即可开启新的右键菜单样式，经测试可正常使用不会崩溃。<strong>操作完成后初次右键点击开始菜单时资源管理器还会崩溃，当资源管理器自动重启后新样式出现便不再崩溃可以使用右键点击或 Win+X 快捷键。</strong></p><p>#管理员模式的命令提示符里执行此命令</p><p>.\vivetool addconfig 26008830 2</p><p>#如需禁用则使用此命令删除新特性</p><p>.\vivetool delconfig 26008830 2</p><p><strong>以上操作配图如下：</strong></p><p><a href="https://img.lancdn.com/landian/2022/02/92750-2.png"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0226/4935c17eb86ed87.png"><img data-original="https://static.cnbetacdn.com/article/2022/0226/4935c17eb86ed87.png" src="https://static.cnbetacdn.com/thumb/article/2022/0226/4935c17eb86ed87.png" referrerpolicy="no-referrer"></a></p>   
</div>
            