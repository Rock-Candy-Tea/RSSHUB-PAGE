
---
title: 'layui 2.6.0 发布，传统 UI 框架表示还想冒个泡'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4982'
author: 开源中国
comments: false
date: Thu, 01 Apr 2021 04:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4982'
---

<div>   
<div class="content">
                                                                    
                                                        <blockquote> 
 <p>久违了，伙计们。上一次在 OSC 冒泡是在 2018年8月30号，我再看了看今天的日历：2021年4月1号？所以这消失的中间，顺着模糊的记忆碎片，我一度怀疑我穿越了，似乎进入了另一个不得了的平行空间，后又受量子纠缠的作用，我又被召唤回了本空间。记忆无法在不同的平行空间共存，从 2018 到 2021，我同时经历了两种记忆，一种不属于当前空间的记忆已被删除，而保留下来的记忆总感觉难以衔接，譬如我仍然记得 OSC 上面的<span style="color:#2ecc71">那抹绿</span>，就一个穿越的来回，它居然变得好看了？</p> 
</blockquote> 
<p>在 <span style="color:#16a085">Vue.js</span> 遍地生根的今天，一大批优秀的现代 UI 组件库闯进了你的「戎码」生活，而像 layui 这样的传统系列，已不断被扔入时代的废纸篓。拥抱更美好的技术方案，正与开发者的特质所匹配。所以 layui 那近乎停更的两年，有来自客观规律的必然，也有带着主观上的使然。毕竟，<span style="color:#e67e22">枫叶</span>并不属于春天，<span style="color:#2ecc71">花红柳绿才是春的主旋律</span>。然而前面提到，我毕竟是穿越来的，穿越的事物通常是可以<span style="color:#2ecc71">原谅的</span>，姑且就<span style="color:#1abc9c">容我踏着春风，再度启航</span>。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.layui.com%2Fdoc%2Fbase%2Fchangelog.html" target="_blank"><span style="color:#999999">更新内容</span></a></p> 
<h4>v2.6.0</h4> 
<ul> 
 <li><span style="color:#7f8c8d">[调整] 核心模块的聚合，统一构建为 layui.js，这意味着不必再按需异步加载模块，直接就可以使用 layui 所提供的所有组件库。该调整向下兼容，对早前版本的写法不受影响。但需要注意的是：1. 如果之前引入了 layui.all.js 的，现在必须改成 layui.js；2. 如果元素存在动态插入，那么您需要执行元素所对应组件的 render() 方法，如 form.render()。</span></li> 
 <li><span style="color:#7f8c8d">[新增] 基础菜单（layui-menu）样式结构，可无限层级嵌套</span></li> 
 <li><span style="color:#7f8c8d">[新增] 通用 dropdown 下拉菜单组件</span> 
  <ul> 
   <li><span style="color:#7f8c8d">亦可作为「右键菜单组件」使用</span></li> 
   <li><span style="color:#7f8c8d">[支持] 无限层级嵌套</span></li> 
   <li><span style="color:#7f8c8d">[支持] 子级菜单的横和竖两种展示方式</span></li> 
   <li><span style="color:#7f8c8d">[支持] 局部或全局的自定义菜单列表模板，可给菜单列表添加任意元素（图片、图标等）</span></li> 
   <li><span style="color:#7f8c8d">[支持] 自定义事件，可通过 click、hover、contextmenu（鼠标右键）等等方式调出组件面板</span></li> 
   <li><span style="color:#7f8c8d">[支持] className、style 属性，用于对组件的样式重置</span></li> 
  </ul> </li> 
 <li><span style="color:#7f8c8d">[新增] 常规面板（layui-panel）样式结构</span></li> 
 <li><span style="color:#7f8c8d">[优化] layer 组件的核心代码，当初始执行弹窗时，不必再套一层 layer.ready() 了</span></li> 
 <li><span style="color:#7f8c8d">[优化] layer 组件局部样式，以更贴近简约和百搭</span></li> 
 <li><span style="color:#7f8c8d">[优化] layDate 组件的日期范围选择，不再是之前一样左右联动的操作方式，而是左右保持完全独立的选择</span></li> 
 <li><span style="color:#7f8c8d">[优化] layDate 组件局部样式，及剔除多余 js 代码</span></li> 
 <li><span style="color:#7f8c8d">[修复] layDate 组件中当设为年/月选择器时，点击选择年/月数值时，面板未自动关闭的问题</span></li> 
 <li><span style="color:#7f8c8d">[修复] layDate 组件当 lang 设置为 'en' 时，部分提示内容未显示英文的问题</span></li> 
 <li><span style="color:#7f8c8d">[新增] table 组件的 table.getData(id) 方法，用于获取表格当前页的所有行数据（现在不必再通过 table.cache 获取）</span></li> 
 <li><span style="color:#7f8c8d">[修复] table 组件的 table.reload() 重载方法在多次执行时，会携带上一次执行时的参数的重大 BUG</span></li> 
 <li><span style="color:#7f8c8d">[新增] util 组件的 unescape(str) 方法，用于将转义后的 HTML 还原</span></li> 
 <li><span style="color:#7f8c8d">[优化] code 组件整体样式</span></li> 
 <li><span style="color:#7f8c8d">[优化] 整体边框/背景等色调，以及边距尺寸，以使得视觉搭配更加和谐自然</span></li> 
 <li><span style="color:#7f8c8d">[优化] 按钮部分样式细节，以及新增对边框按钮各种色系的更好支持</span></li> 
 <li><span style="color:#7f8c8d">[优化] hr 横线样式，以防止某些情况出现边框模糊的问题</span></li> 
 <li><span style="color:#7f8c8d">[新增] 新增 CSS3 从顶部往下滑入、微微往下滑入、平滑放小、弹簧式放小四种动画，并优化部分过度动画</span></li> 
 <li><span style="color:#7f8c8d">[新增] layui-font-样式，可定义常见字体大小和颜色</span></li> 
</ul> 
<h4>v2.6.1</h4> 
<ul> 
 <li><span style="color:#7f8c8d">[加强] table 组件的 table.reload(id, options, deep) 方法，可通过 deep参数控制是否采用深度重载（即参数深度克隆，也就是重载时始终携带初始时及上一次重载时的参数），默认浅重载</span></li> 
 <li><span style="color:#7f8c8d">[新增] table 组件加载失败时的 error 回调</span></li> 
 <li><span style="color:#7f8c8d">[优化] table 组件的 render 和 reload 方法，执行时保留 table.set() 设定的全局参数（同名参数覆盖）</span></li> 
 <li><span style="color:#7f8c8d">[优化] 按钮的尺寸，纯背景色按钮与带边框的按钮，在同等字符长度下尺寸相同</span></li> 
 <li><span style="color:#7f8c8d">[优化] 时间线只有一条数据时仍然显示线的问题，并优化其他细节</span></li> 
 <li><span style="color:#7f8c8d">[优化] 管理系统大布局样式，滚动条采用 body 默认，而非之前的 layui-body 所在的元素</span></li> 
</ul> 
<blockquote> 
 <p><span style="color:#1abc9c">若有不适，请轻喷</span></p> 
</blockquote>
                                        </div>
                                      
</div>
            