
---
title: 'Kotlin 1.7.0-Beta 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8155'
author: 开源中国
comments: false
date: Fri, 27 May 2022 18:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8155'
---

<div>   
<div class="content">
                                                                                            <p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">Kotlin 1.7.0 的首个预览版现已发布。此预览版的一些亮点：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>构建器推断变更。</li> 
 <li>min() 和 max() 集合函数回归。</li> 
 <li>绝对不可空类型得到稳定。</li> 
 <li>新版 Kotlin/Native 内存管理器更新。</li> 
</ul> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">安装 1.7.0-Beta 以试用这些功能，并<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotl.in%2Fissue" target="_blank">报告您发现的任何问题</a>以帮助我们改进 Kotlin 1.7.0。</p> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">我们将在后续博文中介绍其他令人兴奋的功能。敬请关注！</p> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">从 1.7.0 开始，我们更新了我们的发布节奏术语：将“Milestone”（里程碑）更改为“Beta”（测试版）。 这一决定背后有几个原因：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>我们希望 Kotlin 构建术语更加符合软件发布周期的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FSoftware_release_life_cycle%23Beta" target="_blank">标准术语</a>。 更准确地说，“Beta”意味着我们向该特定版本中添加新功能的工作已经完成，并且正在致力于稳定工作。 不过，我们也会实现最终变更，包括基于用户反馈的变更。</li> 
 <li>前段时间，M-release 编译器一直在生成“预发布”代码，这使得这些版本更难测试。 现在完全不一样了。 我们希望避免任何混淆，并强调试用 Kotlin Beta 版本的过程将十分简单，并且 Kotlin 团队非常鼓励大家试用这一版本。</li> 
 <li>最后但同样重要的一点是，“Beta”一词本身就有呼吁社区提供反馈的意味。 借此术语，我们想让您知道我们希望您能与我们分享反馈。</li> 
</ul> 
<h2>构建器推断变更</h2> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">构建器推断是一种特殊的类型推断，在调用泛型构建器函数时很有帮助。 它可以帮助编译器推断调用的类型实参，方法是使用其 lambda 实参中其他调用的相关类型信息。</p> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">Kotlin 1.7.0-Beta 中包含了针对构建器推断的更多变更。 这些变更使我们的构建器推断趋于稳定，我们在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FKT-45618%2FStabilize-builder-inference" target="_blank">路线图</a>中的任务之一也趋于完成。</p> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">在此版本中，如果常规类型推断无法获得有关类型的足够信息，则无需指定 <code>-Xenable-builder-inference</code> 编译器选项（我们<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fdocs%2Fwhatsnew16.html%23changes-to-builder-inference" target="_blank">在 1.6.0 版本中引入</a>），即可自动激活构建器推断。</p> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">这意味着现在您无需应用任何额外的注解或选项，即可编写自己的使用构建器类型推断的构建器。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fdocs%2Fusing-builders-with-builder-inference.html" target="_blank">了解如何编写自定义通用构建器</a>。</p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:start">min() 和 max() 集合函数回归</h2> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fdocs%2Fwhatsnew14.html%23collections" target="_blank">Kotlin 1.4</a> 中，我们将 <code>min()</code> 和 <code>max()</code> 集合函数重命名为 <code>minOrNull()</code> 和 <code>maxOrNull()</code>。 这些新的名称能够更好地反映它们的行为 – 如果接收器集合为空，则返回 <code>null</code>。 它还有助于使函数的行为与整个 Kotlin Collections API 中使用的命名惯例保持一致。<code>minBy()</code>、<code>maxBy()</code>、<code>minWith()</code> 和 <code>maxWith()</code> </p> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">同样如此，在 Kotlin 1.4 中均具有自己的 <code>*OrNull()</code> 同义词。 受此变更影响的旧函数已逐渐弃用。</p> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">Kotlin 1.7.0-Beta 重新引入了原始的函数名称，但加入了不可空返回类型。 现在，更新后的 <code>min()</code>、<code>max()</code>、<code>minBy()</code>、<code>maxBy()</code>、<code>minWith()</code> 和 <code>maxWith()</code> 会严格返回集合元素或抛出异常。</p> 
<div style="text-align:start"> 
 <div> 
  <div> 
   <div> 
    <div> 
     <div> 
      <pre><code>fun main() &#123;
    val numbers = listOf<Int>()
    println(numbers.maxOrNull()) // "null"
    println(numbers.max()) // "Exception in… Collection is empty."
