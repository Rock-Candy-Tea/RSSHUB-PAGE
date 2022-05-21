
---
title: '⭐️Archttp 1.0 新特性来了，简单、灵活、高并发，D 语言 Web 服务端框架！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3143'
author: 开源中国
comments: false
date: Sat, 21 May 2022 03:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3143'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <p>昨天是 5.20 中国式情人节，今天是 5.21 我生日，做开源有十多年了，这也是给自己的一个生日礼物。</p> 
 <p>D语言在国内的环境来说一直热不起来，我和我的开源团队也做过很多开源的框架，全功能的，基本对标 springboot 和 springcloud 那种级别，但是新手用起来不够友好，由于D语言在国内的文档匮乏导致入门难，运行这么庞大的框架更是不可想象的难。</p> 
</blockquote> 
<h2>Archttp 版本发布前言</h2> 
<p>近几年 Golang 的发展很猛烈，比如使用 gin 框架就可以实现高并发能力的微服务应用，更是这几年的发展 NodeJS 写服务端的也是越来越多，尤其是 ExpressJS 这优秀的 API 设计让更多人在做服务端开发选型的时候选择了他们。</p> 
<p>今天我们的主角 Archttp，首先来说 Archttp 拥有类似 ExpressJS 的 API 设计，让开发更轻量简单，其次拥有 Golang 级别的并发能力。</p> 
<h2>框架使用对比</h2> 
<p>我们先看一下 Archttp 最新版本中的基本使用用法和 Gin、Express 的差异。</p> 
<p>DLang 的 Archttp 框架：</p> 
<pre><code class="language-java">import archttp;

