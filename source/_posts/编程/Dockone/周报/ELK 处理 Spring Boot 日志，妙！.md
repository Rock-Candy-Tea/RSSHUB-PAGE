
---
title: 'ELK 处理 Spring Boot 日志，妙！'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/0018349a14c00bfeac7fe7107f3cd569.jpg'
author: Dockone
comments: false
date: 2021-09-08 05:06:11
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/0018349a14c00bfeac7fe7107f3cd569.jpg'
---

<div>   
<br>在排查线上异常的过程中，查询日志总是必不可缺的一部分。现今大多采用的微服务架构，日志被分散在不同的机器上，使得日志的查询变得异常困难。工欲善其事，必先利其器。如果此时有一个统一的实时日志分析平台，那可谓是雪中送碳，必定能够提高我们排查线上问题的效率。本文带您了解一下开源的实时日志分析平台 ELK 的搭建及使用。<br>
<h3>ELK 简介</h3>ELK 是一个开源的实时日志分析平台，它主要由 Elasticsearch、Logstash 和 Kiabana 三部分组成。<br>
<h4>Logstash</h4>Logstash 主要用于收集服务器日志，它是一个开源数据收集引擎，具有实时管道功能。Logstash 可以动态地将来自不同数据源的数据统一起来，并将数据标准化到您所选择的目的地。<br>
<br>Logstash 收集数据的过程主要分为以下三个部分：<br>
<ul><li>输入：数据（包含但不限于日志）往往都是以不同的形式、格式存储在不同的系统中，而 Logstash 支持从多种数据源中收集数据（File、Syslog、MySQL、消息中间件等等）。</li><li>过滤器：实时解析和转换数据，识别已命名的字段以构建结构，并将它们转换成通用格式。</li><li>输出：Elasticsearch 并非存储的唯一选择，Logstash 提供很多输出选择。</li></ul><br>
<br><h4>Elasticsearch</h4>Elasticsearch（ES）是一个分布式的 Restful 风格的搜索和数据分析引擎，它具有以下特点：<br>
<ul><li>查询：允许执行和合并多种类型的搜索 — 结构化、非结构化、地理位置、度量指标 — 搜索方式随心而变。</li><li>分析：Elasticsearch 聚合让您能够从大处着眼，探索数据的趋势和模式。</li><li>速度：很快，可以做到亿万级的数据，毫秒级返回。</li><li>可扩展性：可以在笔记本电脑上运行，也可以在承载了 PB 级数据的成百上千台服务器上运行。</li><li>弹性：运行在一个分布式的环境中，从设计之初就考虑到了这一点。</li><li>灵活性：具备多个案例场景。支持数字、文本、地理位置、结构化、非结构化，所有的数据类型都欢迎。</li></ul><br>
<br><h4>Kibana</h4>Kibana 可以使海量数据通俗易懂。它很简单，基于浏览器的界面便于您快速创建和分享动态数据仪表板来追踪 Elasticsearch 的实时数据变化。其搭建过程也十分简单，您可以分分钟完成 Kibana 的安装并开始探索 Elasticsearch 的索引数据 — 没有代码、不需要额外的基础设施。<br>
<br>对于以上三个组件在 《ELK 协议栈介绍及体系结构》 一文中有具体介绍，这里不再赘述。<br>
<br>在 ELK 中，三大组件的大概工作流程如下图所示，由 Logstash 从各个服务中采集日志并存放至 Elasticsearch 中，然后再由 Kiabana 从 Elasticsearch 中查询日志并展示给终端用户。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/0018349a14c00bfeac7fe7107f3cd569.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/0018349a14c00bfeac7fe7107f3cd569.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 1. ELK 的大致工作流程</em><br>
<h3>ELK 实现方案</h3>通常情况下我们的服务都部署在不同的服务器上，那么如何从多台服务器上收集日志信息就是一个关键点了。本篇文章中提供的解决方案如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/c5112c97445132f375090906fd7369a5.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/c5112c97445132f375090906fd7369a5.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 2. 本文提供的 ELK 实现方案</em><br>
<br>如上图所示，整个 ELK 的运行流程如下：<br>
<ol><li>在微服务（产生日志的服务）上部署一个 Logstash，作为 Shipper 角色，主要负责对所在机器上的服务产生的日志文件进行数据采集，并将消息推送到 Redis 消息队列。</li><li>另用一台服务器部署一个 Indexer 角色的 Logstash，主要负责从 Redis 消息队列中读取数据，并在 Logstash 管道中经过 Filter 的解析和处理后输出到 Elasticsearch 集群中存储。</li><li>Elasticsearch 主副节点之间数据同步。</li><li>单独一台服务器部署 Kibana 读取 Elasticsearch 中的日志数据并展示在 Web 页面。</li></ol><br>
<br>通过这张图，相信您已经大致清楚了我们将要搭建的 ELK 平台的工作流程，以及所需组件。下面就让我们一起开始搭建起来吧。<br>
<h3>ELK 平台搭建</h3>本节主要介绍搭建 ELK 日志平台，包括安装 Indexer 角色的 Logstash，Elasticsearch 以及 Kibana 三个组件。完成本小节，您需要做如下准备：<br>
<ol><li>一台 Ubuntu 机器或虚拟机，作为入门教程，此处省略了 Elasticsearch 集群的搭建，且将 Logstash（Indexer）、Elasticsearch 以及 Kibana 安装在同一机器上。</li><li>在 Ubuntu 上安装 JDK，注意 Logstash 要求 JDK 在 1.7 版本以上。</li><li>Logstash、Elasticsearch、Kibana 安装包，您可以在 此页面 下载。</li></ol><br>
<br><h4>安装 Logstash</h4>解压压缩包：<br>
<pre class="prettyprint">tar -xzvf logstash-7.3.0.tar.gz<br>
</pre><br>
显示更多简单用例测试，进入到解压目录，并启动一个将控制台输入输出到控制台的管道。<br>
<pre class="prettyprint">cd logstash-7.3.0  <br>
elk@elk:~/elk/logstash-7.3.0$ bin/logstash -e 'input &#123; stdin &#123;&#125; &#125; output &#123; &#123; stdout &#123;&#125; &#125; &#125;'<br>
</pre><br>
显示更多看到如下日志就意味着 Logstash 启动成功。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/6727f4d3cc18878bcec17f9e95b943e8.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/6727f4d3cc18878bcec17f9e95b943e8.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 3. Logstash 启动成功日志</em><br>
<br>在控制台输入 Hello Logstash ，看到如下效果代表 Logstash 安装成功。<br>
<pre class="prettyprint">&#123;  <br>
"@timestamp" =&gt; 2019-08-10T16:11:10.040Z,  <br>
      "host" =&gt; "elk",  <br>
  "@version" =&gt; "1",  <br>
   "message" =&gt; "Hello Logstash"  <br>
