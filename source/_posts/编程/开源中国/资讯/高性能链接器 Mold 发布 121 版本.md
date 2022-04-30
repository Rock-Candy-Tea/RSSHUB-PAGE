
---
title: '高性能链接器 Mold 发布 1.2.1 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4816'
author: 开源中国
comments: false
date: Sat, 30 Apr 2022 07:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4816'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">Mold 是现有 Unix 链接器的快速替代品，它比 LLVM lld 链接器快几倍。目前 </span><span style="color:#333333">Mold 发布了 1.2.1 版本，带来以下更改</span></p> 
<ul> 
 <li>修复 --gdb-index 中的各种错误。</li> 
 <li>为了与 LLVM lld 兼容，Mold 现在可以识别 --thinlto-cache-dir 和 --thinlto-cache-policy。 <span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2F7ebd071273691a5cc095203f6542b2b13ec6642c" target="_blank">7ebd071</a><span style="color:#24292f">)</span></li> 
 <li>Mold 现在可以处理 TLS 常用符号，GCC 有时会为线程局部变量创建这样的符号。 <span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2Fcf850f8993210185e57c329ce14a361b7e51cbe0" target="_blank">cf850f8</a><span style="color:#24292f">)</span></li> 
 <li>在某些极端情况下，Mold 为同一符号创建了一个非版本化符号和一个版本化符号，即使一个符号被版本化，所有同名符号也必须被版本化。<span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2F8298c0ad16a4ab9cf95efe4ada43bbba9f33941d" target="_blank">8298c0a</a><span style="color:#24292f">)</span></li> 
 <li>修复：Mold 用于将符号的 PLT 地址而不是其地址写入 .symtab。 <span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2Fe088db72e006e8f1bcbc7c9561a3e22777cd33ff" target="_blank">e088db7</a><span style="color:#24292f">)</span></li> 
 <li>Mold 现在可以处理超过 219 个符号的输入文件。<span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2Ff1f2d40469a3a501c573b1181e0e4362c030a9bf" target="_blank">f1f2d40</a><span style="color:#24292f">)</span></li> 
 <li>/usr/local/libexec/mold/ld 现在安装为相对符号链接，而不是绝对符号链接。<span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Fcommit%2F5803c3c200f301adc3abdb66df16d3d669712d70" target="_blank">5803c3c</a><span style="color:#24292f">)</span></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frui314%2Fmold%2Freleases%2Ftag%2Fv1.2.1" target="_blank">https://github.com/rui314/mold/releases/tag/v1.2.1</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            