
---
title: 'Snapcraft 6.0 发布，Linux 软件包管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9507'
author: 开源中国
comments: false
date: Thu, 28 Oct 2021 06:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9507'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Snapcraft 是一个用于 Linux 系统上的打包、分发与更新工具，由于绑定了依赖项，所以不需要修改就可以在所有主要 Linux 系统上运行。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Snapcraft 6.0 正式发布，更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">Core 20 的<span> </span><strong>Snapcraft</strong></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">现在 Snapcraft 已经转移到 core20 上面，基于Ubuntu 20.04 LTS。由于<span> </span></span><span style="color:#111111">Ubuntu 20.04 LTS 引入了对 riscv64 架构的支持 ，同时对 i386 的支持缩减到 32 位列表，基于 core20 的</span><span style="color:#2e3033"><span> </span>Snapcraft 6.0 也将支持<span> </span></span><span style="color:#111111">riscv64，不再支持 i386 架构。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#111111">不过 i386 架构的用户仍然可以使用<span> </span></span><span style="color:#24292f">Snapcraft 5.x 和 4.x 版本， 6.x 新版本的功能就无法使用了，可</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsnapcraft.io%2Fblog%2Fsnapcraft-6-0-is-around-the-corner" target="_blank"><span style="color:#24292f">点此查看详细信息</span></a><span style="color:#24292f">。</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>实验功能 - offline</strong></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Snapcraft  使用<span> </span><code>--offline</code><span> </span>模式时，缓存将更加激进，无需联网即可工作。这对已经拉取的项目非常有用，因为它们不需要联网了。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">内容更新</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#24292f"><strong>schema：</strong></span><span style="color:#2e3033">将 “microk8s” 添加到系统用户列表里。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3545" target="_blank">#3545</a></li> 
 <li><span style="color:#24292f"><strong>schema：</strong></span>为<span> </span><span style="color:#24292f">hooks 添加环境支持。 (CRAFT-424)<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3565" target="_blank">#3565</a></li> 
 <li><span style="color:#24292f"><strong>lint：</strong>禁用新的 shellcheck 警告。(CRAFT-482)  </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3574" target="_blank">#3574</a></li> 
 <li><span style="color:#24292f"><strong>snaps：</strong>移除对查询 snap 信息的额外调用。(CRAFT-479) </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3573" target="_blank">#3573</a></li> 
 <li><span style="color:#24292f"><strong>extensions：</strong></span><span style="color:#2e3033">从内容快照中预加载 bindtextdomain 。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3569" target="_blank">#3569</a></li> 
 <li><span style="color:#24292f"><strong>cli & providers：</strong></span><span style="color:#2e3033">为<span> </span></span><span style="color:#24292f">lifecycle</span><span style="color:#2e3033"><span> </span>命令传递 part 名称 。</span><span style="color:#24292f">(</span><span style="color:#2e3033"><span> </span></span><span style="color:#24292f">CRAFT-481)<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3572" target="_blank">#3572</a></li> 
 <li><span style="color:#24292f"><strong>ROS V2 插件</strong><span> </span>：解决条件依赖问题。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3570" target="_blank"><u>#3570</u></a><u> </u></li> 
 <li><span style="color:#24292f">ROS 2 插件 v2 杂项更新。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3566" target="_blank">#3566</a></li> 
 <li><span style="color:#24292f"><strong>cli：</strong>加入实验性的 --offline 选项。(CRAFT-480)  </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3577" target="_blank">#3577</a></li> 
 <li><span style="color:#24292f"><strong>snap：</strong>现在基于 core20 。(CRAFT-509)<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3579" target="_blank">#3579</a></li> 
 <li><span style="color:#2e3033"><strong>Github：</strong>更新 snapcore/action-build 管理 。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3582" target="_blank">#3582</a></li> 
 <li><span style="color:#24292f"><strong>environment-setup-local：<span> </span></strong>cryptography 3.4 可能不支持构建 rust 版本。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3580" target="_blank">#3580</a></li> 
 <li><span style="color:#24292f"><strong>packaging：</strong></span><span style="color:#2e3033">在 riscv64 上会加载正确的库，让<span> </span></span><span style="color:#24292f">ctypes 可以在<span> </span></span><span style="color:#2e3033">riscv64 架构上工作。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3581" target="_blank">#3581</a></li> 
 <li><span style="color:#24292f"><strong>build providers：</strong></span>snapcraft 的新基准是 core20，停止对 core18 的更新。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3583" target="_blank">#3583</a></li> 
 <li><span style="color:#24292f"><strong>repo：</strong></span>使用主机状态<span style="color:#24292f">进行 apt 缓存。(CRAFT-488)<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3585" target="_blank">#3585 </a></li> 
 <li><span style="color:#24292f"><strong>yaml：</strong></span><span style="color:#2e3033">在 snapcraft.yaml 中检测并记录重复键的警告。</span><span style="color:#24292f">(CRAFT-553)<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3518" target="_blank">#3518</a></li> 
 <li><span style="color:#24292f"><strong>lifecycle：</strong>基于 core20 初始化 。(CRAFT-517)</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3587" target="_blank"><span> </span>#3587 </a></li> 
 <li><span style="color:#24292f"><strong>snap：</strong></span>修复<span> </span><span style="color:#24292f">riscv64 架构的</span><span> </span><span style="color:#24292f">patchelf 工具。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3588" target="_blank">#3588</a></li> 
 <li><span style="color:#24292f"><strong>snap：</strong></span>为 patchelf 应用适合的补丁。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3589" target="_blank">#3589</a></li> 
 <li><span style="color:#24292f"><strong>snap：</strong>引用正确的补丁路径。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3590" target="_blank">#3590</a></li> 
 <li><span style="color:#24292f"><strong>extensions：</strong>有条件地</span><span style="color:#2e3033">前置<span> </span><code>LIBVA_DRIVERS_PATH</code>，而不是直接覆盖。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3591" target="_blank">#3591</a></li> 
 <li>从桌面助手移植字体渲染的修复。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3586" target="_blank">#3586</a></li> 
 <li><span style="color:#24292f"><strong>extensions/desktop：</strong></span>不再固定导出<span> </span><span style="color:#24292f"><code>QT_QPA_PLATFORM_THEME</code></span>，改由平台决定。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3594" target="_blank">#3594</a></li> 
 <li><span style="color:#24292f"><strong>lifecycle, providers：</strong></span><span style="color:#2e3033">离线模式下</span>跳过需要网络的操作步骤。<span style="color:#24292f">(CRAFT-587)<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Fpull%2F3593" target="_blank">#3593</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Freleases%2Ftag%2F6.0" target="_blank">https://github.com/snapcore/snapcraft/releases/tag/6.0</a> </p> 
<p> </p>
                                        </div>
                                      
</div>
            