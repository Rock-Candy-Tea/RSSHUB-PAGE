
---
title: 'GTK 4.4 发布：NGL 持续改进，Inspector 默认启用'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6694'
author: 开源中国
comments: false
date: Wed, 25 Aug 2021 07:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6694'
---

<div>   
<div class="content">
                                                                    
                                                        <p>GTK 4.4 现已发布，该版本是 5 个月开发的结果，有来自 71 位开发人员的 838 次个人 commit；总共添加了 88133 行，删除了 63094 行。</p> 
<p>一些亮点更新内容如下：</p> 
<p><strong>NGL 渲染器和 GL 支持</strong></p> 
<p>NGL 渲染器正在持续改进中，包括加速、修复转换渲染、避免巨大的中间纹理以及正确处理部分颜色字体。目前，NGL 已可以与 Mali 驱动程序一起正常工作。官方表示，其计划在下一个周期放弃原来的 GL 渲染器。</p> 
<p><strong>主题</strong></p> 
<p>包含的主题已经过重新组织和重命名。官方现已发布名为 Default、Default-dark、Default-hc 和 Default-hc-dark 的主题。Adwaita 主题正在转移到 libadwaita。以及较小的主题改进，包括新的错误下划线（它们现在是虚线而不是波浪线）和对半透明文本选择的支持。</p> 
<p><strong>Input</strong></p> 
<p>输入处理方面也得到了积极地改进。开发团队已经将内置输入法的行为与 IBus 进行了匹配，以显示和处理组合序列和死键。目前支持不产生单个 Unicode 字符的多个死键和死键组合（例如 ẅ）。还完全支持 32-bit keysyms，因此使用 Unicode keysyms（例如用于组合标记）是可行的。</p> 
<p><strong>Emoji</strong></p> 
<p>Emoji 数据已经更新到 CLDR 39，可以按语言和地区寻找翻译后的 Emoji 数据（如 it-ch）。</p> 
<p><strong>Debugging</strong></p> 
<p>Inspector 现在是默认启用的，所以调试 GTK 应用程序应该更容易一些。</p> 
<p><strong>Windows</strong></p> 
<p>除了已经提到的 WGL 改进之外，其现在还使用 GL 在 Windows 上进行媒体播放。4.4 后期的一个重大变化是，将 WinPointer API 用于平板电脑和其他输入设备，取代过时的 wintab API。Windows 上的 DND 支持也得到了改进，本地 DND 协议已被删除。</p> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.gtk.org%2F2021%2F08%2F23%2Fgtk-4-4%2F" target="_blank">https://blog.gtk.org/2021/08/23/gtk-4-4/</a></p>
                                        </div>
                                      
</div>
            