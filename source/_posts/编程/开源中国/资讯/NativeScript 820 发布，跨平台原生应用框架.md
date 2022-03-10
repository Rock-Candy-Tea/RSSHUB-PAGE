
---
title: 'NativeScript 8.2.0 发布，跨平台原生应用框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1891'
author: 开源中国
comments: false
date: Thu, 10 Mar 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1891'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0">NativeScript 8.2.0 现已发布。NativeScript 使用户能够直接从 JavaScript 访问 native API。目前，该框架为丰富的移动开发提供了 iOS 和 Android 运行时，并可用于多种不同的用例。</p> 
<p style="margin-left:0">主要更新内容如下：</p> 
<h4><strong>Bug Fixes</strong></h4> 
<ul> 
 <li><strong>android：</strong>api17 在 a11y 服务上崩溃 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9792" target="_blank">#9792</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F2efcdf57871cc7a8def6a83995cf6f0d7f66f925" target="_blank">2efcdf5</a> )</li> 
 <li><strong>android：</strong>boolean keyboardType 不应该设置 inputType ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9795" target="_blank">#9795</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F9e6371fdaf4a2ba62da9920d9011045a267f4e53" target="_blank">9e6371f</a> )</li> 
 <li>应用程序实例创建仅发生在 Application.run 中 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2Fa518249958df933ca82f2f82f5efe023fa7ae695" target="_blank">a518249</a> )</li> 
 <li><strong>core：</strong>适用于 android css 动画和 iOS 旋转的动画迭代 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9628" target="_blank">#9628</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F608bb1ed24fd32ac6199e632d739e7a66a0da1c8" target="_blank">608bb1e</a> )</li> 
 <li><strong>core：</strong> nativeApp 实例的应用处理（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F6c06c77618c92590d5aa441eac838c4330732753" target="_blank">6c06c77</a>）</li> 
 <li>确保 android 可以在启动前访问本地应用实例 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2Ff10cffcb02a1ae37b436ea22eaf1cf67804927fe" target="_blank">f10cffc</a> )</li> 
 <li><strong>fs：</strong>错误的公共路径（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F51b92f355799409aba82eca4c951b394c4ef894c" target="_blank">51b92f3</a>）</li> 
 <li><strong>ios：</strong>如果背景图像为“none”，则不重绘（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9800" target="_blank">#9800</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F402a7bba2ee9435134d6697dbe5639bd096597f6" target="_blank">402a7bb</a>）</li> 
 <li><strong>ios：</strong>正确的 UITabBarAppearance 处理（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F6c71ce21a20adba7ea350176fc5a81da646f594f" target="_blank">6c71ce2</a>）</li> 
 <li><strong>ios：</strong>Image 处理后 UIImage 内存泄漏 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9777" target="_blank">#9777</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F19d8869f1dc64d64a8b295985514716be5012a2c" target="_blank">19d8869</a> )</li> 
 <li>围绕图像拾取/保存到设备的内存泄漏 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F7dcfecffab10c3b253975a84f711b46111070bf4" target="_blank">7dcfecf</a> )</li> 
 <li>qualifier matcher 不支持单个文件的多个限定词。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9720" target="_blank">#9720</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F3d03f8f06aa36852cbce82a319dcf9de79c929ac" target="_blank">3d03f8f</a> )</li> 
 <li>设置脚本以仅构建必要的 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2Fb05650c4166f5ce04cb761e4f3730cf2656c8192" target="_blank">b05650c</a> )</li> 
 <li>关闭 modal 后拆解视图 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9801" target="_blank">#9801</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2Fb38337e597a8288f6ab0c5058fa9addd622146be" target="_blank">b38337e</a> )</li> 
 <li><strong>Time-picker：</strong>修正 super.disposeNativeView ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2Fc41e7027e45778c9c27fcbc701f56edebd57e33b" target="_blank">c41e702</a> )</li> 
