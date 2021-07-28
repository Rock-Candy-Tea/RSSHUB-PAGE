
---
title: 'HTML5(二)——获取用户位置Geolocation'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31d41fa67d274345afcc1f073ce63edd~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 22:41:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31d41fa67d274345afcc1f073ce63edd~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>地图类、打车、外卖等类型的手机APP，一进入便咨询是否允许获取我们的位置，允许之后会根据我们所在位置推荐好物，逐渐地 H5 网页也开始获取用户位置。Geolocation是 H5 新增的对象，用于定位。常见打开网页有两种方式：移动端和PC端。它们是根据什么如何定位的呢？</p>
<ol>
<li><strong>IP定位：</strong> 通过IP地址定位，由于没有硬件支持，主要是服务器根据 IP库判断所处位置，所以精度差。</li>
<li><strong>GPS(全球定位系统)：</strong> 使用GPS定位，定位时间长，耗电量大，但是精度高。</li>
<li><strong>WIFI定位：</strong> wifi 定位数据是通过三角距离计算得到，三角是指当前多个接入wifi用户的已知距离，wifi在室内也非常准确。</li>
<li><strong>手机地理位置：</strong> 基于手机的地理定位数据是通过用户到一些基站的三角距离确定。这种方法可提供相当准确的位置结果。这种方法通常和基于WIFI基于GPS地位结合使用。</li>
<li><strong>用户自定义：</strong> 用户可以手动输入的地理位置。</li>
</ol>
<h1 data-id="heading-0">Geolocation 方法</h1>
<p>geolocation对象继承在navigator对象内，它有两种方法可以获取用户位置getCurrentPosition()和watchPosition()，还有clearWatch取消watchPosition。</p>
<p><strong>getCurrentPosition：</strong> 获取一次位置</p>
<pre><code class="copyable">navigator.geolocation.getCurrentPosition(success=>&#123;
 console.log(success.coords)//包含位置的经纬度、速度、海拔、经纬度精度、海拔精度信息
&#125;,fail=>&#123;
 console.log(fail)//获取失败的原因
&#125;,&#123;
 //可增加的4个配置参数
  enableHighAccuracy:true,//高精度
  timeout:5000,//超时时间,以ms为单位
  maximumAge:24*60*60*1000,//位置缓存时间,以ms为单位
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>位置获取成功后返回的 <strong>success.coords</strong> 的属性</p>
<ul>
<li>coords.latitude - 纬度</li>
<li>coords.longitude - 经度</li>
<li>coords.altitude - 海拔</li>
<li>coords.speed - 速度</li>
<li>coords.accuracy - 经纬度精度</li>
<li>coords.altitudeAccuracy - 海拔精度</li>
<li>coords.heading - 方向，从正北开始的弧度数</li>
</ul>
<p><strong>watchPosition：</strong> 不断获取位置</p>
<pre><code class="copyable">navigator.geolocation.watchPosition(
 success=>&#123;
  console.log(success.coords)//包含用户位置速度海拔等信息
 &#125;,
 fail=>&#123;
  console.log(fail)//定位失败原因
 &#125;,
 &#123;
  enableHighAccuracy:true,//高精度
  timeout:60*1000,//超时，以ms为单位
  maximumAge:24*60*60*1000,//位置缓存时间，以ms为单位
  frequency:1000,//获取频率
 &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>位置获取成功后返回的 <strong>success.coords</strong> 的属性与上述getCurrentPosition的一致。它两唯一的区别就是一个获取一次，另外一个获取多次，多了一个获取频率参数。</p>
<p><strong>clearWatch()</strong> ： 取消当前位置的获取，停止 watchPosition 方法。</p>
<p>clearWatch 与 js 中的clearInterval类似，clearInterval用于清除定时器。使用时语法如下：</p>
<pre><code class="copyable">var wPId = navigator.geolocation.watchPosition(
 success=>&#123;
  console.log(success.coords)//包含用户位置速度海拔等信息
 &#125;,
 fail=>&#123;
  console.log(fail)//定位失败原因
 &#125;,
 &#123;
  enableHighAccuracy:true,//高精度
  timeout:60*1000,//超时，以ms为单位
  maximumAge:24*60*60*1000,//位置缓存时间，以ms为单位
  frequency:1000,//获取频率
 &#125;
)
navigator.geolocation.clearWatch(wPId)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">Geolocation 应用</h1>
<p>由于该特性可能侵犯用户的隐私，使用时自动会询问用户是否同意授权位置，除非用户同意，否则无法获取到用户位置。</p>
<pre><code class="copyable">function getPosition()&#123;
 if(navigator.geolocation)&#123;
  navigator.geolocation.getCurrentPosition(function(res)&#123;
   console.log("res",res)//位置信息
  &#125;,function(err)&#123;
   console.log("err",err)
  &#125;)
 &#125;
&#125;
getPosition()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在电脑上，直接使用浏览器打开文件，浏览器立马弹出如下显示框：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31d41fa67d274345afcc1f073ce63edd~tplv-k3u1fbpfcp-zoom-1.image" alt="HTML5(二)——获取用户位置Geolocation" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击禁止后，调试器中打印出报错信息，报错信息为：</p>
<pre><code class="copyable">&#123;
code: 1
message: "User denied Geolocation" //用户拒绝地理位置
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击允许之后，发现并未打印出位置信息，什么原因呢？PC是根据电脑的IP地址来解析位置的，此时直接打开文件没有域名或ip，所以无法获取位置，必须把文件放到服务内，如果你是不会起服务可以下载nginx，下载安装成功之后文件放入html文件夹内，启动nginx就可以访问了。</p>
<p>启动本地服务，再次获取位置之后，发现依旧报错，无法返回位置，报错信息为：</p>
<pre><code class="copyable">&#123;
 code: 1, 
 message: "Only secure origins are allowed (see: https://goo.gl/Y0ZkNV)."//只允许安全来源
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>意思就是只能在https域名下才可以哦！</p>
<p>还需要注意的是chrome的google浏览器也不能获取位置，但是IE浏览器可以获取到。</p>
<p>把上述案例放到线上，获取位置只要用户点击同意就没有问题啦！</p>
<p>除此之外，带有位置的我们经常会用到输入位置，在地图中自动标记一个点，移动标记点到更具体的位置，如图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f34aac13b73f439695d875648693fc48~tplv-k3u1fbpfcp-zoom-1.image" alt="HTML5(二)——获取用户位置Geolocation" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一般需要绘制地图的时候，我们就借助三方的百度、高德、腾讯等地图，注册账号，申请密钥才可以使用。</p></div>  
</div>
            