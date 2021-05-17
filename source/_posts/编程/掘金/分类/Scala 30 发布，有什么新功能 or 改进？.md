
---
title: 'Scala 3.0 发布，有什么新功能 or 改进？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4232'
author: 掘金
comments: false
date: Mon, 17 May 2021 00:44:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=4232'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<p>Scala 发布 3.0 版本带来许多功能改进&新功能。</p>
</blockquote>
<p>即将到来的、令人兴奋的Scala 3新版本带来了许多改进和新功能。在这里，我们为你提供一个最重要变化的快速概述。如果你想深入挖掘，还有一些参考资料供你使用。</p>
<ul>
<li><a href="https://docs.scala-lang.org/scala3/book/introduction.html" target="_blank" rel="nofollow noopener noreferrer">The Scala 3 Book</a>：针对的是刚接触Scala语言的开发者。</li>
<li><a href="https://dotty.epfl.ch/docs/reference/syntax.html" target="_blank" rel="nofollow noopener noreferrer">语法概要</a>：为你提供了新语法的正式描述。</li>
<li><a href="https://dotty.epfl.ch/docs/reference/overview.html" target="_blank" rel="nofollow noopener noreferrer">语言参考</a>： 详细描述了从Scala 2到Scala 3 的变化。</li>
<li><a href="https://docs.scala-lang.org/scala3/guides/migration/compatibility-intro.html" target="_blank" rel="nofollow noopener noreferrer">迁移指南</a> ：为你提供了从Scala 2迁移到Scala 3的所有必要信息。</li>
</ul>
<h2 data-id="heading-0">Scala 3 的新内容</h2>
<p>Scala 3是对Scala语言的一次彻底改造。在其核心部分，类型系统的许多方面都被改变了，变得更加原则化。虽然这也带来了令人兴奋的新功能（比如联合类型），但首先意味着类型系统（甚至）更少地妨碍你，例如<a href="https://dotty.epfl.ch/docs/reference/changed-features/type-inference.html" target="_blank" rel="nofollow noopener noreferrer">类型推理</a>和重载解决都得到了很大的改善。</p>
<h3 data-id="heading-1">语法改进</h3>
<p>除了许多（小的）清理，Scala 3的语法还提供了以下改进。</p>
<ul>
<li>为控制结构提供了一种新的 "安静 "语法，如<code>if</code>,<code>while</code>, 和<code>for</code> <a href="https://dotty.epfl.ch/docs/reference/other-new-features/control-syntax.html" target="_blank" rel="nofollow noopener noreferrer">（新的控制语法</a></li>
<li><code>new</code> 关键字是可选的_（又称_ <a href="https://dotty.epfl.ch/docs/reference/other-new-features/creator-applications.html" target="_blank" rel="nofollow noopener noreferrer">创作者应用</a>）。</li>
<li><a href="https://dotty.epfl.ch/docs/reference/other-new-features/indentation.html" target="_blank" rel="nofollow noopener noreferrer">可选的大括号</a>，支持无干扰、缩进敏感的编程风格</li>
<li>将<a href="https://dotty.epfl.ch/docs/reference/changed-features/wildcards.html" target="_blank" rel="nofollow noopener noreferrer">类型级通配符</a>从<code>_</code> 改为<code>?</code> 。</li>
<li>Implicits（和它们的语法）被<a href="https://dotty.epfl.ch/docs/reference/contextual/motivation.html" target="_blank" rel="nofollow noopener noreferrer">大量修改</a>。</li>
</ul>
<h3 data-id="heading-2">上下文抽象</h3>
<p>Scala的一个基本核心概念是（在某种程度上仍然是）为用户提供一小部分强大的功能，这些功能可以被组合成巨大的（有时甚至是不可预见的）表达能力。例如隐含的特性被用来模拟上下文抽象、表达类型级计算、模拟类型类、执行隐式强制、编码扩展方法等等。 从这些用例中学习，Scala 3采取了一个稍微不同的方法，关注<strong>意图</strong>而不是<strong>机制</strong>。 Scala 3没有提供一个非常强大的特性，而是提供多个定制的语言特性，允许程序员直接表达他们的意图。</p>
<ul>
<li>
<p><strong>在上下文信息</strong>上进行缩减。<a href="https://dotty.epfl.ch/docs/reference/contextual/using-clauses.html" target="_blank" rel="nofollow noopener noreferrer">使用子句</a>允许程序员对调用上下文中可用的信息进行抽象，这些信息应该以隐式方式传递。作为对Scala 2隐含信息的改进，使用子句可以按类型指定，将函数签名从从未明确提及的术语变量名中解放出来。</p>
</li>
<li>
<p><strong>提供类型类实例</strong>。<a href="https://dotty.epfl.ch/docs/reference/contextual/givens.html" target="_blank" rel="nofollow noopener noreferrer">给定实例</a>允许程序员定义某种类型的_典型值_。这使得使用类型类的编程更加直接，而不会泄露实现细节。</p>
</li>
<li>
<p><strong>追溯性地扩展类</strong>。在Scala 2中，扩展方法必须使用隐式转换或隐式类进行编码。相比之下，在Scala 3中，<a href="https://dotty.epfl.ch/docs/reference/contextual/extension-methods.html" target="_blank" rel="nofollow noopener noreferrer">扩展方法</a>现在直接内置于语言中，导致更好的错误信息和改进的类型推理。</p>
</li>
<li>
<p><strong>将一种类型视为另一种类型</strong>。隐式转换已经被<a href="https://dotty.epfl.ch/docs/reference/contextual/conversions.html" target="_blank" rel="nofollow noopener noreferrer">重新设计</a>为类型类的实例<code>Conversion</code> 。</p>
</li>
<li>
<p><strong>更高阶的上下文抽象</strong>。<a href="https://dotty.epfl.ch/docs/reference/contextual/context-functions.html" target="_blank" rel="nofollow noopener noreferrer">上下文函数</a>的_全新_特性使上下文抽象成为一流的公民。它们是库作者的一个重要工具，允许表达简洁的特定领域语言。</p>
</li>
<li>
<p><strong>来自编译器的可操作反馈</strong>。如果一个隐式参数不能被编译器解决，它现在会提供可能解决这个问题的<a href="https://www.scala-lang.org/blog/2020/05/05/scala-3-import-suggestions.html" target="_blank" rel="nofollow noopener noreferrer">导入建议</a>。</p>
</li>
</ul>
<h3 data-id="heading-3">类型系统改进</h3>
<p>除了极大地改进了类型推理，Scala 3的类型系统还提供了许多新的功能，为你提供了强大的工具来静态地表达类型中的不变量。</p>
<ul>
<li>
<p><strong>枚举</strong>。<a href="https://dotty.epfl.ch/docs/reference/enums/enums.html" target="_blank" rel="nofollow noopener noreferrer">枚举</a>已经被重新设计，以便与案例类很好地融合，并形成表达<a href="https://dotty.epfl.ch/docs/reference/enums/adts.html" target="_blank" rel="nofollow noopener noreferrer">代数数据类型</a>的新标准。</p>
</li>
<li>
<p>不透明的<strong>类型</strong>。隐藏在<a href="https://dotty.epfl.ch/docs/reference/other-new-features/opaques.html" target="_blank" rel="nofollow noopener noreferrer">不透明类型别名</a>后面的实现细节，而不需要为它的性能付出代价!不透明类型取代了值类，并允许你建立一个抽象的屏障，而不会造成额外的装箱开销。</p>
</li>
<li>
<p><strong>交叉和联合类型</strong>。将类型系统建立在新的基础上导致了新的类型系统特征的引入：<a href="https://dotty.epfl.ch/docs/reference/new-types/intersection-types.html" target="_blank" rel="nofollow noopener noreferrer">交叉类型</a>的实例，如<code>A & B</code> ，是<code>A</code> <em>和</em> <code>B</code> 的实例。<a href="https://dotty.epfl.ch/docs/reference/new-types/union-types.html" target="_blank" rel="nofollow noopener noreferrer">联合类型</a>的实例，如<code>A | B</code> ，是<code>A</code> 或<code>B</code> 的实例_。_这两个结构允许程序员在继承层次结构之外灵活地表达类型约束。</p>
</li>
<li>
<p><strong>从属函数类型</strong>。Scala 2已经允许返回类型依赖于（值）参数。在Scala 3中，现在可以对这种模式进行抽象，表达<a href="https://dotty.epfl.ch/docs/reference/new-types/dependent-function-types.html" target="_blank" rel="nofollow noopener noreferrer">依赖性的函数类型</a>。在类型<code>type F = (e: Entry) => e.Key</code> ，结果类型_取决于_参数</p>
</li>
<li>
<p><strong>多态的函数类型</strong>。和从属函数类型一样，Scala 2支持允许类型参数的方法，但不允许程序员对这些方法进行抽象。在Scala 3中，<a href="https://dotty.epfl.ch/docs/reference/new-types/polymorphic-function-types.html" target="_blank" rel="nofollow noopener noreferrer">多态函数类型</a>（如<code>[A] => List[A] => List[A]</code> ）可以抽象出除值参数外还接受_类型_参数的函数。</p>
</li>
<li>
<p><strong>Type lambdas</strong>。在Scala 2中需要用<a href="https://github.com/typelevel/kind-projector" target="_blank" rel="nofollow noopener noreferrer">编译器插件</a>来表达的功能，现在在Scala 3中成为了一流的功能：Type lambdas是类型级别的函数，可以作为（更高类型的）类型参数传递，而不需要辅助的类型定义。</p>
</li>
<li>
<p><strong>匹配类型</strong>。Scala 3提供了对类型<a href="https://dotty.epfl.ch/docs/reference/new-types/match-types.html" target="_blank" rel="nofollow noopener noreferrer">匹配</a>的直接支持，而不是使用隐式解析来编码类型级计算。将类型级计算集成到类型检查器中，可以改进错误信息，并消除对复杂编码的需求。</p>
</li>
</ul>
<h3 data-id="heading-4">重新设计了面向对象的编程</h3>
<p>Scala一直处于函数式编程和面向对象编程的前沿--而Scala 3在这两个方向上都推动了边界的发展!上述类型系统的变化和上下文抽象的重新设计使得_函数式编程_比以前更容易了。 同时，以下新特性使得结构良好的_面向对象设计_成为可能，并支持最佳实践。</p>
<ul>
<li><strong>传承</strong>。特质更接近于类，现在也可以接受<a href="https://dotty.epfl.ch/docs/reference/other-new-features/trait-parameters.html" target="_blank" rel="nofollow noopener noreferrer">参数</a>，使其作为模块化软件分解的工具更加强大。</li>
<li><strong>为扩展做计划</strong>。在面向对象的设计中，扩展那些不打算扩展的类是一个长期存在的问题。为了解决这个问题，<a href="https://dotty.epfl.ch/docs/reference/other-new-features/open-classes.html" target="_blank" rel="nofollow noopener noreferrer">开放类</a>要求库设计者_明确地_将类标记为开放。</li>
<li><strong>隐藏实现细节</strong>。实现行为的实用特征有时不应该是推断类型的一部分。在Scala 3中，这些特质可以被标记为<a href="https://dotty.epfl.ch/docs/reference/other-new-features/transparent-traits.html" target="_blank" rel="nofollow noopener noreferrer">透明的</a>，向用户隐藏继承性（在推断类型中）。</li>
<li><strong>构成高于继承</strong>。这句话经常被引用，但实现起来却很繁琐。Scala 3的<a href="https://dotty.epfl.ch/docs/reference/other-new-features/export.html" target="_blank" rel="nofollow noopener noreferrer">导出条款</a>则不然：与导入条款对称，导出条款允许用户为对象的选定成员定义别名。</li>
<li><strong>不再有NPEs</strong>。Scala 3比以往任何时候都更安全：<a href="https://dotty.epfl.ch/docs/reference/other-new-features/explicit-nulls.html" target="_blank" rel="nofollow noopener noreferrer">显式nulls</a>将<code>null</code> ，帮助你静态地捕捉错误；<a href="https://dotty.epfl.ch/docs/reference/other-new-features/safe-initialization.html" target="_blank" rel="nofollow noopener noreferrer">安全初始化</a>的额外检查可以检测对未初始化对象的访问。</li>
</ul>
<h3 data-id="heading-5">元编程</h3>
<p>Scala 2中的宏只是一个实验性的功能，而Scala 3为元编程提供了强大的工具库。<a href="https://docs.scala-lang.org/scala3/guides/macros/index.html" target="_blank" rel="nofollow noopener noreferrer">宏教程</a>中包含了不同设施的详细信息。特别是，Scala 3为元编程提供了以下功能。</p>
<ul>
<li><strong>内联</strong>。作为基本的起点，<a href="https://docs.scala-lang.org/scala3/guides/macros/inline.html" target="_blank" rel="nofollow noopener noreferrer">内联功能</a>允许在编译时减少数值和方法。这个简单的功能已经涵盖了许多使用情况，同时也为更高级的功能提供了入口。</li>
<li><strong>编译时操作</strong>。该包 <a href="https://docs.scala-lang.org/scala3/guides/macros/compiletime.html" target="_blank" rel="nofollow noopener noreferrer"><code>scala.compiletime</code></a>包含了额外的功能，可以用来实现内联方法。</li>
<li><strong>引述代码块</strong>。Scala 3增加了代码<a href="https://docs.scala-lang.org/scala3/guides/macros/quotes.html" target="_blank" rel="nofollow noopener noreferrer">准引号</a>的新功能，为构建和分析代码提供了方便的高级接口。构建加一加的代码就像<code>'&#123; 1 + 1 &#125;</code> 一样简单。</li>
<li><strong>反射API</strong>。对于更高级的用例，<a href="https://docs.scala-lang.org/scala3/guides/macros/reflection.html" target="_blank" rel="nofollow noopener noreferrer">quotes.</a>reflect提供了更详细的控制来检查和生成程序树。</li>
</ul>
<p>如果你想进一步了解Scala 3中的元编程，我们邀请你参加我们的<a href="https://docs.scala-lang.org/scala3/guides/macros/index.html" target="_blank" rel="nofollow noopener noreferrer">教程</a>。</p></div>  
</div>
            