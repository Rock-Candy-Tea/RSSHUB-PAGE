
---
title: '文件管理功能重构，MeterSphere 开源持续测试平台 v2.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/c9e19036df6b4a4e92267306ce10f54a~noop.image?_iz=58558&from=article.pc_detail&x-expires=1662370106&x-signature=5DEX9XZBAgrtCtOsie8hpyhtS0s%3D'
author: 开源中国
comments: false
date: Mon, 29 Aug 2022 10:43:00 GMT
thumbnail: 'https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/c9e19036df6b4a4e92267306ce10f54a~noop.image?_iz=58558&from=article.pc_detail&x-expires=1662370106&x-signature=5DEX9XZBAgrtCtOsie8hpyhtS0s%3D'
---

<div>   
<div class="content">
                                                                                            <div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/c9e19036df6b4a4e92267306ce10f54a~noop.image?_iz=58558&from=article.pc_detail&x-expires=1662370106&x-signature=5DEX9XZBAgrtCtOsie8hpyhtS0s%3D" referrerpolicy="no-referrer"> 
 <p style="margin-left:0px; margin-right:0px">2022年8月29日，MeterSphere一站式开源持续测试平台正式发布v2.1.0版本。</p> 
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">在这一版本中，MeterSphere的<strong><span style="color:#783887">UI测试</span></strong>模块对鼠标指令进一步扩展，实现了绘图核心场景的覆盖；在<strong><span style="color:#783887">测试跟踪</span></strong>模块中，对功能用例模板进行了优化，同时支持自定义字段的导入、导出，缺陷模板支持跨项目复制，以满足多租户管理模式下需要频繁设置模板的需求；在<strong><span style="color:#783887">项目设置</span></strong>模块中，对文件管理功能进行重构，与网盘功效一样不限制上传的文件类型，在接口测试或性能测试过程中，需要用到文件的地方支持一键关联文件。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:justify">新增功能</h2> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#783887">■ UI测试覆盖绘图核心场景（X-Pack增强包内）</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">MeterSphere v2.1.0版本中，UI测试模块针对Selenium原生指令进行了进一步的扩展。如鼠标拖拽指定，原生指令只支持从一个指定元素拖拽到目标元素。扩展后的拖拽指令支持从一个坐标位置到目标坐标位置，添加多个坐标位置可以覆盖绘图场景。除此之外，MeterSphere v2.1.0版本还扩展了鼠标的左击、右击、键盘功能键等操作。</p> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/6662a8b8be0c4d55b09c74ef574885ca~noop.image?_iz=58558&from=article.pc_detail&x-expires=1662370106&x-signature=SFVQ2uWeFx6I0HDAwmeKWyAH2a8%3D" referrerpolicy="no-referrer"> 
 <p style="margin-left:0px; margin-right:0px">通过鼠标拖拽指定坐标位置，实现绘图场景的示例：</p> 
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/cad88bac1ca441b0bc1ff23a8a5ee0af~noop.image?_iz=58558&from=article.pc_detail&x-expires=1662370106&x-signature=cwYYhs1NOsqvaR96g%2Fpl%2Fbm4GH4%3D" referrerpolicy="no-referrer"> 
 <p style="margin-left:0px; margin-right:0px"><strong><span style="color:#783887">■ 功能用例支持自定义字段导入、导出</span></strong></p> 
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">MeterSphere的功能用例模板支持自定义字段。在MeterSphere v2.1.0版本中，用例的导入、导出支持自定义导出字段，方便用户在Excel中维护用例。</p> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/a8983a3326314f88926fd3dd7e895336~noop.image?_iz=58558&from=article.pc_detail&x-expires=1662370106&x-signature=e8WBg5%2BYQGeAp19fDWQRWmU%2FaHM%3D" referrerpolicy="no-referrer"> 
 <p style="margin-left:0px; margin-right:0px"><strong><span style="color:#783887">■ 文件管理重构</span></strong></p> 
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">MeterSphere v2.1.0版本对项目设置下的文件管理功能进行了重构。整合系统中的全部文件进行集中管理，不限制上传文件的类型，让文件管理功能像网盘一样简单好用。其中，文件支持列表与缩略图模式展示，浏览文件支持图片预览。对Jar包类型的文件，MeterSphere支持动态加载，无需重启服务。</p> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/ef474fefa3604760a2c3c9fd519ef5a8~noop.image?_iz=58558&from=article.pc_detail&x-expires=1662370106&x-signature=K9gF2xrvHq5fdpwtLPbgIKZ751A%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/14ec88144cf6452985855e60645346b0~noop.image?_iz=58558&from=article.pc_detail&x-expires=1662370106&x-signature=1seEMoncvKhX2N9Uz8W227DC3lo%3D" referrerpolicy="no-referrer"> 
 <p style="margin-left:0px; margin-right:0px">同时，MeterSphere v2.1.0版本将其他模块与文件管理功能进行了打通。在此之前，文件类型的接口测试或者基于CSV数据驱动的接口自动化功能中，只能通过本地上传的方式来上传指定文件。现在，除了本地上传的方式，MeterSphere还提供了关联文件功能，直接关联文件管理列表中的任意文件，且支持文件多选。针对本地上传的文件，也支持一键转存至文件管理列表中进行集中维护。</p> 
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/c099599753b24214a632608a9e66d1f0~noop.image?_iz=58558&from=article.pc_detail&x-expires=1662370106&x-signature=lBc%2Ba5gIyPQ88l%2By%2B6QM0tyjOuI%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/4cc70feeba0344769706a0b85b503580~noop.image?_iz=58558&from=article.pc_detail&x-expires=1662370106&x-signature=VUCpinmOE6XiNq9ZYv5E2d%2BM%2B6Y%3D" referrerpolicy="no-referrer"> 
 <h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#783887">■</span><span> </span>测试跟踪：功能测试用例模板导入优化；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#783887">■</span><span> </span>接口测试：接口导入更新增加消息通知；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#783887">■</span><span> </span>接口测试：API文档展示优化，支持展示高级设置；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#783887">■</span><span> </span>接口测试：场景变量支持查询以及导入、导出；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#783887">■</span><span> </span>UI测试（X-Pack）：支持任意位置添加截图步骤；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#783887">■<span> </span></span>UI测试（X-Pack）：输入步骤支持键盘功能键；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#783887">■<span> </span></span>项目设置：支持二级菜单权限管控；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#783887">■</span><span> </span>项目设置：环境配置中全局变量支持查询以及导入、导出；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#783887">■</span><span> </span>系统设置：OIDC和CAS认证支持配置Callback URL。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:justify">Bug修复</h2> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#783887">■<span> </span></span>fix（测试跟踪）：修复表格用例导入更新，提示更新成功，但是内容没有更新的问题（GitHub #17077）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#783887">■<span> </span></span>fix（测试跟踪）：修复缺陷管理的高级搜索中创建人无法列出所有项目成员的问题（GitHub #16974）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#783887">■<span> </span></span>fix（接口测试）：修复代码片段中导入Python SSL模块在升级到v2.0.1后执行出错的问题（GitHub #16945）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#783887">■<span> </span></span>fix（UI测试）：修复UI自动化点击后端调试与生成报告执行结果不一致的问题（GitHub #16523）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#783887">■</span><span> </span>fix（UI测试）：修复UI自动化场景新复制的场景无创建人信息的问题（GitHub #16732）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#783887">■</span><span> </span>fix（项目设置）：修复消息设置新建缺陷的接收人是处理人，但在消息通知时没有@处理人的问题（GitHub #16751）。</p> 
<p style="color:#222222; margin-left:0px; margin-right:0px; text-align:justify">除了上述提到的新增功能和优化外，MeterSphere v2.1.0版本还包含很多其他功能的更新和优化，欢迎进入MeterSphere项目的官方文档及GitHub仓库的Release页面，查看更加详细的更新日志。</p>
                                        </div>
                                      
</div>
            