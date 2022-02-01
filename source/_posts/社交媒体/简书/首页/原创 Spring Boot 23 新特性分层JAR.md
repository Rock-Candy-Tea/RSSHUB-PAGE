
---
title: '原创 Spring Boot 2.3 新特性分层JAR'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/2718590-0631384c801d4840.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/2718590-0631384c801d4840.png'
---

<div>   
<h2>背景</h2>
<p>在我们实际生产容器化部署过程中，往往会遇到 Docker 镜像很大，部署发布很慢的情况</p>
<p>影响 docker 镜像大小的因素，主要有以下三个方面：</p>
<ul>
<li><ol>
<li>基础镜像的大小 。尽量选择 aphine 作为基础镜像 减少操作系统内置软件</li>
</ol></li>
<li><ol start="2">
<li>Dockerfile 指令层数。 这就要求我们优化 Dockerfile 能合并在一行的尽量合并等</li>
</ol></li>
<li><ol start="3">
<li>应用 jar 的大小。这是今天要分享的重点内容</li>
</ol></li>
</ul>
<h3>helloworld 镜像</h3>
<p>我们先来基于 <code>spring boot 2.3.0</code> 构建一个最简单的 web helloworld，然后构建镜像。</p>
<pre><code>FROM adoptopenjdk:11-jre-hotspot as builder
WORKDIR application
ARG JAR_FILE=target/*.jar
COPY $&#123;JAR_FILE&#125; application.jar
ENTRYPOINT ["java", "-jar application.jar"]
</code></pre>
<pre><code>docker build --build-arg JAR_FILE=./demo-layer-0.0.1-SNAPSHOT.jar  . -t demo:v1.0
</code></pre>
<h3>查看镜像分层信息</h3>
<p>我们通过 <code>docker inspect demo:v1.0</code> 来看下此镜像的每层的散列值</p>
<pre><code>// demo:v1.0 版本镜像分层信息摘要
"Layers": [
    "sha256:b7f7d2967507ba709dbd1dd0426a5b0cdbe1ff936c131f8958c8d0f910eea19e",
    "sha256:a6ebef4a95c345c844c2bf43ffda8e36dd6e053887dd6e283ad616dcc2376be6",
    "sha256:838a37a24627f72df512926fc846dd97c93781cf145690516e23335cc0c27794",
    "sha256:28ba7458d04b8551ff45d2e17dc2abb768bf6ed1a46bb262f26a24d21d8d7233",
    "sha256:55c91231ac46fdd63c3cf84b88b11f8a04c1870482dcff033029a601bc50e1ab",
    "sha256:9816c2d488754509f6024a267738b1e5fe33a7cd33bd25c5a9cdf6d4d7bfed1d",
    "sha256:f5fb3f91797d57a92f3f7e033398b8edd094df664db849a4950eabf2f5474535",
    "sha256:b87d2ff74819f83038ea2f89736a19cfcf99bfa080b8017d191c900a09a7524f"
]
</code></pre>
<h3>helloworld 升级重新构建</h3>
<p>我们对 <code>helloworld</code> 程序进行部分修改（模拟开发过程），然后重新构建镜像</p>
<pre><code>docker build --build-arg JAR_FILE=./demo-layer-0.0.1-SNAPSHOT.jar  . -t demo:v1.1
</code></pre>
<p>此时镜像分层信息如下 <code>docker inspect demo:v1.1</code></p>
<pre><code>// demo:v1.1 版本镜像分层信息摘要
"Layers": [
    "sha256:b7f7d2967507ba709dbd1dd0426a5b0cdbe1ff936c131f8958c8d0f910eea19e",
    "sha256:a6ebef4a95c345c844c2bf43ffda8e36dd6e053887dd6e283ad616dcc2376be6",
    "sha256:838a37a24627f72df512926fc846dd97c93781cf145690516e23335cc0c27794",
    "sha256:28ba7458d04b8551ff45d2e17dc2abb768bf6ed1a46bb262f26a24d21d8d7233",
    "sha256:55c91231ac46fdd63c3cf84b88b11f8a04c1870482dcff033029a601bc50e1ab",
    "sha256:9816c2d488754509f6024a267738b1e5fe33a7cd33bd25c5a9cdf6d4d7bfed1d",
    "sha256:f5fb3f91797d57a92f3f7e033398b8edd094df664db849a4950eabf2f5474535",
    "sha256:c1b6350d545fea605e0605c4bfd7f4529cfeee3f6759750d6a5ddeb9c882fc8f"
]
</code></pre>
<h3>比较 v1.0、v1.1 镜像</h3>
<p>通过比较 v1.0 和 v1.1 版本的镜像摘要信息，我们会发现只有最后的一层发生了变化，我们通过 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fwagoodman%2Fdive" target="_blank">Dive 是一个用 Go 语言编写的 Docker 镜像分析工具</a> 来确定一下 最后一层是做了哪些事情</p>
<p><code>dive demo:v1.0</code>,<strong>大家会看到是最后的 jar 不一样 导致 16M 的内容需要重新构建，当你的业务 jar 很大时，这块就是性能瓶颈</strong></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="699" data-height="261"><img data-original-src="//upload-images.jianshu.io/upload_images/2718590-0631384c801d4840.png" data-original-width="699" data-original-height="261" data-original-format="image/jpeg" data-original-filesize="43971" src="https://upload-images.jianshu.io/upload_images/2718590-0631384c801d4840.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>spring boot 默认打包解密</h3>
<p>默认情况下，spring boot 构建出来的 jar ,解压后可以看到如下目录结构。默认会当做一个整体 ，在构建镜像时作为一个单独层，<strong>没有区分业务 classes 和 引用的第三方 jar</strong></p>
<pre><code>META-INF/
  MANIFEST.MF
org/
  springframework/
    boot/
      loader/
BOOT-INF/
  classes/
  lib/
</code></pre>
<h2>layer jar</h2>
<p>通过上文大家就可以知道分层 jar 的思想就是把，jar 再根据规则细分，业务 class 和 三方 jar 分别对应镜像的不同层，这样改动业务代码，只需变动很少的内容 提高构建速度。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="698" data-height="253"><img data-original-src="//upload-images.jianshu.io/upload_images/2718590-7089c2e47eeb763c.png" data-original-width="698" data-original-height="253" data-original-format="image/jpeg" data-original-filesize="20949" src="https://upload-images.jianshu.io/upload_images/2718590-7089c2e47eeb763c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>开启分层打包</h3>
<pre><code>  <plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
    <configuration>
      <layers>
        <enabled>true</enabled>
      </layers>
    </configuration>
  </plugin>
</code></pre>
<h3>编写支持分层 Dockerfile</h3>
<p>核心是通过 spring boot 提供的 <code>layertools</code> 工具，将 jar 进行拆分 然后通过 COPY 指令去分别加载</p>
<pre><code>FROM adoptopenjdk:11-jre-hotspot as builder
WORKDIR application
ARG JAR_FILE=target/*.jar
COPY $&#123;JAR_FILE&#125; application.jar
RUN java -Djarmode=layertools -jar application.jar extract
FROM adoptopenjdk:11-jre-hotspot
WORKDIR application
COPY --from=builder application/dependencies/ ./
COPY --from=builder application/spring-boot-loader/ ./
COPY --from=builder application/snapshot-dependencies/ ./
COPY --from=builder application/application/ ./
ENTRYPOINT ["java", "org.springframework.boot.loader.JarLauncher"]
</code></pre>
<h3>构建新镜像并查看分层信息</h3>
<pre><code>docker build --build-arg JAR_FILE=./demo-layer-0.0.1-SNAPSHOT.jar  . -t demo:v2.0
</code></pre>
<pre><code>"Layers": [
    "sha256:b7f7d2967507ba709dbd1dd0426a5b0cdbe1ff936c131f8958c8d0f910eea19e",
    "sha256:a6ebef4a95c345c844c2bf43ffda8e36dd6e053887dd6e283ad616dcc2376be6",
    "sha256:838a37a24627f72df512926fc846dd97c93781cf145690516e23335cc0c27794",
    "sha256:28ba7458d04b8551ff45d2e17dc2abb768bf6ed1a46bb262f26a24d21d8d7233",
    "sha256:55c91231ac46fdd63c3cf84b88b11f8a04c1870482dcff033029a601bc50e1ab",
    "sha256:9816c2d488754509f6024a267738b1e5fe33a7cd33bd25c5a9cdf6d4d7bfed1d",
    "sha256:f5fb3f91797d57a92f3f7e033398b8edd094df664db849a4950eabf2f5474535",
    "sha256:06fe18cf8ae7384f120f2c6a3a33b31999dd0460cf1edae45e8f13adeab35942",
    "sha256:16cf814564b8a667fcc9f07314b6084cbef8dc8c0a6565c7a2d91d74faf7e7de",
    "sha256:94be40f716016b68cdd6b99d2cb8154acf8475c3a170a898a22f95a8ef40ffd3",
    "sha256:427d87d6a5fe6da13cb4233939c3a1ff920bc6b4d2f14b5d78af7aef98fda7de"
]
</code></pre>
<p>修改代码部分业务代码，重新构建</p>
<pre><code>docker build --build-arg JAR_FILE=./demo-layer-0.0.1-SNAPSHOT.jar  . -t demo:v2.1
</code></pre>
<pre><code>"Layers": [
    "sha256:b7f7d2967507ba709dbd1dd0426a5b0cdbe1ff936c131f8958c8d0f910eea19e",
    "sha256:a6ebef4a95c345c844c2bf43ffda8e36dd6e053887dd6e283ad616dcc2376be6",
    "sha256:838a37a24627f72df512926fc846dd97c93781cf145690516e23335cc0c27794",
    "sha256:28ba7458d04b8551ff45d2e17dc2abb768bf6ed1a46bb262f26a24d21d8d7233",
    "sha256:55c91231ac46fdd63c3cf84b88b11f8a04c1870482dcff033029a601bc50e1ab",
    "sha256:9816c2d488754509f6024a267738b1e5fe33a7cd33bd25c5a9cdf6d4d7bfed1d",
    "sha256:f5fb3f91797d57a92f3f7e033398b8edd094df664db849a4950eabf2f5474535",
    "sha256:06fe18cf8ae7384f120f2c6a3a33b31999dd0460cf1edae45e8f13adeab35942",
    "sha256:16cf814564b8a667fcc9f07314b6084cbef8dc8c0a6565c7a2d91d74faf7e7de",
    "sha256:94be40f716016b68cdd6b99d2cb8154acf8475c3a170a898a22f95a8ef40ffd3",
    "sha256:8a20c60d361696a4e480fb6fbe1daf8b88bc54c579a98e209da1fb76e25de5aa"
]
</code></pre>
<h3>查看区别层镜像</h3>
<p>最后一层变动大小为 5KB</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="699" data-height="328"><img data-original-src="//upload-images.jianshu.io/upload_images/2718590-e5441fd8354582f2.png" data-original-width="699" data-original-height="328" data-original-format="image/jpeg" data-original-filesize="55730" src="https://upload-images.jianshu.io/upload_images/2718590-e5441fd8354582f2.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h2>总结</h2>
<ul>
<li>16MB -> 5KB 变动，在实际开发过程中 效果会更加明显</li>
<li>可以通过 spring boot maven plugin 指定分层逻辑，具体可以参考官方文档</li>
<li>官方文档： <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdocs.spring.io%2Fspring-boot%2Fdocs%2F2.3.0.RELEASE%2Fmaven-plugin%2Freference%2Fhtml" target="_blank">https://docs.spring.io/spring-boot/docs/2.3.0.RELEASE/maven-plugin/reference/html</a>
</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2182" data-height="324"><img data-original-src="//upload-images.jianshu.io/upload_images/2718590-c9b0cd40acbef525.png" data-original-width="2182" data-original-height="324" data-original-format="image/png" data-original-filesize="16708" src="https://upload-images.jianshu.io/upload_images/2718590-c9b0cd40acbef525.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
  
</div>
            