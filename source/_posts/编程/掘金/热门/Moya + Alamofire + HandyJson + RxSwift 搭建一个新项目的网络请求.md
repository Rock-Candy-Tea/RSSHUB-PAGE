
---
title: 'Moya + Alamofire + HandyJson + RxSwift 搭建一个新项目的网络请求'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4053518b57648f79cacf7e565df21be~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 03 Apr 2021 07:38:04 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4053518b57648f79cacf7e565df21be~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1、前言</h3>
<p>说起来汗颜。</p>
<p>最近项目才开始使用 <code>Swift</code> 语言，正如我一个朋友嘲笑的：<strong>我们都快用烂的东西你们才开始用</strong> ，我当时竟无言以对。</p>
<p>那既然用了 <code>Swift</code>，就要想办法用舒服，用明白。从 <code>OC</code> 工程转换到 <code>Swift</code> 工程，OC 的一些库，比如：网络请求库（AFNetworking），Json解析（YYModel）, 响应式编程（RAC），还有网络请求的封装库(自己封装的或者第三方的) 就要按需更换了。</p>
<h3 data-id="heading-1">2、第三库的选择</h3>
<h4 data-id="heading-2">1、网络请求库</h4>
<p>毫无疑问是 <a href="https://github.com/Alamofire/Alamofire" target="_blank" rel="nofollow noopener noreferrer">Alamofire</a> 了，就和 OC 项目选择 AFNetworking 一样。</p>
<h4 data-id="heading-3">2、Json 解析</h4>
<p><code>Swift</code> 也有不少，比如 <a href="https://github.com/SwiftyJSON/SwiftyJSON" target="_blank" rel="nofollow noopener noreferrer">SwiftyJSON</a>，<a href="https://github.com/alibaba/HandyJSON" target="_blank" rel="nofollow noopener noreferrer">HandyJSON</a> 等。</p>
<p><code>SwiftyJSON</code> 非常强大，能帮助开发者将 Json 转成字典，按照 key 值取出时也帮助开发者进行路径判空，但是，我个人感觉用起来有点奇怪。</p>
<p>后来选择了阿里的 <a href="https://github.com/alibaba/HandyJSON" target="_blank" rel="nofollow noopener noreferrer">HandyJSON</a>，<code>HandyJSON</code> 也支持结构体，支持将 <code>Json</code> 转成对象，支持<strong>模型数组</strong>，因为 <code>Swift</code> 上对泛型的支持，所以对比 <code>OC</code> 上的  <code>YYModel</code> 用起来更舒服些。</p>
<h4 data-id="heading-4">3、响应式编程</h4>
<p><code>Swift</code> 是静态语言，采用链式函数编程，<code>Swift</code> 中使用响应式编程，会让 <code>Swift</code> 更加简单和轻巧。</p>
<p>目前可以选择有很多，比如 <a href="https://github.com/ReactiveCocoa/ReactiveCocoa" target="_blank" rel="nofollow noopener noreferrer">ReactiveCocoa(Swift)</a>，<a href="https://github.com/ReactiveX/RxSwift" target="_blank" rel="nofollow noopener noreferrer">RxSwift</a>，<code>Swift Combine(苹果自己的)</code>，各有优点缺点，各位客官可以自由比对选择，如果第一次接触的话，就自己随意选一个（毕竟使用过了才能对比）。</p>
<ul>
<li>
<p><a href="https://github.com/ReactiveX/RxSwift" target="_blank" rel="nofollow noopener noreferrer">RxSwift</a> 维护人员较多，这意味着你能轻易找到问题的解决方案，并且 <code>RxSwift</code> 是 <code>ReactiveX</code> 的一个而已，它还有 <code>RxJava</code>，<code>RxPython</code> 等等。学会了一个，说不定其他都是一样哦。</p>
</li>
<li>
<p><a href="https://github.com/ReactiveCocoa/ReactiveCocoa" target="_blank" rel="nofollow noopener noreferrer">ReactiveCocoa(Swift)</a>，这个是从 OC 上翻译过来的，有一些历史的 OC 包袱，但是原来熟悉 RAC 的会更容易上手。</p>
</li>
<li>
<p><code>Swift Combine</code> 是苹果自己的，自己的亲儿子，未来更新的几率会更大，并且不会出现第三库不在维护更新的。</p>
</li>
</ul>
<h4 data-id="heading-5">4、网络库封装</h4>
<p>如果你们公司 OC 项目上，有在网络库上再次封装的好用、强大的库，那么这个你就不用看了，你肯定只能混编。</p>
<p>对于之前自己项目只有简单再封装 AFNetworking 或者是新项目的，推荐使用 <a href="https://github.com/Moya/Moya" target="_blank" rel="nofollow noopener noreferrer">Moya</a>。</p>
<p><code>Moya</code>只是对 <code>Alamofire</code> 的再次封装，并不是网络请求库，所以使用 <code>Moya</code>就需要使用 <code>Alamofire</code>。</p>
<blockquote>
<p>既然是网络库的再次封装，那么就可以将 <code>Alamofire</code> 替换成其他的，只需要重写 <code>Moya+Alamofire.swift</code> 就可以了。我个人感觉一般没必要。</p>
</blockquote>
<h3 data-id="heading-6">3、使用方法</h3>
<p><a href="https://github.com/Moya/Moya" target="_blank" rel="nofollow noopener noreferrer">Moya</a> 是对 <code>Alamofire</code> 的再封装，如果只是使用的话，关心 <code>Moya</code> 的使用方法即可。</p>
<p>Moya 分别提供了<a href="https://github.com/Moya/Moya/tree/master/docs" target="_blank" rel="nofollow noopener noreferrer">Moya英文文档</a> 和 <a href="https://github.com/Moya/Moya/tree/master/docs_CN" target="_blank" rel="nofollow noopener noreferrer">Moya中文文档</a>。（英文文档更全面）</p>
<h4 data-id="heading-7">1、熟悉 Moya</h4>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4053518b57648f79cacf7e565df21be~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>下载官方的 Demo 后，先熟悉一下 <code>Moya</code> 的用法。</p>
<ul>
<li><a href="https://github.com/Moya/Moya/blob/master/docs/Examples/Basic.md" target="_blank" rel="nofollow noopener noreferrer">Moya使用方式官方英文文档</a></li>
<li><a href="https://github.com/Moya/Moya/blob/master/docs_CN/Examples/Basic.md" target="_blank" rel="nofollow noopener noreferrer">Moya使用方式官方中文文档</a></li>
</ul>
<p>文档已经很详细，这里简单说明一下</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-comment">/// 创建一个文件 MyService.swift</span>

