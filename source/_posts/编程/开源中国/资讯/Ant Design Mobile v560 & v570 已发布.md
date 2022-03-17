
---
title: 'Ant Design Mobile v5.6.0 & v5.7.0 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9597'
author: 开源中国
comments: false
date: Thu, 17 Mar 2022 07:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9597'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="color:#333333">Ant Design Mobile v5.6.0 和 </span><span style="color:#000000">v5.7.0 </span><span style="color:#333333">发布了。Ant Design Mobile 即 Ant Design 移动端设计规范， 是 Ant Design 的移动规范的 React 实现，服务于蚂蚁及口碑无线业务。</span></p> 
<h3><span style="color:#333333">Ant Design Mobile v5.6.0 </span></h3> 
<ul> 
 <li>特性 
  <ul> 
   <li>TabBar.Item 的 <code>title</code> 属性现在支持渲染函数动态生成内容了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4911" target="_blank">#4911</a></li> 
   <li>FloatingBubble 增加了 <code>--background</code> CSS 变量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4912" target="_blank">#4912</a></li> 
   <li>ActionSheet 增加了 <code>popupClassName</code> 和 <code>popupStyle</code> 属性 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4910" target="_blank">#4910</a></li> 
  </ul> </li> 
 <li>优化 
  <ul> 
   <li>现在 Cascader 和 CascaderView 当层级减少时，会自动选择到最后一个可选的层级 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fcommit%2F423d7146395f9cd9d3ac130025e360c5250bedca" target="_blank">423d714</a></li> 
  </ul> </li> 
 <li>修复 
  <ul> 
   <li>Checkbox & Radio 调整了 onClick 的行为，修复了一些内部元素的点击事件无法被外层捕获的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fcommit%2Fc4678873b07dda0f3817148e8eff61ec6ddcb3b2" target="_blank">c467887</a></li> 
   <li>修复了 Badge 内容如果为数字 0，会无法正常显示的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4906" target="_blank">#4906</a></li> 
   <li>修复了 Modal Dialog ImageViewer ActionSheet 组件调用 <code>show()</code> 后如果立即调用 <code>close()</code> / <code>clear()</code> 可能会无法正确地关闭弹层的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4897" target="_blank">#4897</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4909" target="_blank">#4909</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4914" target="_blank">#4914</a></li> 
  </ul> </li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Freleases%2Ftag%2Fv5.6.0" target="_blank">https://github.com/ant-design/ant-design-mobile/releases/tag/v5.6.0</a> </p> 
<p> </p> 
<h3><span style="color:#333333">Ant Design Mobile v5.6.1</span></h3> 
<ul> 
 <li>特性 
  <ul> 
   <li>Form.Item 现在会暴露出底层 List.Item 的 <code>clickable</code> 属性了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fcommit%2F212d2c75a6d24d40f3166ddafc4c59148cdda197" target="_blank">212d2c7</a></li> 
  </ul> </li> 
 <li>优化 
  <ul> 
   <li>Popover 增加了最大宽度的限制 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fcommit%2F0c187cffcd96e6ddc8ef7aee943945b470f40e32" target="_blank">0c187cf</a></li> 
   <li>优化了 Empty 和 ErrorBlock 中图片资源的引入方式 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fcommit%2F6e8262465729a8d79449f59949a32d952386be4f" target="_blank">6e82624</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fcommit%2F6733003cc994d8a595f84c265ece72c5462f2c87" target="_blank">6733003</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fcommit%2F484e0f47d4f4c971b2505c158e164267e86de762" target="_blank">484e0f4</a><span style="color:#333333"> </span></li> 
  </ul> </li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Freleases%2Ftag%2Fv5.6.1" target="_blank">https://github.com/ant-design/ant-design-mobile/releases/tag/v5.6.1</a> </p> 
<p> </p> 
<h3><span style="color:#333333">Ant Design Mobile v5.7.0 </span></h3> 
<ul> 
 <li>特性 
  <ul> 
   <li>Calendar 增加了 <code>allowClear</code> 属性，同时 <code>onChange</code> 中的 <code>val</code> 参数现在可能为 <code>null</code> 了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fcommit%2F2f6a928de76492669f8c8fc86ada7158840f67ac" target="_blank">2f6a928</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fcommit%2Fd4513d0c867a1f76164db49c64857c5477bdac66" target="_blank">d4513d0</a></li> 
  </ul> </li> 
 <li>优化</li> 
 <li>修复 
  <ul> 
   <li>修复了 Picker 系列组件的 <code>onConfirm</code> 中 <code>extend</code> 参数的数据可能有误的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fissues%2F4924" target="_blank">#4924</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fcommit%2F2e654ce1342accb5f7316da2589e371de95449d4" target="_blank">2e654ce</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fcommit%2F0293ee9c5a74e0e406b39d37b60828a39e3435e0" target="_blank">0293ee9</a></li> 
   <li>修复了 Calendar 在受控模式下行为异常的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fissues%2F4916" target="_blank">#4916</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fcommit%2F2f6a928de76492669f8c8fc86ada7158840f67ac" target="_blank">2f6a928</a></li> 
  </ul> </li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Freleases%2Ftag%2Fv5.7.0" target="_blank">https://github.com/ant-design/ant-design-mobile/releases/tag/v5.7.0</a></p>
                                        </div>
                                      
</div>
            