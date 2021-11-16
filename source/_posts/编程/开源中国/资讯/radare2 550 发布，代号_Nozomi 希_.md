
---
title: 'radare2 5.5.0 发布，代号_Nozomi 希_'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3177'
author: 开源中国
comments: false
date: Tue, 16 Nov 2021 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3177'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">radare2 是 radare 的一个重写版本，是一个逆向工程框架和命令行工具集，可以用来简化逆向工程任务。</span>radare2 5.5.0 现已发布，<span style="background-color:#ffffff; color:#333333">该版本包含了 api、esil、abi 和 commands 中的 breaking changes；插件将需要像往常一样重新编译。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">具体更新内容包括有：</span></p> 
<ul> 
 <li>新的 IOBanks API 和命令替换了 skyline 并使 io 更快（2-10 倍）</li> 
 <li>更快的分析、类型匹配、二进制解析（2-4 倍）</li> 
 <li>[] 和 <span style="background-color:#ffffff; color:#24292f">=[] esil</span> 操作已被删除（大小是强制性的）</li> 
 <li>在 bin 解析器和反汇编器中修复了许多重要的 bug</li> 
 <li>添加对最新的 iOS15 dyld4 Atlas 样式缓存格式的支持</li> 
 <li>自动重命名签名匹配冲突和更快的搜索</li> 
 <li>为 riscv 添加汇编程序，为 PDP11、Alpha64 和 armv7.v35 添加反汇编程序</li> 
 <li>改进了与 r2frida 远程文件系统的集成</li> 
 <li>Cleaning Windows（32 和 64）和 macOS 的调试器使其更加可靠和稳定</li> 
 <li>添加 seven segment printing（ascii-art 文本标题的 ?ea）</li> 
 <li>使用新的 axfm 和 axtm 命令改进 xrefs 可视化</li> 
 <li>添加<code>avg</code>命令来管理全局变量</li> 
 <li>Sixref 插件现在更容易用于在 arm64 代码上查找 xrefs </li> 
 <li>改进了 apk:// 中的 multibin（选择所有 bin 或一个）和 multidex 支持</li> 
 <li>更好地为 Windows 构建脚本（添加 asan 和 w32 配置文件）</li> 
 <li>添加了 armv7.v35 并使用 arm64.v35 改进了 esil 仿真</li> 
 <li>添加更多帮助信息并默认设置 scr.prompt.tabhelp 为 true</li> 
 <li>rahash2 中的 AES 密钥包装算法支持</li> 
 <li>修复调试器重载 (ood) 和项目保存 (Ps) 中的 var 序列化问题</li> 
 <li>添加 Amiga 和 MSX rom/bin 解析器插件并测试</li> 
 <li><span style="background-color:#ffffff; color:#24292f">Visual slides</span> (r2s) 允许在 r2 中使用交互式内容</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Freleases%2Ftag%2F5.5.0" target="_blank">https://github.com/radareorg/radare2/releases/tag/5.5.0</a></p>
                                        </div>
                                      
</div>
            