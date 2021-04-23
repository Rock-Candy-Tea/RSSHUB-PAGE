
---
title: '使用Jib来容器化Spring Boot应用'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210420/a562021067dab30a629194e75ae54fc7.png'
author: Dockone
comments: false
date: 2021-04-23 00:26:42
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210420/a562021067dab30a629194e75ae54fc7.png'
---

<div>   
<br>【把做大会】本文讲解了如何在不安装任何Docker客户端或使用Dockerfiles的情况下，通过使用Google的Jib为Spring Boot应用程序创建Docker或兼容OCI的镜像。<br>
<br>在本文中，我们将学习如何在不安装Docker客户端或使用Dockerfile的情况下为我们的Spring Boot应用程序创建Docker或兼容OCI的镜像。我们将在Jib的帮助下完成这一切。<br>
<h3>什么是Jib?</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210420/a562021067dab30a629194e75ae54fc7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210420/a562021067dab30a629194e75ae54fc7.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Jib是谷歌开发的一个Java容器化工具，它可以让Java开发者使用Maven、Gradle等构建工具构建容器。<br>
<br>但这并不是Jib真正有趣的地方，因为你不需要知道任何关于安装Docker、维护Dockerfiles等的知识。作为一个开发者，你只关心你将产生的程序包（jar、war等），你不需要理睬任何与Docker相关的废话（比如构建/推送等）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210420/115021bb8c94261aa29ad01015e2d71f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210420/115021bb8c94261aa29ad01015e2d71f.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Jib vs. Docker构建流程 （Image source Google Cloud）</em><br>
<br>哇，这真的很厉害！但怎么个厉害法？<br>
<h3>如何玩转<strong>Jib</strong></h3>有了Jib，你可以通过在你的<code class="prettyprint">pom.xml</code>或<code class="prettyprint">build.gradle</code>文件中添加一个Maven或Gradle插件，在短时间内将你的Java应用容器化，就是这么简单。我们将首先介绍Maven，在后面的文章中，我们会提到Gradle，那我们就开始吧。<br>
<br>我们将使用Spring <a href="https://start.spring.io/">Initializr</a>来生成一个示例的Spring Boot项目。我们的Spring Boot应用程序的源代码可以在<a href="https://github.com/userac/spring-boot-jib.git">这里</a>中找到。它只是在通过Jib推送镜像并通过Docker运行镜像时打印一条Hello消息。<br>
<br>一旦我们把IDE配置完毕，就可以进行下一步了。<br>
<h4>配置Maven</h4><pre class="prettyprint"><plugin><br>
<groupId>com.google.cloud.tools</groupId><br>
<artifactId>jib-maven-plugin</artifactId><br>
<version>2.6.0</version><br>
<configuration><br>
  <from><br>
     <image>gcr.io/distroless/java:11</image><br>
  </from><br>
  <to><br>
     <image>registry.hub.docker.com/hiashish/spring-boot-jib-image</image><br>
  </to><br>
