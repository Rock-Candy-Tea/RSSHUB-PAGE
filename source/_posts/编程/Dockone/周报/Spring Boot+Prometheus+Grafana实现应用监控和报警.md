
---
title: 'Spring Boot+Prometheus+Grafana实现应用监控和报警'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/e9cac297316cdfc9373371a2dc884f81.png'
author: Dockone
comments: false
date: 2021-04-26 08:09:09
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/e9cac297316cdfc9373371a2dc884f81.png'
---

<div>   
<br>【编者的话】Spring Boot是由Pivotal团队提供的全新框架，其设计目的是用来简化新Spring应用的初始搭建以及开发过程。该框架使用了特定的方式来进行配置，从而使开发人员不再需要定义样板化的配置。Prometheus是一个开源的服务监控系统和时间序列数据库。 Grafana是一款用Go语言开发的开源数据可视化工具，可以做数据监控和数据统计，带有告警功能。<br>
<h3>背景</h3>Spring Boot的应用监控方案比较多，Spring Boot+Prometheus+Grafana是目前比较常用的方案之一。它们三者之间的关系大概如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/e9cac297316cdfc9373371a2dc884f81.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/e9cac297316cdfc9373371a2dc884f81.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>开发Spring Boot应用</h3>首先，创建一个Spring Boot项目，pom文件如下：<br>
<pre class="prettyprint"><dependency><br>
        <groupId>org.springframework.boot</groupId><br>
        <artifactId>spring-boot-starter-actuator</artifactId><br>
    </dependency><br>
    <dependency><br>
        <groupId>org.springframework.boot</groupId><br>
        <artifactId>spring-boot-starter-web</artifactId><br>
    </dependency><br>
<br>
    <dependency><br>
        <groupId>org.projectlombok</groupId><br>
        <artifactId>lombok</artifactId><br>
        <optional>true</optional><br>
    </dependency><br>
<br>
    <!-- https://mvnrepository.com/artifact/io.prometheus/simpleclient_spring_boot --><br>
    <dependency><br>
        <groupId>io.prometheus</groupId><br>
        <artifactId>simpleclient_spring_boot</artifactId><br>
        <version>0.8.1</version><br>
    </dependency><br>
<br>
    <dependency><br>
        <groupId>org.springframework.boot</groupId><br>
        <artifactId>spring-boot-starter-security</artifactId><br>
    </dependency> <br>
</pre><br>
<strong>注意：</strong> 这里的Spring Boot版本是1.5.7.RELEASE，之所以不用最新的2.X是因为最新的simpleclient_spring_boot只支持1.5.X，不确定2.X版本的能否支持。<br>
<br>MonitorDemoApplication启动类增加注解。<br>
<pre class="prettyprint">package cn.sp; <br>
<br>
import io.prometheus.client.spring.boot.EnablePrometheusEndpoint; <br>
import io.prometheus.client.spring.boot.EnableSpringBootMetricsCollector; <br>
import org.springframework.boot.SpringApplication; <br>
import org.springframework.boot.autoconfigure.SpringBootApplication; <br>
@EnablePrometheusEndpoint <br>
@EnableSpringBootMetricsCollector <br>
@SpringBootApplication <br>
public class MonitorDemoApplication &#123; <br>
<br>
public static void main(String[] args) &#123; <br>
    SpringApplication.run(MonitorDemoApplication.class, args); <br>
&#125; <br>
<br>
&#125;  <br>
</pre><br>
配置文件application.yml：<br>
<pre class="prettyprint">server: <br>
port: 8848 <br>
spring: <br>
application: <br>
name: monitor-demo <br>
<br>
security: <br>
user: <br>
name: admin <br>
password: 1234 <br>
basic: <br>
enabled: true <br>
# 安全路径列表，逗号分隔，此处只针对/admin路径进行认证 <br>
path: /admin <br>
<br>
# actuator暴露接口的前缀 <br>
management: <br>
context-path: /admin <br>
# actuator暴露接口使用的端口，为了和api接口使用的端口进行分离 <br>
port: 8888 <br>
security: <br>
enabled: true <br>
roles: SUPERUSER <br>
</pre><br>
测试代码TestController：<br>
<pre class="prettyprint">@RequestMapping("/heap/test")<br>
@RestController<br>
public class TestController &#123;<br>
<br>
public static final Map<String, Object> map = new ConcurrentHashMap<>();<br>
<br>
@RequestMapping("")<br>
public String testHeapUsed() &#123;<br>
    for (int i = 0; i < 10000000; i++) &#123;<br>
        map.put(i + "", new Object());<br>
    &#125;<br>
    return "ok";<br>
