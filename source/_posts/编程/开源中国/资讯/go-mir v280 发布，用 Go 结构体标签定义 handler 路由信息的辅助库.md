
---
title: 'go-mir v2.8.0 发布，用 Go 结构体标签定义 handler 路由信息的辅助库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/22688664932b1d05818236d1764d60dca2d.jpg'
author: 开源中国
comments: false
date: Wed, 06 Apr 2022 10:39:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/22688664932b1d05818236d1764d60dca2d.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">go-mir v2.8.0 发布了,支持多个web框架，自带mirc脚手架，零基础开发web应用，方便快捷。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>新增特性：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>支持把一个方法注册到多个HTTP METHOD，eg:</li> 
</ul> 
<pre><code class="language-go">type Site struct &#123;
Assets    mir.Any   `mir:"/assets" method:"Head,Get"`
Others    mirAny    `mir:"/others"`
Status    mir.Any   `mir:"/Status" method:"Get,Post,Head"`
&#125;</code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>额～ 还有很多...  有兴趣可以查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falimy%2Fmir%2Freleases" target="_blank">这里</a>。</li> 
</ul> 
<p><s><em>最近疫情原因，呆家出不去，所以...没啥事，就是发个版本打发一下无聊时间～～</em></s></p> 
<p><em><s>这个库其实本质上是一个代码生成器，当初开发这个库就是奔着写代码偷懒去的，本着能自动生成就绝不Ctr-C/Ctr-V的心思，业余时间捣腾几下，还别说，至少在我的项目中，还是蛮省心的，有兴趣的朋友可以尝试一下，万一就对了你的心呢！！！</s></em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>go-mir v2的架构如下：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="go-mir-v2-arc" height="261" src="https://oscimg.oschina.net/oscnet/22688664932b1d05818236d1764d60dca2d.jpg" width="831" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">v2版本升级采用代码生成的方式生成接口代码，同样也是采用golang内置的struct tag定义路由信息，但不同于v1版本在引擎启动时解析后注册路由信息到web引擎，这里参考grpc的接口生成方式，生成接口定义文件，业务逻辑只要实现了接口，注册接口实现的对象到相应的web引擎，启动后就可以对外通过RESTfull接口获取服务。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#333333">go-mir v2<span> </span></span><strong>功能特性</strong>：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>使用Go结构体标签定义handler路由信息；</li> 
 <li>自动根据定义的结构体标签信息生成handler接口，开发者实现相应接口后注册到router，与gRPC的使用方式类似；</li> 
 <li>内置支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgin-gonic%2Fgin" target="_blank">gin</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-chi%2Fchi" target="_blank">go-chi</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorilla%2Fmux" target="_blank">mux</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjulienschmidt%2Fhttprouter" target="_blank">httprouter</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flabstack%2Fecho" target="_blank">echo</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkataras%2Firis" target="_blank">iris</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-macaron%2Fmacaron" target="_blank">macaron</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgofiber%2Ffiber" target="_blank">fiber</a>的代码生成器；</li> 
 <li>自带脚手架<strong>mirc</strong>自动生成<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgin-gonic%2Fgin" target="_blank">gin</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-chi%2Fchi" target="_blank">go-chi</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorilla%2Fmux" target="_blank">mux</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjulienschmidt%2Fhttprouter" target="_blank">httprouter</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flabstack%2Fecho" target="_blank">echo</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkataras%2Firis" target="_blank">iris</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-macaron%2Fmacaron" target="_blank">macaron</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgofiber%2Ffiber" target="_blank">fiber</a>样式的模板工程代码；</li> 
 <li>支持多goroutine并发生成接口代码，加快代码生成效率；</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">go-mir v2 </span><strong>代码示例：(eg: gin style)</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>生成样板代码</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>% <span style="color:#d73a49"><span style="color:#d73a49">go</span></span> get github.com/alimy/mir/mirc/v2@latest
