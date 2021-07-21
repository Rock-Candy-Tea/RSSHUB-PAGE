
---
title: '49 个在工作中常用且容易遗忘的 CSS 样式清单整理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e70588e0872e4dbdac9c54be7d6d6a7b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 20 Jul 2021 18:57:26 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e70588e0872e4dbdac9c54be7d6d6a7b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>喜欢的点赞收藏</code>，关注我不定时分享更多精彩内容。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e70588e0872e4dbdac9c54be7d6d6a7b~tplv-k3u1fbpfcp-watermark.image" alt="微信图片_20210715100908.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>来源：Web前端开发</p>
<h3 data-id="heading-0"><strong>1、文字超出部分显示省略号</strong></h3>
<p>单行文本的溢出显示省略号（一定要有宽度）</p>
<pre><code class="copyable">p&#123;
    width:200rpx;
    overflow: hidden;
    text-overflow:ellipsis;
    white-space: nowrap;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>多行文本溢出显示省略号</p>
<pre><code class="copyable">p &#123;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    overflow: hidden;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1"><strong>2、中英文自动换行</strong></h3>
<p>word-break:break-all;只对英文起作用，以字母作为换行依据word-wrap:break-word; 只对英文起作用，以单词作为换行依据white-space:pre-wrap; 只对中文起作用，强制换行white-space:nowrap; 强制不换行，都起作用</p>
<pre><code class="copyable">p&#123;
  word-wrap: break-word;
  white-space: normal;
  word-break: break-all;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-//不换行 copyable" lang="//不换行">.wrap &#123;
  white-space:nowrap;
&#125;
//自动换行
.wrap &#123;
  word-wrap: break-word;
  word-break: normal;
&#125;
//强制换行
.wrap &#123;
  word-break:break-all;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2"><strong>3、文字阴影</strong></h3>
<p>text-shadow 为网页字体添加阴影，通过对text-shadow属性设置相关的属性值。属性与值的说明如下：text-shadow: [X-offset,Y-offset,Blur,Color];</p>
<blockquote>
<p>X-offset:指阴影居于字体水平偏移的位置。
Y-offset:指阴影居于字体垂直偏移的位置。
Blur:指阴影的模糊值。
color:指阴影的颜色；</p>
</blockquote>
<pre><code class="copyable">h1&#123;
text-shadow: 5px 5px 5px #FF0000;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3"><strong>4、设置placeholder的字体样式</strong></h3>
<pre><code class="copyable">input::-webkit-input-placeholder &#123; /* Chrome/Opera/Safari */
  color: red;
&#125;
input::-moz-placeholder &#123; /* Firefox 19+ */
  color: red;
&#125;
input:-ms-input-placeholder &#123; /* IE 10+ */
  color: red;
&#125;
input:-moz-placeholder &#123; /* Firefox 18- */
  color: red;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4"><strong>5、不固定高宽 div 垂直居中的方法</strong></h3>
<p>方法一：伪元素和 inline-block / vertical-align（兼容 IE8）</p>
<pre><code class="copyable">.box-wrap:before &#123;
      content: '';
      display: inline-block;
      height: 100%;
      vertical-align: middle;
      margin-right: -0.25em; //微调整空格
&#125;
.box &#123;
     display: inline-block;
     vertical-align: middle;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法二：flex(不兼容 ie8 以下)</p>
<pre><code class="copyable">.box-wrap &#123;
     height: 300px;
     justify-content:center;
     align-items:center;
     display:flex;
     background-color:#666;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法三：transform(不兼容 ie8 以下)</p>
<pre><code class="copyable">.box-wrap &#123;
     width:100%;
     height:300px;
     background:rgba(0,0,0,0.7);
     position:relative;
&#125;
.box&#123;
    position:absolute;
    left:50%;
    top:50%;
    transform:translateX(-50%) translateY(-50%);
    -webkit-transform:translateX(-50%) translateY(-50%);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法四：设置 margin:auto（该方法得严格意义上的非固定宽高，而是 50%的父级的宽高。）</p>
<pre><code class="copyable">.box-wrap &#123;
    position: relative;
    width:100%;
    height:300px;
    background-color:#f00;
&#125;
.box-content&#123;
    position: absolute;
    top:0;
    left:0;
    bottom:0;
    right:0;
    width:50%;
    height:50%;
    margin:auto;
    background-color:#ff0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5"><strong>6、解决IOS页面滑动卡顿</strong></h3>
