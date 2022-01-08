
---
title: 'Poppler 22.01 发布，PDF 渲染库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=722'
author: 开源中国
comments: false
date: Sat, 08 Jan 2022 07:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=722'
---

<div>   
<div class="content">
                                                                                            <p>Poppler 是一个用来渲染 PDF 文档的程序库，它是 GNU/Linux 系统上同类程序库中最为常用的一个，并被开源桌面环境 GNOME 和 KDE 上的 PDF 阅读器所使用。</p> 
<p>近日，Poppler 22.01.0 正式发布，更新内容如下：</p> 
<p>Core：</p> 
<ul> 
 <li>允许在 Windows 上使用本地字体目录</li> 
 <li>TextOutputDev：需要更多的列间距</li> 
 <li>修复 <code>Splash::gouraudTriangleShadedFill</code> 的崩溃问题</li> 
 <li>修复调用 <code>Form::reset()</code> 时的崩溃</li> 
 <li>GfxSeparationColorSpace: 检查颜色空间和函数的有效性</li> 
 <li>少量代码改进</li> 
</ul> 
<p>Glib:</p> 
<ul> 
 <li>在使用 glib.h 中的定义之前，请包含 glib.h</li> 
 <li>发生错误时关闭文件描述符</li> 
 <li>修复内存泄漏</li> 
 <li>替换已废弃的 g_memdup/g_time_zone_new 的使用</li> 
 <li>移除 Windows 下的 FD-taking 函数</li> 
</ul> 
<p>实用工具</p> 
<ul> 
 <li>pdfsig: 增加对有密码的文件的支持</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpoppler.freedesktop.org%2F" target="_blank">https://poppler.freedesktop.org/</a></p>
                                        </div>
                                      
</div>
            