
---
title: '对标 Spring Boot & Cloud ，轻量框架 Solon 1.5.2 重要发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2060'
author: 开源中国
comments: false
date: Wed, 16 Jun 2021 09:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2060'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">Solon 是一个轻量的Java基础开发框架。强调，<strong>克制 + 简洁 + 开放的原则</strong>；力求，<strong>更小、更快、更自由的体验</strong>。支持：RPC、REST API、MVC、Job、Micro service、WebSocket、Socket 等多种开发模式。短小而精悍！</p> 
<p style="text-align:start">Solon Cloud 是一系列的接口标准和配置规范，算是 Solon 的分布式开发套件方案。</p> 
<h3 style="text-align:start">快速了解Solon的材料：</h3> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4863844">《Solon 特性简集，相较于 Springboot 有什么区别？》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/5039169">《Solon Cloud 分布式服务开发套件清单，感觉受与 Spring Cloud 的不同》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4980834">《Solon 的想法与架构笔记》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/5053423">《Solon 生态插件清单》</a>，目前已有100多个生态插件</p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4784513">《Solon 框架入门系列》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/5061001">《Solon Aop 特色开发系列》</a></p> 
<h4 style="text-align:start">所谓更小：</h4> 
<p style="text-align:start">内核0.1m，最小的接口开发单位0.2m（相较于 Dubbo、Springboot 的依赖包，小到可以乎略不计）</p> 
<h4 style="text-align:start">所谓更快：</h4> 
<p style="text-align:start">本机http helloworld测试，Qps可达12万之多。可参考：《<a href="https://gitee.com/noear/helloworld_wrk_test">helloworld_wrk_test</a>》</p> 
<h4 style="text-align:start">所谓更自由：(代码操控自由)</h4> 
<pre style="text-align:start"><code class="language-java"><em>// 除了注解模式之外，还可以按需手动</em>
<em>//</em>
<em>//手动获取配置（Props 为 Properties 增强版）</em>
Props db = Solon.cfg().getProp(<span style="color:#50a14f">"db"</span>);

<em>//手动获取容器里的Bean</em>
UserService userService = Aop.get(UserService.<span style="color:#a626a4">class</span>);

<em>//手动监听http post请求</em>
Solon.global().post(<span style="color:#50a14f">"/user/update"</span>, x-> userService.updateById(x.paramMap()));

<em>//手动添加个RPC服务</em>
Solon.global().add(<span style="color:#50a14f">"/rpc/"</span>, HelloService.<span style="color:#a626a4">class</span>, <span style="color:#c18401">true</span>);

<em>//手动获取一个RPC服务消费端</em>
HelloService helloService = Nami.builder().create(HelloService.<span style="color:#a626a4">class</span>);

<em>//手动为容器添加组件</em>
Aop.wrapAndPut(DemoService.<span style="color:#a626a4">class</span>);
</code></pre> 
<h4 style="text-align:start">本次版本主要变化：</h4> 
<h3 style="text-align:start">1、部分插件名调整</h3> 
<table cellspacing="0" style="width:960px"> 
 <thead> 
  <tr> 
   <th>原插件</th> 
   <th>升级为新插件</th> 
   <th>原因说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">solon.extend.auth</td> 
   <td style="border-color:#dfe2e5">solon.auth</td> 
   <td style="border-color:#dfe2e5">地位升级</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">solon.extend.data</td> 
   <td style="border-color:#dfe2e5">solon.data</td> 
   <td style="border-color:#dfe2e5">地位升级</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">solon.extend.validation</td> 
   <td style="border-color:#dfe2e5">solon.validation</td> 
   <td style="border-color:#dfe2e5">地位升级</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">solon.extend.jetty.jsp</td> 
   <td style="border-color:#dfe2e5">solon.boot.jetty.add.jsp</td> 
   <td style="border-color:#dfe2e5">增加与 solon.boot.jetty 关联性</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">solon.extend.jetty.websocket</td> 
   <td style="border-color:#dfe2e5">solon.boot.jetty.add.websocket</td> 
   <td style="border-color:#dfe2e5">增加与 solon.boot.jetty 关联性</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">solon.extend.undertow.jsp</td> 
   <td style="border-color:#dfe2e5">solon.boot.undertow.add.jsp</td> 
   <td style="border-color:#dfe2e5">增加与 solon.boot.undertow 关联性</td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="text-align:start">2、部分包名调整</h3> 
