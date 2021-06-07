
---
title: 'SpringBoot 增强库 yue-library 2.4.0 发布，优雅的实现接口幂等性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/yl-yue/yue-library/raw/master/docs/_images/logo.png'
author: 开源中国
comments: false
date: Mon, 07 Jun 2021 08:36:00 GMT
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
<ul> 
 <li>主要变更：使用SpringBoot2.4新的配置文件机制，提供默认的优化配置实现。</li> 
 <li>主要新特性：使用注解<code>@ApiIdempotent</code>可优雅的实现接口幂等性（数据脱敏功能延迟到2.4.1中发布）</li> 
</ul> 
<h3 style="text-align:left">新特性</h3> 
<ul> 
 <li>【base】新增<code>@CarDrivingLicence</code>、<code>@CarVin</code>、<code>@CreditCode</code>、<code>@ZipCode</code>四个校验注解</li> 
 <li>【base】迁移actuator配置至auth模块，添加actuator配置安全</li> 
 <li>【base】actuator端点默认使用32222端口进行访问，与API服务端口进行区分，保持良好的安全忧患意识</li> 
 <li>【base】网络代理，额外不代理地址默认添加所有内网网段</li> 
 <li>【jdbc】完善逻辑删除，delete_time条件追加时判断sql中是否存在delete_time否则不再追加</li> 
 <li>【redis】新增API接口幂等性优雅实现，使用<code>@ApiIdempotent</code>注解标注接口需要进行幂等性校验</li> 
 <li>【test】新增模块分离测试</li> 
 <li>【docs】新增安全规约</li> 
 <li>【docs】优化异步线程池示例与完善文档</li> 
 <li>【docs】完善逻辑删除文档</li> 
 <li>【docs】添加分布式缓存示例与文档</li> 
 <li>【docs】完善分布式锁与接口幂等性文档</li> 
 <li>【docs】完善POJO与Lombok的使用说明</li> 
 <li>【docs】添加类型转换器Bean别名规范</li> 
 <li>【docs】完善JavaBean参数解析器文档，提示IPO中有无参构造时，解析List<String>类型需传标准是数组字符串</li> 
 <li>【other】删除部分早已标记为失效的方法</li> 
</ul> 
<h3 style="text-align:left">Bug修复</h3> 
<ul> 
 <li>【web】解决SpringBoot2.4版本新出现的跨域问题 <a href="https://gitee.com/yl-yue/yue-library/issues/I3OV7B">#I3OV7B</a></li> 
 <li>【web】修复异步线程装饰器在开启ServletAsyncContext时，接口响应被无故追加404异常 <a href="https://gitee.com/yl-yue/yue-library/issues/I3HTAW">#I3HTAW</a></li> 
