
---
title: 'Ant Design 4.18.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4100'
author: 开源中国
comments: false
date: Tue, 28 Dec 2021 07:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4100'
---

<div>   
<div class="content">
                                                                                            <p>Ant Design 4.18.0 发布了，此版本带来如下变更：</p> 
<ul> 
 <li><span> </span>修复 Skeleton 不支持<span> </span><code>style</code><span> </span>的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33405" target="_blank">#33405</a></li> 
 <li><span> </span>修复 Descriptions 内使用其他组件会被切割的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33392" target="_blank">#33392</a></li> 
 <li><span> </span>统一类 Select 组件泛型定义为 OptionType 以支持自定义 FieldNames 匹配。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33364" target="_blank">#33364</a></li> 
 <li><span> </span>修复 Slider 禁用时<span> </span><code>hover</code><span> </span>色彩的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33369" target="_blank">#33369</a><span> </span></li> 
 <li>Table 
  <ul> 
   <li><span> </span>Table<span> </span><code>colSpan</code><span> </span>与<span> </span><code>rowSpan</code><span> </span>迁移至<span> </span><code>onCell</code><span> </span>方法中，以优化渲染性能。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33114" target="_blank">#33114</a></li> 
   <li><span> </span>Table 支持 Table.EXPAND_COLUMN 和 Table.SELECTION_COLUMN 以实现自定义列排序。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33026" target="_blank">#33026</a></li> 
  </ul> </li> 
 <li>Form 
  <ul> 
   <li><span> </span>Form.List 嵌套使用 Form.Item 时不再需要手工指定<span> </span><code>fieldKey</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32689" target="_blank">#32689</a></li> 
   <li><span> </span>Form 现在支持通过<span> </span><code>labelWrap</code><span> </span>开启标签可换行。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33048" target="_blank">#33048</a></li> 
  </ul> </li> 
 <li><span> </span>ConfigProvider 支持 Form 的 colon 配置。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fcommit%2F9bc148a" target="_blank">9bc148a</a><span> </span></li> 
 <li><span> </span><code>InputNumber</code><span> </span>增加<span> </span><code>prefix</code><span> </span>属性支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32600" target="_blank">#32600</a><span> </span></li> 
 <li> Modal 静态方法支持<span> </span><code>wrapClassName</code><span> </span>属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32676" target="_blank">#32676</a><span> </span></li> 
 <li><span> </span>Popconfirm 新增是否显示取消按钮。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32620" target="_blank">#32620</a><span> </span></li> 
 <li><span> </span>Dropdown.Button 新增<span> </span><code>loading</code><span> </span>属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32467" target="_blank">#32467</a><span> </span></li> 
 <li><span> </span>Input 新增<span> </span><code>showCount</code><span> </span>属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32522" target="_blank">#32522</a><span> </span></li> 
 <li><span> </span>Alert 支持<span> </span><code>closeIcon</code><span> </span>自定义关闭图标。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32345" target="_blank">#32345</a><span> </span></li> 
 <li>Typography 
  <ul> 
   <li><span> </span>对于可编辑段落，可以通过配置<span> </span><code>triggerType</code><span> </span>配置触发编辑状态。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32219" target="_blank">#32219</a></li> 
   <li><span> </span>Typography 支持<span> </span><code>enterIcon</code><span> </span>以设置编辑确认图标。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32220" target="_blank">#32220</a></li> 
  </ul> </li> 
 <li><span> </span>Divider 增加了<span> </span><code>orientationMargin</code><span> </span>属性以设置间距。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32084" target="_blank">#32084</a></li> 
 <li><span> </span>Avatar.Group 添加<span> </span><code>maxPopoverTrigger</code><span> </span>以定制剩余头像展示的触发逻辑。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32197" target="_blank">#32197</a><span> </span></li> 
 <li><span> </span>Upload 新增<span> </span><code>showUploadList.previewIcon</code><span> </span>用于自定义预览图标。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32059" target="_blank">#32059</a><span> </span></li> 
 <li> 修复加泰罗尼亚语 (ca_ES) 对 Form 缺失翻译问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33377" target="_blank">#33377</a><span> </span></li> 
 <li> <span> </span>修复芬兰语 (fi_FI) 对 Table 的缺失翻译问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33372" target="_blank">#33372</a><span> </span></li> 
 <li> <span> </span>新增高棉语 (km_KH) 语言包。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32853" target="_blank">#32853</a><span> </span></li> 
 <li> TypeScript 
  <ul> 
   <li><span> </span>添加 Upload<span> </span><code>capture</code><span> </span>定义。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33370" target="_blank">#33370</a><span> </span></li> 
  </ul> </li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Freleases%2Ftag%2F4.18.0" target="_blank">https://github.com/ant-design/ant-design/releases/tag/4.18.0</a></p>
                                        </div>
                                      
</div>
            