</ul> 
<h4><strong>Features </strong></h4> 
<ul> 
 <li><strong>android：</strong>tab view 的图标渲染模式 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9605" target="_blank">#9605</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F66d8afffc1a987b36605c7206b057268a38ecb06" target="_blank">66d8aff</a> )</li> 
 <li><strong>android：</strong>将 ui-mobile-base 更新为 gradle7 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9778" target="_blank">#9778</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2Fc7df2d0d6f0539ba0db2eda9a5b2ce91a7d59f30" target="_blank">c7df2d0</a> )</li> 
 <li>background/foreground events ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9763" target="_blank">#9763</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2Fb553a900d76893d1f49ea4a20fa361147585a451" target="_blank">b553a90</a> )</li> 
 <li><strong>bindable：</strong>允许绑定内的表达式使用“global”context ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9734" target="_blank">#9734</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F2cbb135250252844ce8c7affabaf3140643ce7b4" target="_blank">2cbb135</a> )</li> 
 <li>绑定表达式解析器的添加和改进 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9791" target="_blank">#9791</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F716b831523829dfa508d32efe0067060109ca574" target="_blank">716b831</a> )</li> 
 <li><strong>config：</strong>为 pathsToClean 添加新选项 (<strong> </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F08d56568998dae416205fe7b0ada8334ebabb2e0" target="_blank">08d5656</a> )</li> 
 <li><strong>config：</strong>cli.additionalPathsToClean 使用 'ns clean' 清理其他路径 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9808" target="_blank">#9808</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F3ec8c429719a9a32238801ba3dd7c17c0b50ec72" target="_blank">3ec8c42</a> )</li> 
 <li><strong>core：</strong>调用 disposeNativeView 时添加事件（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2Ff038e6ba66c319465bde251d1e540d4ee5981373" target="_blank">f038e6b</a>）</li> 
 <li><strong>core：</strong>支持 RGB alpha 符号 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9699" target="_blank">#9699</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F388d7eaa7d956e7785ad26399c14b925664f6a52" target="_blank">388d7ea</a> )</li> 
 <li><strong>datepicker：</strong>通过 showTime 属性显示时间的能力 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9570" target="_blank">#9570</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2Fab4e47a1c1132f73648d76fa332c5633028182f7" target="_blank">ab4e47a</a> )</li> 
 <li><strong>gestures：</strong>添加 GestureEvents.gestureAttached 以在需要时修改 native recognizers ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F168a16972623109afadedabd32ff22d70555026b" target="_blank">168a169</a> )</li> 
 <li>改进了 XML 表达式的转换器和函数调用解析机制 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9805" target="_blank">#9805</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2Fc5856c6daee6901356a55868629484171e64daee" target="_blank">c5856c6</a> )</li> 
 <li><strong>ios：</strong>允许动态 ProMotion 帧刷新率更改 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9775" target="_blank">#9775</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2Fb2924955067c992caea5b14e37d705cea203a509" target="_blank">b292495</a> )</li> 
 <li>用于 xml 绑定的新表达式解析器 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9729" target="_blank">#9729</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F90ceed15d3b4f89f06b0a1f7f78724a37c9985e6" target="_blank">90ceed1</a> )</li> 
 <li>正确处理与未定义的转换器的绑定 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9813" target="_blank">#9813</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2Fa1772c00058d03ee1e4a6e3ba8f96ba2197e3f2b" target="_blank">a1772c0</a> )</li> 
 <li>用于 e2e 测试而不干扰 a11y 的 testID 属性， ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9793" target="_blank">#9793</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F8be543bcc7da2634f9c627ea15b06e6dfef78b93" target="_blank">8be543b</a> ) ，<span style="color:#24292f">closes </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9748" target="_blank">#9748</a></li> 
 <li>......</li> 
</ul> 
<h4><span style="color:#24292f">Performance Improvements</span></h4> 
<ul> 
 <li><strong>ios：</strong>图像扩展的自动释放池（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2Ffbefea4dbad59e9b31ecd9311b1a16f40d041c9d" target="_blank">fbefea4</a>）</li> 
 <li><strong>ios：</strong>防止图像发布崩溃（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F1fb687df550e1c01c5901920e79487d220e834c4" target="_blank">1fb687d</a>）</li> 
 <li><strong>ios：</strong>uifont 和格式化字符串优化以及 uiimage 缩放 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9761" target="_blank">#9761</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F9d3977ea4fd6d6aedeab55e0472999c05ed5a7bd" target="_blank">9d3977e</a> )</li> 
 <li><strong>ios：</strong>UIImage 内存泄漏 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fissues%2F9783" target="_blank">#9783</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Fcommit%2F988f3727883bddd27dd6397d7dfeebeb9b20c559" target="_blank">988f372</a> )</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNativeScript%2FNativeScript%2Freleases%2Ftag%2F8.2.0-core" target="_blank">https://github.com/NativeScript/NativeScript/releases/tag/8.2.0-core</a></p>
                                        </div>
                                      
</div>
            