
---
title: '用JavaScript截取浏览器屏幕成pdf文档'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a7640e5f3b54ecdaf4029dc42750055~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 22:56:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a7640e5f3b54ecdaf4029dc42750055~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、先上效果用的是 html2canvas这个官方插件</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a7640e5f3b54ecdaf4029dc42750055~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">上代码</h2>
<p><strong>主页代码</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="https://unpkg.com/element-ui/lib/theme-chalk/index.css" />
    <style>

    </style>
</head>

<body>
    <div id="app">
        <el-tag size="mini" style="cursor: pointer; text-align: center;" @click="screenshot">下载</el-tag> <br> <br>
        <el-row>
            <el-button>默认按钮</el-button> <br>
            <el-button type="primary">主要按钮</el-button><br>
            <el-button type="success">成功按钮</el-button><br>
            <el-button type="info">信息按钮</el-button><br>
            <el-button type="warning">警告按钮</el-button><br>
            <el-button type="danger">危险按钮</el-button><br>
            <el-button icon="el-icon-search" circle></el-button><br>
            <el-button type="primary" icon="el-icon-edit" circle></el-button><br>
            <el-button type="success" icon="el-icon-check" circle></el-button><br>
            <el-button type="info" icon="el-icon-message" circle></el-button><br>
            <el-button type="warning" icon="el-icon-star-off" circle></el-button><br>
            <el-button type="danger" icon="el-icon-delete" circle></el-button><br>
            <el-button plain>朴素按钮</el-button><br>
            <el-button type="primary" plain>主要按钮</el-button><br>
            <el-button type="success" plain>成功按钮</el-button><br>
            <el-button type="info" plain>信息按钮</el-button><br>
            <el-button type="warning" plain>警告按钮</el-button><br>
            <el-button type="danger" plain>危险按钮</el-button><br><br>
            <el-button round>圆角按钮</el-button><br>
            <el-button type="primary" round>主要按钮</el-button><br>
            <el-button type="success" round>成功按钮</el-button><br>
            <el-button type="info" round>信息按钮</el-button><br>
            <el-button type="warning" round>警告按钮</el-button><br>
            <el-button type="danger" round>危险按钮</el-button><br>
        </el-row>

    </div>
    <script src="https://unpkg.com/vue/dist/vue.js"></script>
    <script src="https://cdn.bootcdn.net/ajax/libs/vue/2.6.2/vue.js"></script>
    <!-- 引入组件库 -->
    <script src="https://unpkg.com/element-ui/lib/index.js"></script>

     <!-- 长截图 -->
    <script src="https://cdn.bootcdn.net/ajax/libs/html2canvas/0.5.0-beta4/html2canvas.js"></script>
<!-- pdf文档使用-->
    <script src="https://cdn.bootcdn.net/ajax/libs/jspdf/2.3.1/jspdf.es.min.js"></script>
    <script>
        new Vue(&#123;
            el: "#app",
            data() &#123;
                return &#123;

                &#125;;
            &#125;,
            methods: &#123;
                //长截图
                screenshot() &#123;
                    var that = this;
                    that.$confirm('是否长截屏?', '提示', &#123;
                        confirmButtonText: '确定',
                        cancelButtonText: '取消',
                        type: 'warning'
                    &#125;).then(() => &#123;
                        const loading = this.$loading(&#123;
                            lock: true,
                        &#125;);
                        setTimeout(() => &#123;
                            html2canvas(document.getElementById("app"), &#123;
                                allowTaint: true,
                                taintTest: true,
                                useCORS: true,
                                onrendered: function (canvas) &#123;
                                    var url = canvas.toDataURL("image/png");
                                    loading.close();
                                    // that.uploadFile(url);
                                    var contentWidth = canvas.width;
                                    var contentHeight = canvas.height;

                                    //一页pdf显示html页面生成的canvas高度;
                                    var pageHeight = contentWidth / 592.28 * 841.89;
                                    //未生成pdf的html页面高度
                                    var leftHeight = contentHeight;
                                    //页面偏移
                                    var position = 0;
                                    //a4纸的尺寸[595.28,841.89]，html页面生成的canvas在pdf中图片的宽高
                                    var imgWidth = 595.28;
                                    var imgHeight = 592.28 / contentWidth * contentHeight;

                                    var pdf = new jsPDF('', 'pt', 'a4');

                                    //有两个高度需要区分，一个是html页面的实际高度，和生成pdf的页面高度(841.89)
                                    //当内容未超过pdf一页显示的范围，无需分页
                                    if (leftHeight < pageHeight) &#123;
                                        pdf.addImage(url, 'JPEG', 0, 0, imgWidth, imgHeight);
                                    &#125; else &#123;
                                        while (leftHeight > 0) &#123;
                                            pdf.addImage(url, 'JPEG', 0, position, imgWidth, imgHeight)
                                            leftHeight -= pageHeight;
                                            position -= 841.89;
                                            //避免添加空白页
                                            if (leftHeight > 0) &#123;
                                                pdf.addPage();
                                            &#125;
                                        &#125;
                                    &#125;

                                    pdf.save('导出名称' + (new Date()).getTime() + '.pdf'); //导出名称
                                &#125;
                            &#125;);
                        &#125;, 500);
                    &#125;).catch(() => &#123;
                        that.$message(&#123;
                            type: 'info',
                            message: '已取消'
                        &#125;);
                    &#125;);
                &#125;,
            &#125;,
        &#125;);
    </script>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>综上就是把浏览器当前页面转换成 pdf格式，如有不懂留言为您解答</p>
<p><strong>最后附上html2canvas官网地址</strong>： <a href="https://link.juejin.cn/?target=http%3A%2F%2Fhtml2canvas.hertzen.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://html2canvas.hertzen.com/" ref="nofollow noopener noreferrer">html2canvas.hertzen.com/</a></p></div>  
</div>
            