
---
title: 'Spring Boot 增强库 yue-library 2.3.2 发布，优雅实现密钥交换加解密'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/yl-yue/yue-library/raw/master/docs/_images/logo.png'
author: 开源中国
comments: false
date: Sun, 18 Apr 2021 10:14:00 GMT
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
 <li>内置丰富的JDK工具</li> 
 <li>自动装配了一系列的基础Bean与环境配置项</li> 
 <li>快速构建SpringCloud项目，让微服务变得更简单</li> 
</ul> 
<h2 style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fylyue.cn%2F%23%2Fchangelog" target="_blank">版本更新日志</a></h2> 
<p style="text-align:left">此版本重点实现：<strong>密钥交换加解密</strong>、<strong>增强Bean转换能力</strong>、<strong>JDBC新增Elasticsearch-SQL、达梦、PostgreSQL方言</strong>。</p> 
<h3 style="text-align:left">新特性</h3> 
<ul> 
 <li>【base】ParamUtils提示优化，添加错误原因</li> 
 <li>【base】添加JSONListConverter类型转换器从而支持<code>List<JSONObject></code>类型处理（JDBC实体数据库查询映射时JSONArray格式文本数据不支持映射成<code>List<JSONObject></code>）</li> 
 <li>【base】优化fastjson bean转换的jsonstr识别方式</li> 
 <li>【base】增强DateUtils与规范UUID工具类为IdUtils并优化IdUtils实现</li> 
 <li>【base】增强fastjson JavaBean转换能力，支持Character类型</li> 
 <li>【base】MapUtils增强值提取，支持list根据key提取map提取值支持map、fastjson <a href="https://gitee.com/yl-yue/yue-library/pulls/17">pulls !17</a></li> 
 <li>【crypto】新增重磅特性-密钥交换加密：支持<code>@RequestDecrypt</code>注解实现请求自动解密</li> 
 <li>【crypto】新增重磅特性-密钥交换加密：支持<code>@ResponseEncrypt</code>注解实现响应内容加密</li> 
 <li>【crypto】密钥交换加密：默认提供本地Map与Redis两种交换密钥存储方案</li> 
 <li>【crypto】密钥交换加密：<code>@RequestDecrypt</code>与<code>@ResponseEncrypt</code>注解支持使用交换密钥加密或自定义密钥等特性</li> 
 <li>【web】修复ApiVersion注解minimumVersion值等于的情况下410</li> 
 <li>【web】优化响应结果处理器在标准HTTP状态码时的空值处理</li> 
 <li>【web】新增ServletUtils.getAuthToken()方法，获取请求中的OAuth2 Token</li> 
 <li>【webflux】修复ApiVersion注解minimumVersion值等于的情况下410</li> 
 <li>【jdbc】对jdbc方言实现进行完善与优化，新增Elasticsearch-SQL、达梦、PostgreSQL方言</li> 
 <li>【jdbc】db.queryForObject 自动识别Bean类型与简单类型</li> 
 <li>【jdbc】参数美化增强支持JSONArray数据类型与<code>List<JSONObject></code>数据类型</li> 
 <li>【jdbc】优化多行查询结果转换为单行查询结果实现</li> 
 <li>【jdbc】所有mappedClass查询方法自动识别所需RowMapper类型，实现JavaBean、map、基本类型结果自动匹配</li> 
 <li>【jdbc】规范内部部分常量命名与移除分页中不优雅的泛型实例PageTVO</li> 
 <li>【jdbc】增强自动方言识别，根据驱动类自动识别所需方言类型</li> 
 <li>【jdbc】默认Db Bean实现根据不同驱动类型，使用对应方言配置</li> 
 <li>【jdbc】优化DAO实现，抽象基础DAO</li> 
 <li>【jdbc】优化所有jdbc方法注释，描述更简洁，表达更清晰，注释更规范</li> 
 <li>【jdbc】删除早期存在的部分过时方法</li> 
 <li>【es】支持配置ConnectTimeout与SocketTimeout，并调大各自默认值为25与15秒</li> 
