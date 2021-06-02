
---
title: 'ViewxJS v1.5.0 发布，前端 MVC 模板引擎框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://developer.mozilla.org/static/media/internet-explorer.cf17782c.svg'
author: 开源中国
comments: false
date: Wed, 02 Jun 2021 09:03:00 GMT
thumbnail: 'https://developer.mozilla.org/static/media/internet-explorer.cf17782c.svg'
---

<div>   
<div class="content">
                                                                    
                                                        <p>ViewxJS，此版本更新内容包括：</p> 
<p>1.增加v-else<br> 2.增加v-elif</p> 
<h4>介绍</h4> 
<p>ViewxJS，一个简单的前端mvc模板引擎框架，简单易用，2kb min+gzip运行大小，无需虚拟DOM高效运行。</p> 
<h4>安装</h4> 
<pre>npm i silis-viewjs</pre> 
<h4>文件大小</h4> 
<table> 
 <thead> 
  <tr> 
   <th>文件名</th> 
   <th>文件大小</th> 
   <th>文件说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>viewx.min.js.zip</td> 
   <td>2.6k</td> 
   <td>js代码压缩 + zip压缩，用于网络要求更高的生产运营环境</td> 
  </tr> 
  <tr> 
   <td>viewx.min.js</td> 
   <td>6k</td> 
   <td>js代码压缩，用于生产运营时使用</td> 
  </tr> 
  <tr> 
   <td>viewx.js</td> 
   <td>15k</td> 
   <td>js源代码，用于开发测试时使用</td> 
  </tr> 
  <tr> 
   <td>jsc.min.js</td> 
   <td>2.8k</td> 
   <td>用于兼容低版本浏览器，如：IE5.5-IE8.0</td> 
  </tr> 
 </tbody> 
</table> 
<h4>兼容版本</h4> 
<table> 
 <thead> 
  <tr> 
   <th>电脑端</th> 
   <th>浏览器</th> 
   <th>最小版本</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td><img alt="Internet Explorer" src="https://developer.mozilla.org/static/media/internet-explorer.cf17782c.svg" referrerpolicy="no-referrer"></td> 
   <td>Internet Explorer</td> 
   <td>5.5</td> 
  </tr> 
  <tr> 
   <td><img alt="Chrome" src="https://developer.mozilla.org/static/media/chrome.4c570865.svg" referrerpolicy="no-referrer"></td> 
   <td>Chrome</td> 
   <td>1</td> 
  </tr> 
  <tr> 
   <td><img alt="Edge" src="https://developer.mozilla.org/static/media/edge.40018f6a.svg" referrerpolicy="no-referrer"></td> 
   <td>Edge</td> 
   <td>12</td> 
  </tr> 
  <tr> 
   <td><img alt="Firefox" src="https://developer.mozilla.org/static/media/firefox.51d8a59c.svg" referrerpolicy="no-referrer"></td> 
   <td>Firefox</td> 
   <td>3</td> 
  </tr> 
  <tr> 
   <td><img alt="Opera" src="https://developer.mozilla.org/static/media/opera.a0ab0c50.svg" referrerpolicy="no-referrer"></td> 
   <td>Opera</td> 
   <td>15</td> 
  </tr> 
  <tr> 
   <td><img alt="Safari" src="https://developer.mozilla.org/static/media/safari.3679eb31.svg" referrerpolicy="no-referrer"></td> 
   <td>Safari</td> 
   <td>4</td> 
  </tr> 
 </tbody> 
</table> 
<table> 
 <thead> 
  <tr> 
   <th>手机端</th> 
   <th>浏览器</th> 
   <th>最小版本</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td><img alt="WebView Android" src="https://developer.mozilla.org/static/media/android.7d9bf320.svg" referrerpolicy="no-referrer"></td> 
   <td>WebView Android</td> 
   <td>1</td> 
  </tr> 
  <tr> 
   <td><img alt="Chrome Android" src="https://developer.mozilla.org/static/media/chrome.4c570865.svg" referrerpolicy="no-referrer"></td> 
   <td>Chrome Android</td> 
   <td>18</td> 
  </tr> 
  <tr> 
   <td><img alt="Firefox Android" src="https://developer.mozilla.org/static/media/firefox.51d8a59c.svg" referrerpolicy="no-referrer"></td> 
   <td>Firefox Android</td> 
   <td>4</td> 
  </tr> 
  <tr> 
   <td><img alt="Opera Android" src="https://developer.mozilla.org/static/media/opera.a0ab0c50.svg" referrerpolicy="no-referrer"></td> 
   <td>Opera Android</td> 
   <td>14</td> 
  </tr> 
  <tr> 
   <td><img alt="iOS Safari" src="https://developer.mozilla.org/static/media/safari.3679eb31.svg" referrerpolicy="no-referrer"></td> 
   <td>iOS Safari</td> 
   <td>3.2</td> 
  </tr> 
  <tr> 
   <td><img alt="Samsung Internet" src="https://developer.mozilla.org/static/media/samsung-internet.6fd7f423.svg" referrerpolicy="no-referrer"></td> 
   <td>Samsung Internet</td> 
   <td>1.0</td> 
  </tr> 
 </tbody> 
</table> 
<blockquote> 
 <p>兼容IE5.5-IE8浏览器，需要引用/lib/jsc.min.js。（如果不需要兼容低版本浏览器，则不需要引用jsc库）</p> 
</blockquote> 
<h4>示例</h4> 
<p>演示最简单的例子say hello</p> 
<pre><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <script src="../lib/jsc.min.js" type="text/javascript"></script>
    <script src="../viewx.min.js"></script>
    <script>
        Page(&#123;
            data: &#123;
                name: "Tom"
            &#125;
        &#125;)
    </script>
</head>
<body>

    <vx>&#123;&#123;name&#125;&#125;</vx> say hello

</body>
</html></pre> 
<p>示例文件：/demo/say-hello.html</p> 
<p>详情查看：<a href="https://gitee.com/silis/ViewxJS/releases/v1.5.0">https://gitee.com/silis/ViewxJS/releases/v1.5.0</a></p>
                                        </div>
                                      
</div>
            