
---
title: 'Apache Bigtop 3.0.0 发布，大数据打包测试工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9694'
author: 开源中国
comments: false
date: Tue, 26 Oct 2021 06:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9694'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Apache Bigtop 3.0.0 现已发布，Apache Bigtop 是一个针对基础设施工程师和数据科学家的开源项目，旨在全面打包、测试和配置领先的开源大数据组件/项目，包括但不限于 Hadoop、HBase 和 Spark 。支持 Debian、Ubuntu、CentOS、Fedora、openSUSE 等操作系统。</span></p> 
<p><strong><span style="background-color:#ffffff; color:#333333">主要更新内容</span></strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#333333">bug 修复</span> 
  <ul> 
   <li><span style="background-color:#ffffff; color:#333333">由于 cmake 版本不匹配，在 CentOS 7 上构建 Hadoop 3.2.1 失败</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">构建 Hadoop 3.2.1 时检查 jar 内容失败</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">修复构建 Oozie 问题</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">修复 hadoop-3 的 puppet 清单</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">修复 Hadoop 和 HBase 之间 Guava 的版本不匹配问题</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">修复工具链不会因创建不必要的符号链接而破坏 cmake</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">修复 Hadoop 和 HBase 之间 Jetty 的版本不匹配问题</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">修复 Livy 与 Spark 3 的构建失败问题</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">在 yarn-site.xml 中的 yarn.nodemanager.env-whitelist 中添加 MapReduce 设置</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">修复由于 gem 版本不兼容导致的 Logstash 构建失败</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">如果安装了 libslf4j-java，Sqoop bin 脚本在 Debian 10 上无法运行</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">删除 Hive 的 HBase jar 链接</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">Hadoop 3.2.2 在 Arm 上构建失败</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">删除 yarn-ui 中的 phantomjs 部署</span></li> 
  </ul> </li> 
 <li><span style="background-color:#ffffff; color:#333333">改进</span> 
  <ul> 
   <li><span style="background-color:#ffffff; color:#333333">​​​​​​​更新用于部署 Flink 1.11.1 的 puppet 清单</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">清理或禁用通过打包 Kibana 安装的 husky</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">在 hadoop 服务中添加 hadoop-yarn-router 和 hadoop-hdfs-dfsrouter</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">在 hadoop 中添加 libhdfspp 软件包</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">更新 hadoop-yarn-router 和 hadoop-hdfs-dfsrouter 的 deb 资源</span></li> 
   <li><span style="background-color:#ffffff; color:#333333"> 在ambari-agent RPM 中添加缺少的文件</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">删除 smoke-tests/odpi-runtime</span></li> 
   <li><span style="background-color:#ffffff; color:#333333">从 Ambari 的 do-component-build 中删除过时的文本替换</span></li> 
  </ul> </li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202110.mbox%2F%253CCAEhbgSJc_UbKi0kWxWkHOxB%3DrCT5nWea1WqJeFTD-4jYAexOAw%40mail.gmail.com%253E" target="_blank">更新公告</a>。</span></p>
                                        </div>
                                      
</div>
            