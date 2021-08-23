
---
title: '如何用Axure画出Web后台产品的菜单栏组件'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/9lu1WAkJci1f0a50R7Lt.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 25 Aug 2020 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/9lu1WAkJci1f0a50R7Lt.jpg'
---

<div>   
<blockquote><p>编辑导语：Web后台的菜单栏通常用来展示产品的整体功能导航，是最常用的Web组件之一，PM一定要了解并学会它的原型画法。本文仔细介绍了用Axure画出Web后台产品的菜单栏组件的步骤与注意要点，希望对你有所启发。</p></blockquote>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/9lu1WAkJci1f0a50R7Lt.jpg" width="900" height="420" referrerpolicy="no-referrer"></p>
<p>我们先来看下Web菜单栏的原型交互效果，详见下图或者访问原型<a title="https://kgnha1.axshare.com" href="https://kgnha1.axshare.com/#g=1" target="_blank" rel="noopener">https://kgnha1.axshare.com</a></p>
<p>由于菜单栏比较常用并且画起来比较麻烦，建议产品经理根据本文的原型步骤制作一份菜单栏rp源文件，方便后续多个项目使用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/VCA83AtG2l8wymCROZV6.gif" width="900" height="1080" referrerpolicy="no-referrer"></p>
<p>仔细查看上图原型，会发现包含以下这些交互用例，接下来作者会详细讲解每一步如何通过Axure RP 9画出来。</p>
<ol>
<li>默认展开左侧菜单的二级页面</li>
<li>处于某一页面的时候，对应菜单项都会处于选中状态并呈现不同的样式。</li>
<li>点击一级分类即可收起对应的二级页面，再次点击即可展开。</li>
<li>默认进入首页，同时首页对应的菜单处于选中状态。此时所有菜单处于展开状态。</li>
</ol>
<p>菜单栏通常有2级结构，第一级菜单是分类，第二级菜单是页面。一般位于页面左侧，并且是每个页面都有它。</p>
<h2 id="toc-1">01 画出无交互原型</h2>
<p><strong>1、先画首页文字。</strong>从默认元件库中拖动“矩形1”到工作区合适位置，修改尺寸为(160,40)，双击输入文字表示首页，字号修改为16px，左侧对齐然后左侧边距修改为40px。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/ys59NjLlCDRhLkH5ZJkN.png" width="900" height="1742" referrerpolicy="no-referrer"></p>
<p><strong>2、再画首页图标。</strong>从默认元件库中拖动“图片”到矩形中合适位置，尺寸修改为(20,20)，样式点击“调整颜色”图标，勾选调整颜色，饱和度拖动到最左边变成0。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/VXg8hJBLCZ0rZjPyoRKd.png" width="900" height="1566" referrerpolicy="no-referrer"></p>
<p><strong>3、再画首页文字的选中样式。</strong>右键点击交互样式，切换到选中状态，然后勾选字色然后输入蓝色#0000FF，点击“确定”按钮。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/XiWWYNSxKvwnI7ubfMzs.jpg" width="900" height="1444" referrerpolicy="no-referrer"></p>
<p><strong>4、再画首页图标的选中样式。</strong>右键点击交互样式，切换到选中状态，然后勾选图像滤波，点击“确定”按钮。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/HamqXjfn0Ep9bfWltmro.jpg" width="900" height="1436" referrerpolicy="no-referrer"></p>
<p><strong>5、再画一级分类。方法同上述4步。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/RwL2abSZoEvN07QD8Ld8.jpg" width="900" height="1421" referrerpolicy="no-referrer"></p>
<p><strong>6、再画二级页面。</strong>方法步骤同1和3，除了字号保持默认。根据需要复制多份二级页面。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/vzLlbzDPvDRiAkRk9lUT.jpg" width="900" height="1436" referrerpolicy="no-referrer"></p>
<p><strong>7、复制多份一级分类和二级页面。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/IaGybsuTXPfRVhbyc8y2.jpg" width="900" height="1436" referrerpolicy="no-referrer"></p>
<p><strong>8、在左侧页面区域，添加文件夹来作为一级分类</strong>，添加页面来作为二级页面。然后右键分类名称-重复-分支来快速复制。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/JLIYp5BglGrCeJt5pgzq.png" width="900" height="1430" referrerpolicy="no-referrer"></p>
<p><strong>9、同时选择所有的菜单栏元件和顶部导航组件</strong>，然后右键点击“转换为母版”，然后命名为“菜单栏”。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/01rnuyNtrQbDHrYn74QT.png" width="900" height="1410" referrerpolicy="no-referrer"></p>
<p><strong>10、在左侧母版区域，</strong>右键母版“菜单栏”，点击“添加到页面中…”然后点击“全选”，勾选“置于底层”，最后点击确定。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/yyfqT63gbNStaGxdvwEn.png" width="900" height="1738" referrerpolicy="no-referrer"></p>
<p><strong>11、生成原型HTML并查看原型效果。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/itJGnvpiUSTTdGm5BXr0.gif" width="900" height="1080" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">02 画出有交互原型</h2>
<p><strong>12、先画进入首页的交互。</strong>双击母版“菜单栏”进入，选择首页，右侧边栏切换到“交互”，点击“新建交互”按钮，选择触发事件“单击时”，添加动作“打开链接”，链接到“首页”，点击“确定”按钮。(需要提前选择首页文字&首页图标并右键设为组合并命名为首页)</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/mCPWMWnEl3Ltn7VtCUY6.png" width="900" height="1336" referrerpolicy="no-referrer"></p>
<p><strong>13、再画每个页面的交互</strong>。右侧边栏切换到“交互”，点击“新建交互”按钮，选择触发事件“单击时”，添加动作“打开链接”，链接到“对应的页面”，点击“确定”按钮。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/6DK2d7QiSWOz7onu2YGJ.png" width="900" height="1336" referrerpolicy="no-referrer"></p>
<p><strong>14、再画一级分类的交互。</strong>同时选择分类名称&分类图标并右键设为组合并命名为一级分类；同时选择多个页面名称并右键设为组合并命名为二级页面。</p>
<p>然后点击组合“一级分类”，右侧边栏切换到“交互”，点击“新建交互”按钮，选择触发事件“单击时”，添加动作“显示/隐藏”，目标选择组合“二级页面”，操作选择“切换”，点击更多选项然后设置“展开收起”，点击“确定”按钮。(同理设置其他一级分类的交互。注意组合需要单独命名，方便选择目标)</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/cv0gVzVHciyubozcMHoM.png" width="900" height="1354" referrerpolicy="no-referrer"></p>
<p><strong>15、设置首页载入的交互。</strong>进入页面“首页”，点击空白区域，右侧边栏切换到“交互”，点击“新建交互”按钮，选择触发事件“页面载入时”，添加动作“设置选中”，目标选择组合“首页”，点击“完成”按钮。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/Y4e0xTysDEF4jHrJUqvU.png" width="900" height="1354" referrerpolicy="no-referrer"></p>
<p><strong>16、设置页面载入的交互。进</strong>入页面“页面名称”，点击空白区域，右侧边栏切换到“交互”，点击“新建交互”按钮，选择触发事件“页面载入时”，添加动作“设置选中”，目标选择“页面名称”，点击“完成”按钮(注意需要提前命名页面名称来方便选择目标)</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/PsMiM6xxutT98pFtjPi4.png" width="900" height="1354" referrerpolicy="no-referrer"></p>
<p><strong>17、生成原型HTML并查看原型效果。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/lR8vV4fJlkuWpnM6PjOS.gif" width="900" height="1080" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">总结</h2>
<p>如果页面特别多，可以采用三级菜单栏，即第一级菜单是分类，第二级菜单是分类，第三级菜单是页面。</p>
<p>另外Axure左侧页面结构中也需要以相应的分类名称页面名称进行使用，方便开发和测试理解。</p>
<h3>#相关阅读#</h3>
<p><a href="http://www.woshipm.com/rp/4118409.html" target="_blank" rel="noopener">Axure教程：制作APP折叠面板</a></p>
<p><a href="http://www.woshipm.com/rp/783247.html" target="_blank" rel="noopener">APP下导航如何用Axure画出来</a></p>
<h3>#专栏作家#</h3>
<p>浪子，个人微信langzipm，公众号：浪子画原型(langzisay)。专注于Axure原型设计和产品规范。</p>
<p>本文由 @浪子 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4150962" data-author="91183" data-avatar="http://image.woshipm.com/wp-files/2020/08/sA8gybUl9UB6F3Qt0GDR.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            