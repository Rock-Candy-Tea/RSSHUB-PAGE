
---
title: 'kkFileView v4.0.0 发布，文件文档在线预览解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2902'
author: 开源中国
comments: false
date: Tue, 06 Jul 2021 11:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2902'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="text-align:left">kkfileview 文件在线预览</h3> 
<p style="text-align:left">此项目为文件文档在线预览项目解决方案，项目使用流行的 spring boot 搭建，易上手和部署，部署好后可以独立提供预览服务，使用 http 接口访问，不需要和应用集成，具有跨系统跨语言使用的特性。提供 zip/tar.gz 发行包、自定义配置文件、和启动/停止脚本等，极大方便部署使用，同时官方发布 Docker 镜像，方便容器环境中部署使用。基本支持主流办公文档的在线预览，如 doc，docx，dwg, ofd, xls，xlsx，ppt，pptx，pdf，txt，zip，rar，7z，mp3，mp4，flv 图片等等。</p> 
<p style="text-align:left">项目地址：<a href="https://gitee.com/kekingcn/file-online-preview" target="_blank">https://gitee.com/kekingcn/file-online-preview</a></p> 
<p style="text-align:left">项目官网：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkkfileview.keking.cn%2F" target="_blank">https://kkfileview.keking.cn</a></p> 
<p style="text-align:left">Docker 镜像：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2Fr%2Fkeking%2Fkkfileview" target="_blank">https://hub.docker.com/r/keking/kkfileview</a></p> 
<h3 style="text-align:left">本次 v4.0.0 更新内容：</h3> 
<ul> 
 <li>底层集成OpenOffice替换为LibreOffice，Office文件兼容性增强，预览效果提升</li> 
 <li>修复压缩文件目录穿越漏洞</li> 
 <li>修复PPT预览使用PDF模式无效</li> 
 <li>修复PPT图片预览模式前端显示异常</li> 
 <li>新增功能：首页文件上传功能可通过配置实时开启或禁用</li> 
 <li>优化增加Office进程关闭日志</li> 
 <li>优化Windows环境下，查找Office组件逻辑(内置的LibreOffice优先)</li> 
 <li>优化启动Office进程改同步执行</li> 
</ul>
                                        </div>
                                      
</div>
            