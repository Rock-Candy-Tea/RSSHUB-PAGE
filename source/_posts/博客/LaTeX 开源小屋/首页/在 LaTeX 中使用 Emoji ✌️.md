
---
title: '在 LaTeX 中使用 Emoji ✌️'
categories: 
 - 博客
 - LaTeX 开源小屋
 - 首页
headimg: 'https://picsum.photos/400/300?random=5794'
author: LaTeX 开源小屋
comments: false
date: Sat, 07 Mar 2020 09:05:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=5794'
---

<div>   
<p>
                                                        </p><p>Emoji（絵え文も字じ）是聊天软件和社交平台的常客，也几乎成为了一种新的「世界语」。虽然 LATEX 以排版严肃的学术类文章见长，但偶尔卖个萌也不为过。</p><h2>背景<a href="https://stone-zeng.github.io//2020-02-28-latex-emoji/#%E8%83%8C%E6%99%AF"></a></h2><p>Emoji 其实是文字的一种，换句话说它们是对应有 Unicode 码位的。而微信、QQ 等聊天工具，为了抹平平台差异以防出现歧义，实际上是用了自己的一套东西，复制出去就会原形毕露，得到 [奸笑]、[旺柴] 这样的字符串。</p><p>在之前引擎没有支持的时候，也有人在 LATEX 中实现过类似的想法，即先把 emoji 导出为图片，再通过一些命令插入，比如：</p><ul style="margin-bottom: 15px;margin-left: 2em;padding: 0px;color: rgb(76, 76, 76);font-family: Inter, 'Source Han Sans SC', 'Noto Sans CJK SC', source-han-sans-cjk-sc, sans-serif;white-space: normal;background-color: rgb(253, 253, 253)" class=" list-paddingleft-2"><li><p><a href="https://ctan.org/pkg/coloremoji">coloremoji</a>（MiK­TEX 已收录）</p></li><li><p><a href="https://github.com/doraTeX/coloremoji">https://github.com/doraTeX/coloremoji</a></p></li><li><p><a href="https://github.com/henningpohl/latex-emoji">https://github.com/henningpohl/latex-emoji</a></p></li></ul><p>这样的机制虽然简单可靠，但毕竟插图不是文字，过多的图片不便于下载和交换（完整的支持至少需要近千个图片文件，这恐怕也是 TEX Live 不收录的原因），也不能自由地切换样式（字体）。不过，Lua­TEX 最近加入了一些功能，使得我们现在也可以在 LATEX 中以字体的形式直接使用 emoji。</p><h2>基本方法<a href="https://stone-zeng.github.io//2020-02-28-latex-emoji/#%E5%9F%BA%E6%9C%AC%E6%96%B9%E6%B3%95"></a></h2><p>2019 年，Luigi Scarso 等人为 Lua­TEX 添加了 HarfBuzz 库支持，构建了另一个分支 LuaHB­TEX。随后，LATEX 的开发版本就改用它代替原来的 Lua­TEX；在 TEX Live 2020 中 LuaHB­TEX 也将成为默认的 Lua­TEX 引擎。因此，为了使用 emoji 字体，我们需要改用 lualatex-dev 命令编译。</p><p>另一方面，显示 emoji 还需有字体的支持。主流操作系统都配有设计精良的字体：</p><ul style="margin-bottom: 15px;margin-left: 2em;padding: 0px;color: rgb(76, 76, 76);font-family: Inter, 'Source Han Sans SC', 'Noto Sans CJK SC', source-han-sans-cjk-sc, sans-serif;white-space: normal;background-color: rgb(253, 253, 253)" class=" list-paddingleft-2"><li><p>Windows 中是 Segoe UI Emoji</p></li><li><p>macOS 中是 Apple Color Emoji</p></li><li><p>Ubuntu 等 Linux 系统大多配有开源的 Noto Color Emoji</p></li></ul><p>在最新版的 TEX Live 中，则包含有 Twemoji Mozilla 和 Noto Color Emoji，它们均是开源免费的。</p><p>与普通字体类似，我们可以使用 fontspec 提供的命令来声明字体，但注意需要加上选项 Renderer=HarfBuzz<a href="https://stone-zeng.github.io//2020-02-28-latex-emoji/#fn:twemoji">[1]</a>。在文档中直接输入想要的表情，就可以使用了：</p><pre class="brush:bash;toolbar:false">\documentclass&#123;article&#125;
\usepackage&#123;fontspec&#125;
\newfontface\EmojiFont&#123;Twemoji Mozilla&#125;[Renderer=HarfBuzz]
\begin&#123;document&#125;The cat eats apple:  &#123;\EmojiFont</pre>                        <p></p>
                        <!-- E 正文 -->
                      
</div>
            