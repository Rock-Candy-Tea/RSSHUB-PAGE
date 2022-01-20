
---
title: 'Ant Design 4.18.4 发布，企业级 UI 设计语言和 React 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1014'
author: 开源中国
comments: false
date: Thu, 20 Jan 2022 07:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1014'
---

<div>   
<div class="content">
                                                                                            <p>Ant Design 4.18.4 现已发布，主要变化如下：</p> 
<ul> 
 <li>Typography 
  <ul> 
   <li>优化 Typography 在配置 <code>tooltip</code> 时优先使用原生省略样式以提升性能。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33669" target="_blank">#33669</a></li> 
   <li>重构 Typography <code>ellipsis</code> 逻辑以修复 <code>children</code> 如果消费上游 Context 会报错的问题。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33725" target="_blank">#33725</a></li> 
  </ul> </li> 
 <li>Icon 
  <ul> 
   <li>修复 <code><Icon component=&#123;HomeOutlined&#125; /></code> 和 <code><HomeOutlined /></code> 不对齐的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33709" target="_blank">#33709</a></li> 
   <li>修复 <code><Icon component=&#123;SyncOutlined&#125; spin /></code> 抖动的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33726" target="_blank">#33726</a></li> 
  </ul> </li> 
 <li>Input 
  <ul> 
   <li>修复 Input 相关组件设置 <code>hidden</code> 时的展示问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33735" target="_blank">#33735</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33706" target="_blank">#33706</a></li> 
   <li>修复 Input 传入 <code>showCount</code> 时控制台 warning 问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33686" target="_blank">#33686</a></li> 
  </ul> </li> 
 <li>修复 ConfigProvider 和 Anchor 的渲染函数多次运行的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33723" target="_blank">#33723</a></li> 
 <li>修复 Cascader 组件中出现重复 key 的控制台 warning 问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33649" target="_blank">#33649</a></li> 
 <li>Checkbox.Group 的 <code>options</code> 支持数组中直接传入 number 和 boolean 类型。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33678" target="_blank">#33678</a></li> 
 <li>修复 Form <code>validateMessages</code> 在多个 ConfigProvider 内错乱的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33705" target="_blank">#33705</a></li> 
 <li>修复 Steps 组件在 <code>type</code> 为 navigation 和 <code>labelPlacement</code> 为 vertical 时，tail 部分不会显示的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33716" target="_blank">#33716</a></li> 
 <li>修复 Image 底部留白问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33631" target="_blank">#33631</a></li> 
 <li>修复 TreeSelect 键盘操作时，激活项不会高亮的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33755" target="_blank">#33755</a></li> 
 <li>修正高棉语 (km_KH) 语言包中部分翻译。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F33738" target="_blank">#33738</a></li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Freleases%2Ftag%2F4.18.4" target="_blank">https://github.com/ant-design/ant-design/releases/tag/4.18.4</a></p>
                                        </div>
                                      
</div>
            