&#125;</code></pre> 
      <p>请参见<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FKT-38854" target="_blank">此 YouTrack 问题</a>以了解详情。</p> 
      <h2>绝对不可空类型得到稳定</h2> 
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">Kotlin 1.7.0 将具有稳定的绝对不可空类型，这些类型是<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fdocs%2Fwhatsnew1620.html%23definitely-non-nullable-types" target="_blank">在 Kotlin 1.6.20 中引入</a>的。</p> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">添加这些类型的目的是在扩展泛型 Java 类和接口时提供更好的互操作性。</p> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">自 Kotlin 1.6.20 起，您已经能够使用新语法 <code>T & Any</code> 在使用站点上将泛型类型形参标记为绝对不可空。 该语法形式来自<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FIntersection_type" target="_blank">相交类型</a>表示法，现在被限制为一个类型形参，<code>&</code> 左侧为可空上限，右侧为不可空 <code>Any</code>：</p> 
<pre><code>fun <T> elvisLike(x: T, y: T & Any): T & Any = x ?: y

fun main() &#123;
    elvisLike<String>("", "").length // OK
    elvisLike<String>("", null).length // Error: 'null' cannot be a value of a non-null type

    elvisLike<String?>(null, "").length // OK
    elvisLike<String?>(null, null).length // Error: 'null' cannot be a value of a non-null type
&#125;</code></pre> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">在此测试版中，将默认启用绝对不可空类型。 无需其他步骤。</p> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKotlin%2FKEEP%2Fblob%2Fc72601cf35c1e95a541bb4b230edb474a6d1d1a8%2Fproposals%2Fdefinitely-non-nullable-types.md" target="_blank">KEEP</a> 中详细了解绝对不可空类型。</p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:start">正则表达式特定位置匹配</h2> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fdocs%2Fwhatsnew1530.html%23matching-with-regex-at-a-particular-position" target="_blank">在 1.5.30 中引入</a>的 <code>Regex.matchAt()</code> 和 <code>Regex.matchesAt()</code> 函数现已达到稳定版本。 它们提供了一种方式来检查正则表达式在 <code>String</code> 或 <code>CharSequence</code> 中的特定位置是否具有精确匹配。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>matchesAt()</code> 可以检查匹配并返回布尔结果：</li> 
</ul> 
<div style="text-align:start"> 
 <div> 
  <div> 
   <div> 
    <div> 
     <div> 
      <pre><code>fun main()&#123;
    val releaseText = "Kotlin 1.7.0 is on its way!"
    // regular expression: one digit, dot, one digit, dot, one or more digits
    val versionRegex = "\\d[.]\\d[.]\\d+".toRegex()

    println(versionRegex.matchesAt(releaseText, 0)) // "false"
    println(versionRegex.matchesAt(releaseText, 7)) // "true"
&#125;</code></pre> 
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code><code>matchAt()</code></code>会在找到匹配的情况下返回匹配，在未找到匹配的情况下返回 null：</li> 
</ul> 
<div style="text-align:start"> 
 <div> 
  <div> 
   <div> 
    <div> 
     <div> 
      <pre><code>fun main()&#123;
    val releaseText = "Kotlin 1.7.0 is on its way!"
    val versionRegex = "\\d[.]\\d[.]\\d+".toRegex()

    println(versionRegex.matchAt(releaseText, 0)) // "null"
    println(versionRegex.matchAt(releaseText, 7)?.value) // "1.7.0"