</ul> 
<h3 style="text-align:left">Bug修复</h3> 
<ul> 
 <li>【base】修复fastjson JavaBean转换BUG <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson%2Fpull%2F3688" target="_blank">#3688</a></li> 
 <li>【jdbc】修复isDataSize()方法可能因为数据库存在多行数据，而返回false的隐患</li> 
 <li>【jdbc】修复因错误测试而删除的参数类型美化（现已支持：Character、JSONObject、LocalDateTime进行特殊转换处理与布尔值映射识别）</li> 
</ul> 
<h3 style="text-align:left">Maven仓库实际发布版本号</h3> 
<p style="text-align:left"><code>j8.2.3.2</code>、<code>j11.2.3.2</code></p> 
<p style="text-align:left"><a href="https://gitee.com/yl-yue/yue-library/blob/j11.2.3.2/pom.xml"><strong>关键pom.xml依赖：</strong></a></p> 
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
   <td style="border-color:#dddddd">2.3.8.RELEASE</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">spring-cloud</td> 
   <td style="border-color:#dddddd">Hoxton.SR10</td> 
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
├── yue-library  基础库
│   ├── yue-library-dependencies  父pom
│   ├── yue-library-base          基础库提供了丰富的Java工具包，同时也自动装配了一系列基础Bean等
│   ├── yue-library-base-crypto   基于Hutool实现的加解密模块，提供诸如数据脱敏此类的更多特性
│   ├── yue-library-web           基础库WebMvc实现，用于servlet项目
│   ├── yue-library-webflux       基础库WebFlux实现，用于响应式编程项目（如：SpringCloudGateway）
│   ├── yue-library-<span style="color:#d73a49">data</span>-jdbc     基于SpringJDBC进行二次封装，拥有着强大性能的同时又不失简单、灵活等
│   ├── yue-library-<span style="color:#d73a49">data</span>-redis    基于SpringRedis进行二次封装，更简单灵活，提供全局token与登录相关特性等
│   ├── yue-library-auth-service  基于SpringSecurity进行二次封装，更简单灵活，提供全局token与登录等特性
│   ├── yue-library-auth-client   auth-client为auth-service客户端模块，提供获取当前登录用户状态信息等特性
│   ├── yue-library-pay           基于pay-java-parent进行二次封装，让你真正做到一行代码实现支付聚合
│   ├── yue-library-cloud-oss
│   └── yue-library-cloud-sms
├── yue-library-samples  基础库示例
│   ├── yue-library-testyue-library代码测试项目：单元测试、接口测试、代码示例
│   ├── yue-library-test-webfluxyue-library-webflux代码测试项目：单元测试、接口测试、代码示例
│   ├── yue-library-template-simpleyue-library模版：SpringBoot项目模版
│   └── yue-library-template-sscyue-library模版：SpringCloud项目模版，SOA共享架构（阿里巴巴中台）
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
<h2 style="text-align:left">密钥交换</h2> 
<p style="text-align:left">密钥交换加密可以实现如下几个特性：</p> 
<ul> 
 <li>每次会话的密钥时随机的，客户端与服务端事先无需约定</li> 
 <li>密钥未直接存储在客户端与服务端中，避免了泄露风险</li> 
 <li>密钥交换过程中，密钥的传输是加密的</li> 
</ul> 
<h3 style="text-align:left">密钥交换流程</h3> 
<p style="text-align:left"><img alt="密钥交换流程" src="https://ylyue.cn/base-crypto/%E5%AF%86%E9%92%A5%E4%BA%A4%E6%8D%A2%E5%8A%A0%E5%AF%86_files/1.jpg" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><strong>密钥交换步骤一：客户端请求传输加密公钥</strong></p> 
<ol> 
 <li>客户端使用密钥存储key，请求获得服务端公钥（用于步骤二请求加密）</li> 
</ol> 
<ul> 
 <li>密钥存储key：作为会话唯一键，在步骤一、步骤二、步骤三中属于必填参数</li> 
 <li>密钥存储key：在用户未登录时一般会随机生成一个UUID，用户登陆后再用token作为别名</li> 
 <li>密钥存储key：用户已登录情况，一般会以用户本次会话token作为存储key</li> 
</ul> 
<ol> 
 <li>服务端收到请求后，生成用于后续传输加解密的公私钥并绑定存储key</li> 
 <li>服务端将生成的公钥返回给客户端</li> 
