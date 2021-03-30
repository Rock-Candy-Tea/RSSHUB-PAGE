
---
title: '【OpenYurt 深度解析】边缘网关缓存能力的优雅实现'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://ucc.alicdn.com/pic/developer-ecology/422ed00f77434888881b5a2cd8ddd199.png'
author: Dockone
comments: false
date: 2021-03-30 08:09:44
thumbnail: 'https://ucc.alicdn.com/pic/developer-ecology/422ed00f77434888881b5a2cd8ddd199.png'
---

<div>   
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/422ed00f77434888881b5a2cd8ddd199.png" alt="头图.png" referrerpolicy="no-referrer"><br>
<br>作者 | 何淋波（新胜）<br>
来源 | <a href="https://mp.weixin.qq.com/s/vdFrCDiIhPLVbOnf6vRxEw">阿里巴巴云原生公众号</a><br>
<br><h1>OpenYurt：延伸原生 K8s 的能力到边缘</h1>阿里云边缘容器服务上线 1 年后，正式开源了云原生边缘计算解决方案 OpenYurt，跟其他开源的容器化边缘计算方案不同的地方在于：OpenYurt 秉持 Extending your native Kubernetes to edge 的理念，对 Kubernetes 系统零修改，并提供一键式转换原生 Kubernetes 为 OpenYurt，让原生 K8s 集群具备边缘集群能力。<br>
<br>同时随着 OpenYurt 的持续演进，也一定会继续保持如下发展理念：<br>
<ul><li>非侵入式增强 K8s</li><li>保持和云原生社区主流技术同步演进</li></ul><br>
<br><h1>OpenYurt 如何解决边缘自治问题</h1>想要实现将 Kubernetes 系统延展到边缘计算场景，那么边缘节点将通过公网和云端连接，网络连接有很大不可控因素，可能带来边缘业务运行的不稳定因素，这是云原生和边缘计算融合的主要难点之一。<br>
<br>解决这个问题，需要使边缘侧具有自治能力，即当云边网络断开或者连接不稳定时，确保边缘业务可以持续运行。在 OpenYurt 中，该能力由 yurt-controller-manager 和 YurtHub 组件提供。<br>
<br><h2>1. YurtHub 架构</h2>在之前的文章中，我们详细介绍了 <a href="https://mp.weixin.qq.com/s/gYxK3GLhDRNkHibYgTchOg">YurtHub 组件的能力</a>。其架构图如下：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210330/3d31e1c0059855d87846016257b1623a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210330/3d31e1c0059855d87846016257b1623a.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><a href="https://raw.githubusercontent.com/openyurtio/openyurt/master/docs/img/yurthub.png">图片链接</a><br>
<br>YurtHub 是一个带有数据缓存功能的“透明网关”，和云端网络断连状态下，如果节点或者组件重启，各个组件（kubelet/kube-proxy 等）将从 YurtHub 中获取到业务容器相关数据，有效解决边缘自治的问题。这也意味着我们需要实现一个轻量的带数据缓存能力的反向代理。<br>
<br><h2>2. 第一想法</h2>实现一个缓存数据的反向代理，第一想法就是从 response.Body 中读取数据，然后分别返回给请求 client 和本地的 Cache 模块。伪代码如下：<br>
<br>```<br>
func HandleResponse(rw http.ResponseWriter, resp *http.Response) &#123;<br>
        bodyBytes, _ := ioutil.ReadAll(resp.Body)<br>
        go func() &#123;<br>
                // cache response on local disk<br>
                cacher.Write(bodyBytes)<br>
        &#125;<br>
<br>        // client reads data from response<br>
        rw.Write(bodyBytes)<br>
&#125;<br>
```<br>
<br>当深入思考后，在 Kubernetes 系统中，上述实现会引发下面的问题：<br>
<ul><li><br>问题 1：流式数据需要如何处理(如: K8s 中的 watch 请求)，意味 ioutil.ReadAll() 一次调用无法返回所有数据。即如何可以返回流数据同时又缓存流数据。</li><li><br>问题 2：同时在本地缓存数据前，有可能需要对传入的 byte slice 数据先进行清洗处理。这意味着需要修改 byte slice，或者先备份 byte slice 再处理。这样会造成内存的大量消耗，同时针对流式数据，到底申请多大的 slice 也不好处理。</li></ul><br>
<br><h2>3. 优雅实现探讨</h2>针对上面的问题，我们将问题逐个抽象，可以发现更优雅的实现方法。<br>
<ul><li><strong>问题 1：如何对流数据同时进行读写</strong></li></ul><br>
<br>针对流式数据的读写(一边返回一边缓存)，如下图所示，其实需要的不过是把 response.Body(io.Reader) 转换成一个 io.Reader 和一个 io.Writer。或者说是一个 io.Reader 和 io.Writer 合成一个 io.Reader。这很容易就联想到 Linux 里面的 Tee 命令。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210330/f01d03e26b35a28c5b3c81d8898d1a79.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210330/f01d03e26b35a28c5b3c81d8898d1a79.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>而在 Golang 中 Tee 命令是实现就是io.TeeReader，那问题 1 的伪代码如下：<br>
<br>```<br>
func HandleResponse(rw http.ResponseWriter, resp *http.Response) &#123;<br>
        // create TeeReader with response.Body and cacher<br>
        newRespBody := io.TeeReader(resp.Body, cacher)<br>
<br>        // client reads data from response<br>
        io.Copy(rw, newRespBody)<br>
&#125;<br>
```<br>
<br>通过 TeeReader 的对 Response.Body 和 Cacher 的整合，当请求 client 端从 response.Body 中读取数据时，将同时向 Cache 中写入返回数据，优雅的解决了流式数据的处理。<br>
<ul><li><strong>问题 2：如何在缓存前先清洗流数据</strong></li></ul><br>
<br>如下图所示，缓存前先清洗流数据，请求端和过滤端需要同时读取 response.Body（2 次读取问题）。也就是需要将 response.Body(io.Reader) 转换成两个 io.Reader。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210330/15eb1b8c6a21ddd91e47dfd7e3d2d0fd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210330/15eb1b8c6a21ddd91e47dfd7e3d2d0fd.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>也意味着问题 2 转化成：问题 1 中缓存端的 io.Writer 转换成 Data Filter 的 io.Reader。其实在 Linux 命令中也能找到类似命令，就是管道。因此问题 2 的伪代码如下：<br>
<br>```<br>
func HandleResponse(rw http.ResponseWriter, resp *http.Response) &#123;<br>
        pr, pw := io.Pipe()<br>
        // create TeeReader with response.Body and Pipe writer<br>
        newRespBody := io.TeeReader(resp.Body, pw)<br>
        go func() &#123;<br>
                // filter reads data from response <br>
                io.Copy(dataFilter, pr)<br>
        &#125;<br>
<br>        // client reads data from response<br>
        io.Copy(rw, newRespBody)<br>
&#125;<br>
```<br>
<br>通过 io.TeeReader 和 io.PiPe，当请求 client 端从 response.Body 中读取数据时，Filter 将同时从 Response 读取到数据，优雅的解决了流式数据的 2 次读取问题。<br>
<br><h1>YurtHub 实现</h1>最后看一下 YurtHub 中相关实现，由于 Response.Body 为 io.ReadCloser，所以实现了 dualReadCloser。同时 YurtHub 可能也面临对 http.Request 的缓存，所以增加了 isRespBody 参数用于判定是否需要负责关闭 response.Body。<br>
<br>```<br>
// <a href="https://github.com/openyurtio/openyurt/blob/master/pkg/yurthub/util/util.go#L156" rel="nofollow" target="_blank">https://github.com/openyurtio/ ... 3L156</a><br>
// NewDualReadCloser create an dualReadCloser object<br>
func NewDualReadCloser(rc io.ReadCloser, isRespBody bool) (io.ReadCloser, io.ReadCloser) &#123;<br>
    pr, pw := io.Pipe()<br>
    dr := &dualReadCloser&#123;<br>
        rc:         rc,<br>
        pw:         pw,<br>
        isRespBody: isRespBody,<br>
    &#125;<br>
<br>    return dr, pr<br>
&#125;<br>
<br>type dualReadCloser struct &#123;<br>
    rc io.ReadCloser<br>
    pw *io.PipeWriter<br>
    // isRespBody shows rc(is.ReadCloser) is a response.Body<br>
    // or not(maybe a request.Body). if it is true(it's a response.Body),<br>
    // we should close the response body in Close func, else not,<br>
    // it(request body) will be closed by http request caller<br>
    isRespBody bool<br>
&#125;<br>
<br>// Read read data into p and write into pipe<br>
func (dr *dualReadCloser) Read(p []byte) (n int, err error) &#123;<br>
    n, err = dr.rc.Read(p)<br>
    if n > 0 &#123;<br>
        if n, err := dr.pw.Write(p[:n]); err != nil &#123;<br>
            klog.Errorf("dualReader: failed to write %v", err)<br>
            return n, err<br>
        &#125;<br>
    &#125;<br>
<br>    return<br>
&#125;<br>
<br>// Close close two readers<br>
func (dr *dualReadCloser) Close() error &#123;<br>
    errs := make([]error, 0)<br>
    if dr.isRespBody &#123;<br>
        if err := dr.rc.Close(); err != nil &#123;<br>
            errs = append(errs, err)<br>
        &#125;<br>
    &#125;<br>
<br>    if err := dr.pw.Close(); err != nil &#123;<br>
        errs = append(errs, err)<br>
    &#125;<br>
<br>    if len(errs) != 0 &#123;<br>
        return fmt.Errorf("failed to close dualReader, %v", errs)<br>
    &#125;<br>
<br>    return nil<br>
&#125;<br>
```<br>
<br>在使用 dualReadCloser 时，可以在httputil.NewSingleHostReverseProxy的modifyResponse()方法中看到。代码如下：<br>
<br>```<br>
// <a href="https://github.com/openyurtio/openyurt/blob/master/pkg/yurthub/proxy/remote/remote.go#L85" rel="nofollow" target="_blank">https://github.com/openyurtio/ ... 23L85</a><br>
func (rp *RemoteProxy) modifyResponse(resp *http.Response) error &#123;rambohe-ch, 10 months ago: • hello openyurt<br>
            // 省略部分前置检查<br><br>
            rc, prc := util.NewDualReadCloser(resp.Body, true)<br>
            go func(ctx context.Context, prc io.ReadCloser, stopCh <-chan struct&#123;&#125;) &#123;<br>
                err := rp.cacheMgr.CacheResponse(ctx, prc, stopCh)<br>
                if err != nil && err != io.EOF && err != context.Canceled &#123;<br>
                    klog.Errorf("%s response cache ended with error, %v", util.ReqString(req), err)<br>
                &#125;<br>
            &#125;(ctx, prc, rp.stopCh)<br>
<br>            resp.Body = rc<br>
&#125;<br>
```<br>
<br><h1>总结</h1>OpenYurt 于 2020 年 9 月进入 CNCF 沙箱后，持续保持了快速发展和迭代，在社区同学一起努力下，目前已经开源的能力有：<br>
<ul><li>边缘自治</li><li>边缘单元化管理</li><li>云边协同运维</li><li>一键式无缝转换能力</li></ul><br>
<br>同时在和社区同学的充分讨论下，OpenYurt 社区也发布了2021 roadmap，欢迎有兴趣的同学来一起贡献。<br>
如果大家对 OpenYurt 感兴趣，欢迎扫码加入我们的社区交流群，以及访问 OpenYurt 官网和 GitHub 项目地址：<br>
<ul><li>OpenYurt 官网：<a href="https://openyurt.io/">_</a><a href="https://openyurt.io_/" rel="nofollow" target="_blank">https://openyurt.io_</a></li><li>GitHub 项目地址：<a href="https://github.com/openyurtio/openyurt">_</a><a href="https://github.com/openyurtio/openyurt_" rel="nofollow" target="_blank">https://github.com/openyurtio/openyurt_</a></li></ul>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            