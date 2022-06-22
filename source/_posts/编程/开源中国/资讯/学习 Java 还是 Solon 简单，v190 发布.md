
---
title: '学习 Java 还是 Solon 简单，v1.9.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3884'
author: 开源中国
comments: false
date: Wed, 22 Jun 2022 09:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3884'
---

<div>   
<div class="content">
                                                                                            <p style="color:#24292e; text-align:start">Solon 1.9.0 发布了，使用方法很简单：</p> 
<p style="color:#24292e; text-align:start">pom.xml 添加依赖</p> 
<pre style="text-align:start"><code class="language-yaml language-yml"><span style="color:#50a14f"><dependency></span>
    <span style="color:#50a14f"><groupId>org.noear</groupId></span>
    <span style="color:#50a14f"><artifactId>solon-api</artifactId></span>
    <span style="color:#50a14f"><version>1.9.0</version></span>
<span style="color:#50a14f"></dependency></span>
</code></pre> 
<p style="color:#24292e; text-align:start">添加几行 java 代码，就可以运行</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">App</span> &#123;
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span> &#123;
        Solon.start(App.class, args);
    &#125;

    <span style="color:#4078f2">@Get</span>
    <span style="color:#4078f2">@Mapping("/hello")</span>
    <span style="color:#a626a4">public</span> String <span style="color:#4078f2">hello</span><span>(<span style="color:#4078f2">@Param(defaultValue = "world")</span> String name)</span> &#123;
        <span style="color:#a626a4">return</span> String.format(<span style="color:#50a14f">"Hello %s!"</span>, name);
    &#125;
&#125;
</code>
</pre> 
<hr> 
<h4 style="text-align:start">相对于 Spring Boot 和 Spring Cloud 的项目</h4> 
<ul> 
 <li>启动快 5 ～ 10 倍</li> 
 <li>qps 高 2～ 3 倍</li> 
 <li>运行时内存节省 1/3 ~ 1/2</li> 
 <li>打包可以缩小到 1/2 ~ 1/10（比如，90Mb 的变成了 9Mb）</li> 
 <li>基于 app.name 进行注册发现 与 k8s svc 相互对应</li> 
 <li>支持 Service Mesh 架构部署方案</li> 
</ul> 
<h4 style="text-align:start">本次更新</h4> 
<ul> 
 <li>新增 grpc-solon-plugin 插件</li> 
 <li>新增 solon.cache.caffeine 插件</li> 
 <li>新增 solon.serialization.fastjson2 插件</li> 
 <li>新增 nami.coder.fastjson2 插件</li> 
 <li>新增 solon.aspect 插件</li> 
 <li>新增 solon.health 插件</li> 
 <li> <p>新增 solon.hotplug 插件</p> <pre><code class="language-csharp"><span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#4078f2">DemoApp</span> &#123;
  <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span>(<span>String[] args</span>)</span> &#123;
      Solon.start(App.<span style="color:#a626a4">class</span>, args, app -> &#123;
          <em>//添加待管理的插件</em>
          PluginManager.<span style="color:#a626a4">add</span>(<span style="color:#50a14f">"add1"</span>, <span style="color:#50a14f">"/x/x/x.jar"</span>);
          PluginManager.<span style="color:#a626a4">add</span>(<span style="color:#50a14f">"add2"</span>, <span style="color:#50a14f">"/x/x/x2.jar"</span>);

          app.<span style="color:#a626a4">get</span>(<span style="color:#50a14f">"start"</span>, ctx -> &#123;
              <em>//启动插件</em>
              PluginManager.start(<span style="color:#50a14f">"add1"</span>);
              ctx.output(<span style="color:#50a14f">"OK"</span>);
          &#125;);

          app.<span style="color:#a626a4">get</span>(<span style="color:#50a14f">"stop"</span>, ctx -> &#123;
              <em>//停止插件</em>
              PluginManager.stop(<span style="color:#50a14f">"add1"</span>);
              ctx.output(<span style="color:#50a14f">"OK"</span>);
          &#125;);
      &#125;);
  &#125;
&#125;
</code></pre> </li> 
 <li>新增 solon.config.yaml 插件</li> 
 <li>新增 solon.web.servlet 插件</li> 
 <li>新增 solon.web.staticfiles 插件</li> 
 <li>新增 solon.web.cors 插件</li> 
 <li>插件 solon.extend.aspect [标为弃用]</li> 
 <li>插件 solon.extend.health [标为弃用]</li> 
 <li>插件 solon.extend.hotplug [标为弃用]</li> 
 <li>插件 solon.extend.properties.yaml [标为弃用]</li> 
 <li>插件 solon.extend.servlet [标为弃用]</li> 
 <li>插件 solon.extend.staticfiles [标为弃用]</li> 
 <li>插件 solon.extend.cors [标为弃用]</li> 
</ul> 
<h4 style="text-align:start">进一步了解 Solon</h4> 
<ul> 
 <li><a href="https://my.oschina.net/noear/blog/4980834">《想法与架构笔记》</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsolon.noear.org%2Farticle%2Ffamily-preview" target="_blank">《生态预览》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/4863844">《与 Spring Boot 的区别？》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/5039169">《与 Spring Cloud 的区别？》</a></li> 
</ul>
                                        </div>
                                      
</div>
            