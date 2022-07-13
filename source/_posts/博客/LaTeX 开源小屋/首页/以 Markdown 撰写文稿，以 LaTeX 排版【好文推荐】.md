
---
title: '以 Markdown 撰写文稿，以 LaTeX 排版【好文推荐】'
categories: 
 - 博客
 - LaTeX 开源小屋
 - 首页
headimg: 'https://picsum.photos/400/300?random=2074'
author: LaTeX 开源小屋
comments: false
date: Mon, 13 Apr 2020 22:50:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=2074'
---

<div>   
<p>
                                                        </p><p>回顾我学习和使用 LaTeX 的经历，有几个时间节点让我感触颇深：</p><ul class=" list-paddingleft-2"><li><p>初次接触 LaTeX 时，感受到它对样式强大的控制能力和对数学公式的排版能力，心中对 Microsoft Word 颇有愤懑。</p></li><li><p>熟练使用 LaTeX 后，困于 LaTeX 中过于强大的样式控制能力带来的复杂性与笔记等需要速记的场景之间难以调和的矛盾。</p></li><li><p>初次接触 Markdown 时，感受到它在内容和样式之间取得了比较好的平衡。它的样式可以用 CSS 来控制。</p></li><li><p>折腾 Sphinx、Pandoc 等工具尝试将 Markdown 文稿转换为 LaTeX 文稿时，对这些工具的转换效果和细节问题感到崩溃。</p></li></ul><p>在这之后很多年里，我一直期待能有一个工具，能够更好地平衡 Markdown 的便捷性和 LaTeX 对样式的控制能力和对数学公式的排版能力。前几天，我发现了 <code>markdown</code> 宏包。我认为已找到了这样梦想中的工具。并且，我认为在熟练使用它之后，可以更好地实现 LaTeX 设计之初的愿望：<a href="https://liam.page/2019/03/18/separation-of-content-and-presentation/">内容与样式分离</a>。</p><blockquote><p>本文又名：「你喜爱的 Markdown 写作，现更以 LaTeX 呈现」。<br>——来自 <a href="https://harrychen.xyz/" target="_blank">Harry Chen</a> 的 Apple 风格标题。</p></blockquote><h2>介绍</h2><p><a href="https://ctan.org/pkg/markdown" target="_blank">markdown 宏包</a>是 Vít Novotný 维护的一个宏包。它的核心机制使用 Lua 编写，同时提供了针对 Plain TeX/LaTeX/ConTeXt 等格式的接口。由于现代 TeX 发行版（TeX Live、MiKTeX 等）通常都包含了 Lua 解释器，因而使用 <code>markdown</code> 宏包通常无需额外安装其他工具，只需打开 <code>--shell-escape</code> 标记即可（LuaLaTeX 除外）。相对 Sphinx、Pandoc 等第三方工具以及之前社区实现的其他类似功能的宏包，这算是一个飞跃式的进步。</p><p><code>markdown</code> 的环境和 <code>\markdownInput</code> 的命令。前者用于在 LaTeX 文稿中直接书写 Markdown 标记内容，后者用于从 Markdown 文件中读入内容。<code>markdown</code> 宏包会在遇到 <code>markdown</code> 环境或者 <code>\markdownInput</code> 命令时，将相应内容交由 Lua 解释器处理，从而将内容翻译成一堆预定义好的 LaTeX 宏。由于这个步骤需要调用 Lua 解释器，故而需要打开 <code>--shell-escape</code> 标记；当然，如果使用 LuaLaTeX 的话，因为直接能交给 Lua 解释器处理，故而不需要打开 <code>--shell-escape</code>。而后，TeX 引擎会读入这些翻译得到的 LaTeX 宏，进行正常的 LaTeX 处理。</p><p>对于常见的 Markdown 功能，<code>markdown</code> 宏包都预设了 LaTeX 宏相应的实现。例如 <code>\markdownRendererImage</code> 是用来渲染图片的宏，当解析到 <code>![imagelabel](imagepath "image caption")</code> 时，Lua 解释器就会使用这个宏来拼接得到翻译结果：<code>\markdownRendererImage&#123;imagelabel&#125;&#123;imagepath&#125;&#123;imagepath&#125;&#123;image caption&#125;</code>。而后，根据 <code>\markdownRendererImage</code> 的定义，TeX 引擎会在后续步骤展开这个宏，再去排版得到相应的结果。</p><p><br></p><p>具体内容看看这里吧：</p><p><a href="https://liam.page/2020/03/30/writing-manuscript-in-Markdown-and-typesetting-with-LaTeX/">https://liam.page/2020/03/30/writing-manuscript-in-Markdown-and-typesetting-with-LaTeX/</a></p><p><br></p>                        <p></p>
                        <!-- E 正文 -->
                      
</div>
            