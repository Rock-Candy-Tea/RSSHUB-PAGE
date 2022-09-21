
---
title: 'Gleam v0.23 发布，Rust 编写的函数式编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0921/070205_9MWs_2720166.gif'
author: 开源中国
comments: false
date: Wed, 21 Sep 2022 07:05:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0921/070205_9MWs_2720166.gif'
---

<div>   
<div class="content">
                                                                                            <p>Gleam 是一种类型安全且可扩展的编程语言，可用于 Erlang 虚拟机和 JavaScript 运行时。</p> 
<p>最近发布的 0.23 版本增加了新特性，以及其他优化。</p> 
<ul> 
 <li><strong>支持 Elixir</strong></li> 
</ul> 
<p>Gleam 在 Erlang 虚拟机上与各种其他优秀编程语言一起运行，因此开发团队希望利用通过这些语言编写的所有包。</p> 
<p>以前使用 Gleam 构建工具的项目可能依赖于用 Gleam 或 Erlang 编写的包。从这个版本开始，还支持用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Felixir-lang.org%2F" target="_blank">Elixir</a> 编写的项目，让 Gleam 程序员可以访问几乎所有在 Erlang 生态的包管理器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhex.pm%2F" target="_blank">Hex 上找到的软件包。</a></p> 
<p>在 Gleam 中使用 Elixir 软件包的开发者体验与使用 Erlang 软件包相同。</p> 
<pre><code># Add an Elixir package to the Gleam project
$ gleam add tzdata</code></pre> 
<pre><code>// Import a function from the package
external fn tzdata_version() -> String =
  "Elixir.Tzdata" "tzdata_version"

// Use it in Gleam
pub fn main() &#123;
  io.println(tzdata_version())
&#125;</code></pre> 
<ul> 
 <li><strong>针对软件包升级的优化</strong></li> 
</ul> 
<p>开发团队希望尽可能简单地使用其他人编写的代码，并且希望避免“依赖地狱”，因此构建工具的用户体验是 Gleam 的一个重要领域。</p> 
<p>到目前为止，难题的一个缺失部分是升级项目所依赖的包版本——以前它在很大程度上是一个手动过程。</p> 
<p>在此版本中，有一个新<code>gleam update</code>命令将使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnex3.medium.com%2Fpubgrub-2fb6470504f" target="_blank">PubGrub</a> 算法有效地解析最新的兼容版本的依赖项。</p> 
<pre><code>$ gleam update
# Tada, you're on the latest versions!</code></pre> 
<ul> 
 <li><strong>优化文档</strong></li> 
</ul> 
<p>Gleam 为软件包生成文档并将 HTML 发布到 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhexdocs.pm%2F" target="_blank">HexDocs</a>，这是 Erlang 生态的文档站点。</p> 
<p>在此版本中，生成的文档包括一个搜索栏，因此可以比以往更轻松地更快地找到函数、类型和模块。该搜索由<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flunrjs.com%2F" target="_blank">Lunr</a> JavaScript 库提供支持，因此支持模糊匹配以帮助解决拼写错误，或者不太记得所需要查询的名称。</p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0921/070205_9MWs_2720166.gif" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgleam.run%2Fnews%2Fgleam-v0.23-released%2F" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            