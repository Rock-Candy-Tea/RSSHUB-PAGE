
---
title: 'SpringBoot 增强库 yue-library 2.6.0 发布，数据脱敏、数据审计、数据填充'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/yl-yue/yue-library/raw/master/docs/_images/logo.png'
author: 开源中国
comments: false
date: Wed, 11 May 2022 08:39:00 GMT
thumbnail: 'https://gitee.com/yl-yue/yue-library/raw/master/docs/_images/logo.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="logo" src="https://gitee.com/yl-yue/yue-library/raw/master/docs/_images/logo.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">yue-library简介</h2> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">yue-library是一个基于SpringBoot封装的增强库</p> 
</blockquote> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>丰富的Java工具类库</li> 
 <li>优越的ORM框架</li> 
 <li>优雅的业务封装</li> 
 <li>优化的Spring环境配置</li> 
 <li>完善的规约限制</li> 
 <li>配套的代码生成平台</li> 
 <li>安稳贴切的开源架构方案</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fylyue.cn%2F%23%2Fchangelog" target="_blank">版本更新日志</a></h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>主要变更：升级SpringBoot到2.6.x，实现依赖优化与版本控制，加入grpc与plumelog，优化逻辑删除与物理删除分离</li> 
 <li>主要新特性：数据脱敏、数据审计、数据填充</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">新特性</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>【base】移除过期的UUIDUtils，用IdUtils代替</li> 
 <li>【jdbc】新增数据脱敏特性，请求加密，响应解密</li> 
 <li>【jdbc】数据脱敏：支持全局密钥配置于表级密钥配置，支持对表中某个字段配置</li> 
 <li>【jdbc】数据脱敏：支持AES、SM4(国密)、自定义加密机等用于脱敏处理</li> 
 <li>【jdbc】新增数据审计特性，增删改操作自动记录操作人</li> 
 <li>【jdbc】数据审计：支持使用配置一键开关需要进行审计的表、支持反向配置不审计的表</li> 
 <li>【jdbc】数据审计：支持自定义审计字段、审计用户</li> 
 <li>【jdbc】数据审计：规范数据审计字段命名并增加创建人、更新人、删除人为默认审计字段</li> 
 <li>【jdbc】新增数据填充特性，用于UUID，租户ID自动填充</li> 
 <li>【jdbc】数据填充：支持使用配置一键开关需要进行填充的表、支持反向配置不填充的表</li> 
 <li>【jdbc】数据填充：支持数据新增时填充，数据更新时填充</li> 
 <li>【jdbc】逻辑删除：完善逻辑删除与物理删除彻底分离，规范逻辑删除方法</li> 
 <li>【jdbc】新增insertAndReturnUuid()方法：插入时返回uuid</li> 
 <li>【jdbc】新增insertAndReturnFields()方法：插入时自定义返回需要的字段</li> 
 <li>【docs】完善jdbc文档，新增配置示例文档、db boolen示例、打印可执行SQL示例、基础的DDL表结构示例、添加Spring JDBC教程</li> 
 <li>【docs】完善数据库设计与交付规约：数据库枚举规约、多租户介绍</li> 
 <li>【docs】完善服务端规约：提供IDE配置模板</li> 
 <li>【docs】完善grpc规约：proto规约、工程结构规范、工程依赖规约、rpc接口版本控制规约</li> 
 <li>【docs】完善服务端工程结构规约：包名规约、Service/DAO层方法命名规约、POJO领域模型命名规约</li> 
 <li>【template-boot】优化并完善示例项目，上手更简单直观</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Bug修复</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>【template-boot】修正因SpringBoot2.4版本新的配置文件机制，导致的启动失败<span> </span><a href="https://gitee.com/yl-yue/yue-library/issues/I40ONA">#I40ONA</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Maven关键依赖库</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/yl-yue/yue-library/blob/j11.2.6.0/pom.xml"><strong>👉Maven详细依赖定义见pom.xml文件</strong></a></p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:1233px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>依赖库</th> 
   <th>依赖版本</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">spring-boot</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">2.6.3</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">spring-cloud</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">2021.0.1</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">spring-cloud-alibaba</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">2021.0.1.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">hutool</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">5.7.22</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">fastjson</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">1.2.79</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:left">工程结构</h2> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>. yue-library
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
<h2 style="margin-left:0; margin-right:0; text-align:left">快速开始</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">引入项目依赖</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">maven项目，在pom.xml文件中添加如下一段代码，并将<code>$&#123;version&#125;</code>替换为对应版本号：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaven-badges.herokuapp.com%2Fmaven-central%2Fai.ylyue%2Fyue-library-dependencies" target="_blank"><img alt="Maven Central with version prefix filter" src="https://img.shields.io/maven-central/v/ai.ylyue/yue-library/j?style=flat-square" referrerpolicy="no-referrer"></a></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-xml"><span style="color:#333333"><<span style="color:#22863a">parent</span>></span>
<span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>ai.ylyue<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
<span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>yue-library-dependencies<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
<span style="color:#333333"><<span style="color:#22863a">version</span>></span>$&#123;version&#125;<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">parent</span>></span>
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">随后引入所需要的模块，如WebMvc项目引入：<code>yue-library-web</code></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">依赖说明：<code>yue-library-base</code>为基础模块，一般情况下不需要单独引入，如：web、data-jdbc、data-redis等模块皆已默认依赖。</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-xml"><span style="color:#333333"><<span style="color:#22863a">dependencies</span>></span>
<span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
<span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>ai.ylyue<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
<span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>yue-library-web<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
...
<span style="color:#333333"></<span style="color:#22863a">dependencies</span>></span>
</code></pre> 
<h3 style="margin-left:0; margin-right:0; text-align:left">启动项目</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新建一个SpringBoot<span> </span><code>main</code>方法启动类：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"><span style="color:#6a737d">@SpringBootApplication</span>
<span style="color:#d73a49">public</span> <span><span style="color:#d73a49">class</span> <span style="color:#6f42c1">TestApplication</span> </span>&#123;

