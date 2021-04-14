
---
title: 'SpringBoot Admin2.0 集成 Java 诊断神器 Arthas 实践'
categories: 
 - 编程
 - segmentfault
 - 用户
headimg: 'https://segmentfault.com/img/bVcRd3t'
author: segmentfault
comments: false
date: 2021-04-14 08:08:45
thumbnail: 'https://segmentfault.com/img/bVcRd3t'
---

<div>   
<p>简介： 项目最初使用 Arthas 主要有两个目的： 1. 通过 arthas 解决实现测试环境、性能测试环境以及生产环境性能问题分析工具的问题。 2. 通过使用 jad、mc、redefine 功能组合实现生产环境部分节点代码热更新的能力。<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRd3t" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>作者 | sparrow<br>来源 | 阿里巴巴云原生公众号</p><p>本文来自 Arthas 2021 年 3 月征文投稿，4 月有奖征文参与方式可见文末。</p><p>项目最初使用 Arthas 主要有两个目的：</p><p>通过 arthas 解决实现测试环境、性能测试环境以及生产环境性能问题分析工具的问题。<br>通过使用 jad、mc、redefine 功能组合实现生产环境部分节点代码热更新的能力。<br>技术选型相关<br>因为公司还未能建立起较为统一的生产微服务配置以及状态管理的能力，各自系统的研发运维较为独立。现在项目使用了 Spring Cloud 以及 Eureka 的框架结构，和 SBA 的基础支撑能力较为匹配，同时，SBA 已经可以提供服务感知，日志级别配置管理，以及基于 actuator 的 JVM、Spring 容器的众多管理插件，可以满足基础使用的需求。</p><p>在调研期间，Arthas 整体版本为 3.4.5，提供了基于 Webconsole 的 Tunner Server 模式，通过前面链接文章已经实践，与SBA已经可以实现集成。因为项目本身没有历史包袱，在实际集成的过程中采用了 SBA 2.0 版本以提供更多的管理功能和图形界面能力。其他优点：</p><p>web console 界面嵌入 SBA 整体密码登录和网页权限管理，实现登陆 SBA 后才可以使用相关 arthas web console 的功能。<br>基于SBA 客户端依赖的 jolokia-core 开放目标服务进程的 jmx 管理，通过实现 jmx 接口复用 SBA 的相关操作界面，减少前端界面开发能力的要求。<br>整体结构<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRd3u" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>几个关键点，使用 JVM 内置 Arthas Spring Boot 插件，参考工商银行的模式建立完善的客户端下载以及修改脚本实现远程控制。内置方案工作开发量小，只需要集成相关的开源组件即可实现相关的远程使用的模式并兼顾安全。工银的方案大而全适合整体架构规划后配置专有研发团队之城。内置方案同时包含通过 JMX 的启停操作（基于 3.4.5 的 Spring Boot 插件无法获得相关句柄，暂时无法实现），默认不启动。通过远程 JMX 开通后，JVM 新增相关线程 8 个，新增虚拟机内存 30MB 左右，和本文参考的 SBA1.0 方案相同，需要考虑在线开启前 JVM 内存是否可以支持。</p><p>实现效果<br>SBA 2.0 最大的方便就是提供了配置化链接外部网页的能力，同时如果网页实现在当前 JVM 进程，可以实现 Spring-Security 的本地权限管理，在生产环境下只有在登录 SBA 后才能使用相关集成的 arthas 功能。</p><p>登录界面<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRd3h" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>外嵌连接位置<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRd3j" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>JMX 的使用<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRd3k" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRd3q" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>跳转 arthas web console<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRd3r" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>改造方案<br>参考原文 -SpringBoot Admin 集成 Arthas 实践中实现的几个步骤。</p><ol><li>整体工程结构<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRd3s" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></li></ol><p>整体工程修改自 SBA 开源项目的 example 工程，具体使用 custom-ui 的工程链接为：[_[spring-boot-admin-sample-custom-ui]_](<a href="https://github.com/codecentric/spring-boot-admin/tree/master/spring-boot-admin-samples/spring-boot-admin-sample-custom-ui)_%EF%BC%8C_%E7%BA%A2%E8%89%B2%E6%A1%86%E7%9A%84%E9%83%A8%E5%88%86%E6%98%AF" rel="nofollow">https://github.com/codecentri...</a> arthas web console 的全部静态文件，通过 Maven Resource 的指定配置打入指定目录，实现 SBA 启动时的自定义加载。maven resource 配置--下：</p><p><resource></p><pre><code>            <directory>static</directory>
            <targetPath>$&#123;project.build.directory&#125;/classes/META-INF/spring-boot-admin-server-ui/extensions/arthas
            </targetPath>
            <filtering>false</filtering>
        </resource></code></pre><p>最终构建的 jar 中 META-INFO 中包含相关的文件即可在 SBA 自带的 tomcat 启动后加载到相关的静态资源，最后的 url 和自定义实现的 arthas console 配置的外部 URL 对应即可。</p><ol><li>外部链接配置<br>SBA 2.0 开始已经使用 vue 全家桶了，扩展集成均比较方便。其中，官方文档给出了外嵌连接的配置方式：[_[Linking / Embedding External Pages]_](<a href="https://codecentric.github.io/spring-boot-admin/2.3.1/#customizing-external-views)_%E3%80%82_" rel="nofollow">https://codecentric.github.io...</a></li></ol><p>参考 sba example 工程的 application.yml 配置即可：</p><h1>tag::customization-external-views[]</h1><pre><code>spring:
  boot:
    admin:
      ui:
        external-views:
          - label: "Arthas Console"
            url: http://21.129.49.153:8080/
            order: 1900
# end::customization-external-views[]</code></pre><ol><li>对应 Spring MVC controller 实现<br>参考引用原实现的 SBA 集成部分，该部分主要修改实现如下功能：</li></ol><p>实现 tunnel server 已经加载实例列表的刷新并展示到前段 AgentID 框供选择点击链接。<br>实现自定义 IP 地址的刷新（解决生产环境双生产 IP 和运维段 IP 不一致的问题）。</p><ol><li>Arthas Spring Boot 插件修改和配置<br>参考引用原实现的 SBA 集成中插件修改以及客户端配置 application.yml。</li></ol><p>对原版 Spring boot 插件修改主要在于原有插件是通过 Spring的@ConditionalOnMissingBean 实现自动加载。</p><p>修改主要是通过修改这部分实现通过配置文件默认不启动，然后使用时通过远程启动相关 agent 线程。</p><ol><li>基于 Spring Actuator 的 JMX 实现<br>SBA client 在 maven 引入中会默认引入 jolokia-core.jar，如果没有因为 SBA client 依赖可以自行引入该包，可以实现通过 actuator 开放基于 http 的 jmx 操作能力和 SBA 控制台的相关功能无缝配合。</li></ol><p>application.yml 中开放 management 相关配置，根据自身环境情况，也可以开在客户端侧开启 Spring security 认证，SBA 也可以很好的支持通过服务发现实现密码保护 actuator 端点的访问。</p><h1>放开management</h1><pre><code>management:
  endpoints:
    web:
      exposure:
        # 这里用* 代表暴露所有端点只是为了观察效果，实际中按照需进行端点暴露
        include: "*"
        exclude: env
  endpoint:
    health:
      # 详细信息显示给所有用户。
      show-details: ALWAYS
  health:
    status:
      http-mapping:
        # 自定义健康检查返回状态码对应的 http 状态码
        FATAL:  503</code></pre><p>JMX 实现参考原文中 EnvironmentChangeListener 的实现思路，基于 Spring 的 JMX 注解实现即可。</p><p>@Component<br>   @ManagedResource(objectName = "com.ArthasAgentManageMbean:name=ArthasMbean", description = "Arthas远程管理Mbean")<br>   public class ArthasMbeanImpl &#123;</p><pre><code>   @Autowired
   private Map<String, String> arthasConfigMap;

   @Autowired
   private ArthasProperties arthasProperties;

   @Autowired
   private ApplicationContext applicationContext;

   /**
    * 初始化
    *
    * @return
    */
   private ArthasAgent arthasAgentInit() &#123;
       arthasConfigMap = StringUtils.removeDashKey(arthasConfigMap);
       // 给配置全加上前缀
       Map<String, String> mapWithPrefix = new HashMap<String, String>(arthasConfigMap.size());
       for (Map.Entry<String, String> entry : arthasConfigMap.entrySet()) &#123;
           mapWithPrefix.put("arthas." + entry.getKey(), entry.getValue());
       &#125;
       final ArthasAgent arthasAgent = new ArthasAgent(mapWithPrefix, arthasProperties.getHome(),
               arthasProperties.isSlientInit(), null);
       arthasAgent.init();
       return arthasAgent;
   &#125;

   @ManagedOperation(description = "获取配置Arthas Tunnel Server地址")
   public String getArthasTunnelServerUrl() &#123;
       return arthasProperties.getTunnelServer();
   &#125;

   @ManagedOperation(description = "设置Arthas Tunnel Server地址，重新attach后生效")
   @ManagedOperationParameter(name = "tunnelServer", description = "example:ws://127.0.0.1:7777/ws")
   public Boolean setArthasTunnelServerUrl(String tunnelServer) &#123;
       if (tunnelServer == null || tunnelServer.trim().equals("") || tunnelServer.indexOf("ws://") < 0) &#123;
           return false;
       &#125;
       arthasProperties.setTunnelServer(tunnelServer);
       return true;
   &#125;

   @ManagedOperation(description = "获取AgentID")
   public String getAgentId() &#123;
       return arthasProperties.getAgentId();
   &#125;

   @ManagedOperation(description = "获取应用名称")
   public String getAppName() &#123;
       return arthasProperties.getAppName();
   &#125;

   @ManagedOperation(description = "获取ArthasConfigMap")
   public HashMap<String, String> getArthasConfigMap() &#123;
       return (HashMap) arthasConfigMap;
   &#125;

   @ManagedOperation(description = "返回是否已经加载Arthas agent")
   public Boolean isArthasAttched() &#123;
       DefaultListableBeanFactory defaultListableBeanFactory = (DefaultListableBeanFactory) applicationContext.getAutowireCapableBeanFactory();
       String bean = "arthasAgent";
       if (defaultListableBeanFactory.containsBean(bean)) &#123;
           return true;
       &#125;
       return false;
   &#125;

   @ManagedOperation(description = "启动Arthas agent")
   public Boolean startArthasAgent() &#123;
       DefaultListableBeanFactory defaultListableBeanFactory = (DefaultListableBeanFactory) applicationContext.getAutowireCapableBeanFactory();
       String bean = "arthasAgent";
       if (defaultListableBeanFactory.containsBean(bean)) &#123;
           ((ArthasAgent) defaultListableBeanFactory.getBean(bean)).init();
           return true;
       &#125;
       defaultListableBeanFactory.registerSingleton(bean, arthasAgentInit());
       return true;
   &#125;

   @ManagedOperation(description = "关闭Arthas agent，暂未实现")
   public Boolean stopArthasAgent() &#123;
       // TODO 无法获取自定义tmp文件夹加载的classLoader，因此无法获取到com.taobao.arthas.core.server.ArthasBootstrap类并调用destroy方法
       DefaultListableBeanFactory defaultListableBeanFactory = (DefaultListableBeanFactory) applicationContext.getAutowireCapableBeanFactory();
       String bean = "arthasAgent";
       if (defaultListableBeanFactory.containsBean(bean)) &#123;
           defaultListableBeanFactory.destroySingleton(bean);
           return true;
       &#125; else &#123;
           return false;
       &#125;
   &#125;</code></pre><p>&#125;<br>实际使用<br>管理工程投产后，多次在生产环境用于问题排查和代码热修复。性能问题主要用于性能流控组件以及灰度发布相关配置参数的在线验证和 debug。</p><p>代码热加载相关初期通过 jad+mc 的方式进行操作，后续发现 jad 在部分代码上因环境配置以及 jvm 问题产生反编译代码不一致的情况，后续通过 maven 打包部署应用程序 source 压缩包的方式解决，直接使用和应用 jar 同版本构建的 source 进行修改更加可靠。整体方案在管理较为严格的生产环境提供了有效的性能分析以及热修复的能力。</p><p>遗留问题<br>现有官方提供的 com.taobao.arthas.agent.attach.ArthasAgent 中启动 arthas agent 的客户端使用的 arthasClassLoader 和 bootstrapClass 均为方法内的临时变量，外部无法获取相关句柄实现通过 bootstrapClass 关闭 arthas agent 的功能；临时解决方案为通过 JMX 启动后，在 web console 连接使用后，使用 stop 命令实现目标进程中 arthas agent 的关闭。</p><p>现有字节码加载工具可以很好的实现内部类，私有类的在线热部署替换，同时经测试可以兼容 SkyWalk8.x 版本的 javaagent 插件，但是在测试环境因为配置有 jacoco 覆盖度采集插件与 Arthas 字节码产生了不兼容的情况，在部分环境使用时需要先关闭对应的 agent 后才能正常使用 arthas 的相关功能。</p><p>欢迎登陆 start.aliyun.com 知行动手实验室体验 Arthas 57 个动手实验：<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRd3e" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>Arthas 实验预览<br><a href="https://developer.aliyun.com/article/783465?utm_content=g_1000262123" rel="nofollow">原文链接</a><br>本文为阿里云原创内容，未经允许不得转载。</p>  
</div>
            