
---
title: 'SpringBoot Admin2.0 集成 Java 诊断神器 Arthas 实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://ucc.alicdn.com/pic/developer-ecology/43a4389a8f2d4ecc909f361551b42d1e.png'
author: Dockone
comments: false
date: 2021-04-12 12:10:35
thumbnail: 'https://ucc.alicdn.com/pic/developer-ecology/43a4389a8f2d4ecc909f361551b42d1e.png'
---

<div>   
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/43a4389a8f2d4ecc909f361551b42d1e.png" alt="头图.png" referrerpolicy="no-referrer"><br>
<br>作者 | sparrow<br>
来源 | <a href="https://mp.weixin.qq.com/s/RlPmNYz13wQHoM5C4Xrmaw">阿里巴巴云原生公众号</a><br>
<br>项目最初使用 Arthas 主要有两个目的：<br>
<ol><li>通过 arthas 解决实现测试环境、性能测试环境以及生产环境性能问题分析工具的问题。</li><li>通过使用 jad、mc、redefine 功能组合实现生产环境部分节点代码热更新的能力。</li></ol><br>
<br><h1>技术选型相关</h1>因为公司还未能建立起较为统一的生产微服务配置以及状态管理的能力，各自系统的研发运维较为独立。现在项目使用了 Spring Cloud 以及 Eureka 的框架结构，和 SBA 的基础支撑能力较为匹配，同时，SBA 已经可以提供服务感知，日志级别配置管理，以及基于 actuator 的 JVM、Spring 容器的众多管理插件，可以满足基础使用的需求。<br>
<br>在调研期间，Arthas 整体版本为 3.4.5，提供了基于 Webconsole 的 Tunner Server 模式，通过前面链接文章已经实践，与SBA已经可以实现集成。因为项目本身没有历史包袱，在实际集成的过程中采用了 SBA 2.0 版本以提供更多的管理功能和图形界面能力。其他优点：<br>
<ul><li><br>web console 界面嵌入 SBA 整体密码登录和网页权限管理，实现登陆 SBA 后才可以使用相关 arthas web console 的功能。</li><li><br>基于SBA 客户端依赖的 jolokia-core 开放目标服务进程的 jmx 管理，通过实现 jmx 接口复用 SBA 的相关操作界面，减少前端界面开发能力的要求。</li></ul><br>
<br><h1>整体结构</h1><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/02ac5f7190cb5f19269ac4890416f239.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/02ac5f7190cb5f19269ac4890416f239.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>几个关键点，使用 JVM 内置 Arthas Spring Boot 插件，参考工商银行的模式建立完善的客户端下载以及修改脚本实现远程控制。内置方案工作开发量小，只需要集成相关的开源组件即可实现相关的远程使用的模式并兼顾安全。工银的方案大而全适合整体架构规划后配置专有研发团队之城。内置方案同时包含通过 JMX 的启停操作（基于 3.4.5 的 Spring Boot 插件无法获得相关句柄，暂时无法实现），默认不启动。通过远程 JMX 开通后，JVM 新增相关线程 8 个，新增虚拟机内存 30MB 左右，和本文参考的 SBA1.0 方案相同，需要考虑在线开启前 JVM 内存是否可以支持。<br>
<br><h1>实现效果</h1>SBA 2.0 最大的方便就是提供了配置化链接外部网页的能力，同时如果网页实现在当前 JVM 进程，可以实现 Spring-Security 的本地权限管理，在生产环境下只有在登录 SBA 后才能使用相关集成的 arthas 功能。<br>
<ul><li>登录界面</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/067b8881c30f257fa55be43f9ae4d294.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/067b8881c30f257fa55be43f9ae4d294.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>外嵌连接位置</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/d2a3ea070a6c79e32ecf4f47a40e8d56.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/d2a3ea070a6c79e32ecf4f47a40e8d56.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>JMX 的使用</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/4ba94130bb9fd4994f8e38707d1a7b81.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/4ba94130bb9fd4994f8e38707d1a7b81.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/b83c0f588f3468d3f6d0b1ee98f6acfa.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/b83c0f588f3468d3f6d0b1ee98f6acfa.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>跳转 arthas web console</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/3a9a98621393eff2cf8c980c4fe1689b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/3a9a98621393eff2cf8c980c4fe1689b.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h1>改造方案</h1>参考原文 -<a href="http://mp.weixin.qq.com/s?__biz=MzUzNzYxNjAzMg==&mid=2247500442&idx=2&sn=39118e58718b2434d605d968d8c9dceb&chksm=fae6c955cd91404319ab47d7641ec57ec24ef2091fb6be3829a0ece8a5f3612d91449e001e13&scene=21#wechat_redirect">SpringBoot Admin 集成 Arthas 实践</a>中实现的几个步骤。<br>
<br><h2>1. 整体工程结构</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/3753c1db319b9d42a7cf49e44a90bf83.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210412/3753c1db319b9d42a7cf49e44a90bf83.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>整体工程修改自 SBA 开源项目的 example 工程，具体使用 custom-ui 的工程链接为：<a href="https://github.com/codecentric/spring-boot-admin/tree/master/spring-boot-admin-samples/spring-boot-admin-sample-custom-ui">_[spring-boot-admin-sample-custom-ui]_</a>_，_红色框的部分是 arthas web console 的全部静态文件，通过 Maven Resource 的指定配置打入指定目录，实现 SBA 启动时的自定义加载。maven resource 配置--下：<br>
<br><code class="prettyprint">&lt;resource><br>
                &lt;directory>static&lt;/directory><br>
                &lt;targetPath>$&#123;project.build.directory&#125;/classes/META-INF/spring-boot-admin-server-ui/extensions/arthas<br>
                &lt;/targetPath><br>
                &lt;filtering>false&lt;/filtering><br>
            &lt;/resource></code><br>
