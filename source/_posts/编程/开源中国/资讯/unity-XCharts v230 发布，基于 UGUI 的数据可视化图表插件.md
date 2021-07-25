
---
title: 'unity-XCharts v2.3.0 发布，基于 UGUI 的数据可视化图表插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=20'
author: 开源中国
comments: false
date: Sat, 24 Jul 2021 20:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=20'
---

<div>   
<div class="content">
                                                                                            <p>unity-XCharts v2.3.0 已经发布，基于 UGUI 的数据可视化图表插件。</p> 
<p>此版本更新内容包括：</p> 
<h3>版本要点</h3> 
<ul> 
 <li>数据存储由<code>float</code>升级为<code>double</code></li> 
 <li>新增<code>MarkLine</code>标线</li> 
 <li><code>Serie</code>下可用<code>IconStyle</code>统一配置图标</li> 
 <li><code>Label</code>支持用代码自定义显示样式</li> 
 <li><code>DataZoom</code>完善</li> 
 <li><code>PieChart</code>优化</li> 
 <li>问题修复</li> 
</ul> 
<h3>升级注意</h3> 
<p>由于数据类型升级为了<code>double</code>，<code>float</code>隐式转<code>double</code>可能有精度问题，所以建议之前为<code>float</code>的数据类型都手动改为<code>double</code>类型。</p> 
<h3>日志详情</h3> 
<ul> 
 <li>(2021.07.24) 发布<code>v2.3.0</code>版本</li> 
 <li>(2021.07.22) 完善<code>SerieSymbol</code>以支持象形柱图<code>PictorialBarChart</code>扩展</li> 
 <li>(2021.07.19) 修复<code>WdbGL</code>平台上<code>Tooltip</code>不显示的问题</li> 
 <li>(2021.07.18) 增加<code>Serie</code>的<code>iconStyle</code>统一配置图标</li> 
 <li>(2021.07.15) 增加<code>MarkLine</code>标线 (#142)</li> 
 <li>(2021.07.09) 优化<code>BarChart</code>可通过<code>serieData.show</code>设置是否显示柱条</li> 
 <li>(2021.07.08) 优化<code>data</code>数据存储类型由<code>float</code>全部转为<code>double</code></li> 
 <li>(2021.07.05) 修复<code>PieChart</code>的<code>avoidLabelOverlap</code>参数不生效的问题</li> 
 <li>(2021.07.04) 修复<code>PieChart</code>选中扇区后鼠标区域指示不准确的问题</li> 
 <li>(2021.07.04) 优化<code>PieChart</code>的<code>Label</code>为<code>Inside</code>时可通过参数<code>Margin</code>调节偏移</li> 
 <li>(2021.07.01) 增加<code>DataZoom</code>的<code>supportInsideScroll</code>和<code>supportInsideDrag</code>参数设置坐标系内是否支持滚动和拖拽</li> 
 <li>(2021.06.27) 增加<code>AxisLabel</code>的<code>showStartLabel</code>和<code>showEndLabel</code>参数设置首尾的<code>Label</code>是否显示</li> 
 <li>(2021.06.27) 增加<code>AxisLabel</code>和<code>SerieLabel</code>的<code>formatter</code>委托方法 (#145)</li> 
 <li>(2021.06.27) 增加<code>DataZoom</code>的<code>orient</code>参数设置水平或垂直样式</li> 
 <li>(2021.06.21) 增加<code>IconStyle</code>的<code>autoHideWhenLabelEmpty</code>参数设置当<code>label</code>为空时是否自动隐藏图标</li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/monitor1394/unity-ugui-XCharts/releases/v2.3.0">https://gitee.com/monitor1394/unity-ugui-XCharts/releases/v2.3.0</a></p>
                                        </div>
                                      
</div>
            