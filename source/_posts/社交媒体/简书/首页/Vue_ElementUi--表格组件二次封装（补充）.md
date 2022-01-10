
---
title: 'Vue_ElementUi--表格组件二次封装（补充）'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/12013390-dcaba04af98df5c7.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/12013390-dcaba04af98df5c7.png'
---

<div>   
<blockquote>
<h4>关于表格组件其它的事件与方法,关于小伙伴的回复</h4>
<blockquote>
<ul>
<li>其实在上篇中，该有的都有了，方法与事件的添加使用都是大同小异，在一个项目中是不可能全部用到的。</li>
<li>上篇中的内容应该阔以解决 <code>68.66375%</code> 的需求，我的本意是保持一定的扩展性，在不同的项目中添加不同的需求,纯全通用的话，太臃肿了一些。</li>
<li>本篇主要解决内容：</li>
</ul>
<blockquote>
<p>1.个别方法添加使用<br>
2.字体颜色判断<br>
3.临时补充，想到什么补什么</p>
</blockquote>
</blockquote>
</blockquote>
<h3>0. 其它</h3>
<p><a href="https://www.jianshu.com/p/c45681796059" target="_blank">上篇链接：Vue/ElementUi--表格组件二次封装</a><br>
<a href="https://links.jianshu.com/go?to=www.lxhblog.cn" target="_blank">链接：小伙伴封装的表格表单图表</a></p>
<h3>1. 再看官方文档</h3>
<ul>
<li><a href="https://links.jianshu.com/go?to=https%3A%2F%2Felement.eleme.cn%2F%23%2Fzh-CN%2Fcomponent%2Ftable" target="_blank">table官方链接</a></li>
<li>官方文档还是挺详细的，但是很少有人能把每一个属性、每一个方法都记下来的，可能大多数小伙伴都跟我一样，有需要的时候才去文档中查找；</li>
<li>这次呢我也是真的认真的看了 <code>81.0786%</code>，稍微整理了一下，都输错好几遍……肯定也不会每一个都搞一遍……</li>
</ul>
<table>
<thead>
<tr>
<th style="text-align:center">/</th>
<th style="text-align:center">类型</th>
<th style="text-align:center">数量</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">Table Attributes</td>
<td style="text-align:center">表格属性</td>
<td style="text-align:center">33</td>
</tr>
<tr>
<td style="text-align:center">Table Events</td>
<td style="text-align:center">表格事件</td>
<td style="text-align:center">17</td>
</tr>
<tr>
<td style="text-align:center">Table Methods</td>
<td style="text-align:center">表格方法</td>
<td style="text-align:center">9</td>
</tr>
<tr>
<td style="text-align:center">Table Slot</td>
<td style="text-align:center">表格插槽</td>
<td style="text-align:center">1</td>
</tr>
<tr>
<td style="text-align:center">Table-column Attributes</td>
<td style="text-align:center">表列属性</td>
<td style="text-align:center">27</td>
</tr>
<tr>
<td style="text-align:center">Table-column Scoped Slot</td>
<td style="text-align:center">表列作用域插槽</td>
<td style="text-align:center">2</td>
</tr>
</tbody>
</table>
<ul>
<li>想想这么多的属性事件方法全部做到一起，额，还是算了~</li>
</ul>
<h3>2. <code>Table Attributes</code>（表格属性）、<code>Table Events</code>（表格事件）、<code>Table Methods</code>（表格方法）的使用</h3>
<ul>
<li>关于父子组件怎么传值就不说了，基于上篇组件，在 props 中添加即可</li>
<li>使用一般加在 <code><el-table></el-table></code> 标签里面，属性动态绑定或者直接加上 <code>: 属性 = “ 属性名 ”</code>，事件或者方法 <code>@ 事件方法 = “ 事件方法名 ”</code><br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1066" data-height="391"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-dcaba04af98df5c7.png" data-original-width="1066" data-original-height="391" data-original-format="image/png" data-original-filesize="32571" src="https://upload-images.jianshu.io/upload_images/12013390-dcaba04af98df5c7.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">表格.png</div>
</div>
</li>
</ul>
<h3>3. <code>Table-column Attributes</code>（表列属性）的使用</h3>
<ul>
<li>需要传值同样在 <code>props</code> 中添加</li>
<li>使用一般加在<code><el-table-column></el-table-column></code>标签中，动态绑定即可<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1040" data-height="270"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-7ffb7bf9e0b6ec50.png" data-original-width="1040" data-original-height="270" data-original-format="image/png" data-original-filesize="33916" src="https://upload-images.jianshu.io/upload_images/12013390-7ffb7bf9e0b6ec50.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">列表.png</div>
</div>
</li>
</ul>
<h3>4. 本地排序</h3>
<ul>
<li>
<p>添加</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="619" data-height="275"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-47004990fcd20d1d.png" data-original-width="619" data-original-height="275" data-original-format="image/png" data-original-filesize="12896" src="https://upload-images.jianshu.io/upload_images/12013390-47004990fcd20d1d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">属性添加.png</div>
</div>
</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="676" data-height="219"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-39c37754ccecb834.png" data-original-width="676" data-original-height="219" data-original-format="image/png" data-original-filesize="12262" src="https://upload-images.jianshu.io/upload_images/12013390-39c37754ccecb834.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">组件中使用.png</div>
</div>
<ul>
<li>
<p>效果</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="495" data-height="294"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-f602d6efb01d5697.gif" data-original-width="495" data-original-height="294" data-original-format="image/gif" data-original-filesize="68617" src="https://upload-images.jianshu.io/upload_images/12013390-f602d6efb01d5697.gif" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">本地排序.gif</div>
</div>
</li>
</ul>
<h3>5. 筛选</h3>
<ul>
<li>
<p>组件中添加 <code>filters</code> 与 <code>filter-method</code>，动态绑定<br>
</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="875" data-height="411"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-647b769dcfbec416.png" data-original-width="875" data-original-height="411" data-original-format="image/png" data-original-filesize="22472" src="https://upload-images.jianshu.io/upload_images/12013390-647b769dcfbec416.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">添加.png</div>
</div>
<p></p>
</li>
<li>
<p>组件<code>props</code> 中加入 <code>filterMethod</code><br>
</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="414" data-height="89"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-906f3b571047036e.png" data-original-width="414" data-original-height="89" data-original-format="image/png" data-original-filesize="4371" src="https://upload-images.jianshu.io/upload_images/12013390-906f3b571047036e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">添加方法.png</div>
</div>
<p></p>
</li>
<li>
<p>模块中使用（直接上图，就少写字描述了，步骤就是图片描述）</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1019" data-height="124"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-b8be3ca8b55add05.png" data-original-width="1019" data-original-height="124" data-original-format="image/png" data-original-filesize="12134" src="https://upload-images.jianshu.io/upload_images/12013390-b8be3ca8b55add05.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">第一步：组件中绑定.png</div>
</div>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="454" data-height="215"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-49c5d47abf2e1e92.png" data-original-width="454" data-original-height="215" data-original-format="image/png" data-original-filesize="8971" src="https://upload-images.jianshu.io/upload_images/12013390-49c5d47abf2e1e92.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">第二步：methods中写方法.png</div>
</div>
</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="942" data-height="379"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-d921eeb384d831c4.png" data-original-width="942" data-original-height="379" data-original-format="image/png" data-original-filesize="29397" src="https://upload-images.jianshu.io/upload_images/12013390-d921eeb384d831c4.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">第三步：数据绑定.png</div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="565" data-height="180"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-94ee5c04f2cbb058.png" data-original-width="565" data-original-height="180" data-original-format="image/png" data-original-filesize="7868" src="https://upload-images.jianshu.io/upload_images/12013390-94ee5c04f2cbb058.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">异步数据赋值.png</div>
</div>
<ul>
<li>
<p>效果</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1323" data-height="384"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-7197fa3c35e37006.gif" data-original-width="1323" data-original-height="384" data-original-format="image/gif" data-original-filesize="89815" src="https://upload-images.jianshu.io/upload_images/12013390-7197fa3c35e37006.gif" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">筛选.gif</div>
</div>
</li>
</ul>
<h3>6. 表格字体变色</h3>
<ul>
<li>
<p>组件中添加，这个也比较简单，直接上图</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="651" data-height="349"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-38aee951c1fe161d.png" data-original-width="651" data-original-height="349" data-original-format="image/png" data-original-filesize="17117" src="https://upload-images.jianshu.io/upload_images/12013390-38aee951c1fe161d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">第一步：添加绑定.png</div>
</div>
</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="463" data-height="107"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-7c666e9a55f1546e.png" data-original-width="463" data-original-height="107" data-original-format="image/png" data-original-filesize="3227" src="https://upload-images.jianshu.io/upload_images/12013390-7c666e9a55f1546e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">第二步：props中添加.png</div>
</div>
<ul>
<li>
<p>模块中使用</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1047" data-height="138"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-efff716615facab7.png" data-original-width="1047" data-original-height="138" data-original-format="image/png" data-original-filesize="13544" src="https://upload-images.jianshu.io/upload_images/12013390-efff716615facab7.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">绑定.png</div>
</div>
</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="841" data-height="445"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-8857df74dc235ff4.png" data-original-width="841" data-original-height="445" data-original-format="image/png" data-original-filesize="22854" src="https://upload-images.jianshu.io/upload_images/12013390-8857df74dc235ff4.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">判断与返回结果.png</div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="869" data-height="283"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-9664852399c16ce0.png" data-original-width="869" data-original-height="283" data-original-format="image/png" data-original-filesize="15109" src="https://upload-images.jianshu.io/upload_images/12013390-9664852399c16ce0.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">判读.png</div>
</div>
<ul>
<li>效果，只要判断条件不同，返回的颜色自然不同，只要有需求还可以搞成七彩的 <code>๑乛◡乛๑</code>。<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1237" data-height="309"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-c34ba50f1d4ecec5.png" data-original-width="1237" data-original-height="309" data-original-format="image/png" data-original-filesize="23726" src="https://upload-images.jianshu.io/upload_images/12013390-c34ba50f1d4ecec5.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">效果.png</div>
</div>
</li>
</ul>
<h3>7. 结束</h3>
<blockquote>
<ul>
<li>方法太多了，个人也不是很想把他们全部集成到一起，不是不能是不想，根据每个项目需求来添加更加的灵活。</li>
<li>当然目前这些都是比较简单的东西，关于复杂表头啊，跨分页过滤啊等等吧，挺复杂的，我也还要再学习一下的。</li>
<li>最近事也比较多，闹心的居多，所以整理基本都是截图图，详细的描述较少，有时间再补了。</li>
</ul>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="267" data-height="268"><img data-original-src="//upload-images.jianshu.io/upload_images/12013390-5a36af65c9f3cc83.png" data-original-width="267" data-original-height="268" data-original-format="image/png" data-original-filesize="14722" src="https://upload-images.jianshu.io/upload_images/12013390-5a36af65c9f3cc83.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">点个赞呗！</div>
</div>
  
</div>
            