<table cellspacing="0" style="width:960px"> 
 <thead> 
  <tr> 
   <th>原包名</th> 
   <th>升级为新包名</th> 
   <th>原因说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">solon.extend.auth.*</td> 
   <td style="border-color:#dfe2e5">solon.auth.*</td> 
   <td style="border-color:#dfe2e5">地位升级</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">solon.extend.validation.*</td> 
   <td style="border-color:#dfe2e5">solon.validation.*</td> 
   <td style="border-color:#dfe2e5">地位升级</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">solon.extend.data.*</td> 
   <td style="border-color:#dfe2e5">solon.data.*</td> 
   <td style="border-color:#dfe2e5">地位升级</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">solon.core.tran.*</td> 
   <td style="border-color:#dfe2e5">solon.data.tran.*</td> 
   <td style="border-color:#dfe2e5">转到 solon.data 统一维护</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">solon.core.cache.*</td> 
   <td style="border-color:#dfe2e5">solon.data.cache.*</td> 
   <td style="border-color:#dfe2e5">转到 solon.data 统一维护</td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="text-align:start">3、solon.validation 插件其它调整与升级</h3> 
<ul> 
 <li>改动 ValidatorManager，由单例模式改为静态模式；并对接口做了优化</li> 
 <li>调整 ValidatorManager::onFailure 更名为 ValidatorManager::setFailureHandler</li> 
 <li>调整 NoRepeatLock 更名为 NoRepeatSubmitChecker（与其它检测器统一为Checker的概念）</li> 
