
---
title: 'yoyogo v1.7.5 发布，独立依赖注入 DI'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202107/15120501_DM51.jpg'
author: 开源中国
comments: false
date: Thu, 15 Jul 2021 11:29:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202107/15120501_DM51.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <div style="text-align:left"> 
 <h2>YoyoGo v1.7.5 🦄🌈 YoyoGo （Go语言框架）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F15014510.html%232913415430" target="_blank">#</a></h2> 
 <p><code>一个简单、轻量、快速、基于依赖注入的微服务框架( web 、grpc ),支持Nacos/Consoul/Etcd/Eureka/k8s /Apollo等 .</code></p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyoyofx%2Fyoyogo" target="_blank">https://github.com/yoyofx/yoyogo</a><br> <img alt src="https://static.oschina.net/uploads/img/202107/15120501_DM51.jpg" referrerpolicy="no-referrer"></p> 
 <h2>v1.7.5 更新内容<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F15014510.html%233979918040" target="_blank">#</a></h2> 
 <h2>Framework dependency:<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F15014510.html%233041687306" target="_blank">#</a></h2> 
 <ul> 
  <li>New dependency injection framework<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyoyofxteam%2Fdependencyinjection" target="_blank">https://github.com/yoyofxteam/dependencyinjection</a></li> 
 </ul> 
 <h2>Features：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F15014510.html%231098958950" target="_blank">#</a></h2> 
 <ul> 
  <li>Support grpc connection timeout with context. (fix)</li> 
 </ul> 
 <h2>Dependency injection<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F15014510.html%233879472712" target="_blank">#</a></h2> 
 <p>依赖注入是更广泛的控制反转技术的一种形式。它的作用是提高程序的模块化和可扩展性。</p> 
 <p>此次升级将DI独立，以便之后集成更多外围生态，开源地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyoyofxteam%2Fdependencyinjection" target="_blank">https://github.com/yoyofxteam/dependencyinjection</a></p> 
 <h2>YoyoGO框架API实例<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F15014510.html%231001355983" target="_blank">#</a></h2> 
 <pre><code class="language-go">type A struct &#123;
Name string
&#125;

func NewA() *A &#123;
r := rand.New(rand.NewSource(time.Now().UnixNano()))
name := "A-" + strconv.Itoa(r.Int())
return &A&#123;Name: ls&#125;
&#125;
// 高层API ， 用于IOC声明，不做DI容器表达。 支持三种生命周期如下：
// Singleton ServiceLifetime = 0 
// Scoped    ServiceLifetime = 1 
// Transient ServiceLifetime = 2
services := NewServiceCollection()
services.AddSingleton(NewA)
//serviceCollection.AddSingletonByImplementsAndName("redis-master", NewRedis, new(abstractions.IDataSource))
//serviceCollection.AddTransientByImplements(NewRedisClient, new(redis.IClient))
//serviceCollection.AddTransientByImplements(NewRedisHealthIndicator, new(health.Indicator))
serviceProvider := services.Build()

var env *A
_ = serviceProvider.GetService(&env) // used</code></pre> 
 <div>
   
 </div> 
 <h3>Installing<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F15014510.html%233272881439" target="_blank">#</a></h3> 
 <pre><code class="language-bash">go get -u github.com/yoyofxteam/dependencyinjection@v1.0.0</code></pre> 
 <div> 
  <h3>服务提供者<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F15014510.html%233451609669" target="_blank">#</a></h3> 
  <pre><code class="language-go">// NewServer creates a http server with provided mux as handler.
func NewServer(mux *http.ServeMux) *http.Server &#123;
return &http.Server&#123;
Handler: mux,
&#125;
&#125;

// NewServeMux creates a new http serve mux.
func NewServeMux() *http.ServeMux &#123;
return &http.ServeMux&#123;&#125;
&#125;</code></pre> 
  <p style="text-align:left"><code>支持的构造器签名如下</code></p> 
  <pre><code class="language-go">func([dep1, dep2, depN]) (result, [cleanup, error])</code></pre> 
  <h3>构建一个DI容器<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F15014510.html%233495712889" target="_blank">#</a></h3> 
  <pre><code class="language-go">import (
  di "github.com/yoyofxteam/dependencyinjection"
)

container := di.New(
// provide http server
    di.Provide(NewServer),
    // provide http serve mux
    di.Provide(NewServeMux)
)</code></pre> 
  <h3>获取容器中的实例<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F15014510.html%231447140039" target="_blank">#</a></h3> 
  <pre><code class="language-go">// declare type variable
var server *http.Server
// extracting
err := container.Extract(&server)
if err != nil &#123;
// check extraction error
&#125;

server.ListenAndServe()</code></pre> 
  <h3>注册Naming定义提供者<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F15014510.html%232545056110" target="_blank">#</a></h3> 
  <pre><code class="language-go">// MasterDatabase provide write database access.
type MasterDatabase struct &#123;
*Database
&#125;

// SlaveDatabase provide read database access.
type SlaveDatabase struct &#123;
*Database
&#125;

// 省略
// provide master database
di.Provide(NewMasterDatabase, di.WithName("master"))
// provide slave database
di.Provide(NewSlaveDatabase, di.WithName("slave"))

var database *Database
err := container.Extract(&database,di.Name(master))  // get master databse</code></pre> 
  <h3>依赖关联<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F15014510.html%23940195966" target="_blank">#</a></h3> 
  <p>可能实际的情况，类型间会有大量依赖，组件A依赖组件B，这种情况我们使用 di.Parameter 来声明结构体，对其它提供者提供多依赖管理：</p> 
  <pre><code class="language-go">// ServiceParameters
type ServiceParameters struct &#123;
di.Parameter
MasterDatabase *Database `di:"master"`
SlaveDatabase *Database  `di:"slave,optional"`   // optional 可选参数，如果没有实例则为nil
&#125;

// NewService creates new service with provided parameters.
func NewService(parameters ServiceParameters) *Service &#123;
return &Service&#123;
MasterDatabase:  parameters.MasterDatabase,
SlaveDatabase: parameters.SlaveDatabase,
&#125;
&#125;</code></pre> 
  <h3>Cleanup函数<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F15014510.html%23977402252" target="_blank">#</a></h3> 
  <p>提供者构造器返回清理函数用于销毁实例和释放资源,它由容器的container.Cleanup()函数统一管理：</p> 
  <pre><code class="language-go">func NewFile(log Logger, path Path) (*os.File, func(), error) &#123;
    f, err := os.Open(string(path))
    if err != nil &#123;
        return nil, nil, err
    &#125;
    cleanup := func() &#123;
        if err := f.Close(); err != nil &#123;
            log.Log(err)
        &#125;
    &#125;
    return f, cleanup, nil
&#125;</code></pre> 
  <p> </p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            