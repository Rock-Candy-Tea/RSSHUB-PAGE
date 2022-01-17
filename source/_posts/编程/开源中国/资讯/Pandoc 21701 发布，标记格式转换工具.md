
---
title: 'Pandoc 2.17.0.1 发布，标记格式转换工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9332'
author: 开源中国
comments: false
date: Mon, 17 Jan 2022 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9332'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Pandoc 2.17.0.1 发布了<span style="color:#333333">，Pandoc 是一个通用标记转换 Haskell 库，用于从一种标记格式转换为另一种，同时也是一个使用该库的命令行工具，它可以转换 28 种标记格式。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">此版本带来如下修复：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>更新到 pandoc-lua-marshal 0.1.3.1，修复了导致 Lua stackoverflow<span> </span><code>List.includes</code><span> </span>和<span> </span><code>List.find</code><span> </span>后续程序崩溃的问题。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjgm%2Fpandoc%2Fissues%2F7831" target="_blank">#7831</a>）</li> 
 <li>HTML 模板：在 math 之前加载 header-includes（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjgm%2Fpandoc%2Fpull%2F7833" target="_blank">#7833</a>）。MathJax 期望在加载 MathJax 脚本之前配置，这种顺序更改允许通过 header-includes 配置 MathJax，详情可参阅<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjgm%2Fpandoc%2Fissues%2F2750" target="_blank">#2750</a><span> </span>。</li> 
 <li>读取默认文件时，停在一行<span> </span><code>...</code>。此行表示 YAML 文档的结束。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjgm%2Fpandoc%2Fissues%2F4627%23issuecomment-1012438765" target="_blank">#4627</a>） </li> 
 <li>Text.Pandoc.Citeproc：允许<code>notes-after-punctuation</code>使用使用上标的数字样式（例如 American-medical-association.csl）以及注释样式。注释样式的默认设置<span> </span><code>notes-after-punctuation</code><span> </span>为 true，否则为 false，这恢复了 pandoc-citeproc 的行为，该行为没有正确地转移到 Citeproc 。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjgm%2Fpandoc%2Fissues%2F7826" target="_blank">#7826</a>） </li> 
 <li>更新到 commonmark-pandoc 0.2.1.2 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjgm%2Fpandoc%2Fissues%2F7769" target="_blank">#7769</a><span> </span>)</li> 
 <li>添加关于 ipynb 容器中图像的常见问题解答（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjgm%2Fpandoc%2Fpull%2F7749" target="_blank">#7749</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjgm%2Fpandoc%2Freleases%2Ftag%2F2.17.0.1" target="_blank">https://github.com/jgm/pandoc/releases/tag/2.17.0.1</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            