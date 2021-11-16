
---
title: 'Go-Spring 发布 v1.1.0-rc2 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4156'
author: 开源中国
comments: false
date: Tue, 16 Nov 2021 07:47:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4156'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span><strong>前言</strong></span></p> 
<p>Go 语言以简单著称，一个很明显的例子就是只需要很少的代码即可实现一个最小的 Web API 。Go-Spring 融合了 Go 简单和 Spring 自动配置的优点。本文通过几个实现最小 Web API 的示例展示 Go-Spring 的简单和强大。</p> 
<p><span><strong>To Gopher</strong></span></p> 
<p>下面是使用 Go 标准库实现的 Hello World! 程序。代码真的很少！</p> 
<pre><code><span><span style="color:#ca7d37">package</span> main</span></code>
<code><span><span style="color:#ca7d37">import</span> (</span></code><code><span>  <span style="color:#dd1144">"net/http"</span></span></code><code><span>)</span></code>
<code><span><span><span style="color:#ca7d37">func</span> <span style="color:#dd1144">main</span><span>()</span></span> &#123;</span></code><code><span>  http.HandleFunc(<span style="color:#dd1144">"/"</span>, <span><span style="color:#ca7d37">func</span><span>(w http.ResponseWriter, r *http.Request)</span></span> &#123;</span></code><code><span>    w.Write([]<span style="color:#ca7d37">byte</span>(<span style="color:#dd1144">"Hello World!"</span>))</span></code><code><span>  &#125;)</span></code><code><span>  http.ListenAndServe(<span style="color:#dd1144">":8080"</span>, <span style="color:#0e9ce5">nil</span>)</span></code><code><span>&#125;</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">Gin 是目前最火的 Web 框架之一，它实现的 <span>Hell</span><span>o</span><span> World</span><span>! 程</span><span>序如下。也很简单。</span></p> 
<pre><code><span>package main</span></code>
<code><span><span style="color:#ca7d37">import</span> (</span></code><code><span>  <span style="color:#dd1144">"github.com/gin-gonic/gin"</span></span></code><code><span>  <span style="color:#dd1144">"github.com/gin-gonic/gin/ginS"</span></span></code><code><span>)</span></code>
<code><span><span><span style="color:#ca7d37">func</span> <span style="color:#dd1144">main</span><span>()</span></span> &#123;</span></code><code><span>  ginS.<span style="color:#0e9ce5">GET</span>(<span style="color:#dd1144">"/"</span>, <span><span style="color:#ca7d37">func</span><span>(<span style="color:#ca7d37">c</span> *gin.Context)</span></span> &#123;</span></code><code><span>    <span style="color:#ca7d37">c</span>.<span style="color:#0e9ce5">String</span>(<span style="color:#0e9ce5">200</span>, <span style="color:#dd1144">"Hello World!"</span>)</span></code><code><span>  &#125;)</span></code><code><span>  ginS.<span style="color:#0e9ce5">Run</span>()</span></code><code><span>&#125;</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">再来看看使用 Go-Spring 实现的 <span>Hell</span><span>o</span><span> World</span><span>!</span><span> </span>程序。同样很简单。</p> 
<pre><code><span>package main</span></code>
<code><span><span style="color:#ca7d37">import</span> (</span></code><code><span>  <span style="color:#dd1144">"github.com/go-spring/spring-core/gs"</span></span></code><code><span>  <span style="color:#dd1144">"github.com/go-spring/spring-core/web"</span></span></code><code><span>  <span style="color:#0e9ce5">_</span> <span style="color:#dd1144">"github.com/go-spring/starter-gin"</span></span></code><code><span>)</span></code>
<code><span><span><span style="color:#ca7d37">func</span> <span style="color:#dd1144">main</span><span>()</span></span> &#123;</span></code><code><span>  gs.<span style="color:#0e9ce5">GetMapping</span>(<span style="color:#dd1144">"/"</span>, <span><span style="color:#ca7d37">func</span><span>(ctx web.Context)</span></span> &#123;</span></code><code><span>    ctx.<span style="color:#0e9ce5">String</span>(<span style="color:#dd1144">"Hello World!"</span>)</span></code><code><span>  &#125;)</span></code><code><span>  gs.<span style="color:#0e9ce5">Run</span>()</span></code><code><span>&#125;</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">但是，<span>可</span><span>以</span><span>注意到</span><span>使用 Go-Spring</span><span><span> </span></span><span>实现的示例</span><span>中有一个匿名导入的包，它的作用是告诉 <span>Hell</span><span>o</span><span> World</span><span>!</span><span><span> </span>程序</span>使用 Gin 作为底层 Web Server 实现。</span><span>如果我们把</span><span>这一行改为如下代码，程序仍然可以正常执行，但是这时候程序使用 Echo 作为底层 Web Server 实现。</span></p> 
<pre><code><span><span style="color:#0e9ce5">_</span> <span style="color:#dd1144">"github.com/go-spring/starter-echo"</span></span></code></pre> 
<p>虽然 Go-Spring 多了一行匿名包导入，但因此获得了比标准库更强大的能力。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong><span>To Javaer</span></strong></p> 
<p>Go-Spring 虽然提供了和 Go 标准库一样的编程模型，但本质上它是基于 IoC (依赖注入) 实现的，因此它具有标准库不具备的自动配置能力，而且与 Java Spring Boot 相比，Go-Spring 的编程效率也不差。</p> 
<p>下面是使用 Java Spring Boot 实现的一个 <span>Hell</span><span>o</span><span> World</span><span>!</span><span> 程序</span>，但是与上面的示例不同，为了展示 Java Spring 的依赖注入能力，它同时会打印 JAVA_HOME 环境变量的值。代码如下。</p> 
<pre><code><span><span style="color:#ca7d37">package</span> com.example.demo11;</span></code>
<code><span><span style="color:#ca7d37">import</span> org.springframework.beans.factory.<span style="color:#ca7d37">annotation</span>.Value;</span></code><code><span><span style="color:#ca7d37">import</span> org.springframework.boot.SpringApplication;</span></code><code><span><span style="color:#ca7d37">import</span> org.springframework.boot.autoconfigure.SpringBootApplication;</span></code><code><span><span style="color:#ca7d37">import</span> org.springframework.web.bind.<span style="color:#ca7d37">annotation</span>.GetMapping;</span></code><code><span><span style="color:#ca7d37">import</span> org.springframework.web.bind.<span style="color:#ca7d37">annotation</span>.RestController;</span></code>
<code><span><span style="color:#afafaf">@RestController</span></span></code><code><span><span><span style="color:#ca7d37">class</span> <span style="color:#0e9ce5">MyController</span> </span>&#123;</span></code>
<code><span>  <span style="color:#afafaf">@Value(<span>"<span style="color:#ca7d37">$&#123;JAVA_HOME&#125;</span>"</span>)</span></span></code><code><span>  String JavaHome;</span></code>
<code><span>  <span style="color:#afafaf">@GetMapping(<span>"/"</span>)</span></span></code><code><span>  <span style="color:#ca7d37">public</span> String hello() &#123;</span></code><code><span>    <span style="color:#ca7d37">return</span> <span style="color:#ca7d37">this</span>.JavaHome + <span style="color:#dd1144">" - Hello World!"</span>;</span></code><code><span>  &#125;</span></code><code><span>  </span></code><code><span>&#125;</span></code>
<code><span><span style="color:#afafaf">@SpringBootApplication</span></span></code><code><span><span style="color:#ca7d37">public</span> <span><span style="color:#ca7d37">class</span> <span style="color:#0e9ce5">Demo11Application</span> </span>&#123;</span></code>
<code><span>  <span style="color:#ca7d37">public</span> static void main(String[] args) &#123;</span></code><code><span>    SpringApplication.run(Demo11Application.<span style="color:#ca7d37">class</span>, args);</span></code><code><span>  &#125;</span></code><code><span>  </span></code><code><span>&#125;</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">下面是使用 Go-Spring 的依赖注入能力实现的能同时打印 GOPATH 环境变量和<span> </span><span>Hell</span><span>o</span><span> World</span><span>!</span><span> 的程序。代码如下。</span></p> 
<pre><code><span>package main</span></code>
<code><span><span style="color:#ca7d37">import</span> (</span></code><code><span>  <span style="color:#dd1144">"github.com/go-spring/spring-core/gs"</span></span></code><code><span>  <span style="color:#dd1144">"github.com/go-spring/spring-core/web"</span></span></code><code><span>  <span style="color:#0e9ce5">_</span> <span style="color:#dd1144">"github.com/go-spring/starter-gin"</span></span></code><code><span>)</span></code>
<code><span><span><span style="color:#ca7d37">func</span> <span style="color:#dd1144">init</span><span>()</span></span> &#123;</span></code><code><span>  gs.<span style="color:#0e9ce5">Object</span>(new(<span style="color:#0e9ce5">MyController</span>)).<span style="color:#0e9ce5">Init</span>(<span><span style="color:#ca7d37">func</span><span>(<span style="color:#ca7d37">c</span> *MyController)</span></span> &#123;</span></code><code><span>    gs.<span style="color:#0e9ce5">GetMapping</span>(<span style="color:#dd1144">"/"</span>, <span style="color:#ca7d37">c</span>.<span style="color:#0e9ce5">Hello</span>)</span></code><code><span>  &#125;)</span></code><code><span>&#125;</span></code>
<code><span>type <span style="color:#0e9ce5">MyController</span> <span><span style="color:#ca7d37">struct</span> </span>&#123;</span></code><code><span>  <span style="color:#0e9ce5">GoPath</span> string `value:<span style="color:#dd1144">"$&#123;GOPATH&#125;"</span>`</span></code><code><span>&#125;</span></code>
<code><span><span><span style="color:#ca7d37">func</span> <span>(<span style="color:#ca7d37">c</span> *MyController)</span></span> <span style="color:#0e9ce5">Hello</span>(ctx web.<span style="color:#0e9ce5">Context</span>) &#123;</span></code><code><span>  ctx.<span style="color:#0e9ce5">String</span>(<span style="color:#ca7d37">c</span>.<span style="color:#0e9ce5">GoPath</span> + <span style="color:#dd1144">" - Hello World!"</span>)</span></code><code><span>&#125;</span></code>
<code><span><span><span style="color:#ca7d37">func</span> <span style="color:#dd1144">main</span><span>()</span></span> &#123;</span></code><code><span>  gs.<span style="color:#0e9ce5">Run</span>()</span></code><code><span>&#125;</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">比较上面两个示例，可以看出 Go-Spring 真正实现了 Go 和 Java Spring 的融合，在保持 Go (语法) 简单的同时具备 Java Spring 的强大配置能力。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">通过本文的介绍，你有没有对 Go-Spring 动心呢？赶紧动手试试吧！</p>
                                        </div>
                                      
</div>
            