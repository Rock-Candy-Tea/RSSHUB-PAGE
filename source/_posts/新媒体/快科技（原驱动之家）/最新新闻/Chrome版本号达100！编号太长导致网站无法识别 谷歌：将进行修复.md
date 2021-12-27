
---
title: 'Chrome版本号达100！编号太长导致网站无法识别 谷歌：将进行修复'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211227/s_8dd9b52bb7e940258601d989f8bce48d.jpg'
author: 快科技（原驱动之家）
comments: false
date: Mon, 27 Dec 2021 15:54:27 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211227/s_8dd9b52bb7e940258601d989f8bce48d.jpg'
---

<div>   
<p>近日，谷歌Chrome浏览器正式开始测试100版本，<strong>作为第一个版本号突破三位数的浏览器，Chrome遇到了一些意想不到的问题。</strong></p>
<p>据悉，通过Chrome 100浏览网站，<span style="color:#ff0000;"><strong>有一定的概率会导致网站无法正常识别浏览器版本，导致用户无法正常使用网页</strong></span>，当前谷歌表示这一问题主要出现在利用Duda开发的网站，并已经开始进行修复。</p>
<p>这一问题的原因其实非常简单，大部分的网站都是通过检查User Agent string（用户代理字符串）来确定用户的浏览器版本，而在Chrome浏览器中，以当前公开版本为例，该字符串中表达版本号的内容为：Chrome/96.0.4664.45。</p>
<p>一般情况下，开发者并不需要知道浏览器的具体版本，因此在Duda中，默认将只读取“Chrome/”后的两位字符，在上述例子中就是仅读取“96”。</p>
<p><strong>这一设计使得Chrome 100会被识别为Chrome 10</strong>，而Duda为了兼容性会阻止版本低于40的Chrome浏览器打开网站，这导致Chrome 100无法正常访问网站。</p>
<p>当前，谷歌已经提出了一个解决方案。</p>
<p>谷歌认为，可以将Chrome的主要版本锁定为99，而版本号则放在次要位置，<strong>这样在用户代理字符串中表达版本号的内容就会以“Chrome/99.100.X.X”的方式呈现，从而解决识别问题。</strong></p>
<p>此外，谷歌也在寻找已经出现识别问题的网站，并试图与开发者取得联系，从而通过修改代码的方式解决问题。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20211227/8dd9b52bb7e940258601d989f8bce48d.jpg" target="_blank"><img alt="Chrome版本号达100！编号太长导致网站无法识别 谷歌：将进行修复" h="400" src="https://img1.mydrivers.com/img/20211227/s_8dd9b52bb7e940258601d989f8bce48d.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/chromeliulanqi.htm"><i>#</i>Chrome浏览器</a><a href="https://news.mydrivers.com/tag/guge.htm"><i>#</i>谷歌</a></p>
<p class="url">
     
<span>责任编辑：乃河</span>
</p>
        
</div>
            