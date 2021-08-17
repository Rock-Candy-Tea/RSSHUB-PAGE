
---
title: 'eKuiper 1.3.0 正式发布：加入 LF Edge 基金会后首个版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0817/150342_5HTC_4252687.png'
author: 开源中国
comments: false
date: Tue, 17 Aug 2021 15:04:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0817/150342_5HTC_4252687.png'
---

<div>   
<div class="content">
                                                                                            <p>eKuiper (原名 EMQ X Kuiper，现已捐献给 LF Edge 基金会，成为其旗下独立项目) 是 Golang 实现的轻量级物联网边缘分析、流式处理开源软件，可以运行在各类资源受限的边缘设备上。eKuiper 设计的一个主要目标就是将在云端运行的实时流式计算框架 (比如 Apache Spark (https://spark.apache.org/)，Apache Storm (https://storm.apache.org/) 和 Apache Flink (https://flink.apache.org/)) 迁移到边缘端。Kuiper 参考了上述云端流式处理项目的架构与实现，结合边缘流式数据处理的特点，采用了编写基于源 (Source)，SQL (业务逻辑处理), 目标 (Sink) 的规则引擎来实现边缘端的流式数据处理。</p> 
<p>eKuiper 的应用场景包括：运行在各类物联网的边缘使用场景中，比如工业物联网中对生产线数据进行实时处理；车联网中的车机对来自汽车总线数据的即时分析；智能城市场景中，对来自于各类城市设施数据的实时分析。通过 eKuiper 在边缘端的处理，可以提升系统响应速度，节省网络带宽费用和存储成本，以及提高系统安全性等。</p> 
<p><img height="206" src="https://static.oschina.net/uploads/space/2021/0817/150342_5HTC_4252687.png" width="500" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p>网址：https://www.lfedge.org/projects/ekuiper/</p> 
 <p>Github仓库：https://github.com/lf-edge/ekuiper</p> 
 <p>eKuiper 1.3.0 Docker 镜像地址：</p> 
 <p>https://registry.hub.docker.com/r/lfedge/ekuiper/tags?page=1&ordering=last_updated</p> 
</blockquote> 
<h4><strong>概述</strong></h4> 
<p><strong>eKuiper 1.3.0 是迁移到 LF Edge 基金会之后发布的第一个版本。</strong>该版本中，eKuiper 根据 LF Edge 基金会的标准和建议进行了一系列重大重构，包括项目网站、GitHub 地址、项目结构、Docker 镜像名称以及镜像仓库地址。项目结构的重构包括重命名了模块名字、项目目录、源代码文件中增加了 CopyRight 声明。我们还重构了构建脚本以及CI脚本。由于这些改动，用户需要到最新的地址浏览项目网站、源代码以及下载最新的 Docker 镜像和插件。同时，本次发布提供了一系列针对 SQL 运行时的新功能，还增加了对 EdgeX source、redis sink 的支持，修复了一些 bug。</p> 
<h4><strong>功能与修复</strong></h4> 
<p>◆ 项目结构</p> 
<ul> 
 <li> <p>重构了项目模块名、项目代码组织、包引用，最新的代码请到此下载（https://github.com/lf-edge/ekuiper）</p> </li> 
 <li> <p>针对本次发布编译插件时请导入最新的 eKuiper 模块，并调整包引用路径</p> </li> 
</ul> 
<p>◆ Docker 镜像</p> 
<ul> 
 <li> <p>重命名了 eKuiper docker 镜像名称，更改了仓库地址（https://hub.docker.com/r/lfedge/ekuiper）</p> </li> 
 <li> <p>重命名了 eKuiper kubernetes tool docker 镜像名称，更改了仓库地址（https://hub.docker.com/r/lfedge/ekuiper-kubernetes-tool）</p> </li> 
 <li> <p>减小了 eKuiper docker 镜像占用空间</p> </li> 
</ul> 
<p>◆ SQL 运行时</p> 
<ul> 
 <li> <p>窗口函数部分增加了 window_start() 和 window_end() 函数 （https://github.com/lf-edge/ekuiper/blob/master/docs/en_US/sqls/built-in_functions.md#aggregate-functions）</p> </li> 
 <li> <p>增加了以表达式作为数组类型索引的支持</p> </li> 
 <li> <p>重构了别名机制以支持更多使用场景</p> </li> 
 <li> <p>重构了 SQL 验证，支持聚合相关的验证</p> </li> 
</ul> 
<p>◆ 增加了 EdgeX source类型，以便让规则引擎直接连到消息总线上（https://github.com/lf-edge/ekuiper/blob/master/docs/en_US/edgex/edgex_source_tutorial.md）</p> 
<p>◆ 增加了 redis sink 插件（https://github.com/lf-edge/ekuiper/blob/master/docs/en_US/plugins/sinks/reids.md）</p> 
<p>◆ 增加了更多 sink dataTemplate 函数（https://github.com/lf-edge/ekuiper/blob/master/docs/en_US/rules/data_template.md)</p> 
<p>◆ 增加了共享 source 实例支持（https://github.com/lf-edge/ekuiper/blob/master/docs/en_US/sqls/streams.md）</p> 
<p>◆ 重构了 eKuiper ui 元数据 API 并在新版的操作控制台中进行适配</p> 
<p>◆ 修复</p> 
<ul> 
 <li> <p>重构 sqlite 键值存储代码，解决了并发访问过大时存储访问异常问题</p> </li> 
 <li> <p>修复了 influxdb 插件多实例问题</p> </li> 
 <li> <p>针对 mqtt source，修复了重连时订阅失败问题</p> </li> 
 <li> <p>在内存和存储中清理过期的 checkpoint</p> </li> 
 <li> <p>当删除规则时，清理存储中的 checkpoint</p> </li> 
 <li> <p>当 source node 关闭时，确保关闭动态缓存</p> </li> 
 <li> <p>修复 http source 中的内存泄漏问题</p> </li> 
</ul> 
<p>◆ 文档修复</p> 
<ul> 
 <li> <p>源代码中增加了 CopyRight 声明</p> </li> 
 <li> <p>更新了 EdgeX 版本2相关文档</p> </li> 
 <li> <p>增加了接入 EdgeX 指导手册</p> </li> 
 <li> <p>增加了 eKuiper 和 OpenYurt 集成指导手册</p> </li> 
 <li> <p>更新了插件开发指导手册</p> </li> 
 <li> <p>更新了插件下载地址</p> </li> 
 <li> <p>更新了参与到本项目的指导说明，问题提交模版以及本项目会议记录</p> </li> 
</ul> 
<p><strong>特别感谢</strong></p> 
<ul> 
 <li>@tixff  修复了 mqtt source 的一个 bug </li> 
 <li>@rwadowski  重构了 sqlite 键值存储   </li> 
 <li>@feng-crazy 提供了 redis sink 插件   </li> 
 <li>@wfnuser 为 http source 内存泄漏提供了一个解决方案</li> 
</ul>
                                        </div>
                                      
</div>
            