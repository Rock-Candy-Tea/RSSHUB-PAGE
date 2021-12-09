
---
title: 'Forest v1.5.14 发布，声明式 HTTP 框架，现已 1.9k star'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e095709750cf803e835235b2f549ef278f6.png'
author: 开源中国
comments: false
date: Thu, 09 Dec 2021 15:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e095709750cf803e835235b2f549ef278f6.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0; margin-right:0"><img height="248" src="https://oscimg.oschina.net/oscnet/up-e095709750cf803e835235b2f549ef278f6.png" width="400" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>Forest已参加2021年度OSC中国开源项目评选活动，如果您喜欢Forest或对Forest感兴趣，请投上您宝贵的一票，感谢！</strong></p> 
<p style="margin-left:0em; margin-right:0em">点击投票👉<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.oschina.net%2Fproject%2Ftop_cn_2021%2F%3Fid%3D573" target="_blank">投票</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><strong>Forest介绍</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 是一个开源的 Java HTTP 客户端框架，它能够将 HTTP 的所有请求信息（包括 URL、Header 以及 Body 等信息）绑定到您自定义的 Interface 方法上，能够通过调用本地接口方法的方式发送 HTTP 请求</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">现已 1.9k star</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://chart.giteye.net/gitee/dromara/forest/NURRL346.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Forest 如何使用</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 不需要您编写具体的 HTTP 调用过程，只需要您定义一个接口，然后通过 Forest 注解将 HTTP 请求的信息添加到接口的方法上即可。请求发送方通过调用您定义的接口便能自动发送请求和接受请求的响应</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Forest 的工作原理</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Forest 会将您定义好的接口通过动态代理的方式生成一个具体的实现类，然后组织、验证 HTTP 请求信息，绑定动态数据，转换数据形式，SSL 验证签名，调用后端 HTTP API(httpclient 等 API)执行实际请求，等待响应，失败重试，转换响应数据到 Java 类型等脏活累活都由这动态代理的实现类给包了。 请求发送方调用这个接口时，实际上就是在调用这个干脏活累活的实现类</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">文档和示例</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com%2F" target="_blank">项目官网</a></li> 
 <li><a href="https://apidoc.gitee.com/dt_flys/forest/">JavaDoc</a></li> 
 <li><a href="https://gitee.com/dt_flys/forest-example">Demo工程</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">重点更新内容</h2> 
<h4 style="margin-left:0; margin-right:0; text-align:start">自定义<code>hostnameVerifier</code></h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">定义一个实现 HostnameVerifier 接口的类</p> 
<div style="text-align:start"> 
 <pre><code><span>/**
 * 自定义SSL主机名/域名验证器
 */</span>
<strong style="color:#333333">public</strong> <span><strong style="color:#333333">class</strong> <strong style="color:#445588">MyHostnameVerifier</strong> <strong style="color:#333333">implements</strong> <strong style="color:#445588">HostnameVerifier</strong> </span>&#123;
    <span>@Override</span>
    <span><strong style="color:#333333">public</strong> <strong style="color:#333333">boolean</strong> <strong style="color:#990000">verify</strong><span>(String s, SSLSession sslSession)</span> </span>&#123;
        <strong style="color:#333333">if</strong> (<span style="color:#dd1144">"gitee.com"</span>.equals(s)) &#123;
            <strong style="color:#333333">return</strong> <strong style="color:#333333">true</strong>;
        &#125;
        <strong style="color:#333333">return</strong> <strong style="color:#333333">false</strong>;
    &#125;
&#125;
</code></pre> 
 <div style="text-align:center">
   
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">将自定义的SSL主机名验证器配置到 Forest 的<code>KeyStore</code>中</p> 
<p>在Springboot项目的<code>application.yml</code>文件中配置</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#dd1144">forest:</span>
  ssl-key-<span style="color:#dd1144">stores:</span>
    - <span style="color:#dd1144">id:</span> keystore1
      hostname-<span style="color:#dd1144">verifier:</span> your.site.MyHostnameVerifier
</code></pre> 
 <div style="text-align:center">
   
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">在接口中绑定</p> 
<div style="text-align:start"> 
 <pre><code><span>@Post</span>(url = <span style="color:#dd1144">"/something"</span>, keyStore = <span style="color:#dd1144">"keystore1"</span>)
<span>String <strong style="color:#990000">postSomething</strong><span>(@Body body)</span></span>;
</code></pre> 
 <div style="text-align:center">
   
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start"><code>@SSLHostnameVerifier</code>注解</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">除了在全局配置文件中的<code>keyStore</code>中配置外, 也可以通过相关注解直接在接口上绑定</p> 
<div style="text-align:start"> 
 <pre><code><strong style="color:#333333">public</strong> <span><strong style="color:#333333">class</strong> <strong style="color:#445588">MyHostnameVerifier</strong> <strong style="color:#333333">implements</strong> <strong style="color:#445588">HostnameVerifier</strong> </span>&#123;
    <span>@Override</span>
    <span><strong style="color:#333333">public</strong> <strong style="color:#333333">boolean</strong> <strong style="color:#990000">verify</strong><span>(String hostname, SSLSession session)</span> </span>&#123;
        <em>// 只通过域名为 gitee.com 的请求</em>
        <strong style="color:#333333">if</strong> (<span style="color:#dd1144">"gitee.com"</span>.equals(hostname)) &#123;
            <strong style="color:#333333">return</strong> <strong style="color:#333333">true</strong>;
        &#125;
        <strong style="color:#333333">return</strong> <strong style="color:#333333">false</strong>;
    &#125;