<span class="hljs-comment">/// 声明一个枚举</span>
<span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">MyService</span> &#123;</span>
    <span class="hljs-comment">/// 分类放置你的请求调用函数</span>
    <span class="hljs-function"><span class="hljs-keyword">case</span> <span class="hljs-title">createUser</span><span class="hljs-params">(firstName: String, lastName: String)</span>
&#125;


<span class="hljs-comment">/// 扩展你的枚举，遵守 TargetType 协议</span>
extension MyService: TargetType </span>&#123;
    var baseURL:  &#123;
        <span class="hljs-comment">/// 放入 host</span>
        <span class="hljs-keyword">return</span> baseURL;
    &#125;
    var path: String &#123;
        <span class="hljs-function"><span class="hljs-keyword">case</span> <span class="hljs-title">createUser</span><span class="hljs-params">(let firstName, let lastName)</span>
            <span class="hljs-comment">/// 返回具体请求路径</span>
            <span class="hljs-keyword">return</span> "/user/create/user"
    &#125;
    var method: Moya.Method </span>&#123;
        <span class="hljs-keyword">switch</span> self &#123;
        <span class="hljs-keyword">case</span> .createUser:
            <span class="hljs-comment">/// 返回 .get 或者 .post</span>
            <span class="hljs-keyword">return</span> .post;
        &#125;
    &#125;
    
    var task: Task &#123;
        <span class="hljs-keyword">switch</span> self &#123;
        <span class="hljs-keyword">case</span> .createUser(let firstName, let lastName): 
            <span class="hljs-comment">/// 具体请求参数</span>
            <span class="hljs-keyword">return</span> .requestParameters(parameters: [<span class="hljs-string">"first_name"</span>: firstName, <span class="hljs-string">"last_name"</span>: lastName], encoding: JSONEncoding.<span class="hljs-keyword">default</span>)
        &#125;
    &#125;
    
    var sampleData: Data &#123;
        <span class="hljs-comment">/// 如果服务器给了测试示例，可以放到这里</span>
        <span class="hljs-keyword">case</span> .createUser(let firstName, let lastName): 
           <span class="hljs-keyword">return</span> <span class="hljs-string">"&#123;\"id\": 100, \"first_name\": \"\(firstName)\", \"last_name\": \"\(lastName)\"&#125;"</span>.utf8Encoded 
    &#125;
    
    var headers: [String: String]? &#123;
        <span class="hljs-comment">/// 请求头设置</span>
        <span class="hljs-keyword">return</span> [<span class="hljs-string">"Content-type"</span>: <span class="hljs-string">"application/json"</span>]
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后你就可以在你的 ViewController 调用了：</p>
<pre><code class="hljs language-c copyable" lang="c">let provider = MoyaProvider<MyService>()
provider.request(.createUser(firstName: <span class="hljs-string">"James"</span>, lastName: <span class="hljs-string">"Potter"</span>)) &#123; result in
    <span class="hljs-comment">// do something with the result (read on for more details)</span>
