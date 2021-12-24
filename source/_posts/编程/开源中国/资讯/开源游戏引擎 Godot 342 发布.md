
---
title: '开源游戏引擎 Godot 3.4.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7299'
author: 开源中国
comments: false
date: Fri, 24 Dec 2021 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7299'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/news/174577/godot">Godot 3.4.1</a> 刚于日前发布，其中包含了大量的 bug 修复；但随后开发团队就发现该版本的 macOS 渲染出现了回归，可能导致 flickering。新的 Godot 3.4.2 是一个 hotfix release，就用于解决此问题和其他一些在此期间修复的小问题。Godot 3.4.2 是对所有 Godot 3.4 和 3.4.1 用户的推荐升级。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">以下是自 3.4.1-stable 以来的主要变化：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>C#：在尝试编辑<code>.csproj</code>之前检查它是否存在（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F56101" target="_blank">GH-56101</a>）。</li> 
 <li>GUI：修复 BaseButton 对工具提示文本的本地化与快捷方式 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F56109" target="_blank">GH-56109</a> )。</li> 
 <li>Input：Revert #55997“修复使用 Nintendo Switch controller 时的 event spam”( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F56029" target="_blank">GH-56029</a> )。 
  <ul style="margin-left:0; margin-right:0"> 
   <li>这恢复了 3.4.1 中引入的更改，该更改大大降低了模拟操纵杆的灵敏度。</li> 
  </ul> </li> 
 <li>macOS：修复 OpenGL flickering 的回归 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F56059" target="_blank">GH-56059</a> )。</li> 
 <li>Rendering：GLES2：修复了 Android 上截断着色器函数的编译 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F56061" target="_blank">GH-56061</a> )。</li> 
 <li>XR：修复 ARVR 管理视口的尺寸问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F56072" target="_blank">GH-56072</a> )。</li> 
 <li>第三方库更新：mbedtls 2.16.12。</li> 
 <li>API 文档和翻译更新。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgodotengine.org%2Farticle%2Fmaintenance-release-godot-3-4-2" target="_blank">https://godotengine.org/article/maintenance-release-godot-3-4-2</a></p>
                                        </div>
                                      
</div>
            