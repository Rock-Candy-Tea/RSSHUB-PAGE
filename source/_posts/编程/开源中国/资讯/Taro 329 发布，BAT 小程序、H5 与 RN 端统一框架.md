
---
title: 'Taro 3.2.9 发布，BAT 小程序、H5 与 RN 端统一框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4981'
author: 开源中国
comments: false
date: Sat, 22 May 2021 09:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4981'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Taro 3.2.9 发布了。Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发微信/京东/百度/支付宝/字节跳动/ QQ 小程序/H5 等应用。此版本更新内容包括：</p> 
<h2>特性</h2> 
<h3>编译</h3> 
<ul> 
 <li>体积优化，添加小程序提取公共模块插件，自动分析抽离分包时子包的公共依赖并打包到子包中，by <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhuangcj99" target="_blank">@huangcj99</a></li> 
</ul> 
<h3>RN</h3> 
<ul> 
 <li>添加 navigationRef 导出到 Current</li> 
</ul> 
<h2>修复</h2> 
<h3>编译</h3> 
<ul> 
 <li>移除 fiber 依赖，兼容新版本 node</li> 
</ul> 
<h3>小程序</h3> 
<ul> 
 <li>区分冒泡事件，对于非冒泡事件不需要在祖先节点批量触发，by <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fivan-94" target="_blank">@ivan-94</a></li> 
</ul> 
<h3>H5</h3> 
<ul> 
 <li>修复 H5 createCanvasContext 相关问题，by <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fivan-94" target="_blank">@ivan-94</a></li> 
</ul> 
<h3>RN</h3> 
<ul> 
 <li>支持 onBuildFinish 编译 Hook</li> 
 <li>增加 CustomWrapper 组件支持</li> 
 <li>修复 @types/node 新版本与 RN 不兼容问题</li> 
 <li>修复 getCurrentPages 页面实例错误 bug</li> 
 <li>增加 native 传递的 props</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Freleases%2Ftag%2Fv3.2.9" target="_blank">https://github.com/NervJS/taro/releases/tag/v3.2.9</a></p>
                                        </div>
                                      
</div>
            