&#125; <br>
</pre><br>
<em>清单 1. 验证 Logstash 是否启动成功Hello Logstash</em><br>
<h4>安装 Elasticsearch</h4>解压安装包：<br>
<pre class="prettyprint">tar -xzvf elasticsearch-7.3.0-linux-x86_64.tar.gz<br>
</pre><br>
启动 Elasticsearch：<br>
<pre class="prettyprint">cd elasticsearch-7.3.0/  <br>
bin/elasticsearch<br>
</pre><br>
在启动 Elasticsearch 的过程中我遇到了两个问题在这里列举一下，方便大家排查。<br>
<br>问题一 ：内存过小，如果您的机器内存小于 Elasticsearch 设置的值，就会报下图所示的错误。解决方案是，修改 elasticsearch-7.3.0/config/jvm.options 文件中的如下配置为适合自己机器的内存大小，若修改后还是报这个错误，可重新连接服务器再试一次。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/948c64c99206fb9a144770b8f654a8d1.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/948c64c99206fb9a144770b8f654a8d1.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 4. 内存过小导致 Elasticsearch 启动报错</em><br>
<br>问题二 ，如果您是以 root 用户启动的话，就会报下图所示的错误。解决方案自然就是添加一个新用户启动 Elasticsearch，至于添加新用户的方法网上有很多，这里就不再赘述。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/077772ee2d965254c9ff475fd0f65fb5.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/077772ee2d965254c9ff475fd0f65fb5.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 5. Root 用户启动 Elasticsearch 报错</em><br>
<br>启动成功后，另起一个会话窗口执行 curl <a href="http://localhost:9200/" rel="nofollow" target="_blank">http://localhost:9200</a> 命令，如果出现如下结果，则代表 Elasticsearch 安装成功。<br>
<pre class="prettyprint">elk@elk:~$ curl http://localhost:9200  <br>
&#123;  <br>
"name" : "elk",  <br>
"cluster_name" : "elasticsearch",  <br>
"cluster_uuid" : "hqp4Aad0T2Gcd4QyiHASmA",  <br>
"version" : &#123;  <br>
"number" : "7.3.0",  <br>
"build_flavor" : "default",  <br>
"build_type" : "tar",  <br>
"build_hash" : "de777fa",  <br>
"build_date" : "2019-07-24T18:30:11.767338Z",  <br>
"build_snapshot" : false,  <br>
"lucene_version" : "8.1.0",  <br>
"minimum_wire_compatibility_version" : "6.8.0",  <br>
"minimum_index_compatibility_version" : "6.0.0-beta1"  <br>
&#125;,  <br>
"tagline" : "You Know, for Search"  <br>
&#125; <br>
</pre><br>
<em>清单 2. 检查 Elasticsearch 是否启动成功</em><br>
<h4>安装 Kibana</h4>解压安装包：<br>
<pre class="prettyprint">tar -xzvf kibana-7.3.0-linux-x86_64.tar.gz<br>
</pre><br>
修改配置文件 config/kibana.yml ，主要指定 Elasticsearch 的信息。<br>
<pre class="prettyprint">elasticsearch.hosts: "http://ip:9200"  <br>
# 允许远程访问  <br>
server.host: "0.0.0.0"  <br>
# Elasticsearch 用户名 这里其实就是我在服务器启动 Elasticsearch 的用户名  <br>
elasticsearch.username: "es"  <br>
# Elasticsearch 鉴权密码 这里其实就是我在服务器启动 Elasticsearch 的密码  <br>
elasticsearch.password: "es"<br>
</pre><br>
<em>清单 3. Kibana 配置信息 #Elasticsearch 主机地址</em><br>
<br>启动 Kibana：<br>
<pre class="prettyprint">cd kibana-7.3.0-linux-x86_64/bin  <br>
./kibana<br>
</pre> <br>
在浏览器中访问 <a href="http://ip:5601/" rel="nofollow" target="_blank">http://ip:5601</a> ，若出现以下界面，则表示 Kibana 安装成功。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/65e69b67663bced801869e9146831dc9.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/65e69b67663bced801869e9146831dc9.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 6. Kibana 启动成功界面</em><br>
<br>ELK 日志平台安装完成后，下面我们就将通过具体的例子来看下如何使用 ELK，下文将分别介绍如何将 Spring Boot 日志和 Nginx 日志交由 ELK 分析。<br>
<h3>在 Spring Boot 中使用 ELK</h3>首先我们需要创建一个 Spring Boot 的项目，之前我写过一篇文章介绍如何使用 AOP 来统一处理 Spring Boot 的 Web 日志 ，本文的 Spring Boot 项目就建立在这篇文章的基础之上。<br>
<h4>修改并部署 Spring Boot 项目</h4>在项目 resources 目录下创建 spring-logback.xml 配置文件。<br>
<pre class="prettyprint"><?xml version="1.0" encoding="UTF-8"?>  <br>
<configuration debug="false">  <br>
<contextName>Logback For demo Mobile</contextName>  <br>
<property name="LOG_HOME" value="/log" />  <br>
<springProperty scope="context" name="appName" source="spring.application.name"  <br>
                defaultValue="localhost" />  <br>
