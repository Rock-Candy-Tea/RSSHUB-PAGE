
---
title: 'Android Studio Bumblebee Canary 11 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5877'
author: 开源中国
comments: false
date: Sun, 05 Sep 2021 08:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5877'
---

<div>   
<div class="content">
                                                                                            <p>Android Studio Bumblebee | 2021.1.1 Canary 11 现已发布，此次更新内容主要为 bug 修复 。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>Android Gradle 插件 
  <ul> 
   <li>TypedefRemover 使用 ASM5，与需要使用 ASM7 的 JDK 11 源代码不兼容</li> 
   <li>AGP 会压缩单元测试 .apk 文件中的所有资源，而不考虑 aaptOptions.noCompress</li> 
   <li>Android 库插件应提供一种构建源代码 jar 的方式</li> 
   <li>AGP 7.0.0 稳定版在执行到 libraryVariants.all &#123; applicationId &#125; 时会抛出 ExternalApiUsageException</li> 
   <li>使用 Android Gradle 构建工具 4.1.2（或 4.2.x）以及 Gradle 6.5 时，Jacoco 报告不显示源代码行</li> 
  </ul> </li> 
 <li>设计工具 
  <ul> 
   <li>矢量可绘制对象预览 bug</li> 
  </ul> </li> 
 <li>lint 
  <ul> 
   <li>lint：未包含有效的注册表清单项 (Lint-Registry-v2)</li> 
  </ul> </li> 
 <li>网络 
  <ul> 
   <li>网络性能分析器不会重复显示多个同名的标题</li> 
  </ul> </li> 
 <li>Resource Manager 
  <ul> 
   <li>(Windows) New -> Vector Asset -> picture.svg：生成的 xml 文件中的“减号”字符 (-) 无效</li> 
  </ul> </li> 
 <li>运行测试 
  <ul> 
   <li>Android Studio Bumblebee：对插桩测试使用“Run Configurations”对话框时，会执行错误的测试</li> 
   <li>Gradle 测试运行程序无法用于 AndroidX 项目</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroidstudio.googleblog.com%2F2021%2F09%2Fandroid-studio-bumblebee-canary-11.html" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            