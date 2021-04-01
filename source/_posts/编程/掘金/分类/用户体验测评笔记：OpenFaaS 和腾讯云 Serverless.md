
---
title: '用户体验测评笔记：OpenFaaS 和腾讯云 Serverless'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a64963319a6495ea58b048e2aaeb295~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 31 Mar 2021 22:41:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a64963319a6495ea58b048e2aaeb295~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近看到<a href="https://mp.weixin.qq.com/s/KdMRNiOhTy2aR_RN8b37cw" target="_blank" rel="nofollow noopener noreferrer">《用 Serverless 架构部署 TensorFlow 模型推理函数》</a>的活动，对 serverless 非常感兴趣，本着学习的心态初步探索两个 serverless 框架，一个是开源的 OpenFaaS，一个是腾讯云，通过实际使用和对比初步入门 Serverless。</p>
<h2 data-id="heading-0">OpenFaaS</h2>
<p>按文档说明在 Ubuntu 20.04 上部署这个框架。</p>
<p>然后创建 Python 函数：</p>
<pre><code class="copyable">def handle(req):
    print("Hello! You said: " + req)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改配置，这里需要写入 docker hub 的帐号。</p>
<pre><code class="copyable">version: 1.0
provider:
  name: openfaas
  gateway: http://127.0.0.1:8080
functions:
  pycon:
    lang: python3
    handler: ./pycon
    image: >>> dockerhub 用户名<<</pycon
<span class="copy-code-btn">复制代码</span></code></pre>
<p>OpenFaaS 提供一个叫 faas-cli 的部署工具，faas-cli 会先将镜像上传到相应的 docker hub 帐号名下，然后再下拉到 OpenFaaS 服务。</p>
<p>开始部署成功后在 Web 界面 127.0.0.1:8080/ui/ 看到刚才创建的函数。</p>
<p>测试：</p>
<pre><code class="copyable">╰─➤  curl localhost:8080/function/pycon -d "Hi"
Hello! You said: Hi
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的例子可以看出：</p>
<ol>
<li>开发者只需要写好事件处理的函数，修改配置文件，确认部署即可，而不需要了解服务器的基础架构，甚至也不需要了解代码实际部署在哪个 Web 框架。</li>
<li>FaaS 服务返回调用接口。</li>
</ol>
<h2 data-id="heading-1">将图像识别服务部署到腾讯云</h2>
<p>除了将 Serverless 业务构建在硬件和容器（比如，OpenFaaS 使用 docker）之外，还有一种新兴的方法: 使用特定于应用程序的虚拟机，比如 WebAssembly（Wasm）。</p>
<p>这个例子通过 Second State 的  Serverless Wasm 虚拟机 (SSVM), 把用 Rust 编写的图像识别业务代码最终编译成 .so 文件，通过 <a href="https://www.serverless.com/" target="_blank" rel="nofollow noopener noreferrer">serverless 工具</a> 上传到腾讯云的 FaaS 中。</p>
<p>根据 Second State 的 demo 部署之后，在项目根目录输入 <code>sls deploy</code>, 验证腾讯云帐号，100 秒左右就部署成功，查看腾讯云的控制台，可以看到刚才部署的功能。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a64963319a6495ea58b048e2aaeb295~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>测试：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53290169a21748e19673b919a028cc52~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">魔改</h2>
<p>通过魔改 Second State 的例子学习腾讯云 Serverless 的用法。</p>
<p>先了解 <a href="https://github.com/second-state/tencent-tensorflow-scf" target="_blank" rel="nofollow noopener noreferrer">tencent-tensorflow-scf</a> 的结构：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3734044bdc1244f9aaadcae3b86aacb0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>cos, layer, scf 三个目录都有 serveress.yml，执行 <code>sls deploy</code> 的时候，可以看到这三个目录的文件被打包上传。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e7276c4643248bf843dc2191b7adbd1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>执行 <code>ssvmup build --enable-ext --enable-aot</code> 生成 <code>pkg/scf.so</code>, 需要将它拷贝至 <code>scf/</code> 目录。</p>
<p><code>scf/bootstrap</code> 是一个脚本，运行后是一个服务进程。</p>
<p>核心命令如下，其中 "$_HANDLER" 是 scf.so</p>
<pre><code class="copyable">RESPONSE=$(LD_LIBRARY_PATH=/opt /opt/ssvm-tensorflow "$_HANDLER" <<< "$EVENT_DATA")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就说明，我们可以在本地运行 "$_HANDLER"。我们可以先在本地调试业务功能。</p>
<p>首先需要编译 <a href="https://github.com/second-state/ssvm-tensorflow" target="_blank" rel="nofollow noopener noreferrer">ssvm-tensorflow</a> , 也可以直接下载二进制运行。</p>
<p>编译完之后，将 <a href="https://github.com/second-state/wasm-learning/tree/master/faas/mobilenet" target="_blank" rel="nofollow noopener noreferrer">这个 demo</a> 的代码迁移到 tencent-tensorflow-scf/src/main.rs, 实现魔改：</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-keyword">use</span> std::io::&#123;<span class="hljs-keyword">self</span>, Read&#125;;
<span class="hljs-keyword">use</span> ssvm_tensorflow_interface;
<span class="hljs-keyword">use</span> serde::Deserialize;

