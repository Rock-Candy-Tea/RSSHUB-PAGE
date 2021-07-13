
---
title: 'Ant Design 4.16.7 发布，企业级 UI 设计语言和 React 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7828'
author: 开源中国
comments: false
date: Tue, 13 Jul 2021 07:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7828'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Ant Design 4.16.7 发布了。Ant Design 是一套企业级的 UI 设计语言和 React 实现，使用 TypeScript 构建，提供完整的类型定义文件，自带提炼自企业级中后台产品的交互语言和视觉风格、开箱即用的高质量 React 组件与全链路开发和设计工具体系。</p> 
<p>此版本更新内容如下：</p> 
<ul> 
 <li>修复 DatePicker 在 Table 内使用时日期未居中的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31306" target="_blank">#31306</a></li> 
 <li>修复 Descriptions 在 Table 内边框丢失的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31307" target="_blank">#31307</a></li> 
 <li>修复 InputNumber 边框和交互范围不匹配的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31300" target="_blank">#31300</a></li> 
 <li>Table 
  <ul> 
   <li>修复 Table 当窗口过小时上边框显示不完全的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31298" target="_blank">#31298</a></li> 
   <li>修复 Table <code>rowSelection</code> 的 <code>selectedRows</code> 属性在初始化时不同步问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31224" target="_blank">#31224</a></li> 
   <li>修复 Table 组合列上的筛选状态 <code>filteredValue</code> 不生效的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30815" target="_blank">#30815</a></li> 
  </ul> </li> 
 <li>Form 
  <ul> 
   <li>修复 Form 错误校验状态下 Input 的聚焦外框色。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31240" target="_blank">#31240</a></li> 
   <li>Form 增加 <code>name</code> 作为验证消息 <code>label</code> 的默认值。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30179" target="_blank">#30179</a></li> 
  </ul> </li> 
 <li>修复 Rate 在 Safari 下聚焦外框的样式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31241" target="_blank">#31241</a></li> 
 <li>微调 Select 箭头垂直位置。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31234" target="_blank">#31234</a></li> 
 <li>清除 Input 内容时不再触发 <code>onBlur</code>，修复可编辑表格 Input 无法正确清除内容的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31202" target="_blank">#31202</a></li> 
 <li>修复 Tooltip <code>arrowPointAtCenter</code> 有一像素偏移的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31201" target="_blank">#31201</a></li> 
 <li>修复 Menu 项 hover 文字色彩的渐变效果。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31189" target="_blank">#31189</a></li> 
 <li>修复 Dropdown.Button 不支持 <code>overlayClassName</code> 和 <code>overlayStyle</code> 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31187" target="_blank">#31187</a></li> 
 <li>使 Pagination 选中禁用状态的按钮样式与单选框相应按钮的样式一致。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31185" target="_blank">#31185</a></li> 
 <li>修复在 Windows 环境下打包组件样式导出文件时路径错误。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31277" target="_blank">#31277</a></li> 
 <li>en_GB 语言文件中增添 <code>selectNone</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31264" target="_blank">#31264</a></li> 
 <li>TypeScript 
  <ul> 
   <li>调整 Transfer <code>listStyle</code> 属性为可选属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31322" target="_blank">#3132</a></li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Freleases%2Ftag%2F4.16.7" target="_blank">https://github.com/ant-design/ant-design/releases/tag/4.16.7</a> </p>
                                        </div>
                                      
</div>
            