<pre><code class="copyable">body,html&#123;
    -webkit-overflow-scrolling: touch;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6"><strong>7、设置滚动条样式</strong></h3>
<pre><code class="copyable">.test::-webkit-scrollbar&#123;
  /*滚动条整体样式*/
  width : 10px;  /*高宽分别对应横竖滚动条的尺寸*/
  height: 1px;
&#125;
.test::-webkit-scrollbar-thumb &#123;
  /*滚动条里面小方块*/
  border-radius   : 10px;
  background-color: skyblue;
  background-image: -webkit-linear-gradient(
      45deg,
      rgba(255, 255, 255, 0.2) 25%,
      transparent 25%,
      transparent 50%,
      rgba(255, 255, 255, 0.2) 50%,
      rgba(255, 255, 255, 0.2) 75%,
      transparent 75%,
      transparent
  );
&#125;
.test::-webkit-scrollbar-track &#123;
  /*滚动条里面轨道*/
  box-shadow   : inset 0 0 5px rgba(0, 0, 0, 0.2);
  background   : #ededed;
  border-radius: 10px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7"><strong>8、实现隐藏滚动条同时又可以滚动</strong></h3>
<pre><code class="copyable">.demo::-webkit-scrollbar &#123;
  display: none; /* Chrome Safari */
&#125;

.demo &#123;
  scrollbar-width: none; /* firefox */
  -ms-overflow-style: none; /* IE 10+ */
  overflow-x: hidden;
  overflow-y: auto;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8"><strong>9、css 绘制三角形</strong></h3>
<pre><code class="copyable">div &#123;
    width: 0;
    height: 0;
    border-width: 0 40px 40px;
    border-style: solid;
    border-color: transparent transparent red;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa3d6a60c8714028aea1cea89512d65a~tplv-k3u1fbpfcp-watermark.image" alt="2500256-5183b73206878275.jpg" loading="lazy" referrerpolicy="no-referrer">
实现带边框的三角形：</p>
<pre><code class="copyable"><div id="blue"><div>

#blue &#123;
    position:relative;
    width: 0;
    height: 0;
    border-width: 0 40px 40px;
    border-style: solid;
    border-color: transparent transparent blue;
&#125;
#blue:after &#123;
    content: "";
    position: absolute;
    top: 1px;
    left: -38px;
    border-width: 0 38px 38px;
    border-style: solid;
    border-color: transparent transparent yellow;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f955e82c9efd4886964968e234903af2~tplv-k3u1fbpfcp-watermark.image" alt="2500256-c0a7fb45c1c84794.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注: 如果想绘制右直角三角，则将左 border 设置为 0；如果想绘制左直角三角，将右 border 设置为 0 即可（其它情况同理），以上方法把其他边框变成透明，点击和鼠标移入移出透明出也会影响效果。我们也可以采用css3的clip-path属性</p>
<pre><code class="copyable"><div class="demo" style="width: 300px; height: 300px; margin: auto; background: red;"></div>

.demo&#123;
-webkit-clip-path: polygon(0 100%, 50% 0, 100% 100%);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0d00553de1048b6a81843ded18fc6c1~tplv-k3u1fbpfcp-watermark.image" alt="san.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>还可以裁剪各种图形可以参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fmoqiutao%2Fp%2F10547330.html%25E6%2596%2587%25E7%25AB%25A0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/moqiutao/p/10547330.html%E6%96%87%E7%AB%A0" ref="nofollow noopener noreferrer">www.cnblogs.com/moqiutao/p/…</a></p>
<p>注意：不支持IE和Firefox，支持webkit浏览器，在现代浏览器中需要使用-webkit-前缀</p>
<h3 data-id="heading-9"><strong>10、Table表格边框合并</strong></h3>
<pre><code class="copyable">table,tr,td&#123;
  border: 1px solid #666;
&#125;
table&#123;
  border-collapse: collapse;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10"><strong>11、css 选取第 n 个标签元素</strong></h3>