<span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">search_vec</span></span>(vector: &<span class="hljs-built_in">Vec</span><<span class="hljs-built_in">f32</span>>, labels: &<span class="hljs-built_in">Vec</span><&<span class="hljs-built_in">str</span>>, value: &<span class="hljs-built_in">f32</span>) -> (<span class="hljs-built_in">i32</span>, <span class="hljs-built_in">String</span>) &#123;
    <span class="hljs-keyword">for</span> (i, f) <span class="hljs-keyword">in</span> vector.iter().enumerate() &#123;
        <span class="hljs-keyword">if</span> f == value &#123;
            <span class="hljs-keyword">return</span> (i <span class="hljs-keyword">as</span> <span class="hljs-built_in">i32</span>, labels[i].to_owned());
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> (-<span class="hljs-number">1</span>, <span class="hljs-string">"Unclassified"</span>.to_owned());
&#125;

<span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">main</span></span>() &#123;
    <span class="hljs-keyword">let</span> model_data: &[<span class="hljs-built_in">u8</span>] = include_bytes!(<span class="hljs-string">"mobilenet_v2_1.4_224_frozen.pb"</span>);
    <span class="hljs-keyword">let</span> labels = <span class="hljs-built_in">include_str!</span>(<span class="hljs-string">"imagenet_slim_labels.txt"</span>);
    <span class="hljs-keyword">let</span> label_lines : <span class="hljs-built_in">Vec</span><&<span class="hljs-built_in">str</span>> = labels.lines().collect();


    <span class="hljs-keyword">let</span> <span class="hljs-keyword">mut</span> buffer = <span class="hljs-built_in">String</span>::new();
    io::stdin().read_to_string(&<span class="hljs-keyword">mut</span> buffer).expect(<span class="hljs-string">"Error reading from STDIN"</span>);
    <span class="hljs-keyword">let</span> obj: FaasInput = serde_json::from_str(&buffer).unwrap();
    <span class="hljs-keyword">let</span> img_buf = base64::decode_config(&(obj.body), base64::STANDARD).unwrap();

    <span class="hljs-keyword">let</span> flat_img = ssvm_tensorflow_interface::load_jpg_image_to_rgb32f(&img_buf, <span class="hljs-number">224</span>, <span class="hljs-number">224</span>);

    <span class="hljs-keyword">let</span> <span class="hljs-keyword">mut</span> session = ssvm_tensorflow_interface::Session::new(model_data, ssvm_tensorflow_interface::ModelType::TensorFlow);
    session.add_input(<span class="hljs-string">"input"</span>, &flat_img, &[<span class="hljs-number">1</span>, <span class="hljs-number">224</span>, <span class="hljs-number">224</span>, <span class="hljs-number">3</span>])
           .add_output(<span class="hljs-string">"MobilenetV2/Predictions/Softmax"</span>)
           .run();
    <span class="hljs-keyword">let</span> res_vec: <span class="hljs-built_in">Vec</span><<span class="hljs-built_in">f32</span>> = session.get_output(<span class="hljs-string">"MobilenetV2/Predictions/Softmax"</span>);
    <span class="hljs-keyword">let</span> <span class="hljs-keyword">mut</span> sorted_vec = res_vec.clone(); 
    sorted_vec.sort_by(|a, b| b.partial_cmp(a).unwrap());

    <span class="hljs-keyword">let</span> top1 = sorted_vec[<span class="hljs-number">0</span>];
    <span class="hljs-keyword">let</span> top2 = sorted_vec[<span class="hljs-number">1</span>];
    <span class="hljs-keyword">let</span> top3 = sorted_vec[<span class="hljs-number">2</span>];

    <span class="hljs-keyword">let</span> r1 = search_vec(&res_vec, &label_lines, &top1);
    <span class="hljs-keyword">let</span> r2 = search_vec(&res_vec, &label_lines, &top2);
    <span class="hljs-keyword">let</span> r3 = search_vec(&res_vec, &label_lines, &top3);

    <span class="hljs-built_in">println!</span>(<span class="hljs-string">"&#123;&#125;: &#123;:.2&#125;%\n&#123;&#125;: &#123;:.2&#125;%\n&#123;&#125;: &#123;:.2&#125;%"</span>
        , r1.<span class="hljs-number">1</span>, top1 * <span class="hljs-number">100.0</span>
        , r2.<span class="hljs-number">1</span>, top2 * <span class="hljs-number">100.0</span>   
        , r3.<span class="hljs-number">1</span>, top3 * <span class="hljs-number">100.0</span>   
        );
&#125;

<span class="hljs-meta">#[derive(Deserialize, Debug)]</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">FaasInput</span></span> &#123;
    body: <span class="hljs-built_in">String</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1cb8a78549d4e7397d584e8d1a6b68f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>输出排名前三的可能结果。</p>
<p>tomato.json 用于模拟请求数据，将图片数据 base64 之后放在 "body" 后面。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48d46344ef2c4b0296b6933e3545c60d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>最后重新 <code>sls deploy</code> 部署上线：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78c3a55cd89d48c29c4b2812cc6abacf~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">总结</h2>
<p>本文通过 OpenFaaS 和腾讯云 Serverless 两种服务，初步了解了将业务部署到云平台的过程。通过 FaaS 服务商提供的工具，用户可以避免直接操作 docker, 或设置脚本运行环境变量等不重要的细节，从而将注意力集中在业务开发上。</p>
<h2 data-id="heading-4">One More Thing</h2>
<p>立即体验腾讯云 Serverless Demo，领取 Serverless 新用户礼包 👉 <a href="https://serverless.cloud.tencent.com/start?c=juejin" target="_blank" rel="nofollow noopener noreferrer">serverless/start</a></p>
<blockquote>
<p>欢迎访问：<a href="https://serverlesscloud.cn/" target="_blank" rel="nofollow noopener noreferrer">Serverless 中文网</a>！</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            