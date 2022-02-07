
---
title: 'ECharts_Vue--（插件）tooltip显示自动播放与列表无缝滚动'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/12013390-d141cac3aa7e29ba.gif'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/12013390-d141cac3aa7e29ba.gif'
---

<div>   
<blockquote>
<h4>记录一次大屏业务</h4>
<blockquote>
<p>本篇需要完成的内容：<br>
1、ECharts的 tooltip 显示自动播放<br>
2、Vue中使用 vue-seamless-scroll.js 做列表无缝滚动</p>
</blockquote>
</blockquote>
<h3>1. ECharts 的 tooltip 显示自动播放</h3>
<ul>
<li>
<p>效果</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="466" data-height="709"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-d141cac3aa7e29ba.gif" data-original-width="466" data-original-height="709" data-original-format="image/gif" data-original-filesize="127310" src="https://upload-images.jianshu.io/upload_images/12013390-d141cac3aa7e29ba.gif" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">tooltip 显示自动播放.gif</div>
</div>
</li>
<li>
<p>安装插件</p>
<ul>
<li><p>有插件用，自己就不写了，官网也是有方法的，插件做了封装</p></li>
<li><p>下载地址：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fliuyishiforever%2Fecharts-auto-tooltip" target="_blank">echarts-auto-tooltip.js</a></p></li>
<li><p>使用（直接复制插件官方的使用文档）：</p></li>
</ul>
<pre><code>1.引入ehcrts-auto-tooltips
<script type="text/javascript" src="js/echarts-auto-tooltip.js"></script>

2.在初始化 echarts 实例并通过 setOption 方法生成图表的代码下添加如下代码
myChart.setOption(option);
tools.loopShowTooltip(myChart, option, &#123;loopSeries: true&#125;); // 使用本插件
</code></pre>
<ul>
<li>
<p>参数：</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="938" data-height="353"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-e76b76112d7c163d.png" data-original-width="938" data-original-height="353" data-original-format="image/png" data-original-filesize="22299" src="https://upload-images.jianshu.io/upload_images/12013390-e76b76112d7c163d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">参数.png</div>
</div>
</li>
</ul>
</li>
</ul>
<h3>2. vue中实现列表无缝滚动</h3>
<ul>
<li>
<p>效果</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="444" data-height="357"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-f824864f2bdde3a7.gif" data-original-width="444" data-original-height="357" data-original-format="image/gif" data-original-filesize="377232" src="https://upload-images.jianshu.io/upload_images/12013390-f824864f2bdde3a7.gif" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">列表滚动.gif</div>
</div>
</li>
<li><p>地址及使用文档<br>
<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fchenxuan0000%2Fvue-seamless-scroll%2Fblob%2Fmaster%2Fdocument%2FREADME.md" target="_blank">中文文档</a></p></li>
<li><p>下载插件</p></li>
</ul>
<pre><code>npm install vue-seamless-scroll --save
</code></pre>
<ul>
<li>引入</li>
</ul>
<pre><code>// main.js
import scroll from 'vue-seamless-scroll'
Vue.use(scroll)
</code></pre>
<ul>
<li>
<p>页面中使用</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="865" data-height="424"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-0499dcffeaabdf1a.png" data-original-width="865" data-original-height="424" data-original-format="image/png" data-original-filesize="37390" src="https://upload-images.jianshu.io/upload_images/12013390-0499dcffeaabdf1a.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">html</div>
</div>
</li>
</ul>
<pre><code>// computed 中 参数配置
computed: &#123;
            classOption() &#123;
                return &#123;
                    step: 0.2, // 数值越大速度滚动越快
                    singleHeight: 26,
                    // isSingleRemUnit:true,
                    limitMoveNum: 2, // 开始无缝滚动的数据量 this.dataList.length
                    hoverStop: true, // 是否开启鼠标悬停stop
                    direction: 1, // 0向下 1向上 2向左 3向右
                    openWatch: true, // 开启数据实时监控刷新dom
                    singleHeight: 0, // 单步运动停止的高度(默认值0是无缝不停止的滚动) direction => 0/1
                    singleWidth: 0, // 单步运动停止的宽度(默认值0是无缝不停止的滚动) direction => 2/3
                    waitTime: 1000 // 单步运动停止的时间(默认值1000ms)
                &#125;
            &#125;
        &#125;,
</code></pre>
<ul>
<li>使用中的一些问题</li>
</ul>
<pre><code>> 问：列表滚动不连贯的问题，不是无缝的情况
> 答：给循环的内容加行高，如：给seamless-warp加行高
.seamless-warp &#123;
   width: 100%;
   height: calc(100% - 80px);
   line-height: 45px;
   overflow: hidden;
&#125;
</code></pre>
<h3>3. 结束</h3>
<blockquote>
<p>over!</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="267" data-height="268"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-5a36af65c9f3cc83.png" data-original-width="267" data-original-height="268" data-original-format="image/png" data-original-filesize="14722" src="https://upload-images.jianshu.io/upload_images/12013390-5a36af65c9f3cc83.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">点个赞呗！</div>
</div>
  
</div>
            