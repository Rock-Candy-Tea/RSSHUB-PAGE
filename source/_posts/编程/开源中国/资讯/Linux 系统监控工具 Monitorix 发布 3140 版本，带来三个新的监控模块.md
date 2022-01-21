
---
title: 'Linux 系统监控工具 Monitorix 发布 3.14.0 版本，带来三个新的监控模块'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a04d2f7a68d218041ce23ff3c83ccf68f4c.png'
author: 开源中国
comments: false
date: Fri, 21 Jan 2022 07:01:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a04d2f7a68d218041ce23ff3c83ccf68f4c.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff">Monitorix 3.14.0 发布了。Monitorix 可用于监测 Linux 系统中的系统和网络资源，定期收集系统和网络数据，并使用 Web 图形界面显示相关信息。此外它还有助于检测性能瓶颈、故障、特殊的超长响应时间及其他异常活动。</span></p> 
<p><span style="background-color:#ffffff">此版本带来了三个新的监控模块（下列图片为模块对应的图表示例）：</span></p> 
<ul> 
 <li><code>nvme.pm</code>：可以监控无限数量的 NVM Express (NVMe) 设备</li> 
</ul> 
<p><img alt height="465" src="https://oscimg.oschina.net/oscnet/up-a04d2f7a68d218041ce23ff3c83ccf68f4c.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><code>amdgpu.pm</code>：可以监控无限数量的 AMD GPU 显卡</li> 
</ul> 
<p><img alt height="853" src="https://oscimg.oschina.net/oscnet/up-6ee3feb2604999306ef531b39ff513df434.png" width="700" referrerpolicy="no-referrer">​​​​​​​</p> 
<ul> 
 <li><code>nvidiagpu.pm</code>：可以看作是当前<code>nvidia.pm</code>模块的扩展版，带有更详细的统计信息</li> 
</ul> 
<p><img alt height="853" src="https://oscimg.oschina.net/oscnet/up-8d9f2ef8005593a193c706e800611c3ece5.png" width="700" referrerpolicy="no-referrer">​​​​​​​</p> 
<p>除了三个新模块外，此版本还有许多 Bug 修复，如：</p> 
<ul> 
 <li>添加了<code>redis.pm</code>连接到套接字文件的支持。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmikaku%2FMonitorix%2Fissues%2F316" target="_blank">#316</a> ]</li> 
 <li>添加了以全屏模式将网站作为 Web 应用查看的功能。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmikaku%2FMonitorix%2Fpull%2F340" target="_blank">#340</a> ]</li> 
 <li>修复了使用 SVG 图像格式时的图片缩放问题，以适应弹出窗口。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmikaku%2FMonitorix%2Fpull%2F342" target="_blank">#342</a> ]</li> 
 <li>一些小的外观变化</li> 
 <li>...</li> 
</ul> 
<p>有关 Monitorix 3.14.0 详细的变更列表，可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.monitorix.org%2Fnews.html" target="_blank">官方发布公告</a>中查看。</p>
                                        </div>
                                      
</div>
            