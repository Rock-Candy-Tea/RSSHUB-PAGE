
---
title: '无需 Dockerfile 的镜像构建：BuildPack vs Dockerfile'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211108/ec8db608fad32be84a4e83d774c37942.png'
author: Dockone
comments: false
date: 2021-11-10 15:08:08
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211108/ec8db608fad32be84a4e83d774c37942.png'
---

<div>   
<br>过去的工作中，我们使用微服务、容器化以及服务编排构建了技术平台。为了提升开发团队的研发效率，我们同时还提供了 CI/CD 平台，用来将代码快速的部署到 OpenShift（企业级的 Kubernetes） 集群。  <br>
<br>部署的第一步就是应用程序的容器化，持续集成的交付物从以往的 jar 包、webpack 等变成了容器镜像。容器化将软件代码和所需的所有组件（库、框架、运行环境）打包到一起，进而可以在任何环境任何基础架构上一致地运行，并与其他应用“隔离”。<br>
<br>我们的代码需要从源码到编译到最终可运行的镜像，甚至部署，这一切在 CI/CD 的流水线中完成。最初，我们在每个代码仓库中都加入了三个文件，也通过项目生成器（类似 Spring Initializer）在新项目中注入：<br>
<ul><li>Jenkinsfile.groovy：用来定义 Jenkins 的 Pipeline，针对不同的语言还会有多种版本</li><li>Manifest YAML：用于定义 Kubernetes 资源，也就是工作负载及其运行的相关描述</li><li>Dockerfile：用于构建对象</li></ul><br>
<br>这个三个文件也需要在工作中不断的演进，起初项目较少（十几个）的时候我们基础团队还可以去各个代码仓库去维护升级。随着项目爆发式的增长，维护的成本越来越高。我们对 CICD 平台进行了迭代，将“Jenkinsfile.groovy”和 “manifest YAML”从项目中移出，变更较少的 Dockerfile 就保留了下来。<br>
<br>随着平台的演进，我们需要考虑将这唯一的“钉子户” Dockerfile 与代码解耦，必要的时候也需要对 Dockerfile 进行升级。因此调研了一下 buildpacks，就有了今天的这篇文章。<br>
<h3>什么是 Dockerfile</h3>Docker 通过读取 Dockerfile 中的说明自动构建镜像。Dockerfile 是一个文本文件，包含了由 Docker 可以执行用于构建镜像的指令。我们拿之前用于<a href="https://github.com/addozhang/tekton-test">测试 Tekton 的 Java 项目</a>的 Dockerfile 为例：<br>
<pre class="prettyprint">FROM openjdk:8-jdk-alpine<br>
RUN mkdir /app<br>
WORKDIR /app<br>
COPY target/*.jar /app/app.jar<br>
ENTRYPOINT ["sh", "-c", "java -Xmx128m -Xms64m -jar app.jar"] <br>
</pre><br>
<h4>镜像分层</h4>你可能会听过 Docker 镜像包含了多个层。每个层与 Dockerfile 中的每个命令对应，比如 <code class="prettyprint">RUN</code>、<code class="prettyprint">COPY</code>、<code class="prettyprint">ADD</code>。某些特定的指令会创建一个新的层，在镜像构建过程中，假如某些层没有发生变化，就会从缓存中获取。<br>
<br>在下面的 Buildpack 中也同样通过镜像分层和 cache 来加速镜像的构建。<br>
<h3>什么是 Buildpack</h3><a href="https://buildpacks.io/">BuildPack</a> 是一个程序，它能将源代码转换成容器镜像的并可以在任意云环境中运行。通常 buildpack 封装了单一语言的生态工具链。适用于 Java、Ruby、Go、NodeJs、Python 等。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211108/ec8db608fad32be84a4e83d774c37942.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211108/ec8db608fad32be84a4e83d774c37942.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>buildpacks.io</em><br>
<h4>Builder 是什么？</h4>一些 buildpacks 按顺序组合之后就是 <strong>builder</strong>，除了 buildpacks， builder 中还加入了<a href="https://buildpacks.io/docs/concepts/components/lifecycle/">生命周期</a> 和 stack 容器镜像。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211108/5e327f8c2b64e93e1641edb67bfa3491.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211108/5e327f8c2b64e93e1641edb67bfa3491.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
stack 容器镜像由两个镜像组成：用于运行 buildpack 的镜像 build image，以及构建应用镜像的基础镜像 run image。如上图，就是 builder 中的运行环境。<br>
<h4>Buildpack 的工作方式</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211108/29eeb83c80f0aeb3ab51d3120f4bb838.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211108/29eeb83c80f0aeb3ab51d3120f4bb838.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>how buildpack works</em><br>
<br>每个 buildpack 运行时都包含了两个阶段：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211108/9f6061748340d5b89e39b6687aa3632c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211108/9f6061748340d5b89e39b6687aa3632c.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>phases</em><br>
<br><strong>检测阶段</strong><br>
<br>通过检查源代码中的某些特定文件/数据，来判断当前 buildpack 是否适用。如果适用，就会进入构建阶段；否则就会退出。比如：<br>
<ul><li>Java maven 的 buildpack 会检查源码中是否有 <code class="prettyprint">pom.xml</code></li><li>Python 的 buildpack 会检查源码中是否有 <code class="prettyprint">requirements.txt</code> 或者 <code class="prettyprint">setup.py</code> 文件</li><li>Node buildpack 会查找 <code class="prettyprint">package-lock.json</code> 文件。</li></ul><br>
<br><strong>构建阶段</strong><br>
<br>在构建阶段会进行如下操作：<br>
<ol><li>设置构建环境和运行时环境</li><li>下载依赖并编译源码（假如需要的话）</li><li>设置正确的 entrypoint 和启动脚本。</li></ol><br>
<br>比如：<br>
<ul><li>Java maven buildpack 在检查到有 <code class="prettyprint">pom.xml</code> 文件之后，会执行 <code class="prettyprint">mvn clean install -DskipTests</code></li><li>Python buildpack 检查到有 <code class="prettyprint">requrements.txt</code> 之后，会执行 <code class="prettyprint">pip install -r requrements.txt</code></li><li>Node build pack 检查到有 <code class="prettyprint">package-lock.json</code> 后执行 <code class="prettyprint">npm install</code></li></ul><br>
<br><h3>BuildPack 上手</h3>那到底如何在没有 Dockerfile 的情况下使用 builderpack 构建镜像的。看了上面这些，大家基本上也都能了解到这个核心就在 buildpack 的编写和使用的。<br>
<br>其实现在有很多开源的 buildpack 可以用，没有特定定制的情况下无需自己手动编写。比如下面的几个大厂开源并维护的 Buildpacks：<br>
<ul><li>Heroku Buildpacks：<a href="https://github.com/heroku/" rel="nofollow" target="_blank">https://github.com/heroku/</a></li><li>Google Buildpacks：<a href="https://github.com/GoogleCloudPlatform/buildpacks" rel="nofollow" target="_blank">https://github.com/GoogleCloudPlatform/buildpacks</a></li><li>Paketo：<a href="https://github.com/paketo-buildpacks" rel="nofollow" target="_blank">https://github.com/paketo-buildpacks</a></li></ul><br>
<br>但是正式详细介绍开源的 buildpacks 之前，我们还是通过自己创建 buildpack 的方式来深入了解 Buildpacks 的工作方式。测试项目呢，我们还是用<a href="https://github.com/addozhang/tekton-test">测试 Tekton 的 Java 项目</a>。<br>
<br>下面所有的内容都提交到了 GitHub 上，可以访问：<a href="https://github.com/addozhang/buildpacks-sample" rel="nofollow" target="_blank">https://github.com/addozhang/buildpacks-sample</a> 获取相关代码。<br>
<br>最终的目录 <code class="prettyprint">buildpacks-sample</code> 结构如下：<br>
<pre class="prettyprint">├── builders<br>
│   └── builder.toml<br>
├── buildpacks<br>
│   └── buildpack-maven<br>
│       ├── bin<br>
│       │   ├── build<br>
│       │   └── detect<br>
│       └── buildpack.toml<br>
└── stacks<br>
├── build<br>
│   └── Dockerfile<br>
├── build.sh<br>
└── run<br>
    └── Dockerfile<br>
</pre><br>
<h4>创建 buildpack</h4><pre class="prettyprint">pack buildpack new examples/maven \<br>
                     --api 0.5 \<br>
                     --path buildpack-maven \<br>
                     --version 0.0.1 \<br>
                     --stacks io.buildpacks.samples.stacks.bionic<br>
</pre><br>
看下生成的 <code class="prettyprint">buildpack-maven</code> 目录：<br>
<pre class="prettyprint">buildpack-maven<br>
├── bin<br>
│   ├── build<br>
│   └── detect<br>
└── buildpack.toml<br>
</pre><br>
各个文件中都是默认的初试数据，并没有什么用处。需要添加些内容：<br>
<br><code class="prettyprint">bin/detect</code>：<br>
<pre class="prettyprint">#!/usr/bin/env bash<br>
if [[ ! -f pom.xml ]]; then<br>
exit 100<br>
fi<br>
plan_path=$2<br>
cat >> "$&#123;plan_path&#125;" <<EOL<br>
[[provides]]<br>
name = "jdk"<br>
[[requires]]<br>
name = "jdk"<br>
EOL<br>
</pre><br>
<br><code class="prettyprint">bin/build</code>：<br>
<pre class="prettyprint">#!/usr/bin/env bash<br>
set -euo pipefail<br>
layers_dir="$1"<br>
env_dir="$2/env"<br>
plan_path="$3"<br>
m2_layer_dir="$&#123;layers_dir&#125;/maven_m2"<br>
if [[ ! -d $&#123;m2_layer_dir&#125; ]]; then<br>
mkdir -p $&#123;m2_layer_dir&#125;<br>
echo "cache = true" > $&#123;m2_layer_dir&#125;.toml<br>
fi<br>
ln -s $&#123;m2_layer_dir&#125; $HOME/.m2<br>
echo "---> Running Maven"<br>
mvn clean install -B -DskipTests<br>
target_dir="target"<br>
for jar_file in $(find "$target_dir" -maxdepth 1 -name "*.jar" -type f); do<br>
cat >> "$&#123;layers_dir&#125;/launch.toml" <<EOL<br>
[[processes]]<br>
type = "web"<br>
command = "java -jar $&#123;jar_file&#125;"<br>
EOL<br>
break;<br>
done<br>
</pre><br>
<br><code class="prettyprint">buildpack.toml</code>：<br>
<pre class="prettyprint">api = "0.5"<br>
[buildpack]<br>
id = "examples/maven"<br>
version = "0.0.1"<br>
[[stacks]]<br>
id = "com.atbug.buildpacks.example.stacks.maven"<br>
</pre><br>
<h4>创建 stack</h4>构建 Maven 项目，首选需要 Java 和 Maven 的环境，我们使用 <code class="prettyprint">maven:3.5.4-jdk-8-slim</code> 作为 build image 的 base 镜像。应用的运行时需要 Java 环境即可，因此使用 <code class="prettyprint">openjdk:8-jdk-slim</code>作为 run image 的 base 镜像。<br>
<br>在 <code class="prettyprint">stacks</code> 目录中分别创建 <code class="prettyprint">build</code> 和 <code class="prettyprint">run</code> 两个目录：<br>
<br><strong><code class="prettyprint">build/Dockerfile</code></strong><br>
<pre class="prettyprint">FROM maven:3.5.4-jdk-8-slim<br>
ARG cnb_uid=1000<br>
ARG cnb_gid=1000<br>
ARG stack_id<br>
ENV CNB_STACK_ID=$&#123;stack_id&#125;<br>
LABEL io.buildpacks.stack.id=$&#123;stack_id&#125;<br>
ENV CNB_USER_ID=$&#123;cnb_uid&#125;<br>
ENV CNB_GROUP_ID=$&#123;cnb_gid&#125;<br>
# Install packages that we want to make available at both build and run time<br>
RUN apt-get update && \<br>
apt-get install -y xz-utils ca-certificates && \<br>
rm -rf /var/lib/apt/lists/*<br>
# Create user and group<br>
RUN groupadd cnb --gid $&#123;cnb_gid&#125; && \<br>
useradd --uid $&#123;cnb_uid&#125; --gid $&#123;cnb_gid&#125; -m -s /bin/bash cnb<br>
USER $&#123;CNB_USER_ID&#125;:$&#123;CNB_GROUP_ID<br>
</pre>&#125;<br>
<br><strong><code class="prettyprint">run/Dockerfile</code></strong><br>
<pre class="prettyprint">FROM openjdk:8-jdk-slim<br>
ARG stack_id<br>
ARG cnb_uid=1000<br>
ARG cnb_gid=1000<br>
LABEL io.buildpacks.stack.id="$&#123;stack_id&#125;"<br>
USER $&#123;cnb_uid&#125;:$&#123;cnb_gid&#125; <br>
</pre><br>
然后使用如下命令构建出两个镜像：<br>
<pre class="prettyprint">export STACK_ID=com.atbug.buildpacks.example.stacks.maven<br>
docker build --build-arg stack_id=$&#123;STACK_ID&#125; -t addozhang/samples-buildpacks-stack-build:latest ./build<br>
docker build --build-arg stack_id=$&#123;STACK_ID&#125; -t addozhang/samples-buildpacks-stack-run:latest ./run<br>
</pre><br>
<h4>创建 Builder</h4>有了 buildpack 和 stack 之后就是创建 Builder 了，首先创建 <code class="prettyprint">builder.toml</code> 文件，并添加如下内容：<br>
<pre class="prettyprint">[[buildpacks]]<br>
id = "examples/maven"<br>
version = "0.0.1"<br>
uri = "../buildpacks/buildpack-maven"<br>
[[order]]<br>
[[order.group]]<br>
id = "examples/maven"<br>
version = "0.0.1"<br>
[stack]<br>
id = "com.atbug.buildpacks.example.stacks.maven"<br>
run-image = "addozhang/samples-buildpacks-stack-run:latest"<br>
build-image = "addozhang/samples-buildpacks-stack-build:latest"<br>
</pre><br>
然后执行命令，注意这里我们使用了 <code class="prettyprint">--pull-policy if-not-present</code> 参数，就不需要将 stack 的两个镜像推送到镜像仓库了：<br>
<pre class="prettyprint">pack builder create example-builder:latest --config ./builder.toml --pull-policy if-not-present<br>
</pre><br>
<h4>测试</h4>有了 builder 之后，我们就可以使用创建好的 builder 来构建镜像了。<br>
<br>这里同样加上了 <code class="prettyprint">--pull-policy if-not-present</code> 参数来使用本地的 builder 镜像：<br>
<pre class="prettyprint"># 目录 buildpacks-sample  与 tekton-test 同级，并在 buildpacks-sample  中执行如下命令<br>
pack build addozhang/tekton-test --builder example-builder:latest --pull-policy if-not-present --path ../tekton-test<br>
</pre><br>
如果看到类似如下内容，就说明镜像构建成功了（第一次构建镜像由于需要下载 maven 依赖耗时可能会比较久，后续就会很快，可以执行两次验证下）：<br>
<pre class="prettyprint">...<br>
===> EXPORTING<br>
[exporter] Adding 1/1 app layer(s)<br>
[exporter] Reusing layer 'launcher'<br>
[exporter] Reusing layer 'config'<br>
[exporter] Reusing layer 'process-types'<br>
[exporter] Adding label 'io.buildpacks.lifecycle.metadata'<br>
[exporter] Adding label 'io.buildpacks.build.metadata'<br>
[exporter] Adding label 'io.buildpacks.project.metadata'<br>
[exporter] Setting default process type 'web'<br>
[exporter] Saving addozhang/tekton-test...<br>
[exporter] *** Images (0d5ac1158bc0):<br>
[exporter]       addozhang/tekton-test<br>
[exporter] Adding cache layer 'examples/maven:maven_m2'<br>
Successfully built image addozhang/tekton-test<br>
</pre><br>
启动容器，会看到 spring boot 应用正常启动：<br>
<pre class="prettyprint">docker run --rm addozhang/tekton-test:latest<br>
.   ____          _            __ _ _<br>
/\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \<br>
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \<br>
\\/  ___)| |_)| | | | | || (_| |  ) ) ) )<br>
'  |____| .__|_| |_|_| |_\__, | / / / /<br>
=========|_|==============|___/=/_/_/_/<br>
:: Spring Boot ::        (v2.2.3.RELEASE)<br>
...<br>
</pre><br>
<h3>总结</h3>其实现在有很多开源的 buildpack 可以用，没有特定定制的情况下无需自己手动编写。比如下面的几个大厂开源并维护的 Buildpacks：<br>
<ul><li>Heroku Buildpacks：<a href="https://github.com/heroku/" rel="nofollow" target="_blank">https://github.com/heroku/</a></li><li>Google Buildpacks：<a href="https://github.com/GoogleCloudPlatform/buildpacks" rel="nofollow" target="_blank">https://github.com/GoogleCloudPlatform/buildpacks</a></li><li>Paketo：<a href="https://github.com/paketo-buildpacks" rel="nofollow" target="_blank">https://github.com/paketo-buildpacks</a></li></ul><br>
<br>上面几个 buildpacks 库内容比较全面，实现上会有些许不同。比如 Heroku 的执行阶段使用 Shell 脚本，而 Paketo 使用 Golang。后者的扩展性较强，由 Cloud Foundry 基金会支持，并拥有由 VMware 赞助的全职核心开发团队。这些小型模块化的 buildpack，可以通过组合扩展使用不同的场景。<br>
<br>当然还是那句话，自己上手写一个会更容易理解 Buildpack 的工作方式。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/MkKbtPn5a0IwIK4nVCOoAw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/MkKbtPn5a0IwIK4nVCOoAw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            