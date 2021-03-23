
---
title: 'Canal高可用架构部署'
categories: 
 - 编程
 - 掘金
 - — 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97cc55af205342548173e7132ff81ffe~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 21 Mar 2021 17:15:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97cc55af205342548173e7132ff81ffe~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="mark" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97cc55af205342548173e7132ff81ffe~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">一、前言</h2>
<p><code>canal</code> 是阿里的一款开源项目，纯 <code>Java</code> 开发。基于数据库增量日志解析，提供增量数据订阅&消费，目前主要支持了 <code>MySQL</code>(也支持 <code>mariaDB</code>)。
<img alt="file" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72c095df59284aaa9c29bdf1274c317a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol>
<li>canal 模拟 mysql slave 的交互协议，伪装自己为 mysql slave，向 mysql master发送 dump 协议；</li>
<li>mysql master 收到 dump 请求，开始推送binary log给 slave(也就是canal)</li>
<li>canal 解析 binary log对象(原始为byte流)。</li>
</ol>
<p> </p>
<p><strong>总体架构</strong>：</p>
<p><img alt="file" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fea908ae060a4556b7bb84614fc9ae4c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<h2 data-id="heading-1">二、部署准备</h2>
<p><strong>下载地址</strong>：
<a href="https://github.com/alibaba/canal/releases" target="_blank" rel="nofollow noopener noreferrer">github.com/alibaba/can…</a></p>
<p>分别下载：canal.admin、canal.deployer、canal.adapter</p>
<blockquote>
<p><strong>PS</strong>：只有1.1.5以上版本才支持es7.x</p>
</blockquote>
<p> </p>
<p><strong>其他依赖</strong>：</p>
<ol>
<li>JDK1.8</li>
<li>MySQL：用于canal-admin存储配置和节点等相关数据</li>
<li>Zookeeper</li>
</ol>
<p> </p>
<h2 data-id="heading-2">三、HA机制</h2>
<p>整个 HA 机制的控制主要是依赖了zookeeper的两个特性：watcher、EPHEMERAL节点。canal的 HA 机制实现分为两部分，canal server 和 canal client分别有对应的实现。
<img alt="file" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9d39bfcbe5e49d4911d4d9e66993d87~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>canal server实现流程如下：</strong></p>
<ol>
<li>canal server 要启动某个 canal instance 时都先向 zookeeper 进行一次尝试启动判断 (实现：创建 EPHEMERAL 节点，谁创建成功就允许谁启动）；</li>
<li>创建 zookeeper 节点成功后，对应的 canal server 就启动对应的 canal instance，没有创建成功的 canal instance 就会处于 standby 状态；</li>
<li>一旦 zookeeper 发现 canal server A 创建的节点消失后，立即通知其他的 canal server 再次进行步骤1的操作，重新选出一个 canal server 启动instance；</li>
<li>canal client 每次进行connect时，会首先向 zookeeper 询问当前是谁启动了canal instance，然后和其建立链接，一旦链接不可用，会重新尝试connect。</li>
</ol>
<p><strong>PS</strong>: 为了减少对mysql dump的请求，不同server上的instance要求同一时间只能有一个处于running，其他的处于standby状态。</p>
<p> </p>
<p><strong>canal client实现流程</strong></p>
<ol>
<li>canal client 的方式和 canal server 方式类似，也是利用 zookeeper 的抢占EPHEMERAL 节点的方式进行控制</li>
<li>为了保证有序性，一份 instance 同一时间只能由一个 canal client 进行get/ack/rollback操作，否则客户端接收无法保证有序。</li>
</ol>
<p> </p>
<h2 data-id="heading-3">四、集群部署</h2>
<h3 data-id="heading-4">4.1. MySQL准备</h3>
<h4 data-id="heading-5">4.1.1. 开启binlog</h4>
<p>MySQL的 <code>my.cnf</code> 中配置如下</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-attr">[mysqld]</span>
<span class="hljs-meta">log-bin</span>=<span class="hljs-string">mysql-bin # 开启 binlog</span>
<span class="hljs-meta">binlog-format</span>=<span class="hljs-string">ROW # 选择 ROW 模式</span>
<span class="hljs-attr">server_id</span>=<span class="hljs-string">1 # 配置 MySQL replaction 需要定义，不要和 canal 的 slaveId 重复</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意</strong>：如果订阅的是mysql的从库，需求增加配置让从库日志也写到binlog里面</p>
<pre><code class="hljs language-properties copyable" lang="properties"><span class="hljs-attr">log_slave_updates</span>=<span class="hljs-string">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以通过在 mysql 终端中执行以下命令判断配置是否生效：</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">show</span> variables <span class="hljs-keyword">like</span> <span class="hljs-string">'log_bin'</span>;
<span class="hljs-keyword">show</span> variables <span class="hljs-keyword">like</span> <span class="hljs-string">'binlog_format'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<h4 data-id="heading-6">4.1.2. 授权账号权限</h4>
<p>授权 canal 链接 MySQL 账号具有作为 MySQL slave 的权限, 如果已有账户可直接 grant：</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">CREATE</span> <span class="hljs-keyword">USER</span> canal IDENTIFIED <span class="hljs-keyword">BY</span> <span class="hljs-string">'canal'</span>;  
<span class="hljs-keyword">GRANT</span> <span class="hljs-keyword">SELECT</span>, REPLICATION SLAVE, REPLICATION CLIENT <span class="hljs-keyword">ON</span> <span class="hljs-operator">*</span>.<span class="hljs-operator">*</span> <span class="hljs-keyword">TO</span> <span class="hljs-string">'canal'</span>@<span class="hljs-string">'%'</span>;
FLUSH PRIVILEGES;
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<h3 data-id="heading-7">4.2. 部署canal-admin</h3>
<h4 data-id="heading-8">4.2.1. 作用</h4>
<ol>
<li>通过图形化界面管理配置参数。</li>
<li>动态启停 <code>Server</code> 和 <code>Instance</code></li>
<li>查看日志信息</li>
</ol>
<p> </p>
<h4 data-id="heading-9">4.2.2. 执行数据库脚本</h4>
<p>执行 <code>conf</code> 目录下载的 <code>canal_manager.sql</code> 脚步，初始化所需的库表。</p>
<blockquote>
<p>初始化SQL脚本里会默认创建canal_manager的数据库，建议使用root等有超级权限的账号进行初始化</p>
</blockquote>
<p> </p>
<h4 data-id="heading-10">4.2.3. 配置修改</h4>
<p>执行 <code>vim conf/application.yml</code></p>
<pre><code class="copyable">server:
  port: 8089
spring:
  jackson:
    date-format: yyyy-MM-dd HH:mm:ss
    time-zone: GMT+8

spring.datasource:
  address: 127.0.0.1:3306
  database: canal_manager
  username: canal
  password: canal
  driver-class-name: com.mysql.jdbc.Driver
  url: jdbc:mysql://$&#123;spring.datasource.address&#125;/$&#123;spring.datasource.database&#125;?useUnicode=true&characterEncoding=UTF-8&useSSL=false
  hikari:
    maximum-pool-size: 30
    minimum-idle: 1

canal:
  adminUser: admin
  adminPasswd: admin
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>修改 <code>address</code>、<code>database</code>、<code>username</code>、<code>password</code> 四个参数</p>
</blockquote>
<p> </p>
<h4 data-id="heading-11">4.2.4. 启停命令</h4>
<p>启动</p>
<pre><code class="hljs language-bash copyable" lang="bash">sh bin/startup.sh
<span class="copy-code-btn">复制代码</span></code></pre>
<p>停止</p>
<pre><code class="hljs language-bash copyable" lang="bash">sh bin/stop.sh
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<h4 data-id="heading-12">4.2.5. 使用</h4>
<p>通过 <a href="http://127.0.0.1:8089/" target="_blank" rel="nofollow noopener noreferrer">http://127.0.0.1:8089/</a> 访问，默认密码：admin/123456</p>
<h5 data-id="heading-13">4.2.5.1. 创建集群</h5>
<p>配置 <strong>集群名称</strong> 与 <strong>ZK地址</strong>
<img alt="file" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2732beb5b9e4d41b92a10c2d0224233~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<p>配置 <strong>主配置</strong>，该配置为集群内的所有Server实例共享的
<img alt="file" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26dc72f98e7f4c20b26be00f7afe9722~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
主要修改以下配置：</p>
<ul>
<li><strong>canal.zkServers</strong> 配置zookeeper集群地址</li>
<li><strong>canal.instance.global.spring.xml</strong> 改为classpath:spring/default-instance.xml</li>
</ul>
<p> </p>
<h5 data-id="heading-14">4.2.5.2. 创建Server</h5>
<p><img alt="file" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40ec09106e364060a5e14c7296b33e74~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
配置项：</p>
<ul>
<li>所属集群，可以选择为单机 或者 集群。一般单机Server的模式主要用于一次性的任务或者测试任务</li>
<li>Server名称，唯一即可，方便自己记忆</li>
<li>Server Ip，机器ip</li>
<li>admin端口，canal 1.1.4版本新增的能力，会在canal-server上提供远程管理操作，默认值11110</li>
<li>tcp端口，canal提供netty数据订阅服务的端口</li>
<li>metric端口， promethues的exporter监控数据端口 (未来会对接监控)</li>
</ul>
<blockquote>
<p>多台Server关联同一个集群即可形成主备HA架构</p>
</blockquote>
<p> </p>
<h5 data-id="heading-15">4.2.5.3. 创建Instance</h5>
<p>每个 <code>Instance</code> 关联一个同步的数据源，如果有多个数据源需要同步则需要创建多个 <strong>实例</strong>
<img alt="file" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22a7eea0825b4bf1a6deffe563352f29~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol>
<li>先填写实例名</li>
<li>选择刚刚创建的集群</li>
<li>载入模板配置</li>
</ol>
<p> </p>
<p>主要修改以下配置：</p>
<ul>
<li><strong>canal.instance.master.address</strong> 配置要同步的数据库地址</li>
<li><strong>canal.instance.dbUsername</strong> 数据库用户名（需同步权限）</li>
<li><strong>canal.instance.dbPassword</strong> 数据库密码</li>
<li><strong>canal.instance.filter.regex</strong> mysql 数据解析关注的表，Perl正则表达式.多个正则之间以逗号(,)分隔，转义符需要双斜杠(\)</li>
</ul>
<blockquote>
<p>canal.instance.filter.regex常见例子：</p>
<ol>
<li>所有表：.* or .<em>\..</em></li>
<li>canal schema下所有表： canal\..*</li>
<li>canal下的以canal打头的表：canal\.canal.*</li>
<li>canal schema下的一张表：canal.test1</li>
<li>多个规则组合使用：canal\..*,mysql.test1,mysql.test2 (逗号分隔)</li>
</ol>
<p>注意：此过滤条件只针对row模式的数据有效(ps. mixed/statement因为不解析sql，所以无法准确提取tableName进行过滤)</p>
</blockquote>
<p> </p>
<h3 data-id="heading-16">4.3. 部署canal-deployer</h3>
<h4 data-id="heading-17">4.3.1. 作用</h4>
<ol>
<li>伪装成 <code>MySQL</code> 的从库，同步主库的binlog日志。</li>
<li>解析并结构化 <code>binary log</code> 对象。</li>
</ol>
<p> </p>
<h4 data-id="heading-18">4.3.2. 修改配置</h4>
<p>执行 <code>vim conf/canal_local.properties</code> 修改配置项 <code>canal.admin.manager</code> 为canal-admin的地址</p>
<p> </p>
<h4 data-id="heading-19">4.3.3. 启停命令</h4>
<p>使用 <strong>local</strong> 配置启动</p>
<pre><code class="hljs language-bash copyable" lang="bash">bin/startup.sh <span class="hljs-built_in">local</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>停止</p>
<pre><code class="hljs language-bash copyable" lang="bash">bin/stop.sh
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<h3 data-id="heading-20">4.4. 部署canal-adapter</h3>
<h4 data-id="heading-21">4.4.1. 作用</h4>
<ol>
<li>对接上游消息，包括kafka、rocketmq、canal-server</li>
<li>实现mysql数据的增量同步</li>
<li>实现mysql数据的全量同步</li>
<li>下游写入支持mysql、es、hbase等</li>
</ol>
<p> </p>
<h4 data-id="heading-22">4.4.2. 修改配置</h4>
<blockquote>
<p><strong>注意</strong>：目前 <code>adapter</code> 是支持动态配置的，也就是说修改配置文件后无需重启，任务会自动刷新配置！</p>
</blockquote>
<p><strong>(1) 修改application.yml</strong></p>
<p>执行 <code>vim conf/application.yml</code> 修改consumerProperties、srcDataSources、canalAdapters的配置</p>
<pre><code class="hljs language-yml copyable" lang="yml"><span class="hljs-attr">canal.conf:</span>
  <span class="hljs-attr">mode:</span> <span class="hljs-string">tcp</span> <span class="hljs-comment"># kafka rocketMQ                # canal client的模式: tcp kafka rocketMQ</span>
  <span class="hljs-attr">flatMessage:</span> <span class="hljs-literal">true</span>                         <span class="hljs-comment"># 扁平message开关, 是否以json字符串形式投递数据, 仅在kafka/rocketMQ模式下有效</span>
  <span class="hljs-attr">syncBatchSize:</span> <span class="hljs-number">1000</span>                       <span class="hljs-comment"># 每次同步的批数量</span>
  <span class="hljs-attr">retries:</span> <span class="hljs-number">0</span>                                <span class="hljs-comment"># 重试次数, -1为无限重试</span>
  <span class="hljs-attr">timeout:</span>                                  <span class="hljs-comment"># 同步超时时间, 单位毫秒</span>
  <span class="hljs-attr">consumerProperties:</span>
    <span class="hljs-attr">canal.tcp.server.host:</span>                  <span class="hljs-comment"># 对应单机模式下的canal</span>
    <span class="hljs-attr">canal.tcp.zookeeper.hosts:</span> <span class="hljs-number">127.0</span><span class="hljs-number">.0</span><span class="hljs-number">.1</span><span class="hljs-string">:2181</span> <span class="hljs-comment"># 对应集群模式下的zk地址, 如果配置了canal.tcp.server.host, 则以canal.tcp.server.host为准</span>
    <span class="hljs-attr">canal.tcp.batch.size:</span> <span class="hljs-number">500</span>               <span class="hljs-comment"># tcp每次拉取消息的数量</span>
  <span class="hljs-attr">srcDataSources:</span>                           <span class="hljs-comment"># 源数据库</span>
    <span class="hljs-attr">defaultDS:</span>                              <span class="hljs-comment"># 自定义名称</span>
      <span class="hljs-attr">url:</span> <span class="hljs-string">jdbc:mysql://127.0.0.1:3306/mytest?useUnicode=true</span>   <span class="hljs-comment"># jdbc url </span>
      <span class="hljs-attr">username:</span> <span class="hljs-string">root</span>                                            <span class="hljs-comment"># jdbc 账号</span>
      <span class="hljs-attr">password:</span> <span class="hljs-number">121212</span>                                          <span class="hljs-comment"># jdbc 密码</span>
  <span class="hljs-attr">canalAdapters:</span>                            <span class="hljs-comment"># 适配器列表</span>
  <span class="hljs-bullet">-</span> <span class="hljs-attr">instance:</span> <span class="hljs-string">example</span>                       <span class="hljs-comment"># canal 实例名或者 MQ topic 名</span>
    <span class="hljs-attr">groups:</span>                                 <span class="hljs-comment"># 分组列表</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">groupId:</span> <span class="hljs-string">g1</span>                           <span class="hljs-comment"># 分组id, 如果是MQ模式将用到该值</span>
      <span class="hljs-attr">outerAdapters:</span>                        <span class="hljs-comment"># 分组内适配器列表</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">es7</span>                           <span class="hljs-comment"># es7适配器</span>
        <span class="hljs-attr">mode:</span> <span class="hljs-string">rest</span>                          <span class="hljs-comment"># transport or rest</span>
        <span class="hljs-attr">hosts:</span> <span class="hljs-number">127.0</span><span class="hljs-number">.0</span><span class="hljs-number">.1</span><span class="hljs-string">:9200</span>               <span class="hljs-comment"># es地址</span>
        <span class="hljs-attr">security.auth:</span> <span class="hljs-string">test:123456</span>          <span class="hljs-comment"># 访问es的认证信息，如没有则不需要填</span>
        <span class="hljs-attr">cluster.name:</span> <span class="hljs-string">my-es</span>                 <span class="hljs-comment"># 集群名称，transport模式必需配置</span>
<span class="hljs-string">......</span>           
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<ol>
<li>一份数据可以被多个group同时消费, 多个group之间会是一个并行执行, 一个group内部是一个串行执行多个outerAdapters, 比如例子中logger和hbase</li>
<li>目前client adapter数据订阅的方式支持两种，直连canal server 或者 订阅kafka/RocketMQ的消息</li>
</ol>
</blockquote>
<p> </p>
<p><strong>(2) conf/es7目录下新增映射配置文件</strong></p>
<blockquote>
<p>adapter将会自动加载 <code>conf/es7</code> 下的所有 <code>.yml</code> 结尾的配置文件</p>
</blockquote>
<p>新增表映射的配置文件，如 <code>sys_user.yml</code> 内容如下：</p>
<pre><code class="hljs language-yml copyable" lang="yml"><span class="hljs-attr">dataSourceKey:</span> <span class="hljs-string">defaultDS</span>
<span class="hljs-attr">destination:</span> <span class="hljs-string">example</span>
<span class="hljs-attr">groupId:</span> <span class="hljs-string">g1</span>
<span class="hljs-attr">esMapping:</span>
  <span class="hljs-attr">_index:</span> <span class="hljs-string">sys_user</span>
  <span class="hljs-attr">_id:</span> <span class="hljs-string">id</span>
  <span class="hljs-attr">upsert:</span> <span class="hljs-literal">true</span>
  <span class="hljs-attr">sql:</span> <span class="hljs-string">"select id, username, 
        , case when sex = 0 then '男' else '女' end sex
        , case when is_del = 0 then '否' else '是' end isdel
      from sys_user"</span>
  <span class="hljs-attr">etlCondition:</span> <span class="hljs-string">"where update_time>=&#123;&#125;"</span>
  <span class="hljs-attr">commitBatch:</span> <span class="hljs-number">3000</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>dataSourceKey</strong> 配置 <code>application.yml</code> 里 <code>srcDataSources</code> 的值</li>
<li><strong>destination</strong> 配置 <code>canal.deployer</code> 的 <code>Instance</code> 名</li>
<li><strong>groupId</strong> 配置 <code>application.yml</code> 里 <code>canalAdapters.groups</code> 的值</li>
<li><strong>_index</strong> 配置索引名</li>
<li><strong>_id</strong> 配置主键对应的字段</li>
<li><strong>upsert</strong> 是否更新</li>
<li><strong>sql</strong> 映射sql</li>
<li><strong>etlCondition</strong> etl 的条件参数，全量同步时可以使用</li>
<li><strong>commitBatch</strong> 提交批大小</li>
</ul>
<p>sql映射支持多表关联自由组合, 但是有一定的限制:</p>
<ol>
<li>主表不能为子查询语句</li>
<li>只能使用left outer join即最左表一定要是主表</li>
<li>关联从表如果是子查询不能有多张表</li>
<li>主sql中不能有where查询条件(从表子查询中可以有where条件但是不推荐, 可能会造成数据同步的不一致, 比如修改了where条件中的字段内容)</li>
<li>关联条件只允许主外键的'='操作不能出现其他常量判断比如: on a.role_id=b.id and b.statues=1</li>
<li>关联条件必须要有一个字段出现在主查询语句中比如: on a.role_id=b.id 其中的 a.role_id 或者 b.id 必须出现在主select语句中</li>
</ol>
<blockquote>
<p>Elastic Search的mapping 属性与sql的查询值将一一对应(不支持 select *), 比如: select a.id as _id, a.name, a.email as _email from user, 其中name将映射到es mapping的name field, _email将 映射到mapping的_email field, 这里以别名(如果有别名)作为最终的映射字段. 这里的_id可以填写到配置文件的 _id: _id映射</p>
</blockquote>
<p> </p>
<h4 data-id="heading-23">4.4.3. 启停命令</h4>
<p>启动</p>
<pre><code class="hljs language-bash copyable" lang="bash">bin/startup.sh
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关闭</p>
<pre><code class="hljs language-bash copyable" lang="bash">bin/stop.sh
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<h3 data-id="heading-24">4.5. 遗留问题</h3>
<p>目前使用的 <code>1.1.5-SNAPSHOT</code> 版本由于还不是发布版，发现 <code>canal-adapter</code> 的集群部署有个bug，配置 <code>zookeeper</code> 地址后启动会出现以下异常：</p>
<pre><code class="hljs language-bash copyable" lang="bash">java.lang.LinkageError: loader constraint violation: when resolving method <span class="hljs-string">"com.alibaba.otter.canal.common.zookeeper.ZkClientx.create(Ljava/lang/String;Ljava/lang/Object;Lorg/apache/zookeeper/CreateMode;)Ljava/lang/String;"</span> the class loader (instance of com/alibaba/otter/canal/connector/core/spi/URLClassExtensionLoader) of the current class, com/alibaba/otter/canal/client/impl/running/ClientRunningMonitor, and the class loader (instance of sun/misc/Launcher<span class="hljs-variable">$AppClassLoader</span>) <span class="hljs-keyword">for</span> the method<span class="hljs-string">'s defining class, org/I0Itec/zkclient/ZkClient, have different Class objects for the type org/apache/zookeeper/CreateMode used in the signature
at com.alibaba.otter.canal.client.impl.running.ClientRunningMonitor.initRunning(ClientRunningMonitor.java:122) [connector.tcp-1.1.5-SNAPSHOT-jar-with-dependencies.jar:na]
at com.alibaba.otter.canal.client.impl.running.ClientRunningMonitor.start(ClientRunningMonitor.java:93) [connector.tcp-1.1.5-SNAPSHOT-jar-with-dependencies.jar:na]
at com.alibaba.otter.canal.client.impl.SimpleCanalConnector.connect(SimpleCanalConnector.java:108) [connector.tcp-1.1.5-SNAPSHOT-jar-with-dependencies.jar:na]
at com.alibaba.otter.canal.client.impl.ClusterCanalConnector.connect(ClusterCanalConnector.java:64) [connector.tcp-1.1.5-SNAPSHOT-jar-with-dependencies.jar:na]
at com.alibaba.otter.canal.connector.tcp.consumer.CanalTCPConsumer.connect(CanalTCPConsumer.java:59) [connector.tcp-1.1.5-SNAPSHOT-jar-with-dependencies.jar:na]
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<p>有以下3个解决思路：</p>
<ol>
<li>adapter暂时使用单实例模式，等待官方解决问题。</li>
<li>自行修复bug</li>
<li>使用 <code>MQ</code> 模式（adapter则无需注册到zookeeper了）</li>
</ol>
<blockquote>
<p>该 <strong>BUG</strong> 已修复：<a href="https://github.com/zlt2000/canal" target="_blank" rel="nofollow noopener noreferrer">github.com/zlt2000/can…</a></p>
</blockquote>
<p> </p>
<h3 data-id="heading-25">五、监控</h3>
<p><code>canal</code> 默认已通过 <code>11112</code> 端口暴露同步相关的 <code>metrics</code> 信息，只需通过集成 <code>prometheus</code> 与 <code>grafana</code> 即可实现实时监控同步情况，效果图如下：</p>
<p><img alt="file" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75b6e63db1fe4616be2201dfdb670871~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>





























































<table><thead><tr><th>指标</th><th>简述</th></tr></thead><tbody><tr><td>Basic</td><td>Canal instance 基本信息。</td></tr><tr><td>Network bandwith</td><td>网络带宽。包含inbound(canal server读取binlog的网络带宽)和outbound(canal server返回给canal client的网络带宽)。</td></tr><tr><td>Delay</td><td>Canal server与master延时；store 的put, get, ack操作对应的延时。</td></tr><tr><td>Blocking</td><td>sink线程blocking占比；dump线程blocking占比(仅parallel mode)。</td></tr><tr><td>TPS(events)</td><td>Canal instance消费所有binlog事件的TPS， 以MySQL binlog events为单位计算。</td></tr><tr><td>TPS(transaction)</td><td>Canal instance 处理binlog的TPS，以MySQL transaction为单位计算。</td></tr><tr><td>TPS(tableRows)</td><td>分别对应store的put, get, ack操作针对数据表变更行的TPS。</td></tr><tr><td>Client requests</td><td>Canal client请求server的请求数统计，结果按请求类型分类(比如get/ack/sub/rollback等)。</td></tr><tr><td>Client QPS</td><td>client发送请求的QPS，按GET与CLIENTACK分类统计。</td></tr><tr><td>Empty packets</td><td>Canal client请求server返回空结果的统计。</td></tr><tr><td>Response time</td><td>Canal client请求server的响应时间统计。</td></tr><tr><td>Store remain events</td><td>Canal instance ringbuffer中堆积的events数量。</td></tr><tr><td>Store remain mem</td><td>Canal instance ringbuffer中堆积的events内存使用量。</td></tr></tbody></table>
<p> </p>
<h3 data-id="heading-26">六、总结</h3>
<ol>
<li>准备MySQL
<ul>
<li>开启binlog（row模式）</li>
<li>准备同步权限的用户</li>
<li>创建canal-admin的库表</li>
</ul>
</li>
<li>准备zookeeper</li>
<li>部署canal-admin
<ul>
<li>创建集群</li>
<li>创建server：关联集群</li>
<li>创建Instance：关联集群，并配置源库信息</li>
</ul>
</li>
<li>启动canal-deployer
<ul>
<li>关联canal-admin</li>
</ul>
</li>
<li>启动canal-adapter
<ul>
<li>关联zookeeper</li>
<li>配置源库信息</li>
<li>关联Instance</li>
<li>配置目标库信息(es)</li>
<li>新增映射配置文件</li>
</ul>
</li>
</ol>
<p> </p>
<p><strong>扫码关注有惊喜！</strong></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            