
---
title: 'Gradle 7.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=862'
author: 开源中国
comments: false
date: Wed, 16 Jun 2021 07:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=862'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Gradle 7.1 现已发布。Gradle 是一个基于 Apache Ant 和 Apache Maven 概念的项目自动化构建工具，支持依赖管理和多项目，类似 Maven，但比之简单轻便。它使用一种基于 Groovy 的特定领域语言来声明项目设置，而不是传统的 XML。</p> 
<p>此版本改进了增量 Java 编译，并使 Kotlin DSL 中配置 Groovy、Scala 和 Antlr sourcesets 变得更加容易。此外还有一些新的弃用和小的改进，使 Gradle 更容易使用。</p> 
<h4><strong>改进的 Java 增量编译</strong></h4> 
<p>Gradle 有一个默认启用的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.1%2Fuserguide%2Fjava_plugin.html%23sec%3Aincremental_compile" target="_blank">Java 增量编译器</a>，它通过只编译需要编译的 Java 源文件来加快增量构建。Java 增量编译器在此版本中获得了重大改进。</p> 
<p><strong>增量编译分析现在存储在构建缓存中</strong></p> 
<p>在以前的 Gradle 版本中，增量编译分析仅存储在本地。这意味着当编译任务的输出从<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.1%2Fuserguide%2Fbuild_cache.html" target="_blank">构建缓存</a>中获取时，后续构建无法进行增量编译，并且总是需要完全重新编译。</p> 
<p>在 Gradle 7.1 中，增量分析的结果现在存储在构建缓存中，从构建缓存中获取后的第一次编译将是增量的。</p> 
<p><strong>增量编译分析更快，使用更少的内存和磁盘空间</strong></p> 
<p>增量编译分析需要 Gradle 从 class files 中提取符号并分析依赖关系的传递图以确定特定符号的 consumers。这会消耗大量内存和时间。</p> 
<p>Gradle 7.1 显着降低了增量编译分析的成本，以及分析的规模。此更改的影响因项目而异，但可能非常明显。官方表示，在 Gradle 项目本身，其能够将增量编译速度提高两倍。</p> 
<p><strong>对常量的更改不再触发全面的重新编译</strong></p> 
<p>由于 Java 编译器的工作方式，以前的 Gradle 版本在上游依赖项中的任何常量发生变化时，就会被迫执行全面的重新编译。</p> 
<p>Gradle 7.1 引入了一个编译器插件，该插件执行常量使用跟踪，并且仅在常量更改时重新编译常量的 consumers。这可以加速使用大量常量的项目的增量构建，这对于从模板引擎生成的代码很常见。</p> 
<h4><strong>在 Kotlin DSL 中更容易配置 source set</strong></h4> 
<p>在使用 Kotlin DSL 时，为 Java 以外的语言配置 source locations 时需要一个特殊的构造。 例如，以下是配置的<code>groovy</code> sources 方式:</p> 
<pre><code class="language-kotlin">sourceSets &#123;
    main &#123;
        withConvention(GroovySourceSet::class) &#123;
            groovy &#123;
                setSrcDirs(listOf("src/groovy"))
            &#125;
        &#125;
    &#125;
&#125;
</code></pre> 
<p>Gradle 7.1 在以下插件中定义了对每种语言的 source sets 的扩展：</p> 
<ul> 
 <li><code>groovy</code></li> 
 <li><code>antlr</code></li> 
 <li><code>scala</code></li> 
</ul> 
<p>这意味着 Kotlin DSL 将可以访问自动生成的访问器，<code>withConvention</code>不再是必要的：</p> 
<pre><code class="language-kotlin">sourceSets &#123;
    main &#123;
        groovy &#123;
            setSrcDirs(listOf("src/groovy"))
        &#125;
    &#125;
&#125;
</code></pre> 
<h4><strong>为编译任务构建缓存友好的命令行参数</strong></h4> 
<p>现在可以使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.1%2Fjavadoc%2Forg%2Fgradle%2Fapi%2Ftasks%2Fcompile%2FProviderAwareCompilerDaemonForkOptions.html%23getJvmArgumentProviders--" target="_blank">jvmArgumentProviders</a> 为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.1%2Fjavadoc%2Forg%2Fgradle%2Fapi%2Ftasks%2Fcompile%2FJavaCompile.html" target="_blank">JavaCompile</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.1%2Fjavadoc%2Forg%2Fgradle%2Fapi%2Ftasks%2Fcompile%2FGroovyCompile.html" target="_blank">GroovyCompile</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.1%2Fjavadoc%2Forg%2Fgradle%2Fapi%2Ftasks%2Fscala%2FScalaCompile.html" target="_blank">ScalaCompile</a> 任务的编译器守护程序提供命令行参数。</p> 
<p>通过<code>jvmArgumentProviders</code>配置的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.1%2Fjavadoc%2Forg%2Fgradle%2Fprocess%2FCommandLineArgumentProvider.html" target="_blank">CommandLineArgumentProvider</a> 对象将被询问输入和/或输出注释，Gradle 会将这些添加到相应的任务中。</p> 
<pre><code>def javaAgent = objects.newInstance(JavaAgent)
javaAgent.jarFile = file('some/path/to/agent.jar')

// This can be done with Groovy, Java or Scala compilation
tasks.withType(GroovyCompile).configureEach &#123;
    groovyOptions.forkOptions.jvmArgumentProviders.add(javaAgent)
&#125;

abstract class JavaAgent implements CommandLineArgumentProvider &#123;
    @Classpath
    abstract RegularFileProperty getJarFile()

    @Override
    List<String> asArguments() &#123;
        def jarFilePath = jarFile.get().asFile.absolutePath
        return ["-javaagent:$&#123;jarFilePath&#125;".toString()]
    &#125;
&#125;</code></pre> 
<h4><strong>JaCoCo 插件支持 Java 15/16</strong></h4> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.1%2Fuserguide%2Fjacoco_plugin.html" target="_blank">JaCoCo 插件</a>已升级到最新的 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jacoco.org%2Fjacoco%2Ftrunk%2Fdoc%2Fchanges.html" target="_blank">JaCoCo 0.8.7 版本</a>，其中包括对 Java 15 和 16 的支持以及对 Java 17 的实验性支持。</p> 
<p>更多详情可查看更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.1%2Frelease-notes.html" target="_blank">https://docs.gradle.org/7.1/release-notes.html</a></p>
                                        </div>
                                      
</div>
            