
---
title: 'windows下sharding jdbc 和 mycat谁更好用？来 咱试试'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e5a0f668be145558f1c936f2cd5a4a4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 15 Aug 2021 02:49:21 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e5a0f668be145558f1c936f2cd5a4a4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第1天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">前言</h1>
<hr>
<p>写这篇博客纯属玩耍，如果有不对的地方，大家看看就好。目前后台的分库分表领域两个标志性的中间件就是sharding jdbc和mycat，今天咱就来分别搭一下，看看都怎么玩。如果你以面试为目的的话，这篇文章应该不是很适合，如果你项目中最近后台架构要改为分库分表，那么这篇文章能使你快速的搭建起来一个分库分表的框架。 玩耍开始。</p>
<h1 data-id="heading-1">数据库准备</h1>
<hr>
<p>我准备的数据库是mysql,版本是5.7.35，太老的版本不支持主从复制，建议5.6版本以上大家自行下载即可。如果你安装的是比较新的版本，安装过程中可能会出现这个错误</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e5a0f668be145558f1c936f2cd5a4a4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>是因为新版本对密码的校验比较严格，只需要返回上一步重新输入密码重新check,让ckeck不通过一下然后在输入通过的密码就可以了，在回到这一步就应该能通过了。</p>
<h1 data-id="heading-2">数据库主从同步</h1>
<hr>
<p>安装完数据库之后咱得搞一套主从同步的机制，因为sharding jdbc只能路由到主库和从库，并不能实现主从数据的同步，主从的同步机制还是得依靠mysql自身的机制。开始搞。</p>
<h2 data-id="heading-3">1 新增mysql实例</h2>
<p>因为我主从全都在本机所以我复制了一份mysql文件如下图所示</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d0bf458cb8d4d58840bad1e96462d20~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
然后修改my.ini文件，然后你会发现目录下并没有my.ini文件</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c27549d244a540c6bd9d1df663674f66~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这就很尴尬了是吧，网上10个有9个半的主从复制都是目录下有my.ini文件的，不要急，这么整，因为新版本的mysql他的my.ini文件默认已经不在文件目录下了，在哪呢？ 在这</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f805017e7c0a452fad14562c67d99cb8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
但是这个ProgramData文件是隐藏的，所以你得设置一下隐藏文件可见。ok 咱复制一份含有ini文件的目录，如下</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ce14a911b5347bc9f286c575585ba36~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
取名为MySQL Server 5.7s1 和主库做一个区分，然后修改以下从库的my.ini文件</p>
<pre><code class="copyable">prot = 3307
basedir="C:/Program Files/MySQL/MySQL Server 5.7s1/"
datadir=C:/ProgramData/MySQL/MySQL Server 5.7s1/Data
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改完后把从库安装为windows服务，命令如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/492d882145f44e8ebea452ce60f0fef9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
然后就能在服务列表中看到了</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a11353224e84078b58574141511d0c7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">2 修改主库从库的ini文件，新增如下内容</h2>
<h3 data-id="heading-5">一、 主库</h3>
<pre><code class="copyable">#开启日志
log-bin=mysql-bin
#服务id 主从不能一致
server-id=1
#需要同步的数据库
binlog_do_db=ds0
binlog_do_db=ds1
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">二、从库</h3>
<pre><code class="copyable">#开启日志
log-bin=mysql-bin
#服务id 主从不能一致
server-id=2
#需要同步的数据库
replicate_wild_do_table=ds0.%
replicate_wild_do_table=ds1.%
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后重新启动主库和从库</p>
<h3 data-id="heading-7">三、主从复制授权账号</h3>
<pre><code class="copyable">登录主库后执行授权命令
grant replication slave on . to myslave@localhost identified by 'myslave';
然后刷新权限
FLUSH PRIVILEGES; 
然后看以下文件名和位点
show master status;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显示如下</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/782344e0e6364f1b909d20e8435e1310~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
记录一下file和position，配置从库的时候会用到。</p>
<h3 data-id="heading-8">四、设置从库同步主库数据</h3>
<pre><code class="copyable">#先停止从库
stop slave;
#修改从库指向主库
change master to 
master_host='localhost',
master_user='myslave',
master_password='myslave', 
master_log_file='mysql-bin.000006',
master_log_pos=15626542;
#启动
start slave;
#查看从库状态
show slave status;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显示如下</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94cfc217ec374759bd5b670c2fec8678~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当看见两个都是yes的时候就是主从同步成功了。如果你们从库是复制的主库的话这里的Slave_IO_Running应该为No,只需要把从库的Data下面的auto.cnf中的uuid改为和主库不一样就行了，如下</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6be1a237697f4b51a5c85fec2e6f61b1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">sharding-jdbc</h1>
<hr>
<p>数据库主从同步搭完了接下来开始搞sharding-jdbc。</p>
<h2 data-id="heading-10">一、springboot整合sharding-jdbc</h2>
<p>1.新建一个springboot工程，然后加入sharding-jdbc的jar包，具体pom文件如下所示</p>
<pre><code class="copyable"><?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xsi:schemaLocation="http://maven.apache.org/POM/4.0.0      https://maven.apache.org/xsd/maven-4.0.0.xsd">
<modelVersion>4.0.0</modelVersion>
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.5.2</version>
    <relativePath/> <!-- lookup parent from repository -->
