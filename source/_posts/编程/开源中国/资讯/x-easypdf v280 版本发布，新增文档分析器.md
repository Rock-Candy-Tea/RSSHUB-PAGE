
---
title: 'x-easypdf v2.8.0 版本发布，新增文档分析器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5828'
author: 开源中国
comments: false
date: Sun, 24 Apr 2022 22:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5828'
---

<div>   
<div class="content">
                                                                                            <p>x-easypdf基于pdfbox二次封装，极大降低使用门槛，以组件化的形式进行pdf的构建。简单易用，仅需一行代码，便可完成pdf的相关操作。</p> 
<p>本次更新内容如下：</p> 
<p>新特性：<br> 1. 新增文档分析器XEasyPdfDocumentAnalyzer<br> 2. XEasyPdfPage页面新增获取文档获取每毫米像素点的方法<br> 3. XEasyPdfPage页面新增获取页面宽度的方法<br> 4. XEasyPdfPage页面新增获取页面高度的方法<br> 5. XEasyPdfPage页面新增获取页面尺寸的方法<br> 6. XEasyPdfPage页面新增获取当前页面索引占位符的方法<br> 7. XEasyPdfHeader页眉新增获取总页码占位符的方法<br> 8. XEasyPdfHeader页眉新增获取当前页码占位符<br> 9. XEasyPdfFooter页脚新增获取总页码占位符的方法<br> 10. XEasyPdfFooter页脚新增获取当前页码占位符<br> 11. XEasyPdfText文本组件新增设置最大高度的方法<br> 12. XEasyPdfText文本组件新增获取字体路径的方法<br> 13. XEasyPdfTable表格组件新增关闭自动拆分行（分页时，自动拆分行数据）的方法，默认开启<br> 14. XEasyPdfTable表格组件新增插入表格行的方法</p> 
<p>原有变更：<br> 1. 优化XEasyPdfPage页面获取最新页面逻辑<br> 2. 各组件移除是否完成绘制的方法<br> 3. 移除XEasyPdfImage图片组件设置图片压缩模式的方法<br> 4. 移除各组件中的PDFont字体属性<br> 5. pdfbox依赖更新到2.0.26</p> 
<p>问题修复：<br> 1. 修复获取总页码的问题（issue#I52M1S）<br> 2. 修复XEasyPdfTable表格组件跨页显示错误问题（issue#I4V5JO）</p>
                                        </div>
                                      
</div>
            