...  <br>
<br>
<appender name="ROLLING_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">  <br>
    ...  <br>
    <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">  <br>
        <pattern>%d&#123;yyyy-MM-dd HH:mm:ss.SSS&#125; [%thread] %-5level %logger&#123;25&#125; $&#123;appName&#125; -%msg%n</pattern>  <br>
    </encoder>  <br>
    ...  <br>
</appender>  <br>
...  <br>
</configuration> <br>
</pre><br>
<em>清单 4. Spring Boot 项目 Logback 的配置</em><br>
<br>以上内容省略了很多内容，您可以在源码中获取。在上面的配置中我们定义了一个名为 ROLLING_FILE 的 Appender 往日志文件中输出指定格式的日志。而上面的 pattern 标签正是具体日志格式的配置，通过上面的配置，我们指定输出了时间、线程、日志级别、logger（通常为日志打印所在类的全路径）以及服务名称等信息。<br>
<br>将项目打包，并部署到一台 Ubuntu 服务器上。<br>
<pre class="prettyprint"># 打包命令  <br>
mvn package -Dmaven.test.skip=true  <br>
# 部署命令  <br>
java -jar sb-elk-start-0.0.1-SNAPSHOT.jar<br>
</pre><br>
<em>清单 5. 打包并部署 Spring Boot 项目</em><br>
<br>查看日志文件， logback 配置文件中我将日志存放在 /log/sb-log.log 文件中，执行 more/log/sb-log.log 命令，出现以下结果表示部署成功。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/fda4ac2126bbf47ac3db522fc3bdb514.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/fda4ac2126bbf47ac3db522fc3bdb514.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 7. Spring Boot 日志文件</em><br>
<h4>配置 Shipper 角色 Logstash</h4>Spring Boot 项目部署成功之后，我们还需要在当前部署的机器上安装并配置 Shipper 角色的 Logstash。Logstash 的安装过程在 ELK 平台搭建小节中已有提到，这里不再赘述。安装完成后，我们需要编写 Logstash 的配置文件，以支持从日志文件中收集日志并输出到 Redis 消息管道中，Shipper 的配置如下所示。<br>
<pre class="prettyprint">input &#123;  <br>
file &#123;  <br>
    path => [  <br>
        # 这里填写需要监控的文件  <br>
        "/log/sb-log.log"  <br>
    ]  <br>