</ol> 
<p style="text-align:left"><strong>密钥交换步骤二：客户端请求最终交换密钥</strong></p> 
<ol> 
 <li>客户端获得服务端的公钥后，创建客户端自身的公私钥</li> 
 <li>客户端使用<strong>服务端的公钥</strong>加密<strong>自身生成的公钥</strong>，向服务端请求最终的交换密钥</li> 
 <li>服务端使用私钥解密获得客户端公钥</li> 
 <li>服务端生成最终交换密钥，并使用客户端公钥进行响应加密</li> 
 <li>客户端获得加密的交换密钥后使用<strong>客户端私钥解密</strong>，获得交换密钥</li> 
</ol> 
<p style="text-align:left"><strong>密钥交换步骤三（可选）：客户端为服务端密钥的存储key添加别名</strong></p> 
<ul> 
 <li>适用场景：</li> 
 <li>步骤一时用户未登录，使用临时的UUID作为服务端密钥存储key，用户登录后想使用token作为密钥存储key，方便后续传输</li> 
</ul> 
<p style="text-align:left"><strong>使用交换密钥加解密</strong></p> 
<ol> 
 <li>客户端获得交换密钥后，请求需要参数加密的接口时，以约定的方式带上密钥存储key，并加密请求参数</li> 
</ol> 
<ul> 
 <li>约定方式：默认为OAuth2 Token认证，故：若步骤一使用UUID作为存储key，需将token添加为存储别名</li> 
 <li>约定方式：除默认方式外支持：Header传参约定、URL Param传参约定（具体传参key为服务端定义，默认key值：<code>Yue-ExchangeKey-StorageKey</code>）</li> 
</ul> 
<ol> 
 <li>服务端解密参数处理业务逻辑后，使用<code>@ResponseEncrypt</code>注解自动加密响应的data参数</li> 
 <li>客户端解密响应结果</li> 
</ol> 
<h3 style="text-align:left">接口说明</h3> 
<p style="text-align:left"><strong>默认算法名称</strong></p> 
<ul> 
 <li>RSA_AES：</li> 
</ul> 
<pre style="text-align:left"><code class="language-java"><span style="color:#6a737d">/** RSA算法，此算法用了默认补位方式为RSA/ECB/PKCS1Padding */</span>
<span style="color:#d73a49">RSA_ECB_PKCS1</span>(<span style="color:#032f62">"RSA/ECB/PKCS1Padding"</span>), 

<span style="color:#6a737d">/** 默认的AES加密方式：AES/ECB/PKCS5Padding */</span>
<span style="color:#d73a49">AES</span>(<span style="color:#032f62">"AES"</span>), 
</code></pre> 
<ul> 
 <li>SM2_SM4</li> 
</ul> 
<pre style="text-align:left"><code class="language-java"><span style="color:#6a737d">/**
 * 算法EC
 */</span>
private <span style="color:#d73a49">static</span> <span style="color:#d73a49">final</span> String ALGORITHM_SM2 = <span style="color:#032f62">"SM2"</span>;

public <span style="color:#d73a49">static</span> <span style="color:#d73a49">final</span> String ALGORITHM_NAME = <span style="color:#032f62">"SM4"</span>;
</code></pre> 
<p style="text-align:left"><strong>密钥交换-第一步：获得加密公钥</strong></p> 
<blockquote> 
 <p>接口地址：POST /open/v2.3/keyExchange/&#123;storageKey&#125;</p> 
</blockquote> 
<table cellspacing="0" style="width:1233px"> 
 <thead> 
  <tr> 
   <th>参数</th> 
   <th>说明</th> 
   <th>参数示例</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">storageKey</td> 
   <td style="border-color:#dddddd">RESTful路径参数，密钥存储key</td> 
   <td style="border-color:#dddddd">23ef1f9418e84cc884187e1720ac1529</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">exchangeKeyType</td> 
   <td style="border-color:#dddddd">交换密钥类型，枚举值：RSA_AES、SM2_SM4</td> 
   <td style="border-color:#dddddd">RSA_AES</td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:left"><strong>密钥交换-第二步：获得交换密钥</strong></p> 
<blockquote> 
 <p>接口地址：POST /open/v2.3/keyExchange/&#123;storageKey&#125;</p> 
