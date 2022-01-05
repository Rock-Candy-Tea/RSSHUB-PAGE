
---
title: 'Spring Native初探'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/5127a93400dc7586c628da76f6c36662.png'
author: Dockone
comments: false
date: 2022-01-05 10:08:48
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/5127a93400dc7586c628da76f6c36662.png'
---

<div>   
<br>近几年“原生”一词一直泛滥在云计算、边缘计算等领域中，而原生宠幸的语言也一直都是Golang，Rust等脱离Sandbox运行的开发语言。Java得益于上世纪流行的一次编译，到处执行的理念，流行至今，但也因为这个原因，导致Java程序脱离不了JVM运行环境，使得不那么受原生程序的青睐。在云原生泛滥的今天，臃肿的JVM使Java应用程序对比其他语言显得无比的庞大，各路大神也想了很多方式让Java变的更“原生”。最近Spring推出了Spring Native概念，并参考了其他大牛的文章后，今天我们就一探如何让用Spring Boot编写原生应用。  <br>
<br>Spring Native借助GraalVM native-image编译器来编译Spring应用，所以我们需要先来了解一下GraalVM。大部分脚本语言或者有动态特效的语言都需要一个语言虚拟机运行，比如CPython，Lua，Erlang，Java，Ruby，R，JS，PHP，Perl，APL等等，但是这些语言的虚拟机水平参差不齐，例如JVM的HotSpotVM、JS的V8都是“艺术”级别的，但CPython的VM就不忍直视。那能不能用一个“艺术”级别的虚拟机跑所有的语言呢？GraalVM就是这么一个高性能的救世主，它使用运行在JVM上的Truffle语言框架，将AST节点编译为机器代码，使用户只需要实现具体语言AST解释器，就能实现性能足够好的虚拟机，而实现这个编译器也是一个Java写的即时编译器Graal，GraalVM也因此得名。  <br>
<br>也许有同学会问了怎么用Java语言编译Java代码呢，而且还是这么高性能？这我们就要说说JEP 243的JVMCI。众所周知，HotSpot JVM内置了两个C++写的即时编译器（JIT）C1和C2，一般频繁的代码先用C1编译，如果热点继续，那么会使用C2编译。JVMCI相当于把本该交给C2编译的代码交给高级JIT：Graal编译，说到底就是将一段<code class="prettyprint">byte[]</code>在运行时换成另一段<code class="prettyprint">byte[]</code>。<br>
<br>那像Go和C/C++这类语言是否也能运行在JVM上呢？答案是肯定的。解决方案是将C/C++这些语言用一些工具（如Clang）转换为LLVM IR，然后使用基于Truffle的AST解释LLVM IR即可。（但，我们为啥要这么做？？）<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211228/5127a93400dc7586c628da76f6c36662.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/5127a93400dc7586c628da76f6c36662.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
到目前为止，几乎所有的语言都能在以JVM为基础，以Graal即时编译器为核心的虚拟机上运行起来了，但大家已经一定疑惑了，程序运行需要依赖JVM，而JVM必须提前安装JDK环境，而且自身启动慢，内存负载高，就不能把程序直接打包成平台相关可执行文件吗？答案是SubstrateVM，它借助Graal编译器，可以将Java程序AOT编译为可执行程序。所以万能的Graal编译器不仅能JIT，还能AOT。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211228/cc59ccd0aa5381308fe41accfb91da5d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/cc59ccd0aa5381308fe41accfb91da5d.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
好了，我们这些“CRUD仔”们了解这些基础魔法就足够了，至于SVM如何解决反射、GC等问题的高级魔法还是交给大牛们吧。现在进入我们的正题：用Spring Boot来编写一个原生应用。<br>
<h3>制作过程</h3><h4>Step 1：安装GraalVM和依赖工具</h4>因为大家都比较熟悉JDK安装过程，所以本过程带过了一些细节，不做重点讲解。首先我们需要安装GraalVM，笔者以自己的macOS系统为例，其他系统请参考官方安装文档。比较遗憾的是，GraalVM并没有提供针对M1优化的AArch64平台的包，我们只能使用AMD64平台，下载地址<a href="https://github.com/graalvm/graalvm-ce-builds/releases">点击这里</a>，我们使用Java 17版本的darwin压缩包，解压至：<br>
<pre class="prettyprint">/Library/Java/JavaVirtualMachines/<br>
</pre><br>
并且设置JAVA_HOME：<br>
<pre class="prettyprint">export GRAALVM17_HOME=$(/usr/libexec/java_home -v 17)<br>
export JAVA_HOME=$GRAALVM17_HOME<br>
</pre><br>
为了使用方便也可以设置Alias：<br>
<pre class="prettyprint">alias java17g='export JAVA_HOME=$GRAALVM17_HOME;java -version'<br>
</pre><br>
由于macOS的安全限制，需要删除<code class="prettyprint">quarantine</code>：<br>
<pre class="prettyprint">$ sudo xattr -r -d com.apple.quarantine $GRAALVM17_HOME<br>
</pre><br>
我们依然需要Maven作为本次探索的打包工具，请大家自行安装Maven，这里不再赘述。一切安装完成，我们可以运行<code class="prettyprint">java -version</code>和<code class="prettyprint">mvn -v</code>来验证一下安装是否成功。<br><br>
<pre class="prettyprint">$ java -version<br>
openjdk version "17.0.1" 2021-10-19<br>
OpenJDK Runtime Environment GraalVM CE 21.3.0 (build 17.0.1+12-jvmci-21.3-b05)<br>
OpenJDK 64-Bit Server VM GraalVM CE 21.3.0 (build 17.0.1+12-jvmci-21.3-b05, mixed mode, sharing)<br>
</pre><br>
最后，我们需要安装<code class="prettyprint">native-image</code>作为原生代码编译工具：<br>
<pre class="prettyprint">$ cd $GRAALVM_HOME/bin<br>
$ ./gu install native-image<br>
</pre><br>
当然，Xcode工具包因为包含GCC等工具，也必须安装，如已经安装可跳过。<br>
<pre class="prettyprint">$ sudo xcode-select --install<br>
</pre><br>
<h4>Step 2：建立Spring Boot应用</h4>按着官方的向导建立一个<strong>基于Spring Boot2.6.2版本，Java版本使用1.8</strong>的Web应用。注意一定要使用最新的2.6.2+版本，否则不支持AOT功能。并且，Java版本也只支持1.8。目录如下：<br>
<pre class="prettyprint">.<br>
├── HELP.md<br>
├── pom.xml<br>
├── src<br>
│   ├── main<br>
│   │   ├── java<br>
│   │   │   └── com<br>
│   │   │       └── ajk<br>
│   │   │           └── testspringnative<br>
│   │   │               └── TestSpringNativeApplication.java<br>
│   │   └── resources<br>
│   │       ├── application.yml<br>
│   │       ├── static<br>
│   │       └── templates<br>
│   └── test<br>
│       └── java<br>
│           └── com<br>
│               └── ajk<br>
│                   └── testspringnative<br>
│                       └── TestSpringNativeApplicationTests.java<br>
</pre><br>
其中<code class="prettyprint">TestSpringNativeApplication</code>代码如下：<br>
<pre class="prettyprint">import org.springframework.boot.SpringApplication;<br>
import org.springframework.boot.autoconfigure.SpringBootApplication;<br>
import org.springframework.web.bind.annotation.GetMapping;<br>
import org.springframework.web.bind.annotation.RequestParam;<br>
import org.springframework.web.bind.annotation.RestController;<br>
<br>
@SpringBootApplication<br>
@RestController<br>
public class TestSpringNativeApplication &#123;<br>
<br>
public static void main(String[] args) &#123;<br>
    SpringApplication.run(TestSpringNativeApplication.class, args);<br>
