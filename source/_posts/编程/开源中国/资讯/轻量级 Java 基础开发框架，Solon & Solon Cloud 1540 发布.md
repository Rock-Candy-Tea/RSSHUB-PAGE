
---
title: '轻量级 Java 基础开发框架，Solon & Solon Cloud 1.5.40 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9950'
author: 开源中国
comments: false
date: Thu, 30 Sep 2021 10:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9950'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="text-align:start">Solon 已有120个生态扩展插件，此次版本以细节打磨为主：</h3> 
<ul> 
 <li>增加 mybatisplus-solon-plugin 插件 <pre><code class="language-java"><em>//至此，Solon 已完成国内外主流的5个ORM框架插件适配</em>
</code></pre> </li> 
 <li> <p>插件 solon.validation，注解 Whitelist、NotBlacklist、Logined 增加可继承支持</p> <pre><code class="language-java"><em>//</em>
<em>//Solon 具体轻量而完整的验证能力及验证扩展机制</em>
<em>//</em>
<span style="color:#4078f2">@Logined</span>
<span style="color:#4078f2">@Valid</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">ApiBaseLogined</span> </span>&#123;
&#125;


<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span> <span style="color:#a626a4">extends</span> <span style="color:#c18401">ApiBaseLogined</span> </span>&#123;
  <span style="color:#4078f2">@Numeric</span>(&#123;<span style="color:#50a14f">"id"</span>&#125;)
  <span style="color:#4078f2">@NotEmpty</span>(&#123;<span style="color:#50a14f">"id"</span>,<span style="color:#50a14f">"name"</span>,<span style="color:#50a14f">"description"</span>&#125;)
  <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"addArchive"</span>)
  <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">addArchive</span><span>(Long id, String name, String description)</span></span>&#123;
      <em>//...</em>
  &#125;

  <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"addArchiveItem"</span>)
  <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">addArchiveItem</span><span>(@Validated ItemModel item)</span></span>&#123;
      <em>//...</em>
  &#125;
