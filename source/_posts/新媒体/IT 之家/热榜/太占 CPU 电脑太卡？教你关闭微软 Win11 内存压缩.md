
---
title: '太占 CPU 电脑太卡？教你关闭微软 Win11 内存压缩'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/2/1a47f3d9-1540-4071-bc1e-6fd30480d032.png'
author: IT 之家
comments: false
date: Thu, 10 Feb 2022 23:40:32 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/2/1a47f3d9-1540-4071-bc1e-6fd30480d032.png'
---

<div>   
<div class="tougao-user">感谢IT之家网友 <a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1785650" rel="nofollow">AMD引领未来</a> 的线索投递！</div>
            <p data-vmark="46e0">很多朋友都注意到，<span class="accentTextColor"><a class="s_tag" href="https://win11.ithome.com/" target="_blank">Win11</a> 默认开启了内存压缩功能</span>。内存压缩顾名思义，可以压缩内存中的数据，让内存占用更少，同时减少 Swap 频次，带来更高的 I / O 效率。</p><p data-vmark="4e49">但与此同时，<span class="accentTextColor">压缩数据需要耗费 CPU 资源</span>，一些朋友使用的是 CPU 性能较弱的设备，例如轻薄本，开启内存压缩可能会造成卡顿缓慢。同时，<span class="accentTextColor">内存压缩需要消耗额外的 CPU 资源，带来更多耗电发热</span>，这对注重续航的设备来说也是不合适的。</p><p data-vmark="28af">实际上，微软在 <a class="s_tag" href="https://win10.ithome.com/" target="_blank">Win10</a> 中就已经启用了内存压缩机制，在 Win11 当中继续了这一设定。那么问题来了，<span class="accentTextColor">如果你不缺内存，但 CPU 性能较弱，而且需要更长的续航</span>，要如何关闭内存压缩？一起来看看吧！</p><h2 data-vmark="d02b">确认内存压缩的开启状态</h2><p data-vmark="525f">首先，我们要确认内存压缩是否真的已经开启，这里有两种方法。</p><p data-vmark="b86e"><strong>・通过任务管理器查看</strong>。如果开启了内存压缩，那么在任务管理器中，就会显示压缩内存的数据，这个还是很容易观察到的。</p><p data-vmark="df34" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/2/1a47f3d9-1540-4071-bc1e-6fd30480d032.png" w="700" h="563" alt="Win11内存压缩 关闭内存压缩" title="太占 CPU 电脑太卡？教你关闭微软 Win11 内存压缩" width="700" height="563" referrerpolicy="no-referrer"></p><p data-vmark="d915"><strong>・通过命令行查看</strong>。使用系统管理员权限，打开 PowerShell，然后输入以下命令：</p><pre class="brush:javascript;toolbar:false">Get-MMAgent</pre><p data-vmark="5c2e" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/2/31032e87-52bb-4c43-9e07-70f04aeae57a.jpg" w="700" h="390" alt="Win11内存压缩 关闭内存压缩" title="太占 CPU 电脑太卡？教你关闭微软 Win11 内存压缩" width="700" height="390" referrerpolicy="no-referrer"></p><p data-vmark="3b54">按下回车键运行，如果看到“MemoryCompression”这一项是“True”，那么说明内存压缩已经开启。</p><p data-vmark="cdd1" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/2/27f83813-f75d-4ad0-b40c-3beaa273fbba.png" w="700" h="422" alt="Win11内存压缩 关闭内存压缩" title="太占 CPU 电脑太卡？教你关闭微软 Win11 内存压缩" width="700" height="422" referrerpolicy="no-referrer"></p><h2 data-vmark="99b1">如何关闭内存压缩？</h2><p data-vmark="38e9">要关闭内存压缩，我们需要借助命令行。使用管理员权限打开 PowerShell，输入以下命令：</p><pre class="brush:javascript;toolbar:false ai-word-checked">Disable-MMAgent -mc</pre><p data-vmark="4907" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/2/1a5ef464-836e-4a2a-9fc3-7e3a842926df.png" w="700" h="422" alt="Win11内存压缩 关闭内存压缩" title="太占 CPU 电脑太卡？教你关闭微软 Win11 内存压缩" width="700" height="422" referrerpolicy="no-referrer"></p><p data-vmark="9459">按下回车键运行，随后重启系统，内存压缩就关闭了。</p><p data-vmark="3dad">如果想要重新打开内存压缩，也很简单，同样利用管理员权限打开 Powershell，使用以下命令：</p><pre class="brush:javascript;toolbar:false">Enable-MMAgent -mc</pre><p data-vmark="8fb3" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/2/57743056-711d-487c-b54f-54bd325085f7.png" w="700" h="422" alt="Win11内存压缩 关闭内存压缩" title="太占 CPU 电脑太卡？教你关闭微软 Win11 内存压缩" width="700" height="422" referrerpolicy="no-referrer"></p><p data-vmark="12d5">重启系统后，内存压缩就重新开启了。</p><h2 data-vmark="5f78">后话</h2><p data-vmark="acb8">总的来说，在大部分情况下，内存压缩是非常实用的技术，它可以增加内存的利用效率，提升 I / O 性能，带来更出色的多任务体验。但如果你的 CPU 能力有限，或者非常注重续航，关闭内存压缩也不失为一种选择，不妨试试本文的方法吧。</p>
          
</div>
            