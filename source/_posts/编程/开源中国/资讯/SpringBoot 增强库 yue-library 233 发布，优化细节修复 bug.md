
---
title: 'SpringBoot 增强库 yue-library 2.3.3 发布，优化细节修复 bug'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/yl-yue/yue-library/raw/master/docs/_images/logo.png'
author: 开源中国
comments: false
date: Mon, 31 May 2021 10:27:00 GMT
thumbnail: 'https://gitee.com/yl-yue/yue-library/raw/master/docs/_images/logo.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><img alt="logo" src="https://gitee.com/yl-yue/yue-library/raw/master/docs/_images/logo.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">yue-library简介</h2> 
<blockquote> 
 <p>yue-library是一个基于SpringBoot封装的增强库</p> 
</blockquote> 
<ul> 
 <li>丰富的Java工具类库</li> 
 <li>优越的ORM框架</li> 
 <li>优雅的业务封装</li> 
 <li>优化的Spring环境配置</li> 
 <li>完善的规约限制</li> 
 <li>配套的代码生成平台</li> 
 <li>安稳贴切的开源架构方案</li> 
</ul> 
<h2 style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fylyue.cn%2F%23%2Fchangelog" target="_blank">版本更新日志</a></h2> 
<p style="text-align:left">2.3.3主要为bug修复与安全加固版本，并优化了大量文档细节，重大新特性将在2.4.x中发布，如：数据脱敏</p> 
<h3 style="text-align:left">新特性</h3> 
<ul> 
 <li>【base】校验框架提供静态方法<code>Validator.getValidatorAndSetParam(Object param)</code>获取参数校验器，无需bean注入</li> 
 <li>【base】校验框架实现分组校验与提供默认分组<code>ValidationGroups</code></li> 
 <li>【base】新增<code>@CarDrivingLicence</code>、<code>@CarVin</code>、<code>@CreditCode</code>、<code>@ZipCode</code>四个校验注解</li> 
 <li>【web】迁移RequestParamUtils实现至ServletUtils，并优化参数获取方式</li> 
 <li>【web】优化ServletUtils内部实现，移除multipart相关类改用hutool提供</li> 
 <li>【jdbc】从<strong>2.3.3</strong>开始使用（强依赖）druid进行连接池管理与SQL解析</li> 
</ul> 
<h3 style="text-align:left">Bug修复</h3> 
<ul> 
 <li>【base】移除actuator配置</li> 
 <li>【web】修复异步线程装饰器在开启ServletAsyncContext时，接口响应被无故追加404异常 <a href="https://gitee.com/yl-yue/yue-library/issues/I3HTAW">#I3HTAW</a></li> 
</ul> 
<h3 style="text-align:left">Maven仓库实际发布版本号</h3> 
<p style="text-align:left"><code>j8.2.3.3</code>、<code>j11.2.3.3</code></p> 
<p style="text-align:left"><a href="https://gitee.com/yl-yue/yue-library/blob/j11.2.3.3/pom.xml"><strong>关键pom.xml依赖：</strong></a></p> 
<table cellspacing="0" style="width:1233px"> 
 <thead> 
  <tr> 
   <th>依赖</th> 
   <th>版本</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">spring-boot</td> 
   <td style="border-color:#dddddd">2.3.10.RELEASE</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">spring-cloud</td> 
   <td style="border-color:#dddddd">Hoxton.SR11</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">spring-cloud-alibaba</td> 
   <td style="border-color:#dddddd">2.2.5.RELEASE</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">hutool</td> 
   <td style="border-color:#dddddd">5.6.3</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">fastjson</td> 
   <td style="border-color:#dddddd">1.2.76</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:left">工程结构</h2> 
