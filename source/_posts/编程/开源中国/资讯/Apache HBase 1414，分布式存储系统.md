
---
title: 'Apache HBase 1.4.14，分布式存储系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2683'
author: 开源中国
comments: false
date: Wed, 27 Oct 2021 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2683'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Apache HBase 1.4.14 已经发布。HBase – Hadoop Database，是一个高可靠性、高性能、面向列、可伸缩的分布式存储系统，利用 HBase 技术可在廉价 PC Server 上搭建起大规模结构化存储集群。</span></p> 
<p><strong><span style="background-color:#ffffff; color:#333333">主要更新内容</span></strong></p> 
<ul> 
 <li>Bug 
  <ul> 
   <li>降低除热分支之外的所有分支的 flakey 重新运行率</li> 
   <li>WALFactory.Providers.multiwal 导致 StackOverflowError</li> 
   <li>[授权] ServiceAuthorizationManager 不可动态更新</li> 
   <li>修复 ServiceAuthorizationManager 上的 findbugs 警告</li> 
   <li>使 hbase.security.authentication 属性的 kerberos 值不区分大小写</li> 
   <li>将 HBASE-24169 的预提交更改向后移植到所有分支</li> 
   <li>使用 SaslConnection MAX_ATTEMPTS 的客户端属性（当前硬编码为 5）</li> 
   <li>将 "-h" 或 "--help" 传递给 bin/hbase 没有按预期执行</li> 
   <li>[Build] 分支 1 的构建似乎因为 pylint 而损坏</li> 
   <li>hbase.rowlock.wait.duration 不应 <= 0</li> 
   <li>删除未使用的凭证 hbaseqa-at-asf-jira</li> 
   <li>CompactionConfiguration 记录不切实际的存储文件大小</li> 
   <li> 使用 maven 运行 UT 时避免修剪错误堆栈跟踪</li> 
  </ul> </li> 
 <li>改进 
  <ul> 
   <li>[RSGroup] 自动将创建的表分配给相应的 rsgroup，而不是手动操作</li> 
   <li>对区域关闭锁使用公平的 ReentrantReadWriteLock</li> 
   <li>将 Thrift 升级到 0.13.0：0.12.0 具有出色的 CVE</li> 
   <li>[Build] Pin rubocop 版本 <= 0.81</li> 
   <li>将 HBASE-24302 反向移植到分支 1</li> 
   <li>修复 HStore#compact 注释中的拼写错误</li> 
  </ul> </li> 
 <li>子任务 
  <ul> 
   <li>将 HBASE-23989 中的个性更改向后移植到所有活动分支</li> 
   <li>在 hadoop 检查中添加 hadoop 3.2.x</li> 
   <li>修复了 hbase-personality.sh 中不稳定的作业 url</li> 
   <li>将不稳定的报告 jenkins 作业从 Hadoop 迁移到 hbase</li> 
   <li>将脆弱的测试 jenkins 作业从 Hadoop 迁移到 hbase</li> 
   <li>将 HBase Nightly jenkins 作业从 Hadoop 迁移到 hbase</li> 
   <li>将 java.io.tmpdir 设置为项目构建目录以避免将 std*deferred 文件写入 /tmp</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202110.mbox%2F%253CCAAAYAnPApDpir%2B_a3LQgCs_TyNQmZPAouhz3dVYRy1DzL7qtSQ%40mail.gmail.com%253E" target="_blank">更新公告。</a></p> 
<p> </p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"> </p> 
<p> </p>
                                        </div>
                                      
</div>
            