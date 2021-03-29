
---
title: 'digiKam 7.2.0 发布，KDE 数字相片管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9249'
author: 开源中国
comments: false
date: Mon, 29 Mar 2021 07:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9249'
---

<div>   
<div class="content">
                                                                                            <p>DigiKam 是 KDE 桌面环境的影像管理和编辑程序，支持所有主要图像格式，并可以组织目录为基础的照片收藏，或按日期、时间、或标签的动态相册。用户还可以对图像添加标题和注释，搜索他们和透过智能文件夹保存搜索。添加插件还可以输出到 Flickr 的相册、Gallery2、谷歌地球的 KML 文件、Simpleviewer、刻录成光盘或创建 Web 画廊。</p> 
<p>近日，digiKam 7.2.0 正式发布，本次更新的部分内容如下：</p> 
<h3>高级重命名</h3> 
<p>在收藏中批量重命名项目的工具已经收到了大量的代码审查，以修复老版本中的功能障碍。这提高了稳定性和可用性。</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D091161" target="_blank">091161</a> 批量处理 —— 重命名问题；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D109517" target="_blank">109517</a> 当重新排列或重新命名相册时，照片标签和注释会丢失；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D135374" target="_blank">135374</a> 重命名图片文件：增加"查找和替换"的可能性；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D237805" target="_blank">237805</a> 在批次队列管理器中使用文件转换工具时，使用元数据重命名文件失败；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D244559" target="_blank">244559</a> 在批处理中重命名文件时发生崩溃；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D249148" target="_blank">249148</a> digiKam 在重命名文件时崩溃；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D251768" target="_blank">251768</a> 从相机导入时，digiKam 自定义文件重命名选项被忽略；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D255830" target="_blank">255830</a> 使用德文 Umlauts 重命名文件时崩溃；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D256314" target="_blank">256314</a> 重命名 jpegs 格式时崩溃；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D257099" target="_blank">257099</a> 如果选择了多个文件，则在退出“重命名”对话框时崩溃；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D430684" target="_blank">430684</a> 重命名 mp4 文件时 —— 元数据字段没有值；</li> 
</ul> 
<h3>相册</h3> 
<p>相册管理得到了改进，修正了数据库，更好地支持特殊情况下的项目分组。过滤引擎也已经修复，以加快用户查询的速度，并更好地支持通配符。</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D104009" target="_blank">104009</a> 照片移至其他相册后仍留在原相册中；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D114189" target="_blank">114189</a> 添加一个可以设置“图片创建权限”的选项；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D432732" target="_blank">432732</a> Wish: 在文本过滤器中支持通配符；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D430179" target="_blank">430179</a> 缩略图排列顺序；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D434017" target="_blank">434017</a> 嵌入在某些 jpg 照片文件中的元数据已消失；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D427067" target="_blank">427067</a> 相册不显示缩略图；时间轴仅显示 1 个文件夹；</li> 
</ul> 
<h3>批处理队列管理器</h3> 
<p>对队列中的项目进行批处理的工具，进行了一些改进和修正，特别是在处理时对可移动项目进行重新管理。</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D430818" target="_blank">430818</a> 在批处理队列管理器中，"运行"命令，总是执行第一个队列；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D430876" target="_blank">430876</a> 重命名图像而不更改任何属性；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D431660" target="_blank">431660</a> BQM 将输出文件存储在比实际目标高一级目录的位置；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D432619" target="_blank">432619</a> Batch Queue Manager 不使用原始相册作为目标；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D434716" target="_blank">434716</a> 使用同步服务（QMAP，Synology 等）旋转多个图像时出现严重问题；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D424437" target="_blank">424437</a> 批量删除重复项；</li> 
</ul> 
<h3>MacOS</h3> 
<p>digiKam 已完全支持 macOS Big Sur，但目前还没有原生支持 Apple Silicon 架构，但在 Apple Rosetta 2 模拟器中运行良好。</p> 
<h3>数据库</h3> 
<p>数据库是主要的应用组件，它被所有的照片管理功能所使用，如搜索工具、元数据引擎、人脸引擎、相似工具等。我们提高了启动时扫描采集阶段的稳定性和速度，Plasma/Baloo 支持，以及维护操作。</p> 
<p>数据库方案已经升级到新的版本，升级后改变了内部标签树的表示方式，从 VIEW 类型迁移到 TABLE 类型，以获得更好的性能。</p> 
<p>我们建议在升级到新版本之前备份你的数据库文件，否则你将无法回到以前的应用版本。Mysql/Mariadb 的支持也已修复，以便更好地支持 NAS 服务器。</p> 
<h3>面部检测、识别</h3> 
<p>我们使用了一个新的数据模型 Yolo。在复杂的拍摄条件下，可以检测到更多图像上的人脸。在处理速度上有所降低，并彻底解决了旧有的内存分配错误的问题。检测红眼的算法从人脸引擎中获得了使用 Yolo 数据模型的机会。红眼检测的效果更好。</p> 
<p>由于人脸数据模型是一个巨大的文件，为了优化应用程序的大小，它们已经从应用程序中默认将其删除，改为按需下载。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.digikam.org%2Fnews%2F2021-03-22-7.2.0_release_announcement%2F" target="_blank">https://www.digikam.org/news/2021-03-22-7.2.0_release_announcement/</a></p>
                                        </div>
                                      
</div>
            