&#125;</code></pre> 
      <p>我们将非常感谢您在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FKT-34021" target="_blank">此 YouTrack 问题</a>中提供反馈。</p> 
      <h2>新版 Kotlin/Native 内存管理器</h2> 
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">我们将继续收集反馈，并改进新版 Kotlin/Native 内存管理器。 目前，您可以在项目中试用 Alpha 版本。 Kotlin 1.7.0-Beta 带来了更多性能改进，这些改进将提升开发者体验。</p> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">新版内存管理器消除了 JVM 与 Native 平台之间的差异。 它在多平台项目中提供了一致的开发者体验。 例如，您可以更加轻松地开发同时适用于 Android 和 iOS 平台的新款跨平台移动应用程序。</p> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">新版 Kotlin/Native 内存管理器解除了线程间对象共享的限制。 它还提供了安全且无需任何特殊管理或注解的无泄漏并发编程语言基元。新版内存管理器将成为未来版本中的默认管理器，因此我们鼓励您立即试用。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fkotlin%2F2021%2F08%2Ftry-the-new-kotlin-native-memory-manager-development-preview%2F" target="_blank">详细了解</a>新版内存管理器并探索演示项目，或直接跳转到<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJetBrains%2Fkotlin%2Fblob%2Fmaster%2Fkotlin-native%2FNEW_MM.md" target="_blank">迁移说明</a>以亲自试用。</p> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">在您的项目中试用新版内存管理器以了解其运作方式，并在我们的问题跟踪器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FKT-48525" target="_blank">YouTrack</a> 中分享您的反馈。</p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:start">JS 和 Native 中的命名捕获组支持</h2> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">从 Kotlin 1.7.0-Beta 起，不仅在 JVM（1.8 及更高版本）上支持，在 JS 和 Native 上也将支持命名捕获组。</p> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">要为捕获组命名，请在正则表达式中使用 <code>(?<name>group)</code> 语法。 要获取组匹配的文本，请调用新引入的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fapi%2Flatest%2Fjvm%2Fstdlib%2Fkotlin.text%2Fget.html" target="_blank"><code>MatchGroupCollection.get()</code></a> 函数并传递组名。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">按名称检索匹配的组值</h3> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">请思考这个匹配城市坐标的示例。 要获取正则表达式匹配的组的集合，请使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fapi%2Flatest%2Fjvm%2Fstdlib%2Fkotlin.text%2F-match-result%2Fgroups.html" target="_blank"><code>groups</code></a>。 比较使用 <code>value</code> 按组的编号（索引）和按组的名称来检索组的内容：</p> 
<div style="text-align:start"> 
 <div> 
  <div> 
   <div> 
    <div> 
     <div> 
      <pre><code>fun main() &#123;
    val regex = "\\b(?<city>[A-Za-z\\s]+),\\s(?<state>[A-Z]&#123;2&#125;):\\s(?<areaCode>[0-9]&#123;3&#125;)\\b".toRegex()
    val input = "Coordinates: Austin, TX: 123"
 
    val match = regex.find(input)!!
    println(match.groups["city"]?.value) // "Austin" — by name
    println(match.groups[2]?.value) // "TX" — by number
&#125;</code></pre> 
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:start">命名向后引用</h3> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">现在，您在向后引用组时还可以使用组名。 向后引用会匹配捕获组先前匹配的相同文本。 为此，请在正则表达式中使用 <code>\k<name></code> 语法：</p> 
<div style="text-align:start"> 
 <div> 
  <div> 
   <div> 
    <div> 
     <div> 
      <pre><code>fun backRef() &#123;
    val regex = "(?<title>\\w+), yes \\k<title>".toRegex()
    val match = regex.find("Do you copy? Sir, yes Sir!")!!
    println(match.value) // "Sir, yes Sir"
    println(match.groups["title"]?.value) // "Sir"
