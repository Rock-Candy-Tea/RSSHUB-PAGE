
---
title: 'gRPC的错误处理实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211116/34edc04b25ee05c5ea78916820c1d513.png'
author: Dockone
comments: false
date: 2021-11-20 02:24:17
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211116/34edc04b25ee05c5ea78916820c1d513.png'
---

<div>   
<br>基于《<a href="http://dockone.io/article/2434612">石墨文档基于Kubernetes的Go微服务实践</a>》，我们这次把该内容中的错误码做了一个详细的介绍。<br>
<h3>背景</h3>我们内部系统全部统一采用<code class="prettyprint">gRPC</code>协议和<code class="prettyprint">protobuf</code>编解码。统一的好处在于不需要在做任何协议、编解码转换，这样就可以使我们所有业务采用同一个<code class="prettyprint">protobuf</code>仓库，基于<code class="prettyprint">CI/CD</code>工具实现许多自动化功能。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211116/34edc04b25ee05c5ea78916820c1d513.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211116/34edc04b25ee05c5ea78916820c1d513.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们要求所有服务提供者提前在独立的路径下定义好接口和错误码的<code class="prettyprint">protobuf</code>文件，然后提交到<code class="prettyprint">GitLab</code>，我们通过<code class="prettyprint">GitLab CI</code>的<code class="prettyprint">check</code>阶段对变更的<code class="prettyprint">protobuf</code>文件做<code class="prettyprint">format</code>、<code class="prettyprint">lint</code>、<code class="prettyprint">breaking</code>  检查。然后在<code class="prettyprint">build</code>阶段，会基于<code class="prettyprint">protobuf</code>文件中的注释自动产生文档，并推送至内部的微服务管理系统接口平台中，还会根据<code class="prettyprint">protobuf</code>文件自动构建<code class="prettyprint">Go/PHP/Node/Java</code>等多种语言的桩代码和错误码，并推送到指定对应的中心化仓库。推送到仓库后，我们就可以通过各语言的包管理工具拉取客户端、服务端的gRPC和错误码的依赖，不需要口头约定对接数据的定义，也不需要通过<code class="prettyprint">IM</code>工具传递对接数据的定义文件，极大的简化了对接成本。<br><br>
<h3>判断Error的错误原理</h3>要了解怎么处理<code class="prettyprint">gRPC</code>的<code class="prettyprint">error</code>之前，我们首先来看下<code class="prettyprint">Go</code>普通的<code class="prettyprint">error</code>是怎么处理的。<br>
<br>我们在判断一个<code class="prettyprint">error</code>的根因，需要根因<code class="prettyprint">error</code>是一个固定地址的指针类型，这样我们才能够使用官方的<code class="prettyprint">errors.Is</code>方法判断他是否为根因。以下是一个代码示例：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211116/fe7a2802c8a7e8a458b9be96bf6379f6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211116/fe7a2802c8a7e8a458b9be96bf6379f6.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们先看这个代码<code class="prettyprint">errors.Is(wrapNewPointerError(), fmt.Errorf(&quot;i am error&quot;))</code>的执行步骤，首先构造了一个<code class="prettyprint">error</code>，然后使用官方<code class="prettyprint">%w</code>的方式将<code class="prettyprint">error</code>进行了包装，我们在使用<code class="prettyprint">errors.Is</code>方法判断的时候，底层函数会将<code class="prettyprint">error</code>解包来判断两个<code class="prettyprint">error</code>的地址是否一致。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211116/a303285bb625c0144c5b7afbafb21974.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211116/a303285bb625c0144c5b7afbafb21974.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
因此我们第一个<code class="prettyprint">errors.Is</code>执行的是个<code class="prettyprint">false</code>。在使用这个代码<code class="prettyprint">errors.Is(wrapConstantPointerError(), sentinelErr)</code>，因为是固定地址的<code class="prettyprint">error</code>，所以判断根因错误的时候，执行的是<code class="prettyprint">true</code>。<br>
<h3>gRPC网络传输的Error</h3>我们客户端在获取到<code class="prettyprint">gRPC</code>的<code class="prettyprint">error</code>的时候，是否可以使用上文说的官方<code class="prettyprint">errors.Is</code>进行判断呢。如果我们直接使用该方法，通过判断error地址是否相等，是无法做到的。原因是因为我们在使用<code class="prettyprint">gRPC</code>的时候，在远程调用过程中，客户端获取的服务端返回的<code class="prettyprint">error</code>，在<code class="prettyprint">tcp</code>传递的时候实际上是一串文本。客户端拿到这个文本，是要将其反序列化转换为<code class="prettyprint">error</code>，在这个反序列化的过程中，其实是<code class="prettyprint">new</code>了一个新的<code class="prettyprint">error</code>地址，这样就无法判断<code class="prettyprint">error</code>地址是否相等。<br>
<br>为了更好的解释<code class="prettyprint">gRPC</code>网络传输的<code class="prettyprint">error</code>，以下描述了整个<code class="prettyprint">error</code>的处理流程。<br>
<ul><li>客户端通过<code class="prettyprint">invoker</code>方法将请求发送到服务端。</li><li>服务端通过<code class="prettyprint">processUnaryRPC</code>方法，获取到用户代码的<code class="prettyprint">error</code>信息。</li><li>服务端通过<code class="prettyprint">status.FromError</code>方法，将<code class="prettyprint">error</code>转化为<code class="prettyprint">status.Status</code>。</li><li>服务端通过<code class="prettyprint">WriteStatus</code>方法将<code class="prettyprint">status.Status</code>里的数据，写入到<code class="prettyprint">grpc-status</code>、<code class="prettyprint">grpc-message</code>、<code class="prettyprint">grpc-status-details-bin</code>的<code class="prettyprint">header</code>头里。</li><li>客户端通过网络获取到这些<code class="prettyprint">header</code>头，使用<code class="prettyprint">strconv.ParseInt</code>解析到<code class="prettyprint">grpc-status</code>信息、<code class="prettyprint">decodeGrpcMessage</code>解析到<code class="prettyprint">grpc-message</code>信息、<code class="prettyprint">decodeGRPCStatusDetails</code>解析为<code class="prettyprint">grpc-status-details-bin</code>信息。</li><li>客户端通过<code class="prettyprint">a.Status().Err()</code>获取到用户代码的错误。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211116/6fce2548f3cf26dc8d321a21738002c3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211116/6fce2548f3cf26dc8d321a21738002c3.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
为了方便理解，我们抓个包，看下<code class="prettyprint">error</code>具体的报文情况。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211116/6d87a32d73d048724079d4e965d13ff0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211116/6d87a32d73d048724079d4e965d13ff0.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>检查gRPC的error信息第一版本</h3>通过上文描述，我们已经了解了<code class="prettyprint">gRPC</code>在网络中如何传输<code class="prettyprint">error</code>，可以看到<code class="prettyprint">new</code>出来的<code class="prettyprint">error</code>是无法判等的。所以我们就想到，使用工具提前生成好<code class="prettyprint">error</code>，这样<code class="prettyprint">error</code>的地址是不会改变的。这样我们就可以使用<code class="prettyprint">errors.Is</code>的方法去检查根因<code class="prettyprint">error</code>。<br>
<br>首先我们可以将错误码编写在<code class="prettyprint">proto</code>里，注释，如下所示：<br>
<pre class="prettyprint">syntax = "proto3";  <br>
package engineering.helloworld;  <br>
option go_package = "engineering/helloworld;helloworld";  <br>
// @plugins=protoc-gen-go-errors  <br>
// 错误  <br>
enum Error &#123;  <br>
// 未知类型  <br>
// @code=UNKNOWN  <br>
RESOURCE_ERR_UNKNOWN = 0;  <br>
// 找不到资源  <br>
// @code=NOT_FOUND  <br>
RESOURCE_ERR_NOT_FOUND = 1;  <br>
// 获取列表数据出错  <br>
// @code=INTERNAL  <br>
RESOURCE_ERR_LIST_MYSQL = 2;  <br>
// 获取详情数据出错  <br>
// @code=INTERNAL  <br>
RESOURCE_ERR_INFO_MYSQL = 3;  <br>
&#125;  <br>
</pre><br>
然后我们可以通过执行<code class="prettyprint">proto</code>错误插件，生成固定地址的<code class="prettyprint">error</code>，将<code class="prettyprint">error</code>注册到全局<code class="prettyprint">map</code>里，同时我们还可以根据<code class="prettyprint">@code</code>的注释，生成<code class="prettyprint">gRPC</code>的状态码。<br>
<pre class="prettyprint">func init() &#123;  <br>
resourceErrUnknown = eerrors.New(int(codes.Unknown), "engineering.helloworld.RESOURCE_ERR_UNKNOWN", Error_RESOURCE_ERR_UNKNOWN.String())  <br>
eerrors.Register(resourceErrUnknown)  <br>
resourceErrNotFound = eerrors.New(int(codes.NotFound), "engineering.helloworld.RESOURCE_ERR_NOT_FOUND", Error_RESOURCE_ERR_NOT_FOUND.String())  <br>
eerrors.Register(resourceErrNotFound)  <br>
resourceErrListMysql = eerrors.New(int(codes.Internal), "engineering.helloworld.RESOURCE_ERR_LIST_MYSQL", Error_RESOURCE_ERR_LIST_MYSQL.String())  <br>
eerrors.Register(resourceErrListMysql)  <br>
resourceErrInfoMysql = eerrors.New(int(codes.Internal), "engineering.helloworld.RESOURCE_ERR_INFO_MYSQL", Error_RESOURCE_ERR_INFO_MYSQL.String())  <br>
eerrors.Register(resourceErrInfoMysql)  <br>
&#125;  <br>
<br>
func ResourceErrUnknown() eerrors.Error &#123;  <br>
return resourceErrUnknown  <br>
&#125;  <br>
....  <br>
</pre><br>
接着我们在获取<code class="prettyprint">gRPC error</code>后，需要使用<code class="prettyprint">FromError</code>方法，转换为我们<code class="prettyprint">proto</code>生成的<code class="prettyprint">error</code>。在这个转换过程中，我们会从之前注册的全局<code class="prettyprint">error map</code>里，通过<code class="prettyprint">reason</code>方法，找到对应的<code class="prettyprint">error</code>，返回给用户。用户这个时候就可以通过<code class="prettyprint">errors.Is</code>来判断根因。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211116/9ce11bdb816ddce30c0dd4e1ee597647.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211116/9ce11bdb816ddce30c0dd4e1ee597647.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>检查gRPC的Error信息第二版本</h3>按以上方案，确实可以解决根因问题，但该<code class="prettyprint">error</code>，无法携带<code class="prettyprint">message</code>，<code class="prettyprint">metadata</code>信息。这就导致我们，很难准确定位一些问题。所以这个时候，我们需要在<code class="prettyprint">error</code>里做一些扩展，增加两个方法。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211116/7bc53261eeea6a76464524d238a3a718.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211116/7bc53261eeea6a76464524d238a3a718.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这种方式可以让我们携带信息，但是他会对原有的<code class="prettyprint">error</code>错误做一次克隆，导致了<code class="prettyprint">error</code>的地址变化，无法在通过<code class="prettyprint">error</code>判等的方式进行校验是否是根因。<br>
<br>这个时候，我们只能通过<code class="prettyprint">errors.Is</code>中的<code class="prettyprint">(interface&#123; Is(error) bool &#125;)</code>断言方式，在我们自定义的<code class="prettyprint">error</code>中，增加一个<code class="prettyprint">Is</code>方法来判断。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211116/ad08ba322191b541e614420432a93dc0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211116/ad08ba322191b541e614420432a93dc0.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
通过这种方式，我们不仅可以判断根因，并且还可以将<code class="prettyprint">error</code>里携带更多排查有用的信息。<br>
<h3>演示gRPC的Error的处理</h3>为了更好的演示error，我们将error处理的方式做成了工具，通过执行脚本，我们就可以下载到对应的工具<br>
<pre class="prettyprint">bash <(curl -L https://raw.githubusercontent.com/gotomicro/egoctl/main/getlatest.sh) <br>
</pre><br>
通过该工具，就可以执行我们<code class="prettyprint">ego error</code>的演示代码<br>
<h4>生成error、grpc的pb文件</h4>我们在该演示代码目录下执行<code class="prettyprint">make gen</code>，可以生成对应的<code class="prettyprint">error</code>、<code class="prettyprint">grpc</code>的<code class="prettyprint">pb</code>文件，如下所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211116/89190418887c9f4d89e7bc3904da6dc3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211116/89190418887c9f4d89e7bc3904da6dc3.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这些<code class="prettyprint">error</code>为了防止其他人不小心篡改，获取<code class="prettyprint">error</code>的时候，都是用方法来获取，如下所示。<br>
<pre class="prettyprint">func ResourceErrUnknown() eerrors.Error &#123;  <br>
return resourceErrUnknown  <br>
&#125;  <br>
</pre><br>
我们在<code class="prettyprint">server</code>里根据客户端发送的<code class="prettyprint">error</code>，返回我们<code class="prettyprint">proto</code>生成的<code class="prettyprint">error</code>信息。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211116/4ad626d792c7ea3d37472eb2b04b569c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211116/4ad626d792c7ea3d37472eb2b04b569c.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们在<code class="prettyprint">client</code>里，判断是否是这个<code class="prettyprint">error</code>，并记录<code class="prettyprint">error</code>里的错误信息。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211116/565f4b34e37dc82ffba70254166a00c8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211116/565f4b34e37dc82ffba70254166a00c8.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>执行指令</h4>在目录下执行<code class="prettyprint">make svc</code>，我们可以启动服务端 然后在目录下，我们在执行<code class="prettyprint">make cli</code>，我们可以启动客户端 执行完后，可以看到如下日志：<br>
<br>服务端展示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211116/2c28cd14aae4cabd2fd2738a774721fb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211116/2c28cd14aae4cabd2fd2738a774721fb.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>客户端展示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211116/65ebbdccf5d6b02209bf606c209253f5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211116/65ebbdccf5d6b02209bf606c209253f5.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到客户端红框里，就是我们业务代码里记录的日志。我们通过官方的errors.Is判断，能够很优雅的做一些业务逻辑处理。<br>
<h4>错误码查看</h4>错误码，我们可以全部放在<code class="prettyprint">proto</code>里管理。那么我们就可以很方便在<code class="prettyprint">proto</code>里查看错误码，或者做的更好一点，将<code class="prettyprint">proto</code>生成更好看的错误码文档。<br>
<br>自此我们将错误码进行了详细的介绍，下次我们会介绍<code class="prettyprint">gRPC</code>如何做单元测试和<code class="prettyprint">mock</code>服务的实践，如何通过<code class="prettyprint">proto</code>文件生成单元测试代码。<br>
<h3>鸣谢</h3>感谢<code class="prettyprint">kratos</code>的<code class="prettyprint">error</code>的处理和生成工具，通过学习它的代码和思想，我们将框架<code class="prettyprint">Ego</code>基于<code class="prettyprint">error</code>处理做了更多的改进，例如通过<code class="prettyprint">proto</code>的注解生成<code class="prettyprint">grpc</code>错误码，生成固定地址的<code class="prettyprint">error</code>。并且我们做了更多的<code class="prettyprint">proto</code>工具，可以通过<code class="prettyprint">proto</code>文件生成单元测试代码、API文档等。<br>
<br>相关链接：<br>
<ul><li>项目演示代码：<a href="https://github.com/gotomicro/go-engineering/tree/main/chapter_grpc_error/egoerror" rel="nofollow" target="_blank">https://github.com/gotomicro/g ... error</a></li><li>项目框架：<a href="https://github.com/gotomicro/ego" rel="nofollow" target="_blank">https://github.com/gotomicro/ego</a></li><li>proto生成插error件：<a href="https://github.com/gotomicro/ego/tree/master/cmd/protoc-gen-go-errors" rel="nofollow" target="_blank">https://github.com/gotomicro/e ... rrors</a></li><li>框架对error的处理：<a href="https://github.com/gotomicro/ego/blob/master/core/eerrors/errors.go" rel="nofollow" target="_blank">https://github.com/gotomicro/e ... rs.go</a></li><li>常量error：<a href="https://dave.cheney.net/2016/04/07/constant-errors" rel="nofollow" target="_blank">https://dave.cheney.net/2016/04/07/constant-errors</a></li><li>Go1.13Error Wrapping分析：<a href="https://www.flysnow.org/2019/09/06/go1.13-error-wrapping.html" rel="nofollow" target="_blank">https://www.flysnow.org/2019/0 ... .html</a></li></ul><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/3XLmGAlGDHfarbLyQoAh7Q" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/3XLmGAlGDHfarbLyQoAh7Q</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            