% mirc <span>new</span> -d mir-examples
% tree mir-examples
mir-examples
├── Makefile
├── README.md
├── <span style="color:#d73a49"><span style="color:#d73a49">go</span></span>.mod
├── main.<span style="color:#d73a49"><span style="color:#d73a49">go</span></span>
└── mirc
    ├── main.<span style="color:#d73a49"><span style="color:#d73a49">go</span></span>
    └── routes
        ├── site.<span style="color:#d73a49"><span style="color:#d73a49">go</span></span>
        ├── v1
        │   └── site.<span style="color:#d73a49"><span style="color:#d73a49">go</span></span>
        └── v2
            └── site.<span style="color:#d73a49"><span style="color:#d73a49">go</span></span>

% cd mir-examples
% <span>make</span> generate</code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>自定义路由信息，比如：</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-go"><span style="color:#6a737d"><span style="color:#6a737d">// file: mirc/routes/v1/site.go</span></span>

<span style="color:#d73a49"><span style="color:#d73a49">package</span></span> v1

<span style="color:#d73a49"><span style="color:#d73a49">import</span></span> (
<span style="color:#032f62"><span style="color:#032f62">"github.com/alimy/mir/v2"</span></span>
<span style="color:#032f62"><span style="color:#032f62">"github.com/alimy/mir/v2/engine"</span></span>
)

<span style="color:#d73a49"><span><span style="color:#d73a49">func</span></span></span><span> </span><span style="color:#6f42c1"><span><span style="color:#6f42c1">init</span></span></span><span><span>()</span></span> &#123;
engine.AddEntry(<span>new</span>(Site))
&#125;

<span style="color:#6a737d"><span style="color:#6a737d">// Site mir's struct tag define</span></span>
<span style="color:#d73a49"><span style="color:#d73a49">type</span></span> Site <span style="color:#d73a49"><span style="color:#d73a49">struct</span></span> &#123;
Chain    mir.Chain <span style="color:#032f62"><span style="color:#032f62">`mir:"-"`</span></span>
Group    mir.Group <span style="color:#032f62"><span style="color:#032f62">`mir:"v1"`</span></span>
Index    mir.Get   <span style="color:#032f62"><span style="color:#032f62">`mir:"/index/"`</span></span>
Articles mir.Get   <span style="color:#032f62"><span style="color:#032f62">`mir:"/articles/:category/"`</span></span>
&#125;</code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li style="text-align:left">定义生成器入口，比如：</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-go"><span style="color:#6a737d"><span style="color:#6a737d">// file: mirc/main.go</span></span>

<span style="color:#d73a49"><span style="color:#d73a49">package</span></span> main

<span style="color:#d73a49"><span style="color:#d73a49">import</span></span> (
<span style="color:#032f62"><span style="color:#032f62">"log"</span></span>

<span style="color:#032f62"><span style="color:#032f62">"github.com/alimy/mir/v2/core"</span></span>
<span style="color:#032f62"><span style="color:#032f62">"github.com/alimy/mir/v2/engine"</span></span>

_ <span style="color:#032f62"><span style="color:#032f62">"github.com/alimy/mir/v2/examples/mirc/routes"</span></span>
_ <span style="color:#032f62"><span style="color:#032f62">"github.com/alimy/mir/v2/examples/mirc/routes/v1"</span></span>
_ <span style="color:#032f62"><span style="color:#032f62">"github.com/alimy/mir/v2/examples/mirc/routes/v2"</span></span>
)

<span style="color:#6a737d"><span style="color:#6a737d">//go:generate go run main.go</span></span>
<span style="color:#d73a49"><span><span style="color:#d73a49">func</span></span></span><span> </span><span style="color:#6f42c1"><span><span style="color:#6f42c1">main</span></span></span><span><span>()</span></span> &#123;
log.Println(<span style="color:#032f62"><span style="color:#032f62">"generate code start"</span></span>)
opts := core.Options&#123;
core.RunMode(core.InSerialDebugMode),
core.GeneratorName(core.GeneratorGin),
core.SinkPath(<span style="color:#032f62"><span style="color:#032f62">"./gen"</span></span>),
&#125;
<span style="color:#d73a49"><span style="color:#d73a49">if</span></span> err := engine.Generate(opts); err != <span style="color:#005cc5"><span style="color:#005cc5">nil</span></span> &#123;
log.Fatal(err)
&#125;
log.Println(<span style="color:#032f62"><span style="color:#032f62">"generate code finish"</span></span>)
&#125;</code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>自动生成接口，基于上面的定义，生成器将自动生成接口定义文件，如下：</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-go">% <span>make</span> generate
% cat mirc/gen/api/v1/site.<span style="color:#d73a49"><span style="color:#d73a49">go</span></span>

