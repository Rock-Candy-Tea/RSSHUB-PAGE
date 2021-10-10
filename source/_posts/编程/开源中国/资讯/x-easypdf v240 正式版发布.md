
---
title: 'x-easypdf v2.4.0 正式版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3f7c61cfb1a16f03d6a50975af1322b8dce.png'
author: 开源中国
comments: false
date: Sun, 10 Oct 2021 08:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3f7c61cfb1a16f03d6a50975af1322b8dce.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>本次更新内容如下：</p> 
<p>新特性：<br> 1. 生成pdf时，根据传入路径，自动创建不存在的目录<br> 2. 新增页面组件XEasyPdfPage设置与获取页面背景图片方法<br> 3. 新增pdf助手XEasyPdfHandler获取当前页码占位符方法<br> 4. 内置细、粗、正常三种开源中文字体（思源字体）<br> 5. 新增设置默认字体样式方法（粗、细、正常，默认为正常）（issue#I3SAUR）<br> 6. 新增图片组件XEasyPdfImage开启图片垂直居中方法<br> 7. 优化文本分行算法<br> 8. 优化表单填充逻辑</p> 
<p>原有变更：<br> 1. 移除所有setFont与getFont方法<br> 2. 文档XEasyPdfDocument#fillForm方法变更为formFiller，返回值变为XEasyPdfDocumentFormFiller(表单填充器)<br> 3. 调整包结构，移除wiki.xsx.core.pdf.page包，原包下相关类移动到wiki.xsx.core.pdf.doc包下</p> 
<p>问题修复：<br> 1. 修复资源路径下读取不到字体问题<br> 2. 修复页脚与文本内容在特殊场景下重叠问题<br> 3. 修复表单填充找不到字体问题(issue#I44LTE，issue#I438MM，issue#I3IR71)<br> 4. 修复未安装字体时乱码问题(issue#I45QMY)<br> 5. 优化图片压缩清晰度（issue#I3T51S，issue#I47XUH）</p> 
<p><img alt height="884" src="https://oscimg.oschina.net/oscnet/up-3f7c61cfb1a16f03d6a50975af1322b8dce.png" width="625" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            