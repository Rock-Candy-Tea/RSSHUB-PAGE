
---
title: 'Soul匹配筛选功能产品原型设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/t0SuXWq3xvUWvDHeM5WE.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 02 Jul 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/t0SuXWq3xvUWvDHeM5WE.jpg'
---

<div>   
<blockquote><p>编辑导语：Soul 的匹配筛选功能是其自身的亮点之一，本文作者关于这个功能制作了一份原型图，一起来看看吧。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-4796278" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/t0SuXWq3xvUWvDHeM5WE.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>修订记录：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/Rxy8JklbTxZRpF8MeCrG.png" alt width="403" height="85" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、 前言</h2>
<h3>1.1 需求背景</h3>
<p>匹配环节是陌生人社交行为链的开始，良好的匹配体验（效率、匹配机制等）可以提升用户在匹配环节的体验，为后续用户的互动破冰、建立关系打下良好基础。</p>
<p>通过对Soul进行竞品分析，找到了产品在匹配环节的改进方向。把进一步优化匹配功能及体验，降低无效匹配提升匹配效率，更好地沉淀用户关系作为产品迭代目标。</p>
<h3>1.2 项目目标</h3>
<ol>
<li>通过匹配时增加匹配对象筛选选项设置、自主选择恋爱铃开启关闭时间等提升匹配时的用户自主性，降低无效匹配。</li>
<li>通过载入时特权卡优惠弹出和匹配前特权卡使用确认，提升特权卡使用率及匹配时的用户体验，实现后续更有效的社交。</li>
</ol>
<h2 id="toc-2">二、功能概述</h2>
<h3>2.1 产品功能描述</h3>
<p>多样化的匹配方式满足用户多社交场景下的使用需求，完善匹配功能，从而更好地提升匹配效率以及用户体验，增强用户粘性，为后续社交环节做铺垫，沉淀用户关系。</p>
<h3>2.2 匹配功能结构图</h3>
<p>（注：红色部分为新增功能）</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/7hgjTUsMAApFdeTpUGqa.png" alt width="701" height="396" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、特性</h2>
<h3>3.1 需求列表</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/w3a61xLIu0pWQgsxGDzx.png" alt width="501" height="456" referrerpolicy="no-referrer"></p>
<h3>3.2 筛选</h3>
<ul>
<li>功能简介</li>
</ul>
<p>在筛选页面可以对恋爱对象进行年龄、距离、星球、星座设置。通过增加筛选选项，实现用户的自主个性化选择，减少无效匹配，提升用户体验。</p>
<ul>
<li>功能原型与主逻辑</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/X02b4em0dU84qYb0SYRo.png" alt width="298" height="607" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/BVG2ZohEUbNP3baQYuvd.png" alt width="301" height="736" referrerpolicy="no-referrer"></p>
<p>主逻辑：</p>
<ol>
<li>点击星球页筛选按钮，发现筛选页面想上弹出，至于顶层；</li>
<li>默认性别筛选为异性；页面年龄、距离筛选默认为最大范围，自动扩大搜索距离开启；期待星球为系统匹配；星座速配为今日最配；</li>
<li>点击切换选项，单选，无法取消选中。左右滑动设置匹配对象年龄及距离范围；</li>
<li>上下滑动显示更多筛选信息；</li>
<li>点击“×”后执行系统默认筛选设置，从搜索页面退回星球页；点击“√”后执行设定后的筛选设置，从搜索页面退回星球页。</li>
</ol>
<h3>3.3 恋爱铃设置</h3>
<ul>
<li>功能简介</li>
</ul>
<p>新增对恋爱铃的开启时段、铃声是否震动等进行编辑设置的功能。通过增加恋爱铃设置功能，能够让用户合理选择规划恋爱铃开启时间，避免打扰用户正常生活工作，提升用户体验。</p>
<ul>
<li>功能原型与主逻辑</li>
</ul>
<p>a）恋爱铃开启关闭</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/nK1V9IJBeY6ZIA7DJL8v.png" alt width="799" height="343" referrerpolicy="no-referrer"></p>
<p>主逻辑</p>
<ol>
<li>点击星球页恋爱铃按钮，恋爱零开启，星球页显示心形；</li>
<li>点击心形显示关闭恋爱铃选项。点击后弹出关闭提示；</li>
<li>点击关闭提示弹窗中的确认关闭后恋爱铃关闭，页面恢复初始星球页。点击保持开启，恋爱铃继续保持开启。</li>
</ol>
<p>b）编辑恋爱铃</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/W8B7OHo7xeofIdSI7LVJ.png" alt width="798" height="441" referrerpolicy="no-referrer"></p>
<p>主逻辑：</p>
<ol>
<li>点击心形按钮，弹出恋爱铃设置选项，点击后恋爱铃设置页面向上弹出，至于顶层。点击空白区域或进行任意操作后将收起；</li>
<li>恋爱铃设置页面默认全天开启，自定义时间开启后，全天开启关闭。 左滑某一自定义恋爱铃显示删除按钮，点击新建按钮新建自定义恋爱铃；</li>
<li>点击某一恋爱铃后显示编辑恋爱铃页面。 页面包含恋爱铃起止时间设置、一周开启时间选择、名称、铃声、是否震动设置以及删除当前恋爱铃按钮；</li>
<li> 重复默认为不选择，点击切换选项，单选，可取消选中；</li>
<li>点击“×”后设置不更改，返回恋爱铃 设置页；点击“√”后执行设定后的设置，返回恋爱铃设置页。</li>
</ol>
<h3>3.4 特权卡设置</h3>
<ul>
<li>功能简介</li>
</ul>
<p>星球页载入时弹出特权卡优惠信息提示弹窗，显示优惠信息，通过弹窗提示提升特权卡使用及购买率。</p>
<ul>
<li>功能原型与主逻辑</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/eSPcnv7pktVZsp483nV1.png" alt width="300" height="612" referrerpolicy="no-referrer"></p>
<p>主逻辑</p>
<ol>
<li>星球页面载入时，弹出特权卡优惠信息提示弹窗。显示匹配福袋优惠信息以及Soul币充值抵扣优惠；</li>
<li>点击“灵魂更好地遇见”按钮页面跳转至匹配福袋特惠页面，点击“立即使用”页面跳转至Soul币充值页面。点击关闭按钮关闭优惠提示。</li>
</ol>
<h2 id="toc-4">四、数据统计需求</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/kyepT6BMXAuP0ks4c0cA.png" alt width="601" height="769" referrerpolicy="no-referrer"></p>
<p> </p>
<p>本文由@Danning 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4790375" data-author="1139897" data-avatar="https://static.woshipm.com/APP_U_202012_20201230163248_3111.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            