&#125;<br>
<br>
@GetMapping("/hello")<br>
public String hello(@RequestParam(value = "name", defaultValue = "World") String name) &#123;<br>
    return String.format("Hello %s!", name);<br>
&#125;<br>
<br>
&#125; <br>
</pre><br>
配置文件<code class="prettyprint">application.yml</code>代码如下：<br>
<pre class="prettyprint">server:<br>
port: 9000<br>
shutdown: graceful<br>
<br>
spring:<br>
profiles:<br>
active: default<br>
<br>
logging:<br>
level:<br>
root: info<br>
</pre><br>
<h4>Step 3：配置Maven</h4>为了方便演示，我们使用了最简单的代码和配置，重点是Maven的配置，以至于我需要用整个Step来说明。  <br>
<br>由于使用了官方向导生成的项目，所以基础<code class="prettyprint">pom.xml</code>文件如下：<br>
<pre class="prettyprint"><project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"<br>
     xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd"><br>
<modelVersion>4.0.0</modelVersion><br>
<parent><br>
    <groupId>org.springframework.boot</groupId><br>
    <artifactId>spring-boot-starter-parent</artifactId><br>
    <version>2.6.2</version><br>
    <relativePath/> <!-- lookup parent from repository --><br>
</parent><br>
<groupId>com.ajk</groupId><br>
<artifactId>test-spring-native</artifactId><br>
<version>0.0.1-SNAPSHOT</version><br>
<name>test-spring-native</name><br>
<description>test-spring-native</description><br>
<properties><br>
    <java.version>1.8</java.version><br>