</parent>
<groupId>com.example</groupId>
<artifactId>demo</artifactId>
<version>0.0.1-SNAPSHOT</version>
<name>liuxc-jdbc</name>
<description>Demo project for Spring Boot</description>
<properties>
    <java.version>1.8</java.version>
</properties>
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.mybatis.spring.boot</groupId>
        <artifactId>mybatis-spring-boot-starter</artifactId>
        <version>2.2.0</version>
    </dependency>

    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <scope>runtime</scope>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.httpcomponents</groupId>
        <artifactId>httpclient</artifactId>
        <version>4.5.5</version>
    </dependency>
    <dependency>
        <groupId>commons-codec</groupId>
        <artifactId>commons-codec</artifactId>
        <version>1.11</version>
    </dependency>
    <dependency>
        <groupId>com.google.code.gson</groupId>
        <artifactId>gson</artifactId>
        <version>2.8.5</version>
    </dependency>

    <dependency>
        <groupId>com.alibaba</groupId>
        <artifactId>fastjson</artifactId>
        <version>1.2.28</version>
    </dependency>
    <!-- https://mvnrepository.com/artifact/org.apache.shardingsphere/sharding-jdbc-core -->
    <dependency>
        <groupId>org.apache.shardingsphere</groupId>
        <artifactId>sharding-jdbc-spring-boot-starter</artifactId>
        <version>4.0.0</version>
    </dependency>
    <dependency>
        <groupId>com.alibaba</groupId>
        <artifactId>druid</artifactId>
        <version>1.1.10</version>
    </dependency>

</dependencies>

<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
    </plugins>
</build>
</project>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>项目的结构大致为</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/909e7748a2914a6eb4b6bdb122cdae0c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>要想使用sharding-jdbc，主要的一个工作就是配置分片规则，在配置分片规则之前我先创建一些库表，如图我在主库和从库中分别创建了两个库ds0和ds1，每个库中的表都是t_user1和t_user2</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f7ae4e378d0447e894704f3de21975c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后配置sharding-jdbc分片规则，在application.properties中进行配置</p>
<pre><code class="copyable">server.port=8080
spring.application.name=sharding-springboot


