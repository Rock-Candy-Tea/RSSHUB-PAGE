
---
title: 'Kotlin 1.6.0 发布，大量新特性与功能稳定'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5457'
author: 开源中国
comments: false
date: Wed, 17 Nov 2021 08:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5457'
---

<div>   
<div class="content">
                                                                                            <p>11 月 16 日，J<span style="background-color:#ffffff; color:#4a4a4a">etBrains </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fkotlin%2F2021%2F11%2Fkotlin-1-6-0-is-released%2F" target="_blank">发布了 Kotlin 1.6.0 </a>，其中包含稳定的详尽 <code>whens</code> 声明、Kover 和 Kotlin/Native 的新内存管理器，1.5.30 中发布的其他语言和标准库功能也变得更稳定。</p> 
<h2 style="margin-left:0px">密封（详尽）<code>when</code> 声明</h2> 
<p style="margin-left:0px">Sealed <code>when</code>是一项<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FKT-12380%3F_ga%3D2.229249755.633909770.1637103893-2081573158.1634857345%26_gl%3D1*10g44sv*_ga*MjA4MTU3MzE1OC4xNjM0ODU3MzQ1*_ga_0WQ2ZF5VGT*MTYzNzEwMzg5Mi4xLjEuMTYzNzEwNDMzMy4w" target="_blank">期待已久的</a>功能，如果你的 when 语句不够详尽，Kotlin 编译器发会警告。</p> 
<p style="margin-left:0px">Kotlin 会详尽地检查封闭类、枚举和布尔类型的表达式，使用那些代数数据类型对域建模时它非常有用。例如对应用程序的用户有不同的契约首选项，建模为一个封闭的类层次结构：</p> 
<pre><code>sealed class Contact &#123;

   data class PhoneCall(val number: String) : Contact()

   data class TextMessage(val number: String) : Contact()

   data class InstantMessage(val type: IMType, val user: String) : Contact()

&#125;</code></pre> 
<p>现在，如果你写了一个表达式：根据不同的联系人偏好返回不同的结果。但是又忘记处理应用程序中的所有类型，编译器将会标记一个错误：</p> 
<pre><code>fun Rates.computeMessageCost(contact: Contact): Cost =

   when (contact) &#123; // ERROR: 'when' expression must be exhaustive

       is Contact.PhoneCall -> phoneCallCost

       is Contact.TextMessage -> textMessageCost

   &#125;</code></pre> 
<p>在 Kotlin 1.6.0 之前，这种问题编译器只会报弱 IDE 检查，从 Kotlin 1.6 开始，它会产生以下编译器警告（warning）：</p> 
<p><code>Non-exhaustive 'when' statements on sealed class/interface will be prohibited in 1.7. Add an 'is InstantMessage' branch or 'else' branch instead.</code></p> 
<p>在 Kotlin 1.7 中它会变成一个错误（ERROR），详情可参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FKT-47709" target="_blank">KT-47709</a> 。</p> 
<h2 style="margin-left:0px">Suspending 函数作为超类型</h2> 
<p style="margin-left:0px">Kotlin 1.6 稳定了对将 <code>suspend</code> 挂起函数类型实现为超级接口的功能。</p> 
<p style="margin-left:0px">设计 Kotlin API 需要自定义各种库函数的行为时，接受函数类型是惯用的做法。例如，<code>kotlinx.coroutines</code> API 在其 Job 接口中有一个成员函数，看起来类似于：</p> 
<pre><code>fun invokeOnCompletion(handler: () -> Unit)</code></pre> 
<p style="margin-left:0px">可以方便地使用像 <code>invokeOnCompletion &#123;doSomething()&#125;</code> 这些 lambda 函数。如果想要处理完成的类，可以通过在类中直接实现函数 type () -> Unit 来简化和优化代码，而不需要创建额外的 lambda 。</p> 
<pre><code>class MyCompletionHandler : () -> Unit &#123;
   override fun invoke() &#123; doSomething() &#125;
