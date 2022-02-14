
---
title: 'MatrixOne 0.2.0 发布，最快的 SQL 计算引擎来了'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-366e1a4f1fabb2a8cee22538406759d5a6a.png'
author: 开源中国
comments: false
date: Mon, 14 Feb 2022 07:42:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-366e1a4f1fabb2a8cee22538406759d5a6a.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt src="https://oscimg.oschina.net/oscnet/up-366e1a4f1fabb2a8cee22538406759d5a6a.png" referrerpolicy="no-referrer"></p> 
<p>在数月的打磨和努力开发之下，MatrixOne 0.2版本正式发布啦！</p> 
<p>项目文档网站：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.matrixorigin.io%2F0.2.0%2F" target="_blank">https://docs.matrixorigin.io/0.2.0/</a></p> 
<p>相比于0.1版本，0.2版本在以下几方面有着明显改进。</p> 
<p style="margin-left:0; margin-right:0"><strong><span>性能大幅提升</span></strong></p> 
<p style="margin-left:0; margin-right:0">0.2版本在原有AOE（Analytical Optimized Engine)引擎的基础上，通过因子化的方式实现了大幅度加速，<strong>性能得到10倍以上的提升</strong>，相比同等配置的Clickhouse也有50-100%的提升。<strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.matrixorigin.cn%2Fblog%2F74.html%23_np%3D103_2299" target="_blank">详细性能报告，点此查看</a>。</strong></p> 
<p style="margin-left:0; margin-right:0"><span><strong>完整的分布式能力</strong></span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e">0.2版本完整实现了独特的分布式&强一致框架——<strong>MatrixCube</strong>，现可以使用MatrixOne构建一个小型集群（</span><span style="color:#3e3e3e">MatrixCube详细介绍请参见官方文档）。</span><span>MatrixCube框架帮助MatrixOne数据库内核获得了分布式部署的能力，同时针对我们的AOE引擎实现了三种负载均衡机制：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e">实现各节点存储空间的均衡，以高效利用各节点存储资源；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e">各节点的Raft-Group Leader的均衡，从而达到读写请求的负载均衡；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e">各节点Table数据分布的均衡，以实现表级别的请求均衡。</span></p> </li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-1ff4451feb378e476ca3a38b82ec2b5168b.png" referrerpolicy="no-referrer"></p> 
<p>▲整体实现架构图</p> 
<p style="margin-left:0; margin-right:0"><strong>新Feature</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e">设计实现了新的SQL Parser</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e">新增对索引Index的支持</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e">新增云端SQL交互Playground</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e">新增SQL支持：</span></p> <p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e">a) 建表时对主键Primary Key的支持</span></p> <p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e">b) +, -, *, /, mod 运算符对不同数据类型的支持</span></p> <p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e">c) >, <, <=, >=, ==, != 对不同数据类型的支持</span></p> <p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e">d) NOT, ! 操作符</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e">新增对DATE/DATETIME数据类型的支持</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e">新增对LIKE运算符的支持</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>文档更新</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">新增分布式框架MatrixCube的架构及使用介绍</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">更新MySQL的语法支持情况</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增MatrixOne分布式集群安装及配置指南</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增纽约出租车benchmark测试指南</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增SSB及纽约出租车benchmark性能测试结果</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增云端Playground操作说明</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增SQL的语法描述及案例</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增数据类型的描述及案例</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增分布式系统参数配置列表</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增系统概念名词表Glossary</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增文档贡献guide及规范</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>Bug Fixes</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">修复包含sum情况下部分列会报错的bug #704</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复不同数字类型之间计算存在的精度问题 #789</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复列别名在查询排序中的识别问题 #796</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复过滤条件同时包含OR与NOT触发的错误 #850</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复偶尔提交数据产生乱序问题 #1075</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复重放场景下出现的相关问题 #1103</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">（MatrixCube）修复因索引值不一致导致的MatrixOne不能重启 #344</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">（MatrixCube）修复在尝试关闭副本两次时带来的实例崩溃 #420</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">（MatrixCube）修复拆分后应用配置更改带来的实例崩溃 #422</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>欢迎加入</strong><strong>MatrixOne社区</strong></p> 
<ul> 
 <li><strong>官网</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmatrixorigin.cn%2F" target="_blank">matrixorigin.cn</a></li> 
 <li><strong>源码：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatrixorigin%2Fmatrixone" target="_blank">github.com/matrixorigin/matrixone</a></li> 
 <li><strong>Slack</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmatrixoneworkspace.slack.com%2F" target="_blank">matrixoneworkspace.slack.com</a></li> 
</ul>
                                        </div>
                                      
</div>
            