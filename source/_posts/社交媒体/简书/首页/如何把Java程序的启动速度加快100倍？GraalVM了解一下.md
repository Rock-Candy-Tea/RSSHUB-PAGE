
---
title: '如何把Java程序的启动速度加快100倍？GraalVM了解一下'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://picsum.photos/400/300?random=9126'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=9126'
---

<div>   
<p>在云原生时代，Java程序是有很大的劣势的，为什么这么说呢？你看Java的一个最简单的hello world都要大几十M的内存，启动也不不快。以最流行的spring boot/spring cloud微服务框架为例，启动一个已经优化好，很多bean需要lazy load的application至少需要3-4秒时间，内存需要几百M，业务逻辑稍微复杂一点点，没有1G以上的内存是很难满足业务的需要呢？</p>
<p>那么在云原生时代，Java会落后吗？答案到现在，笔者也不好说，不过大概率不会，为什么呢？因为java社区没有闲着，弄出来很多好玩的黑科技。下面我就一个充满黑科技的JVM介绍给大家，用他能帮助我们让Java程序的启动速度加快100倍，内存只需要原来的五分之一，甚至更少。</p>
<p>还等什么，让我们开始吧。</p>
<h2>一、Graalvm的介绍</h2>
<p>Graal VM是2018年Oracle开发的下一代JVM实现，被官方称为“Universal VM”和“Polyglot VM”，这是一个在HotSpot虚拟机基础上增强而成的跨语言全栈虚拟机，可以作为“任何语言”的运行平台使用，这里“任何语言”包括了Java、Scala、Groovy、Kotlin等基于Java虚拟机之上的语言，还包括了C、C++、Rust等基于LLVM的语言，同时支持其他像JavaScript、Ruby、Python和R语言等等。Graal VM可以无额外开销地混合使用这些编程语言，支持不同语言中混用对方的接口和对象，也能够支持这些语言使用已经编写好的本地库文件。</p>
<p>主要特性包括：</p>
<ul>
<li>高性能的现代Java</li>
<li>占用资源少，启动速度快</li>
<li>JavaScript, Java, Ruby以及R混合编程</li>
<li>在JVM上运行原生语言</li>
<li>跨语言工具</li>
<li>JVM应用扩展</li>
<li>原生应用扩展</li>
<li>本地Java库</li>
<li>数据库支持多语言</li>
<li>创建自己的语言</li>
</ul>
<h2>二、Graalvm安装及环境配置</h2>
<p>GraalVM包括社区版和企业版，我们以社区版为例，截取当前2020年6月份，最新的Release版本为：Graalvm Community 20.1.0，下载地址：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.graalvm.org%2Fdownloads%2F" target="_blank">https://www.graalvm.org/downloads/</a><br>
不过社区版需要会让你跳转到github进行下载，github下载很慢，需要科学翻墙才行。</p>
<h3>2.1 在Windows 10平台上安装</h3>
<p>请按照以下步骤在x86 64位Windows上安装GraalVM Community Edition。</p>
<ol>
<li><p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fgraalvm%2Fgraalvm-ce-builds%2Freleases" target="_blank">GitHub上</a>的<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fgraalvm%2Fgraalvm-ce-builds%2Freleases" target="_blank">GraalVM Releases存储库</a>。根据电脑配置，选择<strong>graalvm-ce-java8-windows-amd64-20.1.0.zip</strong>或<strong>graalvm-ce-java11-windows-amd64-20.1.0.zip</strong>并下载。</p></li>
<li><p>将文件压缩到文件系统，比如 d盘根目录。</p></li>
<li>
<p>配置<code>JAVA_HOME</code>和<code>PATH</code>环境变量。在Windows 7、8和10中，通过命令行设置环境变量的工作方式相同。</p>
<ul>
<li>
<p>将GraalVM <strong>bin</strong>文件夹添加到<code>PATH</code>环境变量：</p>
<pre><code>setx /M PATH "d:\graalvm-ce-java8-20.1.0\bin;%PATH%"

</code></pre>
</li>
<li>
<p>设置<code>JAVA_HOME</code>环境变量以解析到GraalVM安装目录：</p>
<pre><code>setx /M JAVA_HOME "d:\graalvm-ce-java8-20.1.0"

</code></pre>
<p>请注意<code>/M</code>，等同于的标志<code>-m</code>需要管理员权限的命令行。</p>
</li>
</ul>
</li>
<li>
<p>重新启动命令提示符以重新加载环境变量。然后使用以下命令检查变量设置是否正确：</p>
<pre><code>echo %PATH%
echo %JAVA_HOME%

</code></pre>
</li>
</ol>
<pre><code>    java -version
   openjdk version "1.8.0_252"
   OpenJDK Runtime Environment (build 1.8.0_252-b09)
   OpenJDK 64-Bit Server VM GraalVM CE 20.1.0 (build 25.252-b09-jvmci-20.1-b02, mixed mode)
</code></pre>
<h3>2.2 使用gu工具安装 native image</h3>
<p>要在GraalVM Community Edition中添加对Python，R，Ruby或WebAssembly语言解释器的支持，请使用功能[<code>gu</code>实用程序]GitHub上有一个由Oracle（<code>gu available</code>）维护的组件目录，您可以从中按名称安装组件：</p>
<pre><code>gu install ruby
gu install r
gu install python
gu install wasm

</code></pre>
<p>要安装<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.graalvm.org%2Fdocs%2Freference-manual%2Flanguages%2Fllvm%2F%23llvm-toolchain" target="_blank">LLVM工具链</a>组件，请运行：</p>
<pre><code>gu install llvm-toolchain

</code></pre>
<p>要安装<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.graalvm.org%2Fdocs%2Freference-manual%2Fnative-image%2F" target="_blank">GraalVM本机映像</a>，请运行：</p>
<pre><code>gu install native-image

