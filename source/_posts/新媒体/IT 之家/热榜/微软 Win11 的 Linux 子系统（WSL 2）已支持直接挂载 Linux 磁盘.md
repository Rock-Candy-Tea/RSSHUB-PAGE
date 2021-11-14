
---
title: '微软 Win11 的 Linux 子系统（WSL 2）已支持直接挂载 Linux 磁盘'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/11/d31321a7-4462-40a6-a4b2-dd4c409091f9.png'
author: IT 之家
comments: false
date: Sun, 14 Nov 2021 02:11:22 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/11/d31321a7-4462-40a6-a4b2-dd4c409091f9.png'
---

<div>   
<p data-vmark="f372"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 11 月 14 日消息，根据微软官方更新的文档，<span class="accentTextColor"><a class="s_tag" href="https://win11.ithome.com/" target="_blank">Win11</a> 的 Linux 子系统（WSL 2）已支持直接挂载 Linux 磁盘</span>。</p><p data-vmark="c0af">根据文档，用户需要安装 <span class="accentTextColor"><a class="s_tag" href="https://win11.ithome.com/" target="_blank">Windows 11</a> Build 22000 版本及以上</span>，就可以直接挂载 EXT4 等格式的 Linux 磁盘。</p><h2 data-vmark="379a">挂载未分区的 Linux 磁盘</h2><ul class=" list-paddingleft-2"><li><p data-vmark="cd06">1、识别磁盘：列出 Windows 中的可用磁盘。</p></li></ul><pre class="brush:javascript;toolbar:false ai-word-checked">GET-CimInstance -query "SELECT * from Win32_DiskDrive"</pre><ul class=" list-paddingleft-2"><li><p data-vmark="15ab">2、挂载磁盘：使用 PowerShell 对上面发现的磁盘路径挂载，DiskPath 参数为 DeviceID。</p></li></ul><pre class="brush:javascript;toolbar:false ai-word-checked">wsl --mount <DiskPath></pre><p data-vmark="402e"><img src="https://img.ithome.com/newsuploadfiles/2021/11/d31321a7-4462-40a6-a4b2-dd4c409091f9.png" w="1440" h="951" title="微软 Win11 的 Linux 子系统（WSL 2）已支持直接挂载 Linux 磁盘" width="1440" height="542" referrerpolicy="no-referrer"></p><h2 data-vmark="81ea">挂载已分区的 Linux 磁盘</h2><ul class=" list-paddingleft-2"><li><p data-vmark="5236">1、识别磁盘：列出 Windows 中的可用磁盘。</p></li></ul><pre class="brush:javascript;toolbar:false ai-word-checked">GET-CimInstance -query "SELECT * from Win32_DiskDrive"</pre><ul class=" list-paddingleft-2"><li><p data-vmark="8924">2、列出并选择要在 WSL 2 中安装的分区。</p></li></ul><pre class="brush:javascript;toolbar:false ai-word-checked">wsl --mount <DiskPath> --bare</pre><ul class=" list-paddingleft-2"><li><p data-vmark="8ce7"><span class="hljs-parameter">3、连接后，可以通过在 WSL 2 中运行以下命令来列出分区：</span></p></li></ul><pre class="brush:javascript;toolbar:false ai-word-checked">lsblk</pre><ul class=" list-paddingleft-2"><li><p data-vmark="1e42"><span class="hljs-parameter">4、确定要挂载的分区后，通过以下命令对分区进行挂载：</span></p></li></ul><pre class="brush:javascript;toolbar:false ai-word-checked">wsl --mount <DiskPath> --partition <PartitionNumber> --type <Filesystem></pre><p data-vmark="5c79"><span class="hljs-parameter">IT之家了解到，挂载后的目录为 /mnt/wsl，</span><span class="accentTextColor">Win11 可通过文件资源管理器访问 Linux 磁盘</span><span class="hljs-parameter">，路径为：</span></p><pre class="brush:javascript;toolbar:false">\\wsl$\\<Distro>\\<Mountpoint></pre><p data-vmark="4f18"><span class="hljs-parameter">具体使用方法，大家可以根据<a href="https://docs.microsoft.com/en-us/windows/wsl/wsl2-mount-disk" target="_blank">微软官方文档</a>进行操作。</span></p>
          
</div>
            