&#125;<br>
&#125; <br>
</pre><br>
这里的逻辑就是在请求这个接口后，创建大量对象保存到map中增加堆内存使用量，方便后面测试邮件报警。<br>
<br>启动项目后，可以在IDEA中看到有很多Endpoints，如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/22032fbfe9ccaa34a2ce6e4b52a91cb8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/22032fbfe9ccaa34a2ce6e4b52a91cb8.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
开始我的IDEA是不显示这个Endpoints，后来发现是我使用的idea版本太老了，还是2017.1的，而这个需要 idea 2017.2版本以上才能看到。  后来只好重新下载安装，弄了好久……<br>
<br>启动完毕，访问<a href="http://localhost:8888/admin/prometheus" rel="nofollow" target="_blank">http://localhost:8888/admin/prometheus</a>就可以看到服务暴露的那些监控指标了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/4db857b3f6f90b4474caa50e54d7ad72.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/4db857b3f6f90b4474caa50e54d7ad72.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
注意：由于开启了安全认证，所以访问这个URL的需要提示输入账号/密码，如果提示404请检查下你的请求地址是否正确，如果不设置management.context-path则默认地址是<a href="http://ip/:port/prometheus" rel="nofollow" target="_blank">http://ip/:port/prometheus</a><br>
<h3>安装Prometheus</h3>下载地址<a href="https://prometheus.io/download/">点击这里</a>，本文下载的是Windows版本：prometheus-2.17.2.windows-amd64.tar.gz。<br>
<br>解压后修改prometheus.yml文件，配置数据采集的目标信息。<br>
<pre class="prettyprint">scrape_configs: <br>
# The job name is added as a label `job=<job_name>` to any timeseries scraped from this config. <br>
# - job_name: 'prometheus' <br>
<br>
# metrics_path defaults to '/metrics' <br>
# scheme defaults to 'http'. <br>
<br>
# static_configs: <br>
# - targets: ['localhost:9090'] <br>
- job_name: 'monitor-demo' <br>
scrape_interval: 5s # 刮取的时间间隔 <br>
scrape_timeout: 5s  <br>
metrics_path: /admin/prometheus <br>
scheme: http  <br>
basic_auth: #认证信息 <br>
  username: admin <br>
  password: 1234 <br>
static_configs: <br>
  - targets: <br>
    - 127.0.0.1:8888  #此处填写 Spring Boot 应用的 IP + 端口号<br>
