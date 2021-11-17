
---
title: 'Fastlane 2.198.0 发布，移动端自动化流程工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5758'
author: 开源中国
comments: false
date: Wed, 17 Nov 2021 07:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5758'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">Fastlane 2.198.0 发布了，</span><span style="color:#333333">Fastlane 是一个针对 iOS 和 Android 全方位开发自动化流程的工具。利用目前支持的工具可以做包含自动化和可持续化构建的每个环节，比如单元测试、截图、分发渠道、上传元数据和 ipa 包提交审核等等。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Fastlane 2.198.0 版本主要更新内容：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#24292f">[action][set_github_release]：为可选参数<span> </span></span><code>name</code><span> </span>和<span> </span><code>description</code><span> </span>添加<span> </span><span style="color:#24292f">nil 检查。(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F19560" target="_blank">#19560</a><span style="color:#24292f">)</span></li> 
 <li><span style="color:#24292f">[action][set_github_release] ：</span><span style="color:#2e3033">支持 generate_release_notes 参数。</span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F19558" target="_blank">#19558</a><span style="color:#24292f">) </span></li> 
 <li><span style="color:#24292f">[pem]：</span><span style="color:#2e3033">添加 macOS 平台支持。</span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F19564" target="_blank">#19564</a><span style="color:#24292f">) </span></li> 
 <li><span style="color:#24292f">[fastlane_core]：</span>使用 iTMS 上传 IPA 时，<span style="color:#24292f">用<span> </span><code>-assetFile</code><span> </span>代替<span> </span><code>-f</code>。</span>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F19596" target="_blank">#19596</a><span> </span>)</li> 
 <li><span style="color:#24292f">[action][get_version_number] ：如果目标没有 INFO_PLIST，则在构建设置中搜索 MARKETING_VERSION 。</span>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F19589" target="_blank">#19589</a><span> </span>) </li> 
 <li><span style="color:#24292f">[action][notarize]：为<span> </span><code>notarize</code><span> </span>行为添加可选的<span> </span><code>skip_stapling</code><span> </span>参数。(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F19577" target="_blank">#19577</a><span style="color:#24292f">) </span></li> 
 <li><span style="color:#24292f">[match][cert]：</span><span style="color:#2e3033">如果使用 apple id，则允许创建 developer_id 。</span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F19604" target="_blank">#19604</a><span style="color:#24292f">) </span></li> 
 <li><span style="color:#24292f">[match]：</span><span style="color:#2e3033">支持通过特定证书来过滤 nuke 。</span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F19584" target="_blank">#19584</a><span style="color:#24292f">)</span></li> 
 <li><span style="color:#24292f">[action][set_github_release]：修复了错误的状态代码不会报错的问题。</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F19516" target="_blank">#19516</a>）</li> 
 <li><span style="color:#24292f">[scan]：修复了错误信息的错别字。(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F19514" target="_blank">#19514</a><span style="color:#24292f">)</span></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Freleases%2Ftag%2F2.198.0" target="_blank">https://github.com/fastlane/fastlane/releases/tag/2.198.0</a></p>
                                        </div>
                                      
</div>
            