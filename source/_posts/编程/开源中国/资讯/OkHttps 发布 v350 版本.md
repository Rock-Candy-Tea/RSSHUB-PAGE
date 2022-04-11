
---
title: 'OkHttps 发布 v3.5.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7428'
author: 开源中国
comments: false
date: Mon, 11 Apr 2022 11:58:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7428'
---

<div>   
<div class="content">
                                                                    
                                                        <h4 style="margin-left:0; margin-right:0; text-align:left">重大更新：</h4> 
<ol> 
 <li>增强：<code>HttpTask</code><span> </span>新增<span> </span><strong>Basic Auth</strong><span> </span>便捷方法：<code>basicAuth(String username, String password)</code></li> 
 <li>增强：<code>HttpTask</code><span> </span>新增<span> </span><strong>Bearer Auth</strong><span> </span>便捷方法：<code>bearerAuth(String token)</code></li> 
 <li>增强：<code>HttpTask</code><span> </span>新增<span> </span><strong>流式文件</strong><span> </span>上传方法：<code>addFilePara(String name, String type, InputStream stream)</code></li> 
 <li>增强：<code>HttpTask</code><span> </span>新增<span> </span><strong>流式文件</strong><span> </span>上传方法：<code>addFilePara(String name, String type, String fileName, InputStream stream)</code></li> 
 <li>增强：<code>HttpTask</code><span> </span>增强<span> </span><code>setBodyPara(Object body)</code><span> </span>方法：使其可以接受<span> </span><code>InputStream</code><span> </span>类型的<span> </span><strong>流式报文体</strong><span> </span>参数</li> 
 <li>增强：<code>HttpTask</code><span> </span>使用<span> </span><code>ListMap</code><span> </span>作为请求参数的内部集合容器：使其可以接受<span> </span><strong>多个同名参数</strong><span> </span>并可<span> </span><strong>保持参数的添加顺序</strong></li> 
 <li>增强：<code>HTTP</code><span> </span>的<span> </span><code>HTTP.builder()</code><span> </span>方法，使之支持通过指定系统环境变量来让该方法返回不同的构建器实现类</li> 
 <li>增强：<code>HTTP.Builder</code><span> </span>新增<span> </span><code>clearContentTypes()</code><span> </span>方法</li> 
 <li>增强：<code>HttpResult</code><span> </span>新增<span> </span><code>allHeaders()</code><span> </span>方法</li> 
 <li>优化：<code>HttpTask</code><span> </span>放松校验：移除 必须将路径参数占位符全部填充的 检查</li> 
 <li>优化：<code>HttpTask</code><span> </span>请求时<span> </span><code>Content-Type</code><span> </span>请求头<span> </span><strong>不再</strong><span> </span>默认携带<span> </span><code>charset</code><span> </span>信息</li> 
 <li>优化：<code>AbstractHttpClient</code><span> </span>的<span> </span><code>mediaType</code><span> </span>映射机制</li> 
 <li>完善：<code>OkHttpBuilderImpl</code><span> </span>常见的<span> </span><code>mediaType</code><span> </span>映射</li> 
 <li>完善：<code>DownloadHelper</code><span> </span>添加更多常见的扩展名映射</li> 
 <li>重构：<code>java.util.function.Supplier</code><span> </span>替代<span> </span><code>com.ejlchina.okhttps.PingSupplier</code><span> </span>接口</li> 
 <li>重构：<code>java.util.function.Consumer</code><span> </span>替代<span> </span><code>com.ejlchina.okhttps.OnCallback</code><span> </span>接口</li> 
 <li>升级：<code>data</code>：<code>v1.1.2</code><span> </span>-><span> </span><code>1.4.0</code>：<a href="https://gitee.com/ejlchina-zhxu/data/releases" target="_blank">https://gitee.com/ejlchina-zhxu/data/releases</a> 
  <ul> 
   <li><code>Mapper</code><span> </span>新增<span> </span><code>toBean(Class<T> type)</code>、<code>toBean(TypeRef<T> type)</code><span> </span>与<span> </span><code>toBean(Type type)</code><span> </span>方法</li> 
   <li><code>Array</code><span> </span>新增<span> </span><code>toList(Class<T> type)</code><span> </span>方法</li> 
   <li><code>DataConvertor</code><span> </span>新增：<code>toMapper(String in)</code>、<code>toArray(String in)</code>、<code>serialize(Object object)</code>、<code>toBean(Type type, String in)</code>、<code>toList(Class<T> type, String in)</code><span> </span>方法</li> 
   <li><code>Deserializer</code><span> </span>新增<span> </span><code>getInstance()</code><span> </span>方法</li> 
   <li><code>fastjson</code>:<span> </span><code>v1.2.79</code><span> </span>-><span> </span><code>v1.2.80</code></li> 
   <li><code>jackson</code>:<span> </span><code>v2.12.6</code><span> </span>-><span> </span><code>v2.13.2.2</code></li> 
   <li>新增<span> </span><code>ListMap</code><span> </span>接口 与<span> </span><code>ArrayListMap</code><span> </span>/<span> </span><code>LinkedListMap</code><span> </span>相关实现类</li> 
  </ul> </li> 
 <li>过时：<code>HttpResult</code><span> </span>的<span> </span><code>getHeaders()</code><span> </span>方法标记为已过时</li> 
 <li>过时：<code>HttpResult.Body</code><span> </span>的<span> </span><code>getType()</code><span> </span>方法标记为已过时</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">-----------------------------------</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">参见：<br> https://github.com/ejlchina/okhttps<br> https://gitee.com/ejlchina-zhxu/okhttps</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">软件介绍：</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">OkHttps 是一个强大轻量 且 前后端通用的 HTTP 客户端，同时支持 WebSocket 以及 Stomp 协议 <span style="background-color:#ffffff; color:#40485b">的国产开源软件，</span><span style="background-color:#ffffff; color:#4a4a4a">还不了解的同学点下面的链接哦：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li style="text-align:left"><span style="background-color:#ffffff; color:#4a4a4a">系统教程：https://</span>okhttps<span style="background-color:#ffffff; color:#4a4a4a">.ejlchina.com/</span></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">振兴中华，弘扬国产软件，同胞们觉得还可以的话点个 STAR 吧 ^_^：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Github: https://github.com/ejlchina/okhttps</li> 
 <li>Gitee:   https://gitee.com/ejlchina-zhxu/okhttps</li> 
</ul>
                                        </div>
                                      
</div>
            