<br>最终构建的 jar 中 META-INFO 中包含相关的文件即可在 SBA 自带的 tomcat 启动后加载到相关的静态资源，最后的 url 和自定义实现的 arthas console 配置的外部 URL 对应即可。<br>
<br><h2>2. 外部链接配置</h2>SBA 2.0 开始已经使用 vue 全家桶了，扩展集成均比较方便。其中，官方文档给出了外嵌连接的配置方式：<a href="https://codecentric.github.io/spring-boot-admin/2.3.1/#customizing-external-views">_[Linking / Embedding External Pages]_</a>_。_<br>
<br>参考 sba example 工程的 application.yml 配置即可：<br>
<br><code class="prettyprint"><h1>tag::customization-external-views[]</h1>    spring:<br>
      boot:<br>
        admin:<br>
          ui:<br>
            external-views:<br>
              - label: &quot;Arthas Console&quot;<br>
                url: http://21.129.49.153:8080/<br>
                order: 1900<br>
    # end::customization-external-views[]</code><br>
<br><h2>3. 对应 Spring MVC controller 实现</h2>参考引用原实现的 SBA 集成部分，该部分主要修改实现如下功能：<br>
<ul><li>实现 tunnel server 已经加载实例列表的刷新并展示到前段 AgentID 框供选择点击链接。</li><li>实现自定义 IP 地址的刷新（解决生产环境双生产 IP 和运维段 IP 不一致的问题）。</li></ul><br>
<br><h2>4. Arthas Spring Boot 插件修改和配置</h2>参考引用原实现的 SBA 集成中插件修改以及客户端配置 application.yml。<br>
<br>对原版 Spring boot 插件修改主要在于原有插件是通过 Spring的@ConditionalOnMissingBean 实现自动加载。<br>
<br>修改主要是通过修改这部分实现通过配置文件默认不启动，然后使用时通过远程启动相关 agent 线程。<br>
<br><h2>5. 基于 Spring Actuator 的 JMX 实现</h2>SBA client 在 maven 引入中会默认引入 jolokia-core.jar，如果没有因为 SBA client 依赖可以自行引入该包，可以实现通过 actuator 开放基于 http 的 jmx 操作能力和 SBA 控制台的相关功能无缝配合。<br>
<br>application.yml 中开放 management 相关配置，根据自身环境情况，也可以开在客户端侧开启 Spring security 认证，SBA 也可以很好的支持通过服务发现实现密码保护 actuator 端点的访问。<br>
<br><code class="prettyprint"><h1>放开management</h1>    management:<br>
      endpoints:<br>
        web:<br>
          exposure:<br>
            # 这里用* 代表暴露所有端点只是为了观察效果，实际中按照需进行端点暴露<br>
            include: &quot;*&quot;<br>
            exclude: env<br>
      endpoint:<br>
        health:<br>
          # 详细信息显示给所有用户。<br>
          show-details: ALWAYS<br>
      health:<br>
        status:<br>
          http-mapping:<br>
            # 自定义健康检查返回状态码对应的 http 状态码<br>
            FATAL:  503</code><br>