<span><span style="color:#d73a49">public</span> <span style="color:#d73a49">static</span> <span style="color:#d73a49">void</span> <span style="color:#6f42c1">main</span><span>(String[] args)</span> <span style="color:#d73a49">throws</span> Exception </span>&#123;
SpringApplication.run(TestApplication<span>.<span style="color:#d73a49">class</span>, <span style="color:#6f42c1">args</span>)</span>;
&#125;

&#125;
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">写一个测试接口：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"><span style="color:#032f62">@RestController</span>
<span style="color:#032f62">@RequestMapping</span>(<span style="color:#032f62">"/quickstart"</span>)
public class QuickstartController &#123;

<span style="color:#032f62">@GetMapping</span>(<span style="color:#032f62">"/get"</span>)
public Result<?> get(JSONObject paramJson) &#123;
<span style="color:#d73a49">return</span> <span style="color:#d73a49">ResultInfo</span><span style="color:#6f42c1">.success</span>(paramJson);
&#125;

&#125;
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">访问接口测试，如：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A8080%2Fquickstart%2Fget" target="_blank">http://localhost:8080/quickstart/get</a></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-json">&#123;
    <span style="color:#6f42c1">"code"</span>: <span>200</span>,
    <span style="color:#6f42c1">"msg"</span>: <span style="color:#032f62">"成功"</span>,
    <span style="color:#6f42c1">"flag"</span>: <span style="color:#005cc5">true</span>,
    <span style="color:#6f42c1">"count"</span>: <span style="color:#005cc5">null</span>,
    <span style="color:#6f42c1">"data"</span>: &#123;&#125;
&#125;
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">上述代码完全保持了SpringBoot的风格，但又使用到了yue-library的增强特性，如：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>HTTP消息转换器支持使用Alibaba Fastjson作为参数获取对象</li> 
 <li>请求参数智能解析，无需再为URL query-string、Body from-data、Body application/json传参方式烦恼</li> 
 <li>错误时会对异常进行统一处理，响应RESTful风格的错误提示</li> 
 <li>支持前端跨域请求</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">当然除了这些已使用到的特性之外，你还可以尝试如：响应时间类型时自动格式化、请求参数校验、API接口版本控制、反复读取Servlet输入流等。 并且在<code>yue-library-samples</code>目录下，存放着不同架构类型的示例模板，你可以根据自身需求选择，从而快速上手。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">数据脱敏</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">数据脱敏作为安全层面的大范围话题，包含：数据存储加密、数据展示脱敏等多方面，这里主要实现的是数据存储加密的优雅解决方案。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">数据存储加密解决方案实现，一般分为直接开干方式与优雅实现两种：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>直接开干方式，无非依托于程序员自身，对业务字段进行单独处理，大家实现方式不一，水平不一，实现容易维护苦难</li> 
 <li>优雅实现依托于技术框架底层实现，对需要的字段进行存储加密取出解密，可以定制不同字段不同加密方案，相对优雅简洁少操心</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">应用场景</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">数据存储加解密的实现一般又分为两种，不可逆与对称加密。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>不可逆一般用于像用户密码这样的场景，只需匹配查询，无需解密查看。需求量较小，开发者一般自行处理</li> 
 <li>对称加密大量用于像手机号、身份证号、邮箱等数据，进行存储加密，业务字段多繁杂，不仅需要查询加密可逆，又需保障安全，不能只使用一种加密算法</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">yue-library解决的就是需要大量对称加解密处理的场景，不同的字段可才有不同的密钥与加密算法，存储自动加密，查询自动匹配与解密。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">使用限制</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><code>jdbcQueryxxx</code>开头的查询方法暂时不支持查询参数自动加密匹配，因为SQL中使用<code>?</code>作为占位符，无法解析具体第几个参数是需要加密的</p> 
