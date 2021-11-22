
---
title: 'Fastlane 2.198.1 发布，移动端自动化流程工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=494'
author: 开源中国
comments: false
date: Mon, 22 Nov 2021 07:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=494'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">Fastlane 2.198.1 发布了，</span><span style="color:#333333">Fastlane 是一个针对 iOS 和 Android 全方位开发自动化流程的工具。利用目前支持的工具可以做包含自动化和可持续化构建的每个环节，比如单元测试、截图、分发渠道、上传元数据和 ipa 包提交审核等等。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Fastlane 2.198.1 版本主要更新内容：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#2e3033">解决了上传 iPad Pro 第 5 代截图的问题。</span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F19616" target="_blank">#19616</a><span style="color:#24292f">) </span></li> 
 <li><span style="color:#2e3033">添加<span> </span><code>xcodebuild_command</code><span> </span>选项。</span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F19614" target="_blank">#19614</a><span style="color:#24292f">)</span></li> 
 <li><span style="color:#24292f">[fastlane_core] 修复 TransportExecutor ，以专门查找 ipa、dmg、ipa 和 zip 文件，而不是整个 -assetFile 的目录。(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F19620" target="_blank"><u>#19620</u></a><span style="color:#24292f">)</span></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">新的逻辑有时会试图用<span> </span><code>-assetFile</code><span> </span>上传一个目录(这样不起作用)，应该使用<span> </span><code>-f</code><span> </span>代替。现在在尝试使用<code><span> </span>-assetFile</code><span> </span>之前先切换逻辑，明确查找的并不是整个目录，而是.ipa、.dmg、.pkg 或.zip 文件。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">更新公告：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Freleases%2Ftag%2F2.198.1" target="_blank">https://github.com/fastlane/fastlane/releases/tag/2.198.1</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            