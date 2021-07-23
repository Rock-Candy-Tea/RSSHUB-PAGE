
---
title: 'Android Studio Bumblebee Canary 4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7311'
author: 开源中国
comments: false
date: Fri, 23 Jul 2021 06:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7311'
---

<div>   
<div class="content">
                                                                                            <p>Android Studio Bumblebee Canary 4  现已发布，此次更新主要修复了以下问题。</p> 
<ul> 
 <li><strong>Android Gradle 插件</strong> 
  <ul> 
   <li>采用默认 res 支持 (false) 的测试装置仍然有 resvalue 生成的文件夹</li> 
   <li>我们在 gradle-api 中需要一个 Version 接口</li> 
   <li>4.2.0 会生成缺少类的测试 APK，可能是由混合的 java/kotlin 源代码集所致</li> 
   <li>下一个要公开的工件应为 CLASSES</li> 
   <li>注入的 Android 支持版本“202.7660.26.42.7322048”无效，格式应为“wxyz”- 在执行 Compose 示例时收到此错误</li> 
   <li>重新启用 DSL 创建 vis 实现类，而不是接口</li> 
  </ul> </li> 
 <li><strong>Android Studio</strong> 
  <ul> 
   <li>UI_MODE_NIGHT_YES 无法在预览版中使用</li> 
  </ul> </li> 
 <li><strong>布局编辑器</strong> 
  <ul> 
   <li>TextClock 对象的布局预览有问题</li> 
   <li>预览版与正在运行的应用不完全一样 | ?attr 在 XML [矢量可绘制对象] 的 fillColor 中不受支持</li> 
   <li>添加“androidx.preference:preference:1.1.0”后，Android Studio 布局预览将无法用于原生 android.preference.Preference 和自定义偏好设置</li> 
   <li>Android Studio 4.0 缩放灵敏度</li> 
   <li>布局渲染引擎：更新 strings.xml 时缺少 Unicode 字符</li> 
   <li>Android Studio 崩溃</li> 
  </ul> </li> 
 <li><strong>lint</strong> 
  <ul> 
   <li>lint 循环假正例</li> 
   <li>Android lint 在特定项目中无法查看 androidx.annotation jar</li> 
   <li>@CheckResult 在 lambda 表达式中不起作用</li> 
   <li>“UnknownIssueId”停用后仍会输出警告</li> 
   <li>UnusedResources lint 检查不能针对库正常运行</li> 
   <li>使用 firebase-perf [OutdatedLibrary] 时，即使使用最新版本，也会发生 lint 错误</li> 
  </ul> </li> 
 <li><strong>渲染</strong> 
  <ul> 
   <li>具有透明形状的可绘制对象未正确渲染</li> 
  </ul> </li> 
 <li><strong>资源</strong> 
  <ul> 
   <li>升级到 4.2 后，某些字符串资源中添加了空格</li> 
  </ul> </li> 
 <li><strong>视图绑定</strong> ​​​​​​​ 
  <ul> 
   <li>使用膨胀视图绑定“inflate”方法的静态导入会导致出现未使用的资源</li> 
  </ul> </li> 
 <li><strong>Wear 与 Google 助理配对</strong> ​​​​​​​ 
  <ul> 
   <li>无法从 IJ 启动 Wear 与 Google 助理的配对</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroidstudio.googleblog.com%2F2021%2F07%2Fandroid-studio-bumblebee-canary-4.html" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            