</ul> 
<h3 style="text-align:left">Maven仓库实际发布版本号</h3> 
<p style="text-align:left"><code>j8.2.4.0</code>、<code>j11.2.4.0</code></p> 
<p style="text-align:left"><a href="https://gitee.com/yl-yue/yue-library/blob/j11.2.4.0/pom.xml"><strong>关键pom.xml依赖：</strong></a></p> 
<table cellspacing="0" style="width:913px"> 
 <thead> 
  <tr> 
   <th>依赖</th> 
   <th>版本</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">spring-boot</td> 
   <td style="border-color:#dddddd">2.4.3</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">spring-cloud</td> 
   <td style="border-color:#dddddd">2020.0.2</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">spring-cloud-alibaba</td> 
   <td style="border-color:#dddddd">2021.1</td> 
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
├── yue-library                       
│   ├── yue-library-dependencies      dependencies版本控制
│   ├── yue-library-base              基础核心模块，提供丰富的Java工具类库、接口参数校验、类型转换器等
│   ├── yue-library-base-crypto       加解密模块，提供对称、非对称和摘要算法、密钥交换加解密等
│   ├── yue-library-web               WebMvc模块，servlet编程，提供请求与响应参数的包装与解析等
│   ├── yue-library-webflux           WebFlux实现，响应式编程（如：SpringCloudGateway）
│   ├── yue-library-<span style="color:#d73a49">data</span>-jdbc         ORM框架，基于SpringJdbc，拥有着强大性能的同时又不失简单灵活等
│   ├── yue-library-<span style="color:#d73a49">data</span>-redis        Redis客户端，基于SpringRedis，更简单灵活，提供分布式锁等
│   ├── yue-library-auth-service      OAuth2认证模块，基于SpringSecurity，更简单灵活，提供全局token与登录等
│   ├── yue-library-auth-client       OAuth2客户端模块，提供获取当前登录用户状态信息等
│   └── yue-library-pay               支付模块，基于pay-java-parent，让你真正做到一行代码实现支付聚合
└── yue-library-samples               
    ├── yue-library-test              web测试项目，提供详细的特性使用示例、接口单元测试
    ├── yue-library-test-webflux      webflux测试项目，提供详细的特性使用示例、接口单元测试
    ├── yue-library-template-boot     SpringBoot项目模版，提供快速开发示例
    └── yue-library-template-cloud    SpringCloud项目模版，SOA共享架构（阿里巴巴中台）
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
<p style="text-align:left">上述代码完全保持了SpringBoot的风格，但又使用到了yue-library的增强特性，如：</p> 
<ul> 
 <li>HTTP消息转换器支持使用Alibaba Fastjson作为参数获取对象</li> 
 <li>请求参数智能解析，无需再为URL query-string、Body from-data、Body application/json传参方式烦恼</li> 
 <li>错误时会对异常进行统一处理，响应RESTful风格的错误提示</li> 
 <li>支持前端跨域请求</li> 
</ul> 
<p style="text-align:left">当然除了这些已使用到的特性之外，你还可以尝试如：响应时间类型时自动格式化、请求参数校验、API接口版本控制、反复读取Servlet输入流等。 并且在<code>yue-library-samples</code>目录下，存放着不同架构类型的示例模板，你可以根据自身需求选择，从而快速上手。</p> 
<h2 style="text-align:left">接口幂等性</h2> 
<h3 style="text-align:left">什么是幂等性（引用自OCP项目文档）</h3> 
<p style="text-align:left">HTTP/1.1中对幂等性的定义是：一次和多次请求某一个资源<strong>对于资源本身</strong>应该具有同样的结果（网络超时等问题除外）。也就是说，<strong>其任意多次执行对资源本身所产生的影响均与一次执行的影响相同</strong>。</p> 
<p style="text-align:left">简单来说，是指无论调用多少次都不会有不同结果的 HTTP 方法。</p> 
<h3 style="text-align:left">什么情况下需要幂等</h3> 
<p style="text-align:left">业务开发中，经常会遇到重复提交的情况，无论是由于网络问题无法收到请求结果而重新发起请求，或是前端的操作抖动而造成重复提交情况。 在交易系统，支付系统这种重复提交造成的问题有尤其明显，比如：</p> 
<ol> 
 <li>用户在APP上连续点击了多次提交订单，后台应该只产生一个订单；</li> 
 <li>向支付宝发起支付请求，由于网络问题或系统BUG重发，支付宝应该只扣一次钱。 <strong>很显然，声明幂等的服务认为，外部调用者会存在多次调用的情况，为了防止外部多次调用对系统数据状态的发生多次改变，将服务设计成幂等。</strong></li> 
</ol> 
<h3 style="text-align:left">开始使用</h3> 
<p style="text-align:left">实现接口幂等性的方式有很多种，我比较推崇使用分布式锁或version令牌的方式，而上面我们已经介绍了分布式锁的使用，那么下面我们就来介绍下version令牌的实现与如何使用。</p> 
<h4 style="text-align:left">实现流程</h4> 
<p style="text-align:left">客户端第一次请求：</p> 
<ul> 
 <li>客户端发起请求获得version令牌</li> 
 <li>服务端生成令牌并将之存入redis中，然后将生成的令牌返回给客户端。</li> 
