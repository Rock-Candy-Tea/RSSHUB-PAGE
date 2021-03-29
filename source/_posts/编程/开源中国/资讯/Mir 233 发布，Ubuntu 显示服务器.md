
---
title: 'Mir 2.3.3 发布，Ubuntu 显示服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6381'
author: 开源中国
comments: false
date: Sun, 28 Mar 2021 23:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6381'
---

<div>   
<div class="content">
                                                                                            <p>Mir 2.3.3 现已发布。Mir 是一个 Linux 操作系统下的显示服务器，它用于构建基于 Wayland 的 Shell 的库集，简化了 Shell 作者需要处理的复杂性：它提供了一个稳定，经过良好测试和高性能的平台，具有触摸、鼠标和平板输入，多显示功能和安全的客户端-服务器通信。</p> 
<p>该版本具体更新内容如下：</p> 
<p><strong>ABI summary</strong></p> 
<ul> 
 <li>mirclient ABI 保持在10</li> 
 <li>miral ABI 保持在 4</li> 
 <li>mirserver ABI 保持不变，为 54</li> 
 <li>mircommon ABI 保持在 7</li> 
 <li>mirplatform ABI保持在20</li> 
 <li>mirprotobuf ABI 保持在 3</li> 
 <li>mirplatformgraphics ABI 保持不变，为 18</li> 
 <li>mirinputplatform ABI 保持在 8</li> 
 <li>mircore ABI 保持在 1</li> 
 <li>mircookie ABI 保持在 2</li> 
 <li>mirwayland ABI 保持在 2</li> 
</ul> 
<p><strong>Bugs fixed</strong></p> 
<ul> 
 <li>添加<code>app-env-amend</code>配置选项（Fixes<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMirServer%2Fmir%2Fissues%2F1934" target="_blank">＃1934</a>）</li> 
 <li>[miral-terminal] 等待 gnome-terminal-server 的 exit</li> 
 <li>修复 mirplatform.pc include dirs</li> 
 <li>为 strdup 添加缺少的 header</li> 
 <li>[Wayland] 使用 relative motion 时不要抑制 motion events（Fixes<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMirServer%2Fmir%2Fissues%2F1959" target="_blank">＃1959</a>）</li> 
 <li>修复 Arch 的 protobuf 符号（修复 Arch 上的 FTBFS）</li> 
</ul> 
<p> 更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMirServer%2Fmir%2Freleases%2Ftag%2Fv2.3.3" target="_blank">https://github.com/MirServer/mir/releases/tag/v2.3.3</a></p>
                                        </div>
                                      
</div>
            