&#125;

<span class="hljs-comment">// The full request will result to the following:</span>
<span class="hljs-comment">// POST https://api.myservice.com/users</span>
<span class="hljs-comment">// Request body:</span>
<span class="hljs-comment">// &#123;</span>
<span class="hljs-comment">//   "first_name": "James",</span>
<span class="hljs-comment">//   "last_name": "Potter"</span>
<span class="hljs-comment">// &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">2、了解 Moya</h4>
<p>上面只是初步使用了一下 <code>Moya</code>，但是具体业务远比 Demo 复杂的多，Moya 也给我们提供相当充足的施展空间。</p>
<p>第一步还是创建一个文件，声明一个枚举，实现 <code>TargetType</code> 协议。但是创建 <code>MoyaProvider</code> 对象就不同了。</p>
<p>上方代码只是使用了 <code>let provider = MoyaProvider<MyService>()</code> 创建，其实 <code>MoyaProvider</code> 中还有其他参数的。具体来看一下：</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-comment">/// Initializes a provider.</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">init</span><span class="hljs-params">(endpointClosure: @escaping EndpointClosure = MoyaProvider.defaultEndpointMapping,
                requestClosure: @escaping RequestClosure = MoyaProvider.defaultRequestMapping,
                stubClosure: @escaping StubClosure = MoyaProvider.neverStub,
                callbackQueue: DispatchQueue? = nil,
                manager: Manager = MoyaProvider<Target>.defaultAlamofireManager(),
                plugins: [PluginType] = [],
                trackInflights: Bool = <span class="hljs-literal">false</span>)</span> </span>&#123;

        self.endpointClosure = endpointClosure
        self.requestClosure = requestClosure
        self.stubClosure = stubClosure
        self.manager = manager
        self.plugins = plugins
        self.trackInflights = trackInflights
        self.callbackQueue = callbackQueue
    &#125;

    <span class="hljs-comment">/// Returns an `Endpoint` based on the token, method, and parameters by invoking the `endpointClosure`.</span>
    open func endpoint(_ token: Target) -> Endpoint &#123;
        <span class="hljs-keyword">return</span> endpointClosure(token)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里看到 <code>MoyaProvider</code> 对象 <code>init</code> 的时候还额外提供了 <strong>7</strong> 个参数，只是如果你使用了默认的 <code>init</code>，其他会被自动赋上默认值。</p>
<h5 data-id="heading-9">1、endpointClosure</h5>
<p>默认源码如下：</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">final</span> class func <span class="hljs-title">defaultEndpointMapping</span><span class="hljs-params">(<span class="hljs-keyword">for</span> target: Target)</span> -> Endpoint </span>&#123;
    <span class="hljs-keyword">return</span> Endpoint(
        url: URL(target: target).absoluteString,
        sampleResponseClosure: &#123; .networkResponse(<span class="hljs-number">200</span>, target.sampleData) &#125;,
        method: target.method,
        task: target.task,
        httpHeaderFields: target.headers
        )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里是将创建的遵守协议的枚举 <code>MyService</code> 转化成 <code>Endpoint</code>，往往我们只是使用它的默认方法。 查阅 <code>Endpoint</code> ，发现还提供了两个方法：</p>
<ul>
<li>
<p><code>open func adding(newHTTPHeaderFields: [String: String]) -> Endpoint</code> ：用于更改请求头。</p>
</li>
<li>
<p><code>open func replacing(task: Task) -> Endpoint</code> ： 将原有 <code>MyService</code> 枚举中实现的 <code>task</code> 进行替换。</p>
</li>
</ul>
<p>但是有时候也有业务测试的需求，如：网络错误,超时等。就可以在这里实现。</p>
<blockquote>
<p>Moya官方解释：由于它是一个闭包, 它将在每次调用API时被执行, 所以你可以做任何你想要的操作。</p>
</blockquote>
<p><code>Moya</code> 给了一个例子，只需要将对象 <code>failureEndpointClosure</code> 传入 <code>MoyaProvider</code> 的参数<code>endpointClosure</code> 即可。</p>
<pre><code class="hljs language-c copyable" lang="c">let failureEndpointClosure = &#123; (target: MyService) -> Endpoint in
    let sampleResponseClosure = &#123; () -> (EndpointSampleResponse) in
        <span class="hljs-keyword">if</span> shouldTimeout &#123;
            <span class="hljs-keyword">return</span> .networkError(NSError())
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> .networkResponse(<span class="hljs-number">200</span>, target.sampleData)
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> Endpoint(url: URL(target: target).absoluteString, 
        sampleResponseClosure: sampleResponseClosure, 
        method: target.method, 
        task: target.task)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里可以将 <code>MyService</code> 转化成 <code>Endpoint</code> 对象的时候可以任意改变参数，满足各种测试需求。</p>
