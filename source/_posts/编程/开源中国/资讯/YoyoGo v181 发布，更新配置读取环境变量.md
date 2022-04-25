
---
title: 'YoyoGo v1.8.1 发布，更新配置读取环境变量'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2706'
author: 开源中国
comments: false
date: Mon, 25 Apr 2022 15:47:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2706'
---

<div>   
<div class="content">
                                                                    
                                                        <h2>Features</h2> 
<ol> 
 <li>Get config value for DSL, that support key or ref object.</li> 
</ol> 
<h3>Such as YAML:</h3> 
<pre><code class="language-yaml">env: $&#123;CUSTOM_ENV&#125;
profile:
  dns: $&#123;REMOTE_HOST&#125;
  ip: $&#123;REMOTE_IP:10.0.1.12&#125;
  namespace: $&#123;MYNAMESPACE:space.localhost&#125;
</code></pre> 
<h3>Go Example</h3> 
<pre><code class="language-go">type Profile struct &#123;
    DNS string `config:"dns"`
    IP  string `config:"ip"`
    NS  string `config:"namespace"`
&#125;

config := abstractions.NewConfigurationBuilder().
       AddEnvironment().
       AddYamlFile("config").Build()

config.GetConfigObject("profile", &profile)
assert.Equal(t, profile.NS, "space.yoyogo.run")
assert.Equal(t, profile.DNS, "my host")
assert.Equal(t, profile.IP, "10.0.1.12")
</code></pre> 
<p>or</p> 
<pre><code class="language-go">env := config.Get("env")
dns := config.Get("profile.dns")
ip := config.Get("profile.ip")

assert.Equal(t, env, "my env variable")
assert.Equal(t, dns, "my host")
assert.Equal(t, ip, "10.0.1.12")
</code></pre> 
<hr> 
<p>YoyoGo 是一个用 Go 编写的简单，轻便，快速的微服务框架，目前已实现了Web框架的能力，但是底层设计已支持多种服务架构。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>特性</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>漂亮又快速的路由器</li> 
 <li>中间件支持 (handler func & custom middleware)</li> 
 <li>对 REST API 友好</li> 
 <li>支持 MVC 模式</li> 
 <li>受到许多出色的 Go Web 框架的启发</li> 
</ul>
                                        </div>
                                      
</div>
            