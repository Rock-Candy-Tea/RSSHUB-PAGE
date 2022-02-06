
---
title: 'x-easypdf v2.7.0 已经发布，PDF 构建工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6955'
author: 开源中国
comments: false
date: Sat, 05 Feb 2022 14:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6955'
---

<div>   
<div class="content">
                                                                                            <p>x-easypdf v2.7.0 已经发布，pdf 构建工具</p> 
<p>本次更新内容如下：</p> 
<p>新特性：</p> 
<ol> 
 <li>XEasyPdfText文本组件新增设置下划线的方法</li> 
 <li>XEasyPdfText文本组件新增设置下划线颜色的方法</li> 
 <li>XEasyPdfText文本组件新增设置下划线宽度的方法</li> 
 <li>XEasyPdfText文本组件新增设置删除线的方法</li> 
 <li>XEasyPdfText文本组件新增设置删除线颜色的方法</li> 
 <li>XEasyPdfText文本组件新增设置高亮显示的方法</li> 
 <li>XEasyPdfText文本组件新增设置垂直居中的方法</li> 
 <li>XEasyPdfText文本组件新增开启水平垂直居中的方法</li> 
 <li>XEasyPdfText文本组件新增设置超链接的方法</li> 
 <li>XEasyPdfText文本组件新增设置评论的方法</li> 
 <li>XEasyPdfText文本组件新增开启整行旋转的方法</li> 
 <li>XEasyPdfImage图片组件新增设置垂直居中的方法</li> 
 <li>XEasyPdfImage图片组件新增开启水平垂直居中的方法</li> 
 <li>XEasyPdfDocument文档新增刷新方法（临时保存文件，用于创建较大文档）</li> 
 <li>XEasyPdfDocument文档新增设置临时目录方法（临时文件保存路径，用于创建较大文档）</li> 
 <li>XEasyPdfDocument文档新增获取文档替换器的方法</li> 
 <li>新增XEasyPdfDocumentReplacer文档替换器</li> 
 <li>XEasyPdfDocumentReplacer文档替换器新增文本替换的方法（支持正则替换）</li> 
 <li>XEasyPdfDocumentReplacer文档替换器新增图片替换的方法</li> 
 <li>XEasyPdfDocumentExtractor文档提取器新增提取表单的方法</li> 
 <li>新增XEasyPdfCircle圆形组件</li> 
 <li>新增XEasyPdfPositionStyle位置样式</li> 
 <li>XEasyPdfTable表格组件新增表头行设置的方法</li> 
 <li>XEasyPdfTable表格组件新增自动表头开启的方法</li> 
</ol> 
<p>原有变更：</p> 
<ol> 
 <li>XEasyPdfText文本组件#setStyle方法变更为#setHorizontalStyle方法</li> 
 <li>XEasyPdfImage图片组件#setStyle方法变更为#setHorizontalStyle方法</li> 
 <li>XEasyPdfImage图片组件#enableVerticalCenterStyle方法变更为#setVerticalStyle方法</li> 
 <li>XEasyPdfCell单元格#addContent方法参数由列表变更为单个</li> 
 <li>移除XEasyPdfTableStyle表格样式</li> 
 <li>移除XEasyPdfImageStyle图片样式</li> 
 <li>移除XEasyPdfTextStyle文本样式</li> 
 <li>移除XEasyPdfSimpleTable简单表格组件（可使用XEasyPdfTable表格组件替换）</li> 
</ol> 
<p>问题修复：</p> 
<ol> 
 <li>XEasyPdfText文本组件手动分行失效问题</li> 
 <li>加载源文档添加水印内存溢出问题（issue#I4RGGV，issue#I4MNGP）</li> 
 <li>创建大文档内存溢出问题，可调用flush暂存解决（issue#I4NZXJ，issue#I3TASO）</li> 
</ol> 
<p>详情查看：<a href="https://gitee.com/xsxgit/x-easypdf/releases/v2.7.0">https://gitee.com/xsxgit/x-easypdf/releases/v2.7.0</a></p>
                                        </div>
                                      
</div>
            