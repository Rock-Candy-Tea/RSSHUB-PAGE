
---
title: 'FireFox火狐浏览器无法上网原因查明：程序员大小写搞错了'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220115/b9154c07-19f5-4dd3-a404-0730967188e8.jpg'
author: 快科技（原驱动之家）
comments: false
date: Sat, 15 Jan 2022 20:08:45 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220115/b9154c07-19f5-4dd3-a404-0730967188e8.jpg'
---

<div>   
<p class="MsoNormal">最近两天，在用<span lang="EN-US">FireFox</span>火狐浏览器的用户可能会出现无法连接上网的问题，起初以为是新版升级的问题，还有人怪罪于<span lang="EN-US">Win</span>系统，然而现在问题查明了，是火狐自己的问题，程序员将部分代码的大小写搞错了。</p>
<p class="MsoNormal">火狐浏览器前几天发布了<span lang="EN-US">96.0</span>版，说是大幅减少了主线程负载，意味着可以明显降低对系统资源的占用，运行更快速、更流畅。</p>
<p class="MsoNormal">然而很多人升级之后发现无法连接上网，后面就排查了一系列问题，首先以为真凶是<span lang="EN-US">FireFox 96.0</span>新版，结果发现<span lang="EN-US">FireFox 95</span>及之前的版本也有问题。</p>
<p class="MsoNormal">还有原因归罪于<span lang="EN-US">Windows</span>系统的补丁升级，结果也不是，另外还找了<span lang="EN-US">DNS</span>、云服务商等原因，也排除了。</p>
<p class="MsoNormal"><strong>最后发现问题跟<span lang="EN-US">FireFox</span>的<span lang="EN-US">HTTP3</span>有关，</strong>禁用之后就可以上网，真凶现在找到了，但到底是哪里的问题？<span lang="EN-US">Mozilla </span>基金会最后找到根源了——跟代码大小写有关。</p>
<p class="MsoNormal">据官方介绍，在解析<span lang="EN-US">HTTP</span>标头时，<span lang="EN-US">FireFox</span>会用一个函数结束，<span style="color:#ff0000;"><strong>该函数通常只处理大写的字段，如果是小写的字母那就会无法计算标头长度，从而导致<span lang="EN-US">FireForx</span>代码陷入无限循环中。</strong></span></p>
<p class="MsoNormal">找到问题之后，修复错误的过程也很简单，未来这个代码不会再区分大小写了。</p>

<p class="MsoNormal" style="text-align: center;"><img alt="FireFox火狐浏览器无法上网原因查明：程序员大小写搞错了" h="330" src="https://img1.mydrivers.com/img/20220115/b9154c07-19f5-4dd3-a404-0730967188e8.jpg" style="text-align: center; border: 1px solid black;" w="600" referrerpolicy="no-referrer"></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/daima.htm"><i>#</i>代码</a><a href="https://news.mydrivers.com/tag/huohu.htm"><i>#</i>火狐</a></p>
<p class="url">
     
<span>责任编辑：宪瑞</span>
</p>
        
</div>
            