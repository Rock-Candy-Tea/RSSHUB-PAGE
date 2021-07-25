
---
title: '最简单的Spring Boot 整合ELK教程，实现日志收集'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/370163806003046e61e903f25745ab40.jpg'
author: Dockone
comments: false
date: 2021-07-25 12:09:44
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/370163806003046e61e903f25745ab40.jpg'
---

<div>   
<br><h3>前言</h3>开发任务后，提交代码的那一刻，心情是自由自在……速度是八十迈……<br>
<br>以为接下来是游戏、逛GAI或暖烘烘的被窝。<br>
<br>然而，梦想何其丰满，现实何其骨干。<br>
<br>总有测试小姐姐教你紧急刹车，回头做（改）人（bug）：你这不行啊！（吃瓜群众排排坐，笑歪了嘴）<br>
<br>我低头看了看自己的八块腹肌：行不行可不是你说了算！<br>
<br>小姐姐也不是吃素的，撸起袖子，打开她的联想十代：你行你连连报错，毒奶队友！<br>
<br>我：(⊙o⊙)……原来你说的是这个不行，我还以为……<br>
<br>小姐姐一脸疑惑：以为什么？真以为自己是大神了！<br>
<br>我清咳掉自己的尴尬，绝不认输：我认为是你传错了参数。毕竟本大师在本地调试时可没有任何问题。<br>
<br>小姐姐久经沙场，从无败绩：不！可！能！是你是你就是你！我从来不会错。<br>
<br>那一刻，我仿佛看到生理期的女朋友在面前闪现，内心是崩溃的。<br>
<br>我们俩就这样争执了很久，最后自然不出意料，缴械投降的还是我。<br>
<br>毕竟——<br>
<br>中华民族的传统美（糟）德（粕）是：好男不跟女斗！<br>
<br>于是我只能去服务器上看看日志，但是日志内容累累如高山，多多如牛毛，足足3.5个G，无奈的我只好使用一堆Linux骚命令，将文件切割成一个个小文件，好在最后终于找到了那次请求，排查后找到了原因。<br>
<br>通过这件事，我痛定思痛：如果有一个平台能实时收集我们的日志，并能以可视化的界面呈现出来，那该多好啊！这样我们就再也不用在那堆厚重的日志文件里面找数据了。<br>
<h3>秘籍展示</h3>其实，这种神奇的平台早就有了，那就是ELK，它是三大神兽Elasticsearch（搜索引擎）, Logstash（日志收集），Kibana（可视化的Web界面）的组合，我们来看下架构图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/370163806003046e61e903f25745ab40.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/370163806003046e61e903f25745ab40.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
对照架构图，我们来看下这三大神兽的工作过程：<br>
<ol><li>用户发送请求到我们的服务端</li><li>服务端将需要落日志的数据通过网络请求传送到Logstash</li><li>Logstash对数据进行过滤清洗后，再传给Elasticsearch</li><li>Elasticsearch负责对数据创建索引，进行存储</li><li>用户通过访问Kibana的Web页面，能够实时查看日志</li></ol><br>
<br>好吧，秘籍都告诉你了，现在需要带领你们去实战了。<br>
<h3>必备心法</h3>在打仗之前，我们需要士兵们必须具备以下技能，不然上了战场后，只会被虐的体无完肤。<br>
<ul><li>了解ELK三大组件</li><li>有实操过Docker</li><li>本地有Docker环境</li><li>IDEA工具</li><li>配置相对高一点的武器（电脑），不然会崩溃的</li></ul><br>
<br><h3>准备粮草：准备一个Spring Boot项目</h3>首先创建一个Spring Boot项目，项目结构如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/70086bd8f58f6aefadd398d8486a8639.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/70086bd8f58f6aefadd398d8486a8639.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
引入项目必备依赖：<br>
<pre class="prettyprint"><dependency><br>
        <groupId>org.springframework.boot</groupId><br>
        <artifactId>spring-boot-starter</artifactId><br>
    </dependency><br>
    <dependency><br>
        <groupId>com.alibaba</groupId><br>
        <artifactId>fastjson</artifactId><br>
        <version>1.2.35</version><br>
    </dependency><br>
    <dependency><br>
        <groupId>cn.hutool</groupId><br>
        <artifactId>hutool-all</artifactId><br>
        <version>5.4.0</version><br>
    </dependency><br>
