
---
title: 'jQuery UI 1.13.0 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2232'
author: 开源中国
comments: false
date: Fri, 08 Oct 2021 23:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2232'
---

<div>   
<div class="content">
                                                                    
                                                        <div style="margin-left:0; margin-right:0"> 
 <div style="margin-left:0; margin-right:0"> 
  <div style="margin-left:0; margin-right:0"> 
   <p style="margin-left:0; margin-right:0">jQuery UI 1.13.0 已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jqueryui.com%2F2021%2F10%2Fjquery-ui-1-13-0-released%2F" target="_blank">发布</a>。此版本的主要更新重点是提升与最近发布的 jQuery 版本的兼容性，<span data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333">因此开发团队将大多数破坏性变更（例如删除已弃用的 API 和删除旧版浏览器支持）推迟到了未来版本。</span></p> 
   <p style="margin-left:0; margin-right:0">其他更新内容包括：</p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>修复部分安全问题</li> 
    <li>删除被废弃使用的 jQuery API。<span data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333">当使用 jQuery Migrate 3.3.2 对 jQuery 3.6.0 运行其测试套件时，jQuery UI 1.13 不会触发 jQuery Migrate 警告，即此版本发布时的最新版本。</span></li> 
    <li><span data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333">取消对 jQuery 1.7 的支持；不过仍然支持 jQuery 1.8 和更高版本。</span></li> 
    <li><span data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333">在此版本中，下载生成器生成的所有单独模块文件以及捆绑的 jQuery UI 副本的所有代码都在严格模式下运行。这对大多数用户来说并不重要，因为自 2016 年发布 3.0 以来，jQuery 一直在严格模式下运行。</span></li> 
   </ul> 
   <p style="margin-left:0; margin-right:0"><span data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333">除此之外，还添加了两个小功能：</span></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>Accordion的 header 选项现在不仅可以接受匹配 header 元素的选择器，还可以接受一个以 accordion 元素为参数并返回 header 元素的函数；<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fapi.jqueryui.com%2Faccordion%2F%23option-header">详情查看文档</a>。</li> 
    <li>日期选择器选项现在包括可选的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fapi.jqueryui.com%2Fdatepicker%2F%23option-onUpdateDatepicker">onUpdateDatepicker 回调</a>，当日期选择器小部件的 DOM 更新时会调用。</li> 
   </ul> 
   <p style="margin-left:0; margin-right:0">开发团队还提到，为了简化 jQuery UI 的维护，他们正在淘汰 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.jqueryui.com%2F" target="_blank">https://bugs.jqueryui.com</a> 上的旧错误跟踪器（将其保持为只读模式），未来将通过 GitHub issue 处理和跟踪 bug。</p> 
   <p style="margin-left:0; margin-right:0"><span data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333">在过去的几年里，jQuery UI 一直在努力寻找贡献者；他们的目标是将其更多地转移到维护状态：确保该库与新的 jQuery 版本兼容，并且安全问题得到修复，但没有计划开发新的重要功能。开发团队还将尝试修复 jQuery UI 1.12.1 的重要回归错误；不过较旧的长期错误可能无法修复。</span></p> 
   <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjqueryui.com%2Fchangelog%2F1.13.0%2F" target="_blank">详细更新说明查看 Changelog</a>。</p> 
   <p style="margin-left:0; margin-right:0"><strong>下载</strong></p> 
   <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjqueryui.com%2Fdownload%2Fall%2F" target="_blank"><strong>File Downloads</strong></a></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>Development Bundle: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjqueryui.com%2Fresources%2Fdownload%2Fjquery-ui-1.13.0.zip" target="_blank">https://jqueryui.com/resources/download/jquery-ui-1.13.0.zip</a></li> 
    <li>Themes Package: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjqueryui.com%2Fresources%2Fdownload%2Fjquery-ui-themes-1.13.0.zip" target="_blank">https://jqueryui.com/resources/download/jquery-ui-themes-1.13.0.zip</a></li> 
   </ul> 
   <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjquery%2Fjquery-ui%2F" target="_blank"><strong>Git</strong></a><strong> (contains source files, with @VERSION replaced with 1.13.0, base theme only)</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>Tag: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjquery%2Fjquery-ui%2Ftree%2F1.13.0" target="_blank">https://github.com/jquery/jquery-ui/tree/1.13.0</a></li> 
   </ul> 
  </div> 
 </div> 
 <div style="margin-left:0; margin-right:0">
   
 </div> 
</div> 
<div style="margin-left:0; margin-right:0"> 
 <div style="margin-left:0; margin-right:8px; text-align:center">
   
 </div> 
 <div style="margin-left:-4px; margin-right:-4px; text-align:start">
   
 </div> 
 <div style="margin-left:0; margin-right:0; text-align:start"> 
  <p> </p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            