&#125;  <br>
&#125;  <br>
<br>
output &#123;  <br>
# 输出到 Redis  <br>
redis &#123;  <br>
    host => "10.140.45.190"   # Redis主机地址  <br>
    port => 6379              # Redis端口号  <br>
    db => 8                   # Redis数据库编号  <br>
    data_type => "channel"    # 使用发布/订阅模式  <br>
    key => "logstash_list_0"  # 发布通道名称  <br>
&#125;  <br>
&#125; <br>
</pre><br>
<em>清单 6. Shipper 角色的 Logstash 的配置</em><br>
<br>其实 Logstash 的配置是与前面提到的 Logstash 管道中的三个部分（输入、过滤器、输出）一一对应的，只不过这里我们不需要过滤器所以就没有写出来。上面配置中 Input 使用的数据源是文件类型的，只需要配置上需要收集的本机日志文件路径即可。Output 描述数据如何输出，这里配置的是输出到 Redis。<br>
<br>Redis 的配置 data_type 可选值有 channel 和 list 两个。channel 是 Redis 的发布/订阅通信模式，而 list 是 Redis 的队列数据结构，两者都可以用来实现系统间有序的消息异步通信。channel 相比 list 的好处是，解除了发布者和订阅者之间的耦合。举个例子，一个 Indexer 在持续读取 Redis 中的记录，现在想加入第二个 Indexer，如果使用 list ，就会出现上一条记录被第一个 Indexer 取走，而下一条记录被第二个 Indexer 取走的情况，两个 Indexer 之间产生了竞争，导致任何一方都没有读到完整的日志。channel 就可以避免这种情况。这里 Shipper 角色的配置文件和下面将要提到的 Indexer 角色的配置文件中都使用了 channel 。<br>
<h4>配置 Indexer 角色 Logstash</h4>配置好 Shipper 角色的 Logstash 后，我们还需要配置 Indexer 角色 Logstash 以支持从 Redis 接收日志数据，并通过过滤器解析后存储到 Elasticsearch 中，其配置内容如下所示。<br>
<pre class="prettyprint">input &#123;  <br>
redis &#123;  <br>
    host      => "192.168.142.131"    # Redis主机地址  <br>
    port      => 6379               # Redis端口号  <br>
    db        => 8                  # Redis数据库编号  <br>
    data_type => "channel"          # 使用发布/订阅模式  <br>
    key       => "sb-logback"  # 发布通道名称  <br>
&#125;  <br>
&#125;  <br>
<br>
filter &#123;  <br>
 #定义数据的格式  <br>
 grok &#123;  <br>
   match => &#123; "message" => "%&#123;TIMESTAMP_ISO8601:time&#125; \[%&#123;NOTSPACE:threadName&#125;\] %&#123;LOGLEVEL:level&#125;  %&#123;DATA:logger&#125; %&#123;NOTSPACE:applicationName&#125; -(?:.*=%&#123;NUMBER:timetaken&#125;ms|)"&#125;  <br>
 &#125;  <br>
&#125;  <br>
<br>
output &#123;  <br>
stdout &#123;&#125;  <br>
elasticsearch &#123;  <br>
    hosts => "localhost:9200"  <br>
    index => "logback"  <br>
