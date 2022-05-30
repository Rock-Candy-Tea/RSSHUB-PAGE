
---
title: 'Helix 22.05 发布，后现代模态文本编辑器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5829'
author: 开源中国
comments: false
date: Mon, 30 May 2022 07:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5829'
---

<div>   
<div class="content">
                                                                                            <p>Helix 是一个模态文本编辑器，内置支持多选、语言服务器协议 (LSP)、tree-sitter 以及对调试适配器协议 (DAP) 的实验性支持。目前 Helix  22.05 版本已发布，这是一个功能丰富的版本，带来如下内容：</p> 
<h2><strong>重做缩进系统</strong></h2> 
<p>Indentation 缩进系统已完全重做，仍然可以通过查询已解析的 tree-sitter 语法树来查找文档，但现在查询文件可以使用 tree-sitter 查询的全部表达能力，而不仅仅是简单的节点名称。</p> 
<h2>可配置的 gutters</h2> 
<p>现在可以在 config.toml 文件中配置 Gutters。 例如可以删除行号装订线，同时仍显示 LSP 诊断。</p> 
<pre><code>[editor]
gutters = ["diagnostics"] # default is ["diagnostics", "line-numbers"]</code></pre> 
<h2>rulers 选项</h2> 
<p>可以通过该 rulers 选项配置垂直标尺。在遵守最大线长时将它们用作指南。</p> 
<h2>显示可见的空白</h2> 
<p>现在可以呈现空格、制表符和换行符等空白字符。在运行时使用命令或在编辑器部分下使用该<code>whitespace.render</code>选项。可见的空白指示符可以使 Helix 的选择模型更加直观，尤其是在行尾附近。</p> 
<p> </p> 
<p>更多内容请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhelix-editor.com%2Fnews%2Frelease-22-05-highlights%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            