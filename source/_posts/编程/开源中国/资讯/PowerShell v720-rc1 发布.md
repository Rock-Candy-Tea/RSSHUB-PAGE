
---
title: 'PowerShell v7.2.0-rc.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1588'
author: 开源中国
comments: false
date: Mon, 25 Oct 2021 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1588'
---

<div>   
<div class="content">
                                                                    
                                                        <p>PowerShell v7.2.0-rc.1 现已发布。PowerShell Core 是跨平台的（Windows，Linux和macOS）自动化和配置工具/框架，可与现有的工具配合使用，并针对处理结构化数据（例如 JSON，CSV，XML 等）、REST API 和对象模型进行了优化。它包括命令行 Shell、关联的脚本语言和用于处理 cmdlet 的框架。 </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">具体更新内容如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>General Cmdlet Updates and Fixes</strong></p> 
<ul> 
 <li>禁止 COM 调用 AppLocker 系统锁定 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16268" target="_blank">#16268</a> )</li> 
 <li>配置<code>Microsoft.ApplicationInsights</code>以不发送云角色名称 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16246" target="_blank">#16246</a> )</li> 
 <li>在锁定的机器上不允许在 NoLanguage 模式下的<code>Add-Type</code>  ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16245" target="_blank">#16245</a> )</li> 
 <li>使 color VT100 序列的属性名称与文档一致 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16212" target="_blank">#16212</a> )</li> 
 <li>使用<code>Move-Item</code>将目录移动到自身中是一个错误 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16198" target="_blank">#16198</a> )</li> 
 <li>将 FileSystemInfo.Target 从 CodeProperty 改为 AliasProperty，指向 FileSystemInfo.LinkTarget （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16165" target="_blank">＃16165</a>）</li> 
</ul> 
<p style="text-align:start"><strong>Tests</strong></p> 
<ul> 
 <li>为 PowerShell 发布包删除了已弃用的基于 docker 的测试 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16224" target="_blank">#16224</a> )</li> 
</ul> 
<p><strong>构建和打包改进</strong></p> 
<ul> 
 <li>将 .NET 6 更新到版本 6.0.100-rc.2.21505.57 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16249" target="_blank">#16249</a> )</li> 
 <li>修复 RPM packaging（Internal 17704）</li> 
 <li>更新<code>ThirdPartyNotices.txt</code>( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16283" target="_blank">#16283</a> )</li> 
 <li>更新 pipeline yaml 文件以使用<code>ubuntu-latest</code>image ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16279" target="_blank">#16279</a> )</li> 
 <li>添加脚本以生成<code>cgmanifest.json</code>( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16278" target="_blank">#16278</a> )</li> 
 <li><code>Microsoft.PowerShell.Native</code>和<code>Microsoft.PowerShell.MarkdownRender</code>软件包的更新版本( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16277" target="_blank">#16277</a> )</li> 
 <li>添加<code>cgmanifest.json</code>生成正确的第三方通知文件 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16266" target="_blank">#16266</a> )</li> 
 <li>只为稳定版本上传稳定版本的<code>buildinfo</code> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16251" target="_blank">#16251</a> )</li> 
 <li>不要为 RPM 上传<code>.dep</code>或<code>.tar.gz</code>，因为根本没有 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16230" target="_blank">#16230</a> )</li> 
 <li>确保 RPM license 被识别 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16189" target="_blank">#16189</a> )</li> 
 <li>添加条件以仅在本地开发构建中生成发布文件 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16259" target="_blank">#16259</a> )</li> 
 <li>确保<code>psoptions.json</code>和<code>manifest.spdx.json</code>文件始终存在于包中 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16258" target="_blank">#16258</a> )</li> 
 <li>修复 CI 脚本并拆分 ARM 运行 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16252" target="_blank">#16252</a> )</li> 
 <li>将 vPack task 版本更新为 12 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16250" target="_blank">#16250</a> )</li> 
 <li>签署第三方可执行文件 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16229" target="_blank">#16229</a> )</li> 
 <li>将软件物料清单添加到 main packages ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16202" target="_blank">#16202</a> )</li> 
 <li>为 markdown 测试升级<code>set-value</code>包 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16196" target="_blank">#16196</a> )</li> 
 <li>修复 Microsoft 更新拼写问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16178" target="_blank">#16178</a> )</li> 
 <li>将 vPack build 移动到 1ES Pool ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16169" target="_blank">#16169</a> )</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Freleases%2Ftag%2Fv7.2.0-rc.1" target="_blank">https://github.com/PowerShell/PowerShell/releases/tag/v7.2.0-rc.1</a></p>
                                        </div>
                                      
</div>
            