</ul> 
<h3 style="text-align:start">4、solon.validation 插件增加实体验证支持（也可切换为jsr303）</h3> 
<p style="text-align:start">示例：</p> 
<pre style="text-align:start"><code><span style="color:#4078f2">@Valid</span>
<span style="color:#4078f2">@Mapping(<span style="color:#50a14f">"/demo2/valid"</span>)</span>
<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">ValidController</span> &#123;
    <span style="color:#4078f2">@NoRepeatSubmit</span>
    <span style="color:#4078f2">@Mapping(<span style="color:#50a14f">"nrs"</span>)</span>
    <span style="color:#a626a4">public</span> String nrs() &#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"OK"</span>;
    &#125;

    <span style="color:#4078f2">@NotBlank(&#123;<span style="color:#50a14f">"val1"</span>, <span style="color:#50a14f">"val2"</span>&#125;)</span>
    <span style="color:#4078f2">@Mapping(<span style="color:#50a14f">"nblank"</span>)</span>
    <span style="color:#a626a4">public</span> String nblank(String val1, String val2) &#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"OK"</span>;
    &#125;
    
    <span style="color:#4078f2">@Mapping(<span style="color:#50a14f">"bean"</span>)</span>
    <span style="color:#a626a4">public</span> String bean(<span style="color:#4078f2">@Validated</span> ValidModel model) &#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"OK"</span>;
    &#125;
&#125;

<span style="color:#4078f2">@Data</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">ValidModel</span> &#123;
    <span style="color:#4078f2">@NotBlank(message = <span style="color:#50a14f">"手机号不能为空"</span>)</span>
    <span style="color:#a626a4">private</span> String mobile;

    <span style="color:#4078f2">@NotBlank(message = <span style="color:#50a14f">"密码不能为空"</span>)</span>
    <span style="color:#a626a4">private</span> String password;
&#125;
</code></pre> 
<h3 style="text-align:start">5、solon.auth 插件增加模板标签支持</h3> 
<ul> 
 <li>调整 各模板引擎内部接口名称，显得更统一些</li> 
 <li>模板 beetl 增加权限认证标签支持</li> 
 <li>模板 enjoy 增加权限认证标签支持</li> 
 <li>模板 freemarker 增加权限认证标签支持</li> 
 <li>模板 jsp 增加权限认证标签支持</li> 
 <li>模板 thymeleaf 增加权限认证标签支持</li> 
 <li>模板 velocity 增加权限认证标签支持</li> 
</ul> 
<p style="text-align:start">beetl 示例：</p> 
<pre style="text-align:start"><code class="language-html"><<span style="color:#e45649">#authPermissions</span> <span style="color:#986801">name</span>=<span style="color:#50a14f">"user:del"</span>>
我有user:del权限
</<span style="color:#e45649">#authPermissions</span>>

<<span style="color:#e45649">#authRoles</span> <span style="color:#986801">name</span>=<span style="color:#50a14f">"admin"</span>>
我有admin角色
</<span style="color:#e45649">#authRoles</span>>
</code></pre> 
<p style="text-align:start">enjoy 示例：</p> 
<pre style="text-align:start"><code class="language-html">#authPermissions("user:del")
我有user:del权限
#end

#authRoles("admin")
我有admin角色
#end
</code></pre> 
<p style="text-align:start">freemarker 示例：</p> 
<pre style="text-align:start"><code class="language-xml"><<span style="color:#e45649">@authPermissions</span> <span style="color:#986801">name</span>=<span style="color:#50a14f">"user:del"</span>>
我有user:del权限
</<span style="color:#e45649">@authPermissions</span>>

<<span style="color:#e45649">@authRoles</span> <span style="color:#986801">name</span>=<span style="color:#50a14f">"admin"</span>>
我有admin角色
</<span style="color:#e45649">@authRoles</span>>
</code></pre> 
<h3 style="text-align:start">6、solon core 的事务与缓存定义接口迁到：solon.data 插件</h3> 
<ul> 
 <li>移动 org.noear.solon.core.cache.CacheService 到 org.noear.solon.data.cache.CacheService</li> 
 <li>移动 org.noear.solon.core.tran.TranExecutor 到 org.noear.solon.data.tran.TranExecutor</li> 
 <li>移动 org.noear.solon.core.tran.TranUtils 到 org.noear.solon.data.tran.TranUtils</li> 
</ul> 
<h3 style="text-align:start">7、增加 httputils-solon-plugin 插件</h3> 
<p style="text-align:start">这是基于Solon Cloud 注册发现服务的 HttpUtils 工具，为Rpc客户端方案外提供一个便宜的服务调用方式。</p> 
<p style="text-align:start">非常适合k8s和传统注册发现服务等不同场景。示例：</p> 
<pre style="text-align:start"><code class="language-java">String rst = HttpUtils.http(<span style="color:#50a14f">"helloservice"</span>, <span style="color:#50a14f">"/hello"</span>).data(<span style="color:#50a14f">"name"</span>,<span style="color:#50a14f">"noer"</span>).post();
System.out.println(rst);
</code></pre> 
<h3 style="text-align:start">8、请求参数自动转换日期的格式增加到9种</h3> 
<pre style="text-align:start"><code><span style="color:#50a14f">"yyyy-MM-dd'T'HH🇲🇲ss.SSSXXX"</span>
<span style="color:#50a14f">"yyyy-MM-dd'T'HH🇲🇲ss.SSS'Z'"</span>
<span style="color:#50a14f">"yyyy-MM-dd HH🇲🇲ss,SSS"</span>
<span style="color:#50a14f">"yyyy-MM-dd HH🇲🇲ss.SSS"</span>
<span style="color:#50a14f">"yyyyMMddHHmmssSSSZ"</span>
<span style="color:#50a14f">"yyyy-MM-dd'T'HH🇲🇲ss"</span>
<span style="color:#50a14f">"yyyy-MM-dd HH🇲🇲ss"</span>
<span style="color:#50a14f">"yyyy-MM-dd"</span>
<span style="color:#50a14f">"HH🇲🇲ss"</span>
</code></pre> 
<h3 style="text-align:start">9、其它</h3> 
<ul> 
 <li>修复加载配置时，值为null会出错的问题</li> 
 <li>升级snack3，增加更多的时间处理格式</li> 
 <li>增加更多的时间处理格式（与snack3同）</li> 
 <li>enjoy 模式，分离 debug 引擎的实例</li> 
 <li>Validator 接口的原函数 validate 更名为 validateOfContext；并增加 validateOfEntity 函数定义（支持实体验证）</li> 
 <li>solon.extend.jsr303 插件不再自动注入到容器（Solon Validation，已支持实体验证）</li> 
</ul> 
<h3 style="text-align:start">附：入门示例</h3> 
<ul> 
 <li>Solon 入门教程示例：<a href="https://gitee.com/noear/solon_demo">https://gitee.com/noear/solon_demo</a></li> 
 <li>Solon Api 入门教程示例：<a href="https://gitee.com/noear/solon_api_demo">https://gitee.com/noear/solon_api_demo</a></li> 
 <li>Solon Rpc 入门教程示例：<a href="https://gitee.com/noear/solon_rpc_demo">https://gitee.com/noear/solon_rpc_demo</a></li> 
 <li>Solon Auth 入门教程示例：<a href="https://gitee.com/noear/solon_auth_demo">https://gitee.com/noear/solon_auth_demo</a></li> 
 <li>Solon Cloud 入门教程示例：<a href="https://gitee.com/noear/solon_cloud_demo">https://gitee.com/noear/solon_cloud_demo</a></li> 
 <li>Solon 进阶教程示例：<a href="https://gitee.com/noear/solon_advance_demo">https://gitee.com/noear/solon_advance_demo</a></li> 
</ul>
                                        </div>
                                      
</div>
            