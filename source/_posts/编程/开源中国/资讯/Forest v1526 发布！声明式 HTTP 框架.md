
---
title: 'Forest v1.5.26 发布！声明式 HTTP 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7176a890789deaf0dc6ec8695cc2bb8b13b.png'
author: 开源中国
comments: false
date: Thu, 11 Aug 2022 11:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7176a890789deaf0dc6ec8695cc2bb8b13b.png'
---

<div>   
<div class="content">
                                                                                            <p><img src="https://oscimg.oschina.net/oscnet/up-7176a890789deaf0dc6ec8695cc2bb8b13b.png" width="45%" referrerpolicy="no-referrer"></p> 
<h2>Forest介绍</h2> 
<p>Forest 是一个开源的 Java HTTP 客户端框架，它能够将 HTTP 的所有请求信息（包括 URL、Header 以及 Body 等信息）绑定到您自定义的 Interface 方法上，能够通过调用本地接口方法的方式发送 HTTP 请求</p> 
<h2>Forest 如何使用</h2> 
<p>Forest 不需要您编写具体的 HTTP 调用过程，只需要您定义一个接口，然后通过 Forest 注解将 HTTP 请求的信息添加到接口的方法上即可。请求发送方通过调用您定义的接口便能自动发送请求和接受请求的响应</p> 
<h2>Forest 的工作原理</h2> 
<p>Forest 会将您定义好的接口通过动态代理的方式生成一个具体的实现类，然后组织、验证 HTTP 请求信息，绑定动态数据，转换数据形式，SSL 验证签名，调用后端 HTTP API(httpclient 等 API)执行实际请求，等待响应，失败重试，转换响应数据到 Java 类型等脏活累活都由这动态代理的实现类给包了。 请求发送方调用这个接口时，实际上就是在调用这个干脏活累活的实现类</p> 
<h2>获得奖项</h2> 
<p>2021 年度 OSC 中国开源项目评选「最受欢迎项目」</p> 
<p>相关链接: <a href="https://www.oschina.net/project/top_cn_2021">https://www.oschina.net/project/top_cn_2021</a></p> 
<h2>一个栗子</h2> 
<p>定义请求接口</p> 
<pre><code class="language-java">public interface MyClient &#123;

    @Get("http://localhost:8080/hello")
    String helloRequest();

&#125;
</code></pre> 
<p>发送请求</p> 
<pre><code class="language-java">// 注入自定义的 Forest 接口实例
@Resource
private MyClient myClient;

public void testClient() &#123;
    // 调用自定义的 MyClient 接口方法
    // 等价于发送 HTTP 请求，请求地址和参数即为 helloRequest 方法上注解所标识的内容
    String result = myClient.helloRequest();
    // result 即为 HTTP 请求响应后返回的字符串类型数据
    System.out.println(result);
&#125;
</code></pre> 
<h2>声明式接口</h2> 
<pre><code class="language-java">// 高德地图API
public interface AmapClient &#123;
    /**
     * 根据经纬度查询地址信息
     * 在url中的&#123;0&#125;代表引用第一个参数，&#123;1&#125;引用第二个参数
     */
    @Get("http://ditu.amap.com/service/regeo")
    Map getLocation(@Query("longitude") String longitude, @Query("latitude") String latitude);
&#125;
</code></pre> 
<h2>编程式接口</h2> 
<pre><code class="language-java">// 定义各种参数
// 并以 Map 类型接受
Map<String, Object> map = Forest.post("/data")
      .host("localhost")         // 设置地址的host为 127.0.0.1
      .port(8080)                // 设置地址的端口为 8080
      .contentTypeJson()         // 设置 Content-Type 头为 application/json
      .addBody("a", 1)           // 添加 Body 项(键值对)： a, 1
      .addBody("b", 2)           // 添加 Body 项(键值对：  b, 2
      .executeAsMap();           // 执行并返回Map数据类型对象
</code></pre> 
<h2>官网和仓库地址</h2> 
<blockquote> 
 <h4>官网地址:</h4> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com" target="_blank">http://forest.dtflyx.com</a></p> 
 <h4>Gitee 仓库地址:</h4> 
 <p><a href="https://gitee.com/dromara/forest">https://gitee.com/dromara/forest</a></p> 
 <h4>Github 仓库地址:</h4> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fforest" target="_blank">https://github.com/dromara/forest</a></p> 
</blockquote> 
<h2>本次更新内容</h2> 
<blockquote> 
 <ul> 
  <li>feat: 在使用 OkHttp3 后端情况下，允许Query参数不转义大括号 (#I5ITW9)</li> 
  <li>feat: 在使用 OkHttp3 时绕过空 Multipart 错误 (#I5I1AC)</li> 
  <li>fix: 默认自动绕过SSL验证</li> 
  <li>fix: 声明的接口返回类型如果是String（或其他Charsequencel类型）导致自定义converter (#I5L2P6)</li> 
  <li>fix: okhttp后端自动将charset=UTF-8转成了小写 (#I5L4AS)</li> 
  <li>fix: url域名信息参数赋值会自动参数后添加”/“符号路径导致错误 (#I5I62P)</li> 
  <li>fix: URL路径中的$字符会被转义</li> 
  <li>fix: 请求的ForestURL的ssl属性没有继承类里@BaseRequest的ssl信息 (#I5HXHX)</li> 
  <li>update: 更新 spring 版本到<code>5.3.19</code></li> 
  <li>update: 更新 spring boot 版本到<code>2.6.7</code></li> 
 </ul> 
</blockquote>
                                        </div>
                                      
</div>
            