mybatis.mapper-locations=classpath:mapper/*.xml

spring.shardingsphere.datasource.names= m1,m2,s1,s2

spring.shardingsphere.datasource.m1.type= com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.m1.driver-class-name= com.mysql.jdbc.Driver
spring.shardingsphere.datasource.m1.url= jdbc:mysql://localhost:3306/ds0
spring.shardingsphere.datasource.m1.username= root
spring.shardingsphere.datasource.m1.password= root

spring.shardingsphere.datasource.s1.type= com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.s1.driver-class-name= com.mysql.jdbc.Driver
spring.shardingsphere.datasource.s1.url= jdbc:mysql://localhost:3307/ds0
spring.shardingsphere.datasource.s1.username= root
spring.shardingsphere.datasource.s1.password= root

spring.shardingsphere.datasource.m2.type= com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.m2.driver-class-name= com.mysql.jdbc.Driver
spring.shardingsphere.datasource.m2.url= jdbc:mysql://localhost:3306/ds1
spring.shardingsphere.datasource.m2.username= root
spring.shardingsphere.datasource.m2.password= root

spring.shardingsphere.datasource.s2.type= com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.s2.driver-class-name= com.mysql.jdbc.Driver
spring.shardingsphere.datasource.s2.url= jdbc:mysql://localhost:3307/ds1
spring.shardingsphere.datasource.s2.username= root
spring.shardingsphere.datasource.s2.password= root

#主库从库
spring.shardingsphere.sharding.master-slave-rules.ds1.master-data-source-name=m1
spring.shardingsphere.sharding.master-slave-rules.ds1.slave-data-source-names=s1

spring.shardingsphere.sharding.master-slave-rules.ds2.master-data-source-name=m2
spring.shardingsphere.sharding.master-slave-rules.ds2.slave-data-source-names=s2

#  库配置分片键和分片算法
spring.shardingsphere.sharding.default-database-strategy.inline.sharding-column=user_id
spring.shardingsphere.sharding.default-database-strategy.inline.algorithm-expression=ds$->&#123;user_id % 2+1&#125;
#  表配置分片键和分片算法
spring.shardingsphere.sharding.tables.t_user.actual-data-nodes=ds$->&#123;1..2&#125;.t_user$->&#123;1&#125;
spring.shardingsphere.sharding.tables.t_user.table-strategy.inline.sharding-column=user_id
spring.shardingsphere.sharding.tables.t_user.table-strategy.inline.algorithm-expression=t_user$->&#123;1&#125;
spring.shardingsphere.sharding.tables.t_user.key-generator.column=user_id
spring.shardingsphere.sharding.tables.t_user.key-generator.type=SNOWFLAKE

spring.shardingsphere.props.sql.show=true

logging.level.root=info
logging.level.org.springframework.web=info
<span class="copy-code-btn">复制代码</span></code></pre>
<p>m1、m2对应主库的ds0、ds1。
s1、s2对应从库的ds0、ds1。
主要介绍下主从的配置和分库分表的配置</p>
<pre><code class="copyable">#用master-data-source-name和slave-data-source-names来标明是主库和从库
spring.shardingsphere.sharding.master-slave-rules.ds1.master-data-source-name=m1  
spring.shardingsphere.sharding.master-slave-rules.ds1.slave-data-source-names=s1 
spring.shardingsphere.sharding.master-slave-rules.ds2.master-data-source-name=m2 
spring.shardingsphere.sharding.master-slave-rules.ds2.slave-data-source-names=s2

# 库配置分片键和分片算法  
spring.shardingsphere.sharding.default-database-strategy.inline.sharding-column=user_id 
spring.shardingsphere.sharding.default-database-strategy.inline.algorithm-expression=ds$->&#123;user_id % 2+1&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中ds$->&#123;user_id % 2+1&#125; 一种groovy语法 user_id为偶数 结果就是ds1,基数就为ds2，注意其中的ds1或ds2指的是如下的逻辑节点</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25eba9d89e0744559682a4c06d035397~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
分表的配置</p>
<pre><code class="copyable"># 表配置分片键和分片算法 
#指定表的分布情况，配置数据节点 目前只指点了一个表t_user1，要想指定t_user1和t_user2只需要
t_user$->&#123;1..2&#125;即可 
spring.shardingsphere.sharding.tables.t_user.actual-data-nodes=ds$->&#123;1..2&#125;.t_user$->&#123;1&#125; 

#指定表的分片键和分片算法
spring.shardingsphere.sharding.tables.t_user.table-strategy.inline.sharding-column=user_id  
spring.shardingsphere.sharding.tables.t_user.tablestrategy.inline.algorithm-expression=t_user$->&#123;1&#125; 

#指定表的主键生成策略为雪花算法
spring.shardingsphere.sharding.tables.t_user.key-generator.column=user_id  
spring.shardingsphere.sharding.tables.t_user.key-generator.type=SNOWFLAKE
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ok配置介绍完了，咱写个插入的方法，然后启动项目，看看效果，插入的方法如下</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4eb21f8ec647482281927cf667626155~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
注意一点 sql中的表名必须是逻辑表名，即为这个</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b11193443a204585863f24338991187e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc8094a832bd4f17a48ddcd4a1e96f6f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
然后咱们浏览器访问下看看</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cdfaf789d71448a6892bcc55903336ef~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>显示成功，咱去数据库看看</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dfa2d731a5c46d8a06c0adcb95c2230~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f525c59b0fd54bc7adc03700e03fb21d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>发现user_id为偶数的都在ds0的t_user1表中，user_id为奇数的都在ds1的t_user1表中，日志中也能看出数据全部插入了主库</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dadcc116ccd453fb502d5db31526ddd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后咱写一个查询的方法看看是不是从从库查出来的，偷个懒直接从主库中取一个id查询</p>
<pre><code class="copyable">@RequestMapping("/getUser")
@ResponseBody
public User getUser() &#123;
    User user = userMapper.get(633690716052127744l);
    return user;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看日志，说明是从从库查询的</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89227fbf38c448a1ba845566dca04a89~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
那说明咱们的sharding-jdbc 主从复制、读写分离就成功了，其实还有好知识点没涉及到，就像分片策略我们这里用的是inline,在之前的东家那里做医疗电商的时候我们用的是complex 复合分片策略的等等，每种策略的特点和用法等等，具体的大家就自行去学习吧。</p>
<h1 data-id="heading-11">mycat</h1>
<hr>
<h2 data-id="heading-12">1 下载mycat</h2>
<p>下载mycat之前需要确保安装jdk1.7以上版本，然后从官网下载mycat，下载后解压如下</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6367ac21a67b41bdb3597374ce150635~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>主要看conf下的三个文件</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6db7cbcc65d34421b899a98deffa3b88~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>1.server.xml</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/731dca5e51c247799dc1d75eb19a5819~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下载下来后，应该默认如上图，有一个逻辑库，名字为TESTDB,有两个用户，root和user,默认即可</p>
<p>2.schema.xml</p>
<pre><code class="copyable"><?xml version="1.0"?>
<!DOCTYPE mycat:schema SYSTEM "schema.dtd">
<mycat:schema xmlns:mycat="http://io.mycat/">

<schema name="TESTDB" checkSQLschema="false" sqlMaxLimit="100">
<!-- auto sharding by id (long)  rule="auto-sharding-long" -->
<table name="t_user1" primaryKey="user_id" dataNode="dn1,dn2" rule="crc32slot"/>
<table name="t_user2" primaryKey="user_id" dataNode="dn1,dn2" rule="crc32slot1"/>

</schema>

<dataNode name="dn1" dataHost="localhost1" database="ds0" />
<dataNode name="dn2" dataHost="localhost1" database="ds1" />

<dataHost name="localhost1" maxCon="1000" minCon="10" balance="1"
  writeType="0" dbType="mysql" dbDriver="native" switchType="1"  slaveThreshold="100">
<heartbeat>select user()</heartbeat>
<!-- can have multi write hosts -->
<writeHost host="hostM1" url="localhost:3306" user="root"
   password="root">
<!-- can have multi read hosts -->
<readHost host="hostS2" url="localhost:3307" user="root"                                     password="root" />
</writeHost>

</dataHost>
</mycat:schema>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上部分定义了表名、主键、分布节点和分片算法，下部分定义了读写的路由。这个大家一看就懂就不再赘述了。</p>
<p>3.rule.xml
该文件主要是定义分片规则，上面的crc32slot规则就是这个文件里面定义的，这里需要注意的点是如果有表用了这个方法那么就不能在用了，需要复制一份改个名字在用，就像下面这样</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a922a692828f4a8e86ff0adfefecb974~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">启动mycat</h2>
<p>管理员身份在bin目录下运行</p>
<pre><code class="copyable">mycat.bat install
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看服务列表</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7c2721bf4404ee4ac69903cd4d39497~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后用navicat登录一下 用户名 密码就是server.xml里面配置的</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41db9f9e816f42c2b11be97ea395fc65~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
登录mycat</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19702c8148b94bb59c439bdbe0bc77a3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行以下看看效果，在mycat中新增一条数据</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccfcb82941fd46d3912c59218a869927~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
发现它插入了主库的ds0里面的t_user1</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03803b568d854b9d8d64a2c0fef033ef~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
再插入一条</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9df0ae3bdfb74f03928c35f388dccd34~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
发现在ds1中多了一条</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da1b374dcd6f4bf981b8d836ecd3081d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
说明咱搞的mycat的分库分表没啥问题，mycat这部分其实写的比较笼统，准备的好多点都没有写进去，像balance赋值 0，1，2，3的各种区别等等 。主要是篇幅太长了，而且最后我还想用jmeter再来各自测以下着两种数据中间件，想深入研究的朋友们自己去学习吧。springboot集成mycat的话其实只需要把数据源换成mycat的就行如图</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab5ce496813b4643a50819be1fc3ac79~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-14">最后咱们用jmeter压一下这两种方式</h1>
<hr>
<h2 data-id="heading-15">sharding-jdbc</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c8d32eab06142f699fa1fbc49e84897~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a3e8e86299048fd9d2f29689d287aec~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>100个线程数循环10次，方法中每次插入10条数据，总共插入10000条数据，来咱试试</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84637f5b809b411b842661decd13d06b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
ds0中是4992条</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef4167d30af944408208c8cbd83ef23b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>ds1中是5008条</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e746f3ec24c4862a7d0f44d3843c5ca~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>吞吐量在116左右</p>
<h2 data-id="heading-16">mycat</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6beea8a4d7a74f87ac46f948f853ba4f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/794ea7bb723549eeb93584f450fcd3a2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
吞吐量在60多</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e8ea6d9bda742c6bf354f42761334c6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-17">总结</h1>
<p>哈哈看到这的都是帅仔。从测试数据来看mycat比sharding-jdbc还是差点，当然这和服务器的配置有很大关系，你们测的话可能就不一样了啊，我只是按照我测试的数据来说的，其实写这篇文章主要就是为了玩，所以大家不要太较真。接下来的计划是每周更一篇，下篇写啥还没想好，下周见吧</p></div>  
</div>
            