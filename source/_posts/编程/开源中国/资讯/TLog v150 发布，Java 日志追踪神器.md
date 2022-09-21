
---
title: 'TLog v1.5.0 发布，Java 日志追踪神器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-97d31b0adbcdaa18e8c270bb8bd7e251ea6.png'
author: 开源中国
comments: false
date: Wed, 21 Sep 2022 06:25:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-97d31b0adbcdaa18e8c270bb8bd7e251ea6.png'
---

<div>   
<div class="content">
                                                                                            <p><img height="383" src="https://oscimg.oschina.net/oscnet/up-97d31b0adbcdaa18e8c270bb8bd7e251ea6.png" width="900" referrerpolicy="no-referrer"></p> 
<h2><span>一</span></h2> 
<p style="color:black; margin-left:0; margin-right:0">TLog 1.5.0版本正式发布！</p> 
<p style="color:black; margin-left:0; margin-right:0">TLog是一款Java日志追踪神器，10分钟即可让你的系统日志变的可追踪。</p> 
<p style="color:black; margin-left:0; margin-right:0">如果你是第一次知道TLog这款框架，可以移步以下链接进行了解：</p> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">官网：https://tlog.yomahub.com/</p> 
 <p style="color:black; margin-left:0; margin-right:0">Gitee仓库主页：https://gitee.com/dromara/TLog</p> 
 <p style="color:black; margin-left:0; margin-right:0">Github仓库主页：https://github.com/dromara/TLog</p> 
</blockquote> 
<p style="color:black; margin-left:0; margin-right:0">TLog从1.4.3开始，停更了一段时间。主要原因是精力不够，时间都花在了另外一个开源项目上。况且TLog的核心功能相对来说比较稳定，更多的issue是关于其他框架的支持，在整个微服务生态圈里，TLog后续做的一些事情就是在不停的增加对其他框架的支持。</p> 
<p style="color:black; margin-left:0; margin-right:0">所以就导致了：虽然TLog很小巧，核心代码没多少，但是TLog的模块却异常的多，达到了30个模块（其实每个模块也就1到2个类）。</p> 
<p><img height="1442" src="https://oscimg.oschina.net/oscnet/up-c58a83763a863370fc197020e20f2875620.png" width="1298" referrerpolicy="no-referrer"></p> 
<p style="color:black; margin-left:0; margin-right:0">而且涉及的场景非常多，因为是在微服务中靠日志打印来测试，测试用例不能完全mock掉，导致了无法做标准的测试用例，可能是我功力还不到家，所以只能依靠做测试工程来测试。TLog的测试工程项目有43个之多：</p> 
<p><img height="850" src="https://oscimg.oschina.net/oscnet/up-38b53735f2c8756b219f6f71e80de3bffe3.png" width="776" referrerpolicy="no-referrer"></p> 
<h1><span>二</span></h1> 
<p style="color:black; margin-left:0; margin-right:0">其实说了那么多，TLog 1.5.0版本并没有增加新的特性。</p> 
<p style="color:black; margin-left:0; margin-right:0">之前有很多小伙伴和我说，TLog有些传递依赖存在一些安全漏洞，因为TLog的部署需要在每个项目上进行设置，所以没法在公司通过安全方面的审核。</p> 
<p style="color:black; margin-left:0; margin-right:0">这个版本是一个干净安全的版本，在1.5.0里，升级了大量的不安全依赖包。减少了很多传递依赖。</p> 
<p style="color:black; margin-left:0; margin-right:0">并且在墨菲安全(https://www.murphysec.com/)的检测中，达到了0安全风险的级别。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.murphysec.com%2Fdr%2FCdCESbnNhZl2PtD65A" target="_blank"><img alt="OSCS Status" src="https://www.oscs1024.com/platform/badge/dromara/TLog.git.svg?size=large" referrerpolicy="no-referrer"></a></p> 
<p>OSCS Status</p> 
<h2><span>三</span></h2> 
<p style="color:black; margin-left:0; margin-right:0">有细心的小伙伴也发现了，TLog同时也升级了官网，换了一种风格。之前的暗黑色+黄色系的组合被很多小伙伴诟病。看多了，眼睛容易疲劳，对比度太高。</p> 
<p style="color:black; margin-left:0; margin-right:0">现在TLog的官网采用了比较沉稳的色调，支持三种颜色主题。更加清新了一些。希望你们阅读体验会更加好。</p> 
<p><img height="1770" src="https://oscimg.oschina.net/oscnet/up-bdac8b43e07d0ca3309eafabb8bdec3921a.png" width="2778" referrerpolicy="no-referrer"></p> 
<h2><span>四</span></h2> 
<p style="color:black; margin-left:0; margin-right:0">有想加入社区的小伙伴，或者想进行贡献的小伙伴，在这里能找到加入社区的方法：</p> 
<p style="color:black; margin-left:0; margin-right:0">https://tlog.yomahub.com/pages/73c2c3/</p>
                                        </div>
                                      
</div>
            