&#125;</code></pre> 
<p style="margin-left:0px">从Kotlin 1.6开始，这种优化可以通过挂起函数实现。如果你的 api 接受挂起函数类型，像这样：</p> 
<pre><code>public fun launchOnClick(action: suspend () -> Unit) &#123;&#125;</code></pre> 
<p style="margin-left:0px">那么我们就不再局限于传递 lambda 和挂起函数引用了，也可以在类中实现相应的挂起函数类型：</p> 
<pre><code>class MyClickAction : suspend () -> Unit &#123;
   override suspend fun invoke() &#123; doSomething() &#125;
&#125;</code></pre> 
<h3 style="margin-left:0px">挂起转换</h3> 
<p style="margin-left:0px">Kotlin 1.6 稳定了从常规到挂起函数类型的转换。现在可以传递任何常规函数​​类型的表达式，其中使用预期挂起作为参数，编译器将自动执行转换。</p> 
<h3 style="margin-left:0px">改进了递归泛型类型的类型推断</h3> 
<p>从1.6.0开始，如果默认情况下是递归泛型，Kotlin编译器能根据相应类型形参的上限推断类型实参。这可以实现使用递归泛型类型创建各种模式（通常在 Java 中用于制作构建器 API）：</p> 
<pre><code>// Before 1.5.30
val containerA = PostgreSQLContainer(DockerImageName.parse("postgres:13-alpine")).apply &#123;
    withDatabaseName("db")
    withUsername("user")
    withPassword("password")
    withInitScript("sql/schema.sql")
&#125;

// With compiler option in 1.5.30 or by default starting with 1.6.0
val containerB = PostgreSQLContainer(DockerImageName.parse("postgres:13-alpine"))
    .withDatabaseName("db")
    .withUsername("user")
    .withPassword("password")
    .withInitScript("sql/schema.sql")</code></pre> 
<h2 style="margin-left:0px">Builder inference 改进</h2> 
<p style="margin-left:0px">Kotlin 1.5.30 引入了 <code>-Xunrestricted-builder-inference</code> 编译器选项，让关于构建器调用的类型信息可以在构建器 lambda 中获取。也就是说，它引入了调用返回尚未推断类型的实例的能力，比如 buildList() lambda 中的 <code>get()</code>。</p> 
<p style="margin-left:0px">从 1.6.0 开始，无需指定 <code>-Xunrestricted-builder-inference</code> 进行以前禁止的调用。现在可以使用-Xenable-builder-inference 编译器选项编写自己的泛型构建器，而不需要应用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fapi%2Flatest%2Fjvm%2Fstdlib%2Fkotlin%2F-builder-inference%2F" target="_blank"><code>@BuilderInference</code></a> 注释，且如果常规类型推断无法解析类型信息，你还可以自动启用 Builder inference构建器推断。</p> 
<h3 style="margin-left:0px">长期支持以前的 API 版本</h3> 
<p style="margin-left:0px">从 Kotlin 1.6.0 开始可以使用三个以前的 API 版本进行开发，目前可用的 API 版本包括 1.3、1.4、1.5 和 1.6。</p> 
<h2 style="margin-left:0px">Kotlin/JVM</h2> 
<p style="margin-left:0px"><strong>具有运行时保留的可重复注释。</strong><em> </em>Kotlin 与 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.oracle.com%2Fjavase%2Ftutorial%2Fjava%2Fannotations%2Frepeating.html" target="_blank">Java 8 一样</a>具有可重复的注释。在 Kotlin 1.6 中，该功能与 Java 兼容，<code>@kotlin.annotation.Repeatable</code> 现在接受任何保留并让注释在 Kotlin 和 Java 中都可重复。</p> 
<p style="margin-left:0px">Kotlin 端现在也支持 Java 可重复注释。</p> 
<h2 style="margin-left:0px">Kotlin/Native</h2> 
<ul> 
 <li>现在可以尝试<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fkotlin%2F2021%2F08%2Ftry-the-new-kotlin-native-memory-manager-development-preview%2F" target="_blank"><strong>新 Kotlin/Native 内存管理器</strong></a>的实验版。此功能致力于在多平台项目中提供一致的开发体验。新的内存管理器解除了对线程间对象共享的现有限制，并提供完全无泄漏的并发编程原语，这些原语是安全的，不需要开发人员进行任何特殊管理或注释。</li> 
 <li>Kotlin/Native 现在支持 Xcode 13。</li> 
 <li><strong>在任何主机上编译 Windows 目标，</strong>现在可以在任何支持 Kotlin/Native 的主机上编译 Windows 目标 <code>mingwX64</code> 和 <code>mingwX86</code> 。</li> 
 <li>Kotlin 1.6.0 <strong>重新设计了 </strong>Kotlin/Native 在幕后使用<strong>的 LLVM 依赖项，</strong>同时将 LLVM 版本更新到 11.1.0 ，并减少了依赖项大小。</li> 
 <li><strong>带有 JVM 和 JS IR 后端的统一编译器插件 ABI</strong>。现在，Kotlin 多平台 Gradle 插件能够将可嵌入的编译器 jar（用于 JVM 和 JS IR 后端的那个）用于 Kotlin/Native，这意味着可以为 Native 和其他支持的平台使用相同的编译器插件工件。</li> 
