
---
title: 'SunnyUI 新版 V3.2.4 发布啦！C# WinForm 开源控件库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2021/0324/213615_54240ba9_416720.png'
author: 开源中国
comments: false
date: Tue, 13 Sep 2022 09:13:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2021/0324/213615_54240ba9_416720.png'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:start"> 
 <h1 style="margin-left:0; margin-right:0"><img alt="SunnyUI" src="https://images.gitee.com/uploads/images/2021/0324/213615_54240ba9_416720.png" referrerpolicy="no-referrer"></h1> 
</div> 
<div style="text-align:start"> 
 <div> 
  <div> 
   <div style="text-align:left"> 
    <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/yhuse/SunnyUI/stargazers"><img alt="star" src="https://gitee.com/yhuse/SunnyUI/badge/star.svg?theme=gvp" referrerpolicy="no-referrer"></a><span> </span><a href="https://gitee.com/yhuse/SunnyUI/members"><img alt="fork" src="https://gitee.com/yhuse/SunnyUI/badge/fork.svg?theme=gvp" referrerpolicy="no-referrer"></a></p> 
    <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
     <li>帮助文档:<span> </span><a href="https://gitee.com/yhuse/SunnyUI/wikis/pages">https://gitee.com/yhuse/SunnyUI/wikis/pages</a></li> 
     <li>Gitee:<span> </span><a href="https://gitee.com/yhuse/SunnyUI">https://gitee.com/yhuse/SunnyUI</a></li> 
     <li>GitHub:<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fyhuse%2FSunnyUI">https://github.com/yhuse/SunnyUI</a></li> 
     <li>Nuget:<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FSunnyUI%2F">https://www.nuget.org/packages/SunnyUI/</a></li> 
     <li>Blog:<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.cnblogs.com%2Fyhuse">https://www.cnblogs.com/yhuse</a></li> 
    </ul> 
    <p style="margin-left:0; margin-right:0"><span style="background-color:#ffffff; color:#40485b">SunnyUI.Net 是基于.Net Framework 4.0~4.8、.Net 6 框架的 C# WinForm 开源控件库、工具类库、扩展类库、多页面开发框架。</span></p> 
    <p style="margin-left:0; margin-right:0"><img height="720" src="https://oscimg.oschina.net/oscnet/up-e64d9682c21025cf96222759b286f777fbd.png" width="1024" referrerpolicy="no-referrer"></p> 
    <p style="margin-left:0; margin-right:0"><span style="background-color:#ffffff; color:#333333">此版本更新内容为：</span></p> 
    <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">+ 增加 * 修改 - 删除</span></p> 
   </div> 
  </div> 
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:left">2022-09-11 V3.2.4</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong><img alt="⭐" height="14" src="https://cn-assets.gitee.com/assets/emoji/star-1862a7dd379953410da6c9a141e8d95e.png" width="14" referrerpolicy="no-referrer"><span> </span>重构多页面框架传值</strong><br> * UIForm: 重构多页面框架传值：删除SetParamToPage<br> * UIForm: 重构多页面框架传值：框架发送给页面 SendParamToPage 函数<br> * UIForm: 重构多页面框架传值：接收页面传值 ReceiveParams 事件<br> * UIPage: 重构多页面框架传值：删除SetParam，FeedbackToFrame<br> * UIPage: 重构多页面框架传值：页面发送给框架 SendParamToFrame 函数<br> * UIPage: 重构多页面框架传值：页面发送给框架 SendParamToPage 函数<br> * UIPage: 重构多页面框架传值：接收框架、页面传值 ReceiveParams 事件<br> <strong><img alt="⭐" height="14" src="https://cn-assets.gitee.com/assets/emoji/star-1862a7dd379953410da6c9a141e8d95e.png" width="14" referrerpolicy="no-referrer"><span> </span>UIListBox: 修复Click，DoubleClick事件</strong><br> * UIListBox: 修复Click，DoubleClick事件，替换ItemClick，ItemDoubleClick<br> <strong><img alt="⭐" height="14" src="https://cn-assets.gitee.com/assets/emoji/star-1862a7dd379953410da6c9a141e8d95e.png" width="14" referrerpolicy="no-referrer"><span> </span>其他更新内容：</strong><br> * UIForm: 修复继承页面可响应WM_HOTKEY消息<br> * UIComboDataGridView: 增加过滤字异常判断<br> * UIBarChart: Option.YAxis.ShowGridLine为false时，不显示水平表格虚线<br> * 下拉框控件文字位置微调，和文本框显示位置一致<br> * UITextBox: 修复了无水印文字时，光标有时不显示的问题<br> * UIDataGridViewFooter: 重构文字显示<br> * UIProcessBar: 修改最大值至少为1<br> * UIImageListBox: 增加了一些事件<br> * UIForm: 重构页面添加、选择、删除事件<br> * UIComboBox: 下拉框边框可设置颜色<br> * UIButton: 增加同一个容器的相同GroupIndex的按钮控件的Selected单选<br> * UINavMenu: 修复选中节点右侧图标前景色<br> * UIBarChart: 增加数据可为Nan<br> * UILineChart: 修复数据全为Nan时绘制出错<br> * 增加UIKnob的Demo</p>
                                        </div>
                                      
</div>
            