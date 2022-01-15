
---
title: 'Firefox无法上网原因查明：程序员搞错大小写'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0115/e054be59b394e23.jpg'
author: cnBeta
comments: false
date: Sat, 15 Jan 2022 12:19:19 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0115/e054be59b394e23.jpg'
---

<div>   
最近两天，在用FireFox火狐浏览器的用户可能会出现无法连接上网的问题，起初以为是新版升级的问题，还有人怪罪于Win系统，然而现在问题查明了，是火狐自己的问题，程序员将部分代码的大小写搞错了。<br>
 <p>Firefox浏览器前几天发布了96.0版，说是大幅减少了主线程负载，意味着可以明显降低对系统资源的占用，运行更快速、更流畅。</p><p>然而很多人升级之后发现无法连接上网，后面就排查了一系列问题，首先以为真凶是Firefox 96.0新版，结果发现Firefox 95及之前的版本也有问题。</p><p>还有原因归罪于<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>系统的补丁升级，结果也不是，另外还找了DNS、云服务商等原因，也排除了。</p><p><strong>最后发现问题跟Firefox的HTTP3有关，</strong>禁用之后就可以上网，真凶现在找到了，但到底是哪里的问题？Mozilla 基金会最后找到根源了——跟代码大小写有关。</p><p>据官方介绍，在解析HTTP标头时，Firefox会用一个函数结束，<strong>该函数通常只处理大写的字段，如果是小写的字母那就会无法计算标头长度，从而导致FireForx代码陷入无限循环中。</strong></p><p>找到问题之后，修复错误的过程也很简单，未来这个代码不会再区分大小写了。</p><p><img src="https://static.cnbetacdn.com/article/2022/0115/e054be59b394e23.jpg" referrerpolicy="no-referrer"></p>   
</div>
            