&#125;
</code></pre> </li> 
 <li> <p>调整 路由规则，带 * 号的印射关系排到后面</p> <pre><code class="language-java"><span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span> </span>&#123;
  <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/*"</span>)
  <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">all</span><span>()</span></span>&#123;
  &#125;

  <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/add"</span>) <em>//相对于*，具有优先匹配权</em>
  <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">add</span><span>()</span></span>&#123; 
  &#125;
&#125;
</code></pre> </li> 
 <li>调整 通讯端口被占用时，改为抛出异常</li> 
 <li>国际化 增加 Content-Language 头信息支持，让国际化控制更友好</li> 
 <li> <p>国际化 增加 上下文的 Locale 注入支持</p> <pre><code class="language-java"><span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/demo"</span>)
<span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">demo</span><span>(Locale locale)</span></span>&#123;

&#125; 
</code></pre> </li> 
 <li> <p>国际化 增加 I18nService 类</p> <pre><code class="language-java"><span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span> </span>&#123;
  I18nService i18nService = <span style="color:#a626a4">new</span> I18nService(<span style="color:#50a14f">"i18n.user"</span>);

  <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/demo"</span>)
  <span><span style="color:#a626a4">public</span> String <span style="color:#4078f2">demo</span><span>(Locale locale)</span></span>&#123;
      <span style="color:#a626a4">return</span> i18nService.get(locale, <span style="color:#50a14f">"user.name"</span>);
  &#125;
&#125;
</code></pre> </li> 
 <li>调整 solon.data.cache.CacheServiceDefault 内部类，更名为 LocalCacheService <pre><code class="language-java"><span style="color:#4078f2">@Configuration</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">Config</span> </span>&#123;
  <span style="color:#4078f2">@Bean</span>
  <span><span style="color:#a626a4">public</span> CacheService <span style="color:#4078f2">cache</span><span>()</span></span>&#123;
      <span style="color:#a626a4">return</span> <span style="color:#a626a4">new</span> LocalCacheService();
  &#125;
&#125;
</code></pre> </li> 
 <li>插件 solon.serialization.hession 更名为：插件 solon.serialization.hessian</li> 
 <li>调整序列化渲染方案，不再受accept header影响</li> 
 <li>调整 验证器 Numeric ，空为通过（是否充许为空由@NotEmpty处理）</li> 
 <li>调整 Aop.get(type) 改为 return bean || null</li> 
 <li>取消 Aop.getOrNull(type) 接口，由 Aop.get(type)</li> 
 <li>新增 Aop.getOrNew(type) return bean; 替代旧的 Aop.get(type)</li> 
 <li>接口 CloudFileService 增加 delete 方法 <pre><code class="language-java"><span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span> </span>&#123;
  <span style="color:#4078f2">@Bean</span>
  <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">put</span><span>(UploadedFile file)</span></span>&#123;
      <em>//阿里云 oss  或 AWS s3 或 七牛 图片上传（使用 Solon Cloud 接口会很简便）</em>
      CloudClient.file().putStream(Utils.guid(), file.content, <span style="color:#50a14f">"image/jpg"</span>);
  &#125;
&#125;
</code></pre> </li> 
 <li>修复 solon.extend.staticfiles 会出现 .htm 的mine 匹配 .xhtm 的情况</li> 
 <li>优化不启用缓存的控制（基于代码控制，可根据启动参数变化）</li> 
 <li>优化不启用事务的控制</li> 
 <li>调整缓存标签参数使用策略，缺时出异常方便用者发现</li> 
 <li> <p>增加@Inject("$&#123;xx.xx.ary&#125;") List<span> </span>ary 的支持</p> <pre><code class="language-java"><span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span> </span>&#123;
  <span style="color:#4078f2">@Inject</span>(<span style="color:#50a14f">"$&#123;project.linkes&#125;"</span>)
  List<String> linkes;

  <span style="color:#4078f2">@Inject</span>(<span style="color:#50a14f">"$&#123;project.details&#125;"</span>)
  Map<String,String> details;
&#125;
</code></pre> </li> 
 <li>修复 Props 在 forEach 时，可能出现重复key的问题</li> 
</ul> 
<h3 style="text-align:start">关于 Solon</h3> 
<p style="color:#24292e; text-align:start">Solon 是一个轻量的Java基础开发框架。强调，<strong>克制 + 简洁 + 开放的原则</strong>；力求，<strong>更小、更快、更自由的体验</strong>。支持：RPC、REST API、MVC、Job、Micro service、WebSocket、Socket 等多种开发模式。短小而精悍！</p> 
<p style="color:#24292e; text-align:start">Solon Cloud 是一系列的接口标准和配置规范，算是 Solon 的分布式开发套件方案。</p> 
<h3 style="text-align:start">快速了解 Solon 的材料：</h3> 
<p style="color:#24292e; text-align:start"><a href="https://my.oschina.net/noear/blog/4863844">《Solon 特性简集，相较于 Springboot 有什么区别？》</a></p> 
<p style="color:#24292e; text-align:start"><a href="https://my.oschina.net/noear/blog/5039169">《Solon Cloud 分布式服务开发套件清单，感觉受与 Spring Cloud 的不同》</a></p> 
<p style="color:#24292e; text-align:start"><a href="https://my.oschina.net/noear/blog/4980834">《Solon 的想法与架构笔记》</a></p> 
<h4 style="text-align:start">所谓更小：</h4> 
<p style="color:#24292e; text-align:start">内核0.1m，最小的接口开发单位0.2m（相较于 Dubbo、Springboot 的依赖包，小到可以乎略不计）</p> 
<h4 style="text-align:start">所谓更快：</h4> 
<p style="color:#24292e; text-align:start">本机http helloworld测试，Qps可达12万之多。可参考：《<a href="https://gitee.com/noear/helloworld_wrk_test">helloworld_wrk_test</a>》</p> 
<h4 style="text-align:start">所谓更自由：(代码操控自由)</h4> 
<pre style="text-align:start"><code class="language-java"><em>// 除了注解模式之外，还可以按需手动</em>
<em>//</em>
<em>//手动获取配置（Props 为 Properties 增强版）</em>
Props db = Solon.cfg().getProp(<span style="color:#50a14f">"db"</span>);

<em>//手动获取容器里的Bean</em>
UserService userService = Aop.get(UserService<span>.<span style="color:#a626a4">class</span>)</span>;

<em>//手动监听http post请求</em>
Solon.global().post(<span style="color:#50a14f">"/user/update"</span>, x-> userService.updateById(x.paramMap()));

<em>//手动添加个RPC服务</em>
Solon.global().add(<span style="color:#50a14f">"/rpc/"</span>, HelloService<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">true</span>)</span>;

<em>//手动获取一个RPC服务消费端</em>
HelloService helloService = Nami.builder().create(HelloService<span>.<span style="color:#a626a4">class</span>)</span>;

<em>//手动为容器添加组件</em>
Aop.wrapAndPut(DemoService<span>.<span style="color:#a626a4">class</span>)</span>;
</code></pre> 
<h3 style="text-align:start">Hello world：</h3> 
<pre style="text-align:start"><code class="language-java"><em>//Handler 模式：</em>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">App</span></span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span></span>&#123;
        SolonApp app = Solon.start(App<span>.<span style="color:#a626a4">class</span>,<span style="color:#c18401">args</span>)</span>;
        
        app.get(<span style="color:#50a14f">"/"</span>,(c)->c.output(<span style="color:#50a14f">"Hello world!"</span>));
    &#125;
&#125;

<em>//Controller 模式：(mvc or rest-api)</em>
<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">App</span></span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span></span>&#123;
        Solon.start(App<span>.<span style="color:#a626a4">class</span>,<span style="color:#c18401">args</span>)</span>;
    &#125;
  
    <em>//限定 put 方法类型</em>
    <span style="color:#4078f2">@Put</span>
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/"</span>)
    <span><span style="color:#a626a4">public</span> String <span style="color:#4078f2">hello</span><span>(String name)</span></span>&#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"Hello "</span> + name;
    &#125;
&#125;

<em>//Remoting 模式：(rpc)</em>
<span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/"</span>)
<span style="color:#4078f2">@Remoting</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">App</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">HelloService</span></span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span></span>&#123;
        Solon.start(App<span>.<span style="color:#a626a4">class</span>,<span style="color:#c18401">args</span>)</span>;
    &#125;

    <span style="color:#4078f2">@Override</span>
    <span><span style="color:#a626a4">public</span> String <span style="color:#4078f2">hello</span><span>()</span></span>&#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"Hello world!"</span>;
    &#125;
&#125;
</code>
</pre> 
<h3 style="text-align:start">附：入门示例</h3> 
<ul> 
 <li>Solon 入门教程示例：<a href="https://gitee.com/noear/solon_demo">https://gitee.com/noear/solon_demo</a></li> 
 <li>Solon Api 入门教程示例：<a href="https://gitee.com/noear/solon_api_demo">https://gitee.com/noear/solon_api_demo</a></li> 
 <li>Solon Rpc 入门教程示例：<a href="https://gitee.com/noear/solon_rpc_demo">https://gitee.com/noear/solon_rpc_demo</a></li> 
 <li>Solon Auth 入门教程示例：<a href="https://gitee.com/noear/solon_auth_demo">https://gitee.com/noear/solon_auth_demo</a></li> 
 <li>Solon Cloud 入门教程示例：<a href="https://gitee.com/noear/solon_cloud_demo">https://gitee.com/noear/solon_cloud_demo</a></li> 
 <li>Solon 进阶教程示例：<a href="https://gitee.com/noear/solon_advance_demo">https://gitee.com/noear/solon_advance_demo</a></li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            