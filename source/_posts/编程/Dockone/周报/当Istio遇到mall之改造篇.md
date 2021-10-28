
---
title: '当Istio遇到mall之改造篇'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211026/d65209c495781c7684f701051222a88b.jpg'
author: Dockone
comments: false
date: 2021-10-28 02:21:58
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211026/d65209c495781c7684f701051222a88b.jpg'
---

<div>   
<br>随着微服务的大势不断前进，企业业务逐渐复杂，开发者不得不将原本的一个单体架构，演变成十几个甚至几十上百个微服务来对业务进行拆解。服务增加后，开发者发现多个服务相互通信带来的服务发现问题，网络访问的容错保护，访问安全等问题开始变得复杂起来，就连最简单的查看调用栈实现故障的定位，都变得十分困难。<br>
<br>面对日益凸显的问题，开发者需要一整套针对性的服务治理方案，这套方案能帮助开发者解决由服务数量的增多带来的网络层面的各种麻烦。<br>
<br>微服务SDK曾经是一个常用的解决方案。将微服务化后通用的能力封装在一个开发框架中，开发者使用这个框架开发写自己的业务代码，生成的微服务自然就内置了这些能力。在很长的一段时间内，这种形态是微服务治理的标配，最为典型的例子就是 Spring Cloud，很多开发者甚至以为Spring Cloud就代表着微服务。<br>
<br>随着Kubernetes的流行，云原生的概念又一次推动技术变革。以Service Mesh理念为基础，出现了以Istio为代表的云原生服务治理中间件，Istio为部署在Kubernetes的应用增加了完备的服务治理功能，包括流量策略、可观察性和安全通信。<br>
<br>Istio的出现使得Kubernetes上的微服务可以在一个独立的代理进程中提供服务治理的能力。区别于曾经以Spring Cloud为代表的SDK，Istio作为一种基础设施完全和开发解耦，将服务治理的能力完全从代码中抽离，在有效降低开发难度的同时让开发者专注于自身的业务。<br>
<br><strong>对比</strong><br>
<br>Spring Cloud是一个开发框架，它的出发点是以开发人员的角度去解决微服务的问题。<br>
<br>Istio是Kubernetes上的一个基础设施，它的出发点是以运维平台的角度出发去解决微服务的网络问题。<br>
<br>通过对比我们可以发现，Spring Cloud与Istio在理念上并不存在完全的冲突，在去掉部分功能冲突的部分后可以形成优势互补，开发者既可以借助Spring Cloud在开发上的能力，又可以将运维能力从代码中抽离。<br>
<br><strong>Spring Cloud向Service Mesh的迁移方案</strong><br>
<br>那如何做到在改动最小的情况下进行有效的迁移呢？让我们以mall-swarm项目为例。<br>
<br>mall-swarm项目是mall项目的微服务化版本，是一套比较典型的电商系统，包括前台商城系统及后台管理系统，相比单体形式使用Spring Boot的mall项目，mall-swarm使用了部分SpringCloud组件做微服务化的改造，采用Docker容器化部署，github star 47.7k，是典型的Spring Cloud微服务模板。<br>
<br>改造开始<br>
<br>开始前我们需要准备一个Kubernetes的集群，让我们拉取mall-swarm的代码：<a href="https://github.com/macrozheng/mall-swarm" rel="nofollow" target="_blank">https://github.com/macrozheng/mall-swarm</a><br>
<br>去掉服务注册中心<br>
<br>Spring Cloud项目向Service Mesh的迁移改造第一步其实非常简单，就是去掉服务注册中心。<br>
<br>当然不是说服务注册中心完全无法在Kubernetes上工作，事实上很多服务注册中心都实现了兼容Kubernetes的版本。但是我们任然不推荐使用服务注册中心，理由如下:<br>
<br>1.大多服务注册中心的实现原理是读取注册服务的IP地址进行配置，所有微服务调度都需要先去服务注册中心获取目的服务的真实IP进行访问。这就意味着服务和虚拟机是需要一个稳定的关联关系，然而在Kubernetes集群中，Pod与Node之间是非常松散的，Pod在不同Node间切换经常发生，这会导致服务注册和注销会频繁发生<br>
<br>2.Kubernetes本身已经提供了强大的服务发现机制，Istio是借助在Kubernetes本身提供的服务发现基础上做的流量劫持，服务读取本地IP做服务注册是无法享受到流量劫持的，也就是无法利用istio的能力<br>
<br>将mall-swarm上所有组件的服务注册中心的依赖去掉，这样调度就不会默认走到服务注册中心去。<br>
<pre class="prettyprint"><!--        <dependency>--><br>
<!--            <groupId>com.alibaba.cloud</groupId>--><br>
<!--            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>--><br>
<!--        </dependency>--><br>
<!--        <dependency>--><br>
<!--            <groupId>com.alibaba.cloud</groupId>--><br>
<!--            <artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>--><br>
<!--        </dependency>--><br>
</pre><br>
<br>接着将所有服务间调度的 FeignClient 配置到service上，service名称就用项目名即可，为了方便以后改动，我们可以配置到环境变量中，例如mall-admin这个服务需要调度到mall-auth服务可以这么写：<br>
<pre class="prettyprint">@FeignClient(name = "mall-auth", url = "$&#123;host.mall-auth&#125;") // 直接配置到环境变量上，容易以后改动<br>
public interface AuthService &#123;<br>
<br>
@PostMapping(value = "/oauth/token")<br>
CommonResult getAccessToken(@RequestParam Map<String, String> parameters);<br>
<br>
&#125;<br>
</pre><br>
<br>只需要在application.yml中给一个默认值即可。<br>
<br><pre class="prettyprint">host:<br>
mall-auth: http://mall-auth:8401<br>
</pre><br>
配置网关，让走网关的流量可以被路由到正确的位置。<br>
<pre class="prettyprint">server:<br>
port: 8201<br>
spring:<br>
cloud:<br>
gateway:<br>
  discovery:<br>
    locator:<br>
      enabled: true<br>
      lower-case-service-id: true #使用小写service-id<br>
  routes: #配置路由路径 这里全部更改为service名称<br>
    - id: mall-auth<br>
      uri: http://mall-auth:8401<br>
      predicates:<br>
        - Path=/mall-auth/**<br>
      filters:<br>
        - StripPrefix=1<br>
    - id: mall-admin<br>
      uri: http://mall-admin:8080<br>
      predicates:<br>
        - Path=/mall-admin/**<br>
      filters:<br>
        - StripPrefix=1<br>
    - id: mall-portal<br>
      uri: http://mall-portal:8085<br>
      predicates:<br>
        - Path=/mall-portal/**<br>
      filters:<br>
        - StripPrefix=1<br>
    - id: mall-search<br>
      uri: http://mall-search:8081<br>
      predicates:<br>
        - Path=/mall-search/**<br>
      filters:<br>
        - StripPrefix=1<br>
    - id: mall-demo<br>
      uri: http://mall-demo<br>
      predicates:<br>
        - Path=/mall-demo/**<br>
      filters:<br>
        - StripPrefix=1<br>
    - id: mall-admin-web<br>
      uri: http://mall-admin-web:8080<br>
      predicates:<br>
        - Path=/mall-admin-web/**<br>
      filters:<br>
        - StripPrefix=1<br>
security:<br>
oauth2:<br>
  resourceserver:<br>
    jwt:<br>
      jwk-set-uri: 'http://localhost:8201/mall-auth/rsa/publicKey' #配置RSA的公钥访问地址<br>
redis:<br>
database: 0<br>
port: 6379<br>
host: localhost<br>
password:<br>
secure:<br>
ignore:<br>
urls: #配置白名单路径<br>
  - "/doc.html"<br>
  - "/swagger-resources/**"<br>
  - "/swagger/**"<br>
  - "/**/v2/api-docs"<br>
  - "/**/*.js"<br>
  - "/**/*.css"<br>
  - "/**/*.png"<br>
  - "/**/*.ico"<br>
  - "/webjars/springfox-swagger-ui/**"<br>
  - "/actuator/**"<br>
  - "/mall-auth/oauth/token"<br>
  - "/mall-auth/rsa/publicKey"<br>
  - "/mall-search/**"<br>
  - "/mall-portal/sso/login"<br>
  - "/mall-portal/sso/register"<br>
  - "/mall-portal/sso/getAuthCode"<br>
  - "/mall-portal/home/**"<br>
  - "/mall-portal/product/**"<br>
  - "/mall-portal/brand/**"<br>
  - "/mall-admin/admin/login"<br>
  - "/mall-admin/admin/register"<br>
  - "/mall-admin/minio/upload"<br>
  - "/mall-admin-web/**"<br>
