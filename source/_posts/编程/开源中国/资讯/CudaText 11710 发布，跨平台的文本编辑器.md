
---
title: 'CudaText 1.171.0 发布，跨平台的文本编辑器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1975'
author: 开源中国
comments: false
date: Tue, 20 Sep 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1975'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">CudaText 是一个跨平台的文本编辑器，用 Object Pascal 编写。它是开源项目，启动速度相当快，它可以通过 Python 插件进行扩展，借助 EControl 引擎还带来了功能丰富的语法分析器。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">CudaText 1.171.0 正式发布，更新内容如下：</p> 
<p style="text-align:start"><strong>新增</strong></p> 
<ul> 
 <li><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>当编辑太长的行（2000 多个字符）时，编辑器会关闭 lexer 几秒钟。这是为了防止在此类行上出现 caret rendering 故障。为此添加了一个选项：“max_line_len_for_editing_keeping_lexer”。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>LSP 客户端的一些 API</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>更好地计算 CJK text 的换行位置</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Addon Manager：添加选项“验证 HTTPS 证书”</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>选项“renderer_anti_flicker”现在是 per-lexer（之前是 global）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="text-align:start"><strong>修复</strong></p> 
<ul> 
 <li><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>选项 "renderer_anti_flicker":20 在 FindInFiles4 插件的 UI 中出现了回归</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>“key_left_right_wrap_with_carets”的默认值与 default.json tells 不同</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>1.169.2 中的回归：Emmet 引擎损坏</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>鼠标滚轮 zoomimg 后，滚动条位置变得非常不正确</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>“mouse_wheel_zoom”:false -> Ctrl+wheel 跳转到文件开头</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>如果 UI 比例很大，combobox-arrow 会太宽</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="text-align:start"><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>更多详情可查看：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcudatext.github.io%2Fhistory.txt" target="_blank">https://cudatext.github.io/history.txt</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            