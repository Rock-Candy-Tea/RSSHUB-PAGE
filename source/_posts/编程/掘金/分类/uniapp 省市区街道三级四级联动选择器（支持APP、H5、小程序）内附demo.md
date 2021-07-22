
---
title: 'uniapp 省市区街道三级四级联动选择器（支持APP、H5、小程序）内附demo'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac2ba89b02c744cf92107ea4a389dbf6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 23:16:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac2ba89b02c744cf92107ea4a389dbf6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">概述</h3>
<ol start="0">
<li>支持uniapp（APP、H5、小程序）省市区街道三级四级联动</li>
<li>支持默认地区或已选择地区显示</li>
<li>数据来源可包括高德地图api、公司封装接口返回</li>
</ol>
<h3 data-id="heading-1">API</h3>
<h4 data-id="heading-2">props</h4>


























<table><thead><tr><th>属性</th><th>必填</th><th>说明</th><th>类型</th><th>默认值</th></tr></thead><tbody><tr><td>areaInfoSelected</td><td>否</td><td>已选择的地址对象或默认显示地址对象，属性有：provinceObj,cityObjareaObj,streetObj</td><td>Object</td><td>&#123;&#125;</td></tr><tr><td>selectAreaLevelLimit</td><td>否</td><td>指定选择的级别数，如只需要选择省市区，则指定值为3</td><td>Number</td><td>4</td></tr></tbody></table>
<h4 data-id="heading-3">events</h4>




















<table><thead><tr><th>事件名</th><th>说明</th><th>返回值</th></tr></thead><tbody><tr><td>cancel</td><td>点击取消按钮时触发</td><td>-</td></tr><tr><td>confirm</td><td>点击确认按钮时触发</td><td>选中的省市区街道地址对象,包含如下属性：fullAreaText,provinceCode,,cityCode,areaCode,streetCode,provinceObj,cityObj,areaObj,streetObj</td></tr></tbody></table>
<h3 data-id="heading-4">作者想说</h3>
<p>欢迎大家留言、评论与star😈</p>
<h3 data-id="heading-5">dcloud传送门：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fext.dcloud.net.cn%2Fplugin%3Fid%3D5671" target="_blank" rel="nofollow noopener noreferrer" title="https://ext.dcloud.net.cn/plugin?id=5671" ref="nofollow noopener noreferrer">ext.dcloud.net.cn/plugin?id=5…</a></h3>
<h3 data-id="heading-6"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>github传送门：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLukeLiou%2FUniappPlugins" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/LukeLiou/UniappPlugins" ref="nofollow noopener noreferrer">github.com/LukeLiou/Un…</a></h3>
<h3 data-id="heading-7"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>个人博客：<a href="https://link.juejin.cn/?target=https%3A%2F%2Flukeliou.github.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://lukeliou.github.io/" ref="nofollow noopener noreferrer">lukeliou.github.io/</a></h3>
<h3 data-id="heading-8">效果图：</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac2ba89b02c744cf92107ea4a389dbf6~tplv-k3u1fbpfcp-watermark.image" alt="UniAddressSelector_watermark_2.gif" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            