<span style="color:#6a737d"><span style="color:#6a737d">// Code generated by go-mir. DO NOT EDIT.</span></span>

<span style="color:#d73a49"><span style="color:#d73a49">package</span></span> v1

<span style="color:#d73a49"><span style="color:#d73a49">import</span></span> (
<span style="color:#032f62"><span style="color:#032f62">"github.com/gin-gonic/gin"</span></span>
)

<span style="color:#d73a49"><span style="color:#d73a49">type</span></span> Site <span style="color:#d73a49"><span style="color:#d73a49">interface</span></span> &#123;
<span style="color:#6a737d"><span style="color:#6a737d">// Chain provide handlers chain for gin</span></span>
Chain() gin.HandlersChain

Index(*gin.Context)
Articles(*gin.Context)
&#125;

<span style="color:#6a737d"><span style="color:#6a737d">// RegisterSiteServant register Site servant to gin</span></span>
<span style="color:#d73a49"><span><span style="color:#d73a49">func</span></span></span><span> </span><span style="color:#6f42c1"><span><span style="color:#6f42c1">RegisterSiteServant</span></span></span><span><span>(e *gin.Engine, s Site)</span></span> &#123;
router := e.Group(<span style="color:#032f62"><span style="color:#032f62">"v1"</span></span>)
<span style="color:#6a737d"><span style="color:#6a737d">// use chain for router</span></span>
middlewares := s.Chain()
router.Use(middlewares...)

<span style="color:#6a737d"><span style="color:#6a737d">// register routes info to router</span></span>
router.Handle(<span style="color:#032f62"><span style="color:#032f62">"GET"</span></span>, <span style="color:#032f62"><span style="color:#032f62">"/index/"</span></span>, s.Index)
router.Handle(<span style="color:#032f62"><span style="color:#032f62">"GET"</span></span>, <span style="color:#032f62"><span style="color:#032f62">"/articles/:category/"</span></span>, s.Articles)
&#125;</code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>实现接口逻辑, 比如：</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-go"><span style="color:#6a737d"><span style="color:#6a737d">// file: servants/site_v1.go</span></span>

package servants

<span style="color:#d73a49"><span style="color:#d73a49">import</span></span> (
<span style="color:#032f62"><span style="color:#032f62">"net/http"</span></span>

<span style="color:#032f62"><span style="color:#032f62">"github.com/gin-gonic/gin"</span></span>

api <span style="color:#032f62"><span style="color:#032f62">"github.com/alimy/mir/v2/examples/mirc/gen/api/v1"</span></span>
)

<span style="color:#d73a49"><span style="color:#d73a49">var</span></span> <span>_</span> api.<span style="color:#d73a49"><span style="color:#d73a49">Site</span></span> = <span style="color:#d73a49"><span style="color:#d73a49">EmptySiteV1</span></span>&#123;&#125;

<span style="color:#6a737d"><span style="color:#6a737d">// EmptySiteV1 implement api.Site interface</span></span>
type <span style="color:#d73a49"><span style="color:#d73a49">EmptySiteV1</span></span> <span style="color:#d73a49"><span><span style="color:#d73a49">struct</span></span></span>&#123;&#125;

<span style="color:#d73a49"><span><span style="color:#d73a49">func</span></span></span><span> <span>(EmptySiteV1)</span></span> <span style="color:#d73a49"><span style="color:#d73a49">Chain</span></span>() gin.<span style="color:#d73a49"><span style="color:#d73a49">HandlersChain</span></span> &#123;
<span style="color:#d73a49"><span style="color:#d73a49">return</span></span> gin.<span style="color:#d73a49"><span style="color:#d73a49">HandlersChain</span></span>&#123;gin.<span style="color:#d73a49"><span style="color:#d73a49">Logger</span></span>()&#125;
&#125;

