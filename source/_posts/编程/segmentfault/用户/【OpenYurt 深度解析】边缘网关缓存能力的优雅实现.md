
---
title: '【OpenYurt 深度解析】边缘网关缓存能力的优雅实现'
categories: 
 - 编程
 - segmentfault
 - 用户
headimg: 'https://segmentfault.com/img/remote/1460000039749595'
author: segmentfault
comments: false
date: 2021-03-31 12:10:41
thumbnail: 'https://segmentfault.com/img/remote/1460000039749595'
---

<div>   
<p><strong>简介：</strong> 阿里云边缘容器服务上线 1 年后，正式开源了云原生边缘计算解决方案 OpenYurt，跟其他开源的容器化边缘计算方案不同的地方在于：OpenYurt 秉持 Extending your native Kubernetes to edge 的理念，对 Kubernetes 系统零修改，并提供一键式转换原生 Kubernetes 为 OpenYurt，让原生 K8s 集群具备边缘集群能力。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039749595" alt="头图.png" title="头图.png" referrerpolicy="no-referrer"></span></p><p>作者 | 何淋波（新胜）<br>来源 | <a href="https://mp.weixin.qq.com/s/vdFrCDiIhPLVbOnf6vRxEw" rel="nofollow">阿里巴巴云原生公众号</a></p><h1>OpenYurt：延伸原生 K8s 的能力到边缘</h1><p>阿里云边缘容器服务上线 1 年后，正式开源了云原生边缘计算解决方案 OpenYurt，跟其他开源的容器化边缘计算方案不同的地方在于：OpenYurt 秉持 Extending your native Kubernetes to edge 的理念，对 Kubernetes 系统零修改，并提供一键式转换原生 Kubernetes 为 OpenYurt，让原生 K8s 集群具备边缘集群能力。</p><p>同时随着 OpenYurt 的持续演进，也一定会继续保持如下发展理念：</p><ul><li>非侵入式增强 K8s</li><li>保持和云原生社区主流技术同步演进</li></ul><h1>OpenYurt 如何解决边缘自治问题</h1><p>想要实现将 Kubernetes 系统延展到边缘计算场景，那么边缘节点将通过公网和云端连接，网络连接有很大不可控因素，可能带来边缘业务运行的不稳定因素，这是云原生和边缘计算融合的主要难点之一。</p><p>解决这个问题，需要使边缘侧具有自治能力，即当云边网络断开或者连接不稳定时，确保边缘业务可以持续运行。在 OpenYurt 中，该能力由 yurt-controller-manager 和 YurtHub 组件提供。</p><ol><li><h2>YurtHub 架构</h2></li></ol><p>在之前的文章中，我们详细介绍了 <a href="https://mp.weixin.qq.com/s/gYxK3GLhDRNkHibYgTchOg" rel="nofollow">YurtHub 组件的能力</a>。其架构图如下：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039749592" alt="1.png" title="1.png" referrerpolicy="no-referrer"></span></p><p><a href="https://raw.githubusercontent.com/openyurtio/openyurt/master/docs/img/yurthub.png" rel="nofollow">图片链接</a></p><p>YurtHub 是一个带有数据缓存功能的“透明网关”，和云端网络断连状态下，如果节点或者组件重启，各个组件（kubelet/kube-proxy 等）将从 YurtHub 中获取到业务容器相关数据，有效解决边缘自治的问题。这也意味着我们需要实现一个轻量的带数据缓存能力的反向代理。</p><ol><li><h2>第一想法</h2></li></ol><p>实现一个缓存数据的反向代理，第一想法就是从 response.Body 中读取数据，然后分别返回给请求 client 和本地的 Cache 模块。伪代码如下：</p><pre><code>func HandleResponse(rw http.ResponseWriter, resp *http.Response) &#123;
        bodyBytes, _ := ioutil.ReadAll(resp.Body)
        go func() &#123;
                // cache response on local disk
                cacher.Write(bodyBytes)
        &#125;

        // client reads data from response
        rw.Write(bodyBytes)
&#125;</code></pre><p>当深入思考后，在 Kubernetes 系统中，上述实现会引发下面的问题：</p><ul><li>问题 1：流式数据需要如何处理(如: K8s 中的 watch 请求)，意味 ioutil.ReadAll() 一次调用无法返回所有数据。即如何可以返回流数据同时又缓存流数据。</li><li>问题 2：同时在本地缓存数据前，有可能需要对传入的 byte slice 数据先进行清洗处理。这意味着需要修改 byte slice，或者先备份 byte slice 再处理。这样会造成内存的大量消耗，同时针对流式数据，到底申请多大的 slice 也不好处理。</li></ul><ol><li><h2>优雅实现探讨</h2></li></ol><p>针对上面的问题，我们将问题逐个抽象，可以发现更优雅的实现方法。</p><ul><li><strong>问题 1：如何对流数据同时进行读写</strong></li></ul><p>针对流式数据的读写(一边返回一边缓存)，如下图所示，其实需要的不过是把 response.Body(io.Reader) 转换成一个 io.Reader 和一个 io.Writer。或者说是一个 io.Reader 和 io.Writer 合成一个 io.Reader。这很容易就联想到 Linux 里面的 Tee 命令。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039749594" alt="2.png" title="2.png" referrerpolicy="no-referrer"></span></p><p>而在 Golang 中 Tee 命令是实现就是io.TeeReader，那问题 1 的伪代码如下：</p><pre><code>func HandleResponse(rw http.ResponseWriter, resp *http.Response) &#123;
        // create TeeReader with response.Body and cacher
        newRespBody := io.TeeReader(resp.Body, cacher)

        // client reads data from response
        io.Copy(rw, newRespBody)
