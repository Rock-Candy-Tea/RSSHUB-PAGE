
---
title: 'zlt-mp v4.6.0 发布，基于 Spring Cloud Alibaba 的微服务平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-45ebd22a4d43320cb3454a5f672087370c7.png'
author: 开源中国
comments: false
date: Wed, 28 Jul 2021 08:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-45ebd22a4d43320cb3454a5f672087370c7.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="275" src="https://oscimg.oschina.net/oscnet/up-45ebd22a4d43320cb3454a5f672087370c7.png" width="500" referrerpolicy="no-referrer"></p> 
<h1 style="text-align:left">功能介绍</h1> 
<p style="text-align:left"><img alt height="414" src="https://oscimg.oschina.net/oscnet/up-b7726359902d450aab833cda3b17a69b85c.png" width="500" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">更新内容<strong>更新内容</strong></h2> 
<h3>特性/增强</h3> 
<ul> 
 <li> <p>优化授权中心支持<strong>「多用户体系」</strong>扩展</p> </li> 
 <li> <p>升级spring-boot到2.3.12.RELEASE</p> </li> 
 <li> <p>升级spring-cloud到Hoxton.SR12</p> </li> 
 <li> <p>升级spring-cloud-alibaba到2.2.6.RELEASE</p> </li> 
 <li> <p>升级redisson到3.16.0</p> </li> 
 <li> <p>升级spring-data-elasticsearch到4.2.3</p> </li> 
 <li> <p>升级transmittable到2.12.1</p> </li> 
</ul> 
<h2 style="text-align:left">内容说明</h2> 
<h2 style="text-align:left">一、支持多用户体系</h2> 
<p>统一认证中心uaa支持多用户类型的统一授权和鉴权扩展，当系统需要新增一种用户类型时无需修改原有的代码，增加新的实现类即可。</p> 
<blockquote> 
 <p>多用户类型指的是业务中有多种类型的 <strong>「用户」</strong> ，而通常不同类型的用户分别存储在不同的库表中，例如C端和B端用户。</p> 
</blockquote> 
<h4>默认用户类型为admin</h4> 
<h4>增加test类型用户的实现类</h4> 
<pre><code><span style="color:#61aeee">@Service</span>
<span style="color:#c678dd">public</span> <span style="color:#c678dd">class</span> <span style="color:#e6c07b">TestUserDetailServiceImpl</span> <span style="color:#c678dd">implements</span> <span style="color:#e6c07b">ZltUserDetailsService</span> &#123;
    <span style="color:#c678dd">private</span> <span style="color:#c678dd">static</span> <span style="color:#c678dd">final</span> String ACCOUNT_TYPE = <span style="color:#98c379">"test"</span>;

    <span style="color:#61aeee">@Override</span>
    <span style="color:#c678dd">public</span> <span style="color:#c678dd">boolean</span> <span style="color:#61aeee">supports</span>(String accountType) &#123;
        <span style="color:#c678dd">return</span> ACCOUNT_TYPE.equals(accountType);
    &#125;
    
    <span style="color:#61aeee">@Override</span>
    <span style="color:#c678dd">public</span> UserDetails <span style="color:#61aeee">loadUserByUsername</span>(String username)&#123;
        。。。。。。
    &#125;
&#125;
</code></pre> 
<h4>授权test类型的用户</h4> 
<h2 style="text-align:left"><strong>项目地址</strong></h2> 
<p style="text-align:left">Gitee地址： <a href="https://gitee.com/zlt2000/microservices-platform">https://gitee.com/zlt2000/microservices-platform</a></p> 
<p style="text-align:left">Github地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzlt2000%2Fmicroservices-platform" target="_blank">https://github.com/zlt2000/microservices-platform</a></p> 
<h2 style="text-align:left">项目文档</h2> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzlt2000%2Fmicroservices-platform%2F919417" target="_blank">https://www.kancloud.cn/zlt2000/microservices-platform/919417</a></p> 
<h2 style="text-align:left">项目更新日志</h2> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzlt2000%2Fmicroservices-platform%2F936235" target="_blank">https://www.kancloud.cn/zlt2000/microservices-platform/936235</a></p>
                                        </div>
                                      
</div>
            