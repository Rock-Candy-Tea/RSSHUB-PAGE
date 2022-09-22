
---
title: 'IJPay 2.9.0 版本发布，让支付触手可及'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6850'
author: 开源中国
comments: false
date: Thu, 22 Sep 2022 08:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6850'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">IJPay 让支付触手可及，封装了微信支付、QQ 支付、支付宝支付、银联支付、京东支付、PayPal 支付等常用的支付方式以及各种常用的接口。不依赖任何第三方 mvc 框架，仅仅作为工具使用简单快速完成支付模块的开发，可轻松嵌入到任何系统里。</span></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>特别说明：</strong></p> 
<ul> 
 <li>不依赖任何第三方 MVC 框架，仅仅作为工具使用简单快速完成支付模块的开发，可轻松嵌入到任何系统里。</li> 
 <li>微信支付支持多商户多应用，普通商户模式与服务商商模式当然也支持境外商户、同时支持 Api-v3 与 Api-v2 版本的接口。</li> 
 <li>支付宝支付支持多商户多应用，签名同时支持普通公钥方式与公钥证书方式</li> 
</ul> 
<p>本期更新内容如下</p> 
<ol> 
 <li>第三方依赖升级，支付宝SDK升级至 「4.33.44.ALL」</li> 
 <li>第三方依赖升级，huTool 升级至 「5.8.7」</li> 
 <li>微信支付 V2 版本接口沙箱环境 「sandboxnew」 变更为 「xdc/apiv2sandbox」</li> 
 <li>微信支付  「WxApiType」接口枚举由于接口过多过于臃肿标记弃用，替代方案使用「 com.ijpay.wxpay.enums.v2」「 com.ijpay.wxpay.enums.v3」包下的枚举，方便后期扩展以及维护。</li> 
 <li>支持打包至容器中部署，新增了辅助方法 「com.ijpay.core.kit.PayKit#getFileToStream」、「com.ijpay.core.kit.PayKit#getAbsolutePath」、「com.ijpay.core.kit.PayKit#getCertFileInputStream」</li> 
 <li>解决「解决直连商户APP支付下单时，提示'请求中含有未在API文档中定义的参数'的错误」 感谢 kun928 的贡献</li> 
 <li>「扩展微信V3版分账Model」感谢 kun928 的贡献</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">欢迎大家贡献代码，任何支付问题，欢迎在此一起探讨 <a href="https://www.oschina.net/p/ijpay">右上角 - 我要提问</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Node.js 版本微信支付：</strong> <a href="https://gitee.com/javen205/TNWX">TNWX 微信系开发脚手架</a></p>
                                        </div>
                                      
</div>
            