<pre style="text-align:left"><code>. yue-library
├── yue-library  父pom
│   ├── yue-library-dependencies  dependencies版本控制
│   ├── yue-library-base          基础库提供了丰富的Java工具包，同时也自动装配了一系列基础Bean等
│   ├── yue-library-base-crypto   基于Hutool实现的加解密模块，提供诸如数据脱敏此类的更多特性
│   ├── yue-library-web           基础库WebMvc实现，用于servlet项目
│   ├── yue-library-webflux       基础库WebFlux实现，用于响应式编程项目（如：SpringCloudGateway）
│   ├── yue-library-<span style="color:#d73a49">data</span>-jdbc     基于SpringJDBC进行二次封装，拥有着强大性能的同时又不失简单、灵活等
│   ├── yue-library-<span style="color:#d73a49">data</span>-redis    基于SpringRedis进行二次封装，更简单灵活，提供全局token与登录相关特性等
│   ├── yue-library-auth-service  基于SpringSecurity进行二次封装，更简单灵活，提供全局token与登录等特性
│   ├── yue-library-auth-client   auth-client为auth-service客户端模块，提供获取当前登录用户状态信息等特性
│   └── yue-library-pay           基于pay-java-parent进行二次封装，让你真正做到一行代码实现支付聚合
├── yue-library-samples  基础库示例
│   ├── yue-library-test                yue-library-web代码测试项目：单元测试、接口测试、代码示例
│   ├── yue-library-test-webflux        yue-library-webflux代码测试项目：单元测试、接口测试、代码示例
│   ├── yue-library-template-simple     yue-library模版：SpringBoot项目模版
│   └── yue-library-template-ssc        yue-library模版：SpringCloud项目模版，SOA共享架构（阿里巴巴中台）
└── yue
</code></pre> 
<h2 style="text-align:left">快速开始</h2> 
<h3 style="text-align:left">引入项目依赖</h3> 
<p style="text-align:left">maven项目，在pom.xml文件中添加如下一段代码，并将<code>$&#123;version&#125;</code>替换为对应版本号：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaven-badges.herokuapp.com%2Fmaven-central%2Fai.ylyue%2Fyue-library-dependencies" target="_blank"><img alt="Maven Central with version prefix filter" src="https://img.shields.io/maven-central/v/ai.ylyue/yue-library/j?style=flat-square" referrerpolicy="no-referrer"></a></p> 
<pre style="text-align:left"><code class="language-xml"><span style="color:#333333"><<span style="color:#22863a">parent</span>></span>
<span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>ai.ylyue<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
<span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>yue-library-dependencies<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
<span style="color:#333333"><<span style="color:#22863a">version</span>></span>$&#123;version&#125;<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">parent</span>></span>
</code></pre> 
<p style="text-align:left">随后引入所需要的模块，如WebMvc项目引入：<code>yue-library-web</code></p> 
<p style="text-align:left">依赖说明：<code>yue-library-base</code>为基础模块，一般情况下不需要单独引入，如：web、data-jdbc、data-redis等模块皆已默认依赖。</p> 
<pre style="text-align:left"><code class="language-xml"><span style="color:#333333"><<span style="color:#22863a">dependencies</span>></span>
<span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
<span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>ai.ylyue<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
<span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>yue-library-web<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
...
<span style="color:#333333"></<span style="color:#22863a">dependencies</span>></span>
</code></pre> 
<h3 style="text-align:left">启动项目</h3> 
<p style="text-align:left">新建一个SpringBoot <code>main</code>方法启动类：</p> 
<pre style="text-align:left"><code class="language-java"><span style="color:#6a737d">@SpringBootApplication</span>
<span style="color:#d73a49">public</span> <span style="color:#d73a49">class</span> <span style="color:#6f42c1">TestApplication</span> &#123;

<span style="color:#d73a49">public</span> <span style="color:#d73a49">static</span> <span style="color:#d73a49">void</span> <span style="color:#6f42c1">main</span>(String[] args) <span style="color:#d73a49">throws</span> Exception &#123;
SpringApplication.run(TestApplication.<span style="color:#d73a49">class</span>, <span style="color:#6f42c1">args</span>);
&#125;

&#125;
</code></pre> 
<p style="text-align:left">写一个测试接口：</p> 
<pre style="text-align:left"><code class="language-java"><span style="color:#032f62">@RestController</span>
<span style="color:#032f62">@RequestMapping</span>(<span style="color:#032f62">"/quickstart"</span>)
public class QuickstartController &#123;

<span style="color:#032f62">@GetMapping</span>(<span style="color:#032f62">"/get"</span>)
public Result<?> get(JSONObject paramJson) &#123;
<span style="color:#d73a49">return</span> <span style="color:#d73a49">ResultInfo</span><span style="color:#6f42c1">.success</span>(paramJson);
&#125;

&#125;
</code></pre> 
<p style="text-align:left">访问接口测试，如：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A8080%2Fquickstart%2Fget" target="_blank">http://localhost:8080/quickstart/get</a></p> 
<pre style="text-align:left"><code class="language-json">&#123;
    <span style="color:#6f42c1">"code"</span>: 200,
    <span style="color:#6f42c1">"msg"</span>: <span style="color:#032f62">"成功"</span>,
    <span style="color:#6f42c1">"flag"</span>: <span style="color:#005cc5">true</span>,
    <span style="color:#6f42c1">"count"</span>: <span style="color:#005cc5">null</span>,
    <span style="color:#6f42c1">"data"</span>: &#123;&#125;
&#125;
</code></pre> 
<p style="text-align:left">上面的代码完全保持了SpringBoot的风格，但又提供了更多特性增强，如：HTTP消息转换器对 <strong>Alibaba Fastjson</strong> 的支持，同时不再区分 <strong>query from-data json</strong> 等传参方式，默认也对 <strong>跨域、时间格式、异常、参数校验</strong> 等常见坑点进行了本土化处理与特性增强。</p> 
<h2 style="text-align:left">对比脚手架</h2> 
<p style="text-align:left">yue-library正在计划提供属于自身的脚手架项目，但相比于单纯的脚手架项目，他更具有以下几点优势：</p> 
<ul> 
 <li>简单易学：优雅的实现各个功能特性，并配备了完善的说明文档</li> 
 <li>轻松引用：不同于脚手架，对于现有的SpringBoot项目也可以引入yue-library</li> 
 <li>更易升级：以spring-boot-starter的方式提供支持，可随时跟进最新稳定版本</li> 
 <li>无需维护：开发者只需专注自身业务逻辑实现，并熟练运用你所使用的特性</li> 
 <li>灵活选取：你可以随时弃用yue-library保留SpringBoot原生使用</li> 
</ul> 
<p style="text-align:left">收藏一波以表支持吧(≧▽≦)/！</p>
                                        </div>
                                      
</div>
            