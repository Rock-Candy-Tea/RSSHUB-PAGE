
---
title: 'Payment Spring Boot 1.0.14 发布，微信支付 V3 全功能实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3127'
author: 开源中国
comments: false
date: Fri, 16 Sep 2022 08:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3127'
---

<div>   
<div class="content">
                                                                                            <p style="color:#363c42; text-align:start"><span><strong><span>Payment Spring Boot</span></strong></span><span> 发布 </span><span><strong><span>1.0.14.RELEASE</span></strong></span><span> 版本，<strong>本次版本发布后已经实现了微信支付V3几乎全部的服务商和直连商户系列API，已经能够完全适用于微信支付提供的所有支付场景</strong>。</span></p> 
<p style="color:#363c42; text-align:start"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNotFound403%2Fpayment-spring-boot"><span>Payment Spring Boot</span></a></span><span> 是微信支付 V3 的 </span><span><strong><span>Java</span></strong></span><span> 实现，仅仅依赖 </span><span><strong><span>Spring</span></strong></span><span> 内置的一些类库。配置简单方便，可以让开发者快速、优雅地为 </span><span><strong><span>Spring Boot</span></strong></span><span> 应用接入微信支付，并且屏蔽了签名、验签的复杂流程，开发者成功配置后即可进行业务开发。更多更新信息请参考 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnotfound403.github.io%2Fpayment-spring-boot%2F%23%2Fchangelog"><span>changelog</span></a></span><span>。</span></p> 
<h2 style="text-align:start"><span>环境要求</span></h2> 
<ul> 
 <li> <p style="color:var(--text-color); margin-left:.5rem; margin-right:0"><span>OpenJDK 8或者高版本Oracle JDK 8 </span></p> </li> 
 <li> <p style="color:var(--text-color); margin-left:.5rem; margin-right:0"><span>Spring Boot 2.5以上</span></p> </li> 
</ul> 
<h2 style="text-align:start"><span>项目地址</span></h2> 
<ul> 
 <li> <p style="color:var(--text-color); margin-left:.5rem; margin-right:0"><span><strong><span>Github：</span></strong></span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNotFound403%2Fpayment-spring-boot"><span>https://github.com/NotFound403/payment-spring-boot</span></a></span></p> </li> 
 <li> <p style="color:var(--text-color); margin-left:.5rem; margin-right:0"><span><strong><span>Gitee：</span></strong></span><span> </span><span><a href="https://gitee.com/felord/payment-spring-boot">https://gitee.com/felord/payment-spring-boot</a></span></p> </li> 
</ul> 
<blockquote> 
 <p style="color:var(--quote-text-color); margin-left:0; margin-right:0"><span>欢迎 </span><span><strong><span>Star</span></strong></span><span> 、</span><span><strong><span>PR</span></strong></span><span>，有问题请 </span><span><strong><span>ISSUE</span></strong></span><span>。</span></p> 
</blockquote> 
<h2 style="text-align:start"><span>1.0.14 更新日志</span></h2> 
<h3 style="text-align:start"><span>微信支付</span></h3> 
<ul> 
 <li> <p style="color:var(--text-color); margin-left:.5rem; margin-right:0"><span>fix: 批量转账到零钱查询BUG </span><span><a href="https://gitee.com/felord/payment-spring-boot/issues/I5E2X7"><span>（#I5E2X7）</span></a></span></p> </li> 
 <li> <p style="color:var(--text-color); margin-left:.5rem; margin-right:0"><span>feat: 移除了被标记过期的API，包括基于<strong>微信支付V2版本</strong>的分账实现，使用相关接口的同学需要针对性的进行迁移</span></p> </li> 
 <li> <p style="color:var(--text-color); margin-left:.5rem; margin-right:0"><span>feat: 增加证书绝对路径实现，现在证书可以进行外部配置了。</span></p> 
  <ul> 
   <li style="list-style-type:circle"> <p style="color:var(--text-color); margin-left:.5rem; margin-right:0"><span>配置项增加</span><span><code>certAbsolutePath</code></span><span>字段用来定义支付证书的绝对路径，优先级高于</span><span><code>certPath</code></span><span>，当这两个路径都不配置时采用</span><span><code>classpath</code></span><span>路径</span><span><code>wechat/apiclient_cert.p12</code></span><span> </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNotFound403%2Fpayment-spring-boot%2Fissues%2F73" target="_blank"><span>（#73）</span></a></span></p> </li> 
  </ul> </li> 
</ul> 
<h4 style="text-align:start"><span>服务商</span></h4> 
<ul> 
 <li> <p style="color:var(--text-color); margin-left:.5rem; margin-right:0"><span>feat: 实现服务商商户进件-特约商户进件相关API</span></p> </li> 
 <li> <p style="color:var(--text-color); margin-left:.5rem; margin-right:0"><span>feat: 实现点金计划相关API，适用于服务商</span></p> </li> 
 <li> <p style="color:var(--text-color); margin-left:.5rem; margin-right:0"><span>feat: 实现行业方案-电商收付通相关API</span></p> </li> 
 <li> <p style="color:var(--text-color); margin-left:.5rem; margin-right:0"><span>feat: 实现行业方案-智慧商圈相关API</span></p> </li> 
 <li> <p style="color:var(--text-color); margin-left:.5rem; margin-right:0"><span>feat: 实现其它能力-银行组件（服务商）相关API</span></p> </li> 
 <li> <p style="color:var(--text-color); margin-left:.5rem; margin-right:0"><span>enhance: 新增服务商分账下载账单接口</span></p> </li> 
 <li> <p style="color:var(--text-color); margin-left:.5rem; margin-right:0"><span>enhance: 新增服务商退款回调接口</span></p> </li> 
</ul> 
<h4 style="text-align:start"><span>通用能力</span></h4> 
<ul> 
 <li> <p style="color:var(--text-color); margin-left:.5rem; margin-right:0"><span>feat: 实现其它能力-图片、视频上传相关API</span></p> </li> 
 <li> <p style="color:var(--text-color); margin-left:.5rem; margin-right:0"><span>feat: 实现支付即服务相关API，适用于服务商和直连商户</span></p> </li> 
</ul>
                                        </div>
                                      
</div>
            