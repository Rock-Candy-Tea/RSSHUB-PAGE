
---
title: 'Fastlane 2.207.0 发布，移动端自动化流程工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7491'
author: 开源中国
comments: false
date: Fri, 01 Jul 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7491'
---

<div>   
<div class="content">
                                                                                            <p>Fastlane 是一个针对 iOS 和 Android 全方位开发自动化流程的工具。利用目前支持的工具可以做包含自动化和可持续化构建的每个环节，比如单元测试、截图、分发渠道、上传元数据和 ipa 包提交审核等等。</p> 
<p>Fastlane 2.207.0 发布了，此版本带来许多改进，放弃了对 Ruby 2.5 的支持。具体更新细项如下：</p> 
<ul> 
 <li>[match]检查配置文件是否存在时，添加 profile_type 过滤 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F20311" target="_blank">#20311</a>)</li> 
 <li>[deliver] update deliver/runner.rb to handle both ipa and pkg paths. (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F20043" target="_blank">#20043</a>) via Stefan Natchev (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnatchev" target="_blank"><strong>@snatchev</strong></a>)</li> 
 <li>[match] <span style="color:#24292f">更新 Deliver/runner.rb 以处理 ipa 和 pkg 路径。</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F20418" target="_blank">#20418</a>) </li> 
 <li>[match] <span style="color:#24292f">添加对 GitLab 安全文件的支持作为匹配存储模式</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F20386" target="_blank">#20386</a>) </li> 
 <li>[match] 改进 Match::CommandsGenerator 的解密选项单元测试 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F20395" target="_blank">#20395</a>) </li> 
 <li>[match] 添加了 Match::CommandsGenerator 的导入选项单元测试 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F20396" target="_blank">#20396</a>) </li> 
 <li>[fastlane-core][scan] 在 <code>xcodebuild</code> 命令中添加了目标参数支持  (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F20399" target="_blank">#20399</a>) </li> 
 <li>[pilot] <span style="color:#24292f">添加了 Pilot::TesterExporter 类单元测试</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F20394" target="_blank">#20394</a>)  </li> 
 <li>[frameit] 加入 Google Pixel 5 设备 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F20389" target="_blank">#20389</a>)  </li> 
 <li>[action][update_info_plist] 改进 plist 文件路径选项验证检查 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F20356" target="_blank">#20356</a>) </li> 
 <li>[match] 指定 s3 对象前缀 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F20344" target="_blank">#20344</a>)  </li> 
 <li>[snapshot] 将丢失的 iPod touch 添加到生成的 <span style="color:#24292f">Snapshot </span>报告 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F20337" target="_blank">#20337</a>)</li> 
 <li>[Ruby] Ruby 2.6 现在是最低版本（放弃对 Ruby 2.5 的支持） (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Fpull%2F20413" target="_blank">#20413</a>) </li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffastlane%2Ffastlane%2Freleases%2Ftag%2F2.207.0" target="_blank">https://github.com/fastlane/fastlane/releases/tag/2.207.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            