management: #开启SpringBoot Admin的监控<br>
endpoints:<br>
web:<br>
  exposure:<br>
    include: '*'<br>
endpoint:<br>
health:<br>
  show-details: always<br>
</pre><br>
<br>这样，我们服务的所有改造工作就完成了，只需要将代码重新编译打成docker的image即可交付，接下来就是运维的工作。<br>
<br>添加label<br>
<br>在mall-swarm的document/k8s文件夹下面提供了部署k8s所需的yaml，我们需要对这些yaml添加必要的label，才能让istio发现它们。<br>
<br>在控制器和template中添加 app,version 2个label，例如mall-admin这个服务。<br>
<pre class="prettyprint">apiVersion: apps/v1<br>
kind: Deployment<br>
metadata:<br>
name: mall-admin<br>
namespace: mall<br>
labels:<br>
app: mall-admin # 添加 app<br>
version: v1 # 添加 version<br>
spec:<br>
replicas: 1<br>
selector:<br>
matchLabels:<br>
  app: mall-admin<br>
template:<br>
metadata:<br>
  labels:<br>
    app: mall-admin # 添加 app<br>
    version: v1 # 添加 version<br>
spec:<br>
  restartPolicy: Always<br>
  containers:<br>
    - name: mall-admin<br>
      # 指定Docker Hub中的镜像地址<br>
      image: harbor.cloud2go.cn/macrodocker/mall-admin:1.0-SNAPSHOT<br>
      imagePullPolicy: Always<br>
      ports:<br>
        - containerPort: 8080<br>
      env:<br>
        # 指定环境<br>
        - name: spring.profiles.active<br>
          value: prod<br>
        # 指定时区<br>
        - name: TZ<br>
          value: Asia/Shanghai<br>
        - name: spring_datasource_url<br>
          value: jdbc:mysql://mall-mysql:3306/mall?useUnicode=true&characterEncoding=utf-8&serverTimezone=Asia/Shanghai<br>
        - name: spring_elasticsearch_rest_uris<br>
          value: elasticsearch:9200<br>
        - name: spring_redis_host<br>
          value: redis<br>
        - name: spring_rabbitmq_host<br>
          value: rabbitmq<br>
        - name: spring_rabbitmq_username<br>
          value: guest<br>
        - name: spring_rabbitmq_password<br>
          value: guest<br>
