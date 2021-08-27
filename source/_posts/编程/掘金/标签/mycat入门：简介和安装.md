
---
title: 'mycat入门：简介和安装'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0478bf3de5146489bca5047038cbf7d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 16:15:22 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0478bf3de5146489bca5047038cbf7d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第27天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<blockquote>
<p>mycat是分库分表的中间件，同学们可以参照做一下demo，初步的理解的和了解分库分表。</p>
</blockquote>
<h2 data-id="heading-0">1.什么是MYCAT</h2>
<ul>
<li>一个彻底开源的，面向企业应用开发的大数据库集群</li>
<li>支持事务、ACID、可以替代MySQL的加强版数据库</li>
<li>一个可以视为MySQL集群的企业级数据库，用来替代昂贵的Oracle集群</li>
<li>一个融合内存缓存技术、NoSQL技术、HDFS大数据的新型SQL Server</li>
<li>结合传统数据库和新型分布式数据仓库的新一代企业级数据库产品</li>
<li>一个新颖的数据库中间件产品</li>
</ul>
<h2 data-id="heading-1">2.关键特性</h2>
<ul>
<li>支持SQL92标准</li>
<li>支持MySQL、Oracle、DB2、SQL Server、PostgreSQL等DB的常见SQL语法</li>
<li>遵守Mysql原生协议，跨语言，跨平台，跨数据库的通用中间件代理。</li>
<li>基于心跳的自动故障切换，支持读写分离，支持MySQL主从，以及galera cluster集群。</li>
<li>支持Galera for MySQL集群，Percona Cluster或者MariaDB cluster</li>
<li>基于Nio实现，有效管理线程，解决高并发问题。</li>
<li>支持数据的多片自动路由与聚合，支持sum,count,max等常用的聚合函数,支持跨库分页。</li>
<li>支持单库内部任意join，支持跨库2表join，甚至基于caltlet的多表join。</li>
<li>支持通过全局表，ER关系的分片策略，实现了高效的多表join查询。</li>
<li>支持多租户方案。</li>
<li>支持分布式事务（弱xa）。</li>
<li>支持XA分布式事务（1.6.5）。</li>
<li>支持全局序列号，解决分布式下的主键生成问题。</li>
<li>分片规则丰富，插件化开发，易于扩展。</li>
<li>强大的web，命令行监控。</li>
<li>支持前端作为MySQL通用代理，后端JDBC方式支持Oracle、DB2、SQL Server 、 mongodb 、巨杉。</li>
<li>支持密码加密</li>
<li>支持服务降级</li>
<li>支持IP白名单</li>
<li>支持SQL黑名单、sql注入攻击拦截</li>
<li>支持prepare预编译指令（1.6）</li>
<li>支持非堆内存(Direct Memory)聚合计算（1.6）</li>
<li>支持PostgreSQL的native协议（1.6）</li>
<li>支持mysql和oracle存储过程，out参数、多结果集返回（1.6）</li>
<li>支持zookeeper协调主从切换、zk序列、配置zk化（1.6）</li>
<li>支持库内分表（1.6）</li>
<li>集群基于ZooKeeper管理，在线升级，扩容，智能优化，大数据处理（2.0开发版）</li>
</ul>
<h2 data-id="heading-2">3.优势</h2>
<p>基于阿里开源的Cobar产品而研发，Cobar的稳定性、可靠性、优秀的架构和性能以及众多成熟的使用案例使得MYCAT一开始就拥有一个很好的起点，站在巨人的肩膀上，我们能看到更远。业界优秀的开源项目和创新思路被广泛融入到MYCAT的基因中，使得MYCAT在很多方面都领先于目前其他一些同类的开源项目，甚至超越某些商业产品。</p>
<p>MYCAT背后有一支强大的技术团队，其参与者都是5年以上软件工程师、架构师、DBA等，优秀的技术团队保证了MYCAT的产品质量。</p>
<p>MYCAT并不依托于任何一个商业公司，因此不像某些开源项目，将一些重要的特性封闭在其商业产品中，使得开源项目成了一个摆设。</p>
<h2 data-id="heading-3">4.结构</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0478bf3de5146489bca5047038cbf7d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>个人理解：mycat本身虚拟成了一个mysql服务，我们可以直接调用，当我们操作mycat服务时，mycat会按照配置操作mysql服务。</p>
</blockquote>
<h2 data-id="heading-4">5.下载和安装</h2>
<p>进入官网<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.mycat.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://www.mycat.io/" ref="nofollow noopener noreferrer">www.mycat.io/</a>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/816300572ede4eb3b037712c9790526f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>楼主这里使用的事windows版。下载后是一个，直接解压就可以了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5095c83b9584785ab76ab4b41fb9b2a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">6.配置修改</h2>
<h3 data-id="heading-6">1.server.xml  </h3>
<pre><code class="copyable">   <user name="root">
<property name="password">123456</property>
<property name="schemas">TESTDB</property>