</configuration><br>
</plugin><br>
</pre><br>
对于Maven来说，你可以把上面的内容粘贴到你的<code class="prettyprint">pom.xml</code>的插件部分就可以。但我想在这里解释一下<code class="prettyprint">&lt;from></code>和<code class="prettyprint">&lt;image></code>标签。<br>
<br><blockquote><br><code class="prettyprint">&lt;from></code>配置用于构建应用程序的基础镜像</blockquote>通常情况下，你不需要提供<from>作为默认值，因为它使用的是无发行版的Java 8镜像。然而，我使用的是Java 11，所以我需要在这里明确配置这一项。此外，根据你的实际场景，你可能想要使用不同的基础镜像。<br>
<br><blockquote><br><code class="prettyprint">&lt;image></code>指的是将推送到容器注册中心的目标映像名称</blockquote>我使用的是Docker注册表，但你可以使用任何云提供商的（ECS、GCR、ACR）容器注册。<br>
<br>关于插件使用的其他配置选项，你可以参考<a href="https://github.com/GoogleContainerTools/jib/tree/master/jib-maven-plugin">文档</a>。<br>
<h4>配置注册中心的访问密钥</h4>如果要推送镜像，我们需要在Maven的<code class="prettyprint">settings.xml</code>文件中添加注册中心的证书。由于我们只是在做演示，所以这样提供凭证是可以的，但要避免在真实世界的项目中使用，因为它不安全。你可能希望按照<a href="https://maven.apache.org/guides/mini/guide-encryption.html">这里提到的方式</a>来确保证书的安全。<br>
<pre class="prettyprint"><server><br>
<id>registry.hub.docker.com</id><br>
<username>username</username><br>
<password>password</password><br>
</server><br>
</pre><br>
<h4>构建镜像</h4>要建立一个镜像，我们可以通过以下方式来实现。<br>
<br><strong>在IDE中构建</strong><br>
<br>例如，在IntelliJ中，你可以进入项目的Maven视图，然后进入Plugins>jib下，然后右键点击并运行Maven构建。你可能想创建一个IntelliJ运行配置，可以运行Maven目标，如clean、编译等，然后推送你的镜像。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210420/1ed9ad72a877bb75f334f618770c787a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210420/1ed9ad72a877bb75f334f618770c787a.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>使用命令行</strong><br>
<br>只需运行下面的命令来构建应用程序的镜像。请确保你已经安装了Maven。<br>
<pre class="prettyprint">mvn compile jib:build<br>
</pre><br>
这将触发编译、构建流程，然后将应用程序的镜像推送到配置的容器注册中心。<br>
<br>以下是输出结果。<br>
<pre class="prettyprint">ashish@MacBook-Air springboot % mvn compile jib:build<br>
[INFO] Scanning for projects…<br>
[INFO]<br>
[INFO] — — — — — — — — — — < com.example:spring-boot-jib > — — — — — — — — — — -<br>
[INFO] Building springboot 0.0.1-SNAPSHOT<br>
[INFO] — — — — — — — — — — — — — — — — [ jar ] — — — — — — — — — — — — — — — — -<br>
[INFO]<br>
[INFO] — — maven-resources-plugin:3.1.0:resources (default-resources) @ spring-boot-jib — -<br>
[INFO] Using ‘UTF-8’ encoding to copy filtered resources.<br>
[INFO] Copying 1 resource<br>
[INFO] Copying 0 resource<br>
[INFO]<br>
[INFO] — — maven-compiler-plugin:3.8.1:compile (default-compile) @ spring-boot-jib — -<br>
[INFO] Nothing to compile — all classes are up to date<br>
[INFO]<br>
[INFO] — — jib-maven-plugin:2.6.0:build (default-cli) @ spring-boot-jib — -<br>
[WARNING] ‘mainClass’ configured in ‘maven-jar-plugin’ is not a valid Java class: $&#123;start-class&#125;<br>
[INFO]<br>
[INFO] Containerizing application to registry.hub.docker.com/hiashish/spring-boot-jib-image…<br>
[WARNING] Base image ‘gcr.io/distroless/java:11’ does not use a specific image digest — build may not be reproducible<br>
[INFO] Using credentials from Maven settings file for registry.hub.docker.com/hiashish/spring-boot-jib-image<br>
[INFO] Using base image with digest: sha256:b25c7a4f771209c2899b6c8a24fda89612b5e55200ab14aa10428f60fd5ef1d1<br>
[INFO]<br>
[INFO] Executing tasks:<br>
[INFO]<br>
[INFO] Executing tasks:<br>
[INFO]<br>
[INFO] Executing tasks:<br>
[INFO] [======= ] 25.0% complete<br>
[INFO]<br>
[INFO] Executing tasks:<br>
[INFO] [======= ] 25.0% complete<br>
[INFO] > pushing blob sha256:6508f436f385b3751366f90b6…<br>
[INFO]<br>
[INFO] Executing tasks:<br>
[INFO] [======= ] 25.0% complete<br>
[INFO] > pushing blob sha256:6508f436f385b3751366f90b6…<br>
[INFO] > pushing blob sha256:c5e22041fc97b838b93a2e18d…<br>
[INFO]<br>
[INFO] Executing tasks:<br>
[INFO] [======= ] 25.0% complete<br>
[INFO] > pushing blob sha256:6508f436f385b3751366f90b6…<br>
[INFO] > pushing blob sha256:c5e22041fc97b838b93a2e18d…<br>
[INFO] > pushing blob sha256:b25902383f9ee26808b68ca62…<br>
[INFO]<br>
[INFO] Executing tasks:<br>
[INFO] [======= ] 25.0% complete<br>
[INFO] > pushing blob sha256:6508f436f385b3751366f90b6…<br>
[INFO] > pushing blob sha256:c5e22041fc97b838b93a2e18d…<br>
[INFO] > pushing blob sha256:b25902383f9ee26808b68ca62…<br>
[INFO] > checking base image layer sha256:31eb28996804…<br>
[INFO]<br>
[INFO] Executing tasks:<br>
[INFO] [======== ] 27.8% complete<br>
[INFO] > pushing blob sha256:c5e22041fc97b838b93a2e18d…<br>
[INFO] > pushing blob sha256:b25902383f9ee26808b68ca62…<br>
[INFO] > checking base image layer sha256:31eb28996804…<br>
[INFO]<br>
[INFO] Executing tasks:<br>
[INFO] [========= ] 30.6% complete<br>
[INFO] > pushing blob sha256:c5e22041fc97b838b93a2e18d…<br>
[INFO] > checking base image layer sha256:31eb28996804…<br>
[INFO]<br>
[INFO] Executing tasks:<br>
[INFO] [========== ] 33.3% complete<br>
[INFO] > checking base image layer sha256:31eb28996804…<br>
[INFO]<br>
[INFO] Executing tasks:<br>
[INFO] [=========== ] 35.0% complete<br>
[INFO]<br>
[INFO] Executing tasks:<br>
[INFO]<br>
[INFO]<br>
[INFO]<br>
[INFO] Container entrypoint set to [java, -cp, /app/resources:/app/classes:/app/libs/*, com.jib.example.spring.SpringbootApplication]<br>
[INFO]<br>
[INFO] Built and pushed image as registry.hub.docker.com/hiashish/spring-boot-jib-image<br>
[INFO] Executing tasks:<br>
[INFO] [=========================== ] 91.7% complete<br>
[INFO] > launching layer pushers<br>
[INFO]<br>
[INFO] — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —<br>
[INFO] BUILD SUCCESS<br>
[INFO] — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —<br>
[INFO] Total time: 8.746 s<br>
[INFO] Finished at: 2020–11–16T02:34:33+05:30<br>
[INFO] — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —<br>
</pre><br>
<h4>运行镜像</h4>我们已经成功地将镜像（镜像名称：spring-boot-jib-image）推送到<a href="https://hub.docker.com/r/hiashish/spring-boot-jib-image">Docker注册中心</a>。现在我们可以使用Docker来运行这个镜像，<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210420/4e81dfeb5876b16906b6d0ae9a1236dc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210420/4e81dfeb5876b16906b6d0ae9a1236dc.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>运行镜像</em><br>
<br>正如你所看到的，我们的应用程序正在一个容器内运行。现在只需运行curl命令，你就会收到来自Spring Boot应用程序的hello消息。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210420/be086f825c18c52a6e302d7fc00d38c8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210420/be086f825c18c52a6e302d7fc00d38c8.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Hello消息</em><br>
<h3>结论</h3>在这篇文章中，我们已经了解了如何在没有Docker的情况下对我们的Java应用进行容器化。另外，通过Jib，你也可以使用Docker来构建镜像，当然这并不是Jib的最佳实践，不值一提。在你的Java应用中使用Jib的其他好处包括：与Java应用更紧密的集成，更快的构建速度，可重复的构建，得到Google的支持等等。如果你想要详细了解Jib的更多特性与优势，可以访问<a href="https://cloud.google.com/blog/products/application-development/introducing-jib-build-java-docker-images-better">这个链接</a>。<br>
<br><strong>原文链接：<a href="https://dzone.com/articles/containerizing-springboot-application-with-jib">Containerizing SpringBoot Application With Jib</a>（翻译：小灰灰）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            