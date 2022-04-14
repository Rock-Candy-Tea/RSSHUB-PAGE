
---
title: 'Ant Design 4.20.0-alpha.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3245'
author: 开源中国
comments: false
date: Thu, 14 Apr 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3245'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#000000">Ant Design 4.20.0-alpha.0 现已发布，主要变化如下：</span></p> 
<ul> 
 <li>新增组件 Segmented。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34319" target="_blank">#34319</a></li> 
 <li>Table 
  <ul> 
   <li>Table 列筛选条件重置时，支持重置为默认值而非空值。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34355" target="_blank">#34355</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fheiyu4585" target="_blank">@heiyu4585</a></li> 
   <li>修复 Table<span> </span><code>size="small"</code><span> </span>时列头背景色和选择列宽度的样式问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34963" target="_blank">#34963</a></li> 
   <li>补全 Table 的德语国际化文案。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34836" target="_blank">#34836</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpfedan" target="_blank">@pfedan</a></li> 
  </ul> </li> 
 <li>Tree 
  <ul> 
   <li>Tree 组件的<span> </span><code>switcherIcon</code><span> </span>属性支持 render-prop。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34470" target="_blank">#34470</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzqran" target="_blank">@zqran</a></li> 
   <li>Tree 支持<span> </span><code>rootClassName</code><span> </span>and<span> </span><code>rootStyle</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34578" target="_blank">#34578</a></li> 
  </ul> </li> 
 <li>Anchor<span> </span><code>getCurrentAnchor</code><span> </span>参数中返回默认高亮项。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34799" target="_blank">#34799</a></li> 
 <li>Dropdown 支持方向键切换选项。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34738" target="_blank">#34738</a></li> 
 <li>Cascader 添加<span> </span><code>showCheckedStrategy</code><span> </span>用于配置回填方式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34568" target="_blank">#34568</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fheiyu4585" target="_blank">@heiyu4585</a></li> 
 <li>Typography 的<span> </span><code>onCopy</code><span> </span>方法支持获取点击事件对象。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34655" target="_blank">#34655</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyzwxk" target="_blank">@yzwxk</a></li> 
 <li>Grid 支持<span> </span><code>justify="space-evenly"</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34606" target="_blank">#34606</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgp5251" target="_blank">@gp5251</a></li> 
 <li>Dialog 及 Image 支持<span> </span><code>rootClassName</code><span> </span>属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34574" target="_blank">#34574</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fheiyu4585" target="_blank">@heiyu4585</a></li> 
 <li>修复 Skeleton 在没有<span> </span><code>children</code><span> </span>并设置<span> </span><code>loading</code><span> </span>为 false 时提示<span> </span><code>Nothing was returned from render</code><span> </span>的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34872" target="_blank">#34872</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAlbertAZ1992" target="_blank">@AlbertAZ1992</a></li> 
 <li>修复 BackTop 组件在严格模式下不能正常工作的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34858" target="_blank">#34858</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftmkx" target="_blank">@tmkx</a></li> 
 <li>修复 Title、Text、Paragraph 组件不支持<span> </span><code>ref</code><span> </span>的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34847" target="_blank">#34847</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMQuy" target="_blank">@MQuy</a></li> 
 <li>Input 
  <ul> 
   <li>Input.Group 对子组件屏蔽 Form.Item 的样式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34764" target="_blank">#34764</a></li> 
   <li>调整 Form<span> </span>下 TextArea 的样式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34714" target="_blank">#34714</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMadCcc" target="_blank">@MadCcc</a></li> 
   <li>修复 Form<span> </span><code>labelCol=&#123;&#123; sm: 24 &#125;&#125;</code><span> </span>和<span> </span><code>wrapperCol=&#123;&#123; sm: 24 &#125;&#125;</code><span> </span>时样式错乱的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34907" target="_blank">#34907</a></li> 
   <li>修复 Badge 在 RTL 模式下、独立使用时的动画效果。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34899" target="_blank">#34899</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhmz22" target="_blank">@hmz22</a></li> 
   <li>修复 Checkbox 缺少<span> </span><code>aria-checked</code><span> </span>属性导致屏幕阅读器识别错误的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34862" target="_blank">#34862</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSpaNb4" target="_blank">@SpaNb4</a></li> 
   <li>Spin 添加<span> </span><code>aria</code><span> </span>属性以提升可访问性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34408" target="_blank">#34408</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fheiyu4585" target="_blank">@heiyu4585</a></li> 
   <li>为 Breadcrumb 层次结构增加可访问性支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34082" target="_blank">#34082</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FVladimirOtroshchenko" target="_blank">@VladimirOtroshchenko</a></li> 
   <li>Menu 添加<span> </span><code>items</code><span> </span>数据化菜单项支持以为将来性能提升做准备，并且<span> </span><code>children</code><span> </span>将会在下个大版本中废弃。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34559" target="_blank">#34559</a></li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Freleases%2Ftag%2F4.20.0-alpha.0" target="_blank">https://github.com/ant-design/ant-design/releases/tag/4.20.0-alpha.0</a></p>
                                        </div>
                                      
</div>
            