
---
title: 'DevEco Studio 2.1 Beta4 发布，HarmonyOS 的配套 IDE'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4b9fd18ab4aa13402f5054bbf722dd16c97.png'
author: 开源中国
comments: false
date: Sat, 01 May 2021 07:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4b9fd18ab4aa13402f5054bbf722dd16c97.png'
---

<div>   
<div class="content">
                                                                                            <p>HUAWEI DevEco Studio 2.1 Beta4版本来啦！相比2.1 Beta3版本，新版本增加服务卡片开发、提供代码混淆功能，并更新HarmonyOS SDK至2.1.1.20版本，Stage为Release，支持应用上架。同时修复低概率联想失败、性能卡顿等遗留缺陷。</p> 
<p>具体信息如何，一起看看吧！</p> 
<p><strong>新增特性：</strong></p> 
<h1>01 新增服务卡片开发</h1> 
<p>服务卡片是<strong>FA的一种主要信息呈现形式</strong>，开发者可以在卡片中展示用户最关心的FA数据，并可以通过点击卡片内容直接打开FA。</p> 
<p>DevEco Studio 2.1 Beta4服务卡片提供了多种类型的模板，开发者可根据需要展示的信息类型<strong>灵活选择模板</strong>，快速构建服务卡片。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-4b9fd18ab4aa13402f5054bbf722dd16c97.png" referrerpolicy="no-referrer"></p> 
<h1>02 提供代码混淆功能</h1> 
<p>使用ProGuard工具（ProGuard是一个开源的Java代码混淆器）<strong>将工程中的Java文件源代码进行混淆</strong>，以简短无意义的名称（例如a、b、c等），对类、字段和方法等进行重命名。<strong>在有效减少应用大小的同时，提升反编译的难度，起到保护源代码的目的。</strong></p> 
<p>在DevEco Studio中，混淆功能默认是关闭的。如果需要开启混淆功能，在模块的build.gradle文件中配置proguardEnabled为true即可。</p> 
<p>此外，DevEco Studio 2.1 Beta4还更新HarmonyOS SDK至2.1.1.20版本，Stage为Release，支持应用上架。</p> 
<p>同时，DevEco Studio 2.1 Beta4修复一系列问题，体验更佳：</p> 
<h1>解决如下问题：</h1> 
<ol> 
 <li>解决通过公共变量的方式配置build.gradle脚本中的compileSdkVersion时，可能会导致的layout下xml文件报红问题</li> 
 <li>解决config.json可视化配置界面中，输入package的值不自动联想的问题</li> 
 <li>解决config.json可视化配置界面中，当表格存在必填字段的标签时，不进行输入校验的问题</li> 
 <li>解决打开HVD Mananger进行登录授权时，若登录后在未授权的情况下关闭HVD Manager，出现DevEco Studio卡死的问题</li> 
 <li>解决使用Phone和Tablet模拟器进行Java调试时，无法进入断点的问题</li> 
 <li>解决css文件在代码量大（例如2000行）时，可能出现自动联想及跳转失效的问题</li> 
 <li>解决批量拷贝js page到当前工程后，编辑器可能出现自动联想补齐失效的问题</li> 
</ol> 
<p><strong>DevEco Studio 2.1 Beta4 下载链接：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.harmonyos.com%2Fcn%2Fdevelop%2Fdeveco-studio" target="_blank">https://developer.harmonyos.com/cn/develop/deveco-studio</a><br> <strong>反馈连接：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.huawei.com%2Fconsumer%2Fcn%2Fforum" target="_blank">https://developer.huawei.com/consumer/cn/forum</a></p>
                                        </div>
                                      
</div>
            