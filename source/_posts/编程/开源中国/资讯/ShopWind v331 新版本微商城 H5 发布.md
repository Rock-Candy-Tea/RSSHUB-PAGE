
---
title: 'ShopWind v3.3.1 新版本微商城 H5 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-1ce626e0cac1fbccf7775bc40e96112cc7c.JPEG'
author: 开源中国
comments: false
date: Mon, 19 Jul 2021 16:20:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-1ce626e0cac1fbccf7775bc40e96112cc7c.JPEG'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">ShopWind开源电商系统新版本H5基于uniapp开发，使用开发HBuilderX工具开发生成。前端使用vue.js，后端通过接口调用数据，不仅实现了和APP客户端功能的同步，且大大提高了开发效率。下面介绍下ShopWind新版本H5的功能特点和部署步骤。</p> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff"><strong>1.   </strong><strong>先看从外观认识下新版本（uni版）和旧版本H5端。</strong></span></span></p> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">uni版H5演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fh5.shopwind.net%2F" target="_blank">https://h5.shopwind.net</a></span></span></p> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">旧版H5演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fm.test.shopwind.net%2F" target="_blank">http://m.test.shopwind.net</a></span></span></p> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">                           <span style="background-color:#ffffff">uni</span><span style="background-color:#ffffff">版H5</span><span style="background-color:#ffffff"> 首页                                                                    </span><span style="background-color:#ffffff">旧版H5首页         </span></span></span></p> 
<p style="text-align:start"><img alt height="778" src="https://oscimg.oschina.net/oscnet/up-1ce626e0cac1fbccf7775bc40e96112cc7c.JPEG" width="350" referrerpolicy="no-referrer">        <img alt height="778" src="https://oscimg.oschina.net/oscnet/up-0f946d544db07ff5ef57a9e307e28dfd501.JPEG" width="350" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">                     <span style="background-color:#ffffff">uni</span><span style="background-color:#ffffff">版H5</span><span style="background-color:#ffffff"> 会员中心页                                                              </span><span style="background-color:#ffffff">旧版H5会员中心页 </span></span></span></p> 
<p style="text-align:start"><img alt height="778" src="https://oscimg.oschina.net/oscnet/up-e72f3121e207c7cc36648e5963e5d573dea.JPEG" width="350" referrerpolicy="no-referrer">        <img alt height="778" src="https://oscimg.oschina.net/oscnet/up-2f43da096275b1be36584de2f8c220e3552.JPEG" width="350" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">2.    <strong>Uni版开发的主要优势</strong></span></span></p> 
<ul> 
 <li><strong>多端功能同步。 </strong>一套源码生成多端，iOS、Android、H5、微信小程序、头条小程序等用户端，实现多端功能同步。当然也需要测试不同场景的兼容性问题，比如说支付、登录、分享等接口在各端的兼容和支持情况，以及一些链接配置和导航条等显示的兼容性问题。</li> 
 <li><strong>双向数据绑定，异步更新。</strong>Vue采用MVVM 模式，数据双向绑定，减少了 DOM 操作，彻底放弃了传统前端开发使用jquery操作文档的模式，将更多精力放在数据和业务逻辑上。</li> 
</ul> 
<p><img alt height="455" src="https://oscimg.oschina.net/oscnet/up-556107f4e9c1d984d2648a5668df2d3d34d.JPEG" width="875" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>标签简化，布局更加容易。</strong>Uni开发采用view标签取代了html中传统的div、p、span等标签，化繁为简。采用flex布局取代了css中的定位和浮动，对浏览器的兼容性更加友好。</li> 
 <li><strong>丰富的组件选择。</strong>Uniapp有较多的原生组件，例如对话框、地区选择、日期选择等原生组件，调用时传参给组件即可，非常方便。也可以自己制作组件，多页面重复应用。同时DCloud平台也有非常多优秀的开发者，分享各种优秀的组件。组件的使用使得开发变得简单方便。</li> 
 <li><strong>采用最新的Vue.js库。</strong>Vue.js是非常轻巧、高性能库，拥有非常容易上手的 API，响应和运行非常快速。</li> 
</ul> 
<p><img alt height="385" src="https://oscimg.oschina.net/oscnet/up-a0d9c94225cd78c1ea663f235cf86d6a922.png" width="911" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff"><strong>3.  </strong><strong> </strong><strong>新版本</strong><strong>H5</strong><strong>（</strong><strong>uni</strong><strong>版）的发行和配置</strong></span></span></p> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">1）把ShopWind移动端源码项目导入到HBuilderX工具中，打开manifest.json文件，选择h5配置标题等信息。路由模式推荐选择：<span style="color:#e53333">history模式</span>，选择该模式后，必须配置伪静态规则（按如下第6点操作），如果选择hash模式，访问地址就会带上“<span style="color:#e56600">#</span>”符合，无法兼容第三方账号登录/支付接口的回调地址</span></span></p> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff"><img height="516" src="https://oscimg.oschina.net/oscnet/up-b60d99893e3853930a5f48981046f41a9ab.png" width="900" referrerpolicy="no-referrer"></span></span></p> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">2）ShopWind电商系统只需要经过以上几步，就可以完成生成Uni版H5配置，之后我们需要获取H5源码部署到云服务器上，HBuilderX工具点击工具栏中的 “发行”，选择“网站-PC web或手机H5”项点击。</span></span></p> 
<p style="text-align:start"><img alt height="547" src="https://oscimg.oschina.net/oscnet/up-14c1bcd2cab94057b9b467d07cba35a2d81.png" width="900" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">3）在点击发行之后，会在弹窗中配置网站标题和将要使用的H5访问域名，此处填写自己的真实域名（以后你的H5站点使用的域名），配置后无法修改（如果需要修改，只能再次发行）</span></span></p> 
<p style="text-align:start"><img alt height="511" src="https://oscimg.oschina.net/oscnet/up-5199a20158ab726ebc2107985ce9518dd43.png" width="900" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">4）点击发行，工具编译完成后在项目文件目录下生产一个名为H5的文件包，如下图所示</span></span></p> 
<p style="text-align:start"><img alt height="314" src="https://oscimg.oschina.net/oscnet/up-53f4dc9cf051fe9d7e6d1310c70bc486e37.png" width="900" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">5）将上图中static文件夹及index.html首页文件上传至服务器上的网站根目录，把发行前配置的访问域名解析到该目录</span></span></p> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff"><img alt height="270" src="https://oscimg.oschina.net/oscnet/up-529a0b0c65aadcbaa4568641796ea625d2e.png" width="900" referrerpolicy="no-referrer"></span></span></p> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">6) 将源代码上传到服务器后， 如果发行的时候，选择的模式是：history模式，请务必添加web服务器的伪静态规则，以下是nginx（apache服务器请配置.htaccess, apache规则请自行转换一下）</span></span></p> 
<pre><code>location / &#123;
  try_files $uri $uri/ /index.html;
&#125;</code></pre> 
<p style="text-align:start">7)至此配置完成，如要修改页面等更新，需要重新发行，重复以上步骤</p>
                                        </div>
                                      
</div>
            