<br>JMX 实现参考原文中 EnvironmentChangeListener 的实现思路，基于 Spring 的 JMX 注解实现即可。<br>
<br>```<br>
@Component<br>
   @ManagedResource(objectName = "com.ArthasAgentManageMbean:name=ArthasMbean", description = "Arthas远程管理Mbean")<br>
   public class ArthasMbeanImpl &#123;<br>
<br>       @Autowired<br>
       private Map<String, String> arthasConfigMap;<br>
<br>       @Autowired<br>
       private ArthasProperties arthasProperties;<br>
<br>       @Autowired<br>
       private ApplicationContext applicationContext;<br>
<br>       /**<br>
        * 初始化<br>
        *<br>
        * @return<br>
        */<br>
       private ArthasAgent arthasAgentInit() &#123;<br>
           arthasConfigMap = StringUtils.removeDashKey(arthasConfigMap);<br>
           // 给配置全加上前缀<br>
           Map<String, String> mapWithPrefix = new HashMap<String, String>(arthasConfigMap.size());<br>
           for (Map.Entry<String, String> entry : arthasConfigMap.entrySet()) &#123;<br>
               mapWithPrefix.put("arthas." + entry.getKey(), entry.getValue());<br>
           &#125;<br>
           final ArthasAgent arthasAgent = new ArthasAgent(mapWithPrefix, arthasProperties.getHome(),<br>
                   arthasProperties.isSlientInit(), null);<br>
           arthasAgent.init();<br>
           return arthasAgent;<br>
       &#125;<br>
<br>       @ManagedOperation(description = "获取配置Arthas Tunnel Server地址")<br>
       public String getArthasTunnelServerUrl() &#123;<br>
           return arthasProperties.getTunnelServer();<br>
       &#125;<br>
<br>       @ManagedOperation(description = "设置Arthas Tunnel Server地址，重新attach后生效")<br>
       @ManagedOperationParameter(name = "tunnelServer", description = "example:ws://127.0.0.1:7777/ws")<br>
       public Boolean setArthasTunnelServerUrl(String tunnelServer) &#123;<br>
           if (tunnelServer == null || tunnelServer.trim().equals("") || tunnelServer.indexOf("ws://") < 0) &#123;<br>
               return false;<br>
           &#125;<br>
           arthasProperties.setTunnelServer(tunnelServer);<br>
           return true;<br>
       &#125;<br>
<br>       @ManagedOperation(description = "获取AgentID")<br>
       public String getAgentId() &#123;<br>
           return arthasProperties.getAgentId();<br>
       &#125;<br>
<br>       @ManagedOperation(description = "获取应用名称")<br>
       public String getAppName() &#123;<br>
           return arthasProperties.getAppName();<br>
       &#125;<br>
<br>       @ManagedOperation(description = "获取ArthasConfigMap")<br>
       public HashMap<String, String> getArthasConfigMap() &#123;<br>
           return (HashMap) arthasConfigMap;<br>
       &#125;<br>
<br>       @ManagedOperation(description = "返回是否已经加载Arthas agent")<br>
       public Boolean isArthasAttched() &#123;<br>
           DefaultListableBeanFactory defaultListableBeanFactory = (DefaultListableBeanFactory) applicationContext.getAutowireCapableBeanFactory();<br>
           String bean = "arthasAgent";<br>
           if (defaultListableBeanFactory.containsBean(bean)) &#123;<br>
               return true;<br>
           &#125;<br>
           return false;<br>
       &#125;<br>
<br>       @ManagedOperation(description = "启动Arthas agent")<br>
       public Boolean startArthasAgent() &#123;<br>
           DefaultListableBeanFactory defaultListableBeanFactory = (DefaultListableBeanFactory) applicationContext.getAutowireCapableBeanFactory();<br>
           String bean = "arthasAgent";<br>
           if (defaultListableBeanFactory.containsBean(bean)) &#123;<br>
               ((ArthasAgent) defaultListableBeanFactory.getBean(bean)).init();<br>
               return true;<br>
           &#125;<br>
           defaultListableBeanFactory.registerSingleton(bean, arthasAgentInit());<br>
           return true;<br>
       &#125;<br>
<br>       @ManagedOperation(description = "关闭Arthas agent，暂未实现")<br>
       public Boolean stopArthasAgent() &#123;<br>
           // TODO 无法获取自定义tmp文件夹加载的classLoader，因此无法获取到com.taobao.arthas.core.server.ArthasBootstrap类并调用destroy方法<br>
           DefaultListableBeanFactory defaultListableBeanFactory = (DefaultListableBeanFactory) applicationContext.getAutowireCapableBeanFactory();<br>
           String bean = "arthasAgent";<br>
           if (defaultListableBeanFactory.containsBean(bean)) &#123;<br>
               defaultListableBeanFactory.destroySingleton(bean);<br>
               return true;<br>
           &#125; else &#123;<br>
               return false;<br>
           &#125;<br>
       &#125;<br>
   &#125;<br>
```<br>
<br><h1>实际使用</h1>管理工程投产后，多次在生产环境用于问题排查和代码热修复。性能问题主要用于性能流控组件以及灰度发布相关配置参数的在线验证和 debug。<br>
<br>代码热加载相关初期通过 jad+mc 的方式进行操作，后续发现 jad 在部分代码上因环境配置以及 jvm 问题产生反编译代码不一致的情况，后续通过 maven 打包部署应用程序 source 压缩包的方式解决，直接使用和应用 jar 同版本构建的 source 进行修改更加可靠。整体方案在管理较为严格的生产环境提供了有效的性能分析以及热修复的能力。<br>
<br><h1>遗留问题</h1>现有官方提供的 com.taobao.arthas.agent.attach.ArthasAgent 中启动 arthas agent 的客户端使用的 arthasClassLoader 和 bootstrapClass 均为方法内的临时变量，外部无法获取相关句柄实现通过 bootstrapClass 关闭 arthas agent 的功能；临时解决方案为通过 JMX 启动后，在 web console 连接使用后，使用 stop 命令实现目标进程中 arthas agent 的关闭。<br>
<br>现有字节码加载工具可以很好的实现内部类，私有类的在线热部署替换，同时经测试可以兼容 SkyWalk8.x 版本的 javaagent 插件，但是在测试环境因为配置有 jacoco 覆盖度采集插件与 Arthas 字节码产生了不兼容的情况，在部分环境使用时需要先关闭对应的 agent 后才能正常使用 arthas 的相关功能。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            