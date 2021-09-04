
---
title: 'Apache Geode 1.14.0 发布，数据管理平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4191'
author: 开源中国
comments: false
date: Sat, 04 Sep 2021 08:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4191'
---

<div>   
<div class="content">
                                                                                            <p>Apache Geode 1.14.0 现已发布。<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgeode.apache.org%2F" target="_blank">Apache Geode</a> 是一个数据管理平台，可在广泛分布的云体系结构中提供对数据密集型应用程序的实时一致的访问。其将内存、CPU、网络资源以及可选的本地磁盘在多个进程间进行池化，以管理应用程序对象和行为。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>OQL 索引的创建现在适用于子区域</li> 
 <li>当一个区域在函数执行过程中被销毁时，会抛出适当的异常</li> 
 <li>现在在重新平衡区域时使用守护线程</li> 
 <li>在集群重启期间并行恢复磁盘存储</li> 
 <li>GFSH命令中的新选项 "启动网关发送器" 可以控制清理现有队列</li> 
 <li>在OQL查询GFSH命令中增加了新的成员字段，以指向将要执行查询的成员</li> 
 <li>使用 JTA 事务时不再出现 ConcurrentModificationException</li> 
 <li>如果端点验证被禁用，现在不需要设置SNI服务器名称</li> 
 <li>在试图创建 Lucene 索引时限制重试，以防止堆栈溢出问题</li> 
 <li>增加了一个新的统计数字，以获得网关发送者队列所占用的堆内存</li> 
 <li>创建网关接收器时设置的最大间隔时间现在不会被忽略</li> 
 <li>java垃圾回收和 tombstone 收集同时进行以防止死锁</li> 
 <li>在滚动升级期间，登记兴趣的速度得到了改善</li> 
 <li>存储桶统计已修复</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202109.mbox%2F%253CCABcWz0JmgmcCTeaqtZ0hRPCN45EpHoLWBQpGwJ-YheLvciOPyQ%40mail.gmail.com%253E" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            