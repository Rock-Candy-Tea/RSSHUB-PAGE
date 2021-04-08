
---
title: '谈_ 移动端适配Rem到底是怎么回事_'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3712'
author: 掘金
comments: false
date: Wed, 07 Apr 2021 19:22:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=3712'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>最近几年都是基于PC在开发,突然要搞移动端有点不适应,主要还是处理各终端的适配.我们通常开发的页面在PC浏览器上显示正常,但是如果放在窄屏设备(移动设备)上,会在比屏幕宽的虚拟窗口或者视口中呈现页面,以便让用户可以一次性看到所有内容,用户可以通过平移缩放查看不同区域,这是没有进行移动优化的页面,它的体验是很不好的,或者说看起来很差.</p>
<p>后来,使用<code>媒体查询</code>,进行一些优化.但仍然存在问题,比如无法或者说很难做到更细的窗口变化体验.只能是一个区间来控制.</p>
<h2 data-id="heading-1">meta和viewport</h2>
<p>简单的说<code>viewport</code>就是浏览器的窗口宽度高度.但是在移动端就变得复杂了,移动端的viewport宽度高度都变小,做布局需要用到两个<code>viewport</code>: <code>viewportvisualviewport</code>(虚拟的viewport)和<code>viewportlayoutviewport</code>(布局的viewport).</p>
<p>我们在针对移动设备优化的网站需要有以下内容:</p>
<pre><code class="copyable"><meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的<code>width与height</code>来控制视口的大小.可以将它设置为特定的像素(例如<code>width = 666</code>).这边设置为<code>device-width(也有device-height)</code>,表示CSS像素的屏幕宽度,缩放比例为100%.<code>initial-scale</code>控制页面首次加载是的缩放级别,<code>maximum-scale，minimum-scale和user-scalable</code>属性控制用户如何/是否允许缩放页面。</p>
<p>比如我们平时开发UI给的设计图一般按照iphone6的尺寸也就是 375.这时候我们可以设置<code>width=375, initial-scale=1</code>.这样子可以精确的适应这个尺寸的设备.但是如果有其他的尺寸的话,就会出现问题...<a href="https://experienceleague.adobe.com/docs/target/using/experiences/vec/mobile-viewports.html?lang=en#task_B4B161499DC0470584ED922A4D20FCAB" target="_blank" rel="nofollow noopener noreferrer">这里是各种设备的尺寸参考</a></p>
<h2 data-id="heading-2">rem or em</h2>
<p><code>em</code>是一个长度单位.表示相对于父级文本的字体尺寸.如果父级字体没有设置尺寸,那就相对于浏览器默认尺寸<code>font-size: 16px</code>.<code>它的值不是固定的,可以继承父级字体尺寸</code>.</p>
<p><strong>元素的width/height/line-height/padding/margin用em为单位都是是相对于该元素的font-size</strong></p>
<pre><code class="copyable">.div1 &#123;font-size: 16px;&#125;
.div2 &#123;font-size: 2em;height: 2em;&#125;
.div3 &#123;font-size: 2em;&#125;

<div class="div1">   // font-size: 16px;
    <div class="div2">1</div> // font-size: 32px;height: 64px;
    <div class="div3">1</div> // font-size: 32px;
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>rem</code>是css3的相对单位.它设置的字体元素相对的是HTML根元素.也就是说我们设置html页面跟元素的<code>font-size</code>, 那项目里的其他节点使用<code>rem</code>这个单位去换算,都会依照这个根元素的值.</p>
<p><strong>其实它就是基于宽度的等比缩放.比如我们将屏幕平分100份,那我们如果知道屏幕宽度,然后去换算出来1份的宽度.然后我们开发中每次设置元素的大小都基于这个比例,那我们只需要关注屏幕宽度就可以了.换句话说,我们通过js去拿到屏幕宽度,然后去换算出每一份的值, 把这个值作为根节点的<code>font-size</code>,不就解决问题了.</strong></p>
<p><strong>实际的是,浏览器字体最小是<code>12px</code>, 如果100份,那换算出来只有个位数大小.浏览器不支持了,我们一般都换算10份.</strong></p>
<p>这里还涉及一个概念,就是<code>设备像素比(device pixel ratio)</code>,它是用<code>物理像素/设备独立像素得到的</code>.在Javascript中可以通过<code>window.devicePixelRatio</code>获取当前设备的dpr.我们可以通过dpr<code>设置body的font-size来支持项目中的字体适配em这个单位.</code></p>
<pre><code class="copyable">css:
html &#123;
    font-size: 37.5px; /* 375/10 */
&#125;
body &#123;
    font-size: 24px; /* 12 * dpr 修正字体大小 */
    width: 10rem;
&#125;
.p1 &#123;
    width: 5rem;
    height: 5rem;
    font-size: 1.2em; /* 字体使用em */
&#125;
html:
...