</blockquote> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><code>queryForxxx</code>开头的查询方法暂时不支持查询参数自动加密匹配，因为这是基础查询方法，容易出现多重加密错误。 我们可以采用调用<code>public void dataEncrypt(String tableName, JSONObject... paramJsons)</code>方法，将参数实现处理，然后传入到<code>queryForxxx</code>方法中，解决此问题。</p> 
</blockquote> 
<h3 style="margin-left:0; margin-right:0; text-align:left">如何使用</h3> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>配置脱敏字段与加密算法</li> 
</ol> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-yml"><span style="color:#6f42c1">yue:</span>
  <span style="color:#6f42c1">jdbc:</span>
    <span style="color:#6f42c1">data-encrypt-algorithm:</span> <span style="color:#032f62">AES</span>            <span style="color:#6a737d"># 缺省数据加密算法（仅当在表级未配置单独的加密算法时，以缺省值的方式生效）</span>
    <span style="color:#6f42c1">data-encrypt-key:</span> <span>1234567890123456</span>     <span style="color:#6a737d"># 缺省数据加密密钥（仅当在表级未配置单独的加密密钥时，以缺省值的方式生效）</span>
    <span style="color:#6f42c1">data-encrypt-configs:</span>                  <span style="color:#6a737d"># 数据加密配置（key：表名，value：数据加密规则）</span>
      <span style="color:#6f42c1">data_encrypt:</span>                        <span style="color:#6a737d"># 数据库对应的表名</span>
        <span style="color:#6f42c1">data-encrypt-algorithm:</span> <span style="color:#032f62">AES</span>        <span style="color:#6a737d"># 当前表加密算法（未设置使用缺省值）</span>
        <span style="color:#6f42c1">data-encrypt-key:</span> <span>1234567890123455</span> <span style="color:#6a737d"># 当前表加密密钥（未设置使用缺省值）</span>
        <span style="color:#6f42c1">fieldNames:</span>                        <span style="color:#6a737d"># 加密字段</span>
          <span style="color:#005cc5">-</span> <span style="color:#032f62">cellphone</span>
          <span style="color:#005cc5">-</span> <span style="color:#032f62">password</span>
      <span style="color:#6f42c1">data_encrypt_2:</span>                      <span style="color:#6a737d"># 数据库对应的表名</span>
        <span style="color:#6f42c1">fieldNames:</span>                        <span style="color:#6a737d"># 加密字段</span>
          <span style="color:#005cc5">-</span> <span style="color:#032f62">email</span>
          <span style="color:#005cc5">-</span> <span style="color:#032f62">password</span>
</code></pre> 
<ol start="2" style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>使用测试</li> 
</ol> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>使用<code>db.insertXXX()</code>方法测试加密存储</li> 
 <li>使用<code>db.deleteXXX()</code>方法测试条件自动加密匹配</li> 
 <li>使用<code>db.updateXXX()</code>方法测试条件自动加密匹配与更新内容加密存储</li> 
 <li>使用<code>db.getXXX()</code>、<code>db.listXXX()</code>、<code>db.pageXXX()</code>方法测试条件自动加密匹配查，存储数据自动解密</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">查询自动解密</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">查询自动解密，只支持DO实体类映射方式，并且类上面需要使用<code>org.springframework.data.relational.core.mapping.@Table</code>注解声明解密表名，如下：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"><span style="color:#6a737d">@Table</span>(<span style="color:#032f62">"data_encrypt"</span>)
