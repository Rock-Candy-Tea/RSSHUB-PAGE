
---
title: 'x86架构应用如何向Arm架构低成本迁移'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://static.goodrain.com/wechat/arm-compile/rainbondauth.png'
author: Dockone
comments: false
date: 2022-01-25 02:29:56
thumbnail: 'https://static.goodrain.com/wechat/arm-compile/rainbondauth.png'
---

<div>   
<br><blockquote><br>曾几何时，无论是在服务器还是个人电脑，CPU芯片领域一直是 Intel 独占鳌头，旗下的 X86_64 架构被广泛采用。然而王权没有永恒，近年来 Arm64 架构异军突起，服务器端有华为鲲鹏920高性能芯片做代表，个人电脑端则以苹果M1芯片惊艳世人。Arm64 架构芯片用低功耗和高性能炫耀着其市场价值，国产化替代的洪流也在不断将 Arm64 推向军队、政府、国企的供应商们。抓住先机，迅速拥抱与适配国产化芯片，是这个时代软件交付的新话题。</blockquote><h3>拥抱 Arm64 的难处</h3>从 <code class="prettyprint">X86_64</code> 迈向 <code class="prettyprint">Arm64</code> 并非易事，指令集的改变，影响半径极大。<br>
<br>最直接的影响，是原来在  <code class="prettyprint">X86_64</code> 环境中可以正常运行的业务系统需要基于 <code class="prettyprint">Arm64</code> 重新编译才可以运行。即使开发时使用的语言具备跨架构的能力，重新编译本身就是一种很繁复的工作，需要投入大量的人力成本和时间成本。<br>
<br><code class="prettyprint">Arm64</code> 的开发语言生态并不是那么健全，这无形中会增加了本不该开发人员关心的负担。很多语言本身的运行环境都需要重新编译，更不要提很多开源中间件的适配工作。<br>
<br>以上仅仅是开发人员关注的重点。<br>
<br>在软件交付领域，软件交付到客户环境中运行起来，仅仅是个开始。业务系统的管理、监控、迭代、容灾都是交付团队需要持续关注的点。多数交付团队在 <code class="prettyprint">X86_64</code> 架构下，都已经有了自己的解决方案。那么容器、Kubernetes、DevOps这些先进的工具方法，在 <code class="prettyprint">Arm64</code> 架构下如何复刻？<br>
<br><h3>解决之道</h3><a href="https://www.rainbond.com/?channel=dockone">Rainbond</a> 可以利用自身能力抹平芯片架构的差异，无论是开发人员，还是交付人员，都可以基于 Rainbond 找到拥抱 <code class="prettyprint">Arm64</code> 的解决之道。Rainbond 通过不同层次的能力来解决从 <code class="prettyprint">X86_64</code> 到 <code class="prettyprint">Arm64</code> 的迁移问题。<br>
<ul><li><br>既有能力：Rainbond 本身是一款适用于软件交付，或者应用运维管理的云原生应用管理平台。无论是快速交付部署，还是应用的管理、监控、迭代、容灾，既有的功能已经可以满足交付运维人员的日常需求。</li><li><br>容器化技术：Rainbond基于容器化技术实现，容器这种轻量级的虚拟化技术在 <code class="prettyprint">Arm64</code>领域已然大放异彩。自从容器支持多架构之后，绝大多数开源中间件都已经提供了基于不同架构的基础镜像，<code class="prettyprint">Arm64</code> 自然是其中的标配。选择容器化技术，相当于选择了 <code class="prettyprint">Arm64</code> 的生态支持。</li><li>自身兼容 <code class="prettyprint">Arm64</code> ：Rainbond 很早就开始落子国产化架构适配，自身适配了包含 <code class="prettyprint">Arm64</code> 在内的多种架构。</li><li>极简的开发环境部署： Rainbond 已经支持运行于各种个人平台的 Docker Desktop 环境中，开发者只需要借助一台具有 M1 芯片的 MacBook ，即可花十分钟搭建起自己的 Rainbond Arm64 开发环境，方便至极。</li><li>源码构建兼容 <code class="prettyprint">Arm64</code> ：这是打通迁移到 <code class="prettyprint">Arm64</code> 架构的最后一环。在 Rainbond 中，开发人员可以不改一行代码，直接利用源码构建自己的业务组件，即可将之部署运行于 <code class="prettyprint">Arm64</code> 环境中。目前Rainbond源码构建已经支持了市面上多种主流语言，围绕语言自身的各种扩展依赖已经趋于完整。</li></ul><br>
<br><h3>Rainbond 兼容 Arm64</h3><a href="https://www.rainbond.com/?channel=dockone">Rainbond</a> 云原生应用管理平台可以被部署在 <code class="prettyprint">Arm64</code> 环境中。从 2020 年 1 月起，Rainbond 分别和华为、飞腾进行了适配测试。经过验证，Rainbond 在 Kunpeng 920 芯片以及 FT2000+/64 这两款 <code class="prettyprint">Arm64</code> 芯片上均可以稳定运行， 达到生产可用的标准。<br>
<br><img src="https://static.goodrain.com/wechat/arm-compile/rainbondauth.png" alt referrerpolicy="no-referrer"><br>
<br>而对于个人开发领域，Rainbond 也在持续发力。目前，Rainbond 支持在各种个人 PC 平台下利用 Docker Desktop 运行。我们将 Rainbond 的所有组件集成进一个容器，这种方式可以使得个人开发者以最简化的方式，利用十分钟时间运行起个人的开发测试环境。而对于使用具有 M1 芯片的 MacBook 个人开发者而言，就已经相当于基于 <code class="prettyprint">Arm64</code> 架构进行开发了。<br>
<ul><li><br><a href="https://mp.weixin.qq.com/s/tNKNfi4RhDpyTB_GuLka7w">在Mac上运行Rainbond，10分钟快速安装</a></li><li><br><a href="https://mp.weixin.qq.com/s/OPINQRRSRcBLc4zQ-S3raw">在Windows上运行Rainbond，10分钟快速安装</a></li></ul><br>
<br><h3>Arm64中的源码编译</h3><a href="https://www.rainbond.com/?channel=dockone">Rainbond</a> 具备的源码编译能力由来已久。该功能脱胎自 Heroku/buildpack 项目，并由 Rainbond 团队针对自身需求做了大量优化。借助其能力，使用者可以基于多种语言的源代码，跳过编写 Dockerfile 的过程，完成业务的容器化。源码编译是部署企业自行开发业务的最简单方式，仅需要提供源代码的仓库地址。<br>
<br>目前 <code class="prettyprint">Arm64</code> 源码编译支持的语言及版本如下：<br>
<pre class="prettyprint">|              语言支持              | 版本支持                                                     |                           扩展支持                           |<br>
| :--------------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------: |<br>
|    Java： Maven/Jar/War/Gradle     | openjdk 8 / 9 / 10 / 11 / 12 / 13                            |               pinpoint agent<br/> jmx-exporter               |<br>
|              Node.js               | Node 4.9.1 / 5.12.0 / 6.14.4 / 7.10.1 / 8.9.3 / 8.12.0 / 9.11.2 / 10.13.0 / 11.1.0 |                          Yarn 1.9.4                          |<br>
| Node.js 前端项目<br/>（VUE React） | Node 4.9.1 / 5.12.0 / 6.14.4 / 7.10.1 / 8.9.3 / 8.12.0 / 9.11.2 / 10.13.0 / 11.1.0 |                  Yarn 1.9.4<br>Nginx 1.18.0                  |<br>
|               Golang               | Go 1.8 / 1.9 / 1.10 / 1.11 / 1.12 / 1.13 / 1.14 / 1.15 / 1.16 |                                                              |<br>
|               Python               | Python 2.7.9 / 2.7.17 / 3.4.9 / 3.5.7 / 3.6.6 / 3.6.10       |                                                              |<br>
|                PHP                 | PHP 5.5.38 / 5.6.32～37 / 7.0.29 / 7.1.27 / 7.2.16 / 7.3.3   | apcu / ev / event / imgick <br/>memcached / mongodb <br/>oauth / phalcon <br/> pq / raphf / redis |<br>
|                Html                | Nginx 1.18.0 / Apache Httpd 2.2.19                           |                                                              |<br>
</pre><br>
<br>在源码构建功能适配 <code class="prettyprint">Arm64</code> 之后，使用者不需要自己对业务进行容器化，仅需要提供源码即可。这种体验，可以被称之为将业务零成本迁移至 <code class="prettyprint">Arm64</code> 容器之中。极大的减轻了开发人员的技术负担，降低了迁移适配成本。而这一过程中，代码运行环境的处理、扩展依赖的处理都已经由 Rainbond Arm64 源码构建能力处理完成。<br>
<br>源码构建的原理并不复杂：<br>
<ul><li>基于 <a href="https://github.com/goodrain/builder">Builder</a> 提供一个统一的构建环境，根据业务源代码的特征，选择对应语言的 buildpack 脚本。</li><li>根据 buildpack 脚本的不同，以及用户在 Rainbond 控制台中指定的版本，会从第三方对象存储（Rainbond AliyunOSS）下载对应的语言运行环境预编译包（如 Openjdk）准备基础编译环境。</li><li>执行预编译过程，根据用户在 Rainbond 控制台中定义的编译特性（如依赖仓库地址等）进行编译环境的配置。</li><li>根据用户在 Rainbond 控制台指定的编译命令，或各语言的默认值，开始进行编译工作。期间会根据语言特征执行特定的操作，比如执行勾子函数、下载指定的扩展（PHP 扩展）等。</li><li>将构建完成的产物统一打包，打包的格式，是 Heroku 风格的 Slug 包。</li><li>基于 <a href="https://github.com/goodrain/runner">Runner</a> 作为基础镜像，联合 Slug 包打包成为业务容器镜像，运行时自动解压 Slug 包，根据用户指定的启动命令，完成最终的运行。</li></ul><br>
<br>整个构建过程拥有实时推送的日志，对于开发人员而言，和在自己的开发环境中编译操作没有太多差别。而编译过程中，需要提供 <code class="prettyprint">Arm64</code> 支持的包括：语言运行环境预编译包、扩展、Nginx/Httpd 等中间价都已经由官方完成适配，免去了开发人员的辛劳，少掉了不少头发。<br>
<br>新安装的 Rainbond 平台，在首次进行源码构建时，会拉取 builder  和 runner 镜像，这个过程会花费几分钟时间。已经在 <code class="prettyprint">Arm64</code> 环境中安装过 Rainbond 的用户，可以执行以下命令，拉取最新的镜像，来获取 <code class="prettyprint">Arm64</code> 源码编译能力。<br>
<br>以 MacBook M1 电脑上安装的 Rainbond 为例，进入 rainbond-allinone 容器中操作：<br>
<pre class="prettyprint">docker exec -ti rainbond-allinone bash<br>
</pre><br>
<br>获取内置镜像仓库的登录密码，登录镜像仓库：<br>
<pre class="prettyprint">hubpassword=$(kubectl get rainbondcluster -o yaml -n rbd-system | grep password | awk '&#123;print $2&#125;')<br>
docker login --username=admin --password=$&#123;hubpassword&#125; goodrain.me<br>
</pre><br>
<br>处理镜像：<br>
<pre class="prettyprint">images=(builder runner)<br>
for image in $&#123;images[@]&#125;<br>
do<br>
docker pull registry.cn-hangzhou.aliyuncs.com/goodrain/$&#123;image&#125;:v5.5.0-release<br>
docker tag registry.cn-hangzhou.aliyuncs.com/goodrain/$&#123;image&#125;:v5.5.0-release goodrain.me/$&#123;image&#125;<br>
docker push goodrain.me/$&#123;image&#125;<br>
done<br>
</pre><br>
<br>Rainbond 提供了示例代码，可供源码构建测试之用。<br>
<br><img src="https://static.goodrain.com/wechat/arm-compile/bilde-demo.png" alt referrerpolicy="no-referrer"><br>
<br>开始构建后，会自动弹出实时推送的构建日志，供开发人员了解构建进度。<br>
<br><img src="https://static.goodrain.com/wechat/arm-compile/build-1.png" alt referrerpolicy="no-referrer"><br>
<br>当前日志中依次提供以下信息：<br>
<ul><li>代码仓库地址</li><li>代码最新提交信息</li><li>首次源码构建拉取 builder 镜像（该过程仅在首次构建中拉取）</li><li>识别构建环境 CPU 架构，当前为 linux-arm64</li><li>识别语言及构建方式，当前为 Java-maven</li><li>语言运行环境版本，当前会下载 Arm64 环境可用的 openjdk1.8</li><li>安装 Java 语言的能力扩展，包括 Pinpoint APM agent 和 jmx-exporter </li><li>安装 Maven 构建环境，当前版本 3.3.9</li><li>执行构建命令。</li></ul><br>
<br>接下来的输出，和标准的 Java-maven 构建输出无二，是下载 pom 及依赖的过程。在构建完成后，输出日志：<br>
<br><img src="https://static.goodrain.com/wechat/arm-compile/build-2.png" alt referrerpolicy="no-referrer"><br>
<br>代码编译过程到此完成，接下来，runner 会利用编译打包后的 slug 文件继续构建镜像，并完成向内置镜像仓库的推送：<br>
<br><img src="https://static.goodrain.com/wechat/arm-compile/build-3.png" alt referrerpolicy="no-referrer"><br>
<br>首次构建，会拉取 runner 镜像，这个行为只会进行一次。<br>
<br><img src="https://static.goodrain.com/wechat/arm-compile/build-4.png" alt referrerpolicy="no-referrer"><br>
<br>至此，源代码就已经变成了可以运行的容器镜像，该镜像可以在 <code class="prettyprint">Arm64</code> 环境中运行。<br>
<br><h3>持续交付</h3>当开发者成功将自己的业务系统部署在 Rainbond Arm64 环境中后，Rainbond 已有的交付流程，就可以最大化的降低向 <code class="prettyprint">Arm64</code> 环境交付的难度。通过将业务系统整体发布为应用模版，就得到了可以向最终生产环境交付的标准交付物。无论是导出为离线包，还是基于线上 RainStore 交付，都可以很方便的实现。后续的流程可以参考以往的文章或参考官方文档。<br>
<br><a href="https://mp.weixin.qq.com/s/7_i-UbVBxcAEoGaxuuET3w">使用Rainbond实现离线环境软件交付</a> 
                                
                                                              
</div>
            