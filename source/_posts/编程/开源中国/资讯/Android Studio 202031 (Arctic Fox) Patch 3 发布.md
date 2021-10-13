
---
title: 'Android Studio 2020.3.1 (Arctic Fox) Patch 3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0729/184704_bpUM_2720166.png'
author: 开源中国
comments: false
date: Wed, 13 Oct 2021 07:02:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0729/184704_bpUM_2720166.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="color:rgba(0, 0, 0, 0.87)">Android Studio </span>2020.3.1（代号"<span style="color:rgba(0, 0, 0, 0.87)">Arctic Fox"</span>）稳定版<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroidstudio.googleblog.com%2F2021%2F10%2Fandroid-studio-arctic-fox-202031-patch.html" target="_blank">已发布</a>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">从 2020.3.1 起，Android Studio 开始启用<a href="https://www.oschina.net/news/152848/as-arctic-fox-stable" target="_blank">新的版本号命名方案</a>。2020.3.1 即为原计划的 4.3。<a href="https://www.oschina.net/news/142143/android-studio-arctic-fox-beta" target="_blank">谷歌称</a>采用新的方案主要是为了与 IntelliJ 的版本对齐。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://static.oschina.net/uploads/space/2021/0729/184704_bpUM_2720166.png" referrerpolicy="no-referrer"></p> 
<p>此版本的更新内容主要是 Bugfix：</p> 
<div style="margin-left:0; margin-right:0; text-align:start">
 <strong>Android Gradle Plugin</strong>
</div> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <ul style="margin-left:0; margin-right:0"> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F198453608" target="_blank">Issue #198453608</a>: <span style="color:rgba(0, 0, 0, 0.87)">lint 独立插件无法正确处理 gradleApi() 依赖项</span></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F183632446" target="_blank">Issue #183632446</a>: 当 Gradle build 在 Studio 之外运行时会触发 JPS build</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F198667126" target="_blank">Issue #198667126</a>: <span style="color:rgba(0, 0, 0, 0.87)">在包含生成源的处理器的项目中同时启用 KSP 和 Kapt 会破坏 BundleLibraryClassesInputs</span></li> 
 </ul> 
</div> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <div style="margin-left:0; margin-right:0">
  <strong>C++ Editor</strong>
 </div> 
 <div style="margin-left:0; margin-right:0"> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F197323118" target="_blank">Issue #197323118</a>:  <span style="color:rgba(0, 0, 0, 0.87)">UI 因后台长时间的 JniReferencesSearch 计算而被冻结</span></li> 
  </ul> 
  <p><strong>Database Inspector </strong></p> 
 </div> 
 <div style="margin-left:0; margin-right:0"> 
  <div style="margin-left:0; margin-right:0"> 
   <ul style="margin-left:0; margin-right:0"> 
    <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F161081452" target="_blank">Issue #161081452</a>: 支持保存 DBs</li> 
    <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F195968515" target="_blank">Issue #195968515</a>: <span style="color:rgba(0, 0, 0, 0.87)">当路径中有空格时</span><span style="color:rgba(0, 0, 0, 0.87)">，无法使用 </span>App Inspection/Database Inspector <span style="color:rgba(0, 0, 0, 0.87)">导出数据</span></li> 
   </ul> 
   <div style="margin-left:0; margin-right:0"> 
    <div style="margin-left:0; margin-right:0">
     <strong>Dexer (D8) </strong>
    </div> 
    <div style="margin-left:0; margin-right:0"> 
     <ul style="margin-left:0; margin-right:0"> 
      <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F197625454" target="_blank">Issue #197625454</a>: Java lambda 在对 class 进行 subclass 操作时导致意外行为</li> 
     </ul> 
    </div> 
   </div> 
  </div> 
 </div> 
</div> 
<div style="margin-left:0; margin-right:0; text-align:start">
 <strong>Shrinker (R8)</strong>
</div> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <ul style="margin-left:0; margin-right:0"> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F197754200" target="_blank">Issue #197754200</a>: 'Cannot constrain type' error during r8 minification</li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2Fissues%2F200057495" target="_blank">Issue #200057495</a>: 运行 R8 3.0.69 (from AGP 7.0.2) 和 3.0.72 时出现问题</li> 
 </ul> 
</div> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fstudio%2Freleases%23arctic-fox" target="_blank">详情查看 release notes</a>。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fstudio%2F%23downloads" target="_blank">https://developer.android.com/studio/#downloads</a></p>
                                        </div>
                                      
</div>
            