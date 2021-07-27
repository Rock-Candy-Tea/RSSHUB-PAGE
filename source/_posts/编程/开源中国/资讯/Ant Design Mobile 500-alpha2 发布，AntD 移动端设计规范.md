
---
title: 'Ant Design Mobile 5.0.0-alpha.2 发布，AntD 移动端设计规范'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9439'
author: 开源中国
comments: false
date: Tue, 27 Jul 2021 07:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9439'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Ant Design Mobile 5.0.0-alpha.2 发布了。Ant Design Mobile 即 Ant Design 移动端设计规范，<code>antd-mobile</code> 是 Ant Design 的移动规范的 React 实现，服务于蚂蚁及口碑无线业务。</p> 
<p>更新内容如下：</p> 
<ul> 
 <li>特性 
  <ul> 
   <li>新增了 umd 构建产物</li> 
   <li>新增了 TextArea 组件</li> 
  </ul> </li> 
 <li>优化 
  <ul> 
   <li>包结构调整，<code>lib</code> 目录更名为 <code>cjs</code></li> 
   <li>重构了 Steps 组件，横向模式下也支持了 icon 属性</li> 
  </ul> </li> 
 <li>修复 
  <ul> 
   <li>修复了 Input 组件 placeholder 文字颜色过深的问题</li> 
  </ul> </li> 
</ul> 
<p><strong>迁移建议</strong></p> 
<ul> 
 <li>由于 <code>lib</code> 目录调整为了 <code>cjs</code> 目录，所以如果之前有引入过 <code>lib/index.css</code> 的话，需要替换为 <code>es/index.css</code> 或 <code>cjs/index.css</code></li> 
 <li>Steps 组件进行了重构，默认是只展示小圆点的，没有图标，如果需要展示图标的话需要手动传入</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Freleases%2Ftag%2Fv5.0.0-alpha.2" target="_blank">https://github.com/ant-design/ant-design-mobile/releases/tag/v5.0.0-alpha.2</a></p>
                                        </div>
                                      
</div>
            