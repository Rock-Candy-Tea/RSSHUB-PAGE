
---
title: 'Kotlin 1.5.3 首个 RC 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=62'
author: 开源中国
comments: false
date: Thu, 12 Aug 2021 23:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=62'
---

<div>   
<div class="content">
                                                                                            <p>Kotlin 1.5.3 发布了首个 RC 版本。RC 意味着所有特性已确定，在正式发布前的主要工作是修复 bug。</p> 
<p>主要新特性包括：</p> 
<ul> 
 <li>对 Opt-in 要求的更新</li> 
 <li>Kotlin/JS IR 后端进入 Beta 阶段</li> 
 <li>Gradle 插件对 Java 工具链的支持</li> 
 <li>标准库中对 Regex 和 Duration 的改进</li> 
</ul> 
<p><strong>Kotlin/JS IR 后端进入 Beta 阶段</strong></p> 
<p>自 Kotlin 1.4 发布以来，Kotlin/JS 编译器的 IR 后端一直处于 Alpha 状态。现在终于进入了 Beta 阶段，这意味着后续不会出现破坏性变化，未来工作主要集中在提升稳定性上。</p> 
<p>文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fdocs%2Fjs-ir-compiler.html" target="_blank">https://kotlinlang.org/docs/js-ir-compiler.html</a></p> 
<p><strong>Gradle：构建脚本中 Kotlin 守护进程增加 JVM 选项以及 Java 工具链支持</strong></p> 
<p>Gradle 6.7 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.gradle.org%2Fjava-toolchains" target="_blank">引入</a>了对 Java 工具链的支持——可用于为项目编译选择 JDK。开发者只需在构建脚本中声明所需的版本，Gradle 会自动完成剩下的工作。Kotlin 1.5.30-RC 针对 Kotlin 编译任务启用了 Java 工具链支持：</p> 
<pre><code>kotlin &#123;
    jvmToolchain &#123;
        (this as JavaToolchainSpec).languageVersion.set(JavaLanguageVersion.of(<MAJOR_JDK_VERSION>)
    &#125;
&#125;</code></pre> 
<p>其他与 Gradle 相关的改进包括为 Kotlin Gradle 守护进程提供 JVM 选项的新方法。开发者可以在<code>gradle.properties</code>的单独代码行进行指定：</p> 
<pre><code>kotlin.daemon.jvmargs = "-Xmx486m -Xms256m -XX:+UseG1GC"</code></pre> 
<p>或在<code>build.gradle.kts</code>中进行指定：</p> 
<pre><code>kotlin &#123;
   kotlinDaemonJvmArgs = listOf("-Xmx486m", "-Xms256m", "-XX:+UseG1GC")
&#125;</code></pre> 
<p><strong>改进 Regex 和 Duration API</strong></p> 
<p>Kotlin 的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fapi%2Flatest%2Fjvm%2Fstdlib%2Fkotlin.text%2F-regex%2F" target="_blank">Regex</a> API 新增实验性功能。</p> 
<ul> 
 <li><code>matchesAt()</code>用于检查正则表达式是否在字符串的指定位置匹配。如果找到匹配项，会返回匹配项本身。</li> 
</ul> 
<pre><code>val releaseText = "Kotlin 1.5.30 is coming!"
// regular expression: one digit, dot, one digit, dot, one or more digits
val versionRegex = "\\d[.]\\d[.]\\d+".toRegex()
println(versionRegex.matchesAt(releaseText, 7)) // "true"
println(versionRegex.matchAt(releaseText, 7)?.value) // "1.5.30"</code></pre> 
<ul> 
 <li><code>splitToSequence()</code>与<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fapi%2Flatest%2Fjvm%2Fstdlib%2Fkotlin.text%2F-regex%2Fsplit.html" target="_blank"><code>split()</code></a>相对应——围绕给定正则表达式的匹配项拆分字符串，但会将返回的结果作为<code>Sequence</code>。类似的功能也已被添加到<code>CharSequence</code>。</li> 
</ul> 
<pre><code>val phoneNumber = "+7 (123) 456-78-90"
val regex = "[ ()-]+".toRegex()
val parts = phoneNumber.splitToSequence(regex)
// or
// val parts = regex.splitToSequence(phoneNumber)

// any processing operation on parts are executed lazily</code></pre> 
<p>更多内容查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fkotlin%2F2021%2F08%2Fkotlin-1-5-30-rc-released%2F" target="_blank">发布公告</a>。</p>
                                        </div>
                                      
</div>
            