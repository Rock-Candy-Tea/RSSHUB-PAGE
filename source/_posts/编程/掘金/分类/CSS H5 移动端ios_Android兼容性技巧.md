
---
title: 'CSS H5 移动端ios_Android兼容性技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcac465b344847aeac4f497a0c17c015~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 01:43:05 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcac465b344847aeac4f497a0c17c015~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">理解一下meta</h2>
<pre><code class="copyable"><meta charset="utf-8">
<!--主要I是强制让文档的宽度与设备宽度保持1:1，最大宽度1.0，禁止屏幕缩放。-->
<meta content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport">
<!--这个也是iphone私有标签，允许全屏浏览。-->
<meta content="yes" name="apple-mobile-web-app-capable">
<!--iphone的私有标签，iphone顶端状态条的样式。-->
<meta content="black" name="apple-mobile-web-app-status-bar-style">
<!--禁止数字自动识别为电话号码，这个比较有用，因为一串数字在iphone上会显示成蓝色，样式加成别的颜色也是不生效的。-->
<meta content="telephone=no" name="format-detection">
<!--禁止email识别-->
<meta content="email=no" name="format-detection">
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>禁止复制、选中文本</strong></p>
<pre><code class="hljs language-.el copyable" lang=".el">  -webkit-user-select: none;
  -moz-user-select: none;
  -khtml-user-select: none;
   user-select: none;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>IOS中input键盘事件keyup、keydown、keypress支持不是很好, 用input监听键盘keyup事件，在安卓手机浏览器中是可以的，但是在ios手机浏览器中用输入法输入之后，并未立刻相应keyup事件，只有在通过删除之后才可以响应
方法：可以用html5的oninput事件去代替keyup</p>
<pre><code class="hljs language-<input copyable" lang="<input"><script type="text/javascript">
  document.getElementById('input').addEventListener('input', function(e)&#123;
    var value = e.target.value;
  &#125;);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>ios 设置input 按钮样式会被默认样式覆盖</strong></p>
<pre><code class="copyable">input,textarea &#123;
  border: 0;
  -webkit-appearance: none;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>flex布局对于低版本的安卓，不支持flex-wrap:wrap属性，但是ios系统支持换行属性，这个时候如何解决呢？当然是不使用换行，用其他方式代替。</p>
<pre><code class="copyable">.box&#123;
    display: -webkit-box; 
    /* 老版本语法: Safari, iOS, Android browser, older WebKit browsers. */
    display: -moz-box; /* 老版本语法: Firefox (buggy) */
    display: -ms-flexbox; /* 混合版本语法: IE 10 */
    display: -webkit-flex; /* 新版本语法: Chrome 21+ */
    display: flex; /* 新版本语法: Opera 12.1, Firefox 22+ */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>input 的placeholder属性会使文本位置偏上</strong></p>
<pre><code class="hljs language-line-height: copyable" lang="line-height:">line-height：normal ---移动端解决方法
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>实现android和ios系统手机打开相机并可选择相册功能</strong></p>
<pre><code class="copyable"><input class="js_upFile cover1" type="file" name="cover" accept="image/*" capture="camera" multiple/>
$(function () &#123;
    //获取浏览器的userAgent,并转化为小写
    var ua = navigator.userAgent.toLowerCase();
    //判断是否是苹果手机，是则是true
    var isIos = (ua.indexOf('iphone') != -1) || (ua.indexOf('ipad') != -1);
    if (isIos) &#123;
        $("input:file").removeAttr("capture");
    &#125;;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>移动端 HTML5 audio autoplay 失效问题</strong></p>
<pre><code class="copyable">document.addEventListener('touchstart',function() &#123;
  document.getElementsByTagName('audio')[0].play();
  document.getElementsByTagName('audio')[0].pause();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>针对ios的刘海屏问题的解决：</strong></p>
<pre><code class="hljs language-<meta copyable" lang="<meta"><span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>把页面主体内容限定在安全区内</strong></p>
<pre><code class="hljs language-body copyable" lang="body">    padding-top: constant(safe-area-inset-top);
    padding-top: env(safe-area-inset-top);
    padding-bottom: constant(safe-area-inset-bottom);
    padding-bottom: env(safe-area-inset-bottom);
    padding-left: constant(safe-area-inset-left);
    padding-left: env(safe-area-inset-left);
    padding-right: constant(safe-area-inset-right);
    padding-right: env(safe-area-inset-right);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>针对android的刘海屏、水滴屏等问题的解决</strong>
在公共样式内定义：</p>
<pre><code class="copyable">// ios顶部留出20px高度
.havetop &#123;
    .my-header &#123;
        padding-top: 20px;
    &#125;
    .content &#123;
        padding-top: 20px;
    &#125;
&#125;
.isios &#123;
    .my-header &#123;
        padding-top: constant(safe-area-inset-top);
        padding-top: env(safe-area-inset-top);
    &#125;
    .content &#123;
        padding-top: constant(safe-area-inset-top);
        padding-top: env(safe-area-inset-top);
    &#125;
&#125;
<script>
    window.onload = function () &#123;
        document.getElementById('app').classList.add('havetop');
        if (/iPhone/.test(navigator.userAgent)) &#123;
            document.getElementById('app').classList.add('isios');
        &#125;
    &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注：具体使用的页面头部（.my-header）是非定位，主体部分（.content）是absolute定位，如图所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcac465b344847aeac4f497a0c17c015~tplv-k3u1fbpfcp-watermark.image" alt="20200903181610776.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可能会出现的问题：部分状态栏高的安卓机型，头部会有部分的遮盖，在这里可以用上面的judgeBigScreen这个方法判断一下是否是android的全面屏，如果是全面屏的话给头部和主体部分的padding值适当增加：</p>
<pre><code class="hljs language-<script> copyable" lang="<script>">    //判断屏幕是否为全面屏
    function judgeBigScreen() &#123;
        //这里根据返回值 true 或false ,返回true的话 则为全面屏
        var result = false;
        var rate = window.screen.height / window.screen.width;
        var limit = window.screen.height == window.screen.availHeight ? 1.8 : 1.65; // 临界判断值
        // window.screen.height为屏幕高度
        //  window.screen.availHeight 为浏览器 可用高度
        if (rate > limit) &#123;
            result = true;
        &#125;
        return result;
    &#125;
    window.onload = function () &#123;
       document.getElementById('app').classList.add('havetop');
        if (/iPhone/.test(navigator.userAgent)) &#123;
            document.getElementById('app').classList.add('isios');
        &#125; else &#123;
            //全面屏
            let judgeFullScreen = judgeBigScreen();
            if (judgeFullScreen) &#123;
                document.getElementById('app').classList.add('isFullScreen');
            &#125;
        &#125;
    &#125;
</script>
.isFullScreen &#123;
    .my-header &#123;
        padding-top: 30px;
        padding-top: 30px;
    &#125;
    .content &#123;
        padding-top: 30px;
        padding-top: 30px;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下图所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/158c03c218f744d49c2dfc30b1787b64~tplv-k3u1fbpfcp-watermark.image" alt="20200904135513337.jpeg" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            