<blockquote>
<p>first-child first-child 表示选择列表中的第一个标签。
last-child last-child 表示选择列表中的最后一个标签
nth-child(3) 表示选择列表中的第 3 个标签
nth-child(2n) 这个表示选择列表中的偶数标签
nth-child(2n-1) 这个表示选择列表中的奇数标签
nth-child(n+3) 这个表示选择列表中的标签从第 3 个开始到最后。
nth-child(-n+3) 这个表示选择列表中的标签从 0 到 3，即小于 3 的标签。
nth-last-child(3) 这个表示选择列表中的倒数第 3 个标签。</p>
</blockquote>
<p>使用方法：</p>
<p><code>li:first-child&#123;&#125;</code></p>
<h3 data-id="heading-11"><strong>12、移动端软键盘变为搜索方式</strong></h3>
<p>默认情况下软键盘上该键位为前往或者确认等文字，要使其变为搜索文字，需要在 input 上加上 type 声明：</p>
<pre><code class="copyable"><form action="#">
    <input type="search" placeholder="请输入..." name="search" />
</form>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要一个 form 标签套起来,并且设置 action 属性,这样写完之后输入法的右下角就会自动变成搜索,同时，使用了 search 类型后，搜索框上会默认自带删除按钮。</p>
<h3 data-id="heading-12"><strong>13、onerror 处理图片异常</strong></h3>
<p>使用 onerror 异常处理时，若 onerror 的图片也出现问题，则图片显示会陷入死循环，所以要在赋值异常图片之后，将地址置空</p>
<p><code><img onerror="this.src='url;this.onerror=null'" /></code></p>
<h3 data-id="heading-13"><strong>14、背景图片的大小</strong></h3>
<pre><code class="copyable">.bg-img&#123;
    background:url(../img/find_pw_on_2.png)  no-repeat center center !important;
    background-size: 27px auto !important;
    /*background-size: 100% 100%;*/
    /*background-size: 50px 100px*/
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14"><strong>15、文字之间的间距</strong></h3>
<p>单词text-indent抬头距离，letter-spacing字与字间距</p>
<pre><code class="copyable">p&#123;
  text-indent：10px；//单词抬头距离
  letter-spacing：10px；//间距
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15"><strong>16、元素占满整个屏幕</strong></h3>
<p>heigth如果使用100%，会根据父级的高度来决定，所以使用100vh单位。</p>
<pre><code class="copyable">.dom&#123;
  width:100%;
  height:100vh;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16"><strong>17、CSS实现文本两端对齐</strong></h3>
<pre><code class="copyable">.wrap &#123;
    text-align: justify;
    text-justify: distribute-all-lines;  //ie6-8
    text-align-last: justify;  //一个块或行的最后一行对齐方式
    -moz-text-align-last: justify;
    -webkit-text-align-last: justify;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17"><strong>18、实现文字竖向排版</strong></h3>
<pre><code class="hljs language-// 单列展示时 copyable" lang="// 单列展示时">.wrap &#123;
    width: 25px;
    line-height: 18px;
    height: auto;
    font-size: 12px;
    padding: 8px 5px;
    word-wrap: break-word;/*英文的时候需要加上这句，自动换行*/ 
&#125;
// 多列展示时
.wrap &#123;
    height: 210px;
    line-height: 30px;
    text-align: justify;
    writing-mode: vertical-lr;  //从左向右    
    writing-mode: tb-lr;        //IE从左向右
    //writing-mode: vertical-rl;  -- 从右向左
    //writing-mode: tb-rl;        -- 从右向左
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18"><strong>19、使元素鼠标事件失效</strong></h3>
<pre><code class="copyable">.wrap &#123;
  // 如果按tab能选中该元素，如button，然后按回车还是能执行对应的事件，如click。
 pointer-events: none;
 cursor: default;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19"><strong>20、禁止用户选择</strong></h3>
<pre><code class="copyable">.wrap &#123;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20"><strong>21、使用硬件加速</strong></h3>
<p>在浏览器中用css开启硬件加速，使GPU (Graphics Processing Unit) 发挥功能，从而提升性能。硬件加速在移动端尤其有用，因为它可以有效的减少资源的利用。
目前主流浏览器会检测到页面中某个DOM元素应用了某些CSS规则时就会开启，最显著的特征的元素的3D变换。如果不使用3D变形，我们可以通过下面方式来开启：</p>
<pre><code class="copyable">.wrap &#123;
    transform: translateZ(0);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21"><strong>22、页面动画出现闪烁问题</strong></h3>
