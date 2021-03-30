
---
title: 'React Native入门详解--基础组件的使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c2a467b74d14470b48fa949315e11a9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 30 Mar 2021 01:13:13 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c2a467b74d14470b48fa949315e11a9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文中会介绍一些RN中基础组件和这些组件常规的需求，该教程默认你具备一定的ReactJS使用经验。</p>
<h1 data-id="heading-0">RN常用组件</h1>
<h2 data-id="heading-1">1、View组件和组件的样式</h2>
<p>View是RN中最基础的组件，类似于html中的div标签，他可以作为组件的容器。</p>
<h3 data-id="heading-2">组件样式</h3>
<ul>
<li>大部分组件的样式通过组件的<strong>style</strong>属性来控制,<strong>style</strong>的值可以为数组也可以为对象</li>
<li>样式属性key要遵循小驼峰命名法</li>
<li>当<strong>style</strong>的值为<strong>对象</strong>时，对象的key为样式属性value则为样式的值；当<strong>style</strong>的值为<strong>数组</strong>时，<strong>数组</strong>的元素必须为<strong>对象</strong>，并且<strong>当数组中多个对象具有相同的样式属性时，后面对象的样式属性会覆盖前面对象的。</strong>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">import</span> &#123; View &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>
&#123;<span class="hljs-comment">/*style值为对象    生成一个宽为200dp，高为100dp背景色为粉色的View组件*/</span>&#125;
 <View style=&#123;&#123;<span class="hljs-attr">height</span>:<span class="hljs-number">100</span>,<span class="hljs-attr">width</span>:<span class="hljs-number">200</span>,<span class="hljs-attr">backgroundColor</span>:<span class="hljs-string">"pink"</span>&#125;&#125;><View>  
 
&#123;<span class="hljs-comment">/*style值为数组    生成一个宽为200dp，高为200dp背景色为红色的View组件*/</span>&#125;
 <View style=&#123;[
     &#123;<span class="hljs-attr">height</span>:<span class="hljs-number">100</span>,<span class="hljs-attr">width</span>:<span class="hljs-number">200</span>,<span class="hljs-attr">backgroundColor</span>:<span class="hljs-string">"pink"</span>&#125;，
     &#123;<span class="hljs-attr">height</span>:<span class="hljs-number">200</span>,<span class="hljs-attr">backgroundColor</span>:<span class="hljs-string">"red"</span>&#125;
 ]&#125;><View>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>某些具有多种特性 复杂样式的值必须为数组，如transform
