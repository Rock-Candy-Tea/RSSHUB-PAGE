
---
title: 'PeaZip 8.4.0 发布，压缩管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1118'
author: 开源中国
comments: false
date: Fri, 17 Dec 2021 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1118'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">PeaZip 是一个适用于 Windows 和 Linux 的免费文件存档工具和 rar 提取器，可处理 200 多种存档类型（7z, ace, arc, bz2, cab, gz, iso, paq, pea, rar, tar, wim, zip, zipx...），处理跨区存档（001, r01, z01...）并支持多种存档加密标准。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">该项目旨在为多种开源技术（7-Zip、FreeArc、PAQ、PEA、UPX）提供一个跨平台、可移植的 GUI 前端，专注于文件和档案管理，以及安全（强加密、双因素认证、加密密码管理器、安全删除）。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">PeaZip 8.4.0 正式发布，该版本更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">后端：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Pea 1.05</li> 
 <li>7z 21.06 在 Darwin/macOS、Linux 和 Windows 上默认使用。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">代码：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修正了当临时工作路径被设置为用户的 temp 时的问题 
  <ul style="margin-left:0; margin-right:0"> 
   <li>(Windows) 修正了对不存在的输出目录的不必要的确认信息</li> 
   <li>修正了智能提取不能去除额外的嵌套层的问题</li> 
  </ul> </li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">文件管理器：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>增加了单核和多核性能基准，在主菜单工具>系统基准中 
  <ul style="margin-left:0; margin-right:0"> 
   <li>该基准执行整数和浮点算术运算</li> 
   <li>基准结果单位是任意的，只是为了在不同平台之间进行比较。 
    <ul style="margin-left:0; margin-right:0"> 
     <li>作为参考，aarm 64 构建下，2020 年 MacBook Air M1 的得分是 100（单核）和 515（多核）</li> 
    </ul> </li> 
  </ul> </li> 
 <li>(Darwin/macOS, Linux) 文件管理器列的菜单可在右键单击状态栏时使用</li> 
 <li>(Darwin/macOS) 改进了文件管理器 
  <ul style="margin-left:0; margin-right:0"> 
   <li>在导航树视图中增加了卷、应用程序和系统/应用程序的链接</li> 
   <li>为 "以……打开" 子菜单添加了自动配置的自定义应用程序</li> 
   <li>在上下文菜单中增加了 macOS 特有的功能，"文件管理器">"系统工具"：启动台、活动监视器、系统偏好设置、磁盘工具</li> 
   <li>从 PeaZip 启动的 PeaUtils 现在可以使用了</li> 
  </ul> </li> 
 <li>语言现在可以从常规设置标签的下拉菜单中改变 
  <ul style="margin-left:0; margin-right:0"> 
   <li>此前允许手动选择语言文件的方法仍然可以从下拉菜单前的链接中获得</li> 
  </ul> </li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">提取和存档：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>新增选项，除非遇到错误，否则不停止存档测试任务的序列 
  <ul style="margin-left:0; margin-right:0"> 
   <li>有了这个设置，除非在归档中发现错误，否则一个成功的归档测试在完成后就会关闭；如果测试失败，错误信息和完整的报告就会显示给用户。</li> 
  </ul> </li> 
 <li>改进对临时工作文件的管理</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpeazip.github.io%2Fchangelog.html" target="_blank">https://peazip.github.io/changelog.html</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            