</pre><br>
更多配置信息请查看官方文档。<br>
<br>现在可以启动Prometheus了，命令行输入：prometheus.exe --config.file=prometheus.yml，访问<a href="http://localhost:9090/targets" rel="nofollow" target="_blank">http://localhost:9090/targets</a>，查看Spring Boot采集状态是否正常。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/2399253851d529c5af507f333363b42c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/2399253851d529c5af507f333363b42c.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>安装Grafana</h3>下载地址<a href="https://grafana.com/grafana/download">点击这里</a>，本文用到的是Windows版本：grafana-6.3.3.windows-amd64.zip。<br>
<br>解压后运行bin目录下的grafana-server.exe启动，游览器访问<a href="http://localhost:3000/" rel="nofollow" target="_blank">http://localhost:3000</a>即可看到登录页面，默认账号密码是admin/admin。<br>
<br>现在开始创建自己的可视化监控面板。<br><br>
<h4>设置数据源</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/3b1298aa43fe855f2f97f451f4495f30.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/3b1298aa43fe855f2f97f451f4495f30.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>创建一个Dashboard</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/ca04bb626d06563bb84308ef883a040c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/ca04bb626d06563bb84308ef883a040c.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/351208b6a34a3a141b5b59b2f81236cb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/351208b6a34a3a141b5b59b2f81236cb.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>填写采集的指标点</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/11fbe229e5f26f9d4fe80432b5a1744b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/11fbe229e5f26f9d4fe80432b5a1744b.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>注意</strong>：这里的指标点不能随便填，必须是已有的可以在Prometheus看到。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/bc53bb24a140c8f69f5ebe679344a74a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/bc53bb24a140c8f69f5ebe679344a74a.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>选择图表样式</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/580e80ca0a17b1ad77ab2709bc07f8db.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/580e80ca0a17b1ad77ab2709bc07f8db.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>填写标题描述</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/10d8733ea74f3da859be813fd3cd1501.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/10d8733ea74f3da859be813fd3cd1501.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
最后点击右上角的保存，输入Dashboad的名称即可。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/55bf0c2f6016ad6d330114661ad32c52.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/55bf0c2f6016ad6d330114661ad32c52.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Tips：这里的图表布局是可以用鼠标拖动的。<br>
<h3>添加邮件报警</h3>在实际项目中当监控的某的个指标超过阈值（比如CPU使用率过高），希望监控系统自动通过短信、钉钉和邮件等方式报警及时通知运维人员，Grafana就支持该功能。<br>
<h4>第一步：点击[Alerting]——>[Notification channels]添加通知通道</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/bed15a632f8d90fe87cfbb2113b0abcc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/bed15a632f8d90fe87cfbb2113b0abcc.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>创建通道</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/e910514b362ffe1c5711b44d17206c97.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/e910514b362ffe1c5711b44d17206c97.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>编辑</em><br>
<br>这里的Type有很多选项，包括Webhook、钉钉等，这里以邮件为例。<br>
<h4>第二步：邮箱配置</h4>Grafana默认使用conf目录下defaults.ini作为配置文件运行，根据官方的建议我们不要更改defaults.ini而是在同级目录下新建一个配置文件custom.ini。  <br>
<br>以腾讯企业邮箱为例，配置如下：<br>
<pre class="prettyprint">#################################### SMTP / Emailing #####################<br>
[smtp]<br>
enabled = true<br>
host = smtp.exmail.qq.com:465<br>
user = xxxx@ininin.com<br>
# If the password contains # or ; you have to wrap it with triple quotes. Ex """#password;"""<br>
password = XXX<br>
cert_file =<br>
key_file =<br>
skip_verify = true<br>
from_address = xxxx@ininin.com<br>
from_name = Grafana<br>
ehlo_identity = ininin.com<br>
</pre><br>
然后需要重启Grafana，命令：grafana-server.exe -config=E:\file\grafana-6.3.3\conf\custom.ini<br>
<h4>第三步：为指标添加alert</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/36cf49e88d8f777ff8092c3a1a13053c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/36cf49e88d8f777ff8092c3a1a13053c.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>配置预警规则</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/2a59856ed477c70433a77d6ad95bc285.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/2a59856ed477c70433a77d6ad95bc285.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>配置通知方式和信息</em><br>
<br>Evaluate every：表示检测评率，这里为了测试效果，改为1秒<br>
<br>For：如果警报规则配置了For，并且查询违反了配置的阈值，那么它将首先从OK变为Pending。从OK到Pending Grafana不会发送任何通知。一旦警报规则的触发时间超过持续时间，它将更改为Alerting并发送警报通知。<br>
<br>Conditions：when 表示什么时间，of 表示条件，is above 表示触发值，同时，设置了is above后会有一条红线。<br>
<br>If no data or all values are null：如果没有数据或所有值都为空，这里选择触发报警<br>
<br>If execution error or timeout：如果执行错误或超时，这里选择触发报警<br>
<br>注意：下一次触发，比如10秒后，它不会再次触发，防止报警风暴产生！<br>
<h4>第四步：测试</h4>请求<a href="http://localhost:8848/heap/test" rel="nofollow" target="_blank">http://localhost:8848/heap/test</a>接口后，内存升高大于设置的阈值，然后就收到报警邮件。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/bbe444ec7b90fe808a78309eb5e19337.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/bbe444ec7b90fe808a78309eb5e19337.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这里图片没有显示出来，搞不懂为什么。<br>
<h3>总结</h3>这套监控功能还是挺强大的，就是Prometheus的表达式有点多。<br>
<br>代码地址：<a href="https://github.com/2YSP/monitor-demo" rel="nofollow" target="_blank">https://github.com/2YSP/monitor-demo</a><br>
<br>原文链接：<a href="https://www.cnblogs.com/2YSP/p/12827487.html" rel="nofollow" target="_blank">https://www.cnblogs.com/2YSP/p/12827487.html</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            