</ul> 
<p style="text-align:left">客户端第二次请求：</p> 
<ul> 
 <li>客户端将拿到的version令牌携带在，将要请求的业务接口中</li> 
 <li>服务端校验客户端是否携带令牌与令牌是否过期</li> 
</ul> 
<h4 style="text-align:left">后端编码</h4> 
<ol> 
 <li>开启接口幂等性校验</li> 
</ol> 
<pre style="text-align:left"><code class="language-yml"><span style="color:#6f42c1">yue:</span>
  <span style="color:#6f42c1">redis:</span>
    <span style="color:#6f42c1">api-idempotent:</span>
      <span style="color:#6f42c1">enabled:</span> <span style="color:#005cc5">true</span>
</code></pre> 
<ol> 
 <li>在需要进行接口幂等性校验的接口加上<code>@ApiIdempotent</code>注解</li> 
</ol> 
<pre style="text-align:left"><code class="language-java"><span style="color:#032f62">@ApiIdempotent</span>
<span style="color:#032f62">@PostMapping</span>(<span style="color:#032f62">"/test"</span>)
public Result<?> test(JSONObject paramJson) &#123;
<span style="color:#d73a49">return</span> <span style="color:#d73a49">R</span><span style="color:#6f42c1">.success</span>(paramJson);
&#125;
</code></pre> 
<h4 style="text-align:left">前端调用</h4> 
<ol> 
 <li>请求获取version令牌</li> 
</ol> 
<blockquote> 
 <p>接口地址：GET /open/v2.3/apiIdempotent/getVersion</p> 
</blockquote> 
<p style="text-align:left">正确响应示例：</p> 
<pre style="text-align:left"><code class="language-json">&#123;
    <span style="color:#6f42c1">"code"</span>: 200,
    <span style="color:#6f42c1">"msg"</span>: <span style="color:#032f62">"成功"</span>,
    <span style="color:#6f42c1">"flag"</span>: <span style="color:#005cc5">true</span>,
    <span style="color:#6f42c1">"count"</span>: <span style="color:#005cc5">null</span>,
    <span style="color:#6f42c1">"data"</span>: <span style="color:#032f62">"c4ac1fc37f3c44c2bc5f14fdbd0a1b27"</span>
&#125;
</code></pre> 
<ol> 
 <li>将获取到的version令牌，携带在需要幂等性验证的接口中请求</li> 
</ol> 
<ul> 
 <li>如果前端未携带<code>apiIdempotentVersion</code>参数访问需要进行幂等性校验的接口时，会抛出幂等性错误提示</li> 
 <li><code>apiIdempotentVersion</code>参数推荐放在header中</li> 
 <li>一个令牌只能被使用一次</li> 
</ul> 
<p style="text-align:left">错误请求时的响应示例：</p> 
<pre style="text-align:left"><code class="language-json">&#123;
    <span style="color:#6f42c1">"code"</span>: 600,
    <span style="color:#6f42c1">"msg"</span>: <span style="color:#032f62">"请勿重复操作"</span>,
    <span style="color:#6f42c1">"flag"</span>: <span style="color:#005cc5">false</span>,
    <span style="color:#6f42c1">"count"</span>: <span style="color:#005cc5">null</span>,
    <span style="color:#6f42c1">"data"</span>: <span style="color:#032f62">"【幂等性】幂等校验失败，apiIdempotentVersion 参数已失效，当前 value: 9b94ca639d3e49f489583a8719a637ac"</span>
&#125;
</code></pre> 
<h3 style="text-align:left">注解说明</h3> 
<p style="text-align:left"><code>@ApiIdempotent</code>接口幂等性注解：</p> 
<ul> 
 <li>被此元素注解的接口，表示需要进行幂等性校验</li> 
 <li>前端请求被此元素注解的接口时，必须携带<code>apiIdempotentVersion</code>参数</li> 
 <li><code>apiIdempotentVersion</code>参数值，需要调用<code>getVersion</code>接口预先获取，获得的值只可被使用一次</li> 
</ul> 
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
            