&#125;
</code></pre> 
 <div style="text-align:center">
   
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">通过<code>@SSLHostnameVerifier</code>注解绑定到接口</p> 
<div style="text-align:start"> 
 <pre><code><span>@Post</span>(url = <span style="color:#dd1144">"/something"</span>)
<span>@SSLHostnameVerifier</span>(TrustAnyHostnameVerifier.class)
<span>String <strong style="color:#990000">postSomething</strong><span>(@Body body)</span></span>;
</code></pre> 
 <div style="text-align:center">
   
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start"><code>@SSLSocketFactoryBuilder</code>注解</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">同理 SSLSocketFactory 也一样可以自定义，同时由<code>@SSLSocketFactoryBuilder</code>注解来绑定</p> 
<div style="text-align:start"> 
 <pre><code><strong style="color:#333333">public</strong> <span><strong style="color:#333333">class</strong> <strong style="color:#445588">MySSLSocketFactoryBuilder</strong> <strong style="color:#333333">implements</strong> <strong style="color:#445588">SSLSocketFactoryBuilder</strong> </span>&#123;

    <span>@Override</span>
    <span><strong style="color:#333333">public</strong> SSLSocketFactory <strong style="color:#990000">getSSLSocketFactory</strong><span>(ForestRequest request, String protocol)</span> <strong style="color:#333333">throws</strong> Exception </span>&#123;
        SSLContext sslContext = SSLContext.getInstance(<span style="color:#dd1144">"SSL"</span>);
        sslContext.init(<strong style="color:#333333">null</strong>,
                <strong style="color:#333333">new</strong> TrustManager[] &#123; <strong style="color:#333333">new</strong> TrustAllManager() &#125;,
                <strong style="color:#333333">new</strong> SecureRandom());
        System.out.println(<span style="color:#dd1144">"do MySSLSocketFactoryBuilder"</span>);
        <strong style="color:#333333">return</strong> sslContext.getSocketFactory();
    &#125;
&#125;
</code></pre> 
 <div style="text-align:center">
   
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">绑定到接口</p> 
<div style="text-align:start"> 
 <pre><code><span>@Post</span>(url = <span style="color:#dd1144">"/something"</span>)
<span>@SSLSocketFactoryBuilder</span>(MySSLSocketFactoryBuilder.class)
<span>String <strong style="color:#990000">postSomething</strong><span>(@Body body)</span></span>;</code></pre> 
</div> 
<div style="text-align:start"> 
 <div> 
  <div style="text-align:left"> 
   <div style="text-align:start"> 
    <div style="text-align:left"> 
     <h3 style="margin-left:0; margin-right:0">本次更新</h3> 
     <blockquote> 
      <div style="text-align:start"> 
       <div style="text-align:start"> 
        <div style="text-align:start"> 
         <h4 style="margin-left:0; margin-right:0; text-align:start">新增特性</h4> 
         <ul> 
          <li>feat: 自定义 hostnameVerifier 和 SSLSocketFactoryBuilder (<a href="https://gitee.com/dromara/forest/issues/I4LGW8">#I4LGW8:自定义 hostnameVerifier 和 SSLSocketFactoryBuilder<span> </span></a>)</li> 
          <li>feat: 根据Response的Content-Encoding自动识别是否为gzip压缩数据，并自动解压</li> 
         </ul> 
         <h4 style="margin-left:0; margin-right:0; text-align:start">修复问题</h4> 
         <ul> 
          <li>fix: 重定向后URL的Query参数会重复增加 (<a href="https://gitee.com/dromara/forest/issues/I4LPGU">#I4LPGU:重定向后URL的Query参数会重复增加</a>)</li> 
          <li>fix: 修复content-encoding导致的字符编码转换异常 (<a href="https://gitee.com/dromara/forest/issues/I4LJ3X">#I4LJ3X:在返回压缩数据时,如果 响应头content-type 没有charset ForestResponse.byteToString 方法异常</a>)</li> 
          <li>fix: 修复字符编码判断的BUG</li> 
         </ul> 
         <h4 style="margin-left:0; margin-right:0; text-align:start">代码更新</h4> 
         <ul> 
          <li>add: @SSLHostnameVerifier 注解</li> 
          <li>add: @SSLSocketFactoryBuilder 注解</li> 
         </ul> 
         <h2 style="margin-left:0; margin-right:0; text-align:start">鸣谢</h2> 
         <p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">本次更新有<span> </span><a href="https://gitee.com/designer">@AlexShi<span> </span></a>小伙伴参与贡献，万分感谢！</p> 
        </div> 
       </div> 
      </div> 
     </blockquote> 
    </div> 
   </div> 
  </div> 
 </div> 
</div> 
<div style="text-align:start"> 
 <h2 style="margin-left:0; margin-right:0">2021年度OSC中国开源项目评选</h2> 
 <p style="margin-left:0; margin-right:0"><strong>Forest已参加2021年度OSC中国开源项目评选活动，如果您喜欢Forest或对Forest感兴趣，请投上您宝贵的一票，感谢！</strong></p> 
 <p style="margin-left:0em; margin-right:0em">点击投票👉<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.oschina.net%2Fproject%2Ftop_cn_2021%2F%3Fid%3D573" target="_blank">投票</a></p> 
</div>
                                        </div>
                                      
</div>
            