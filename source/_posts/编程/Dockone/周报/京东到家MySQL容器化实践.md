
---
title: '京东到家MySQL容器化实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210605/c7d4991fc1e770ed6ce437bdf764694e.png'
author: Dockone
comments: false
date: 2021-06-06 12:32:40
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210605/c7d4991fc1e770ed6ce437bdf764694e.png'
---

<div>   
<br>【编者的话】本文介绍了京东到家MySQL容器化的实践，包括基于容器的底层资源平台、监控系统及数据库自动化运维平台。同时也详细介绍了具体的技术实现，包括软硬件选型、容器调度算法、数据库高可用实现、监控系统及数据库自动化运维平台开发。<br>
<h3>背景</h3>随着京东到家业务的快速发展，MySQL数据库的访问量越来越大，在云主机上搭建MySQL越来越无法满足我们的要求。<br>
<ul><li>云主机的云硬盘IO性能并不能满足MySQL所需的高并发访问需求。</li><li>云主机所在宿主机使用不透明，当发生网络或者硬件故障时无法及时定位问题。</li><li>搭建在云主机上的MySQL在有变更规格的需求时，需要关机才能变更配置。</li><li>云主机上搭建MySQL成本高，采购云MySQL成本更高。</li></ul><br>
<br>基于上述原因，我们最终选择采购物理机，在物理机上将MySQL容器化部署来解决以上问题。<br>
<h3>技术方案</h3>我们认为一套完善的数据库运维方案包括以下几个部分：数据库底层资源平台、监控系统及数据库自动化运维平台。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210605/c7d4991fc1e770ed6ce437bdf764694e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210605/c7d4991fc1e770ed6ce437bdf764694e.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图1 整体架构</em><br>
<h4>数据库底层资源平台</h4><ul><li>在物理机上搭建Docker环境，将MySQL实例部署在Docker内，基于Docker的特性，实现资源隔离和资源超卖。</li><li>自定义规则算法来进行容器的调度。</li><li>在高可用方面，针对MHA和Zabbix进行二次开发，实现宕机后快速切换。</li></ul><br>
<br><h4>监控系统</h4>监控系统采用Zabbix，其中每个容器的监控数据（CPU、内存等）通过Docker Api来获取。<br>
<h4>数据库自动化运维平台</h4>基于Python和Flask框架，开发MySQL自动化运维平台，实现MySQL完整生命周期自动化运维，提高运维人员的工作效率。<br>
<h3>技术实现</h3><h4>数据库底层资源平台的搭建</h4><strong>软硬件选型</strong>  <br>
<br>MySQL运行的场景需求为高并发高IO，我们在软硬件上做了如下选择：<br>
<ul><li>物理机：64核、256G内存、16*960G SSD组成RAID10 or 4T NVME RAID0</li><li>操作系统：CentOS 7.5</li><li>容器：Docker版本1.13.1 、网络模式选择host模式。（从这也可以看出，我们主要是对CPU和内存进行了资源隔离，网络层面没进行资源隔离）</li><li>镜像：自定义的MySQL5.6.36镜像、MySQL5.7.22镜像</li></ul><br>
<br>对基于容器的MySQL实例和基于云主机的MySQL实例，同规格下进行了压测对比，云主机中MySQL QPS最大值23K。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210605/21a70fd0a9c9b237f2e97556bbb606e6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210605/21a70fd0a9c9b237f2e97556bbb606e6.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图2 云主机压测结果</em><br>
<br>容器中的MySQL充分利用了本地SSD硬盘的高IO， QPS最大值达90K。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210605/6953bdd0e3223d3c5eaf4087981019d0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210605/6953bdd0e3223d3c5eaf4087981019d0.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图3 容器压测结果</em><br>
<br>容器化后MySQL性能远超云主机上的MySQL，完全可以满足京东到家当前的MySQL性能需求。<br>
<br><strong>容器调度算法</strong><br>
<br>MySQL作为一种有状态的服务，DBA不需要对之进行频繁的操作，要保持相对稳定和健壮，我们自行定义了规则算法来进行容器的调度。<br>
<ul><li>同一集群的实例分布在不同可用区。</li><li>同一集群的实例分布在不同宿主机。</li><li>根据业务级别不同MySQL分布不同宿主机，核心业务在一台宿主机上不能部署过多。</li><li>分库系统，各分片MySQL分布不同宿主机。  </li><li>优先分配CPU、内存、磁盘空间资源最空闲的主机。</li><li>通过Docker超卖CPU，超卖的倍数不超过实际CPU核数2倍。</li></ul><br>
<br>基于以上原则，我们开发了容器调度系统，对容器的分配进行整体调度。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210605/5c2d7c8828c7f76e6a3bdf390e12b05b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210605/5c2d7c8828c7f76e6a3bdf390e12b05b.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图4 容器调度系统</em><br>
<br><strong>MySQL的高可用实现</strong><br>
<br>到家应用服务器访问MySQL是通过域名方式来进行连接的，我们对MHA和Zabbix监控系统进行二次开发，故障时通过快速更改域名解析来进行故障切换。整个切换过程在10秒内可以完成。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210605/b79c5e24b18ed7090c76376895388375.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210605/b79c5e24b18ed7090c76376895388375.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图5 数据库高可用架构</em><br>
<br>Zabbix监控系统发现MySQL发生宕机后，首先判断是主库还是从库，如果主库宕机由MHA Manager来进行处理，从库宕机由Zabbix监控调用脚本来进行处理。<br>
<br>主库宕机：MHA Manager将Master_Log_File和Read_Master_Log_Pos最高的从库提升为新主库，同时MHA Manager也会调用DNS解析接口将主库域名解析到新主库IP。由于域名DNS解析可能存在缓存，域名更新生效时间可能比较长。故障切换系统同时会根据宕机的MySQL数据库域名查找连接的所有应用服务器IP，通过Saltstack批量修改/etc/hosts文件绑定域名到新IP，下发到各应用主机上，缩短域名解析生效时间，能达到秒级解析生效。  <br>
<br>从库宕机：由Zabbix调用DNS解析接口，将宕机从库绑定的域名解析到主库上，后续操作与主库宕机操作流程类似。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210605/de32f49dc95bd3a739474889030eeb57.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210605/de32f49dc95bd3a739474889030eeb57.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图6 数据库宕机处理流程</em><br>
<h4>监控系统</h4>到家的监控系统采用的是Zabbix，使用自定义模板对MySQL运行状态进行监控。需要注意的是Docker内部CPU和内存的监控数据从OS层的获取值并不准确，我们通过调用Docker API的方式进行采集，再汇总到Zabbix。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210605/ac5313aa3ad95b03513f4c067b781f92.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210605/ac5313aa3ad95b03513f4c067b781f92.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图7 监控数据Zabbix展示</em><br>
<br>Zabbix通过设置触发器，当出现告警时自动执行自定义脚本，利用这个功能，可以实现MySQL故障后自愈的功能。<br>
<ul><li>MySQL实例触发所在磁盘空间不足报警时，自动执行脚本删除占冗余的文件从而释放空间。</li><li>MySQL实例触发CPU使用率过高报警时，自动执行脚本将当前运行的SQL及所有连接发邮件给DBA及相关研发，以便快速找到CPU报警的原因。</li><li>前面提到的MySQL宕机后自动进行域名切换，也是利用Zabbix的这个功能。</li></ul><br>
<br><h4>开发自动化运维平台</h4>我们基于Python和Flask开发了MySQL自动化运维系统，从MySQL资源申请、实例创建、销毁、主从架构部署、集群不同角色备份策略的选择、监控添加、销毁等，将MySQL整个生命周期实现流程化和自动化。<br>
<br><strong>MySQL申请及交付</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210605/37fe8394455bb23811d92a5da4feb835.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210605/37fe8394455bb23811d92a5da4feb835.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图8 申请信息</em><br>
<br>研发通过数据库运维平台申请MySQL资源，经DBA审批后，程序根据容器调度算法，后端会自动创建一套主从架构的MySQL数据库集群。并为MySQL自动添加相应的账号及授权，账号类型包含：监控、备份、主从、工具类等。同时容器创建之后就包含：MySQL服务端、Zabbix客户端、SaltStack客户端、Percona Toolkit、备份脚本、慢日志切割脚本等。<br>
<br>整个过程已实现自动化，并且基于镜像快速创建容器，5分钟内可交付一套完整可用的MySQL集群。<br>
<br><strong>配置变更</strong><br>
<br>得益于容器的特性，调用Docker的update命令可实时改变对应容器的CPU和内存配额。从而可以不停机进行MySQL实例规格变更，实现快速扩容或缩容。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210605/ba0d01da76a12248f36844c1ab5440e9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210605/ba0d01da76a12248f36844c1ab5440e9.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图9 实例扩容</em><br>
<br><strong>MySQL工具</strong><br>
<br>MySQL交付之后，我们提供了大量的MySQL工具：语法分析工具、当前慢日志分析工具、MySQL连接数查询工具、从库延迟查询工具、主从关系查询工具、正在运行SQL查询工具、MySQL快速健康检查、物理机监控、错误日志等。这些工具方便了研发的平时使用，可以借助这些工具进行排查解决。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210605/82250c5b4eefb902a1358a668e632845.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210605/82250c5b4eefb902a1358a668e632845.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图10 数据库工具</em><br>
<h3>总结</h3>目前到家的MySQL实例有95%以上都运行在了容器中，容器化后的MySQL平台经受住了415周年庆、618、1020等所有大促考验，对于我们来说，目前的容器化MySQL平台给我们带来了三大好处：<br>
<ul><li>满足性能：运行在物理机Docker内的MySQL实例性能高，能满足到家多个业务场景的性能需求。</li><li>降低成本：Docker容器之间可进行资源隔离，可以在同一台机器上部署多个MySQL实例。而且通过Docker超卖CPU资源，可提高资源利用率，相比在云主机上搭建MySQL成本降低了50%，比采购云MySQL成本降低了100%。</li><li>提高效率：所有MySQL流程自动化，5分钟内可以交付一套可用的MySQL主从集群，运维效率得到很大提高。</li></ul><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/0R9vQVFNmY8r2a00cYSv3g" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/0R9vQVFNmY8r2a00cYSv3g</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            