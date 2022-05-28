
---
title: '墨干编辑器 v1.0.4 已经发布，基于 GNU TeXmacs 的结构化编辑器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8456'
author: 开源中国
comments: false
date: Sat, 28 May 2022 08:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8456'
---

<div>   
<div class="content">
                                                                                            <p>墨干编辑器 v1.0.4 已经发布，基于 GNU TeXmacs 的结构化编辑器</p> 
<p>此版本更新内容包括：</p> 
<h2>马上下载</h2> 
<table> 
 <thead> 
  <tr> 
   <th>点我下载</th> 
   <th>系统</th> 
   <th>MD5校验</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td><a href="https://gitee.com/link?target=https%3A%2F%2Fgitcode.net%2FXmacsLabs%2Fmogan%2Fuploads%2F089b3b73cd4fbbaa88ff170c0c3f1866%2FMogan-v1.0.4-64bit-installer.exe" target="_blank">点我</a></td> 
   <td>Windows 64位</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td><a href="https://gitee.com/link?target=https%3A%2F%2Fgitcode.net%2FXmacsLabs%2Fmogan%2Fuploads%2F3d49cab60a89988815c658d7e2dc9326%2FMogan-v1.0.4-32bit-installer.exe" target="_blank">点我</a></td> 
   <td>Windows 32位</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td><a href="https://gitee.com/link?target=https%3A%2F%2Fgitcode.net%2FXmacsLabs%2Fmogan%2Fuploads%2F2d713e9f9f19b9120f34e3b2176fcc36%2FMogan_v1.0.4.dmg" target="_blank">点我</a></td> 
   <td>macOS >= 10.15</td> 
   <td> </td> 
  </tr> 
 </tbody> 
</table> 
<h2>马上观看<a href="https://gitee.com/link?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1jY4y1L7eX" target="_blank">发布会视频</a></h2> 
<h2>墨干编辑器V1.0.4是V1.0.x系列最后一个版本。</h2> 
<h2>墨干编辑器的宗旨</h2> 
<p>总结一下墨干编辑器V1.0.4和GNU TeXmacs 2.1.1的三大区别： ① 墨干编辑器优先服务教育，尤其是中学教育，基于TeXmacs，从软件本身角度上讲，墨干编辑器会尽力降低TeXmacs的使用门槛。 ② 墨干编辑器是墨者实验室旗下结构化编辑器，将会和墨者实验室旗下墨客星球深度集成。墨客星球致力于解决网络上TeXmacs文档匮乏的现状，是科技和教育领域的内容平台。 ③ 墨干编辑器V1.0.4基于GNU TeXmacs 2.1.1定制，采用高性能的S7 Scheme脚本引擎，并且已经升级到了Qt 5.15.x。</p> 
<h2>重要变更</h2> 
<ul> 
 <li>经过多次迭代，S7 Scheme脚本引擎对于初级用户的常用功能来说，已经十分稳定流畅</li> 
 <li>通过 帮助→墨客星球 ，只要连接互联网，就可以免费获得 
  <ul> 
   <li>2021年十份高考数学试题真题（例如：<a href="https://gitee.com/link?target=https%3A%2F%2Fwww.slidestalk.com%2Fu282%2Fzjmath202182681" target="_blank">示说网PDF在线查看：2021年浙江高考数学试题</a>）</li> 
   <li>基础数学结构和希腊字母的输入方式，并配有<a href="https://gitee.com/link?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1tU4y1171q" target="_blank">B站教学视频合集</a>（共六个10分钟以内的视频）</li> 
  </ul> </li> 
 <li><strong>插件：</strong> 修复Gnuplot插件若干问题，并录制Gnuplot插件<a href="https://gitee.com/link?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1mS4y1B7Hd" target="_blank">安装</a>和<a href="https://gitee.com/link?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1K34y1E7dp" target="_blank">使用</a>两个教学视频，可用于中学教育中函数图像的绘制</li> 
 <li><strong>插件：</strong> 内置200K以内的<a href="https://gitee.com/link?target=http%3A%2F%2Feukleides.org%2F" target="_blank">欧几里得绘图软件</a>可执行文件，欧几里得插件默认可用（Windows平台仍需从应用商店安装Python），可用于中学教育中的平面几何教学</li> 
 <li><strong>修复了困扰TeXmacs中文用户多年的中文输入法漏字（非期望提交上屏）的问题</strong></li> 
 <li><strong>修复了 帮助→查找→文档 弹窗使用中文输入法直接崩溃的问题</strong></li> 
 <li><strong>修复了远程文档中非TeXmacs文档链接的跳转问题，V1.0.4开始，非TeXmacs文档链接可以直接跳转到浏览器打开</strong></li> 
 <li>修复了分段函数的排版问题，由于该修复是临时解决方案，暂时没有反馈到上游GNU TeXmacs代码仓库</li> 
 <li><strong>易用性：</strong> 在右键菜单中顶部增加了复制、剪切、粘贴三个菜单项，更加符合用户日常使用习惯</li> 
 <li><strong>易用性：</strong> 在中文文档中，新增一系列按键序列转化以方便输入①②③，例如：@1用于输入①</li> 
 <li><strong>易用性：</strong> 调整了一些TeXmacs的默认配置，比如默认使用Emacs快捷键，具体请看发布会视频</li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/XmacsLabs/mogan/releases/v1.0.4">https://gitee.com/XmacsLabs/mogan/releases/v1.0.4</a></p>
                                        </div>
                                      
</div>
            