<body>
    <div class="p1">
        <div class="s1"></div>
    </div>
</body>
...
js:
var doc = document.documentElement;

function callback() &#123;
    var rem = docEl.clientWidth / 10
    docEl.style.fontSize = rem + 'px'
    if (document.body) &#123;
      // 设置全局body为当前dpr * 12px
      document.body.style.fontSize = (12 * dpr) + 'px'
    &#125;
&#125;

document.addEventListener('DOMContentLoaded', callback);
window.addEventListener('resize', callback)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子可以使用<code>rem</code>做移动端优化,但是字体使用的是<code>em</code>.原因就是<strong>设置根节点字体大小,会影响所以字体大小,字体大小会继承.总不能每个字体都设置字体大小...还有就是大屏用户可以选择要更大的字体还是更多的内容,如果使用rem,那就限制了用户的选择</strong>.所以在开发中,图片盒子宽度这些使用<code>rem</code>, 字体大小使用<code>em</code>.</p>
<h2 data-id="heading-3">vue项目如何使用</h2>
<p>在vue项目中其实有比较成熟的方案了.<code>lib-flexible</code>与<code>Postcss(pxtorem)</code>.前者所做的事情就是去获取屏幕并换算出合适的根<code>font-size</code>值,后者顾名思义,就是把<code>px</code>转为<code>rem</code>,方便我们在项目中可以放心使用<code>px</code>这个单位开发.这里是源码位置:<a href="https://github.com/amfe/lib-flexible" target="_blank" rel="nofollow noopener noreferrer">lib-flexible</a>,<a href="https://github.com/cuth/postcss-pxtorem" target="_blank" rel="nofollow noopener noreferrer">Postcss(pxtorem)</a></p>
<p>使用起来很简单只需要:</p>
<pre><code class="copyable">npm i amfe-flexible --save-dev
npm i postcss postcss-pxtorem --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在项目中分别引入:</p>
<pre><code class="copyable">main.js

import "amfe-flexible";

vue.config.js
css: &#123;
    loaderOptions: &#123;
      postcss: &#123;
        plugins: [
          require("postcss-pxtorem")(&#123;
            rootValue: 37.5,
            propList: ["*"], //作用于哪些标签
          &#125;)
        ]
      &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就可以了.至于<code>amfe-flexible</code>与<code>pxtorem</code>具体原理,可以去看源码.下面贴一部分<code>amfe-flexible</code>的代码,其实很简单:</p>
<pre><code class="copyable">  var docEl = document.documentElement
  var dpr = window.devicePixelRatio || 1

  // adjust body font size
  function setBodyFontSize () &#123;
    if (document.body) &#123;
      // 设置全局body为当前dpr * 12px
      document.body.style.fontSize = (12 * dpr) + 'px'
    &#125;
    else &#123;
      document.addEventListener('DOMContentLoaded', setBodyFontSize)
    &#125;
  &#125;
  setBodyFontSize();

  // set 1rem = viewWidth / 10
  function setRemUnit () &#123;
    var rem = docEl.clientWidth / 10
    docEl.style.fontSize = rem + 'px'
  &#125;

  setRemUnit()

  // reset rem unit on page resize
  window.addEventListener('resize', setRemUnit)
  window.addEventListener('pageshow', function (e) &#123;
    if (e.persisted) &#123;
      setRemUnit()
    &#125;
  &#125;)
  
  if (dpr >= 2) &#123;
    var fakeBody = document.createElement('body')
    var testElement = document.createElement('div')
    testElement.style.border = '.5px solid transparent'
    fakeBody.appendChild(testElement)
    docEl.appendChild(fakeBody)
    if (testElement.offsetHeight === 1) &#123;
      docEl.classList.add('hairlines')
    &#125;
    docEl.removeChild(fakeBody)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于<code>setBodyFontSize</code>这个方法,<a href="https://github.com/amfe/lib-flexible/issues/163" target="_blank" rel="nofollow noopener noreferrer">官方的解释在这里</a>.,个人觉得用来设置字体的单位<code>em</code>倒是也可以.</p>
<p><code>pxtorem</code>作为一个plugin,可想而知它做的事情就是基于webpack而完成的,对代码解析,然后把项目开发时的<code>px</code>转换为<code>rem</code>.</p>
<h1 data-id="heading-4">总结</h1>
<p>一个项目做完,总得有所收获.移动端适配也算是web开发的一个经典难题,从开始到解决这个过程也是挺艰辛的,而我们现在能站在巨人的肩膀上去做事,能做的就是了解这个历程,这样能让我们有很多收获与新的感悟.</p>
<p>尽管目前来说<code>flexible</code>不更新维护了,这边的目的在于搞清楚它到底做了什么.毕竟现在浏览器对<code>rem</code>是挺友好的.等后续<code>vw/vh</code>可以完美支持了,可以修改方案.</p>
<p>加油.</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            