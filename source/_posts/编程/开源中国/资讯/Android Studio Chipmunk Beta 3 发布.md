
---
title: 'Android Studio Chipmunk Beta 3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6310'
author: 开源中国
comments: false
date: Wed, 09 Mar 2022 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6310'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#000000">Android Studio 2021.</span><span style="background-color:#ffffff; color:#000000">2</span><span style="background-color:#ffffff; color:#000000">.1（代号"</span>Chipmunk<span style="background-color:#ffffff; color:#000000">"）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroidstudio.googleblog.com%2F2022%2F03%2Fandroid-studio-chipmunk-beta-3-now.html" target="_blank">发布</a>了第三个 Beta 测试版。</span></p> 
<p>此版本主要是修复错误：</p> 
<p><strong style="color:#202124">Android Gradle 插件</strong></p> 
<ul> 
 <li>基于 ASM 的转换 API 会在包含 JSR/RET 指令时尝试计算 Java 6 字节码的帧（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F213348892" target="_blank">问题 213348892</a>）</li> 
 <li>运行 shrinkReleaseRes 后，未创建 resources.txt 诊断信息文件（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F215407007" target="_blank">问题 215407007</a>）</li> 
 <li>Studio 和 AGP 兼容性选项的链接指向公司网站（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F214079804" target="_blank">问题 214079804</a>）</li> 
 <li><span style="background-color:rgba(255, 255, 255, 0.95); color:#202124">Android studio 2021.1.1 beta5。Gradle 同步失败，并显示“无法加载类‘com.android.build.api.extension.AndroidComponentsExtension’”（</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F210484302" target="_blank">问题 210484302</a><span style="background-color:rgba(255, 255, 255, 0.95); color:#202124">）</span></li> 
</ul> 
<p><strong style="color:#202124">Benchmark</strong></p> 
<ul> 
 <li>Macrobenchmark 链接（非 Perfetto 跟踪记录）在 Studio 中无法正常运行（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F201405014" target="_blank">问题 201405014</a>）</li> 
</ul> 
<p><strong>CPU</strong></p> 
<ul> 
 <li>配置文件采样损坏基准测量（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F207159244" target="_blank">问题 207159244</a>）​​​​​​</li> 
</ul> 
<p><strong>代码分析</strong></p> 
<ul> 
 <li>@IntDev 不支持负值？（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F167750517" target="_blank">问题 167750517</a>）</li> 
</ul> 
<p><strong>lint</strong></p> 
<ul> 
 <li>kotlinx-coroutines-core 中存在可疑的缩进 lint 检查假正例（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F215741972" target="_blank">问题 215741972</a>）</li> 
 <li>ObsoleteSdkInt 检查应标记 @TargetApi 使用情况（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F74130329" target="_blank">问题 74130329</a>）</li> 
 <li>lint：由 LintCliXmlParser 的 getValueLocation 计算的位置不正确（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F211693606" target="_blank">问题 211693606</a>）</li> 
 <li>ObsoleteSdkInt 检查应包含 tools:targetApi（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F37140910" target="_blank">问题 37140910</a>）</li> 
 <li>ObsoleteSdkInt 应检查 RequiresApi、TargetApi 和 SdkSuppress 注解（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F110692931" target="_blank">问题 110692931</a>）</li> 
 <li>IDE 中未使用 Quickfix 逻辑顺序（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F211770054" target="_blank">问题 211770054</a>）</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroidstudio.googleblog.com%2F2022%2F03%2Fandroid-studio-chipmunk-beta-3-now.html" target="_blank">详情查看发布公告</a>。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fstudio%2Fpreview%2Findex.html" target="_blank">https://developer.android.com/studio/preview/index.html</a></p>
                                        </div>
                                      
</div>
            