<pre><code class="hljs language-js copyable" lang="js"><View style=&#123;&#123;
    <span class="hljs-attr">height</span>:<span class="hljs-number">100</span>,
    <span class="hljs-attr">width</span>:<span class="hljs-number">200</span>,
    <span class="hljs-attr">backgroundColor</span>:<span class="hljs-string">"pink"</span>,
    <span class="hljs-attr">transform</span>:[&#123;<span class="hljs-attr">translateX</span>:<span class="hljs-number">100</span>&#125;]
&#125;&#125;><View>  
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-3"><code>内联式样式</code></h4>
<p>如上，直接在style中书写样式对象就是内联式写法，这种适合样式少，样式简单的组件使用</p>
<h4 data-id="heading-4"><code>样式对象式样式</code></h4>
<ul>
<li>有些组件样式比较复杂如果写在jsx结构上，会让组件结构复杂增加阅读成本</li>
<li>某些样式是可以被其他组件复用不需要多次数书写。为了解决这些问题我们可以用样式对象式样式</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">&#123;<span class="hljs-comment">/*导入创建样式对象的 StyleSheet*/</span>&#125;
<span class="hljs-keyword">import</span> &#123; View,StyleSheet, &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>
<View style=&#123;styles.container&#125;>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;styles.content&#125;</span></<span class="hljs-attr">View</span>></span></span>
<View>
&#123;<span class="hljs-comment">/*创建样式对象*/</span>&#125;
<span class="hljs-keyword">const</span> styles = StyleSheet.create(&#123;
    <span class="hljs-attr">container</span>:&#123;
        <span class="hljs-attr">width</span>:<span class="hljs-number">100</span>,
        <span class="hljs-attr">height</span>:<span class="hljs-number">200</span>
    &#125;,
    <span class="hljs-attr">content</span>:&#123;
        <span class="hljs-attr">width</span>:<span class="hljs-number">50</span>,
        <span class="hljs-attr">height</span>:<span class="hljs-number">50</span>
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">组件布局</h3>
<p>RN有三种布局方式：常规的布局、Flex布局、定位布局</p>
<h4 data-id="heading-6"><code>Flex布局</code></h4>
<p>常规属性：<br>
<strong>flex</strong>：同css的flex属性用法类似<br>
<strong>flexDirection</strong>：RN没有display:flex用法，flexDirection就是将当前盒子设为伸缩盒子，并设置主轴方向</p>
<ul>
<li>值：<strong>row</strong> | <strong>column</strong> | <strong>row-reverse</strong> | <strong>column-reverse</strong></li>
</ul>
<p><strong>justifyContent</strong>：同css的flex属性用法类似<br>
<strong>alignItems</strong>：同css的flex属性用法类似
<strong>flexWrap</strong>：同css的flex属性用法类似<br>
<strong>alignSelf</strong>：<strong>flex-start</strong> | <strong>flex-end</strong> | <strong>center</strong></p>
<h4 data-id="heading-7"><code>定位布局</code></h4>
<p><strong>position</strong>：同css的position属性，但是没有fixed值</p>
<h2 data-id="heading-8">2、Text组件</h2>
<p>在RN的很多组件内没法直接显示文字内容，我们需要使用Text组件来显示文字</p>
<h3 data-id="heading-9"><code>组件常规属性</code></h3>
<p><strong>numberOfLines</strong>：文本行数限制，超出的内容以省略号形式显示<br>
<strong>ellipsizeMode</strong>：设置文本缩略格式，配合numberOfLines使用</p>
<ul>
<li>值：<strong>tail</strong>：在末尾...省略（默认值）| <strong>clip</strong>：在末尾切割，直接切割字符无省略符 | <strong>head</strong>：在前面...省略 | <strong>middle</strong>：在中间...省略</li>
</ul>
<p><strong>onPress</strong>：点击事件</p>
<h3 data-id="heading-10"><code>组件样式属性</code></h3>
<p><strong>color</strong>：字体颜色<br>
<strong>fontSize</strong>：字体大小<br>
<strong>fontFamily</strong>：字体<br>
<strong>fontStyle</strong>：字体样式（normal：正常italic：斜体）<br>
<strong>fontWeight</strong>：设置字体粗体（normal：正常bold：粗体100，200，300， 400， 500， 600， 700， 800， 900）<br>
<strong>lineHeight</strong>：行高<br>
<strong>textAlign</strong>：对齐方式（auto：自动对齐left：左对齐right：右对齐 center：居中对齐 justify:仅ios支持 两端对齐）
<strong>textDecorationLine</strong>：文字下划线和删除线样式（none：无线underline：下划线line-through：删除线 underline line-through：下划线和删除线）</p>
<h2 data-id="heading-11">3、Image组件</h2>
<h3 data-id="heading-12"><code>组件属性</code></h3>
<p><strong>source</strong>：图片的资源，使用本地图片时需要先将图片导入当前组件中然后绑定到source上；使用网络图片时，source需要绑定一个具有uri字段的对象 这个uri就是图片URL</p>
<h3 data-id="heading-13"><code>组件样式属性</code></h3>
<p><strong>resizeMode</strong>：图片显示模式</p>
<ul>
<li><strong>contain</strong>：保持宽高缩放图片，使图片的长边能完全显示出来</li>
<li><strong>cover</strong>：保持宽高缩放图片，使图片的短边能完全显示出来，裁剪长边</li>
<li><strong>stretch</strong>：图片将完全显示出来并拉伸变形铺满整个屏幕</li>
<li><strong>repeat</strong>：图片将重复并铺满屏幕（只支持ios）</li>
<li><strong>center</strong>：图片不拉伸不缩放且居中</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; Image &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>
&#123;<span class="hljs-comment">/* 本地图片 */</span>&#125;
<span class="hljs-keyword">const</span> img1 = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../asstes/img1.png"</span>)  
<Image source=&#123;img1&#125; />  
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Image</span> <span class="hljs-attr">source</span>=<span class="hljs-string">&#123;require(</span>"<span class="hljs-attr">..</span>/<span class="hljs-attr">asstes</span>/<span class="hljs-attr">img.png</span>")&#125; /></span></span>  
&#123;<span class="hljs-comment">/* 网络图片 */</span>&#125;
<Image source=&#123;&#123;uri：<span class="hljs-string">"http:ww......."</span>&#125;&#125; />
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">4、TouchAbleopacity组件</h2>
<p>某些组件没有点击相关的事件，我们可以将其嵌套TouchAbleopacity组件中使用点击等相关能力</p>
<h3 data-id="heading-15"><code>组件常规属性</code></h3>
<p><strong>activeOpacity</strong>：设置组件在进行触摸的时候，显示的不透明度（取值在0~1之间）<br>
<strong>onPress</strong>：触摸事件触发时执行的回调<br>
<strong>onPressIn</strong>：手指按下时触发的回调
<strong>onPressOut</strong>：手指松开时触发的回调</p>
<pre><code class="hljs language-js' copyable" lang="js'">function Home() &#123;
    const hPress = () => &#123;console.log("touch事件被触发了")&#125;
    return <TouchableOpacity activeOpacity=&#123;1&#125; onPress=&#123;hPress&#125;>
        <View style=&#123;&#123;width:100,height:200&#125;&#125;></View>  
    </TouchableOpacity>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">5、ScrollView组件</h2>
<p>如果你的页面需要滚动（不管是水平还是竖直方向），你都可以使用这个组件.<br>
ScrollView组件滚动有两个前提：</p>
<ul>
<li>它自身有一个固定的高度或宽度</li>
<li>它的内容高度或宽度 超过他自身的高度或宽度</li>
</ul>
<h3 data-id="heading-17"><code>组件常规属性</code></h3>
<p><strong>horizontal</strong>：控制滚动的方向（true：水平滚动，false：竖向滚动，默认是false）<br>
<strong>onScroll</strong>：滚动事件触发时的回调<br>
<strong>keyboardDismissMode</strong>：当拖拽滚动视图时，是否要隐藏软键盘</p>
<ul>
<li>none：（默认值），拖拽时不隐藏软键盘</li>
<li>on-drag：当拖拽开始的时候隐藏软键盘</li>
<li>interactive：（仅ios），软键盘伴随拖拽操作同步地消失,上滑动会恢复键盘</li>
</ul>
<p><strong>keyboardShouldPersistTaps</strong>：点击ScrollView是否收起软键盘，TextInput无法自动失去焦点/需点击多次才切换到其他组件原因就是没有TextInput放入ScrollView中。</p>
<h3 data-id="heading-18"><code>组件方法</code></h3>
<p><strong>scrollTo(x，y，naimate)</strong>：让ScrollView滚动到指定位置的方法，参数1：X轴坐标，参数2：Y轴坐标 参数3：滚动是否启用平滑动画<br>
<strong>scrollTo(&#123;x: 0, y: 0, animated: true&#125;)</strong><br>
注意：指定滚动持续时间的示例(仅限 Android):<br>
<strong>scrollTo(&#123;x: 0, y: 0, duration: 500&#125;)</strong></p>
<h3 data-id="heading-19"><code>实例</code></h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useEffect, useRef &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; View, Text, StyleSheet, ScrollView &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>
<span class="hljs-comment">// 引入适配工具</span>
<span class="hljs-keyword">import</span> pxTodp <span class="hljs-keyword">from</span> <span class="hljs-string">'../../utils/adaptive'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Home</span>(<span class="hljs-params">props</span>) </span>&#123;
 <span class="hljs-keyword">const</span> myScrollViewNode = useRef()
 useEffect(<span class="hljs-function">() =></span> &#123;
   <span class="hljs-comment">// 页面初始，让ScrollView滚动到 X:200 Y:0 的位置</span>
   myScrollViewNode.current.scrollTo(&#123; <span class="hljs-attr">x</span>: <span class="hljs-number">200</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">animated</span>: <span class="hljs-literal">true</span> &#125;)
 &#125;, [])
 <span class="hljs-keyword">const</span> dataList = [&#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"box1"</span> &#125;, &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"box2"</span> &#125;, &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"box3"</span> &#125;, &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"box4"</span> &#125;, &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"box5"</span> &#125;, &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"box6"</span> &#125;, &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"box7"</span> &#125;,]
 <span class="hljs-keyword">const</span> hScroll = <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
  <span class="hljs-comment">// 获取组件位置和尺寸</span>
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"获取组件位置和尺寸"</span>, e.nativeEvent);
 &#125;
 <span class="hljs-keyword">return</span> (
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">ScrollView</span> <span class="hljs-attr">horizontal</span>=<span class="hljs-string">&#123;true&#125;</span> <span class="hljs-attr">onScroll</span>=<span class="hljs-string">&#123;hScroll&#125;</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;myScrollViewNode&#125;</span>></span>
       &#123; dataList.map(e => &#123;
           return <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;e.text&#125;</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">backgroundColor:</span> '<span class="hljs-attr">pink</span>', <span class="hljs-attr">width:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">200</span>), <span class="hljs-attr">height:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">200</span>), <span class="hljs-attr">flexDirection:</span> "<span class="hljs-attr">row</span>", <span class="hljs-attr">justifyContent:</span> "<span class="hljs-attr">center</span>", <span class="hljs-attr">alignItems:</span> "<span class="hljs-attr">center</span>" &#125;&#125;></span>
             <span class="hljs-tag"><<span class="hljs-name">Text</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">height:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">100</span>), <span class="hljs-attr">width:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">100</span>), <span class="hljs-attr">textAlign:</span> "<span class="hljs-attr">center</span>", <span class="hljs-attr">lineHeight:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">100</span>), <span class="hljs-attr">backgroundColor:</span> "<span class="hljs-attr">powderblue</span>" &#125;&#125;></span>&#123;e.text&#125;<span class="hljs-tag"></<span class="hljs-name">Text</span>></span>
           <span class="hljs-tag"></<span class="hljs-name">View</span>></span>
         &#125;)&#125;
     <span class="hljs-tag"></<span class="hljs-name">ScrollView</span>></span>
   <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
 )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="微信截图_20210330101717.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c2a467b74d14470b48fa949315e11a9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-20">6、TextInput组件</h2>
<h3 data-id="heading-21"><code>组件常规属性</code></h3>
<p><strong>placeholder</strong>：输入框的占位符<br>
<strong>placeholderTextColor</strong>：占位字符串显示的文字颜色
<strong>autoFocus</strong>：是否在componentDidMount后会获得焦点，默认false
<strong>multiline</strong>：文本框中可以输入多行文字。默认值为 false。
<strong>value</strong>：输入框的显示内容<br>
<strong>onChangeText</strong>：输入框内容被改变时触发的回调</p>
<h3 data-id="heading-22"><code>组件样式属性</code></h3>
<p><strong>paddingVertical</strong>：去除内边距，在安卓中，你可能会出现TextInput占位符显示不全的问题，可以通过 <strong>paddingVertical:0</strong> 解决这个问题</p>
<h3 data-id="heading-23"><code>数据双向绑定示例</code></h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; View, Text, TextInput &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>
<span class="hljs-comment">// 引入适配工具</span>
<span class="hljs-keyword">import</span> pxTodp <span class="hljs-keyword">from</span> <span class="hljs-string">'../../utils/adaptive'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Home</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">const</span> [state, setState] = useState(&#123; <span class="hljs-attr">value</span>: <span class="hljs-string">"11"</span> &#125;)
  <span class="hljs-keyword">const</span> hChangeText = <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-comment">// 获取输入框最新数据 并更新state.value</span>
    setState(<span class="hljs-function"><span class="hljs-params">oldState</span> =></span> (&#123; ...oldState, <span class="hljs-attr">value</span>: e &#125;))
  &#125;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">height:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">400</span>), <span class="hljs-attr">marginTop:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">100</span>), <span class="hljs-attr">backgroundColor:</span> "<span class="hljs-attr">pink</span>" &#125;&#125; ></span>
      <span class="hljs-tag"><<span class="hljs-name">Text</span>></span>TextInput组件：<span class="hljs-tag"></<span class="hljs-name">Text</span>></span>
      &#123;/* 将state.value绑定到 TextInput组件上 */&#125;
      <span class="hljs-tag"><<span class="hljs-name">TextInput</span> <span class="hljs-attr">onChangeText</span>=<span class="hljs-string">&#123;hChangeText&#125;</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;state.value&#125;</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"这是占位符"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">backgroundColor:</span> "<span class="hljs-attr">powderblue</span>" &#125;&#125;></span><span class="hljs-tag"></<span class="hljs-name">TextInput</span>></span>
    </View >
  )
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-24">7、StatusBar组件</h2>
<p>它是控制应用状态栏的组件，他可以在任何视图加载，当有多个状态栏组件时，后加载的会覆盖前面的这点 在使用导航器的时候需要注意。</p>
<h3 data-id="heading-25"><code>组件常规属性</code></h3>
<p><strong>animated</strong>：状态栏的某些属性变化时，是否以动画形式呈现默认为false，目前支持的属性：backgroundColor, barStyle 和 hidden。<br>
<strong>translucent</strong>：状态栏背景是否透明，默认false（仅安卓）<br>
<strong>backgroundColor</strong>：状态栏背景色（仅安卓）<br>
<strong>barStyle</strong>：状态栏文本颜色：default | light-content | dark-content<br>
<strong>hidden</strong>：是否显示状态栏，默认false</p>
<h2 data-id="heading-26">8、Animated组件</h2>
<p>Animated组件对安卓和ios动画的封装，通过统一的接口为RN提供了的动画的功能</p>
<h3 data-id="heading-27">值类型</h3>
<ul>
<li><strong>Animated.Value()</strong> 用于单个值</li>
<li><strong>Animated.ValueXY()</strong> 用于矢量值</li>
</ul>
<p><strong>AnimatedValue.setValue（newValue）</strong>：在不触发动画的情况下修改动画的值</p>
<h3 data-id="heading-28">配置动画</h3>
<p>RN提供了三种类型动画，并对其进行配置</p>
<ul>
<li><strong>Animated.decay(value, config)</strong>：以指定的初始速度开始变化，然后变化速度越来越慢直至停下</li>
<li><strong>Animated.spring(value，config)</strong>：提供了一个基础的弹簧物理模型</li>
<li><strong>Animated.timing(value，config)</strong>：使用easing 函数让数值随时间动起来。它默认使用对称的easeInOut 曲线，将对象逐渐加速到全速，然后通过逐渐减速停止结束。
<ul>
<li><strong>value</strong>：需要被更改的动画值</li>
<li><strong>config</strong>：动画配置对象
<ul>
<li><strong>duration</strong>：动画的持续时间（毫秒）。默认值为 500</li>
<li><strong>easing</strong>：缓动函数。 默认为Easing.inOut(Easing.ease)。</li>
<li><strong>delay</strong>: 开始动画前的延迟时间（毫秒）。默认为 0.</li>
<li><strong>isInteraction</strong>：指定本动画是否在InteractionManager的队列中注册以影响其任务调度。默       认值为 true。</li>
<li><strong>useNativeDriver</strong>: 启用原生动画驱动。默认不启用(false)。</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>大部分业务场景用 <strong>Animated.timing()</strong> 就足够了，这里重点介绍一下它。</p>
<h3 data-id="heading-29">执行动画</h3>
<p><strong>Animated.timing().start()</strong><br>
配置动画完成后，调用start方法就会执行这个动画，start可以传入一个回调函数，当动画结束后会执行这个回调，同时向这个回调传入动画执行的状态&#123;finished：false | true&#125;</p>
<pre><code class="hljs language-js copyable" lang="js">Animated.timing(&#123;&#125;).start(<span class="hljs-function">(<span class="hljs-params">&#123; finished &#125;</span>) =></span> &#123;
  <span class="hljs-comment">/* 动画完成的回调函数 */</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">动画组件</h3>
<p>在RN中，组件必须通过特殊处理才能使用动画。Animated提供了几个可以直接使用的组件：<strong>Animated.Image</strong>、<strong>Animated.ScrollView</strong>、<strong>Animated.Text</strong>、<strong>Animated.View</strong><br>
如果内置的动画组件无法满足你，你可用通过 <strong>createAnimatedComponent()</strong> 自己封装动画组件</p>
<h3 data-id="heading-31"><code>示例1</code></h3>
<p>这个一个简单的动画示例，会将组件通过scale属性实现组件从小到大的动画。点击红色按钮开始执行动画，点击绿色按钮将组件恢复到动画之前的状态。</p>
<p><img alt="500x698_1617092231341.gif" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a484c3bf27e5408e87e4739850512657~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useEffect, useRef &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; View, Text, Animated &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>
<span class="hljs-comment">// 引入适配工具</span>
<span class="hljs-keyword">import</span> pxTodp <span class="hljs-keyword">from</span> <span class="hljs-string">'../../utils/adaptive'</span>;
<span class="hljs-keyword">let</span> scaleAnimate = <span class="hljs-keyword">new</span> Animated.Value(<span class="hljs-number">0</span>)
<span class="hljs-keyword">const</span> handleAnimate = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 点击粉色按钮配置动画，并执行它</span>
  Animated.timing(scaleAnimate, &#123; <span class="hljs-attr">duration</span>: <span class="hljs-number">1000</span>, <span class="hljs-attr">toValue</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">useNativeDriver</span>: <span class="hljs-literal">false</span> &#125;).start()
&#125;
<span class="hljs-keyword">const</span> resetAnimate = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 将动画值设置为0</span>
  scaleAnimate.setValue(<span class="hljs-number">0</span>)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Home</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">backgroundColor:</span> "<span class="hljs-attr">gray</span>", <span class="hljs-attr">flex:</span> <span class="hljs-attr">1</span> &#125;&#125;></span>
      <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">width:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">540</span>), <span class="hljs-attr">height:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">540</span>), <span class="hljs-attr">backgroundColor:</span> "<span class="hljs-attr">white</span>", <span class="hljs-attr">flexDirection:</span> "<span class="hljs-attr">row</span>", <span class="hljs-attr">justifyContent:</span> "<span class="hljs-attr">center</span>", <span class="hljs-attr">alignItems:</span> "<span class="hljs-attr">center</span>" &#125;&#125;></span>
        <span class="hljs-tag"><<span class="hljs-name">Animated.View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">width:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">200</span>), <span class="hljs-attr">height:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">200</span>), <span class="hljs-attr">backgroundColor:</span> "<span class="hljs-attr">pink</span>", <span class="hljs-attr">transform:</span> [&#123; <span class="hljs-attr">scale:</span> <span class="hljs-attr">scaleAnimate</span> &#125;] &#125;&#125;></span><span class="hljs-tag"></<span class="hljs-name">Animated.View</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">View</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">marginTop:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">50</span>), <span class="hljs-attr">flexDirection:</span> "<span class="hljs-attr">row</span>", <span class="hljs-attr">justifyContent:</span> "<span class="hljs-attr">space-between</span>", <span class="hljs-attr">paddingLeft:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">60</span>), <span class="hljs-attr">paddingRight:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">60</span>) &#125;&#125;></span>
        <span class="hljs-tag"><<span class="hljs-name">Text</span> <span class="hljs-attr">onPress</span>=<span class="hljs-string">&#123;handleAnimate&#125;</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">backgroundColor:</span> "<span class="hljs-attr">pink</span>", <span class="hljs-attr">color:</span> "<span class="hljs-attr">white</span>", <span class="hljs-attr">borderRadius:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">10</span>), <span class="hljs-attr">width:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">120</span>), <span class="hljs-attr">height:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">50</span>), <span class="hljs-attr">lineHeight:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">50</span>), <span class="hljs-attr">textAlign:</span> "<span class="hljs-attr">center</span>" &#125;&#125;></span>执行动画<span class="hljs-tag"></<span class="hljs-name">Text</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Text</span> <span class="hljs-attr">onPress</span>=<span class="hljs-string">&#123;resetAnimate&#125;</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">backgroundColor:</span> "<span class="hljs-attr">green</span>", <span class="hljs-attr">color:</span> "<span class="hljs-attr">white</span>", <span class="hljs-attr">borderRadius:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">10</span>), <span class="hljs-attr">width:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">120</span>), <span class="hljs-attr">height:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">50</span>), <span class="hljs-attr">lineHeight:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">50</span>), <span class="hljs-attr">textAlign:</span> "<span class="hljs-attr">center</span>" &#125;&#125;></span>重置动画<span class="hljs-tag"></<span class="hljs-name">Text</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">View</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
  )
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">差值</h3>
<p>有些动画效果无法通过纯数字来实现，例如颜色的渐变，0deg-180deg角度的变化，你可以通过差值来实现。
它是指将一定范围的输入值映射到另一组不同的输出值，一般我们使用线性的映射，但是也可以使用 easing 函数<br>
<strong>AnimateValue.interpolate(&#123; inputRange: [0,1], outputRange: [0,300]&#125;)</strong></p>
<ul>
<li>inputRange：输入值的区间</li>
<li>inputRange：输出值的区间</li>
</ul>
<p><strong>AnimateValue.interpolate(&#123; inputRange: [0,1], outputRange: ["rgba(0,0,0,.1)","rgba(255,255,255,1)"]&#125;)</strong><br>
<strong>AnimateValue.interpolate(&#123; inputRange: [0,1], outputRange: ["0deg","300deg"]&#125;)</strong><br>
<code>interpolate()还支持定义多个区间段落，常用来定义静止区间</code><br>
AnimateValue.interpolate(&#123;
inputRange: [-300, -100, 0, 100, 101],
outputRange: [300, 0, 1, 0, 0]
&#125;);<br>
这样当AnimateValue=-400时输出值为450；当AnimateValue=-300时输出值为300；当AnimateValue=0时输出值为1；当AnimateValue=100时输出值为0；当AnimateValue大于100时输出值为0；</p>
<h3 data-id="heading-33"><code>示例</code></h3>
<p>基于缩放的动画值，创建颜色渐变和旋转角度的差值<br>
<img alt="530x675_1617095036210.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b070c5f430748acbc87eb5662867b13~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useEffect, useRef &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; View, Text, StyleSheet, ScrollView, Animated &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>
<span class="hljs-comment">// 引入适配工具</span>
<span class="hljs-keyword">import</span> pxTodp <span class="hljs-keyword">from</span> <span class="hljs-string">'../../utils/adaptive'</span>;
<span class="hljs-keyword">let</span> scaleAnimate = <span class="hljs-keyword">new</span> Animated.Value(<span class="hljs-number">0</span>)
<span class="hljs-comment">// 颜色渐变差值映射动画</span>
<span class="hljs-keyword">let</span> colorAnimate = scaleAnimate.interpolate(&#123;
  <span class="hljs-attr">inputRange</span>: [<span class="hljs-number">0</span>, <span class="hljs-number">1.5</span>],
  <span class="hljs-attr">outputRange</span>: [<span class="hljs-string">"green"</span>, <span class="hljs-string">"red"</span>]
&#125;)
<span class="hljs-comment">// 旋转角度差值映射动画</span>
<span class="hljs-keyword">let</span> rotateAnimate = scaleAnimate.interpolate(&#123;
  <span class="hljs-attr">inputRange</span>: [<span class="hljs-number">0</span>, <span class="hljs-number">1.5</span>],
  <span class="hljs-attr">outputRange</span>: [<span class="hljs-string">"0deg"</span>, <span class="hljs-string">"360deg"</span>]
&#125;)
<span class="hljs-keyword">const</span> handleAnimate = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 点击粉色按钮配置动画，并执行它</span>
  Animated.timing(scaleAnimate, &#123; <span class="hljs-attr">duration</span>: <span class="hljs-number">3000</span>, <span class="hljs-attr">toValue</span>: <span class="hljs-number">1.5</span>, <span class="hljs-attr">useNativeDriver</span>: <span class="hljs-literal">false</span> &#125;).start()
&#125;
<span class="hljs-keyword">const</span> resetAnimate = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 将动画值设置为0</span>
  scaleAnimate.setValue(<span class="hljs-number">0</span>)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Home</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">backgroundColor:</span> "<span class="hljs-attr">gray</span>", <span class="hljs-attr">flex:</span> <span class="hljs-attr">1</span> &#125;&#125;></span>
      <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">width:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">540</span>), <span class="hljs-attr">height:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">540</span>), <span class="hljs-attr">backgroundColor:</span> "<span class="hljs-attr">white</span>", <span class="hljs-attr">flexDirection:</span> "<span class="hljs-attr">row</span>", <span class="hljs-attr">justifyContent:</span> "<span class="hljs-attr">center</span>", <span class="hljs-attr">alignItems:</span> "<span class="hljs-attr">center</span>" &#125;&#125;></span>
        <span class="hljs-tag"><<span class="hljs-name">Animated.View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">width:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">200</span>), <span class="hljs-attr">height:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">200</span>), <span class="hljs-attr">backgroundColor:</span> <span class="hljs-attr">colorAnimate</span>, <span class="hljs-attr">transform:</span> [&#123; <span class="hljs-attr">scale:</span> <span class="hljs-attr">scaleAnimate</span>, &#125;, &#123; <span class="hljs-attr">rotate:</span> <span class="hljs-attr">rotateAnimate</span> &#125;] &#125;&#125;></span><span class="hljs-tag"></<span class="hljs-name">Animated.View</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">View</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">marginTop:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">50</span>), <span class="hljs-attr">flexDirection:</span> "<span class="hljs-attr">row</span>", <span class="hljs-attr">justifyContent:</span> "<span class="hljs-attr">space-between</span>", <span class="hljs-attr">paddingLeft:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">60</span>), <span class="hljs-attr">paddingRight:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">60</span>) &#125;&#125;></span>
        <span class="hljs-tag"><<span class="hljs-name">Text</span> <span class="hljs-attr">onPress</span>=<span class="hljs-string">&#123;handleAnimate&#125;</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">backgroundColor:</span> "<span class="hljs-attr">pink</span>", <span class="hljs-attr">color:</span> "<span class="hljs-attr">white</span>", <span class="hljs-attr">borderRadius:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">10</span>), <span class="hljs-attr">width:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">120</span>), <span class="hljs-attr">height:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">50</span>), <span class="hljs-attr">lineHeight:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">50</span>), <span class="hljs-attr">textAlign:</span> "<span class="hljs-attr">center</span>" &#125;&#125;></span>执行动画<span class="hljs-tag"></<span class="hljs-name">Text</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Text</span> <span class="hljs-attr">onPress</span>=<span class="hljs-string">&#123;resetAnimate&#125;</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">backgroundColor:</span> "<span class="hljs-attr">green</span>", <span class="hljs-attr">color:</span> "<span class="hljs-attr">white</span>", <span class="hljs-attr">borderRadius:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">10</span>), <span class="hljs-attr">width:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">120</span>), <span class="hljs-attr">height:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">50</span>), <span class="hljs-attr">lineHeight:</span> <span class="hljs-attr">pxTodp</span>(<span class="hljs-attr">50</span>), <span class="hljs-attr">textAlign:</span> "<span class="hljs-attr">center</span>" &#125;&#125;></span>重置动画<span class="hljs-tag"></<span class="hljs-name">Text</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">View</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-34">最后</h2>
<p>相信大家的RN搭建过程可能会不太顺利，如果有需要帮助或者技术上交流的同猿欢迎加  V: <strong>gg_0632</strong></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            