void main()
&#123;
    auto app = new Archttp;

    app.get("/", (req, res) &#123;
        res.send("Hello, World!");
    &#125;);

    app.listen(8080);
&#125;
</code></pre> 
<p>Golang 的 Gin 框架：</p> 
<pre><code class="language-go">package main

import (
        "net/http"
        "github.com/gin-gonic/gin"
)

func main() &#123;

        r := gin.Default()

        r.GET("/", func(context *gin.Context) &#123;
                context.String(http.StatusOK, "Hello world!")
        &#125;)

        r.Run(":8081")
&#125;
</code></pre> 
<p>NodeJS 的 ExpressJS 框架：</p> 
<pre><code class="language-javascript">var express = require('express');

var app = express();

app.get('/', function(req, res) &#123;
   res.send("Hello world!");
&#125;);

app.listen(8082);
</code></pre> 
<p>可以看出来这三个框架的使用都够简单，关于性能方面大家可以自己去做测试，作者目前只做了 Linux 平台下的性能测试，目前我的测试结果是 Archttp 最佳，系统是 Debian 11 虚拟机，欢迎大家一起来测试和反馈。</p> 
<h2>新版本特性：</h2> 
<ul> 
 <li>统一将方法名调整为小写字母驼峰命名</li> 
 <li>优化 Router 流程和模块调整</li> 
 <li>支持 response.sendFile(filepath, filename) 形式的下载</li> 
 <li>request 和 response 提供完整的 cookie 支持</li> 
 <li>app.use() 中间件功能可用</li> 
 <li>现在可以通过 app.newRouter() 创建新的 Router 对象</li> 
 <li>现在 app.use("/admin", Router) 可以进行子路由绑定，方便一个项目编写多个服务</li> 
 <li>完善 HttpRequest 内置方法，接近 ExpressJS 的 API 使用</li> 
 <li>完善 HttpResponse 内置方法，接近 ExpressJS 的 API 使用</li> 
 <li><span><span>稳定性测试和修复</span></span></li> 
</ul> 
<h3>路由功能示例代码</h3> 
<pre><code class="language-java">import archttp;

void main()
&#123;
    auto app = new Archttp;

    app.get("/", (req, res) &#123;
        res.send("Hello, World!");
    &#125;);

    app.get("/user/&#123;id:\\d+&#125;", (req, res) &#123;
        res.send("User id: " ~ req.params["id"]);
    &#125;);

    app.get("/blog/&#123;name&#125;", (req, res) &#123;
        res.send("Username: " ~ req.params["name"]);
    &#125;);

    app.listen(8080);
&#125;
</code></pre> 
<p>可以看出 Archttp 的路由功能非常简单清晰，也支持正则匹配和取值。</p> 
<h3>中间件使用示例代码</h3> 
<pre><code class="language-java">import archttp;

import std.stdio : writeln;

void main()
&#123;
    auto app = new Archttp;

    app.use((req, res, next) &#123;
        writeln("middleware 1 ..");
        next();
    &#125;);

    app.use((req, res, next) &#123;
        writeln("middleware 2 ..");
        next();
    &#125;);

    app.use((req, res, next) &#123;
        writeln("middleware 3 ..");
        next();
    &#125;);

    app.use((req, es, next) &#123;
        writeln("middleware 4 ..");
    &#125;);

    app.use((req, res, next) &#123;
        writeln("middleware 5 ..");
    &#125;);

    app.get("/", (req, res) &#123;
        res.send("Hello, World!");
    &#125;);

    app.listen(8080);
&#125;
</code></pre> 
<p>这段代码运行之后可以发现没有执行到 middleware 5，现在 Archttp 的执行遵循洋葱规则。</p> 
<h3>Cookie 使用示例代码</h3> 
<pre><code class="language-java">import archttp;

import std.stdio : writeln;

void main()
&#123;
    auto app = new Archttp;

    app.get("/", (request, response) &#123;

        writeln(request.cookie("token"));
        writeln(request.cookies());

        response.cookie("username", "myuser");
        response.cookie("token", "0123456789");

        response.send("Set cookies ..");
    &#125;);

    app.listen(8080);
&#125;
</code></pre> 
<h3>下载文件示例代码</h3> 
<pre><code class="language-java">import archttp;

void main()
&#123;
    auto app = new Archttp;

    app.get("/download", (req, res) &#123;
        res.sendFile("./attachments/avatar.jpg");
    &#125;);

    app.listen(8080);
&#125;
</code></pre> 
<h3>路由绑定示例代码</h3> 
<pre><code class="language-java">import archttp;

void main()
&#123;
    auto app = new Archttp;

    app.get("/", (req, res) &#123;
        res.send("Front page!");
    &#125;);

    auto adminRouter = Archttp.newRouter();
    
    adminRouter.get("/", (req, res) &#123;
        res.send("Hello, Admin!");
    &#125;);

    adminRouter.get("/login", (req, res) &#123;
        res.send("Login page!");
    &#125;);

    app.use("/admin", adminRouter);

    app.listen(8080);
&#125;
</code></pre> 
<p>可以看出 adminRouter 相当于一个路由组（路由组的概念来自于 Hunt Framework），路由组可以使用自己的中间件规则，也就是他相当于一个独立的子应用，可以独立控制权限等。</p> 
<h2>鸣谢</h2> 
<p>感谢我团队成员的支持，感谢所有支持我创建D语言中文社区的朋友们，感谢我D语言中文社区联合创始人张雪平老师和我一起打造D语言国内生态，感谢D语言国际社区的开发者们给我的支持，感谢开源中国提供国内开源平台。</p> 
<h2>收尾</h2> 
<p>我们做D语言开源项目已经有 7 年了，也听到很多好的坏的声音，但是我们看到的是一个值得使用的 D语言，我们拥有15年以上的框架架构能力，也希望能够打造一个 DLang 生态中不可或缺的一个开源项目，协助 D语言中文社区生态的发展。</p> 
<p>希望更多人参与到开源贡献中，希望开源中国越办越好，希望码云越来越好尽快度过目前的难关！</p> 
<h2>QQ交流群</h2> 
<p>184183224</p>
                                        </div>
                                      
</div>
            