</properties><br>
<dependencies><br>
    <dependency><br>
        <groupId>org.springframework.boot</groupId><br>
        <artifactId>spring-boot-starter-web</artifactId><br>
    </dependency><br>
<br>
    <dependency><br>
        <groupId>org.springframework.boot</groupId><br>
        <artifactId>spring-boot-starter-test</artifactId><br>
        <scope>test</scope><br>
    </dependency><br>
<dependencies><br>
<build><br>
    <plugins><br>
        <plugin><br>
            <groupId>org.springframework.boot</groupId><br>
            <artifactId>spring-boot-maven-plugin</artifactId><br>
        </plugin><br>
    </plugins><br>
</build><br>
</project><br>
</pre><br>
接下来我们开始配置Spring Boot Native，官方有两种方式实现编译原生应用：<br>
<ul><li>用Spring Boot Buildpacks生成包含原生应用的OCI容器。</li><li>用GraalVM native image Maven plugin生成原生应用。  </li></ul><br>
<br>由于篇幅关系，这里只介绍第二种方式，即编译为原生应用。  <br>
<br>首先增加包和插件依赖库：<br>
<pre class="prettyprint"><repositories><br>
<!-- ... --><br>
<repository><br>
    <id>spring-release</id><br>
    <name>Spring release</name><br>
    <url>https://repo.spring.io/release</url><br>
</repository><br>
</repositories><br>
<pluginRepositories><br>
<!-- ... --><br>
<pluginRepository><br>
    <id>spring-release</id><br>
    <name>Spring release</name><br>
    <url>https://repo.spring.io/release</url><br>
</pluginRepository><br>
</pluginRepositories><br>
</pre><br>
再次确认我们的Spring Boot版本为2.6.2（因为Spring Native 0.11.1版本支持此版本），并添加如下依赖：<br>
<pre class="prettyprint"><dependencies><br>
<!-- ... --><br>
<dependency><br>
    <groupId>org.springframework.experimental</groupId><br>
    <artifactId>spring-native</artifactId><br>
    <version>0.11.1</version><br>
</dependency><br>
</dependencies><br>
</pre><br>
添加Spring AOT部署插件：<br>
<pre class="prettyprint"><build><br>
<plugins><br>
    <!-- ... --><br>
    <plugin><br>
        <groupId>org.springframework.experimental</groupId><br>
        <artifactId>spring-aot-maven-plugin</artifactId><br>
        <version>0.11.1</version><br>
        <executions><br>
            <execution><br>
                <id>generate</id><br>
                <goals><br>
                    <goal>generate</goal><br>
                </goals><br>
            </execution><br>
            <execution><br>
                <id>test-generate</id><br>
                <goals><br>
                    <goal>test-generate</goal><br>
                </goals><br>
            </execution><br>
        </executions><br>
    </plugin><br>
