
---
title: 'Android Studio Bumblebee Canary 1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8279'
author: 开源中国
comments: false
date: Thu, 27 May 2021 06:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8279'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Android Studio Bumblebee Canary 1 现已发布，此次更新主要修复了以下问题。</p> 
<p><strong>Android Gradle Plugin </strong></p> 
<ul> 
 <li>对于未知标志 --class-dir，使用 --help 获取使用信息</li> 
 <li>不要对 DefaultLintModelVariant.shrinkable 进行硬编码</li> 
 <li>支持依赖库中的应用模块安装</li> 
 <li>AGP 7.0.0 Alpha 15 抛出未解决的引用：missingDimensionStrategy</li> 
 <li>Android Lint VectorDrawableCompat 检查发出错误的警告</li> 
 <li>buildConfigField 替换警告打印出的值，可能包含敏感信息</li> 
 <li>ASM 转换的配置缓存问题</li> 
 <li>com.android.databinding:baseLibrary 使用支持遗留库</li> 
</ul> 
<p><strong>Build Tools </strong></p> 
<ul> 
 <li>在AGP 4.2.0-rc01 中，lint.xml 文件被忽略</li> 
</ul> 
<p><strong>Build Variants </strong></p> 
<ul> 
 <li>对于 Kotlin/Kapt 来说，切换缓存变体不能正确工作</li> 
 <li>Build variant 部分总是空的（加载中）</li> 
 <li>复合构建根项目在构建变体选择器工具窗口中显示为 ":"</li> 
</ul> 
<p><strong>Code Analysis</strong></p> 
<ul> 
 <li>Android lint 显示 API 级别检查的误报，以获取已继承的接口中的字段</li> 
</ul> 
<p><strong>Import/Sync</strong></p> 
<ul> 
 <li>Android Studio 用 "assemble" 而不是 ":app:assembleDebug" 进行构建</li> 
 <li>Manifest 索引无法识别生成文件夹中的清单</li> 
 <li>没有办法在构建变量选择工具窗口中搜索模块</li> 
</ul> 
<p><strong>Lint</strong></p> 
<ul> 
 <li>当 LintOptions.absolutePaths 为假时，绝对路径出现在部分结果文件中</li> 
 <li>新的 lint 集成中的 RestrictedApi 检测器的潜在问题</li> 
 <li>RestrictToDetector 抛出 StringIndexOutOfBoundsException</li> 
 <li>通过 lintOptions.enable 启用的问题总是有严重性警告。</li> 
 <li>当只有测试类时，Lint 会给出失败的分析结果</li> 
 <li>ExifInterfaceDetector 的 Lint 检查指的是过时的类</li> 
 <li>Lint 日志中的垃圾邮："不正确的检测器报告禁用问题 ExtraTranslation"</li> 
</ul> 
<p>详细内容请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroidstudio.googleblog.com%2F2021%2F05%2Fandroid-studio-bumblebee-canary-1.html" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            