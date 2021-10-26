
---
title: 'Apache ShenYu(incubating) 发布 2.4.1'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2310'
author: 开源中国
comments: false
date: Tue, 26 Oct 2021 16:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2310'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="margin-left:0; margin-right:0"><span style="color:inherit">Apache ShenYu(Incubating) 2.4.1 正式发布</span></h3> 
<h4 style="margin-left:0; margin-right:0"><span style="color:inherit">新功能</span></h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span style="color:inherit">Admin管理后台开始支持PostgreSQL。</span></li> 
 <li><span style="color:inherit">支持插件的动态加载。</span></li> 
 <li><span style="color:inherit">新增Websocket插件。</span></li> 
 <li><span style="color:inherit">新增请求参数加解密插件。</span></li> 
 <li><span style="color:inherit">新增返回参数加解密插件。</span></li> 
 <li><span style="color:inherit">支持 dubbo的灰度发布。</span></li> 
 <li><span style="color:inherit">支持 springCloud灰度发布。</span></li> 
 <li><span style="color:inherit">支持自定义crossFilter配置。</span></li> 
 <li><span style="color:inherit">Sign插件支持自定义动态签名算法。</span></li> 
 <li><span style="color:inherit">支持 JDK8~JDK15</span></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0"><span style="color:inherit">优化项</span></h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span style="color:inherit">优化 admin管理后台 SQL语句初始化。</span></li> 
 <li><span style="color:inherit">优化 admin管理后台 分页查询逻辑。</span></li> 
 <li><span style="color:inherit">优化dubbo异步回调的问题。</span></li> 
 <li><span style="color:inherit">优化客户端注册逻辑。</span></li> 
 <li><span style="color:inherit">优化全局异常处理。</span></li> 
 <li><span style="color:inherit">优化Dubbo参数转换出来。</span></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0"><span style="color:inherit">删除项</span></h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span style="color:inherit">删除lombok依赖</span></li> 
 <li><span style="color:inherit">删除mapstruct依赖</span></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0"><span style="color:inherit">Bug fix</span></h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span style="color:inherit">解决 JwtPlugin， 关于JsonSyntaxException的问题。</span></li> 
 <li><span style="color:inherit">解决 resilience4jPlugin 配置初始化丢失的问题。</span></li> 
 <li><span style="color:inherit">解决 motanPlugin， 配置初始化丢失的问题。</span></li> 
 <li><span style="color:inherit">解决健康检查死锁的问题。</span></li> 
 <li><span style="color:inherit">解决客户端注册失败，重试的问题。</span></li> 
 <li><span style="color:inherit">解决Nacos使用默认分组的问题。</span></li> 
 <li><span style="color:inherit">解决docker镜像启动失败的问题。</span></li> 
 <li><span style="color:inherit">解决Gson转换null对象，空指针问题。</span></li> 
 <li><span style="color:inherit">解决 ContextPath错误配置的问题。</span></li> 
 <li><span style="color:inherit">解决客户端注册失败的问题。</span></li> 
 <li><span style="color:inherit">解决元数据写入失败的问题。</span></li> 
 <li><span style="color:inherit">解决 responsePlugin排序的问题。</span></li> 
 <li><span style="color:inherit">解决monitor插件未初始化Metrics的问题。</span></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0"><span style="color:inherit">配置项的更改</span></h4> 
<p style="color:inherit; margin-left:0; margin-right:0">具体详解请查看 ： https://shenyu.apache.org/zh/docs/next/user-guide/property-config/gateway-property-config</p> 
<pre style="margin-left:0; margin-right:0"><code class="language-yaml">shenyu:
#  httpclient:
#    strategy: webClient
#    connectTimeout: 45000
#    readTimeout: 3000
#    writeTimeout: 3000
#    wiretap: false
#    pool:
#      type: ELASTIC
#      name: proxy
#      maxConnections: 16
#      acquireTimeout: 45000
#    proxy:
#      host:
#      port:
#      username:
#      password:
#      nonProxyHostsPattern:
#    ssl:
#      useInsecureTrustManager: false
#      trustedX509Certificates:
#      handshakeTimeout:
#      closeNotifyFlushTimeout:
#      closeNotifyReadTimeout:
#      defaultConfigurationType:
  sync:
    websocket:
      urls: ws://localhost:9095/websocket