</plugins><br>
</build><br>
</pre><br>
再添加原生编译插件，这里使用一个profile来更好的管理：<br>
<pre class="prettyprint"><profiles><br>
<profile><br>
    <id>native</id><br>
    <build><br>
        <plugins><br>
            <plugin><br>
                <groupId>org.graalvm.buildtools</groupId><br>
                <artifactId>native-maven-plugin</artifactId><br>
                <version>0.9.9</version><br>
                <extensions>true</extensions><br>
                <executions><br>
                    <execution><br>
                        <id>build-native</id><br>
                        <goals><br>
                            <goal>build</goal><br>
                        </goals><br>
                        <phase>package</phase><br>
                    </execution><br>
                </executions><br>
                <configuration><br>
                    <!-- ... --><br>
                </configuration><br>
            </plugin><br>
            <!-- Avoid a clash between Spring Boot repackaging and native-maven-plugin --><br>
            <plugin><br>
                <groupId>org.springframework.boot</groupId><br>
                <artifactId>spring-boot-maven-plugin</artifactId><br>
                <configuration><br>
                    <classifier>exec</classifier><br>
                </configuration><br>
            </plugin><br>
        </plugins><br>
    </build><br>
</profile><br>
</profiles><br>
</pre><br>
一切妥当！开始编译吧！<br>
<pre class="prettyprint">$ mvn clean -Pnative -DskipTests package<br>
</pre><br>
官方推荐编译的机器不能少于8核8G内存，否则编译工具会报错。在我的M1的机器上，编译大概需要10分钟左右，编译时CPU峰值使用率大概在50%，内存占用6.9GB。<br>
<h3>简单评测</h3>首先看一下编译文件大小对比：<br>
<ul><li>fatjar包文件为17.8M（不包含JRE），原生可执行文件为68.2M。</li><li>使用spring-boot-maven-plugin生成包含JRE运行环境的容器镜像大小为270M，而使用Tiny Core Linux+原生应用的形式，镜像大小可以控制在100M以内，为96M。压缩比达到35%之多  。</li></ul><br>
<br>再来看看启动速度对比：<br>
<ul><li>fatjar启动时间为8.2s</li><li>原生文件启动时间为5.6s</li></ul><br>
<br>程序使用CPU和内存对比：<br>
<ul><li>fatjar空载CPU 0.5%，内存使用528M</li><li>原生应用空载CPU 0.3%，内存使用85M  </li></ul><br>
<br>如下表格：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211228/889a2be59698af45779285ea0d87b615.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211228/889a2be59698af45779285ea0d87b615.png" class="img-polaroid" title="b.png" alt="b.png" referrerpolicy="no-referrer"></a>
</div>
<br>
总体来讲，原生应用从产物大小，启动速度，运行负载来讲都优与Jar包应用，这还是在没有针对arm的指令集做优化的基础上的，但对比官方宣传的内存使用20M内存占用还有一定差距。<br>
<h3>总结</h3>经过几天折腾，GraalVM的性能即使不编译为原生应用也优于HotSpot VM，在编译为原生应用后，性能也有一定的提升。但目前Spring Native还不够成熟，笔者想用undertow代替Tomcat Web容器而编译后的原生应用，始终无法运行。相信后面版本应该会修复一些问题。  <br>
<br>本文总结了一种编译原生的方式，另一种生成原生镜像的方式大家可以自行研究（注意，编译成原生镜像需要阅读大量文章）。另外，由于时间有限，在两者的压测过程中，原生应用GC回收内存速度快于jar包应用，大家也可以深入研究原生内存回收方式。<br>
<br>所有代码可在<a href="https://github.com/huang-kai/test-spring-native">GitHub</a>上参考。<br>
<br>参考资料：<br>
<ol><li><a href="https://www.graalvm.org/docs/introduction/" rel="nofollow" target="_blank">https://www.graalvm.org/docs/introduction/</a></li><li><a href="https://docs.spring.io/spring-native/docs/current/reference/htmlsingle/" rel="nofollow" target="_blank">https://docs.spring.io/spring- ... ngle/</a></li><li><a href="https://openjdk.java.net/jeps/243" rel="nofollow" target="_blank">https://openjdk.java.net/jeps/243</a></li><li><a href="http://trufflesuite.com/truffle/" rel="nofollow" target="_blank">http://trufflesuite.com/truffle/</a></li><li><a href="https://github.com/graalvm/labs-openjdk-17" rel="nofollow" target="_blank">https://github.com/graalvm/labs-openjdk-17</a></li></ol><br>
<br>作者：黄凯，58安居客新房技术部负责人。拥有10多年Java/Go研发经验，多年从事云计算研究和架构设计经验，对系统架构和业务架构都有一定研究。加入58安居客之前曾任职于百姓网、拼多多、沪江教育、IBM、HP等互联网和外企公司。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            