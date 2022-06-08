
---
title: 'Ant Design 4.21 发布，企业级 UI 设计语言和 React 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4862'
author: 开源中国
comments: false
date: Wed, 08 Jun 2022 07:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4862'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Ant Design 4.21 现已发布，主要变化如下：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>新增 Form 级别控制输入组件<span> </span><code>disabled</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35210" target="_blank">#35210</a></li> 
 <li>Tabs 组件支持<span> </span><code>popupClassName</code><span> </span>用于更多菜单。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35892" target="_blank">#35892</a></li> 
 <li>Table 组件<span> </span><code>rowSelection.onChange</code><span> </span>新增<span> </span><code>info.type</code><span> </span>参数。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35598" target="_blank">#35598</a></li> 
 <li>Typography.Paragraph 的<span> </span><code>copyable</code><span> </span>属性支持<span> </span><code>format</code><span> </span>以重置剪切板数据的 Mime Type。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35219" target="_blank">#35219</a></li> 
 <li>TreeSelect 支持<span> </span><code>treeExpandAction</code><span> </span>定义展开操作。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35618" target="_blank">#35618</a></li> 
 <li>ConfigProvider 
  <ul style="margin-left:0; margin-right:0"> 
   <li>ConfigProvider 支持全局配置 Pagination<span> </span><code>showSizeChanger</code><span> </span>属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35750" target="_blank">#35750</a></li> 
   <li>ConfigProvider 支持<span> </span><code>componentDisabled</code><span> </span>来配置组件禁用状态。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35718" target="_blank">#35718</a></li> 
   <li>重构 ConfigProvider 移除默认的<span> </span><code>renderEmpty</code><span> </span>方法以解决打包循环依赖的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35570" target="_blank">#35570</a></li> 
  </ul> </li> 
 <li>Collapse 
  <ul style="margin-left:0; margin-right:0"> 
   <li>重构 Collapse 标题部分以确保其稳定的 DOM 结构易于样式选择。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35781" target="_blank">#35781</a></li> 
   <li>重构 Collapse<span> </span><code>expandIconPosition</code><span> </span>为逻辑位置<span> </span><code>start</code><span> </span>与<span> </span><code>end</code><span> </span>以解决 RTL 下的样式问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35770" target="_blank">#35770</a></li> 
  </ul> </li> 
 <li>Progress 
  <ul style="margin-left:0; margin-right:0"> 
   <li>Progress 分步进度条支持单独自定义色彩。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35855" target="_blank">#35855</a></li> 
   <li>重构 Progress<span> </span><code>type="circle"</code><span> </span>和<span> </span><code>type="dashboard"</code><span> </span>以简化 dom 结构和带来更好的渲染效果。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35433" target="_blank">#35433</a></li> 
   <li>重构 Progress 成 React hooks。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35393" target="_blank">#35393</a></li> 
   <li>修复 Progress 进度接近 100% 间距几乎消失的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35433" target="_blank">#35433</a></li> 
   <li>修复 Progress<span> </span><code>type="dashboard"</code><span> </span>的<span> </span><code>gapDegree</code><span> </span>角度不准确的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35433" target="_blank">#35433</a></li> 
   <li>修复 Progress<span> </span><code>type="line"</code><span> </span>和<span> </span><code>strokeLinecap="butt"</code><span> </span>时的圆角样式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35822" target="_blank">#35822</a></li> 
  </ul> </li> 
 <li>Dropdown 
  <ul style="margin-left:0; margin-right:0"> 
   <li>Dropdown 支持<span> </span><code>autoFocus</code><span> </span>属性，打开时自动聚焦下拉单。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35391" target="_blank">#35391</a></li> 
   <li>修复 Dropdown 嵌套菜单注入逻辑。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35810" target="_blank">#35810</a></li> 
  </ul> </li> 
 <li>Card 
  <ul style="margin-left:0; margin-right:0"> 
   <li>使用 Skeleton 重构 Card<span> </span><code>loading</code><span> </span>属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35525" target="_blank">#35525</a></li> 
   <li>重构 Card 样式用 flex 代替 float。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35236" target="_blank">#35236</a></li> 
  </ul> </li> 
 <li>DatePicker 重构成 React hooks。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35425" target="_blank">#35425</a></li> 
 <li>将 Pagination<span> </span><code>mini</code><span> </span>模式的 className 重命名为<span> </span><code>ant-pagination-mini</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35881" target="_blank">#35881</a></li> 
 <li>重构 Popconfirm 内部实现为 Popover 组件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35676" target="_blank">#35676</a></li> 
 <li>改变 Modal confirm 组件底部按钮布局实现方式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35530" target="_blank">#35530</a></li> 
 <li>修复波浪效果在 React 18 严格模式不生效的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35889" target="_blank">#35889</a></li> 
 <li>修复 Drawer 关闭 2 次后<span> </span><code>children</code><span> </span>为 undefined 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35853" target="_blank">#35853</a></li> 
 <li>Skeleton 
  <ul style="margin-left:0; margin-right:0"> 
   <li>移除 Skeleton 默认的<span> </span><code>margin-top</code><span> </span>以便在默认情况下更对称。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35848" target="_blank">#35848</a></li> 
   <li>优化 Skeleton<span> </span><code>active</code><span> </span>的动画性能。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35836" target="_blank">#35836</a></li> 
  </ul> </li> 
 <li>移除 Radio 禁用状态时样式中的<span> </span><code>!important</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35920" target="_blank">#35920</a></li> 
 <li>TypeScript 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复 Form.List 类型<span> </span><code>FormListFieldData</code><span> </span>缺失属性<span> </span><code>fieldKey</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35884" target="_blank">#35884</a></li> 
  </ul> </li> 
 <li>国际化 
  <ul style="margin-left:0; margin-right:0"> 
   <li>添加土库曼语国际化。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35605" target="_blank">#35605</a></li> 
  </ul> </li> 
 <li>RTL 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修正 Input 和 InputNumber 的<span> </span><code>border</code><span> </span>和<span> </span><code>border-radius</code><span> </span>在 RTL 模式下的方向问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35876" target="_blank">#35876</a></li> 
  </ul> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Freleases%2Ftag%2F4.21.0" target="_blank">https://github.com/ant-design/ant-design/releases/tag/4.21.0</a></p>
                                        </div>
                                      
</div>
            