#    zookeeper:
#      url: localhost:2181
#      sessionTimeout: 5000
#      connectionTimeout: 2000
#    http:
#      url: http://localhost:9095
#    nacos:
#      url: localhost:8848
#      namespace: 1c10d748-af86-43b9-8265-75f487d20c6c
#      username:
#      password:
#      acm:
#        enabled: false
#        endpoint: acm.aliyun.com
#        namespace:
#        accessKey:
#        secretKey:
#    etcd:
#      url: http://localhost:2379
#    consul:
#      url: http://localhost:8500
#      waitTime: 1000
#      watchDelay: 1000
  cross:
    enabled: true
    allowedHeaders:
    allowedMethods: "*"
    allowedOrigin: "*"
    allowedExpose: "*"
    maxAge: "18000"
    allowCredentials: true
  switchConfig:
    local: true
  file:
    enabled: true
    maxSize : 10
  exclude:
    enabled: false
    paths:
      - /favicon.ico
  extPlugin:
    path:
    enabled: true
    threads: 1
    scheduleTime: 300
    scheduleDelay: 30
  scheduler:
    enabled: false
    type: fixed
    threads: 16
  upstreamCheck:
    enabled: false
    timeout: 3000
    healthyThreshold: 1
    unhealthyThreshold: 1
    interval: 5000
    printEnabled: true
    printInterval: 60000
</code></pre> 
<h4 style="margin-left:0; margin-right:0"><span style="color:inherit">Webscoket插件使用</span></h4> 
<p style="color:inherit; margin-left:0; margin-right:0"><code>Apache ShenYu</code> 网关通过<code>Websocket</code>插件实现了对<code>websocket</code>代理的支持。</p> 
<p><span style="color:inherit">环境准备</span></p> 
<p style="color:inherit; margin-left:0; margin-right:0">需要在基础配置<code>-></code>插件管理中，把<code>websocket</code> 插件设置为开启。</p> 
<p style="color:inherit; margin-left:0; margin-right:0">在网关的 <code>pom.xml</code> 文件中引入<code>websocket</code>插件的相关依赖：</p> 
<pre style="margin-left:0; margin-right:0"><code class="language-xml">  <span style="color:#808080"><!--if you use http proxy start this--></span>
<span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-websocket<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
</code></pre> 
<p><span style="color:inherit">请求方式</span></p> 
<p style="color:inherit; margin-left:0; margin-right:0">使用 Apache ShenYu 代理websocket的时候，只需要使用ws协议开头，后面路径为真实Websocket路径：</p> 
<pre style="margin-left:0; margin-right:0"><code>ws:<span style="color:#808080">//localhost:9195/xxx</span>
</code></pre> 
<h4 style="margin-left:0; margin-right:0"><span style="color:inherit">CryptorRequest 插件使用</span></h4> 
<p style="color:inherit; margin-left:0; margin-right:0"><code>cryptorRequest</code> 插件是通过 <code>fieldNames</code> 去匹配 <code>requestBody</code> 里面的参数进行 <code>解密</code> 处理，替换当前 <code>requestBody</code> 内容。防互联网黑产，恶意获取数据。提高数据安全性。</p> 
<p><span style="color:inherit">插件使用</span></p> 
<p style="color:inherit; margin-left:0; margin-right:0">具体使用请参考 ： https://shenyu.apache.org/zh/docs/next/plugin-center/authority-and-certification/cryptor-request-plugin/</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">在 <code>shenyu-admin</code> --> 基础配置 --> 插件管理 --> <code>cryptor_request</code> 设置为开启。</p> </li> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">在网关的 <code>pom.xml</code> 文件中添加 <code>cryptorRequest</code> 的支持。</p> </li> 
</ul> 
<pre style="margin-left:0; margin-right:0"><code class="language-xml"><span style="color:#808080"><!-- apache shenyu Cryptor Request plugin start--></span>
<span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-cryptor<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
<span style="color:#808080"><!-- apache shenyu Cryptor Request plugin end--></span>
</code></pre> 
<h4 style="margin-left:0; margin-right:0"><span style="color:inherit">CryptorResponse 插件使用</span></h4> 
<p style="color:inherit; margin-left:0; margin-right:0"><code>CryptorResponse</code> 插件是通过 <code>fieldNames</code> 去匹配 <code>responseBody</code> 里面的参数进行 <code>加密</code> 处理，替换当前 <code>fieldNames</code> 对应内容。防互联网黑产，恶意获取数据。提高数据安全性。</p> 
<p><span style="color:inherit">插件使用</span></p> 
<p style="color:inherit; margin-left:0; margin-right:0">具体使用请参考 ： https://shenyu.apache.org/zh/docs/next/plugin-center/authority-and-certification/cryptor-response-plugin</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">在 <code>shenyu-admin</code> --> 基础配置 --> 插件管理 --> <code>cryptor_response</code> 设置为开启</p> </li> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">在网关的 <code>pom.xml</code> 文件中添加 <code>cryptorResponse</code> 的支持。</p> </li> 
</ul> 
<pre style="margin-left:0; margin-right:0"><code class="language-xml"><span style="color:#808080"><!-- apache shenyu Cryptor Response plugin start--></span>
<span style="color:inherit"><<span style="color:#f82375">dependency</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">groupId</span>></span>org.apache.shenyu<span style="color:inherit"></<span style="color:#f82375">groupId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">artifactId</span>></span>shenyu-spring-boot-starter-plugin-cryptor<span style="color:inherit"></<span style="color:#f82375">artifactId</span>></span>
  <span style="color:inherit"><<span style="color:#f82375">version</span>></span>$&#123;project.version&#125;<span style="color:inherit"></<span style="color:#f82375">version</span>></span>
