
---
title: 'Apache Maven 3.8.3 发布，项目管理和构建工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8230'
author: 开源中国
comments: false
date: Wed, 06 Oct 2021 07:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8230'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Maven 3.8.3 发布了。Apache Maven 是一个项目管理和构建工具。基于项目对象模型（POM）的概念， Maven 可以从中心位置管理项目的构建、报告和文档。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此版本更新内容如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Bug</strong></p> 
<ul> 
 <li>[MNG-7045] - 从 Maven 中删除 CDI API</li> 
 <li>[MNG-7214] - CDI API 中的过渡性依赖 parent 不好。</li> 
 <li>[MNG-7215] - [Regression] Maven 网站插件无法解决 parent 问题 </li> 
 <li>[MNG-7216] - Revert MNG-7170</li> 
 <li>[MNG-7218] - [Regression] o.a.m.model.Build.getSourceDirectory() </li> 
 <li>[MNG-7219] - [Regression] transitive 中缺少 plexus-cipher</li> 
 <li>[MNG-7220] - [RegRESSION] test-classpath 错误解析</li> 
 <li> <p style="text-align:start"><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>[MNG-7251] </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>- <span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>修复泄漏到 cloned 中的 threadLocalArtifactsHolder </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> </li> 
 <li>[MNG-7253] - Relocation 信息从不显示</li> 
</ul> 
<p style="color:#333333; margin-left:0px; margin-right:0px; text-align:left"><strong>New Feature</strong></p> 
<ul> 
 <li>[MNG-7164] - 添加 constructor MojoExecutionException(Throwable)</li> 
</ul> 
<p style="color:#333333; margin-left:0px; margin-right:0px; text-align:left"><strong>Improvement</strong></p> 
<ul> 
 <li>[MNG-7235] - 计算排序时的速度改进。</li> 
 <li>[MNG-7236] - DefaultPluginVersionResolver 应该缓存会话的结果</li> 
</ul> 
<p style="color:#333333; margin-left:0px; margin-right:0px; text-align:left"><strong>Task</strong></p> 
<ul> 
 <li>[MNG-7252] - 修复由 dependency:analyze 发出的警告</li> 
 <li>[MNG-7254] - 由于 JDK-8195129，为 Jansi 扩展 Windows 本地库。</li> 
</ul> 
<p style="text-align:left"><strong>Dependency upgrade</strong></p> 
<ul> 
 <li>[MNG-6818] - 升级 Plexus Utils 至 3.3.0</li> 
 <li>[MNG-6841] - 升级 Plexus Interpolation 到 1.26</li> 
 <li>[MNG-7246] - 将 Plexus Cipher 和 Sec Dispatcher 升级至 2.0</li> 
 <li>[MNG-7250] - 将 Sisu Inject/Plexus 升级至 0.3.5</li> 
</ul> 
<p>详情可查看更新公告： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaven.apache.org%2Fdocs%2F3.8.3%2Frelease-notes.html" target="_blank">https://maven.apache.org/docs/3.8.3/release-notes.html</a></p>
                                        </div>
                                      
</div>
            