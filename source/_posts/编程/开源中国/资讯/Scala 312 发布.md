
---
title: 'Scala 3.1.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8638'
author: 开源中国
comments: false
date: Wed, 27 Apr 2022 07:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8638'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">Scala 3.1.2 已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.scala-lang.org%2Fblog%2F2022%2F04%2F12%2Fscala-3.1.2-released.html" target="_blank">发布</a>，这个新版本带来了一些社区所期待的重大改进。具体更新亮点有：</span></p> 
<h4><span style="color:#000000"><strong>可配置的 Scala output version</strong></span></h4> 
<p><span style="color:#000000">新版本带来了一种实验性的配置 Scala output version 的可能性。这意味着编译器现在可以生成 TASTy 文件和 classfiles，其格式由较早的 Scala 小版本使用（目前只能是 3.0.x），有效地指定了能够阅读你的编译代码的最小版本的编译器。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">使用 Scala 3.1.2 编译库时，可以将 output version 设置为 Scala 3.0。然后，你的库可以被使用 Scala 3.0、3.1 或任何未来版本编译的代码使用。所有生成的 TASTy 文件都将与 Scala 3.0 和更高版本兼容。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">虽然编译器设置本身没有明确标记为实验性（其相应的标志在其名称中没有<code class="language-plaintext">-X</code>或<code class="language-plaintext">-Y</code>前缀），但它在更广泛的 Scala 库生态系统中的作用尚未确定。官方表示，其正等待着库的维护者的反馈。希望听取大众的意见以促使选择正确的策略来支持为以前的 Scala 版本编译的代码，以便可以在兼容性和语言发展的可能性之间找到平衡。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000"><strong>Current support</strong></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">你可以通过使用一个新的编译器标志来设置 Scala output version，该标志名为 -scala-output-version，并以一个次要的发布版本作为参数。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">从 1.7.0-M1 版本开始，有一个 scalaOutputVersion，它不仅可以设置编译器标志，还可以决定哪个版本的标准库将被指定为你项目的依赖。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">scalaOutputVersion <span style="background-color:#ffffff">被设计为在你仍然被迫交叉编译的情况下也能顺利工作（例如，如果你的项目包含宏但你想同时支持 Scala 2 和 3）。在这种情况下，如果 scalaVersion 中的编译器还不支持 -scala-output-version 标志，你只需要确保 scalaOutputVersion 被设置为与 scalaVersion 相同的值（相当于不定义 scalaOutputVersion）。例如</span></span></p> 
<pre><code><span>ThisBuild</span> <span>/</span> <span>scalaVersion</span> <span>:=</span> <span>"3.1.2"</span>
<span>ThisBuild</span> <span>/</span> <span>crossScalaVersions</span> <span>:=</span> <span>List</span><span>(</span><span>"2.13.8"</span><span>,</span> <span>"3.1.2"</span><span>)</span>
<span>ThisBuild</span> <span>/</span> <span>scalaOutputVersion</span> <span>:=</span> <span>&#123;</span>
  <span>CrossVersion</span><span>.</span><span>partialVersion</span><span>(</span><span>scalaVersion</span><span>.</span><span>value</span><span>)</span> <span>match</span> <span>&#123;</span>
    <span>case</span> <span>Some</span><span>((</span><span>3</span><span>,</span> <span>_</span><span>))</span> <span>=></span> <span>"3.0.2"</span>
    <span>case</span> <span>_</span> <span>=></span> <span>scalaVersion</span><span>.</span><span>value</span>
  <span>&#125;</span>
<span>&#125;</span></code></pre> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000"><strong>对其他兼容性标志的修改</strong></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">目前的 output compatibility flags 有一些混乱，增加一个新的标志只会使情况更糟。因此，官方决定重新命名现有的标志。-release 现在是 -java-output-version，而- Xtarget 是 -Xunchecked-java-output-version。为了兼容起见，旧的名字被保留为别名。</span></p> 
<h4><span style="color:#000000">其他改进</span></h4> 
<ul> 
 <li><span style="color:#000000">现在你可以在编译过程中传递 -Xmacro-settings 标志，以自定义代码中的宏的行为。这个功能仍然是试验性的。例如，你可以用 -Xmacro-settings:present,key=value 编译以下代码：</span></li> 
</ul> 
<pre><code><span>//> using options "-Xmacro-settings:present,key=value"</span>

<span>import</span> <span>scala.quoted.</span><span>*</span>

<span>inline</span> <span>def</span> <span>customizable</span> <span>=</span> <span>$</span><span>&#123;</span> <span>customizableImpl</span> <span>&#125;</span>

<span>def</span> <span>customizableImpl</span><span>(</span><span>using</span> <span>Quotes</span><span>)</span> <span>=</span>
  <span>import</span> <span>quotes.reflect.</span><span>*</span>
  <span>val</span> <span>settings</span> <span>=</span> <span>CompilationInfo</span><span>.</span><span>XmacroSettings</span>

  <span>val</span> <span>present</span>    <span>=</span> <span>settings</span><span>.</span><span>contains</span><span>(</span><span>"present"</span><span>)</span>       <span>// true</span>
  <span>val</span> <span>notPresent</span> <span>=</span> <span>settings</span><span>.</span><span>contains</span><span>(</span><span>"not-present"</span><span>)</span>   <span>// false</span>
  <span>val</span> <span>withValue</span>  <span>=</span> <span>settings</span><span>.</span><span>collectFirst</span> <span>&#123;</span>            <span>// Some("value")</span>
    <span>case</span> <span>s</span><span>"key=$value"</span> <span>=></span> <span>value</span>
  <span>&#125;</span>

  <span>???</span> <span>// Do something fancy with your settings</span></code></pre> 
<ul> 
 <li>你可以用 -e flag 运行 scala 命令，从命令行快速执行 Scala 语句。</li> 
</ul> 
<div> 
 <div> 
  <pre><code>  scala <span>-e</span> <span>"println(22*38)"</span>
</code></pre> 
 </div> 
</div> 
<p style="color:#4a5659; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">将在 standard output 上 print 836，并退出 Scala 进程。</span></p> 
<ul> 
 <li><span style="color:#000000">在 typer 中有一些新的优化，在某些情况下可能会导致显著的速度提升。你可以在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flampepfl%2Fdotty%2Fpull%2F13637" target="_blank">相关的 PR 中</a>找到更多信息和基准测试结果。</span></li> 
</ul> 
<p><span style="color:#000000">更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.scala-lang.org%2Fblog%2F2022%2F04%2F12%2Fscala-3.1.2-released.html" target="_blank">查看官方博客</a>。</span></p>
                                        </div>
                                      
</div>
            