</blockquote> 
<table cellspacing="0" style="width:1233px"> 
 <thead> 
  <tr> 
   <th>参数</th> 
   <th>说明</th> 
   <th>参数示例</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">storageKey</td> 
   <td style="border-color:#dddddd">RESTful路径参数，密钥存储key</td> 
   <td style="border-color:#dddddd">23ef1f9418e84cc884187e1720ac1529</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">exchangeKeyType</td> 
   <td style="border-color:#dddddd">交换密钥类型，枚举值：RSA_AES、SM2_SM4</td> 
   <td style="border-color:#dddddd">RSA_AES</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">encryptedClientPublicKey</td> 
   <td style="border-color:#dddddd">使用服务端公钥加密的客户端公钥（encryptBase64）</td> 
   <td style="border-color:#dddddd"><code>SsowXMaZfQiec39 ..略n.. uv/DbVr6gslrjY3Q==</code></td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:left"><strong>密钥交换-第三步：添加存储key别名</strong></p> 
<blockquote> 
 <p>接口地址：POST /open/v2.3/keyExchange/&#123;storageKey&#125;/addAlias</p> 
</blockquote> 
<table cellspacing="0" style="width:1233px"> 
 <thead> 
  <tr> 
   <th>参数</th> 
   <th>说明</th> 
   <th>参数示例</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">storageKey</td> 
   <td style="border-color:#dddddd">RESTful路径参数，密钥存储key</td> 
   <td style="border-color:#dddddd">23ef1f9418e84cc884187e1720ac1529</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">storageKeyAlias</td> 
   <td style="border-color:#dddddd">存储别名</td> 
   <td style="border-color:#dddddd">cbf55767c47e4d4e9feb90cfa2bdf5aa</td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="text-align:left">配置</h3> 
<pre style="text-align:left"><code class="language-java"><span style="color:#6f42c1">yue:</span> 
  <span style="color:#6f42c1">crypto:</span>
    <span style="color:#6f42c1">key-exchange:</span>
      <span style="color:#6f42c1">enabled:</span> <span style="color:#005cc5">true</span> <span style="color:#6a737d"># 默认false，启用密钥交换</span>
      <span style="color:#6f42c1">key-exchange-storage-type:</span> <span style="color:#032f62">redis</span> <span style="color:#6a737d"># 使用redis作为密钥交换存储类型</span>
</code></pre> 
<h3 style="text-align:left">注解使用说明</h3> 
<p style="text-align:left"><code>@RequestDecrypt</code>请求解密注解：</p> 
<ul> 
 <li>必须与<code>@RequestBody</code>注解一同使用</li> 
 <li><code>@RequestBody</code>注解只支持使用Body传参，并映射为实体参数。</li> 
 <li><code>Content-Type=application/json;charset=UTF-8</code></li> 
</ul> 
<pre style="text-align:left"><code class="language-java">    <span style="color:#032f62">@RequestDecrypt</span>
    <span style="color:#032f62">@PostMapping</span>(<span style="color:#032f62">"/decrypt"</span>)
    public Result<?> decrypt(<span style="color:#032f62">@RequestBody</span> UserIPO userIPO) &#123;
        <span style="color:#d73a49">return</span> <span style="color:#d73a49">R</span><span style="color:#6f42c1">.success</span>(userIPO);
    &#125;
</code></pre> 
<p style="text-align:left"><code>@ResponseEncrypt</code>响应加密注解：</p> 
<ul> 
 <li>必须与<code>@ResponseBody</code>注解一同使用，<code>@RestController</code>注解默认已集成<code>@ResponseBody</code></li> 
 <li>必须使用<code>Result</code>作为返回类型，并且加密的是data参数</li> 
</ul> 
<pre style="text-align:left"><code class="language-java">    <span style="color:#032f62">@ResponseEncrypt</span>
    <span style="color:#032f62">@GetMapping</span>(<span style="color:#032f62">"/&#123;encrypt&#125;"</span>)
    public Result<?> encrypt(<span style="color:#032f62">@PathVariable</span> String encrypt) &#123;
        <span style="color:#d73a49">return</span> <span style="color:#d73a49">R</span><span style="color:#6f42c1">.success</span>(encrypt);
    &#125;
</code></pre> 
<p style="text-align:left">收藏一波以表支持吧(≧▽≦)/！</p>
                                        </div>
                                      
</div>
            