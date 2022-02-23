
---
title: 'MatrixOne 0.2.0 发布 ！最快的 SQL 计算引擎来了！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202202/23145506_2oHS.png'
author: 开源中国
comments: false
date: Wed, 23 Feb 2022 15:11:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202202/23145506_2oHS.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img alt src="https://static.oschina.net/uploads/img/202202/23145506_2oHS.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"> <strong>在数月的打磨和努力开发之下,</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><strong>MatrixOne 0.2版本正式发布啦！</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><strong>项目文档网站</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.matrixorigin.io%2F0.2.0%2F" target="_blank">Home - MatrixOne Docs</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>重点关注，相比于0.1版本，0.2版本在以下几方面有着明显改进：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#1a439c"><strong>1. 性能大幅提升</strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">0.2版本在原有AOE（Analytical Optimized Engine)引擎的基础上，通过因子化的方式实现了大幅度加速，<strong>性能得到10倍以上的提升</strong>，相比同等配置的Clickhouse也有50-100%的提升。<strong>详细性能报告，请点击“‍<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.matrixorigin.cn%2Fblog%2F74.html%23_np%3D103_2299" target="_blank">MatrixOne 0.2.0性能测试报告</a>‍”查看</strong>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#1a439c"><strong>2. 完整的分布式能力</strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">0.2版本完整实现了独特的分布式&强一致框架——MatrixCube，现可以使用MatrixOne构建一个小型集群（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.matrixorigin.io%2F0.2.0%2FMatrixOne%2FOverview%2Fmatrixcube%2Fmatrixcube-introduction%2F" target="_blank">MatrixCube详细介绍请参见官方文档</a>）。MatrixCube框架帮助MatrixOne数据库内核获得了分布式部署的能力，同时针对我们的AOE引擎实现了三种负载均衡机制：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>实现各节点存储空间的均衡，以高效利用各节点存储资源；</li> 
 <li>各节点的Raft-Group Leader的均衡，从而达到读写请求的负载均衡；</li> 
 <li>各节点Table数据分布的均衡，以实现表级别的请求均衡。</li> 
</ul> 
<div style="text-align:left"> 
 <p style="margin-left:0; margin-right:0; text-align:center"><img alt src="https://static.oschina.net/uploads/img/202202/23145506_uYCa.png" referrerpolicy="no-referrer">​</p> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><span style="color:#1a439c"><em>整体实现架构图</em></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#1a439c"><strong>3. 新Feature</strong></span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">设计实现了新的SQL Parser</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增对索引Index的支持</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增云端SQL交互Playground</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增SQL支持：</p> <p style="margin-left:0; margin-right:0">a) 建表时对主键Primary Key的支持</p> <p style="margin-left:0; margin-right:0">b) +, -, *, /, mod 运算符对不同数据类型的支持</p> <p style="margin-left:0; margin-right:0">c) >, <, <=, >=, ==, != 对不同数据类型的支持</p> <p style="margin-left:0; margin-right:0">d) NOT, ! 操作符</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增对DATE/DATETIME数据类型的支持</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增对LIKE运算符的支持</p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#1a439c"><strong>4. 文档更新</strong></span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
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
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>5. Bug Fixes</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">修复包含sum情况下部分列会报错的bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatrixorigin%2Fmatrixone%2Fissues%2F704" target="_blank">#704</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复不同数字类型之间计算存在的精度问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatrixorigin%2Fmatrixone%2Fissues%2F789" target="_blank"> #789</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复列别名在查询排序中的识别问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatrixorigin%2Fmatrixone%2Fissues%2F796" target="_blank">#796</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复过滤条件同时包含OR与NOT触发的错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatrixorigin%2Fmatrixone%2Fissues%2F850" target="_blank"> #850</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复偶尔提交数据产生乱序问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatrixorigin%2Fmatrixone%2Fissues%2F1075" target="_blank">#1075</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复重放场景下出现的相关问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatrixorigin%2Fmatrixone%2Fissues%2F1103" target="_blank">#1103</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">（MatrixCube）修复因索引值不一致导致的MatrixOne不能重启 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatrixorigin%2Fmatrixone%2Fissues%2F344" target="_blank">#344</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">（MatrixCube）修复在尝试关闭副本两次时带来的实例崩溃 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatrixorigin%2Fmatrixone%2Fissues%2F420" target="_blank">#420</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">（MatrixCube）修复拆分后应用配置更改带来的实例崩溃 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatrixorigin%2Fmatrixone%2Fissues%2F422" target="_blank">#422</a></p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#1a439c"><strong>6. 欢迎加入MatrixOne社区</strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>官网：</strong><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmatrixorigin.cn" target="_blank">matrixorigin.cn</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>源码：</strong><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgithub.com%2Fmatrixorigin%2Fmatrixone%25C2%25A0" target="_blank">github.com/matrixorigin/matrixone </a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Slack：</strong><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmatrixoneworkspace.slack.com" target="_blank">matrixoneworkspace.slack.com</a></p>
                                        </div>
                                      
</div>
            