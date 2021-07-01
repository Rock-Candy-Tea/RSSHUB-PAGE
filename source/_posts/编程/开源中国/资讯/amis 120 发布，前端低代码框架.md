
---
title: 'amis 1.2.0 发布，前端低代码框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9294'
author: 开源中国
comments: false
date: Thu, 01 Jul 2021 09:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9294'
---

<div>   
<div class="content">
                                                                    
                                                        <p>amis 1.2.0 已经发布，前端低代码框架.</p> 
<p>此版本更新内容包括：</p> 
<h2>Feature ✨</h2> 
<p><strong>Breaking Change</strong>：</p> 
<p>在 1.2.0 之前的版本中，表单项和非表单项在配置上不一致，名称重名也带来了很多困惑，系统实现也得分两份带来了维护成本，因此 1.2.0 对配置项做了调整，使得配置写法统一，表单项和非表单项也能混用了。</p> 
<blockquote> 
 <p>1.2.0 版本向下兼容之前的配置，但推荐使用新的配置方式。</p> 
</blockquote> 
<p>文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaidu.github.io%2Famis%2Fzh-CN%2Fdocs%2Fstart%2F1-2-0" target="_blank">https://baidu.github.io/amis/zh-CN/docs/start/1-2-0</a> 相关PR：(#2039) (#2058) (#2059) (#2064) (#2082) (#2083) (#2084) (#2085) (#2086) (#2114) (#2118) (#2131) (#2132) (#2134) (#2135) (#2151) (#2172)</p> 
<p>其他 Feature：</p> 
<ul> 
 <li>Dialog 支持配置点击其它区域关闭 (#2176) <a href="https://www.oschina.net/nwind">@nwind </a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaidu.github.io%2Famis%2Fzh-CN%2Fcomponents%2Fdialog%3Fpage%3D1%23%25E9%2585%258D%25E7%25BD%25AE-esc-%25E9%2594%25AE%25E5%2592%258C%25E7%2582%25B9%25E5%2587%25BB%25E5%25A4%2596%25E9%2583%25A8%25E5%2585%25B3%25E9%2597%25AD%25E5%25BC%25B9%25E6%25A1%2586" target="_blank">文档</a></li> 
 <li>新增 <code>code</code> 代码高亮组件 (#2171) <a href="https://www.oschina.net/nwind">@nwind </a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaidu.github.io%2Famis%2Fzh-CN%2Fcomponents%2Fcode" target="_blank">文档</a></li> 
 <li>TableView 组件 (#2139) (#2163) <a href="https://www.oschina.net/nwind">@nwind </a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaidu.github.io%2Famis%2Fzh-CN%2Fcomponents%2Ftable-view" target="_blank">文档</a></li> 
 <li>单个表单项支持后端校验 (#2127) @RickCole21 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaidu.github.io%2Famis%2Fzh-CN%2Fcomponents%2Fform%2Fformitem%23%25E9%2580%259A%25E8%25BF%2587%25E8%25A1%25A8%25E5%258D%2595%25E9%25A1%25B9%25E6%25A0%25A1%25E9%25AA%258C%25E6%258E%25A5%25E5%258F%25A3" target="_blank">文档</a></li> 
 <li>增加季度范围选择器 (#2080) (#2115) <a href="https://www.oschina.net/xuzhendong666">@毛主席夸我帅 </a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaidu.github.io%2Famis%2Fzh-CN%2Fcomponents%2Fform%2Finput-quarter-range" target="_blank">文档</a></li> 
 <li>Added German translation (#2063) @abasse</li> 
</ul> 
<h2>Enhancement</h2> 
<ul> 
 <li>升级 <code>echarts</code>、<code>react-json-tree</code>、<code>react-visibility-sensor</code> 到最新版本 (#2181) <a href="https://www.oschina.net/nwind">@nwind </a></li> 
 <li>当表单 <code>disabled</code> 时隐藏 QuickEdit (#2178) @qinhaoyan</li> 
 <li>Avator <code>icon</code> 关键字支持上下文 (#2154) @tonglsh</li> 
 <li><code>componentWillMount</code> & <code>componentWillReceiveProps</code> 调整 (#2167) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>月度选择器支持年份选择切换 (#2150) <a href="https://www.oschina.net/xuzhendong666">@毛主席夸我帅 </a></li> 
 <li>月份选择器增加快捷键支持 (#2145) <a href="https://www.oschina.net/xuzhendong666">@毛主席夸我帅 </a></li> 
 <li>导出 Excel 的 tpl 模式默认滤掉 html 标签 (#2147) <a href="https://www.oschina.net/nwind">@nwind </a></li> 
 <li>如果有列被隐藏显示激活状态提醒 (#2123) <a href="https://www.oschina.net/nwind">@nwind </a></li> 
 <li>组件 <code>value</code> 逻辑优化 (#2103) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>JSSDK 支持 hash 路由改造 (#2105) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>DateTime 组件时间支持可点选 (#2100) @allenve</li> 
 <li>FieldSet 支持 <code>disabled</code> (#2106) @RickCole21</li> 
 <li>Image & File 组件上传过程中取消逻辑完善 (#2092) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>quickEdit <code>controls</code> 调整 (#2076) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>NestedSelect <code>noResultText</code> 支持模板 (#2048) @RickCole21</li> 
 <li>Select 支持不换行模式 (#2049) @Akikonata</li> 
 <li>Popover 默认显示 (#2047) <a href="https://www.oschina.net/nwind">@nwind </a></li> 
 <li>增加字体样式 helper (#2046) <a href="https://www.oschina.net/nwind">@nwind </a></li> 
</ul> 
<h2>Bugfix</h2> 
<ul> 
 <li>修复 JSSDK 的 <code>alert</code>、<code>toast</code> 不支持 <code>locale</code> 设置问题 (#2170) <a href="https://www.oschina.net/nwind">@nwind </a></li> 
 <li>修复搜索框 <code>clear-and-submit</code> 时有多级属性时的错误行为 (#2162) @cyboning</li> 
 <li>修复 Table 拖拽时子级找不到父级 (#2164) @qinhaoyan</li> 
 <li>修复弹窗打开卡主问题 (#2146) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>避免条件组合中的字段文本折行 (#2140) <a href="https://www.oschina.net/nwind">@nwind </a></li> 
 <li>Combo tabs vertical 模式文本折行问题 (#2116) @hsm-lv</li> 
 <li>修复 File <code>disabled</code> 无效问题 (#2113) @RickCole21</li> 
 <li>Select 高亮问题 (#2111) @RickCole21</li> 
 <li>修复 FormItem 通过 <code>children</code> 返回 <code>jsx.element</code> 的方式导致重复刷新的问题 (#2099) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>ButtonToolbar 中数据同步不及时 (#2097) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
 <li>优化 <code>options</code> 数据量太大时计算量太大的问题 (#2087) <a href="https://www.oschina.net/linziwei">@WEI丶子林 </a></li> 
 <li>修复 <code>blob</code> 模式返回报错信息不显示问题 (#2081) <a href="https://www.oschina.net/nwind">@nwind </a></li> 
 <li>修复导出在 Excel csv 乱码问题 (#2068) <a href="https://www.oschina.net/nwind">@nwind </a></li> 
 <li>处理某些特殊情况下会传入空字符串导致无法识别值的问题 (#2043) @Akikonata</li> 
 <li>文件上传组件样式问题 (#2044) @hsm-lv</li> 
 <li>修复弹窗自动关闭问题 (#2180) @hsm-lv</li> 
 <li>优化 Static 下的 quickEdit 处理逻辑 (#2184) <a href="https://www.oschina.net/2betop">@2betop </a></li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/baidu/amis/releases/1.2.0">https://gitee.com/baidu/amis/releases/1.2.0</a></p>
                                        </div>
                                      
</div>
            