<h5 data-id="heading-10">2、requestClosure</h5>
<p>根据 <code>Endpoint</code> 生成 <code>URLRequest</code>。</p>
<p>默认源码如下：</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">final</span> class func <span class="hljs-title">defaultRequestMapping</span><span class="hljs-params">(<span class="hljs-keyword">for</span> endpoint: Endpoint, closure: RequestResultClosure)</span> </span>&#123;
    <span class="hljs-keyword">do</span> &#123;
        let urlRequest = <span class="hljs-keyword">try</span> endpoint.urlRequest()
        closure(.success(urlRequest))
    &#125; <span class="hljs-keyword">catch</span> MoyaError.requestMapping(let url) &#123;
        closure(.failure(MoyaError.requestMapping(url)))
    &#125; <span class="hljs-keyword">catch</span> MoyaError.parameterEncoding(let error) &#123;
        closure(.failure(MoyaError.parameterEncoding(error)))
    &#125; <span class="hljs-keyword">catch</span> &#123;
        closure(.failure(MoyaError.underlying(error, nil)))
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码中看到，通过 <code>let urlRequest = try endpoint.urlRequest()</code> 方式由 <code>Endpoint</code> 生成一个 <code>URLRequest</code>对象，就意味着可以修改 <code>URLRequest</code> 中的参数，比如需要给 <code>URLRequest</code> 设置 <code>timeoutInterval</code> 等。</p>
<p>示例如下：</p>
<pre><code class="hljs language-c copyable" lang="c">let requestClosure = &#123; (endpoint: Endpoint, done: MoyaProvider.RequestResultClosure) in
    <span class="hljs-keyword">do</span> &#123;
        var request: URLRequest = <span class="hljs-keyword">try</span> endpoint.urlRequest()
        request.httpShouldHandleCookies = <span class="hljs-literal">false</span>
        request.timeoutInterval = <span class="hljs-number">15</span>
        done(.success(request))
    &#125; <span class="hljs-keyword">catch</span> &#123;
        done(.failure(MoyaError.underlying(error, nil)))
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">3、stubClosure</h5>
<p>这个参数提供了3个枚举：</p>
<ul>
<li>
<p><code>.never</code> (默认的)：直接请求服务器；</p>
</li>
<li>
<p><code>.immediate</code>：走协议中 <code>sampleData</code> 示例数据；</p>
</li>
<li>
<p><code>.delayed(seconds)</code> 可以把 stub 请求延迟指定时间，例如， <code>.delayed(0.2)</code> 可以把每个 stub 请求延迟 0.2s 。 这个在单元测试中来模拟网络请求是非常有用的。</p>
</li>
</ul>
<p>官方示例：</p>
<pre><code class="hljs language-c copyable" lang="c">let stubClosure =  &#123; target: MyService -> Moya.StubBehavior in
    <span class="hljs-keyword">switch</span> target &#123;
        <span class="hljs-comment">/* Return something different based on the target. */</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">4、callbackQueue</h5>
