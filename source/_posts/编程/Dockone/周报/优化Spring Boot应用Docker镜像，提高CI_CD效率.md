
---
title: '优化Spring Boot应用Docker镜像，提高CI_CD效率'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210402/d7a514d8c4333ad2ec342da95218a1c3.png'
author: Dockone
comments: false
date: 2021-04-05 12:10:30
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210402/d7a514d8c4333ad2ec342da95218a1c3.png'
---

<div>   
<br>越来越多的项目容器化，Docker已经成为软件开发中的重要工具。通常我们可以通过如下的<code class="prettyprint">Dockerfile</code>把<strong>Spring Boot</strong>应用的<strong>fat jar</strong>打包成Docker镜像：<br>
<pre class="prettyprint">FROM adoptopenjdk:8-jre-hotspot  <br>
ARG JAR_FILE=target/*.jar  <br>
COPY $&#123;JAR_FILE&#125; app.jar  <br>
EXPOSE 8080  <br>
ENTRYPOINT ["java","-jar","/app.jar"]   <br>
</pre><br>
看起来不错，但是你会发现如果我们修改了业务代码，镜像都会重新构建，哪怕你仅仅修改了一个字符串。如果你使用了CI/CD去构建部署Docker镜像，你会发现有时候CI管道中构建的时间会很长，甚至卡住不动，特别在镜像比较多的时候这种感觉非常明显。所以我们项目要优化这个地方。<br>
<h3>Docker的分层机制</h3>要优化就要了解Docker镜像的构建分层机制。<strong>Docker镜像由很多层组成，每个层代表Dockerfile中的一条指令。每一层都是基础层上变化的增量，而且自下而上的进行增量构建。</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210402/d7a514d8c4333ad2ec342da95218a1c3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210402/d7a514d8c4333ad2ec342da95218a1c3.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Docker镜像层</em><br>
<br>这种机制其实也是Docker名称的由来，就像码头工人在码货物一样。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210402/3ce23a27fba990180c8872650f594c96.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210402/3ce23a27fba990180c8872650f594c96.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
另外当我们构建Docker镜像时，它会被分层提取并缓存在主机中，这些层可以被重用，这就给了我们优化的机会。<br>
<br>就像上面的集装箱，我们如果把容易变动的集装箱放在底层，每次变动我们就需要把它上面的移开；如果我们把它置于底层就可以减少工作量。对于Docker镜像的构建构建也是这样。<br>
<h3>Spring Boot 镜像的优化</h3>Spring Boot的<strong>fat jar</strong>如果能拆分成一层一层构建，把重复的层从主机缓存中复用起来就可以大大提高效率。所以按照变动的频率Spring Boot应用可以划分如下的层级：<br>
<ul><li><code class="prettyprint">dependencies</code>  （依赖项一般变化不大）</li><li><code class="prettyprint">spring-boot-loader</code>（Spring Boot加载器变化也不大）</li><li><code class="prettyprint">snapshot-dependencies</code>  （快照依赖，为快照版本的依赖，更新迭代的会快一些）</li><li><code class="prettyprint">application</code>  （业务层，也就是我们最频繁变动的）</li></ul><br>
<br>自<strong>Spring Boot 2.3</strong>起，Spring Boot提供了<code class="prettyprint">spring-boot-jarmode-layertools</code>的jar包，该jar将作为依赖项添加到应用的jar中。通过<code class="prettyprint">layertools</code>jar模式启动jar：<br>
<pre class="prettyprint">$ java -Djarmode=layertools -jar my-app.jar<br>
</pre><br>
就会生成上述四种层级的索引文件<code class="prettyprint">layers.idx</code>。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210402/47940e9c060334fbf5f3589ef48b757d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210402/47940e9c060334fbf5f3589ef48b757d.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
上面就是该模式下构建的<strong>Spring Boot</strong>  应用jar的信息，我们可以看到这两个东西。<br>
<br><blockquote><br>这个功能依赖<code class="prettyprint">spring-boot-maven-plugin</code>插件。</blockquote>我们只需要将<code class="prettyprint">Dockerfile</code>修改为：<br>
<pre class="prettyprint"># 第一阶段使用layertools的extract命令将应用程序拆分为多个层，本次构建标记为builder  <br>
FROM adoptopenjdk:8-jre-hotspot as builder  <br>
WORKDIR application  <br>
ARG JAR_FILE=target/*.jar  <br>
COPY $&#123;JAR_FILE&#125; app.jar  <br>
RUN java -Djarmode=layertools -jar app.jar extract  <br>
<br>
#  第二阶段从分层中复制并构建镜像  <br>
FROM adoptopenjdk:8-jre-hotspot  <br>
WORKDIR application  <br>
# 从上面构建的builder中复制层，注意保证层的顺序  <br>
COPY --from=builder application/dependencies/ ./  <br>
COPY --from=builder application/spring-boot-loader/ ./  <br>
COPY --from=builder application/snapshot-dependencies/ ./  <br>
COPY --from=builder application/application/ ./  <br>
ENTRYPOINT ["java", "org.springframework.boot.loader.JarLauncher"] <br>
</pre><br>
就可以复用主机中的Docker缓存层来加速构建效率。构建命令为：<br>
<pre class="prettyprint">docker build --build-arg JAR_FILE=path/to/myapp.jar . -tag demo<br>
</pre><br>
然后会输出：<br>
<pre class="prettyprint">Sending build context to Docker daemon  41.87MB  <br>
Step 1/12 : adoptopenjdk:8-jre-hotspot as builder  <br>
– -> 973c18dbf567  <br>
Step 2/12 : WORKDIR application  <br>
– -> Using cache  <br>
– -> b6b89995bd66  <br>
Step 3/12 : ARG JAR_FILE=target/*.jar  <br>
– -> Using cache  <br>
– -> 2065a4ad00d4  <br>
Step 4/12 : COPY $&#123;JAR_FILE&#125; app.jar  <br>
– -> c107bce376f9  <br>
Step 5/12 : RUN java -Djarmode=layertools -jar app.jar extract  <br>
– -> Running in 7a6dfd889b0e  <br>
Removing intermediate container 7a6dfd889b0e  <br>
– -> edb00225ad75  <br>
Step 6/12 : FROM  adoptopenjdk:8-jre-hotspot  <br>
– -> 973c18dbf567  <br>
Step 7/12 : WORKDIR application  <br>
– -> Using cache  <br>
– -> b6b89995bd66  <br>
Step 8/12 : COPY – from=builder application/dependencies/ ./  <br>
– -> Using cache  <br>
– -> c9a01ed348a9  <br>
Step 9/12 : COPY – from=builder application/spring-boot-loader/ ./  <br>
– -> Using cache  <br>
– -> e3861c690a96  <br>
Step 10/12 : COPY – from=builder application/snapshot-dependencies/ ./  <br>
– -> Using cache  <br>
– -> f928837acc47  <br>
Step 11/12 : COPY – from=builder application/application/ ./  <br>
– -> 3a5f60a9b204  <br>
Step 12/12 : ENTRYPOINT ["java", "org.springframework.boot.loader.JarLauncher"]  <br>
– -> Running in f1eb4befc4e0  <br>
Removing intermediate container f1eb4befc4e0  <br>
– -> 8575cc3ac2e3  <br>
Successfully built 8575cc3ac2e3  <br>
Successfully tagged demo:latest <br>
</pre><br>
<br><blockquote><br><code class="prettyprint">java -Djarmode=layertools -jar</code>  不建议在启动脚本中使用，仅推荐在构建中使用 。</blockquote><h3>补充</h3>关于插件目前有版本上的差异，在<strong>Spring Boot 2.3</strong>中需要：<br>
<pre class="prettyprint"><build>  <br>
<plugins>  <br>
<plugin>  <br>
  <groupId>org.springframework.boot</groupId>  <br>
  <artifactId>spring-boot-maven-plugin</artifactId>  <br>
  <configuration>  <br>
      <layers>  <br>
        <enabled>true</enabled>  <br>
      </layers>  <br>
  </configuration>  <br>
</plugin>  <br>
...  <br>
</plugins>  <br>
...  <br>
</build><br>
</pre><br>
在<strong>Spring Boot 2.4.x</strong>以上版本默认：<br>
<pre class="prettyprint"><build>  <br>
<plugins>  <br>
    <plugin>  <br>
        <groupId>org.springframework.boot</groupId>  <br>
        <artifactId>spring-boot-maven-plugin</artifactId>  <br>
        <!--当然你可以修改layers.enabled为false以关闭此功能。-->  <br>
    </plugin>  <br>
</plugins>  <br>
</build><br>
</pre><br>
通过启用分层构建Spring Boot应用镜像，我明显感觉到推送镜像的速度快了不少（当然这是依赖没有改动的情况下）；另外从远程拉取镜像时只需要拉取变化的层，速度也明显加快了；对构建其实上是构建了两次，虽然配合缓存，效率其实变化不大。也就是说在镜像的网络传输上分层构建有明显的优势，值得一试。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/JMcBd6OULcVd9aRKyEGc0w" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/JMcBd6OULcVd9aRKyEGc0w</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            