<span style="color:#d73a49"><span><span style="color:#d73a49">func</span></span></span><span> <span>(EmptySiteV1)</span></span> <span style="color:#d73a49"><span style="color:#d73a49">Index</span></span>(<span>c</span> *gin.<span style="color:#d73a49"><span style="color:#d73a49">Context</span></span>) &#123;
<span>c</span>.<span style="color:#d73a49"><span style="color:#d73a49">String</span></span>(http.<span style="color:#d73a49"><span style="color:#d73a49">StatusOK</span></span>, <span style="color:#032f62"><span style="color:#032f62">"get index data (v1)"</span></span>)
&#125;

<span style="color:#d73a49"><span><span style="color:#d73a49">func</span></span></span><span> <span>(EmptySiteV1)</span></span> <span style="color:#d73a49"><span style="color:#d73a49">Articles</span></span>(<span>c</span> *gin.<span style="color:#d73a49"><span style="color:#d73a49">Context</span></span>) &#123;
<span>c</span>.<span style="color:#d73a49"><span style="color:#d73a49">String</span></span>(http.<span style="color:#d73a49"><span style="color:#d73a49">StatusOK</span></span>, <span style="color:#032f62"><span style="color:#032f62">"get articles data (v1)"</span></span>)
&#125;</code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>注册接口实现对象到相对应的router，比如：</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">package</span></span></span> main

<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">import</span></span></span> (
<span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"log"</span></span></span>

<span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"github.com/gin-gonic/gin"</span></span></span>

<span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"github.com/alimy/mir/v2/examples/mirc/gen/api"</span></span></span>
<span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"github.com/alimy/mir/v2/examples/mirc/gen/api/v1"</span></span></span>
<span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"github.com/alimy/mir/v2/examples/mirc/gen/api/v2"</span></span></span>
<span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"github.com/alimy/mir/v2/examples/servants"</span></span></span>
)

<span style="color:#d73a49"><span style="color:#d73a49"><span><span style="color:#d73a49">func</span></span></span></span><span> </span><span style="color:#6f42c1"><span style="color:#6f42c1"><span><span style="color:#6f42c1">main</span></span></span></span><span><span>()</span></span> &#123;
e := gin.New()

<span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// register servants to engine</span></span></span>
registerServants(e)

<span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// start servant service</span></span></span>
<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">if</span></span></span> err := e.Run(); err != <span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">nil</span></span></span> &#123;
log.Fatal(err)
&#125;
&#125;

<span style="color:#d73a49"><span style="color:#d73a49"><span><span style="color:#d73a49">func</span></span></span></span><span> </span><span style="color:#6f42c1"><span style="color:#6f42c1"><span><span style="color:#6f42c1">registerServants</span></span></span></span><span><span>(e *gin.Engine)</span></span> &#123;
<span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// register default group routes</span></span></span>
api.RegisterSiteServant(e, servants.EmptySiteWithNoGroup&#123;&#125;)

<span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// register routes for group v1</span></span></span>
v1.RegisterSiteServant(e, servants.EmptySiteV1&#123;&#125;)

<span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// register routes for group v2</span></span></span>
v2.RegisterSiteServant(e, servants.EmptySiteV2&#123;&#125;)
&#125;</code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>最后，构建并运行应用:</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#6a737d"><span style="color:#6a737d">%</span></span><span> make run</span></code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>大功告成，是不是很简单，赶紧上手吧:)</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>演示项目：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falimy%2Fmir%2Ftree%2Fmaster%2Fexamples" target="_blank">examples</a>：一个简单的快速了解如何使用mir的演示项目；</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falimy%2Fmirage" target="_blank">Mirage-幻影</a>: 简单的Docker图形化管理，示范如何使用<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falimy%2Fmir" target="_blank">go-mir</a>构建web应用程序.</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falimy%2Fmir-covid19" target="_blank">mir-covid19</a>:  新冠疫情统计<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2FTH_COVID19_International" target="_blank">TH_COVID19_International</a>的Golang版本，完整的演示了如何使用mir快速开发一个web应用。</strong></p> 
<p> </p>
                                        </div>
                                      
</div>
            