&#125;</code></pre> 
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:start">替换表达式中的命名组</h3> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">最后，命名组引用可以与替换表达式一起使用。 请思考用于将输入中出现的所有正则表达式替换为替换表达式的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fapi%2Flatest%2Fjvm%2Fstdlib%2Fkotlin.text%2F-regex%2Freplace.html" target="_blank"><code>replace()</code></a> 函数，以及仅交换第一个匹配项的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fapi%2Flatest%2Fjvm%2Fstdlib%2Fkotlin.text%2F-regex%2Freplace-first.html" target="_blank"><code>replaceFirst()</code></a> 函数。</p> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">替换字符串中出现的各个 <code>$&#123;name&#125;</code> 会被替换为与具有指定名称的捕获组对应的子序列。 比较按名称和按索引替换组引用：</p> 
<div style="text-align:start"> 
 <div> 
  <div> 
   <div> 
    <div> 
     <div> 
      <pre><code>fun dateReplace() &#123;
    val dateRegex = Regex("(?<dd>\\d&#123;2&#125;)-(?<mm>\\d&#123;2&#125;)-(?<yyyy>\\d&#123;4&#125;)")
    val input = "Date of birth: 27-04-2022"
    println(dateRegex.replace(input, "\$&#123;yyyy&#125;-\$&#123;mm&#125;-\$&#123;dd&#125;")) // "Date of birth: 2022-04-27"  — by name
    println(dateRegex.replace(input, "\$3-\$2-\$1")) // "Date of birth: 2022-04-27" — by number
&#125;</code></pre> 
      <h2>试用新功能并提供反馈</h2> 
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">您可以在 1.7.0 预览版 Kotlin 1.7.0-Beta 中使用这些新功能。 您可以轻松地将它安装在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com.cn%2Fidea%2Fdownload%2F" target="_blank">IntelliJ IDEA</a> 或 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fstudio%2Fpreview" target="_blank">Android Studio</a> IDE 中。</p> 
<div style="margin-right:0px; text-align:left"> 
 <p style="margin-left:0; margin-right:0">由于 Android Studio 插件重命名（测试版），支持在 1.6.20 及后续版本中安装插件。</p> 
</div> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">请通过以下任一方式安装 Kotlin 1.7.0-Beta：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>如果您使用<em>抢先体验预览</em>更新通道，IDE 将在 1.7.0-Beta 可用时立即建议自动更新至该版本。</li> 
 <li>如果您使用<em>稳定版</em>更新通道，则可以随时在您的 IDE 中选择 <strong>Tools</strong> | <strong>Kotlin</strong> | <strong>Configure Kotlin Plugin Updates</strong>（工具 | Kotlin | 配置 Kotlin 插件更新）以切换至<em>抢先体验预览</em>通道。 然后，您将能够安装最新的预览版。 请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fdocs%2Finstall-eap-plugin.html" target="_blank">这些说明</a>以了解详情。</li> 
</ul> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">您可以随时下载这些 IDE 的最新版本以保证对 Kotlin 的全面支持：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com.cn%2Fidea%2Fdownload%2F" target="_blank">IntelliJ IDEA</a> – 用于为不同平台开发 Kotlin 应用程序。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fstudio%2Fpreview" target="_blank">Android Studio</a> – 用于开发 Android 和跨平台移动应用程序。</li> 
</ul> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">完成 1.7.0-Beta 安装后，不要忘记在您的构建脚本中<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fdocs%2Fconfigure-build-for-eap.html" target="_blank">将 Kotlin 版本更改</a>为 1.7.0-Beta。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">如果您遇到任何问题：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>向<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotl.in%2Fissue" target="_blank">我们的问题跟踪器 YouTrack</a> 报告问题。</li> 
 <li>在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fapp.slack.com%2Fclient%2FT09229ZC6%2FC0KLZSCHF" target="_blank">Kotlin Slack 中的 #eap 频道</a>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsurveys.jetbrains.com%2Fs3%2Fkotlin-slack-sign-up" target="_blank">获得邀请</a>）中获取帮助。</li> 
 <li>回滚到最新的稳定版本。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fdocs%2Finstall-eap-plugin.html%23if-you-run-into-any-problems" target="_blank">了解方法</a>。</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">阅读更多</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fdocs%2Feap.html" target="_blank">参与抢先体验预览</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fdocs%2Froadmap.html" target="_blank">Kotlin 路线图</a></li> 
</ul>
                                        </div>
                                      
</div>
            