&#125;  <br>
&#125; <br>
</pre><br>
<em>清单 7. Indexer 角色的 Logstash 的配置</em><br>
<br>与 Shipper 不同的是，Indexer 的管道中我们定义了过滤器，也正是在这里将日志解析成结构化的数据。下面是我截取的一条 logback 的日志内容：<br>
<pre class="prettyprint">2019-08-11 18:01:31.602 [http-nio-8080-exec-2] INFO  c.i.s.aop.WebLogAspect sb-elk -接口日志  <br>
POST 请求测试接口结束调用:耗时=11ms,result=BaseResponse&#123;code=10000, message='操作成功'&#125; <br>
</pre> <br>
<em>清单 8. Spring Boot 项目输出的一条日志</em><br>
<br>在 Filter 中我们使用 Grok 插件从上面这条日志中解析出了时间、线程名称、Logger、服务名称以及接口耗时几个字段。Grok 又是如何工作的呢？<br>
<ol><li>message 字段是 Logstash 存放收集到的数据的字段， match = &#123;"message" => ...&#125; 代表是对日志内容做处理。</li><li>Grok 实际上也是通过正则表达式来解析数据的，上面出现的 TIMESTAMP_ISO8601、NOTSPACE 等都是 Grok 内置的 patterns。</li><li>我们编写的解析字符串可以使用 Grok Debugger 来测试是否正确，这样避免了重复在真实环境中校验解析规则的正确性。</li></ol><br>
<br><h4>查看效果</h4>经过上面的步骤，我们已经完成了整个 ELK 平台的搭建以及 Spring Boot 项目的接入。下面我们按照以下步骤执行一些操作来看下效果。<br>
<br>启动 Elasticsearch，启动命令在 ELK 平台搭建 小节中有提到，这里不赘述（Kibana 启动同）。启动 Indexer 角色的 Logstash。<br>
<pre class="prettyprint"># 进入到 Logstash 的解压目录，然后执行下面的命令  <br>
bin/logstash -f indexer-logstash.conf<br>
</pre><br>
启动 Kibana。<br>
<br>启动 Shipper 角色的 Logstash。<br>
<pre class="prettyprint"># 进入到 Logstash 的解压目录，然后执行下面的命令  <br>
bin/logstash -f shipper-logstash.conf<br>
</pre><br>
调用 Spring Boot 接口，此时应该已经有数据写入到 ES 中了。<br>
<br>在浏览器中访问 <a href="http://ip:5601/" rel="nofollow" target="_blank">http://ip:5601</a> ，打开 Kibana 的 Web 界面，并且如下图所示添加 logback 索引。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/ae0a0c017ce543c694956ede54e8072d.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/ae0a0c017ce543c694956ede54e8072d.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 8. 在 Kibana 中添加 Elasticsearch 索引</em><br>
<br>进入 Discover 界面，选择 logback 索引，就可以看到日志数据了，如下图所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/47c8079c96cebce6066d390f4c129a76.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/47c8079c96cebce6066d390f4c129a76.jpg" class="img-polaroid" title="9.jpg" alt="9.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 9. ELK 日志查看</em><br>
<h3>在 Nginx 中使用 ELK</h3>相信通过上面的步骤您已经成功的搭建起了自己的 ELK 实时日志平台，并且接入了 Logback 类型的日志。但是实际场景下，几乎不可能只有一种类型的日志，下面我们就再在上面步骤的基础之上接入 Nginx 的日志。当然这一步的前提是我们需要在服务器上安装 Nginx，具体的安装过程网上有很多介绍，这里不再赘述。查看 Nginx 的日志如下（Nginx 的访问日志默认在 /var/log/nginx/access.log 文件中）。<br>
<pre class="prettyprint">192.168.142.1 - - [17/Aug/2019:21:31:43 +0800] "GET /weblog/get-test?name=elk HTTP/1.1"  <br>
200 3 "http://192.168.142.131/swagger-ui.html" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)  <br>
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"<br>
</pre><br>
<em>清单 9. Nginx 的访问日志</em><br>
<br>同样，我们需要为此日志编写一个 Grok 解析规则，如下所示：<br>
<pre class="prettyprint">%&#123;IPV4:ip&#125; \- \- \[%&#123;HTTPDATE:time&#125;\] "%&#123;NOTSPACE:method&#125; %&#123;DATA:requestUrl&#125;  <br>
HTTP/%&#123;NUMBER:httpVersion&#125;" %&#123;NUMBER:httpStatus&#125; %&#123;NUMBER:bytes&#125;  <br>
"%&#123;DATA:referer&#125;" "%&#123;DATA:agent&#125;"<br>
</pre><br>
<em>清单 10. 针对 Nginx 访问日志的 Grok 解析规则</em><br>
<br>完成上面这些之后的关键点是 Indexer 类型的 Logstash 需要支持两种类型的输入、过滤器以及输出，如何支持呢？首先需要给输入指定类型，然后再根据不同的输入类型走不同的过滤器和输出，如下所示（篇幅原因，配置文件在此没有全部展示，可以 点击此处获取 ）。<br>
<pre class="prettyprint">input &#123;  <br>
redis &#123;  <br>
    type      => "logback"  <br>
    ...  <br>
