
---
title: '从Kratos设计看Go微服务工程实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210714/4076012e50b42e8ee1665b6a5c751d78.png'
author: Dockone
comments: false
date: 2021-07-15 09:07:10
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210714/4076012e50b42e8ee1665b6a5c751d78.png'
---

<div>   
<br><h3>导读</h3>github.com/go-kratos/kratos（以下简称Kratos）是一套轻量级Go微服务框架，致力于提供完整的微服务研发体验，整合相关框架及周边工具后，微服务治理相关部分可对整体业务开发周期无感，从而更加聚焦于业务交付。Kratos在设计之初就考虑到了高可扩展性，组件化，工程化，规范化等。对每位开发者而言，整套Kratos框架也是不错的学习仓库，可以了解和参考微服务的技术积累和经验。<br>
<br>接下来我们从<strong>Protobuf</strong>、<strong>开放性</strong>、<strong>规范</strong>、<strong>依赖注入</strong>这4个点了解一下Kratos在Go微服务工程领域的实践。<br>
<h3>基于Protocol Buffers（Protobuf）的生态</h3>在Kratos中，API定义、gRPC Service、HTTP Service、请求参数校验、错误定义、Swagger API json、应用服务模版等都是基于Protobuf IDL来构建的：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210714/4076012e50b42e8ee1665b6a5c751d78.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210714/4076012e50b42e8ee1665b6a5c751d78.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
举一个简单的helloworld.proto例子：<br>
<pre class="prettyprint">syntax = "proto3";<br>
<br>
package helloworld;<br>
<br>
import "google/api/annotations.proto";<br>
import "protoc-gen-openapiv2/options/annotations.proto";<br>
import "validate/validate.proto";<br>
import "errors/errors.proto";<br>
<br>
option go_package = "github.com/go-kratos/kratos/examples/helloworld/helloworld";<br>
<br>
// The greeting service definition.<br>
service Greeter &#123;<br>
// Sends a greeting<br>
rpc SayHello (HelloRequest) returns (HelloReply)  &#123;<br>
option (google.api.http) = &#123;<br>
// 定义一个HTTP GET接口，并且把name映射到HelloRequest<br>
get: "/helloworld/&#123;name&#125;",<br>
    &#125;;<br>
// 添加API接口描述（swagger api）<br>
option (grpc.gateway.protoc_gen_openapiv2.options.openapiv2_operation) = &#123;<br>
description: "这是SayHello接口";<br>
    &#125;;<br>
