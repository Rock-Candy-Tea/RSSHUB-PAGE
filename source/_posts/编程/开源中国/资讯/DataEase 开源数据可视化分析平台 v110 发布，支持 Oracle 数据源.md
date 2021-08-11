
---
title: 'DataEase 开源数据可视化分析平台 v1.1.0 发布，支持 Oracle 数据源'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-81b69a4946957f625d729c2ade219cc3850.png'
author: 开源中国
comments: false
date: Wed, 11 Aug 2021 09:54:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-81b69a4946957f625d729c2ade219cc3850.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <div> 
   <div>
    <img alt height="293" src="https://oscimg.oschina.net/oscnet/up-81b69a4946957f625d729c2ade219cc3850.png" width="561" referrerpolicy="no-referrer">
   </div> 
  </div> 
 </div> 
</div> 
<div> 
 <div> 
  <div> 
   <div style="text-align:left"> 
    <p style="text-align:left">8月9日，DataEase开源数据可视化分析平台正式发布v1.1.0版本。在该版本中，新增了对Oracle数据源的支持，同时还新增两大功能：即消息中心和定时任务中心。在消息中心内，用户可以获取到系统发给自己的系统事件通知。在定时任务中心内，用户可对数据集的定时同步任务做统一的全生命周期管理。此外，我们还对数据集、视图、仪表板等常用的功能也进行了大量的优化和修复。</p> 
    <h2 style="text-align:left">新增功能</h2> 
    <p style="text-align:left"><strong><span style="color:#0a7be0">■ Oracle数据源支持</span></strong></p> 
    <p style="text-align:left">作为市面上主流的关系型数据库，用户对Oracle数据源的要求非常迫切。在DataEase v1.1.0版本中，我们增加了对Oracle数据源的支持。目前已在Oracle 11和Oracle 12两个版本上完成了验证。</p> 
    <p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-69fd75139a9d6b16c56e1d94208ddbbac4d.png" referrerpolicy="no-referrer"></p> 
    <p style="text-align:left"><strong><span style="color:#0a7be0">■ 消息中心</span></strong></p> 
    <p style="text-align:left">在DataEase v1.1.0版本中，新增了对消息中心的支持。用户可以在第一时间接收到异步任务的完成消息，以及其他用户对自己的授权通知。点击系统界面右上角的消息通知按钮，即可快速进入到消息中心。目前，消息中心支持的事件有仪表板分享、数据集同步，后续会逐步添加其他系统事件的支持。消息中心默认为每个用户开启了“仪表板分享”和“数据集同步失败”消息的订阅。如不需要相关通知，可以在“接收管理”菜单中选择关闭即可。</p> 
    <p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-3fb8a8f488b60ff95b3793abcc752064081.png" referrerpolicy="no-referrer"></p> 
    <p style="text-align:left"><strong><span style="color:#0a7be0">■ 定时任务中心</span></strong></p> 
    <p style="text-align:left">在DataEase v1.1.0版本中，新增了对定时任务中心的支持。在此之前的版本中，用户需要单独在每个数据集中去设置定时任务。定时任务多起来之后，管理起来会非常不方便。在新增的定时任务中心内，用户可以集中查看系统中所添加的所有任务的情况，包括当前执行状况、下次执行计划、任务执行历史记录等，还可以对指定任务进行启动、停止、删除等操作，极大地提升了用户的使用体验。</p> 
    <p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-3c0a1418783c4f8af84989d0cadf8f82a48.png" referrerpolicy="no-referrer"></p> 
    <p style="text-align:left"><strong><span style="color:#0a7be0">■ 同数据源直连数据集之间支持数据关联</span></strong></p> 
    <p style="text-align:left">在此前的版本中，DataEase支持设置数据关联关系的数据集仅包含定时同步类型的数据集和Excel数据集。在DataEase v1.1.0版本中，对于相同数据源的直连模式数据集，我们也可以设置数据集之间的关联关系，从而创建衍生的自定义数据集。</p> 
    <p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-07ce3e5bb41440a185b79a620d2cd558a71.png" referrerpolicy="no-referrer"></p> 
    <p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-111f9a0592adc02f4b8ec609ab5ec51d96e.png" referrerpolicy="no-referrer"></p> 
    <p style="text-align:left"><strong><span style="color:#0a7be0">■ 视图支持更换数据集</span></strong></p> 
    <p style="text-align:left">在DataEase v1.1.0版本中新增了视图更换数据集的支持。在以往的版本中，用户创建了视图之后，如果数据集有变动或失效，就需要重新制作视图。如果该视图已经用在了多个仪表板中，则还需要去修改相关的仪表板。在DataEase v1.1.0版本中，用户可以直接编辑视图，更换相关数据集，重新制作的视图会自动更新到所有相关的仪表板中。</p> 
    <p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-82661947c6ae7da48eb69d01cee33a2ccb3.png" referrerpolicy="no-referrer"></p> 
    <p style="text-align:left"><strong><span style="color:#0a7be0">■ 仪表板编辑增加新建视图功能，可直接在仪表板新建视图</span></strong></p> 
    <p style="text-align:left">DataEase v1.1.0版本支持在编辑仪表板的同时新建视图的功能。用户可以更加快速方便地在仪表板中加入所需展示的视图，而无需经历进行退出仪表板→进入视图→新建视图→进入仪表板→编辑仪表板等一系列繁杂的操作，进一步提升了仪表板的开发效率。</p> 
    <p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-d92ec66c3c6d79ec43065a8ef2d2ab6a677.png" referrerpolicy="no-referrer"></p> 
    <p style="text-align:left">除了上述提到的新增功能外，DataEase v1.1.0版本还包含了很多其他的功能更新和优化，欢迎进入我们的官方文档及GitHub仓库的Release页面查看更加详细的更新日志。</p> 
    <h2 style="text-align:left">功能优化</h2> 
    <p style="text-align:left"><span style="color:#0a7be0">■  </span>refactor（数据集）：数据关联选择数据集Tree优化；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> refactor（数据集）：数据集视图底层SQL拼接使用STG重构（MySQL部分）；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> feat（数据集）：同步数据集预览数据从Doris中提取；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> feat（数据集）：添加非直连数据集时，默认全量同步一次；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> feat（数据集）：根据预览的前100行推断Excel类型；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> feat（数据集）：数据关联改为左连接等方式；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> refactor（视图）：视图缓存增加互斥锁，避免出现缓存击穿现象；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> refactor（视图）：视图UI布局调整；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> refactor（视图）：过滤组件条件调整；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> refactor（视图）：视图分组Tree优化；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> refactor（仪表板）：矩阵设计模式下点击一次组件也无需保存镜像；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> refactor（仪表板）：创建分组或者仪表板时，点击“取消”按钮，不发出目录树的请求；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> refactor（仪表板）：仪表板编辑不再使用右键操作，统一在组件的右上角添加设置入口；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> refactor（仪表板）：查看分享链接使用独立拦截器；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> refactor：优化任务日志查询；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■ </span>refactor：可配置Kettle相关的文件是否保留。</p> 
    <h2 style="text-align:left">Bug 修复</h2> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> 修复内网环境请求远程axios.js报错的问题；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> 修复部分开发环境仪表板编辑无法拖拽的问题；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> 修复文本悬浮样式组件样式穿透未生效的问题；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> 修复组件查询条件无效的问题；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> 修复矩形组件和文本组件在非自适应画布区域模式下对应悬浮组件定位的问题；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> 处理kettle tinyint识别错误的问题；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> 修复仪表板图表明细数据下载数值为0不显示的问题；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> 修复中文输入法回车键直接保存的问题；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> 修复仪表板保存直接退出的问题；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> 修复数据集字段浮点转整型的问题；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> 修复Tree搜索后无法折叠的问题；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> 修复单指标图表可能下标越界的问题；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> 修复同一张图片无法连续两次被导入到仪表板的问题；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> 修复在编辑仪表板时，复制堆叠柱状图时出错的问题；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> 修复预览模式下部分尺寸的显示屏仪表板抖动的问题；</p> 
    <p style="text-align:left"><span style="color:#0a7be0">■</span> 修复Excel替换/追加的问题。</p> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            