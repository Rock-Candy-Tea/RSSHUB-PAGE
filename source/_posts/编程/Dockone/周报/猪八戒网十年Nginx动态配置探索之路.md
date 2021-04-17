
---
title: '猪八戒网十年Nginx动态配置探索之路'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210416/a8efd261b5c028d693e24c2fb6023644.png'
author: Dockone
comments: false
date: 2021-04-17 12:09:42
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210416/a8efd261b5c028d693e24c2fb6023644.png'
---

<div>   
<br><h3>关于Nginx</h3>Nginx（engine X）是一款开源的Web服务器软件，因其具有性能稳定、高并发、低内存耗用、高性能的处理能力等特点而闻名。该软件由Igor Sysoev创建并于2004年首次公开发布，Nginx实现了Web服务器的基本功能，用户通过简单的配置指令就能快速完成Web服务器的搭建，它还是一款四七层负载均衡代理软件，支持TCP/UDP、FastCGI、uwsgi、 SCGI、gRPC等协议，并且支持很多第三方的模块扩展。<br>
<h3>约十年前，猪八戒Nginx的使用</h3>在2011年初的时候，猪八戒网就已经开始使用Nginx了，我们使用Nginx的场景也特别简单，仅仅只是用于HTTP/HTTPS协议的反向代理转发，我记得当时的Nginx运行版本是0.8.x，还不支持TCP/UDP、WebSocket、gRPC等协议。那时我们的服务器都是物理机，扳起手指都能数过来，而且就只有测试环境与生产环境，几乎都是通过手动进行运维，所以都是在服务器上直接进行Nginx配置操作。<br>
<br>那时的Nginx架构很简单，如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210416/a8efd261b5c028d693e24c2fb6023644.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210416/a8efd261b5c028d693e24c2fb6023644.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
测试环境Nginx配置：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210416/d5235b0e44bd1cfa061020e734fe65db.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210416/d5235b0e44bd1cfa061020e734fe65db.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
生产环境Nginx配置：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210416/282c909e03ac640a9c1b03537280aa85.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210416/282c909e03ac640a9c1b03537280aa85.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>约五年前，猪八戒Nginx的使用</h3>但随着业务访问量的直线增长，猪八戒网的应用、研发人员都出现了很大规模的增长。伴随着很多问题也出现了，从单（机房）数据中心变为多（机房）数据中心，2个环境变为多个环境（最多高达20个+），原来运行在物理机上的应用也迁移到虚拟机或容器上，如果还按照原来的手工模式维护几十个NginxConf配置，将导致环境差异性、Nginx配置不可移植、操作繁琐且容易出错、而且维护成本高。<br>
<br>那时每个数据中心每个环境都有独立的nginx配置，如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210416/465d77bac8df6cb3f4f7b1ff2d4e9e09.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210416/465d77bac8df6cb3f4f7b1ff2d4e9e09.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>开始探索自动适配多数据中心多环境多版本的Nginx配置</h3>针对以上情况的问题，我们该怎么实现一份Nginx配置如何能够自动适配多数据中心多环境多版本？  <br>
<br>下图是我们想要的实现的效果。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210416/207a4baa75588ec83cea8de316dbcaaf.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210416/207a4baa75588ec83cea8de316dbcaaf.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
其实Nginx官方有种解决方案是将DNS用于Nginx的服务发现，但是缺失Upstream的管理，我们就放弃这个方案了。如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210416/329b9b7cbc775db03fd9b8f87af3af38.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210416/329b9b7cbc775db03fd9b8f87af3af38.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
经过我们多次测试，发现仅仅通过Nginx配置是无法实现这个需求的，要么自己开发Nginx模块来实现，但是需要用C语言开发，而且用C语言开发模块必须要熟悉Nginx的源代码，使得我们对其望而生畏。于是在google搜索有没有符合我们需求的开源的第三方nginx模块，经过半天的时间调研，终于找到了一款ngx_lua模块符合我们的需求。<br>
<h4>什么是ngx_lua？</h4>ngx_lua是Nginx的一个模块，将Lua嵌入到Nginx中，采用Lua脚本实现业务逻辑，由于Lua的紧凑、快速以及内建协程，所以在保证高并发服务能力的同时极大地降低了业务逻辑实现成本。<br>
<h4>实现方式</h4><strong>1、定义“数据中心”、“环境”、“版本”三个环境系统变量，变量名暂定为：DC、DC_ENV、DC_VER</strong><br>
<ul><li>DC表示这台系统所在的（北京廊坊、天津华苑）数据中心；</li><li>DC_ENV表示这台系统所处的（开发、测试、预发布、生产等）环境；</li><li>DC_VER表示这台系统代理的应用版本（默认为latest）；</li></ul><br>
<br><strong>2、Nginx Server配置将测试域名、正式域名与应用进行关联，应用名变量暂定$target。</strong><br>
<ul><li>测试域名为什么是正则匹配？因为运行环境特别多，测试域名都不一样，例：<a href="http://www.t1.zbjtest.com/" rel="nofollow" target="_blank">www.t1.zbjtest.com</a>、<a href="http://www.test.zbjtest.com/" rel="nofollow" target="_blank">www.test.zbjtest.com</a></li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210416/88d5a5a5e587815f89848c7fae3fb8c4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210416/88d5a5a5e587815f89848c7fae3fb8c4.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>3、制定应用关联Upstream的命名规范，我们协定以“应用名+数据中心+环境+版本”进行命名。</strong><br>
<ul><li>Upstream：www_bjlf_test_latest表示应用“www”运行在北京廊坊测试环境的最新版本；</li><li>Upstream：www_bjlf_prod_latest表示应用“www”运行在北京廊坊生产环境的最新版本；</li><li>Upstream：www_bjlf_prod_v2表示应用“www”运行在北京廊坊测试环境的v2版本；</li></ul><br>
<br><strong>4、配置nginx.conf，加载“DC”、“DC_ENV”、“DC_VER”系统变量，定义加载Lua代码路径</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210416/363f5f82fe9b172ade1bdf044ece0188.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210416/363f5f82fe9b172ade1bdf044ece0188.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>5、当Nginx启动的时候，init_by_lua_file阶段会将DC、DC_ENV、DC_VER加载到Lua内存中</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210416/581f767b1759b518339d73a7df242faf.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210416/581f767b1759b518339d73a7df242faf.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>6、当用户请求<a href="http://www.zbj.com/" rel="nofollow" target="_blank">www.zbj.com</a>的时候，执行rewrite_by_lua_file阶段将根据target、DC、DC_ENV、DC_VER封装应用的Upstream名称，这样就能代理转发了。</strong><br>
<ul><li>关于Upstream是如何注册到nginx中，我们是基于Consul + ngx_http_dyups_module来实现的。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210416/5b4e18265b65f637ae6793b657885816.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210416/5b4e18265b65f637ae6793b657885816.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这样一份Nginx配置就能适配多个数据中心多个环境多个版本了，这样大大<strong>降低Nginx冗余配置，并保证环境一致性。</strong><br>
<br>本文主要阐述如何利用ngx_lua的init_by_lua_file与rewrite_by_lua_file阶段来简单实现<strong>Nginx配置适配多数据中心多环境多版本的功能</strong>，还能用ngx_lua实现waf、灰度发布、服务发现、动态限速等功能，关于ngx_lua的更多特性，可以参考官方文档。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/w2e910zGPpbfyjUG-XsMQw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/w2e910zGPpbfyjUG-XsMQw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            