&#125;  <br>
redis &#123;  <br>
   type       => "nginx"  <br>
   ...  <br>
&#125;  <br>
&#125;  <br>
<br>
filter &#123;  <br>
 if [type] == "logback" &#123;  <br>
     ...  <br>
 &#125;  <br>
 if [type] == "nginx" &#123;  <br>
     ...  <br>
 &#125;  <br>
&#125;  <br>
<br>
output &#123;  <br>
if [type] == "logback" &#123;  <br>
    ...  <br>
&#125;  <br>
if [type] == "nginx" &#123;  <br>
   ...  <br>
&#125;  <br>
&#125; <br>
</pre><br>
<em>清单 11. 支持两种日志输入的 Indexer 角色的 Logstash 配置</em><br>
<br>我的 Nginx 与 Spring Boot 项目部署在同一台机器上，所以还需修改 Shipper 类型的 Logstash 的配置以支持两种类型的日志输入和输出，其配置文件的内容可 点击这里获取 。以上配置完成后，我们按照 查看效果 章节中的步骤，启动 ELK 平台、Shipper 角色的 Logstash、Nginx 以及 Spring Boot 项目,然后在 Kibana 上添加 Nignx 索引后就可同时查看 Spring Boot 和 Nginx 的日志了，如下图所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/f30928a569d549029ed32a7c9a6fac60.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/f30928a569d549029ed32a7c9a6fac60.jpg" class="img-polaroid" title="10.jpg" alt="10.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 10. ELK 查看 Nginx 日志</em><br>
<h3>ELK 启动</h3>在上面的步骤中，ELK 的启动过程是我们一个一个的去执行三大组件的启动命令的。而且还是在前台启动的，意味着如果我们关闭会话窗口，该组件就会停止导致整个 ELK 平台无法使用，这在实际工作过程中是不现实的，我们剩下的问题就在于如何使 ELK 在后台运行。根据 《Logstash 最佳实践》 一书的推荐，我们将使用 Supervisor 来管理 ELK 的启停。首先我们需要安装 Supervisor，在 Ubuntu 上执行 apt-get install supervisor 即可。安装成功后，我们还需要在 Supervisor 的配置文件中配置 ELK 三大组件（其配置文件默认为 /etc/supervisor/supervisord.conf 文件）。<br>
<pre class="prettyprint">[program:elasticsearch]  <br>
environment=JAVA_HOME="/usr/java/jdk1.8.0_221/"  <br>
directory=/home/elk/elk/elasticsearch  <br>
user=elk  <br>
command=/home/elk/elk/elasticsearch/bin/elasticsearch  <br>
<br>
[program:logstash]  <br>
environment=JAVA_HOME="/usr/java/jdk1.8.0_221/"  <br>
directory=/home/elk/elk/logstash  <br>
user=elk  <br>
command=/home/elk/elk/logstash/bin/logstash -f /home/elk/elk/logstash/indexer-logstash.conf  <br>
<br>
[program:kibana]  <br>
environment=LS_HEAP_SIZE=5000m  <br>
directory=/home/elk/elk/kibana  <br>
user=elk  <br>
command=/home/elk/elk/kibana/bin/kibana<br>
</pre><br>
<em>清单 12. ELK 后台启动</em><br>
<br>按照以上内容配置完成后，执行 sudo supervisorctl reload 即可完成整个 ELK 的启动，而且其默认是开机自启。当然，我们也可以使用 sudo supervisorctl start/stop [program_name] 来管理单独的应用。<br>
<h3>结束语</h3>在本教程中，我们主要了解了什么是 ELK，然后通过实际操作和大家一起搭建了一个 ELK 日志分析平台，并且接入了 Logback 和 Nginx 两种日志。<br>
<br>原文链接：<a href="https://developer.ibm.com/zh/articles/build-elk-and-use-it-for-springboot-and-nginx/" rel="nofollow" target="_blank">https://developer.ibm.com/zh/a ... ginx/</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            