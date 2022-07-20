
---
title: 'CudaText 1.167 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=314'
author: 开源中国
comments: false
date: Wed, 20 Jul 2022 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=314'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">CudaText 是一个跨平台的文本编辑器，用 Object Pascal 编写。它是开源项目，启动速度相当快，它可以通过 Python 插件进行扩展，借助 EControl 引擎还带来了功能丰富的语法分析器。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">CudaText 1.167 正式发布，更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新增</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>新增加快 ExTerminal 插件的 API</li> 
 <li>增加：“Go to”对话框可以像处理尾部的 "+" 一样处理前面的 "+"</li> 
 <li>列表 "文件/打开最近" 也存储图片/二进制文件</li> 
 <li>添加 TRegExpr 引擎：为某些 unicode 范围更新 "大写/小写表"</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">优化</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在 10 万行以上用 "markers" 进行渲染时速度很慢</li> 
 <li>在 10 万行以上的文档中，"Inverse bookmarks" 命令非常慢</li> 
 <li>Git Status 插件在 Git 变化超过 1 万行时非常慢</li> 
 <li>在大规模替换过程中，不能激活对括号搜索器</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在 Windows 上，启动 2 个以上的组时，不能恢复 "最大化" 状态</li> 
 <li>修复了在 "Caret_after_end" 开启/关闭的情况下，Up/Down/PageUp/PageDown 的几个问题</li> 
 <li>修复：由于 IDE 的错误，"浮动" 面板功能在 GTK2 版本中被禁用</li> 
 <li>修复：当光标越过 minimap 时，无法继续用鼠标选择</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcudatext.github.io%2Fhistory.txt" target="_blank">https://cudatext.github.io/history.txt</a></p>
                                        </div>
                                      
</div>
            