<!-- 表级 DML 权限设置 -->
<!-- 
<privileges check="false">
<schema name="TESTDB" dml="0110" >
<table name="tb01" dml="0000"></table>
<table name="tb02" dml="1111"></table>
</schema>
</privileges>
 -->
</user>

<user name="user">
<property name="password">user</property>
<property name="schemas">TESTDB</property>
<property name="readOnly">true</property>
</user>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>配置的是mycat作为服务区，对外的服务名，密码，(和mysql的服务器名，和密码概念相同) 。默认的端口号为8066，如果不想改数据库名，此类不用我们修改。</p>
</blockquote>
<h3 data-id="heading-7">2.wrapper.conf</h3>
<pre><code class="copyable">#********************************************************************
# Wrapper Properties
#********************************************************************
# Java Application
wrapper.java.command=C:\Program Files\Java\jdk1.8.0_144
wrapper.working.dir=..

# Java Main class.  This class must implement the WrapperListener interface
#  or guarantee that the WrapperManager class is initialized.  Helper
#  classes are provided to do this for you.  See the Integration section
#  of the documentation for details.
wrapper.java.mainclass=org.tanukisoftware.wrapper.WrapperSimpleApp
set.default.REPO_DIR=lib
set.APP_BASE=.
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>wrapper.java.command=C:\Program Files\Java\jdk1.8.0_144 改为jdk路径</p>
</blockquote>
<h3 data-id="heading-8">3.schema.xml</h3>
<pre><code class="copyable"><?xml version="1.0"?>
<!DOCTYPE mycat:schema SYSTEM "schema.dtd">
<mycat:schema xmlns:mycat="http://io.mycat/">
    <!-- name:server中配置的mycat服务名 -->
<schema name="TESTDB" checkSQLschema="false" sqlMaxLimit="100">
<!-- name:表名 datanode 是数据库别名 意思是 dn1,dn2中的user表 在mycat服务中生成，所以需要在datanode中的数据库都需要有user表 rule则是分片策略 而mod-long为分片策略-->
<table name="user" primaryKey="id" autoIncrement="true" dataNode="dn1,dn2" rule="mod-long" />
</schema>

    <!-- dn1 dn2对应着上面配置的datanode datahost是下面配置数据源的别名 database：l连接到的mysql服务的test数据库 -->
<dataNode name="dn1" dataHost="localhost1" database="test" />
<dataNode name="dn2" dataHost="localhost2" database="test" />

    <!-- name对应着上面 datehost中配置 指定datahost的数据源 -->
<dataHost name="localhost1" maxCon="1000" minCon="10" balance="0"
  writeType="0" dbType="mysql" dbDriver="native" switchType="1"  slaveThreshold="100">
<heartbeat>select user()</heartbeat>
<!-- can have multi write hosts -->
<writeHost host="hostM1" url="localhost:3306" user="root"
   password="root">
</writeHost>
</dataHost>

<dataHost name="localhost2" maxCon="1000" minCon="10" balance="0"
  writeType="0" dbType="mysql" dbDriver="native" switchType="1"  slaveThreshold="100">
<heartbeat>select user()</heartbeat>
<!-- can have multi write hosts -->
<writeHost host="hostS2" url="192.168.2.134:3306" user="root"
   password="123">
</writeHost>
</dataHost>
</mycat:schema>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">4.rule.xml</h3>
<p>此处划重点！一定要去rule中取查看自己配置的策略，安装后自带配置的为<code><property name="count">3</property></code></p>
<p>但是如果你mysql服务只有2个就会报错，所以每次配置时，来rule.xml中看看配置的数量和你数据库服务数量是否能对上。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc14a3bfbd884ca0bf9089caef59a335~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后启动服务，双击bin文件夹下的startup_nowrap.bat。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da37ebfce10d485dafcead2371b1a296~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/075b89b8d6e94ad3bf3f09d36387bcf8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果出现以上信息，则启动成功。</p></div>  
</div>
            