<span style="color:inherit"></<span style="color:#f82375">dependency</span>></span>
<span style="color:#808080"><!-- apache shenyu Cryptor Response plugin end--></span>
</code></pre> 
<h4 style="margin-left:0; margin-right:0"><span style="color:inherit">插件动态加载</span></h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">当用户自定义扩展插件时候，可以使用此功能。扩展 <code>ShenyuPlugin</code>, <code>PluginDataHandler</code>, 不用成为 <code>spring bean</code>。只需要构建出扩展项目的jar包即可。</p> </li> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">使用以下配置：</p> </li> 
</ul> 
<pre style="margin-left:0; margin-right:0"><code class="language-yaml">shenyu:
  extPlugin:
    path:  //加载扩展插件jar包路径
    enabled: true //是否开启
    threads: 1  //加载插件线程数量
    scheduleTime: 300 //间隔时间（单位：秒）
    scheduleDelay: 30 //网关启动后延迟多久加载（单位：秒）
</code></pre> 
<p><span style="color:inherit">插件加载路径详解</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">此路径是为存放扩展插件jar包的目录。</p> </li> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">可以使用 <code>-Dplugin-ext=xxxx</code> 指定，也可以使用 <code>shenyu.extPlugin.path</code>配置文件指定，如果都没配置，默认会加载网关启动路径下的 <code>ext-lib</code>目录。</p> </li> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">优先级 ：<code>-Dplugin-ext=xxxx</code> > <code>shenyu.extPlugin.path</code> > <code>ext-lib(default)</code></p> </li> 
</ul> 
<h4 style="margin-left:0; margin-right:0"><span style="color:inherit">灰度发布</span></h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span style="color:inherit">dubbo灰度发布请查看: </span></li> 
</ul> 
<p style="color:inherit; margin-left:0; margin-right:0">https://shenyu.apache.org/zh/docs/next/plugin-center/proxy/dubbo-plugin</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span style="color:inherit">springCloud灰度发布请查看：</span></li> 
</ul> 
<p style="color:inherit; margin-left:0; margin-right:0">https://shenyu.apache.org/zh/docs/next/plugin-center/proxy/spring-cloud-plugin</p> 
<h4 style="margin-left:0; margin-right:0"><span style="color:inherit">下个版本规划</span></h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">GRPC,Tars,Sofa,Motan灰度发布的支持</p> </li> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">MQTT协议的支持。</p> </li> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">其他插件的增强。</p> </li> 
 <li> <p style="color:inherit; margin-left:0; margin-right:0">新增Agent模块，提供网关Tracing的功能</p> </li> 
</ul> 
<h4 style="margin-left:0; margin-right:0"><span style="color:inherit">关于Apache ShenYu</span></h4> 
<p style="color:inherit; margin-left:0; margin-right:0">高性能，多协议，易扩展，响应式的API网关。于2021年5月进入Apache基金会进行孵化。</p> 
<p style="color:inherit; margin-left:0; margin-right:0">官网地址：https://shenyu.apache.org</p> 
<p style="color:inherit; margin-left:0; margin-right:0">Gitee地址 ： https://gitee.com/Apache-ShenYu/incubator-shenyu<br> Github地址：https://github.com/apache/incubator-shenyu</p>
                                        </div>
                                      
</div>
            