
---
title: '全面支持 JS_eTS 应用开发，DevEco Studio 3.0 Beta4 新版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-37f636b345ac73d0c6fc1d76f1ef6f749f4.png'
author: 开源中国
comments: false
date: Fri, 08 Jul 2022 09:11:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-37f636b345ac73d0c6fc1d76f1ef6f749f4.png'
---

<div>   
<div class="content">
                                                                                            <p><span>HUAWEI DevEco Studio（后文简称DevEco Studio）作为HarmonyOS应用及服务开发的IDE，最近升级了新版本——DevEco Studio 3.0 Beta 4。本次新版本主要支持在HarmonyOS 3.0 Beta版上开发JS/eTS应用及服务，同时还增强了低代码开发、预览器和编辑器的能力，优化了信息中心体验。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><strong><span>升级方式：</span></strong></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#7f7f7f"><strong><span>建议您从官网下载安装包进行全量升级：</span></strong></span><span style="color:#7f7f7f">https://developer.harmonyos.com/cn/develop/deveco-studio</span></p> 
<p> </p> 
<p style="margin-left:0; margin-right:0"><strong><span><span>一、支持JS/eTS应用及服务开发</span></span></strong></p> 
<p><span>基于HarmonyOS 3.0 Beta版开发JS/eTS应用和服务时，需要同时下载OpenHarmony SDK（API Version 8）以及HarmonyOS SDK下的Previewer和Toolchains（API Version 8）。</span></p> 
<p> </p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:center"><span style="color:#7f7f7f"><img alt height="705" src="https://oscimg.oschina.net/oscnet/up-37f636b345ac73d0c6fc1d76f1ef6f749f4.png" width="906" referrerpolicy="no-referrer"></span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:center"><span style="color:#7f7f7f">图1 OpenHarmony SDK下载</span></p> 
<p><img alt height="709" src="https://oscimg.oschina.net/oscnet/up-e47ffdd787b337d9d07ff4384c1da9274f4.png" width="981" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:center"><span style="color:#7f7f7f">图2 HarmonyOS SDK下载</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span>完成以上操作，就可以开始你的HarmonyOS 3.0 Beta版的JS/eTS应用开发之旅了。</span></p> 
<p> </p> 
<p style="margin-left:0; margin-right:0"><strong><span><span>二、支持低代码开发</span></span></strong></p> 
<p><span style="color:#333333">低代码开发功能，是DevEco Studio为开发者提供的可视化界面开发方式，具有丰富的UI界面编辑功能。</span><span style="color:#333333">开发者可自由拖拽组件，快速预览界面效果，所见即所得，有效降低时间成本，提升UI界面的<span style="background-color:#ffffff; color:#333333">构建</span>效率。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span>此次新版本新增eTS低代码开发功能，支持组件自由拖拽排版以及数据绑定。创建工程时选择开启Super Visual，打开使用低代码开发功能。在工程目录结构下打开“.visual”文件，即可进行UI界面的可视化布局设计与开发。</span></p> 
<p><img alt height="679" src="https://oscimg.oschina.net/oscnet/up-713a52cbec48ee7e43423ab497ac1b79759.gif" width="1079" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:center"><span style="color:#7f7f7f">图3 eTS低代码开发</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span>此外，服务卡片与低代码开发的功能特性非常契合，通过使用低代码开发完全可以做到服务卡片零码化开发。将所需资源放到对应的文件夹后，在index.visual界面通过拖拽组件排版以及属性设置编辑界面框架，在json面板中定义变量，然后在属性样式栏进行数据绑定，就可完成服务卡片开发。</span></p> 
<p><img alt height="653" src="https://oscimg.oschina.net/oscnet/up-258047c65088eb7f20f1a7a99575806c061.gif" width="1079" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:center"><span style="color:#7f7f7f">图4 低代码开发服务卡片</span></p> 
<p> </p> 
<p style="margin-left:0; margin-right:0"><strong><span><span>三、支持ArkUI声明式范式组件的极速预览</span></span></strong></p> 
<p><span style="color:#333333">DevEco Studio现已提供多种预览功能，包括多端设备预览、双向预览、实时预览、动态预览等，让开发者可以在UI界面开发时快速查看UI代码运行的效果。</span><span style="color:#333333">此次新版本的实时预览功能新增支持ArkUI声明式范式组件的极速预览。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><span>我们之前提供的实时预览功能，需要在添加或删除UI组件后使用快捷键Ctrl+S进行保存，预览器才会刷新预览结果。此次新版本中，如果修改了ArkUI声明式范式组件的属性和属性值，在该组件没有绑定变量的情况下，无需操作保存，预览器就会亚秒级同步刷新预览结果，让开发者更加快速地看到预览界面的变化效果。</span></p> 
<p><img alt height="511" src="https://oscimg.oschina.net/oscnet/up-8c770d6b5496905bcfc860a100f9a760bd1.gif" width="1078" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:center"><span style="color:#7f7f7f">图5 ArkUI声明式范式组件的极速预览</span></p> 
<p> </p> 
<p style="margin-left:0; margin-right:0"><strong><span><span>四、编辑器能力增强</span></span></strong></p> 
<p><span style="color:#333333">此</span><span style="color:#333333">次DevEco Studio新版本新增了以下三项编辑器能力，让应用开发更加简单高效！</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><strong><span>1. ArkUI代码格式化</span></strong></p> 
<p><span>实际应用开发中，为了精准地表达业务逻辑，提高代码可读性，往往会对代码的格式有要求。为解决你在编辑代码时的格式问题，DevEco Studio提供了ArkUI代码格式化功能。 </span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span>在“Setting > Editor > Code Style”下选择对应的语言，且开启代码格式化功能后，即可进行缩进（Tabs and Indents）、空格（Spaces）、换行（Wrapping and Braces）、空行（Blank Lines）和代码排序（Arrangement）的格式化操作。本次新增eTS、JavaScript和TypeScript三种语言的Arrangement功能，支持相应语言的代码排序排列功能的设置，更便于你编辑代码。</span></p> 
<p><img alt height="714" src="https://oscimg.oschina.net/oscnet/up-fc8b0288d83e65465dc66dac009713c935a.png" width="982" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:center"><span style="color:#7f7f7f">图6 ArkUI代码格式化</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><strong><span>2. ArkUI自定义代码折叠</span></strong></p> 
<p><span>实际应用开发中，如果要实现复杂的功能，代码也会比较复杂。为解决代码太长不便于查看代码逻辑的问题，DevEco Studio提供ArkUI自定义代码折叠功能。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span>当你选中想要折叠的代码后，选择菜单栏的Code，打开surround with或者使用快捷键Ctrl+Alt+T来进行代码的自定义折叠设置。通过自定义折叠设置可自动生成具有环绕性质的代码，如if..else、try..catch、for、synchronized等，还包括2种不同风格的自定义折叠样式选项，包括<editor-fold...>Comments和region...endregion Comments。 </span></p> 
<p><img alt height="583" src="https://oscimg.oschina.net/oscnet/up-05adef5ff5532a54080ec747dd2f389744f.gif" width="1079" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:center"><span style="color:#7f7f7f">图7 ArkUI自定义代码折叠</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><strong><span>3. 字符串可视化编辑</span></strong></p> 
<p><span>有的APP需要面对多个国家的受众，因此开发时需要将字符串资源翻译成多种语言。在进行多种语言翻译时，就可以用到DevEco Studio提供的字符串可视化编辑功能。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span>如图8所示，在编辑字符串资源文件string.json时，你可以打开字符串资源编辑器，采用表格可视化的方式来编辑。在字符串资源编辑器中可以展示所有string.json文件中设置的字符串，并且支持添加、修改、删除字符串，且支持直接同步到原string.json文件中。</span></p> 
<p><img alt height="583" src="https://oscimg.oschina.net/oscnet/up-72b58b8d5a0a6846654af6b855bcac29ecb.gif" width="1079" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:center"><span style="color:#7f7f7f">图8 字符串可视化编辑</span></p> 
<p> </p> 
<p style="margin-left:0; margin-right:0"><strong><span><span>五、信息中心体验优化</span></span></strong></p> 
<p><span style="color:#333333">在开发过程中可能会遇到问题，需要查阅文档或者资料，为此DevEco Studio基于开发旅程提供了一站式信息获取平台——信息中心（InfoCenter），遇到问题时可以直接在信息中心查阅文档、资料。</span></p> 
<p style="margin-left:0; margin-right:0"><span><strong><span><span>● </span>1. 资源快捷入口</span></strong></span></p> 
<p style="margin-left:0; margin-right:0"><span>信息中心提供了HarmonyOS和OpenHarmony的快速入门、示例教程、开发指南、API参考、版本变更、常见问题等内容，且与DevEco Studio的功能深度融合，在信息阅读过程中可一键直达相应功能，实现信息阅读与操作的快速切换。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><img alt height="768" src="https://oscimg.oschina.net/oscnet/up-3f3031c4efd4354ca80af37388c0ffc66dd.png" width="745" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:center"> </p> 
<p><span style="color:#7f7f7f">图9 信息中心（InfoCenter）</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span>● 2. 资源实时更新</span></strong></p> 
<p style="margin-left:0; margin-right:0"><span>新版本的信息中心，支持根据开发的应用/服务类型进行手动自助切换资源类型，还集成了更多的开发资源，如开发指南、API参考这些常用文档资源。当资源内容动态更新后，底部栏会有提示告知，第一时间通知您。本次升级，信息中心支持Banner页资源推荐，整合开发者重点关注的资源（如文档上新、重点手册优化、意见答复等），方便您在DevEco Studio中体验沉浸式资源阅读，更快速找到想要查阅的资源。</span></p> 
<p style="margin-left:0; margin-right:0"><span><strong><span>● 3. 问题求助及意见反馈</span></strong></span></p> 
<p style="margin-left:0; margin-right:0">与此同时，信息中心也提供了问题求助入口，您可以查阅常见问题，也支持在线提单或通过快捷入口前往开发者论坛发帖求助。欢迎您通过意见反馈界面，反馈DevEco Studio工具/开发者文档的错误、Bug、改进意见等，您的宝贵意见是我们改进的重要参考。</p> 
<p style="margin-left:0; margin-right:0; text-align:center"><img alt height="842" src="https://oscimg.oschina.net/oscnet/up-f5ed1d1a68855b66645f3c71aecde1c644b.png" width="801" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span style="color:#7f7f7f">图10 问题和意见反馈</span></p> 
<p><span style="color:#333333">启动DevEco Studio后，在菜单栏选择“Help > InfoCenter”，即可打开信息中心，快来体验吧！</span></p> 
<p><span style="color:#333333">工欲善其事，必先利其器，赶快点击“阅读原文”下载DevEco Studio 3.0 Beta4来开发JS/eTS</span><span style="color:#333333">的应用或者服务吧！</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><span>最后，也欢迎你提出好的建议或者意见，帮助DevEco Studio往更好的方向前进发展，为HarmonyOS应用打造更强大的开发工具。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#7f7f7f"><strong><span style="color:#7f7f7f">反馈渠道：</span></strong></span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#7f7f7f">https://developer.huawei.com/consumer/cn/forum/block/deveco-studio</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            