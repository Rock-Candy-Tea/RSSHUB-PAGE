
---
title: 'ECharts 5.1.0 发布，JS 实现的交互式图表可视化库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4312'
author: 开源中国
comments: false
date: Tue, 20 Apr 2021 07:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4312'
---

<div>   
<div class="content">
                                                                    
                                                        <p>ECharts 是一个使用 JavaScript 实现的开源可视化库，可以流畅的运行在 PC 和移动设备上，兼容当前绝大部分浏览器（IE8/9/10/11，Chrome，Firefox，Safari等），底层依赖矢量图形库 ZRender，提供直观，交互丰富，可高度个性化定制的数据可视化图表。</p> 
<p>ECharts 5.1.0 正式发布，本次更新内容如下：</p> 
<ul> 
 <li>地理组件和地图系列支持 SVG 格式来源 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14571" target="_blank">#14571</a></li> 
 <li>默认图例设计更直观  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14497" target="_blank">#14497</a></li> 
 <li>添加捷克语翻译 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14468" target="_blank">#14468</a></li> 
 <li>在调整大小中添加动画配置 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14553" target="_blank">#14553</a></li> 
 <li>为 effectScatter 添加 clip <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14574" target="_blank">#14574</a></li> 
 <li>优化缺少组件或系列时的错误日志 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14568" target="_blank">#14568</a></li> 
 <li>提高工具提示的性能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14246" target="_blank">#14246</a></li> 
 <li>修正标签可能有错误的 <code>z</code>，以及不在前面的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14542" target="_blank">#14542</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14417" target="_blank">#14417</a></li> 
 <li>修正 <code>CanvasPatttern#setTransform</code> 可能不存在的错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fecomfe%2Fzrender%2Fissues%2F738" target="_blank">#738</a></li> 
 <li>修正使用时间轴时格式错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14471" target="_blank">#14471</a></li> 
 <li>使 <code>symbolOffset</code> 在所有使用符号的组件上使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14375" target="_blank">#14375</a></li> 
 <li>修正 markArea 背景颜色消失的 bug</li> 
 <li>修正字符串类型数据在 markLine 中可能无法使用的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14300" target="_blank">#14300</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14314" target="_blank">#14314</a></li> 
 <li>修正检查选中状态时的空访问错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14293" target="_blank">#14293</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14413" target="_blank">#14413</a></li> 
 <li>修复 dataZoom 设置无效果 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14388" target="_blank">#14388</a></li> 
 <li>修正动画之间NaN值可能存在的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fecomfe%2Fzrender%2Fissues%2F730" target="_blank">#730</a></li> 
 <li>使用 itemSymbol 作为默认符号类型 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F5719" target="_blank">#5719</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14243" target="_blank">#14243</a></li> 
 <li>修正加载的文字不在前面，被其他元素覆盖的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14191" target="_blank">#14191</a></li> 
 <li>修正自定义系列上的系列标签不能正常使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14092" target="_blank">#14092</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14254" target="_blank">#14254</a></li> 
 <li>修正地图标签在使用 labelLayout 时不会更新位置 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14578" target="_blank">#14578</a></li> 
 <li>修正日标漂移的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F11508" target="_blank">#11508</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F13902" target="_blank">#13902</a></li> 
 <li>修正线条动画可能会有多余的点，以及混乱的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F13638" target="_blank">#13638</a></li> 
 <li>在扩展中导出更多必要的类型以生成声明 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14289" target="_blank">#14289</a></li> 
 <li>增加 LegendComponentOption.icon 属性类型 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14263" target="_blank">#14263</a></li> 
 <li>删除遗留的转换用法 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F14357" target="_blank">#14357</a></li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Freleases%2Ftag%2F5.1.0" target="_blank">https://github.com/apache/echarts/releases/tag/5.1.0</a></p>
                                        </div>
                                      
</div>
            