<p>在 Chrome and Safari中，当我们使用CSS transforms 或者 animations时可能会有页面闪烁的效果，下面的代码可以修复此情况：</p>
<pre><code class="copyable">.cube &#123;
   -webkit-backface-visibility: hidden;
   backface-visibility: hidden;

   -webkit-perspective: 1000;
   perspective: 1000;
   /* Other transform properties here */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在webkit内核的浏览器中，另一个行之有效的方法是</p>
<pre><code class="copyable">.cube &#123;
   -webkit-transform: translate3d(0, 0, 0);
   transform: translate3d(0, 0, 0);
  /* Other transform properties here */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22"><strong>23、字母大小写转换</strong></h3>
<pre><code class="copyable">p &#123;text-transform: uppercase&#125;  // 将所有字母变成大写字母
p &#123;text-transform: lowercase&#125;  // 将所有字母变成小写字母
p &#123;text-transform: capitalize&#125; // 首字母大写
p &#123;font-variant: small-caps&#125;   // 将字体变成小型的大写字母
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23"><strong>24、将一个容器设为透明</strong></h3>
<pre><code class="copyable">.wrap &#123; 
  filter:alpha(opacity=50); 
  -moz-opacity:0.5; 
  -khtml-opacity: 0.5; 
  opacity: 0.5; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24"><strong>25、消除transition闪屏</strong></h3>
<pre><code class="copyable">.wrap &#123;
    -webkit-transform-style: preserve-3d;
    -webkit-backface-visibility: hidden;
    -webkit-perspective: 1000;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25"><strong>26、识别字符串里的 '\n' 并换行</strong></h3>
<p>一般在富文本中返回换行符不是<br>的标签，而且\n。不使用正则转换的情况下，可通过下面样式实现换行。</p>
<pre><code class="copyable">body &#123;
   white-space: pre-line;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26"><strong>27、移除a标签被点链接的边框</strong></h3>
<pre><code class="copyable">a &#123;
  outline: none；//或者outline: 0
  text-decoration:none; //取消默认下划线
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27"><strong>28、CSS显示链接之后的URL</strong></h3>
<pre><code class="copyable"><a href="//www.webqdkf.com">有课前端网</a>
<style> a:after &#123;content: " (" attr(href) ")";&#125; </style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28"><strong>29、select内容居中显示、下拉内容右对齐</strong></h3>
<pre><code class="copyable">select&#123;
    text-align: center;
    text-align-last: center;
&#125;
select option &#123;
    direction: rtl;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29"><strong>30、修改input输入框中光标的颜色不改变字体的颜色</strong></h3>
<pre><code class="copyable">input&#123;
    color:  #fff;
    caret-color: red;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30"><strong>31、子元素固定宽度 父元素宽度被撑开</strong></h3>
<pre><code class="hljs language-// 父元素下的子元素是行内元素 copyable" lang="// 父元素下的子元素是行内元素">.wrap &#123;
  white-space: nowrap;
&#125;
// 若父元素下的子元素是块级元素
.wrap &#123;
  white-space: nowrap;  // 子元素不被换行
  display: inline-block;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31"><strong>32、让div里的图片和文字同时上下居中</strong></h3>
<p>这里不使用flex布局的情况。通过vertival-align</p>
<pre><code class="copyable">.wrap &#123;
  height: 100,
  line-height: 100
&#125;
img &#123;
  vertival-align：middle
&#125;
// vertical-align css的属性vertical-align用来指定行内元素（inline）或表格单元格（table-cell）元素的垂直对齐方式。只对行内元素、表格单元格元素生效，不能用它垂直对齐块级元素
// vertical-align：baseline/top/middle/bottom/sub/text-top;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32"><strong>33、实现宽高等比例自适应矩形</strong></h3>
<pre><code class="copyable">.scale &#123;
  width: 100%;
  padding-bottom: 56.25%;
  height: 0;
  position: relative; 
&#125;
.item &#123;
  position: absolute; 
  width: 100%;
  height: 100%;
  background-color: 499e56;
&#125;    
<div class="scale">
     <div class="item">
         这里是所有子元素的容器
     </div>
 </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33"><strong>34、transfrom的rotate属性在span标签下失效</strong></h3>
