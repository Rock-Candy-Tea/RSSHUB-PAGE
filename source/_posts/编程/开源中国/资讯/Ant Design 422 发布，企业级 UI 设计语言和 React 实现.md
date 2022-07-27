
---
title: 'Ant Design 4.22 发布，企业级 UI 设计语言和 React 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1088'
author: 开源中国
comments: false
date: Wed, 27 Jul 2022 07:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1088'
---

<div>   
<div class="content">
                                                                                            <p>Ant Design 4.22 现已发布，主要变化如下：</p> 
<ul> 
 <li>Form 
  <ul> 
   <li>Form 新增 <code>Form.Item.useStatus</code> 用于获取 Form.Item 的校验状态。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36486" target="_blank">#36486</a></li> 
   <li>Form 支持 <code>setFieldValue</code> 以简化设置数字单个值的操作流程。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36058" target="_blank">#36058</a></li> 
   <li>修复 Form.Item 在快速切换校验状态时高度抖动的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36575" target="_blank">#36575</a></li> 
  </ul> </li> 
 <li>Radio.Group 支持 <code>onBlur</code> 和 <code>onFocus</code> 属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36041" target="_blank">#36041</a></li> 
 <li>Typography <code>ellipsis.tooltip</code> 属性支持传入一个对象。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36099" target="_blank">#36099</a></li> 
 <li>重构 Drawer 移除直接的 dom 操作以使其更符合 React 运作方式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36672" target="_blank">#36672</a></li> 
 <li>重构 Sketelon.Button square shape 样式为宽高相等，之前的 square 改为默认样式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36123" target="_blank">#36123</a></li> 
 <li>修复 Modal.confirm 中 <code>onCancel(close)</code> 参数有时候不是 function 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36600" target="_blank">#36600</a></li> 
 <li>回滚 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36439" target="_blank">#36439</a> 以修复上传和删除文件时状态不对的问题，并再次修复 Upload 移除文件时状态色会变化的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36706" target="_blank">#36706</a></li> 
 <li>Tree 
  <ul> 
   <li>Tree/TreeSelect <code>switcherIcon</code> 参数现在支持完整 TreeNode 属性，从 <code>&#123; expanded: boolean &#125;</code> 变为 <code>AntTreeNodeProps</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36651" target="_blank">#36651</a></li> 
   <li>修改 Tree <code>draggable</code> 函数的参数类型由 AntTreeNode 改为 DataNode。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36648" target="_blank">#36648</a></li> 
  </ul> </li> 
 <li>Table 
  <ul> 
   <li>修复 Table 固定列额外阴影和滚动条样式的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36606" target="_blank">#36606</a></li> 
   <li>修复 Table 树形数据固定列的省略样式错位的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36608" target="_blank">#36608</a></li> 
  </ul> </li> 
 <li>国际化 
  <ul> 
   <li>添加斯里兰卡语言。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F36149" target="_blank">#36149</a></li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Freleases%2Ftag%2F4.22.0" target="_blank">https://github.com/ant-design/ant-design/releases/tag/4.22.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            