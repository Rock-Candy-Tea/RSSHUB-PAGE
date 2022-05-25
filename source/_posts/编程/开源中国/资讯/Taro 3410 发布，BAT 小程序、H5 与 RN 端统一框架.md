
---
title: 'Taro 3.4.10 发布，BAT 小程序、H5 与 RN 端统一框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4144'
author: 开源中国
comments: false
date: Wed, 25 May 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4144'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Taro 3.4.10 现已发布。Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发微信 / 京东 / 百度 / 支付宝 / 字节跳动 / QQ 小程序 / H5 等应用。具体更新内容如下：</span></p> 
<h4><strong>修复</strong></h4> 
<p style="text-align:start"><strong>小程序</strong></p> 
<ul> 
 <li>补充字节小程序<span> </span><code>Textarea</code><span> </span>组件的属性，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11776" target="_blank">#11776</a></li> 
 <li>修复支付宝小程序<span> </span><code>PickerViewColumn</code><span> </span>组件不能设置类名和<span> </span><code>style</code><span> </span>的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F10264" target="_blank">#10264</a></li> 
 <li>调整路由参数逻辑，修复当页面被蜘蛛抓取时，路由字符串不固定的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11713" target="_blank">#11713</a></li> 
 <li>支持<span> </span><code>style</code><span> </span>设置部分<span> </span><code>webkit</code><span> </span>样式，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F8109" target="_blank">#8109</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11802" target="_blank">#11802</a></li> 
 <li>模板支持为第三方自定义组件的属性设置默认值，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11575" target="_blank">#11575</a></li> 
</ul> 
<p style="text-align:start"><strong>RN</strong></p> 
<ul> 
 <li>修复<span> </span><code>request</code><span> </span>请求中当不传<span> </span><code>header</code><span> </span>时，<code>content-type</code><span> </span>为<span> </span><code>undefined</code><span> </span>导致代码报错的问题</li> 
</ul> 
<p style="text-align:start"><strong>@tarojs/plugin-mini-ci</strong></p> 
<ul> 
 <li>针对字节小程序 CLI 工具的用法进行了升级，兼容<span> </span><code>upload</code><span> </span>与<span> </span><code>preview</code><span> </span>方法</li> 
</ul> 
<h4>Typings</h4> 
<ul> 
 <li>为一部分支持字节小程序的类型增加支持字节的注释</li> 
 <li>更新组件及 API 中的 RN 标记</li> 
 <li>补充<span> </span><code>pageScrollTo</code><span> </span>API 的类型</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Freleases%2Ftag%2Fv3.4.10" target="_blank">https://github.com/NervJS/taro/releases/tag/v3.4.10</a></p>
                                        </div>
                                      
</div>
            