</code></pre>
<h4>在Windows上使用native images的先决条件</h4>
<p>要在Windows上使用本机映像，请遵循其他建议。所需的Microsoft Visual C ++（MSVC）版本取决于GraalVM所基于的JDK版本。对于基于JDK 8的GraalVM分发，您将需要MSVC 2010 SP1版本。推荐的安装方法是使用Microsoft Windows SDK 7.1：</p>
<ol>
<li>
<code>GRMSDKX_EN_DVD.iso</code>从<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.microsoft.com%2Fen-gb%2Fdownload" target="_blank">Microsoft</a>下载SDK文件。</li>
<li>通过<code>F:\Setup\SDKSetup.exe</code>直接打开安装图像。</li>
</ol>
<p>对于基于JDK 11的GraalVM分发，您将需要MSVC 2017 15.5.5或更高版本。</p>
<p>对于基于JDK 11和JDK 8的GraalVM发行版，共同的最后一个先决条件是适用于您的<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fvisualstudio.microsoft.com%2Fvs%2F" target="_blank">Visual Studio</a>版本的正确的<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fcpp%2Fbuild%2Fbuilding-on-the-command-line%3Fview%3Dvs-2019%23developer_command_prompt_shortcuts" target="_blank">Developer Command Prompt</a>。即，它应该是x64本机工具命令提示符。使用Visual Studio 2017或更高版本。</p>
<h2>三、spring boot之Graalvm</h2>
<p>其实在2019年spring 团队已经开始作手支持graalvm的native image功能。就在前几天（2020-6-10）<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fspring.io%2Fblog%2F2020%2F06%2F10%2Fthe-path-towards-spring-boot-native-applications" target="_blank">spring-graalvm-native 发布了0.7.0版本</a>。Spring团队承诺对Graal VM的支持必须在2020年10月之后才会正式提供，但现在的我们其实已经可以使用Graal VM来（实验性地）运行Spring、Spring Boot、Spring Data、Netty、JPA等等的一系列组件（不过SpringCloud中的组件暂时还不行）。<br>
接下来，我们将尝试使用Graal VM来编译一个标准的Spring Boot应用。</p>
<h3>3.1 准备工作</h3>
<p>首先，我们先假设你准备编译的代码是“符合要求”的，即没有使用到Graal VM不支持的特性，譬如前面提到的Finalizer、CGLIB、InvokeDynamic这类功能。然后，由于我们用的是Graal VM的Java 8版本，也必须假设你编译使用Java语言级别在Java 8以内。<br>
spring-graalvm-native的0.7版本基于刚刚发布的Spring Boot 2.3和上面提到的Graalvm 20.1.0 版本。请将你的pom.xml中的Spring Boot版本修改如下（假设你编译用的是Maven，用Gradle的请自行调整）：</p>
<pre><code><parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.3.0</version>
    <relativePath/>
</parent> 
</code></pre>
<p>同时在pom.xml中增加spring对graalvm的支持(别忘了现在也添加Spring Milestones存储库，因为现在还没有通过Maven Central发行）。)：</p>
<pre><code><dependencies>
        <dependency>
            <groupId>org.springframework.experimental</groupId>
            <artifactId>spring-graalvm-native</artifactId>
            <version>0.7.0</version>
        </dependency>
        ...
        <dependencies>
    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
        </repository>
    </repositories>
    <pluginRepositories>
        <pluginRepository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
        </pluginRepository>
    </pluginRepositories>
</code></pre>
<p>由于GraalVM不支持GCLIB代理，因此Spring Boot需要<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Foracle%2Fgraal%2Fblob%2Fmaster%2Fsubstratevm%2FDYNAMIC_PROXY.md" target="_blank">使用JDK代理</a>。因此，请使用<code>proxyBeanMethods = false</code>@SpringBootApplication类的属性：</p>
<pre><code>@SpringBootApplication(proxyBeanMethods = false)
public class SpringBootHelloApplication &#123;
    ...
&#125;
</code></pre>
<p>3.2 开始native image成本地原生程序</p>
<p>现在，我们几乎已经准备好一切，最终可以运行<code>native-image</code>命令。这是一个示例，该示例基于提到的<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fjonashackt%2Fspring-boot-graalvm" target="_blank">实现Reactive Spring Boot Web应用程序的示例项目</a>。把java程序编译成本地程序，是一个很难一次性成功的事情，它取决于要编译为GraalVM本机映像的Spring Boot应用程序的类型！因此，最好的方法是从<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-graalvm-native%2Ftree%2Fmaster%2Fspring-graalvm-native-samples" target="_blank">spring-graal-native项目的示例项目中</a>获得一些参考和提示。</p>
<p>开始吧：</p>
<ol>
<li>先maven编译，这部很简单，我们都很熟悉</li>
</ol>
<pre><code>mvn clean package
</code></pre>
<ol start="2">
<li>运行native image命令进行本地原生编译</li>
</ol>
<pre><code>native-image \
  -H:+TraceClassInitialization \
  -H:Name=spring-boot-graal
  -H:+ReportExceptionStackTraces \
  -Dspring.graal.remove-unused-autoconfig=true \
  -Dspring.graal.remove-yaml-support=true \
  -cp target/spring-boot-graal.jar
</code></pre>
<p>这个过程可能有点长，建议你起来喝杯水或者喝杯咖啡！这需要一些时间，具体取决于您的硬件！示例项目大约需要3-4分钟。如果一切顺利，您将在中找到本地编译的Spring Boot应用程序<code>/target/spring-boot-graal</code>。只需使用以下命令运行它：</p>
<pre><code>./target/spring-boot-graal
</code></pre>
<p>=============================</p>
  
</div>
            