&#125;</code></pre><p>通过 TeeReader 的对 Response.Body 和 Cacher 的整合，当请求 client 端从 response.Body 中读取数据时，将同时向 Cache 中写入返回数据，优雅的解决了流式数据的处理。</p><ul><li><strong>问题 2：如何在缓存前先清洗流数据</strong></li></ul><p>如下图所示，缓存前先清洗流数据，请求端和过滤端需要同时读取 response.Body（2 次读取问题）。也就是需要将 response.Body(io.Reader) 转换成两个 io.Reader。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039749593" alt="3.png" title="3.png" referrerpolicy="no-referrer"></span></p><p>也意味着问题 2 转化成：问题 1 中缓存端的 io.Writer 转换成 Data Filter 的 io.Reader。其实在 Linux 命令中也能找到类似命令，就是管道。因此问题 2 的伪代码如下：</p><pre><code>func HandleResponse(rw http.ResponseWriter, resp *http.Response) &#123;
        pr, pw := io.Pipe()
        // create TeeReader with response.Body and Pipe writer
        newRespBody := io.TeeReader(resp.Body, pw)
        go func() &#123;
                // filter reads data from response 
                io.Copy(dataFilter, pr)
        &#125;

        // client reads data from response
        io.Copy(rw, newRespBody)
&#125;</code></pre><p>通过 io.TeeReader 和 io.PiPe，当请求 client 端从 response.Body 中读取数据时，Filter 将同时从 Response 读取到数据，优雅的解决了流式数据的 2 次读取问题。</p><h1>YurtHub 实现</h1><p>最后看一下 YurtHub 中相关实现，由于 Response.Body 为 io.ReadCloser，所以实现了 dualReadCloser。同时 YurtHub 可能也面临对 http.Request 的缓存，所以增加了 isRespBody 参数用于判定是否需要负责关闭 response.Body。</p><pre><code>// https://github.com/openyurtio/openyurt/blob/master/pkg/yurthub/util/util.go#L156
// NewDualReadCloser create an dualReadCloser object
func NewDualReadCloser(rc io.ReadCloser, isRespBody bool) (io.ReadCloser, io.ReadCloser) &#123;
    pr, pw := io.Pipe()
    dr := &dualReadCloser&#123;
        rc:         rc,
        pw:         pw,
        isRespBody: isRespBody,
    &#125;

    return dr, pr
&#125;

type dualReadCloser struct &#123;
    rc io.ReadCloser
    pw *io.PipeWriter
    // isRespBody shows rc(is.ReadCloser) is a response.Body
    // or not(maybe a request.Body). if it is true(it's a response.Body),
    // we should close the response body in Close func, else not,
    // it(request body) will be closed by http request caller
    isRespBody bool
&#125;

// Read read data into p and write into pipe
func (dr *dualReadCloser) Read(p []byte) (n int, err error) &#123;
    n, err = dr.rc.Read(p)
    if n > 0 &#123;
        if n, err := dr.pw.Write(p[:n]); err != nil &#123;
            klog.Errorf("dualReader: failed to write %v", err)
            return n, err
        &#125;
    &#125;

    return
&#125;

// Close close two readers
func (dr *dualReadCloser) Close() error &#123;
    errs := make([]error, 0)
    if dr.isRespBody &#123;
        if err := dr.rc.Close(); err != nil &#123;
            errs = append(errs, err)
        &#125;
    &#125;

    if err := dr.pw.Close(); err != nil &#123;
        errs = append(errs, err)
    &#125;

    if len(errs) != 0 &#123;
        return fmt.Errorf("failed to close dualReader, %v", errs)
    &#125;

    return nil
&#125;</code></pre><p>在使用 dualReadCloser 时，可以在httputil.NewSingleHostReverseProxy的modifyResponse()方法中看到。代码如下：</p><pre><code>// https://github.com/openyurtio/openyurt/blob/master/pkg/yurthub/proxy/remote/remote.go#L85
func (rp *RemoteProxy) modifyResponse(resp *http.Response) error &#123;rambohe-ch, 10 months ago: • hello openyurt
            // 省略部分前置检查 
            rc, prc := util.NewDualReadCloser(resp.Body, true)
            go func(ctx context.Context, prc io.ReadCloser, stopCh <-chan struct&#123;&#125;) &#123;
                err := rp.cacheMgr.CacheResponse(ctx, prc, stopCh)
                if err != nil && err != io.EOF && err != context.Canceled &#123;
                    klog.Errorf("%s response cache ended with error, %v", util.ReqString(req), err)
                &#125;
            &#125;(ctx, prc, rp.stopCh)

            resp.Body = rc
&#125;</code></pre><h1>总结</h1><p>OpenYurt 于 2020 年 9 月进入 CNCF 沙箱后，持续保持了快速发展和迭代，在社区同学一起努力下，目前已经开源的能力有：</p><ul><li>边缘自治</li><li>边缘单元化管理</li><li>云边协同运维</li><li>一键式无缝转换能力</li></ul><p>同时在和社区同学的充分讨论下，OpenYurt 社区也发布了2021 roadmap，欢迎有兴趣的同学来一起贡献。</p><p><a href="https://developer.aliyun.com/article/783234?utm_content=g_1000258279" rel="nofollow">原文链接</a><br>本文为阿里云原创内容，未经允许不得转载。</p>  
</div>
            