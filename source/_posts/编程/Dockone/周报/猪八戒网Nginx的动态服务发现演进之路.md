
---
title: '猪八戒网Nginx的动态服务发现演进之路'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210720/d75018f1e1a886649b04bcc4a0e4afab.png'
author: Dockone
comments: false
date: 2021-07-21 14:06:37
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210720/d75018f1e1a886649b04bcc4a0e4afab.png'
---

<div>   
<br>【编者的话】随着业务访问量的直线增长，业务项目数量也越来越多，期间各个业务项目的频繁上线、回滚、动态扩容与缩容等，促使了微服务架构的流行，又新引入了容器化部署发布方式，当容器发布及重建的时候，实例IP将会发生变化，如果我们还是继续通过手工维护后端的Upstream配置，将导致Upstream配置不可维护，且Nginx频繁reload会造成QPS波动。本文将分为四个阶段来叙述猪八戒网这十年Nginx的动态服务发现演进之路。<br>
<h3>阶段一：手工配置</h3>早期猪八戒网的应用较少、架构简单，业务项目都是运行在虚拟机或物理机上，都是通过手工配置Nginx后端应用的Upstream文件，然后进行nginx -s reload。如图1：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210720/d75018f1e1a886649b04bcc4a0e4afab.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210720/d75018f1e1a886649b04bcc4a0e4afab.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图1：手工配置</em><br>
<h3>阶段二：自动配置（渲染模板）</h3>中期业务应用越来越多，但那时容器化还没普及，所以我们还是基于物理机或虚拟机部署方式上线，期间CMDB系统也基本上开发完成，自动化部署基于puppet实现了项目支持物理机、虚拟机的代码发布，而且在CMDB中关联了项目与实例的对应关系，因为物理机与虚拟机部署触发更新Upstream只会作用于新建和删除的阶段，不会频繁的reload nginx，当时就采样了渲染Upstream模板方式集成到CMDB中，在这个阶段，服务的发现与注册、自动渲染nginx模板都是全自主开发的，依托CMDB强大的事件管理，轻松的完成了Nginx的动态服务发现。如图2 - 6：<br>
<br>大致流程：<br>
<ol><li>创建虚拟机与项目进行关联，自动渲染puppet模板；</li><li>启动虚拟机拉取对应puppet部署模板，开始自动部署；</li><li>虚拟机中agent监听业务部署状态是否成功，然后进行上报CMDB；</li><li>CMDB接收到虚拟机的注册事件，并自动渲染Upstream模板到Puppet；</li><li>Nginx代理服务器同步配置，最后进行nginx -s reload生效。</li></ol><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210720/70c18e63c4a749d299bedbbd6457ddba.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210720/70c18e63c4a749d299bedbbd6457ddba.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图2：渲染模板</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210720/2d9cd4ef8e812f5429c44825feca88b9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210720/2d9cd4ef8e812f5429c44825feca88b9.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图3：注册渲染Upstream事件API</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210720/f1dded408081eca3bbb859fa87a110fc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210720/f1dded408081eca3bbb859fa87a110fc.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图4：Upstream事件日志列表</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210720/7e2dd630a19bb320e6119f6ccb7a63ed.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210720/7e2dd630a19bb320e6119f6ccb7a63ed.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图5：Upstream事件详情页</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210720/d572e2bfcebcb97b97197ba731384b40.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210720/d572e2bfcebcb97b97197ba731384b40.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图6：Upstream WEB化管理</em><br>
<h3>阶段三：动态配置（渲染模板+Consul）</h3>中后期的时候，容器化开始普及了，由于项目上线时容器随着发布将导致IP发生变化，对于这种频繁变动Nginx配置进行reload，让渲染模板的方式出现了瓶颈，会造成QPS波动。根据容器IP经常变动的场景，后来我们采用了Consul + ngx_lua + ngx_http_dyups_module的方式来实现Upstream服务的注册与发现，那时考虑到各方面不稳定因素怕影响现有业务，我们又独立部署了一套名为docker-proxy的Nginx代理用于容器发布，然后就变成了2种并行的服务发现模式的架构。如图7：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210720/b26563dce99d507097edfd6d37f7fc2b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210720/b26563dce99d507097edfd6d37f7fc2b.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图7：容器与物理机、虚拟机的分流图</em><br>
<br>关于Consul + ngx_lua + ngx_http_dyups_module的实现方式，这个阶段只是利用consul实现了动态服务发现，还没有实现Web化管理Upstream节点的权重 、连接数、状态等功能。如图8：<br>
<br>大致流程：<br>
<ol><li>项目关联容器发布类型，容器发布集成Consul Agent服务；</li><li>Consul agent实时探测业务检查状态，并汇报至Consul Server；</li><li>Nginx中的ngx_lua间隔3秒请求Consul API获取实例信息；</li><li>ngx_lua生成Upstream配置，并通过ngx.dyups更新到Nginx worker；</li><li>Nginx实时动态发现Upstream，无需进行nginx -sreload。</li></ol><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210720/744e0a4a6696f685475ea0d9f5ee412b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210720/744e0a4a6696f685475ea0d9f5ee412b.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图8：动态配置（容器）</em><br>
<h3>阶段四：动态配置（Consul）</h3>后期，经历了阶段三（渲染模板+Consul）的混合架构模式，发现维护成本变得十分高，因为第一层代理的域名需要关联虚拟机或者容器的Nginx代理，造成Nginx配置冗余，而且还浪费额外的服务器成本等。所以我们再一次进行了整合升级，还是基于Consul服务注册与发现的方式，将物理机、虚拟机与容器整合到一个Nginx代理上（清洗数据），将Nginx中ngx_lua服务发现的业务代码的进行移除，改造了dyups模块的接口支持json格式，然后开发了dyups-agent来实现与Consul API、dyups api交互的服务发现功能，且支持Web化管理Upstream节点的权重 、连接数、状态等操作。如图9：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210720/a8a1406b9a0a145999966dd65fd96628.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210720/a8a1406b9a0a145999966dd65fd96628.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图9：动态配置（物理机、虚拟机、容器）</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210720/9180ae161f79c46d32e06139a3e4dbdf.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210720/9180ae161f79c46d32e06139a3e4dbdf.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图10：Upstream列表</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210720/e8e8d46f4233fe6684ee3ac8e3de85ab.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210720/e8e8d46f4233fe6684ee3ac8e3de85ab.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图11：Upstream节点管理</em><br>
<br>最后，阶段四升级改造后，在这一年的运行期间，每天接近有上千实例节点进行服务注册与发现，至今还没出过Upstream服务异常的问题，所以还是相当稳定的。而且在阶段四中我们还实现了双活架构、关联DNS解析、动态http/https、灰度发布、动态限速等功能，希望在下次分享的时候，主要讲讲猪八戒网的双活架构模式。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/QYgfgb7vnk7D0CNppBzzSg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/QYgfgb7vnk7D0CNppBzzSg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            