<span style="color:#d73a49">public</span> <span><span style="color:#d73a49">class</span> <span style="color:#6f42c1">DataEncryptDO</span> <span style="color:#d73a49">extends</span> <span style="color:#6f42c1">BaseCamelCaseDO</span> </span>&#123;
&#125;
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">当我们使用Json查询数据时，可以调用<code>public void dataDecrypt(String tableName, JSONObject... resultJsons)</code>方法，将结果进行解密。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">数据审计</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">数据审计用于记录对数据执行增删改动作的操作人，结合数据版本控制可达到数据360安全审计效果，结合操作日志可对一起链路操作进行追踪溯源。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">如何使用</h3> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>添加配置</li> 
</ol> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-yml"><span style="color:#6f42c1">yue:</span>
  <span style="color:#6f42c1">jdbc:</span>
    <span style="color:#6f42c1">data-audit-table-name-match-enum:</span> <span style="color:#032f62">match</span>                 <span style="color:#6a737d"># 数据审计表名匹配方式</span>
    <span style="color:#6f42c1">data-audit-table-names:</span>                                 <span style="color:#6a737d"># 数据审计表名 </span>
      <span style="color:#005cc5">-</span> <span style="color:#032f62">data_audit</span>
  <span style="color:#005cc5">-</span> <span style="color:#032f62">data_audit2</span>
  <span style="color:#005cc5">-</span> <span style="color:#032f62">data_audit3</span>
</code></pre> 
<ol start="2" style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>提供审计用户信息，实现<code>AuditUserProvider</code>接口并配置为Bean</li> 
</ol> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"><span style="color:#6a737d">@Bean</span>
<span><span style="color:#d73a49">public</span> AuditUserProvider <span style="color:#6f42c1">auditUserProvider</span><span>()</span> </span>&#123;
<span style="color:#d73a49">return</span> <span style="color:#d73a49">new</span> AuditUserProvider() &#123;
<span style="color:#6a737d">// 在你的应用程序中，如何获得当前用户信息，一般从Token中获取</span>
<span style="color:#6a737d">@Override</span>
<span><span style="color:#d73a49">public</span> String <span style="color:#6f42c1">getUser</span><span>()</span> </span>&#123;
<span style="color:#d73a49">return</span> <span style="color:#032f62">"ylyue"</span>;
&#125;

<span style="color:#6a737d">@Override</span>
<span><span style="color:#d73a49">public</span> String <span style="color:#6f42c1">getUserUuid</span><span>()</span> </span>&#123;
<span style="color:#d73a49">return</span> <span style="color:#032f62">"8fb1e1556cc84ba880d5a794e7b5f9e7"</span>;
&#125;
&#125;;
&#125;
</code></pre> 
<ol start="3" style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>测试</li> 
</ol> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>调用<code>db.insertXXX()</code>方法，测试数据创建人审计</li> 
 <li>调用<code>db.deleteLogicXXX()</code>方法，测试数据删除人审计</li> 
 <li>调用<code>db.updateXXX()</code>方法，测试数据更新人审计</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">自定义审计字段名</h3> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-yml"><span style="color:#005cc5">yue</span>:
  <span style="color:#005cc5">jdbc</span>:
    <span style="color:#005cc5">data-audit-properties</span>:
      <span style="color:#005cc5">field-name-create-user</span>: create_user
      <span style="color:#005cc5">field_name_create_user_uuid</span>: create_user_uuid
      <span style="color:#005cc5">field_name_create_time</span>: create_time
      <span style="color:#005cc5">field_name_update_user</span>: update_user
      <span style="color:#005cc5">field_name_update_user_uuid</span>: update_user_uuid
      <span style="color:#005cc5">field_name_update_time</span>: update_time
      <span style="color:#005cc5">field_name_delete_user</span>: delete_user
      <span style="color:#005cc5">field_name_delete_user_uuid</span>: delete_user_uuid
      <span style="color:#005cc5">field_name_delete_time</span>: delete_time
</code></pre> 
<hr> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><strong>数据填充、逻辑删除等新特性见官方文档</strong></p> 
</blockquote> 
<h2 style="margin-left:0; margin-right:0; text-align:left">对比脚手架</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">yue-library正在计划提供属于自身的脚手架项目，但相比于单纯的脚手架项目，他更具有以下几点优势：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>简单易学：优雅的实现各个功能特性，并配备了完善的说明文档</li> 
 <li>轻松引用：不同于脚手架，对于现有的SpringBoot项目也可以引入yue-library</li> 
 <li>更易升级：以spring-boot-starter的方式提供支持，可随时跟进最新稳定版本</li> 
 <li>无需维护：开发者只需专注自身业务逻辑实现，并熟练运用你所使用的特性</li> 
 <li>灵活选取：你可以随时弃用yue-library保留SpringBoot原生使用</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">收藏一波以表支持吧(≧▽≦)/！</p>
                                        </div>
                                      
</div>
            