</pre><br>
<br>在service中添加 app 这个label，例如mall-admin这个服务。<br>
<br><pre class="prettyprint">apiVersion: v1<br>
kind: Service<br>
metadata:<br>
name: mall-admin<br>
namespace: mall<br>
labels:<br>
app: mall-admin # 添加 app<br>
spec:<br>
type: ClusterIP<br>
selector:<br>
app: mall-admin<br>
ports:<br>
- name: http<br>
  protocol: TCP<br>
  port: 8080<br>
  targetPort: 8080<br>
</pre><br>
其他服务类似，改造完成之后我们就可以部署到Kubernetes环境中了。<br>
<br>改造完的仓库可见：<a href="https://github.com/solarmesh-cn/mall-swarm-istio" rel="nofollow" target="_blank">https://github.com/solarmesh-cn/mall-swarm-istio</a><br>
<br>验证<br>
<br>我们将mall-swarm项目部署进集群之后，接下来就需要安装istio了<br>
<br>istio选择1.6版本，并使用solarmesh进行安装。solarmesh是一款基于istio的云原生流量监管平台，提供应用网络观测能力，方便快捷的策略配置，安全可靠的istio使用体验。使用solarmesh能快速安装istio，并且流量视图功能将会提供直观的流量拓扑图。<br>
<br>接入sidecar<br>
<br>solarmesh提供了namespace级别的自动注入能力，只需要在solarmesh的页面上开启自动注入就可以了，之前我们将mall-swarm项目的所有组件都部署在mall这个namespace中。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211026/d65209c495781c7684f701051222a88b.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211026/d65209c495781c7684f701051222a88b.jpg" class="img-polaroid" title="微信图片_20211026155422.jpg" alt="微信图片_20211026155422.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>流量监控<br>
<br>直接访问mall-swarm项目的前端页面，比如我们希望查看订单列表。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211026/a3dd39298dbd00b8d4b23ef61ad57320.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211026/a3dd39298dbd00b8d4b23ef61ad57320.png" class="img-polaroid" title="微信图片_20211026155437.png" alt="微信图片_20211026155437.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>访问solarmesh的流量视图页面，可以看到，流量视图已经将mall-swarm项目的服务调度清晰的展现出来了。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211026/9288372c0bc0c39c13b9f7d9dbfb905e.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211026/9288372c0bc0c39c13b9f7d9dbfb905e.jpg" class="img-polaroid" title="微信图片_20211026155448.jpg" alt="微信图片_20211026155448.jpg" referrerpolicy="no-referrer"></a>
</div>

                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            