&#125;<br>
&#125;<br>
<br>
// The request message containing the user's name.<br>
message HelloRequest &#123;<br>
// 增加name字段参数校验，字符数需在1到16之间<br>
string name = 1 [(validate.rules).string = &#123;min_len: 1, max_len: 16&#125;];<br>
&#125;<br>
<br>
// The response message containing the greetings<br>
message HelloReply &#123;<br>
string message = 1;<br>
&#125;<br>
<br>
enum ErrorReason &#123;<br>
// 设置缺省错误码<br>
option (errors.default_code) = 500;<br>
// 为某个错误枚举单独设置错误码<br>
USER_NOT_FOUND = 0 [(errors.code) = 404];<br>
CONTENT_MISSING = 1 [(errors.code) = 400];;<br>
&#125; <br>
</pre><br>
以上是一个简单的helloworld服务定义的例子，这里我们定义了一个Service叫Greeter，给Greeter添加了一个SayHello的接口，并根据googleapis规范给这个接口添加了Restful风格的HTTP接口定义，然后还利用openapiv2添加了接口的Swagger API描述，同时还给请求消息结构体HelloRequest中的name字段加上了参数校验，最后我们在文件的末尾还定义了这个服务可能返回的错误码。<br>
<br>这时我们在终端中执行：kratos proto client api/helloworld/ helloworld.proto，便可以生成以下文件：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210714/b00781237214869b6ad914f301891004.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210714/b00781237214869b6ad914f301891004.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
由上，我们看到Kraots脚手架工具帮我们一键生成了上面提到的能力。从这个例子中，我们可以直观感受到使用使用Protobuf带来的开发效率的提升，除此之外Kratos还有以下优点：<br>
<ul><li><strong>清晰</strong>：做到了定义即文档，定义即代码</li><li><strong>收敛、统一</strong>：将逻辑都收敛统一到一起，通过代码生成工具来保证HTTP Service、gRPC Service等功能具有一致的行为</li><li><strong>跨语言</strong>：众所周知Protobuf是跨语言的，Java、Go、Python、PHP、JS、C等等主流语言都支持</li><li><strong>拥抱开源生态</strong>：比如Kratos复用了google.http.api、protoc-gen-openapiv2、protoc-gen-validate等等一些犀利的Protobuf周边生态工具或规范，这比起自己造一个IDL的轮子要容易维护得多，同时老的使用这些轮子的gRPC项目迁移成本也更低</li></ul><br>
<br><h3>开放性</h3>一个基础框架在设计的时候就要考虑未来的可扩展性，那Kratos是怎么做的呢？<br>
<h4>Server Transport</h4>我们先看下服务协议层的代码：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210714/feb181daf1b903a4ed076e2fb37ffa93.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210714/feb181daf1b903a4ed076e2fb37ffa93.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
上面是Kratos RPC服务协议层的接口定义，这里我们可以看到如果想要给Kratos新增一个新的服务协议，只要实现Start()、Stop()、Endpoint()这几个方法即可。这样的设计解耦了应用和服务协议层的实现，使得扩展服务协议更加方便。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210714/bfb2cb73cd928baaf88b5de63505ef6f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210714/bfb2cb73cd928baaf88b5de63505ef6f.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
从上图中我们可以看到App层无需关心底层服务协议的实现，只是一个容器管理好应用配置、服务生命周期、加载顺序即可。<br>
<h4>Log</h4>我们再看一个Kratos日志模块的设计：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210714/a8a7c23b25aaf907bcdc0f87557919c4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210714/a8a7c23b25aaf907bcdc0f87557919c4.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这里Kratos定义了一个日志输出接口Logger，它的设计的非常简单 - 只用了一个方法、两个输入、一个输出。我们知道一个包暴露的接口越少，越容易维护，同时对使用和实现方的心智负担更小，扩展日志实现会变得更容易。但问题来了，这个接口从功能上来讲似乎只能输出日志level和固定的kv paris，如何能支持更高级的功能？比如输出caller stack、实时timestamp、 context traceID？这里我们定义了一个回调接口Valuer：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210714/3dfbe807860ec245675eb4b295d2a2c2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210714/3dfbe807860ec245675eb4b295d2a2c2.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这个Valuer可以被当作key/value pairs中的value被Append到日志里，并被实时调用。<br>
<br>我们看一下如何给日志加时间戳的Valuer实现：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210714/6fff1d58d3149cc2dfa5eb64c74043dd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210714/6fff1d58d3149cc2dfa5eb64c74043dd.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
使用时只要在原始的logger上再append一个固定的key和一个动态的valuer即可：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210714/dd7325aef1b6dbadaf5e503dce023154.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210714/dd7325aef1b6dbadaf5e503dce023154.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这里的With是一个Helper function，里面new了一个新的logger（也实现了Logger接口），并将key\value pairs暂存在新的logger里，等到Log方法被调用时再通过断言.(Valuer)的方式获取值并输出给底层原始的logger。<br>
<br>所以我们可以看到仅仅通过两个简单的接口+一个Helper function的组合我们就实现了日志的大多数功能，这样大大提高了可扩展性。实际上还有日志过滤、多日志源输出等功能也是通过组合使用这两接口来实现，这里待下次分享再展开细讲。<br>
<h4>Tracing</h4>最后我们来看下Kratos的Tracing组件，这里Kratos采用的是CNCF项目OpenTelemetry。<br>
<br>OpenTelemetry在设计之初就考虑到了组件化和高可扩展性，其实现了OpenTracing和W3C Trace Context的规范，可以无缝对接Zipkin、Jaeger等主流开源Tracing系统，并且可以自定义Propagator和TraceProvider。通过otel.SetTracerProvider()我们可以轻易得替换Span的落地协议和格式，从而兼容老系统中的trace采集agent；通过otel.SetTextMapPropagtor()我们可以替换Span在RPC中的Encoding协议，从而可以和老系统中的服务互相调用时也能兼容。<br>
<h3>工程流程</h3>我们知道在工程实践的时候，强规范和约束往往比自由和更多的选择更有优势，那么在Go工程规范这块我这里主要介绍三块：<br>
<h4>面向包的设计规范</h4>Go是一个面向包名设计的语言，Package在Go程序中主要起到功能隔离的作用，标准库就是很好的设计范例。Kratos也是可以按包进行组织代码结构，这里我们抽取Kratos根目录下主要几个Package包来看下：<br>
<ul><li><strong>/cmd</strong>：可以通过go install一键安装生成工具，使用户更加方便地使用框架。</li><li><strong>/api</strong>：Kratos框架本身的暴露的接口定义。</li><li><strong>/errors</strong>：统一的业务错误封装，方便返回错误码和业务原因。</li><li><strong>/config</strong>：支持多数据源方式，进行配置合并铺平，通过Atomic方式支热更配置。</li><li><strong>/internal</strong>：存放对外不可见或者不稳定的接口。</li><li><strong>/transport</strong>：服务协议层（HTTP/gRPC）的抽象封装，可以方便获取对应的接口信息。</li><li><strong>/middleware</strong>：中间件抽象接口，主要跟transport和service之间的桥梁适配器。</li><li><strong>/third_party</strong>：第三方外部的依赖。</li></ul><br>
<br>可以看到Kratos的包命名清晰简短，按功能进行划分，每个包具有唯一的职责。<br>
<br>在设计包时我们还需要考虑到以下几点：<br>
<ul><li>包的设计必须以使用者为中心，直观且易于使用，包的命名必须旨在描述它提供的内容，如果包的名称不能立即暗示这一点，则它可能包含一组零散的功能。  </li><li>包的目的是为特定问题域而提供的，为了有目的，包必须提供，而不是包含。包不能成为不同问题域的聚合地，随着时间的推移，它将影响项目的简洁和重构、适应、扩展和分离的能力。</li><li>高便携性，尽量减少依赖其他代码库，一个包与其它包依赖越少，一个包的可重用性就越高。</li><li>不能成为单点依赖，当包被单一的依赖点时，就像一个公共包（common），会给项目带来很高的耦合性。</li></ul><br>
<br><h4>配置</h4>首先，我们来看下常见的基础框架是怎么初始化配置的：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210714/83c50228dd1986e0134a902e869daced.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210714/83c50228dd1986e0134a902e869daced.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这是Go标准库HTTP Server配置初始化的例子，但是这样做会有如下几个问题：<br>
<ul><li>&http.Server&#123;&#125;由于是一个取址引用，里面的参数可能会被外部运行时修改，这种运行时修改带来的危害是不可把控的。</li><li>无法区分nil和0值，当里面的参数值为0的时候，不知道是用户未设置还是就是被设置成了0。</li><li>难以分辨必传和选传参数，只能通过文档说明来隐式约定，没有强约束力。</li></ul><br>
<br>那么Kraots是怎么解决这些问题的呢？答案就是Functional Options 。我们看下transport/http/client.go的代码：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210714/f29fb95bb98b739f753df5dfce824112.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210714/f29fb95bb98b739f753df5dfce824112.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Client.go中定义了一个回调函数ClientOption，该函数接受一个定义了一个存放实际配置的未导出结构体clientOptions的指针，然后我们在NewClient的时候，使用可变参数进行传递，然后再初始化函数内部通过for循环调用修改相关的配置。<br>
<br>这么做有这么几个好处：<br>
<ul><li>由于clientOptions结构体是未导出的，那么就不存在被外部修改的可能。</li><li>可以区分0值和未设置，首先我们在new clientOptions时会设置默认参数，那么如果外部没有传递相应的Option就不会修改这个默认参数。</li><li>必选参数显示定义，可选值则通过Go可变参数进行传递，很好的区分必传和选传。</li></ul><br>
<br><h4>Error规范</h4>Kratos为微服务提供了统一的Error模型：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210714/3bf1f8e1328c2bf30cf738e642e53998.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210714/3bf1f8e1328c2bf30cf738e642e53998.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>Code用作外部展示和初步判断，服务端无需定义大量全局唯一的XXX_NOT_FOUND，而是使用一个标准Code.NOT_FOUND错误代码并告诉客户端找不到某个资源。错误空间变小降低了文档的复杂性，在客户端库中提供了更好的惯用映射，并降低了客户端的逻辑复杂性。同时这种标准的大类Code的存在也对外部的观测系统更友好，比如可以通过分析Nginx Access Log中的HTTP StatusCode来做服务端监控和告警。</li><li>Reason是具体的错误原因，可以用来更详细的错误判定。每个微服务都会定义自己Reason，那么要保持全局唯一就需要加上领域前缀，比如User_XXX。</li><li>Message错误信息可以帮助用户轻松快捷地理解和解决API错误。</li><li>Metadata中则可以存放一些标准的错误详情，比如retryInfo、error stack等。</li><li>这种强制规范，避免了开发人员直接透传Go的error从而导致一些敏感信息泄露。</li></ul><br>
<br>接下来我们看下Error结构体还实现了哪些接口：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210714/28286421a1ac92d9686e5622055032d8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210714/28286421a1ac92d9686e5622055032d8.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>实现了GRPCStatus () *status.Status接口，这样就实现了从http status code到grpc status code的转换，这样Kratos Error可以被gRPC直接转成google.rpc.Status传递出去。</li><li>实现了标准库errors包的Is (error) bool接口，这样使用者可以直接调用errors.Is()来比较两个erorr中的reason是否相等，避免了使用==来直接判断error是否相等这种错误姿势。</li></ul><br>
<br><h3>依赖注入</h3>依赖注入（Dependency Injection）可以理解为一种代码的构造模式，按照这样的方式来写，能够让你的代码更加容易维护，一般在Java的项目中见到的比较多。<br>
<br>依赖注入初看起来比较违反直觉，那么为什么Go也需要依赖注入？假设我们要实现一个用户访问计数的功能。我们先看看不使用依赖注入的项目代码：<br>
<pre class="prettyprint">type Service struct &#123;<br>
redisCli *redis.Client<br>
&#125;<br>
<br>
func (s *Service) AddUserCount(ctx context.Context) &#123;<br>
//do some business logic<br>
s.redisCli.Incr(ctx, "user_count")<br>
&#125;<br>
<br>
func NewService(cfg *redis.Options) *Service &#123;<br>
return &Service&#123;redisCli: redis.NewClient(cfg)&#125;<br>
&#125; <br>
</pre><br>
这种方式比较常见，在项目刚开始或者规模小的时候没什么问题，但我们如果考虑下面这些因素：<br>
<ul><li>Redis是基础组件，往往会在项目的很多地方被依赖，那么如果哪天我们想整体修改Redis SDK的甚至想把Redis整体替换成MySQL时，需要在每个被用到的地方都进行修改，耗时耗力还容易出错。  </li><li>很难对App这个类写单元测试，因为我们需要创建一个真实的redis.Client。</li></ul><br>
<br>使用依赖注入改造后的Service：<br>
<pre class="prettyprint">type DataSource interface&#123;<br>
Incr(context.Context, string)<br>
&#125;<br>
<br>
type Service struct &#123;<br>
dataSource DataSource<br>
&#125;<br>
<br>
func (s *Service) AddUserCount(ctx context.Context) &#123;<br>
//do some business logic<br>
s.dataSource.Incr(ctx, "user_count")<br>
&#125;<br>
<br>
func NewService(ds DataSource) *Service &#123;<br>
return &Service&#123;dataSource: ds&#125;<br>
&#125; <br>
</pre><br>
上面代码中我们把*redis.Client实体替换成了一个DataSource接口，同时不控制dataSource的创建和销毁，把dataSource生命周期控制权交给了上层来处理，以上操作有三个主要原因：<br>
<ul><li>因为Service层已不再关心dataSource的创建和销毁，这样当我们需要修改dataSource实现的时候，只要在上层统一修改即可，无需在各个被依赖的地方一一修改。</li><li>因为依赖的是一个接口，我们写单元测试的时候只要传递一个mock后的Datasource实现即可 。</li><li>这里dataSource这个基础组件不再被会到处创建，可以做到复用一个单例节省资源开销。</li></ul><br>
<br>Go的依赖注入框架有两类，一类是通过反射在运行时进行依赖注入，典型代表是Uber开源的dig，另外一类是通过generate进行代码生成，典型代表是Google开源的wire。使用dig功能会强大一些，但是缺点就是错误只能在运行时才能发现，这样如果不小心的话可能会导致一些隐藏的bug出现。使用wire的缺点就是功能限制多一些，但是好处就是编译的时候就可以发现问题，并且生成的代码其实和我们自己手写相关代码差不太多，更符合直觉，心智负担更小。所以Kratos更加推荐wire，Kratos的默认项目模板中kratos-layout也正是使用了google/wire进行依赖注入。<br>
<br>我们来看下wire使用方式：<br>
<br>我们首先要定义一个ProviderSet，这个Set会返回构建依赖关系所需的组件Provider。如下所示，Provider往往是一些简单的工厂函数，这些函数不会太复杂：<br>
<pre class="prettyprint">type RedisSource struct &#123;<br>
redisCli *redis.Client<br>
&#125;<br>
<br>
// RedisSource实现了Datasource的Incr接口<br>
func (ds *RedisSource) Incr(ctx context.Context, key string) &#123;<br>
ds.redisCli.Incr(ctx, key)<br>
&#125;<br>
<br>
// 构建实现了DataSource接口的Provider<br>
func NewRedisSource(db *redis.Client) *RedisSource &#123;<br>
return &RedisSource&#123;redisCli: db&#125;<br>
&#125;<br>
<br>
// 构建*redis.Client的Provider<br>
func NewRedis(cfg *redis.Options) *redis.Client &#123;<br>
return redis.NewClient(cfg)<br>
&#125;<br>
// 这是一个Provider的集合，告诉wire这个包提供了哪些Provider<br>
var ProviderSet = wire.NewSet(NewRedis, NewRedisSource)<br>
</pre><br>
接着我们要在应用启动处新建一个wire.go文件并定义Injector，Injctor会分析依赖关系并将Provider串联起来构建出最终的Service：<br>
<pre class="prettyprint">// +build wireinject<br>
<br>
func initService(cfg *redis.Options) *service.Service &#123;<br>
panic(wire.Build(<br>
    redisSource.ProviderSet,<br>
//使用wire.Bind将Struct和接口进行绑定了，表示这个结构体实现了这个接口<br>
wire.Bind(new(data.DataSource), new(*redisSource.RedisSource)),<br>
    service.NewService),<br>
)<br>
&#125; <br>
</pre><br>
最后执行wire .后自动生成的代码如下：<br>
<pre class="prettyprint">//go:generate go run github.com/google/wire/cmd/wire<br>
//+build !wireinject<br>
<br>
func initService(cfg *redis.Options) *service.Service &#123;<br>
client := redis2.NewRedis(cfg)<br>
redisSource := redis2.NewRedisSource(client)<br>
serviceService := service.NewService(redisSource)<br>
return serviceService<br>
&#125; <br>
</pre><br>
由此我们可以看到只要定义好组件初始化的Provider函数，还有把这些Provider组装在一起的Injector就可以直接生成初始化链路代码了，上手还是相对简单的，生成的代码所见即所得，容易Debug。<br>
<br>综上可见，Kraots是一款凝结了开源社区力量以及Go同学们大量微服务工程实践后诞生的一款微服务框架。现在腾讯云微服务治理治理平台（微服务平台TSF）也已支持Kratos框架，给Kratos赋予了更多企业级服务治理能力、提供多维度服务，如：应用生命周期托管、一键上云、私有化部署、多语言发布。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/ZCoc3qA_r1fKzPOURA2V2g" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/ZCoc3qA_r1fKzPOURA2V2g</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            