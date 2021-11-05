
---
title: 'ZUI 前端框架发布 1.10.0 版本，新增下拉选择器插件，兼容 Chosen 用法'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://user-images.githubusercontent.com/472425/140286357-665495e1-7eef-47b3-96ed-5c37cef607c0.png'
author: 开源中国
comments: false
date: Fri, 05 Nov 2021 02:45:00 GMT
thumbnail: 'https://user-images.githubusercontent.com/472425/140286357-665495e1-7eef-47b3-96ed-5c37cef607c0.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>本次更新新增下拉选择器插件，兼容 Chosen 用法，支持大数目选项列表以及从服务器进行搜索；本次更新还修复了大量已知问题，欢迎更新！</p> 
 <p><strong>新增下拉选择器组件</strong></p> 
 <table> 
  <thead> 
   <tr> 
    <th>单选模式</th> 
    <th>多选模式</th> 
   </tr> 
  </thead> 
  <tbody> 
   <tr> 
    <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F472425%2F140286357-665495e1-7eef-47b3-96ed-5c37cef607c0.png" target="_blank"><img alt="picker2" src="https://user-images.githubusercontent.com/472425/140286357-665495e1-7eef-47b3-96ed-5c37cef607c0.png" referrerpolicy="no-referrer"></a></td> 
    <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F472425%2F140286070-5aa421d5-1812-45bd-8b0f-287f5fbf60c1.png" target="_blank"><img alt="picker" src="https://user-images.githubusercontent.com/472425/140286070-5aa421d5-1812-45bd-8b0f-287f5fbf60c1.png" referrerpolicy="no-referrer"></a></td> 
   </tr> 
  </tbody> 
 </table> 
 <h3>更新明细</h3> 
 <ul> 
  <li>下拉选择器： 
   <ul> 
    <li>新增下拉选择器组件，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openzui.com%2F%23javascript%2Fpicker" target="_blank">详情参考</a>；</li> 
   </ul> </li> 
  <li>表单： 
   <ul> 
    <li>优化了火狐下单选框控件样式，移除了高亮时不协调的虚线边框；</li> 
   </ul> </li> 
  <li>下拉菜单： 
   <ul> 
    <li>添加对特殊辅助类 <code>.not-clear-menu</code> 的支持，在 <code>.dropdown-menu</code> 内使用此辅助类可以禁用用户点击特定元素时隐藏下拉菜单；</li> 
   </ul> </li> 
  <li>对话框和对话框触发器： 
   <ul> 
    <li>修复了打开对话框可能导致页面抖动的问题；</li> 
    <li>修复了当启用 <code>scrollInside</code> 选项后，对话框尺寸可能计算错误的问题；</li> 
    <li>修复了有时执行 <code>$.fn.modalTrigger(methodName)</code> 导致重复监听触发打开事件的问题；</li> 
   </ul> </li> 
  <li>上下文菜单： 
   <ul> 
    <li>新增下拉菜单增强模式；</li> 
    <li>新增了一些功能选项： 
     <ul> 
      <li>新增选项 <code>limitInsideWindow</code> 用于限制菜单面板显示在窗口区域内；</li> 
      <li>新增选项 <code>show</code> 用于初始化完成后立即显示菜单；</li> 
      <li>新增选项 <code>toggleTrigger</code> 用于启用点击触发元素切换菜单显示和隐藏行为；</li> 
      <li>新增选项 <code>menuCreator</code> 用于自定义生成菜单元素；</li> 
      <li>新增选项 <code>position</code> 用于动态返回菜单位置；</li> 
     </ul> </li> 
    <li>新增 <code>ContextMenu.isShow</code> 方法用于检查指定 ID 菜单是否已经显示；</li> 
   </ul> </li> 
  <li>Chosen： 
   <ul> 
    <li>优化了清除按钮图标在不同浏览器上的样式差异；</li> 
   </ul> </li> 
  <li>富文本编辑器（Kindeditor）： 
   <ul> 
    <li>新增选项 <code>transferEvents</code> 用于将编辑器 iframe 页面内的点击事件传递到父级页面；</li> 
    <li>优化插入音视频功能，现在使用 HTML5 音视频实现，移除了 flash 音视频实现；</li> 
    <li>优化了界面上一些图标；</li> 
    <li>优化了表格功能和样式，修复了界面可能显示错误的问题；</li> 
    <li>修复了全屏动作之后编辑器内的锚点丢失的问题；</li> 
    <li>修复了表格隔行变色设置无效的问题；</li> 
    <li>修复了百度地图无法使用的问题，更新了 API 调用形式；</li> 
    <li>修复了有时对话框由于位置计算错误可能无法显示的问题；</li> 
    <li>修复了加载中图标可能没有显示的问题；</li> 
   </ul> </li> 
  <li>日历： 
   <ul> 
    <li>优化周末栏头部文本排版，避免文本换行显示；</li> 
   </ul> </li> 
  <li>日期时间选择器： 
   <ul> 
    <li>优化仅选择时间时的情况，此时下拉面板不显示底部切换日期的按钮；</li> 
   </ul> </li> 
  <li>图表： 
   <ul> 
    <li>修复了曲线图中热点检查可能不符合预期的问题；</li> 
   </ul> </li> 
  <li>辅助方法： 
   <ul> 
    <li>为 IE8 默认添加 <code>Array.forEach</code> 和 <code>Array.isArray</code> polyfills；</li> 
    <li>修复了 <code>$.zui.uuid()</code> 在 IE11 下失效的问题；</li> 
    <li>修复了因为使用 <code>const</code> 关键字导致在 IE8 下 JS 执行错误。</li> 
   </ul> </li> 
 </ul> 
 <div> 
  <h3>下载安装</h3> 
  <div> 
   <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feasysoft%2Fzui%2Freleases%2Fdownload%2Fv1.10.0%2Fzui-1.10.0-dist.zip" target="_blank"><span style="color:#337fe5">zui-1.10.0-dist.zip</span></a></p> 
   <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feasysoft%2Fzui%2Farchive%2Frefs%2Ftags%2Fv1.10.0.zip" target="_blank"><span style="color:#337fe5">Source code</span><span style="color:#337fe5"> (zip) </span></a></p> 
   <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feasysoft%2Fzui%2Farchive%2Frefs%2Ftags%2Fv1.10.0.tar.gz" target="_blank"><span style="color:#337fe5">Source code</span><span style="color:#337fe5"> (tar.gz) </span></a></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            