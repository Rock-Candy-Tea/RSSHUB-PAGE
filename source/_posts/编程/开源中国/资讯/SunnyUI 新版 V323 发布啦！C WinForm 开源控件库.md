
---
title: 'SunnyUI 新版 V3.2.3 发布啦！C# WinForm 开源控件库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2021/0324/213615_54240ba9_416720.png'
author: 开源中国
comments: false
date: Tue, 16 Aug 2022 10:01:00 GMT
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
<h4 style="margin-left:0; margin-right:0; text-align:left">2022-08-16 V3.2.3</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>〇〇 关于图表数据显示格式化已经重构，需重点关注，可参考Demo：</strong><br> * UILineChart: 数据显示的小数位数重构调整至数据序列 Series.XAxisDecimalPlaces，YAxisDecimalPlaces<br> * UILineChart: 数据显示的日期格式重构调整至数据序列 Series.XAxisDateTimeFormat<br> * UILineChart: 坐标轴的小数位数重构调整至坐标轴标签 AxisLabel.DecimalPlaces<br> * UILineChart: 坐标轴的日期格式重构调整至坐标轴标签 AxisLabel.DateTimeFormat<br> * UIBarChart: 数据显示的小数位数重构调整至数据序列 Series.DecimalPlaces<br> * UIBarChart: 坐标轴的小数位数重构调整至坐标轴标签 AxisLabel.DecimalPlaces<br> * UIDoughnutChart: 数据显示的小数位数重构调整至Option.DecimalPlaces<br> * UIPieChart: 数据显示的小数位数重构调整至Option.DecimalPlaces<br> * UIDoubleUpDown, UIProcessBar, UITextBox: 小数位数统一改名为DecimalPlaces<br> <strong>〇〇 UITabControlMenu需要重新设置ItemSize：</strong><br> * UITabControlMenu: 重写ItemSize，将宽、高调整为正常显示<br> <strong>〇〇 其他更新内容：</strong><br> * UITreeView: 去掉窗体控件的默认设计器<br> * UINavBar: 删除界面此控件的编辑器<br> + UIKnob: 新增控件<br> * UIBarChart: 修复Y轴显示名称<br> * IniFile: 读数据缓存增加到2048，但还是不建议Ini文件保存过长的数据<br> * UILineChart: 修复双Y轴时，数据为空，刷新出错的问题<br> * UITextBox: 修改了描述错别字<br> * UIChartOption: 清理一些无用的属性<br> * UIDataGridView: 修复了ScrollBars为None时仍然显示滚动条的问题<br> * UITextBox: 修复了有水印文字时，不响应Click和DoubleClick事件的问题<br> * UILineChart: 修复双Y轴数据点提示文字显示<br> * UIGifAvatar: 重写图片刷新流程，减少内存及GC<br> * UIForm: 多页面框架增加程序关闭时调用UIPage的Final和FormClosed事件<br> + 增加LineAweSome字体图标，测试下看看效果<br> - 删除LineAweSome字体图标，经过测试显示效果不理想</p>
                                        </div>
                                      
</div>
            