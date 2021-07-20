
---
title: 'Go 函数式编程：Higher-order function'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/488e2fc0d1094d81a70cac2f919f9ff9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 20:28:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/488e2fc0d1094d81a70cac2f919f9ff9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在请求处理过程中，应用程序会接受和处理请求，然后返回响应结果。在该过程中，还存在一些通用的功能，例如：鉴权、监控、链路追踪。众多 RPC 框架会提供称之为 Middleware 或者 Interceptor 等概念，以可插拔的方式来支持上述谈到的众多功能。以 gRPC 为例，工作原理如图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/488e2fc0d1094d81a70cac2f919f9ff9~tplv-k3u1fbpfcp-zoom-1.image" alt="grpc-interceptors.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其服务端的接口如下所示：</p>
<pre><code class="hljs language-hljs copyable" lang="hljs">func UnaryServerInterceptor(ctx context.Context, req interface&#123;&#125;, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface&#123;&#125;, error)

func StreamServerInterceptor (srv interface&#123;&#125;, stream grpc.ServerStream, info *grpc.StreamServerInfo, handler grpc.StreamHandler) error
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，接口明确定义了输入参数，输出结果。如果我们要自己实现一个组件，需要支持使用者传入特定的配置，有没有什么办法可以做到呢？</p>
<p>答案是肯定的。</p>
<h3 data-id="heading-0"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cyningsun.com%2F07-19-2021%2Fgo-higher-order-function.html%23Higher-order-function" title="https://www.cyningsun.com/07-19-2021/go-higher-order-function.html#Higher-order-function" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer"></a>Higher-order function</h3>
<p>在了解具体的解决方案之前，需要先了解一个概念叫<code>Higher-order function（高阶函数）</code></p>
<p>高阶函数是指至少支持以下特定之一的函数：</p>
<ol>
<li>将一个或多个函数作为参数（即过程参数），</li>
<li>返回函数作为其结果</li>
</ol>
<p>第二点，正是需要的特性。以限流的 interceptor 为例，支持传入自定义的限流器。此时就需要定义一个以限流器为参数的高阶函数，然后返回的函数是框架需要的 Interceptor，并在 Interceptor 函数内使用传入的限流器判断是否需要限流。按照接口限流的 Interceptor 具体实现为：</p>
<pre><code class="hljs language-hljs copyable" lang="hljs">type Limiter interface &#123;
Limit(key string) bool
&#125;

func UnaryServerInterceptor(limiter Limiter) grpc.UnaryServerInterceptor &#123;
return func(ctx context.Context, req interface&#123;&#125;, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface&#123;&#125;, error) &#123;
if limiter.Limit(info.FullMethod) &#123;
return nil, status.Errorf(codes.ResourceExhausted, "%s is rejected by grpc_ratelimit middleware, please retry later.", info.FullMethod)
&#125;
return handler(ctx, req)
&#125;
&#125;

...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目前传入的参数是固定的，可以这么来实现。更进一步，如果使用比较复杂，除了当前已经确定的参数，可以预期以后会增加更多的参数。也就要求当前设计的接口需要有很好的扩展性。还有办法么？</p>
<p>答案同样是肯定的。</p>
<h3 data-id="heading-1"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cyningsun.com%2F07-19-2021%2Fgo-higher-order-function.html%23Functional-Options" title="https://www.cyningsun.com/07-19-2021/go-higher-order-function.html#Functional-Options" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer"></a>Functional Options</h3>
<p>没有意外，利用的就是高阶函数的第一点，该编程模式有一个特定的名称：Functional Options。</p>
<p>首先为传入的参数定义结构体</p>
<pre><code class="hljs language-hljs copyable" lang="hljs">type options struct &#123;
    byMethod  bool
    byUser    bool
    byClientIP bool
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其次，再定义一个函数类型：</p>
<pre><code class="hljs language-hljs copyable" lang="hljs">type Option func(*Options)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次，定义修改配置的一组函数</p>
<pre><code class="hljs language-hljs copyable" lang="hljs">func ByMethod(m bool) Option &#123;
    return func(o *options) &#123;
        o.byMethod = m
    &#125;
&#125;

func ByUser(u bool) Option &#123;
    return func(o *options) &#123;
        o.byUser = u
    &#125;
&#125;

func ByClientIP(c bool) Option &#123;
    return func(o *options) &#123;
        o.byClientIP = c
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，修改提供的 Interceptor 为：</p>
<pre><code class="hljs language-hljs copyable" lang="hljs">func UnaryServerInterceptor(limiter Limiter, opts ...Option) grpc.UnaryServerInterceptor &#123;
return func(ctx context.Context, req interface&#123;&#125;, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface&#123;&#125;, error) &#123;
        default := options &#123;
            byMethod: true,
            byUser: false,
            byClientIP: false,
        &#125;
        for _, opt := range opts &#123;
            opt(&default)
        &#125;
        ...
return handler(ctx, req)
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如是，你就拥有了一个具有扩展性、支持自定义参数的 Interceptor。</p>
<h3 data-id="heading-2"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cyningsun.com%2F07-19-2021%2Fgo-higher-order-function.html%23%25E6%259C%2580%25E5%2590%258E" title="https://www.cyningsun.com/07-19-2021/go-higher-order-function.html#%E6%9C%80%E5%90%8E" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer"></a>最后</h3>
<p>做个总结，谈个观点：</p>
<ol>
<li>高阶函数，并不是属于哪一个特定的编程语言。其他语言如C++，同样支持类似的特性。</li>
<li>作为架构师需要了解实现细节么，答案是需要。否则，在特定环境下，拿什么来支撑设计所谓的扩展性呢。</li>
</ol>
<p><strong>本文作者</strong>：cyningsun<br>
<strong>本文地址</strong>： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cyningsun.com%2F07-19-2021%2Fgo-higher-order-function.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cyningsun.com/07-19-2021/go-higher-order-function.html" ref="nofollow noopener noreferrer">www.cyningsun.com/07-19-2021/…</a><br>
<strong>版权声明</strong>：本博客所有文章除特别声明外，均采用 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fcreativecommons.org%2Flicenses%2Fby-nc-nd%2F3.0%2Fcn%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://creativecommons.org/licenses/by-nc-nd/3.0/cn/" ref="nofollow noopener noreferrer">CC BY-NC-ND 3.0 CN</a> 许可协议。转载请注明出处！</p></div>  
</div>
            