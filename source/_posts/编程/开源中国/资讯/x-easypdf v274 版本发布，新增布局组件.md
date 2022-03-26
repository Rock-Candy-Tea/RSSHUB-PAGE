
---
title: 'x-easypdf v2.7.4 版本发布，新增布局组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-637cf75193a67c7aa7056d34de8dffe4a0e.png'
author: 开源中国
comments: false
date: Sat, 26 Mar 2022 16:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-637cf75193a67c7aa7056d34de8dffe4a0e.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#40485b">一个用搭积木的方式构建pdf的框架（基于pdfbox）</span></p> 
<pre>本次更新内容如下：

新特性：
<span>1. XEasyPdfDocumentImager</span>文档图像器新增设置图片<span>DPI</span>的方法
<span>2. XEasyPdfTable</span>表格组件支持表格嵌套
<span>3. XEasyPdfRow</span>表格行新增手动分页的方法
<span>4. XEasyPdfCell</span>单元格新增关闭上、下、左、右边框的方法
<span>5. XEasyPdfWatermark</span>水印组件新增设置水印单行文本数的方法
<span>6. XEasyPdfWatermark</span>水印组件新增设置水印文本字符间隔的方法
<span>7. XEasyPdfWatermark</span>水印组件新增设置水印文本行间距的方法
<span>8. XEasyPdfWatermark</span>水印组件新增设置位置坐标的方法
<span>9. </span>新增<span>XEasyPdfHorizontalLayout</span>水平布局组件，支持嵌套任意组件
<span>10. </span>新增<span>XEasyPdfVerticalLayout</span>垂直布局组件，支持嵌套任意组件

原有变更：
无

问题修复：
<span>1. </span>文本替换问题（<span>issue#I4YVA6</span>）
<span>2. </span>使用布局组件可实现文本环绕图片的需求（<span>issue#I4VFXH</span>）</pre> 
<p>布局组件的简单应用：实现文字环绕图片的效果</p> 
<pre><code class="language-java">String filePath = OUTPUT_PATH + "testLayout.pdf";
        String imagePath = OUTPUT_PATH + "test.jpg";
        List<String> leftList = new ArrayList<>();
        List<String> rightList = new ArrayList<>();
        String content = "经过实际测试，目前在访问上述提及的四款广告拦截扩展的页面时，确实是会弹出以下提示";
        boolean isLeft = true;
        // 拆分文本
        while (content.length()>5) &#123;
            if (isLeft) &#123;
                leftList.add(content.substring(0, 5));
                isLeft = false;
            &#125;else &#123;
                rightList.add(content.substring(0, 5));
                isLeft = true;
            &#125;
            content = content.substring(5);
        &#125;
        rightList.add(content);
        // 添加页面
        XEasyPdfHandler.Document.build().addPage(
                // 添加组件
                XEasyPdfHandler.Page.build().addComponent(
                        // 构建垂直布局(包含三行)
                        XEasyPdfHandler.Layout.Vertical.build().setMarginLeft(150F).setMarginTop(200F)
                                // 添加布局组件(第一行)
                                .addLayoutComponent(
                                        // 构建布局组件
                                        XEasyPdfHandler.Layout.Component.build(300F, 20F).setComponent(
                                                // 构建水平布局
                                                XEasyPdfHandler.Layout.Horizontal.build()
                                                        // 添加布局组件
                                                        .addLayoutComponent(
                                                                // 构建布局组件
                                                                XEasyPdfHandler.Layout.Component.build(300F, 20F).setComponent(
                                                                        // 设置文本组件
                                                                        XEasyPdfHandler.Text.build("贵阳贵阳贵阳贵阳贵阳贵阳贵阳贵").setFontSize(20F)
                                                                )
                                                        )
                                        )
                                )
                                // 添加布局组件(第二行)
                                .addLayoutComponent(
                                        // 构建布局组件
                                        XEasyPdfHandler.Layout.Component.build(100F, 100F).setComponent(
                                                // 构建水平布局(包含三列)
                                                XEasyPdfHandler.Layout.Horizontal.build()
                                                        // 添加布局组件
                                                        .addLayoutComponent(
                                                                // 构建布局组件
                                                                XEasyPdfHandler.Layout.Component.build(100F, 100F).setComponent(
                                                                        // 设置文本组件
                                                                        XEasyPdfHandler.Text.build(leftList).setFontSize(20F)
                                                                )
                                                        )
                                                        // 添加布局组件
                                                        .addLayoutComponent(
                                                                // 构建布局组件
                                                                XEasyPdfHandler.Layout.Component.build(100F, 100F).setComponent(
                                                                        // 设置图片组件
                                                                        XEasyPdfHandler.Image.build(new File(imagePath)).disableSelfAdaption()
                                                                )
                                                        )
                                                        // 添加布局组件
                                                        .addLayoutComponent(
                                                                // 构建布局组件
                                                                XEasyPdfHandler.Layout.Component.build(100F, 100F).setComponent(
                                                                        // 设置文本组件
                                                                        XEasyPdfHandler.Text.build(rightList).setFontSize(20F)
                                                                )
                                                        )
                                        )
                                )
                                // 添加布局组件(第三行)
                                .addLayoutComponent(
                                        // 构建布局组件
                                        XEasyPdfHandler.Layout.Component.build(300F, 20F).setComponent(
                                                // 构建水平布局
                                                XEasyPdfHandler.Layout.Horizontal.build()
                                                        // 添加布局组件
                                                        .addLayoutComponent(
                                                                // 构建布局组件
                                                                XEasyPdfHandler.Layout.Component.build(300F, 20F).setComponent(
                                                                        // 设置文本组件
                                                                        XEasyPdfHandler.Text.build("贵阳贵阳贵阳贵阳贵阳贵阳贵阳贵").setFontSize(20F)
                                                                )
                                                        )
                                        )
                                )
                )
                // 保存并关闭
        ).save(filePath).close();</code></pre> 
<p><img alt height="719" src="https://oscimg.oschina.net/oscnet/up-637cf75193a67c7aa7056d34de8dffe4a0e.png" width="797" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            