<pre><code class="copyable">span &#123;
  display: inline-block
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-34"><strong>35、CSS加载动画</strong></h3>
<p>主要是通过css旋转动画的实现：</p>
<pre><code class="copyable">.dom&#123;
  -webkit-animation:circle 1s infinite linear;
&#125;
@keyframes circle&#123;
  0%&#123; transform: rotate(0deg); &#125;
  100%&#123; transform: rotate(360deg); &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现如下效果：</p>
<pre><code class="copyable"><div class="loader"></div>
<style> .loader &#123;
  border: 16px solid #f3f3f3;
  border-radius: 50%;
  border-top: 16px solid #3498db;
  width: 80px;
  height: 80px;
  -webkit-animation: spin 2s linear infinite;
  animation: spin 2s linear infinite;
&#125;

@-webkit-keyframes spin &#123;
  0% &#123; -webkit-transform: rotate(0deg); &#125;
  100% &#123; -webkit-transform: rotate(360deg); &#125;
&#125;

@keyframes spin &#123;
  0% &#123; transform: rotate(0deg); &#125;
  100% &#123; transform: rotate(360deg); &#125;
&#125; </style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-35"><strong>36、文字渐变效果实现</strong></h3>
<pre><code class="copyable"><div class="text_signature " >fly63前端网，一个免费学习前端知识的网站</div>
<style> .text_signature &#123;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-image: linear-gradient(to right, #ec2239, #40a4e2,#ea96f5);
    width: 320px;
&#125; </style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36"><strong>37、好看的边框阴影</strong></h3>
<pre><code class="copyable"><div class="text_shadow"></div>
<style>.text_shadow&#123;
  width:500px;
  height:100px;
  box-shadow: 0px 0px 13px 1px rgba(51, 51, 51, 0.1);
&#125; </style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-37"><strong>38、好看的背景渐变</strong></h3>
<pre><code class="copyable"><div class="text_gradient"></div>
<style>.text_gradient&#123;
  width:500px;
  height:100px;
  background: linear-gradient(25deg, rgb(79, 107, 208), rgb(98, 141, 185), rgb(102, 175, 161), rgb(92, 210, 133)) rgb(182, 228, 253);
&#125; </style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-38"><strong>39、实现立体字的效果</strong></h3>
<pre><code class="copyable"><div class="text_solid">有课前端网-web前端技术学习平台</div>
<style>.text_solid&#123;
    font-size: 32px;
    text-align: center;
    font-weight: bold;
    line-height:100px;
    text-transform:uppercase;
    position: relative;
  background-color: #333;
    color:#fff;
    text-shadow:
    0px 1px 0px #c0c0c0,
    0px 2px 0px #b0b0b0,
    0px 3px 0px #a0a0a0,
    0px 4px 0px #909090,
    0px 5px 10px rgba(0, 0, 0, 0.6);
&#125; </style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-39"><strong>40、全屏背景图片的实现</strong></h3>
<pre><code class="copyable">.swper&#123;
  background-image: url(./img/bg.jpg);
  width:100%;
  height:100%;//父级高不为100%请使用100vh
  zoom: 1;
  background-color: #fff;
  background-repeat: no-repeat;
  background-size: cover;
  -webkit-background-size: cover;
  -o-background-size: cover;
  background-position: center 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-40"><strong>41、实现文字描边的2种方法</strong></h3>
<p>方式一：</p>
<pre><code class="copyable">.stroke &#123;
      -webkit-text-stroke: 1px greenyellow;
     text-stroke: 1px greenyellow;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方式二：</p>
