
---
title: 'TDengine入驻Rainbond开源应用商店'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://pic.imgdb.cn/item/6177a00a2ab3f51d91c9ce88.png'
author: Dockone
comments: false
date: 2021-12-13 04:10:55
thumbnail: 'https://pic.imgdb.cn/item/6177a00a2ab3f51d91c9ce88.png'
---

<div>   
<br><h2>前言</h2>TDengine是一个高效的存储、查询、分析时序大数据的平台，专为物联网、车联网、工业互联网、运维监测等优化而设计。Rianbond擅长应用自动化管理 ，两者结合起来实现1+1大于2，本文详细讲述如何整合TDengine和Rainbond，并通过整合实现高效快捷，便利简洁。<br>
<br><h2>TDengine</h2>TDengine  是涛思数据面对高速增长的物联网大数据市场和技术挑战推出的创新性的大数据处理产品，它不依赖任何第三方 软件，也不是优化或包装了一个开源的数据库或流式计算产品，而是在吸取众多传统关系型数据库、NoSQL 数据库、流式计算引擎、消息队列等软件的优点之后自主开发的产品，在时序空间大数据处理上，有着自己独到的优势，可将典型的物联网、车联网、工业互联网大数据平台的总拥有成本大幅降低。<br>
<br><img src="https://pic.imgdb.cn/item/6177a00a2ab3f51d91c9ce88.png" alt referrerpolicy="no-referrer"><br>
<br><h2>快速安装</h2>目前TDengine官方支持安装包，源码和docker进行安装，现在新增通过Rainbond进行安装，通过Rainbond安装有什么优势呢？<br>
<ul><li><br>集成了TDengine官方推荐的可视化探测工具Grafana，开盒即用，方便快捷。</li><li><br>集成了TDengine三节点集群，无需手动配置，安装即集群模式，提高部署效率。</li><li><br>集群安装过程仅需3分钟，高效便利。<br>
<br>在通过Rainbond平台进行安装TDengine之前，首先保证有一个可用的Rainbond，具体安装可以参考文档<a href="https://www.rainbond.com/docs/quick-start/quick-install?channel=dockone">Rainbond快速安装</a>。<br>
<br>安装完Rainbond以后界面首页总览，点击新增，选择基于应用市场创建组件，选择开源应用商店，直接搜索即可，目前分别上架了 “单机版” “集群版”的TDengine， 根据需求进行点击安装。</li></ul><br>
<br><img src="https://pic.imgdb.cn/item/618353f72ab3f51d917a49b1.png" alt referrerpolicy="no-referrer"><br>
<br><h2>安装成功示例</h2><img src="https://pic.imgdb.cn/item/618381c32ab3f51d91a869cb.png" alt="成功拓扑图" referrerpolicy="no-referrer"><br>
<br>| TDengine            | Grafana             |<br>
| ------------------- | ------------------- |<br>
| user : root         | user  : admin       |<br>
| password : taosdata | password : 12345678 |<br>
<br>登录Grafana以后直接选择配置好的dashboard，进行展示就可以，效果图如下<br>
<br><img src="https://pic.imgdb.cn/item/617a1b842ab3f51d91a8016b.png" alt referrerpolicy="no-referrer"><br>
<br><h2>客户端连接</h2>日常工作中真正去使用数据库的时候，其实都是远程进行访问或者写入数据，目前平台经过测试也是支持的，需要进行简单的调式即可使用，要注意的点就是需要保证6030-6041端口全部打开。<br>
<ul><li><br>Rainbond支持两种治理模式，一种是平台特有的内置 ServiceMesh 模式，另外一种是kubernetes原生 service 模式。<br>
<br>TDengine在进行连接之前只需要把默认的治理模式，serviceMesh更改为原生的service才可以。</li><li><br>在实例伸缩选项里面复制查询命令在终端执行即可查询，集群的详细信息。 <br>
<br><img src="https://pic.imgdb.cn/item/618b93fd2ab3f51d91f6393c.png" alt referrerpolicy="no-referrer"><br>
<br><img src="https://pic.imgdb.cn/item/618b92d62ab3f51d91f579b1.png" alt referrerpolicy="no-referrer"><strong>示例</strong>：在client端  <code class="prettyprint">taos容器终端直接执行命令行进行连接即可，taos  -host grf77a29</code> 就实现写入数据了。</li></ul><br>
<br><h2>性能测试</h2>| 基础测试环境           | 数据呈现     |<br>
| ---------------------- | ------------ |<br>
| TDengine版本           | 2.2.1.1      |<br>
| TDengine集群节点数量   | 3            |<br>
| TDengine集群单节点内存 | 4G           |<br>
| TDengine集群类型       | container    |<br>
| 100000000条数据写入    | 94.17s       |<br>
| 每秒写入性能           | 1061965.70条 |<br>
| 测试工具               | taosdemo     |<br>
<br><strong>注意：</strong>本次测试是基于Rainbond平台进行，数据仅供参考。平台默认单节点内存为512M，如需进行测试内存保证最少为4G，实际生产环境根据需求进行设置内存大小。<br>
<br><h2>小结</h2>TDengine作为目前非常火热的时序性数据库之一，值得我们去不断地探索发现，本文只是简单讲解了一部分功能而已，想要了解更多可以关注<a href="https://www.taosdata.com/cn/">TDengine官方</a>学习研究。<br>
<br>-----<br>
<br><a href="https://www.rainbond.com/?channel=dockone">Rainbond</a>是一个开源的云原生应用管理平台，使用简单，不需要懂容器和Kubernetes，支持管理多个Kubernetes集群，提供企业级应用的全生命周期管理，功能包括应用开发环境、应用市场、微服务架构、应用持续交付、应用运维、应用级多云管理等。
                                
                                                              
</div>
            