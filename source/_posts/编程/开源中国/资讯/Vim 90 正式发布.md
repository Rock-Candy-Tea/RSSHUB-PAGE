
---
title: 'Vim 9.0 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9562'
author: 开源中国
comments: false
date: Wed, 29 Jun 2022 07:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9562'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <p>将 Vim 9.0 版本献给 <a href="https://www.oschina.net/news/183696/vim-main-promoter-programmer-sven-guckes-passed-away">Sven Guckes</a>，他于 2022 年 2 月去世。Sven 是 Vim 的核心维护者，他注册了 vim.org 域名并创建了第一个 Vim 网站，我们将以此纪念他。</p> 
</blockquote> 
<p>经过多年的逐步改进，Vim 现在推出了一个重要版本，向前迈出了一大步。除了许多小的补充改进之外，该版本的重点是 Vim 脚本语言的一个新的变化：Vim9 Script。</p> 
<p>上一个版本是 2019 年 12 月发布的 8.2 版。由于最新的源代码总是会在 GitHub 上提供，因此许多用户已经安装了后来的补丁版本（有超过 5000 个），这些变化也已经被许多用户试用过了。在 8.2 的基础上，许多错误得到了修复、安全问题得到了解决，代码覆盖率得到了极大的提升。这个版本比以前的任何版本都更可靠。</p> 
<h3>Vim9 Script</h3> 
<p>Vim 的脚本随着时间的推移而不断发展，同时保留了向后的兼容性。这意味着过去的错误选择往往无法改变，与 Vi 的兼容性也限制了可能的解决方案。因此执行速度相当慢，每次执行时都要对每一行进行解析。</p> 
<p>Vim9 Script 的主要目标是极大地提高性能。这是通过将命令编译成可以有效执行的指令来实现的，执行速度有望提高 10 到 100 倍。</p> 
<p>Vim9 Script 的次要目标是避免 Vim 特有的结构，使其更接近于常用的编程语言，如 JavaScript、TypeScript 和 Java。</p> 
<p>性能的提高只能通过<strong>不 100%</strong> 向后兼容来实现。例如，通过创建一个 "a: " 字典使函数参数可用涉及到相当多的开销，在 Vim9 函数中，这个字典不再可用。</p> 
<p>对于那些有大量传统脚本的开发者来说也不用过于担心，这些脚本依然可以像以前一样使用。目前没有计划放弃对传统脚本的支持，变化不会像 Python 2 到 Python 3 那样剧烈。</p> 
<h3>有趣的功能</h3> 
<p>为了从加速中获益，一个函数必须用 <code>def</code> 来定义，必须指定参数和返回类型。这不仅是为了使执行速度更快，也有助于在函数被编译成字节码时及早发现错误。变量需要用 <code>var</code> 来声明的，并且也有一个类型，可以是明确的，也可以是从分配的值中推断出来的。</p> 
<p>行的延续不需要使用反斜杠，这是在传统脚本中使用的机制。</p> 
<p>函数调用不需要 <code>call</code>，赋值不需要 <code>let</code>，表达式的求值不需要 <code>eval</code>。这使得 Vim9 Script 看起来更像大多数编程语言。</p> 
<p>将一个大的脚本分割成小块如今也变得简单多了。在一个脚本中， <code>export</code> 被用来使特定的函数和变量对其他脚本可用，然后在需要使用导出的项目的地方使用 <code>import</code>。结合自动加载机制，这为实现大型插件带来了一种灵活而强大的方式。</p> 
<p>现在注释以 <code>#</code> 开头。以前的双引号语法来自古老的 Vi，会干扰字符串的使用。在许多其他语言中，例如 Python 和 shell 脚本，都知道 <code>#</code> 的含义。</p> 
<h3>未来的工作</h3> 
<p>在 Vim9 Script 的计划之一是添加类，虽然可以用字典来模拟，但这还远远不够理想。大多数程序员都熟悉类，在 Vim9 Script 中也应该加入这样的东西，目前关键字已经被保留。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.vim.org%2Fvim90.php" target="_blank">https://www.vim.org/vim90.php</a></p>
                                        </div>
                                      
</div>
            