</ul> 
<h2 style="margin-left:0px">稳定的 <code>typeOf()</code></h2> 
<p style="margin-left:0px">Kotlin 1.6.0 带来了稳定的 <code>typeOf()</code>。从 1.3.40 开始，<code>typeOf()</code>作为实验性 API 在 JVM 平台上可用，现在可以在任何 Kotlin 平台上使用它，且 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fapi%2Flatest%2Fjvm%2Fstdlib%2Fkotlin.reflect%2F-k-type%2F%23kotlin.reflect.KType" target="_blank"><code>KType</code></a> 编译器可以推断任何 Kotlin 类型的表示。</p> 
<pre><code>inline fun  renderType(): String &#123;
    val type = typeOf()
    return type.toString()
&#125;

fun main() &#123;
    val fromExplicitType = typeOf()
    val fromReifiedType = renderType>()
&#125;</code></pre> 
<h2 style="margin-left:0px">稳定的集合构建器</h2> 
<p style="margin-left:0px"><code>buildMap()</code>，<code>buildList()</code> 和 <code>buildSet()</code> 已经稳定，构建器返回的集合现在可以在只读状态下序列化。</p> 
<h3 style="margin-left:0px">稳定的整数位旋转操作</h3> 
<p style="margin-left:0px">将数字的二进制表达式向左或向右旋转指定位数的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fapi%2Flatest%2Fjvm%2Fstdlib%2Fkotlin%2Frotate-left.html" target="_blank"><code>rotateLeft()</code></a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fapi%2Flatest%2Fjvm%2Fstdlib%2Fkotlin%2Frotate-right.html" target="_blank"><code>rotateRight()</code></a> 函数已经稳定。</p> 
<pre><code>val number: Short = 0b10001
println(number.rotateRight(2).toString(radix = 2)) // 100000000000100
println(number.rotateLeft(2).toString(radix = 2))  // 1000100</code></pre> 
<h3 style="margin-left:0px">稳定正则表达式函数</h3> 
<p style="margin-left:0px">稳定了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fapi%2Flatest%2Fjvm%2Fstdlib%2Fkotlin.text%2F-regex%2Fsplit-to-sequence.html" target="_blank"><code>splitToSequence()</code></a>——一个用于将字符串拆分为序列的正则表达式函数</p> 
<pre><code>val colorsText = "green, red , brown&blue, orange, pink&green"
val regex = "[,\\\\\\\\s]+".toRegex()
val mixedColor = regex.splitToSequence(colorsText)
    .onEach &#123; println(it) &#125;
    .firstOrNull &#123; it.contains('&') &#125;
println(mixedColor) // "brown&blue"</code></pre> 
<p style="margin-left:0px">有关 Kotlin 1.6.0 的详尽信息可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fkotlin%2F2021%2F11%2Fkotlin-1-6-0-is-released%2F" target="_blank">发布公告</a>中查看。</p>
                                        </div>
                                      
</div>
            