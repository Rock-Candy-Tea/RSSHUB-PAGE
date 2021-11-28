
---
title: 'mica 2.5.7 发布，mica-redis 优化，方便自定义序列化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/596392912/mica/raw/master/docs/img/mica2.x-open.jpg'
author: 开源中国
comments: false
date: Sun, 28 Nov 2021 13:45:00 GMT
thumbnail: 'https://gitee.com/596392912/mica/raw/master/docs/img/mica2.x-open.jpg'
---

<div>   
<div class="content">
                                                                                            <h2>一、mica（云母）</h2> 
<p><code>mica</code>是一个微服务组件集，但不仅仅是组件，我们关注的是微服务生态并持续演进，尽量做到开箱即用，简化使用和排坑。总共已有 40+ 组件，并且很多组件已经打通。 </p> 
<p><img alt="mica 2.x 模块图" src="https://gitee.com/596392912/mica/raw/master/docs/img/mica2.x-open.jpg" referrerpolicy="no-referrer"></p> 
<p><img height="1350" src="https://oscimg.oschina.net/oscnet/up-96f6f25f5a7454fb9d645c13600d3d17d52.png" width="2046" referrerpolicy="no-referrer"></p> 
<h2>二、版本说明</h2> 
<table> 
 <thead> 
  <tr> 
   <th>最新版本</th> 
   <th>mica 版本</th> 
   <th>spring boot 版本</th> 
   <th>spring cloud 版本</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>2.5.7</td> 
   <td>mica 2.5.x</td> 
   <td>2.5.x</td> 
   <td>2020</td> 
  </tr> 
  <tr> 
   <td>2.4.11</td> 
   <td>mica 2.4.x</td> 
   <td>2.4.x</td> 
   <td>2020</td> 
  </tr> 
  <tr> 
   <td>2.1.1-GA</td> 
   <td>mica 2.0.x~2.1.x</td> 
   <td>2.2.x ~ 2.3.x</td> 
   <td>Hoxton</td> 
  </tr> 
 </tbody> 
</table> 
<p><strong>说明：<strong>mica 对 Spring cloud 为非强制依赖，除了 mica-jobs、mica-prometheus 其他组件</strong>普通 Spring boot 项目也可以使用</strong>。</p> 
<h2>三、更新记录</h2> 
<h3>v2.5.7 - 2021-11-28</h3> 
<ul> 
 <li>✨ mica-redis 优化，方便自定义序列化。</li> 
 <li>✨ mica-xss 优化，避免 xss 关闭时被类扫描，导致 bean 找不到异常。</li> 
 <li>✨ mica-core 添加 retry 接口。</li> 
 <li>✨ mica-http 代码优化去掉 spring retry 依赖。，感谢 Jap 作者亚东的建议。</li> 
 <li>📝 mica-redis 优化 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2FREADME.md" target="_blank">README.md</a> 文档，感谢 Jap 作者亚东的 pr。</li> 
 <li>📝 mica-http 更新 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2FREADME.md" target="_blank">README.md</a> 文档。</li> 
 <li>⬆️ Upgrading dependencies.</li> 
 <li>⬆️ 升级 Gradle 到 7.3。</li> 
 <li>⬆️ 升级 lombok 到 1.18.22。</li> 
 <li>⬆️ 升级 Spring boot 到 2.5.7。</li> 
 <li>⬆️ 升级 mica-weixin 到 2.1.2。</li> 
</ul> 
<h3>v2.5.6 - 2021-10-28</h3> 
<ul> 
 <li>✨ mica-redis 优化 MicaRedisCache bean 名称。</li> 
 <li>✨ mica-spider 更好的支持 java17。</li> 
 <li>✨ mica-core BeanUtil#generator 支持 java17。</li> 
 <li>🐛 mica-redis rpush、lpush 修复，优化 MicaRedisCache 方法泛型。</li> 
 <li>⬆️ 升级 druid 到 1.2.8</li> 
 <li>⬆️ 升级到 Spring boot 到 2.5.6</li> 
</ul> 
<h3>mica-http 使用</h3> 
<p>mica-http 是基于 okhttp 封装，Fluent 语法的 http 工具包。</p> 
<pre><code class="language-java">// 同步请求 url，方法支持 get、post、patch、put、delete
HttpRequest.get("https://www.baidu.com")
    .useSlf4jLog() // 使用 Slf4j 日志，同类的有 .useConsoleLog(),日志级别为 BODY
    .addHeader("x-account-id", "mica001") // 添加 header
    .addCookie(builder -> builder.domain("www.baidu.com").name("name").value("value"))  // 添加 cookie
    .query("q", "mica") // 设置 url 参数，默认进行 url encode
    .queryEncoded("name", "encodedValue")
    .retryOn(responseSpec -> !responseSpec.isOk()) // 对结果集进行断言重试
    .proxy(InetSocketAddress.createUnresolved("127.0.0.1", 8080)) // 设置代理
    .formBuilder()                  // 表单构造器，同类 multipartFormBuilder 文件上传表单
    .add("id", 123123)              // 表单参数
    .execute()                      // 发起请求
    .asJsonNode();                  // 结果集转换，注：如果网络异常等会直接抛出异常。
// 同类的方法有 asString、asBytes
// json 类响应：asJsonNode、asValue、asList、asMap、atJsonPath、，采用 jackson 处理
// file 文件：toFile
</code></pre> 
<h2>四、mica生态</h2> 
<ul> 
 <li>mica-auto (Spring boot starter 利器):<a href="https://gitee.com/596392912/mica-auto?fileGuid=m5kv9JK8Jmc1XgqX">https://gitee.com/596392912/mica-auto</a></li> 
 <li>mica-weixin（jfinal weixin 的 spring boot starter）：<a href="https://gitee.com/596392912/mica-weixin?fileGuid=m5kv9JK8Jmc1XgqX">https://gitee.com/596392912/mica-weixin</a></li> 
 <li>mica-mqtt（基于 t-io 实现的 mqtt组件）：<a href="https://gitee.com/596392912/mica-mqtt?fileGuid=m5kv9JK8Jmc1XgqX">https://gitee.com/596392912/mica-mqtt</a></li> 
 <li>Spring cloud 微服务 http2 方案（h2c）:<a href="https://gitee.com/596392912/spring-cloud-java11?fileGuid=m5kv9JK8Jmc1XgqX">https://gitee.com/596392912/spring-cloud-java11</a></li> 
 <li>mica-security（mica权限系统 vue 改造中）:<a href="https://gitee.com/596392912/mica-security?fileGuid=m5kv9JK8Jmc1XgqX">https://gitee.com/596392912/mica-security</a></li> 
</ul> 
<h2>五、文档</h2> 
<ul> 
 <li>文档地址（官网）：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwiki.dreamlu.net%2Fguide%2Fgetting-started.html%3FfileGuid%3Dm5kv9JK8Jmc1XgqX" target="_blank">http://wiki.dreamlu.net</a></li> 
 <li>文档地址（语雀-可关注订阅）：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fdreamlu%3FfileGuid%3Dm5kv9JK8Jmc1XgqX" target="_blank">https://www.yuque.com/dreamlu</a></li> 
</ul>
                                        </div>
                                      
</div>
            