</pre><br>
创建一些基础组件：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/3b4e7ec117ccb6f4fe3b74fe9805b4b5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/3b4e7ec117ccb6f4fe3b74fe9805b4b5.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
创建切面，实现低耦合记录日志。<br>
<br>下面是核心代码：<br>
<pre class="prettyprint">// 使用环绕通知<br>
@Around("controllerLog()")<br>
public Object doAround(ProceedingJoinPoint joinPoint) throws Throwable &#123;<br>
long startTime = System.currentTimeMillis();<br>
// 获取当前请求对象<br>
ServletRequestAttributes attributes =<br>
    (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();<br>
HttpServletRequest request = attributes.getRequest();<br>
// 记录请求信息<br>
ReqRspLog webLog = new ReqRspLog();<br>
Object result = joinPoint.proceed();<br>
Signature signature = joinPoint.getSignature();<br>
MethodSignature methodSignature = (MethodSignature) signature;<br>
Method method = methodSignature.getMethod();<br>
// 通过反射，获取入参和出参，封装成json，落日志<br>
long endTime = System.currentTimeMillis();<br>
String urlStr = request.getRequestURL().toString();<br>
webLog.setBasePath(StrUtil.removeSuffix(urlStr, URLUtil.url(urlStr).getPath()));<br>
webLog.setIp(request.getRemoteUser());<br>
webLog.setMethod(request.getMethod());<br>
webLog.setParameter(getParameter(method, joinPoint.getArgs()));<br>
webLog.setResult(result);<br>
webLog.setSpendTime((int) (endTime - startTime));<br>
webLog.setStartTime(startTime);<br>
webLog.setUri(request.getRequestURI());<br>
webLog.setUrl(request.getRequestURL().toString());<br>
logger.info("&#123;&#125;", JSONUtil.parse(webLog));<br>
return result;<br>
&#125; <br>
</pre><br>
创建测试接口：<br>
<pre class="prettyprint">@RestController<br>
@RequestMapping("/api")<br>
public class ApiController &#123;<br>
@GetMapping<br>
public R<String> addLog(@RequestParam(value = "param1",required = false) String param1)&#123;<br>
    return R.success("你好，这段话将被日志记录");<br>
&#125;<br>
&#125; <br>
</pre><br>
我们现在请求一下接口，会发现在控制台打印出这样一段日志：<br>
<pre class="prettyprint">&#123;"method":"GET","uri":"/api","url":"http://localhost:8080/api","result":&#123;"code":200,"data":"你好，这段话将被日志记录","message":"操作成功"&#125;,"basePath":"http://localhost:8080","parameter":&#123;"param1":"测试ELK"&#125;,"startTime":1611529379353,"spendTime":9&#125; <br>
</pre><br>
使用切面，实现日志记录并打印到控制台上已经完成了，现在我们按照架构图，需要通过Logstash把日志发送到es里面，接下来整合Logstash实现传送日志的功能。<br>
<h3>招兵买马：整合Logstash</h3>添加Logstash依赖：<br>
<pre class="prettyprint"><!--集成Logstash--><br>
    <dependency><br>
        <groupId>net.logstash.logback</groupId><br>
        <artifactId>logstash-logback-encoder</artifactId><br>
        <version>5.3</version><br>
    </dependency><br>
    <dependency><br>
        <groupId>org.projectlombok</groupId><br>
        <artifactId>lombok</artifactId><br>
        <optional>true</optional><br>
    </dependency><br>
</pre><br>
编辑配置文件logback-spring.xml：<br>
<pre class="prettyprint"><?xml version="1.0" encoding="UTF-8"?><br>
<!DOCTYPE configuration><br>
<configuration><br>
<include resource="org/springframework/boot/logging/logback/defaults.xml"/><br>
<include resource="org/springframework/boot/logging/logback/console-appender.xml"/><br>
<!--应用名称--><br>
<property name="APP_NAME" value="mall-admin"/><br>
<!--日志文件保存路径--><br>
<property name="LOG_FILE_PATH" value="$&#123;LOG_FILE:-$&#123;LOG_PATH:-$&#123;LOG_TEMP:-$&#123;java.io.tmpdir:-/tmp&#125; &#125; &#125;/logs&#125;"/><br>
<contextName>$&#123;APP_NAME&#125;</contextName><br>
<!--每天记录日志到文件appender--><br>
<appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender"><br>
    <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy"><br>
        <fileNamePattern>$&#123;LOG_FILE_PATH&#125;/$&#123;APP_NAME&#125;-%d&#123;yyyy-MM-dd&#125;.log</fileNamePattern><br>
        <maxHistory>30</maxHistory><br>
    </rollingPolicy><br>
    <encoder><br>
        <pattern>$&#123;FILE_LOG_PATTERN&#125;</pattern><br>
    </encoder><br>
</appender><br>
<!--输出到Logstash的appender--><br>
<appender name="LOGSTASH" class="net.logstash.logback.appender.LogstashTcpSocketAppender"><br>
    <!--可以访问的Logstash日志收集端口--><br>
    <destination>127.0.0.1:4560</destination><br>
    <encoder charset="UTF-8" class="net.logstash.logback.encoder.LogstashEncoder"/><br>
</appender><br>
<root level="info"><br>
    <appender-ref ref="CONSOLE"/><br>
    <appender-ref ref="FILE"/><br>
    <appender-ref ref="LOGSTASH"/><br>
</root><br>
</configuration><br>
</pre><br>
编辑完之后，项目结构是这样的：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/4ef4ff182a2acf818a0ff1a8d55a616c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/4ef4ff182a2acf818a0ff1a8d55a616c.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
虽然在项目中已经集成了Logstash功能，但是Logstash还不知道把日志往哪里发，因为我们还没有城池。<br>
<br>既然没有，那就建造吧！<br>
<h3>搭建城池：搭建ELK环境</h3>ELK这里我使用dokcer-compose搭建，一个字：快！<br>
<br>首先我们约定一个根目录：/user/aimashi/docker<br>
<br>按要求执行如下命令：<br>
<pre class="prettyprint">mkdir -p /Users/yangle/docker<br>
cd /Users/yangle/docker<br>
mkdir elk_stanrd<br>
cd elk_stanrd<br>
mkdir logstash<br>
cd logstash<br>
vim logstash.conf<br>
</pre><br>
将以下文件内容复制到logstash.conf。<br>
<pre class="prettyprint">input &#123;<br>
tcp &#123;<br>
mode => "server"<br>
host => "0.0.0.0"<br>
port => 4560<br>
codec => json_lines<br>
&#125;<br>
&#125;<br>
<br>
output &#123;<br>
elasticsearch &#123;<br>
hosts => "es:9200"<br>
index => "logstash-service-%&#123;+YYYY.MM.dd&#125;"<br>
&#125;<br>
&#125; <br>
</pre><br>
继续执行如下命令：<br>
<pre class="prettyprint">cd ../<br>
vim docker-compose.yml<br>
</pre><br>
同样将以下内容复制到配置文件中。<br>
<pre class="prettyprint">version: '3'<br>
services:<br>
elasticsearch:<br>
image: elasticsearch:6.4.0<br>
container_name: elasticsearch<br>
environment:<br>
  - "cluster.name=elasticsearch" #设置集群名称为Elasticsearch<br>
  - "discovery.type=single-node" #以单一节点模式启动<br>
  - "ES_JAVA_OPTS=-Xms512m -Xmx512m" #设置使用JVM内存大小<br>
volumes:<br>
  - /Users/yangle/docker/elk_stanrd/elasticsearch/plugins:/usr/share/elasticsearch/plugins #插件文件挂载<br>
  - /Users/yangle/docker/elk_stanrd/elasticsearch/data:/usr/share/elasticsearch/data #数据文件挂载<br>
ports:<br>
  - 9200:9200<br>
  - 9300:9300<br>
kibana:<br>
image: kibana:6.4.0<br>
container_name: kibana<br>
links:<br>
  - elasticsearch:es #可以用es这个域名访问Elasticsearch服务<br>
depends_on:<br>
  - elasticsearch #Kibana在Elasticsearch启动之后再启动<br>
environment:<br>
  - "elasticsearch.hosts=http://es:9200" #设置访问Elasticsearch的地址<br>
ports:<br>
  - 5601:5601<br>
logstash:<br>
image: logstash:6.4.0<br>
container_name: logstash<br>
volumes:<br>
  - ~/Users/yangle/docker/elk_stanrd/logstash/logstash.conf:/usr/share/logstash/pipeline/logstash.conf #挂载Logstash的配置文件<br>
depends_on:<br>
  - elasticsearch #Kibana在Elasticsearch启动之后再启动<br>
links:<br>
  - elasticsearch:es #可以用es这个域名访问Elasticsearch服务<br>
ports:<br>
  - 4560:4560<br>
</pre><br>
到目前为止，搭建ELK环境的准备工作已经完成。<br>
<br>现在需要启动ELK，在/Users/yangle/docker/elk_stanrd目录下执行如下命令：<br>
<pre class="prettyprint">docker-compose up -d<br>
</pre><br>
执行之后出现如下提示，则代表初创建成功。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/60cfd51b1326787ec424ec62ce07301b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/60cfd51b1326787ec424ec62ce07301b.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
接下来，我们执行docker ps 来查看容器是否启动。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/5fba2de60bed6eed89badf8086519d7f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/5fba2de60bed6eed89badf8086519d7f.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如果和图中一样，代表容器正常启动，但是还需等待一分钟左右，才能访问可视化平台。<br>
<br>访问地址：<a href="http://localhost:5601/" rel="nofollow" target="_blank">http://localhost:5601/</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/a10aa58a801ea90ae5d639513b345b0d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/a10aa58a801ea90ae5d639513b345b0d.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如果出现这个页面，则代表ELK已经搭建完成，现在，我们需要往里面塞点数据。<br>
<h3>发起进攻：发送请求</h3>ELK环境搭建完成之后，需要产生一点数据。该怎么做呢？<br>
<br>只要调用：<a href="http://localhost:8080/api?param1=" rel="nofollow" target="_blank">http://localhost:8080/api?param1=</a>测试ELK接口，多调用几次，就会产生一些测试数据。<br>
<br>除此之外，还需要做一些配置才能让es去收集这些日志，用户才能看到：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/ff70b4f7ae5f6582c055ca24028b7689.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/ff70b4f7ae5f6582c055ca24028b7689.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/c187d1086b3a2579507c54ac3f6a8167.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/c187d1086b3a2579507c54ac3f6a8167.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
选择字段，创建索引：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/5c05a8b872350851199c038b598e74f2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/5c05a8b872350851199c038b598e74f2.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
成功创建索引之后的界面：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/74193a3367a252d8e5fe30ecb498e19f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/74193a3367a252d8e5fe30ecb498e19f.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/56549def23ab65264e346f9a1d4bea9d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/56549def23ab65264e346f9a1d4bea9d.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
选择logstash-servicez之后，界面是这样的：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/d5bc7583b2b25e8ef7cc06d5b6ae5a9d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/d5bc7583b2b25e8ef7cc06d5b6ae5a9d.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到系统中的日志已经被收集上来了，试下搜索“你好”。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/cf519dee55d65575c3d2aacfe24ef009.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/cf519dee55d65575c3d2aacfe24ef009.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
所有包含“你好”的日志都被筛选出来，当然这里还可以有很多检索条件，例如右上角有一个时间过滤检索，我就不一一演示了，大家有兴趣的话可以自己研究下。<br>
<br>仓库：<a href="https://gitee.com/yangleliu/learning.git" rel="nofollow" target="_blank">https://gitee.com/yangleliu/learning.git</a><br>
<h3>战后总结</h3>每个新技术的出现，都是为了解决某一类问题。<br>
<br>就像ELK的出现，就是为了减少日渐脱发的代码攻城狮们从海量日志中找数据的时间，节省出更多的精力放在业务处理上面。<br>
<br>有了ELK，我们只需要在输入框中，轻松输入关键字，敲下回车，需要的数据就会呈现在我们面前。<br>
<br>测试小姐姐等待的时间短了，心情好了，矛盾自然也就少了。<br>
<br>如此想来，如果能有一个平台，将女友的十万个情绪爆发的原因实时展现出来，那世界将是多么美好的明天！<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/4lpM7DcpMq0e4lvhhL2yx" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/4lpM7DcpMq0e4lvhhL2yx</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            