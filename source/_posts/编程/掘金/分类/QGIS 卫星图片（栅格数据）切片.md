
---
title: 'QGIS 卫星图片（栅格数据）切片'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa275015690b423fb0aec45e42d5a8f5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 01:58:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa275015690b423fb0aec45e42d5a8f5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">添加栅格图片</h3>
<p>点击 “<strong>打开数据源管理器</strong>”</p>
<p>点击  “<strong>栅格</strong>”</p>
<p>选择要切片的卫星照片（tiff格式），地图的高清卫星照片可以在 Bigemap 、水经注等软件下载。</p>
<p>点击 ”<strong>添加</strong>“</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa275015690b423fb0aec45e42d5a8f5~tplv-k3u1fbpfcp-watermark.image" alt="image-20210817171948971" loading="lazy" referrerpolicy="no-referrer"></p>
<p>卫星照片（tiff格式） 添加成功</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d17f9728a6e4ec08a470e1a93826588~tplv-k3u1fbpfcp-watermark.image" alt="image-20210817173649010" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">切片</h3>
<p>面板上右键，勾选”<strong>工具箱面板</strong>“</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/071660c49db346cfb23ba4dee0948194~tplv-k3u1fbpfcp-watermark.image" alt="image-20210817174102232" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在工具箱中，选择”<strong>栅格工具</strong>“下的”生成XYZ瓦片（目录）“</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c0f5b26af034e959bd01e1d95ece996~tplv-k3u1fbpfcp-watermark.image" alt="image-20210817174235983" loading="lazy" referrerpolicy="no-referrer"></p>
<p>填写 Extent （切片范围） ，以及输出目录</p>
<p>点击”<strong>运行</strong>“</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d59ad9ab1449465da4f814e0de4d49fe~tplv-k3u1fbpfcp-watermark.image" alt="image-20210817175028855" loading="lazy" referrerpolicy="no-referrer"></p>
<p>生成瓦片成功</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce28ea3ddd244554890d79d75a8966a8~tplv-k3u1fbpfcp-watermark.image" alt="image-20210817175422216" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">查看瓦片</h3>
<p>打开输出目录查看瓦片，用chrome 浏览器打开 demo.html</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/026c31d50bbf4fb3807e1467cd74a47b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210817175549688" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9b8620ec81b48a39b969f4baec5849b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210817175638753" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            