<pre><code class="copyable">.stroke &#123;
  text-shadow:#000 1px 0 0,#000 0 1px 0,#000 -1px 0 0,#000 0 -1px 0;
  -webkit-text-shadow:#000 1px 0 0,#000 0 1px 0,#000 -1px 0 0,#000 0 -1px 0;
  -moz-text-shadow:#000 1px 0 0,#000 0 1px 0,#000 -1px 0 0,#000 0 -1px 0;
  *filter: Glow(color=#000, strength=1);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-41"><strong>42、元素透明度的实现</strong></h3>
<pre><code class="copyable">.dom&#123;
  opacity:0.4;
  filter:alpha(opacity=40); /* IE8 及其更早版本 */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用rgba()设置颜色透明度。</p>
<pre><code class="copyable">.demo&#123;
  background:rgba(255,0,0,1);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说明：RGBA 是代表Red（红色） Green（绿色） Blue（蓝色）和 Alpha（不透明度）三个单词的缩写。</p>
<h3 data-id="heading-42"><strong>43、解决1px边框变粗问题</strong></h3>
<pre><code class="copyable">.dom&#123;
  height: 1px;
  background: #dbdbdb;
  transform:scaleY(0.5);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Ps：出现1px变粗的原因，比如在2倍屏时1px的像素实际对应2个物理像素。</p>
<h3 data-id="heading-43"><strong>44、CSS不同单位的运算</strong></h3>
<p>css自己也能够进行简单的运算，主要是用到了calc这个函数。实现不同单位的加减运算：</p>
<pre><code class="copyable">.div&#123; 
   width: calc(100% - 50px); 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-44"><strong>45、CSS实现文字模糊效果</strong></h3>
<pre><code class="copyable">.vague_text&#123;
  color: transparent; 
  text-shadow: #111 0 0 5px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-45"><strong>46、通过滤镜让图标变灰</strong></h3>
<p>一张彩色的图片就能实现鼠标移入变彩色，移出变灰的效果。</p>
<pre><code class="copyable"><a href='' class='icon'><img src='01.jpg' /></a>
<style> .icon&#123;
  -webkit-filter: grayscale(100%);
  -moz-filter: grayscale(100%);
  -ms-filter: grayscale(100%);
  -o-filter: grayscale(100%);   
  filter: grayscale(100%);
  filter: gray;
&#125;
.icon:hover&#123;
  filter: none;
  -webkit-filter: grayscale(0%);
&#125; </style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-46"><strong>47、图片自适应object-fit</strong></h3>
<p>当图片比例不固定时，想要让图片自适应，一般都会用background-size:cover/contain，但是这个只适用于背景图。css3中可使用object-fit属性来解决图片被拉伸或是被缩放的问题。使用的提前条件：图片的父级容器要有宽高。</p>
<pre><code class="copyable">img&#123;
    width: 100%;
    height: 100%;
    object-fit: cover;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>fill: 默认值。内容拉伸填满整个content box, 不保证保持原有的比例。contain: 保持原有尺寸比例。长度和高度中长的那条边跟容器大小一致，短的那条等比缩放，可能会有留白。cover: 保持原有尺寸比例。宽度和高度中短的那条边跟容器大小一致，长的那条等比缩放。可能会有部分区域不可见。（常用）none: 保持原有尺寸比例。同时保持替换内容原始尺寸大小。scale-down:保持原有尺寸比例,如果容器尺寸大于图片内容尺寸，保持图片的原有尺寸，不会放大失真；容器尺寸小于图片内容尺寸，用法跟contain一样。</p>
<h3 data-id="heading-47"><strong>48、行内标签元素出现间隙问题</strong></h3>
<p>方式一：父级font-size设置为0</p>
<pre><code class="hljs language-. copyable" lang=".">father&#123;
 font-size:0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方式二：父元素上设置word-spacing的值为合适的负值</p>
<pre><code class="copyable">.father&#123;
   word-spacing:-2px
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其它方案：1将行内元素写为1行(影响阅读)；2使用浮动样式（会影响布局）。</p>
<h3 data-id="heading-48"><strong>49、解决vertical-align属性不生效</strong></h3>
<p>在使用vertical-align:middle实现垂直居中的时候，经常会发现不生效的情况。这里需要注意它生效需要满足的条件：</p>
<blockquote>
<p>**作用环境：**父元素设置line-height。需要和height一致。或者将display属性设置为table-cell，将块元素转化为单元格。
**作用对象：**子元素中的inline-block和inline元素。</p>
</blockquote>
<pre><code class="copyable"><div class="box">
  <img src=".\test.jpg"/>
  <span>内部文字</span>
</div>
<style> .box&#123;
  width:300px; 
  line-height: 300px;
  font-size: 16px; 
&#125;
.box img&#123;
  width: 30px; 
  height:30px; 
  vertical-align:middle
&#125;
.box span&#123;
  vertical-align:middle
&#125; </style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>PS：vertical-align不可继承，必须对子元素单独设置。同时需要注意的是line-height的高度基于font-size（即字体的高度），如果文字要转行会出现异常哦。如有侵权联系小编删除本文完~</p></div>  
</div>
            