<p>回调线程。</p>
<h5 data-id="heading-13">5、manager</h5>
<p>这里直接使用官方解释了，大多工程这里都用默认的。</p>
<p>接下来就是 session 参数，默认会获得一个通过基本配置进行初始化的自定义的 Alamofire.Session 实例对象</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">final</span> class func <span class="hljs-title">defaultAlamofireSession</span><span class="hljs-params">()</span> -> Session </span>&#123;
    let configuration = URLSessionConfiguration.<span class="hljs-keyword">default</span>
    configuration.headers = .<span class="hljs-keyword">default</span>
    
    <span class="hljs-keyword">return</span> Session(configuration: configuration, startRequestsImmediately: <span class="hljs-literal">false</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这儿只有一个需要注意的事情：由于在 AF 中创建一个 <code>Alamofire.Request</code> 对象时默认会立即触发请求，即使为单元测试进行 "stubbing" 请求也一样。 因此在Moya中, <code>startRequestsImmediately</code> 属性被默认设置成了 <code>false</code> 。</p>
<p>如果你需要自定义自己的 session ， 比如说创建一个 <code>SSL pinning</code> 并且添加到 <code>session</code> 中，所有请求将通过自定义配置的 <code>session</code> 进行路由。</p>
<pre><code class="hljs language-c copyable" lang="c">let serverTrustManager = ServerTrustManager(evaluators: [<span class="hljs-string">"example.com"</span>: PinnedCertificatesTrustEvaluator()])

let session = Session(
    configuration: configuration, 
    startRequestsImmediately: <span class="hljs-literal">false</span>, 
    serverTrustManager: serverTrustManager
)

let provider = MoyaProvider<MyTarget>(session: session)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">6、plugins</h5>
<p><code>plugins</code> 是一个拦截器数组，可以传入多个遵守 <code>PluginType</code> 协议的对象。查阅 <code>PluginType</code> 协议：</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-comment">///     - inject additional information into a request</span>
<span class="hljs-keyword">public</span> protocol PluginType &#123;
    <span class="hljs-comment">/// Called to modify a request before sending.</span>
    <span class="hljs-comment">/// requestClosure 生成 URLRequest 生成之后回调此方法</span>
    <span class="hljs-function">func <span class="hljs-title">prepare</span><span class="hljs-params">(_ request: URLRequest, target: TargetType)</span> -> URLRequest

    <span class="hljs-comment">/// Called immediately before a request is sent over the network (or stubbed).</span>
    <span class="hljs-comment">/// 网络请求发出前回调此方法</span>
    func <span class="hljs-title">willSend</span><span class="hljs-params">(_ request: RequestType, target: TargetType)</span>

    <span class="hljs-comment">/// Called after a response has been received, but before the MoyaProvider has invoked its completion handler.</span>
    <span class="hljs-comment">/// 收到数据，Moya 还没有进行处理是回调此方法</span>
    func <span class="hljs-title">didReceive</span><span class="hljs-params">(_ result: Result<Moya.Response, MoyaError>, target: TargetType)</span>

    <span class="hljs-comment">/// Called to modify a result before completion.</span>
    <span class="hljs-comment">/// 在网络 callBack 闭包回调前回调此方法</span>
    func <span class="hljs-title">process</span><span class="hljs-params">(_ result: Result<Moya.Response, MoyaError>, target: TargetType)</span> -> Result<Moya.Response, MoyaError>
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>这里能干的事情太多。</p>
<ul>
<li>比如：<code>func prepare(_ request: URLRequest, target: TargetType) -> URLRequest</code> 方法回调后，可以将公共参数（版本号，token，userid）进行拼接，或者对数据进行 <code>RSA</code> 加密加签。</li>
</ul>
<p>举个 🌰 ：</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-comment">/// Called to modify a request before sending.</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> func <span class="hljs-title">prepare</span><span class="hljs-params">(_ request: URLRequest, target: TargetType)</span> -> URLRequest </span>&#123;
    <span class="hljs-comment">/// 这里做公共参数</span>
    
    let target = target as! MyService
    var parameters : [String: Any]?
    <span class="hljs-keyword">if</span> let requstData = request.httpBody &#123;
        <span class="hljs-keyword">do</span> &#123;
            let json = <span class="hljs-keyword">try</span> JSONSerialization.jsonObject(with: requstData, options: .mutableContainers)
            parameters = json as? [String: Any]
        &#125; <span class="hljs-keyword">catch</span>  &#123;
            <span class="hljs-comment">/// 失败处理 ...</span>
        &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
        parameters = [String: Any]()
    &#125;
    
    <span class="hljs-comment">/// 拼接公共参数</span>
    parameters = paramsForPublicParmeters(parameters: parameters)
    
    <span class="hljs-comment">/// 加密加签</span>
    parameters = RSA.sign(withParamDic: parameters)
    
    <span class="hljs-keyword">do</span> &#123;
        <span class="hljs-comment">/// 替换 httpBody</span>
        <span class="hljs-keyword">if</span> let parameters = parameters &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">try</span> request.encoded(parameters: parameters, parameterEncoding: JSONEncoding.<span class="hljs-keyword">default</span>)
        &#125;
    &#125; <span class="hljs-keyword">catch</span>  &#123;
        <span class="hljs-comment">/// 失败处理 ...</span>
    &#125;
    
    <span class="hljs-keyword">return</span> request
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>比如：<code>func process(_ result: Result<Moya.Response, MoyaError>, target: TargetType) -> Result<Moya.Response, MoyaError></code> 方法回调后，可以对数据进行验签解密。</li>
</ul>
<p>举个 🌰 ：</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-comment">/// Called to modify a result before completion.</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> func <span class="hljs-title">process</span><span class="hljs-params">(_ result: Result<Moya.Response, MoyaError>, target: TargetType)</span> -> Result<Moya.Response, MoyaError> </span>&#123;
    
    <span class="hljs-comment">/// 验签</span>
    <span class="hljs-keyword">if</span> <span class="hljs-keyword">case</span> .success(let response) = result &#123;
        <span class="hljs-keyword">do</span> &#123;
            let responseString = <span class="hljs-keyword">try</span> response.mapJSON()
            
            <span class="hljs-comment">/// Json 转成 字典</span>
            let dic =  JsonToDic(responseString)
            
            <span class="hljs-comment">/// 验签</span>
            <span class="hljs-keyword">if</span> let _ = SignUntil.verifySign(withParamDic: dic) &#123;
                
                <span class="hljs-comment">/// 数据解密</span>
                dic = RSA.decodeRSA(withParamDic: dic)
                
                <span class="hljs-comment">/// 重新生成 Moya.response</span>
                <span class="hljs-comment">/// ...</span>
                
                <span class="hljs-comment">/// 返回 Moya.response</span>
                <span class="hljs-keyword">return</span> .success(response)
            &#125; <span class="hljs-keyword">else</span> &#123;
                let error = NSError(domain: <span class="hljs-string">"验签失败"</span>, code: <span class="hljs-number">1</span>, userInfo: nil)
                <span class="hljs-keyword">return</span> .failure(MoyaError.underlying(error, nil))
            &#125;
        &#125; <span class="hljs-keyword">catch</span> &#123;
            let error = NSError(domain: <span class="hljs-string">"拦截器 response 转 json 失败"</span>, code: <span class="hljs-number">1</span>, userInfo: nil)
            <span class="hljs-keyword">return</span> .failure(MoyaError.underlying(error, nil))
        &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">/// 原本就失败了就丢回了</span>
        <span class="hljs-keyword">return</span> result
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>你还可以在 <code>willSend</code> 和 <code>didReceive</code> 做日志打印：</li>
</ul>
<p>举个 🌰 ：</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-comment">/// 准备发送的时候拦截打印日志</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> func <span class="hljs-title">willSend</span><span class="hljs-params">(_ request: RequestType, target: TargetType)</span> </span>&#123;
    <span class="hljs-comment">/// 请求日志打印</span>
    NetWorkingLoggerOutPut.outPutLoggerRequest(request.request, andRequestURL: request.request?.url?.absoluteString)
&#125;

<span class="hljs-comment">/// 将要接受的时候拦截打印日志</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> func <span class="hljs-title">didReceive</span><span class="hljs-params">(_ result: Result<Moya.Response, MoyaError>, target: TargetType)</span> </span>&#123;
    <span class="hljs-comment">/// 返回日志打印</span>
    <span class="hljs-keyword">switch</span> result &#123;
    <span class="hljs-keyword">case</span> .success(let response):
        NetWorkingLoggerOutPut.outPutLoggerReponseString(response.response, andRequest: response.request, andResponseObj:tryResponseToJSON(response: response) )
    <span class="hljs-keyword">case</span> .failure(let error):
        NetWorkingLoggerOutPut.outPutLoggerReponseString(error.response?.response, andRequest: error.response?.request, andResponseObj: tryResponseToJSON(response: error.response))
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，这只是一些代码片段，但是重要代码已经贴出来了，你可以以此为灵感继续扩展。</p>
<h5 data-id="heading-15">7、trackInflights</h5>
<p>一个请求在 <code>init</code> 的时候将 <code>trackInflights</code> 设置为 <code>true</code>，那么在 <code>Moya</code> 中就会存储这个请求的 <code>endpoint</code>。在返回数据的时候，如果需要跟踪了重复请求，那么就将一次实际发送请求返回的数据，多次返回。</p>
<h3 data-id="heading-16">3、使用 Moya</h3>
<p>3.1 和 3.2 基本上对 Moya 的使用详细说明了，这里就说调用方式吧。</p>
<h4 data-id="heading-17">1、普通调用方式</h4>
<pre><code class="hljs language-c copyable" lang="c">let provider = MoyaProvider(endpointClosure: endpointClosure,
                        requestClosure: requestClosure,
                        stubClosure: stubClosure,
                        manager: manager,
                        plugins: plugins)
                        
provider.request(.createUser(<span class="hljs-string">"三"</span>,<span class="hljs-string">"张"</span>)) &#123; result in
    <span class="hljs-keyword">do</span> &#123;
        let response = <span class="hljs-keyword">try</span> result.get()
        let value = <span class="hljs-keyword">try</span> response.mapNSArray()
        self.repos = value
    &#125; <span class="hljs-keyword">catch</span> &#123;
        let printableError = error as CustomStringConvertible
        self.showAlert(<span class="hljs-string">"GitHub Fetch"</span>, message: printableError.description)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">2、RxSwift 调用方式</h4>
<p>如果使用 <code>RxSwift</code> 需要导入库 <code>RxMoya</code>，根据 <code>Moya</code> 官方主页导入即可。</p>
<pre><code class="hljs language-c copyable" lang="c">provider.rx.request(.createUser(<span class="hljs-string">"三"</span>,<span class="hljs-string">"张"</span>))
    .asObservable()
    .mapJSON()
    .mapHandyModel(type: UserModel.self)
    .asSingle()
    .subscribe &#123; (userModel) in
        
    &#125; onFailure: &#123; (error) in
        
    &#125; onDisposed: &#123;
        
    &#125;
    .disposable(by:disposable)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">3、Moya 的二次封装</h4>
<p>看完上面的内容，应该对 <code>Moya</code> 有一定的了解了，实际开发中，我们需要涉及的东西相当的多。比如，不同的接口可能需要不同的网络超时时间、还能可能需要配置接口需不需要对用户信息的验证，是否走本地测试数据，等等。</p>
<p>还有一些，比如 <code>baseURL</code> ，网络请求头 <code>headers</code> ， <code>HTTPMethod</code> 大多都是一样的，如果每次都重新设置，那有一天改了 <code>baseURL</code> 的地址，<code>headers</code> 都需要增加一个参数，那时候杀人的心都有了。</p>
<h5 data-id="heading-20">1、扩展 TargetType 协议</h5>
<p>既然 <code>Moya</code> 已经提供了 <code>TargetType</code> 我们何不扩展一下呢？</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">public</span> protocol BaseHttpAPIManager: TargetType &#123;
    
    <span class="hljs-comment">///是否验证用户身份</span>
    var validUser : Bool &#123; get &#125;
    
    <span class="hljs-comment">///超时时间</span>
    var timeoutInterval : Double &#123; get &#125;
    
    <span class="hljs-comment">/// 是否走测试数据 默认 .never</span>
    var stubBehavior: Moya.StubBehavior &#123; get &#125;
    
    <span class="hljs-comment">/// 等等 ... </span>
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>协议继承完成之后，这里就可以对我们基本不变化的参数进行赋值。</p>
<pre><code class="hljs language-c copyable" lang="c">extension BaseHttpAPIManager &#123;
  
    <span class="hljs-keyword">public</span> var baseURL: URL &#123;
        <span class="hljs-keyword">return</span> URL(<span class="hljs-built_in">string</span>: WebService.shared.BaseURL)!
    &#125;
    
    <span class="hljs-keyword">public</span> var method: Moya.Method &#123;
        <span class="hljs-keyword">return</span> .post
    &#125;
    
    <span class="hljs-keyword">public</span> var sampleData: Data &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"response: test data"</span>.data(<span class="hljs-keyword">using</span>: String.Encoding.utf8)!
    &#125;
    
    <span class="hljs-keyword">public</span> var task: Task &#123;
        <span class="hljs-keyword">return</span> .requestPlain
    &#125;
    
    <span class="hljs-comment">///是否验证成功码</span>
    <span class="hljs-keyword">public</span> var validationType: Moya.ValidationType &#123;
        <span class="hljs-keyword">return</span> .successCodes
    &#125;
    
    <span class="hljs-comment">///请求头</span>
    <span class="hljs-keyword">public</span> var headers: [String : String]? &#123;
        <span class="hljs-keyword">return</span> WebService.shared.HttpHeaders
    &#125;
    
    
    <span class="hljs-comment">///以下为自定义扩展</span>
    
    <span class="hljs-keyword">public</span> var validUser : Bool &#123;
        <span class="hljs-keyword">return</span> WebService.shared.ValidUser
    &#125;
    
    <span class="hljs-keyword">public</span> var timeoutInterval : Double &#123;
        <span class="hljs-keyword">return</span> WebService.shared.TimeoutInterval
    &#125;
    
    <span class="hljs-comment">/// 是否走测试数据 默认 .never</span>
    <span class="hljs-keyword">public</span> var stubBehavior: StubBehavior &#123;
        <span class="hljs-keyword">return</span> .never
    &#125;
    
     <span class="hljs-comment">//...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为 <code>TargetType</code> 协议是贯穿 <code>Moya</code> 整个核心的，所以你基本可以在任意地方使用它。之后只需要实现遵守 <code>BaseHttpAPIManager</code> 协议就可以了。</p>
<h5 data-id="heading-21">2、将 MoyaProvider 的创建封装</h5>
<p>这里我就不写代码了，我推荐一个 <a href="https://github.com/chensx1993/moyaManager" target="_blank" rel="nofollow noopener noreferrer">GitHub 上的 Demo</a> 看一下，本菜鸡也是从这里借鉴的。</p>
<h3 data-id="heading-22">4、使用 HandyJson</h3>
<p>因为 HandyJson 可以支持结构体。<code>Swift</code> 中如果不需要继承的类，建议使用结构体，占用内存更小。</p>
<h4 data-id="heading-23">1、声明</h4>
<p>声明一个 <code>struct</code> 或者 <code>class</code>，必须支持 <code>HandyJSON</code> 协议。</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">UserModel</span> :</span> HandyJSON &#123;
    var name    : String?
    var age     : Int?
    var address : String?
    var hobby   : [HobbyModel]? <span class="hljs-comment">/// 支持模型数组，但是需要将数组中类型写清楚</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">2、使用</h4>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-comment">/// 普通模型转换</span>
let parsedElement = UserModel.deserialize(from: AnyObject)

<span class="hljs-comment">/// 数组模型转换</span>
let parsedArray = [UserModel].deserialize(from: AnyObject)

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">3、联合 RxSwfit 使用</h4>
<p>扩展 <code>Observable</code> 就可以了。</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-keyword">public</span> extension Observable where Element : Any &#123;
    
    <span class="hljs-comment">/// 普通 Json 转 Model</span>
    func mapHandyModel <T : HandyJSON> (type : T.Type) -> Observable<T?> &#123;
        <span class="hljs-keyword">return</span> self.<span class="hljs-built_in">map</span> &#123; (element) -> T? in
        
            <span class="hljs-comment">/// 这里的data 是 String 或者 dic</span>
            let data = element
            
            let parsedElement : T?
            <span class="hljs-keyword">if</span> let <span class="hljs-built_in">string</span> = data as? String &#123;
                parsedElement = T.deserialize(from: <span class="hljs-built_in">string</span>)
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> let dictionary = data as? Dictionary<String , Any> &#123;
                parsedElement = T.deserialize(from: dictionary)
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> let dictionary = data as? [String : Any] &#123;
                parsedElement = T.deserialize(from: dictionary)
            &#125; <span class="hljs-keyword">else</span> &#123;
                parsedElement = nil
            &#125;
            <span class="hljs-keyword">return</span> parsedElement
        &#125;
    &#125;
    
    <span class="hljs-comment">// 将 Json 转成 模型数组</span>
    func mapHandyModelArray<T: HandyJSON>(type: T.Type) -> Observable<[T?]?> &#123;
        <span class="hljs-keyword">return</span> self.<span class="hljs-built_in">map</span> &#123; (element) -> [T?]? in
        
            <span class="hljs-comment">/// 这里的data 是 String 或者 dic</span>
            let data = element
            
            let parsedArray : [T?]?
            <span class="hljs-keyword">if</span> let <span class="hljs-built_in">string</span> = data as? String &#123;
                parsedArray = [T].deserialize(from: <span class="hljs-built_in">string</span>)
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> let <span class="hljs-built_in">array</span> = data as? [Any] &#123;
                parsedArray = [T].deserialize(from: <span class="hljs-built_in">array</span>)
            &#125; <span class="hljs-keyword">else</span> &#123;
                parsedArray = nil
            &#125;
            <span class="hljs-keyword">return</span> parsedArray
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>联合方式上方 3.3.2 <code>Moya RxSwift 调用方式</code> 已经给出了。</p>
<pre><code class="hljs language-c copyable" lang="c">json.rx.mapHandyModel(type: UserModel.self)
    .asSingle()
    .subscribe &#123; (userModel) in
        
    &#125; onFailure: &#123; (error) in
        
    &#125; onDisposed: &#123;
        
    &#125;
    .disposable(by:disposable)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">5、RxSwift</h3>
<p>关于 <code>RxSwift</code> 的使用方式看 <a href="https://juejin.cn/post/6844903912542044173" target="_blank">Cooci 的博客 RxSwift 用法</a>。</p>
<h3 data-id="heading-27">6、总结</h3>
<p>有了这些，你就可以快速搭建新项目的网络请求了，如果感觉帮助了你些许，能给个赞最好了，感谢各位。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            