
---
title: 'Netlify 中的 Rust 与 WebAssembly Serverless 函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e34b8c907334290a2c34b1fb7bd927c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 00:57:04 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e34b8c907334290a2c34b1fb7bd927c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.netlify.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.netlify.com/" ref="nofollow noopener noreferrer">Netlify</a> 是一个开发和托管 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fjamstack.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://jamstack.org/" ref="nofollow noopener noreferrer">Jamstack</a> 应用的平台。实际上，Jamstack 是Netlify 的创始人 Mathias Biilmann 于 2015年造出来的一个词。 Netlify 也是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fjamstackconf.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://jamstackconf.com/" ref="nofollow noopener noreferrer">JamstackConf</a> 的主要组织者。</p>
<p>Jamstack 应用程序由一个静态 UI (HTML 和 JavaScript) 和一系列 serverless 函数组成。动态 UI 元素由 JavaScript 向 serverless 函数获取数据生成。Jamstack 的好处有很多，但这其中最重要的好处之一是性能绝佳。由于 UI 不再从中心服务器的 runtime 生成，因此服务器上的负载要少得多，我们可以通过边缘网络（例如 CDN）部署 UI。</p>
<p>但是边缘 CDN 只解决了分发静态 UI 文件的问题。后端 serverless 函数可能仍然很慢。事实上，流行的 Serverless 平台存在众所周知的性能问题，例如冷启动缓慢，尤其是对于交互式应用程序而言。在这方面， WebAssembly 大有可为。</p>
<p>使用由 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.secondstate.io%2Farticles%2Fwasmedge-joins-cncf%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.secondstate.io/articles/wasmedge-joins-cncf/" ref="nofollow noopener noreferrer">CNCF</a> 托管的云原生 WebAssembly runtime <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/WasmEdge/WasmEdge" ref="nofollow noopener noreferrer">WasmEdge</a> ，开发者可以编写部署在公共云或边缘计算节点上的高性能serverless 函数。本文中，我们将探索如何使用 Rust 编写的 WasmEdge 函数来支持 Netlify 应用程序后端。</p>
<h2 data-id="heading-0">为什么用 WebAssembly 实现 Netlify 函数</h2>
<p>Netlify 平台已经有一个非常易于使用的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.netlify.com%2Fproducts%2Ffunctions%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.netlify.com/products/functions/" ref="nofollow noopener noreferrer">用于部署函数的 serverless 框架。</a>正如上面讨论的，使用 WebAssembly 以及 WasmEdge 是为了<strong>进一步提高性能</strong>。用 C/C++、Rust 和 Swift 写的高性能函数可以轻松编译成 WebAssembly。这些 WebAssembly 函数比 serverless 函数中常用的 JavaScript 或 Python 快得多。</p>
<p>可是，如果原始性能是唯一的目标，为什么不直接将这些函数编译为机器本地可执行文件呢(本地客户端或者 NaCl)？这是因为 Netlify 已经在使用 Firecracker microVM 在 AWS Lambda 中安全地运行这些函数。</p>
<blockquote>
<p>我们对未来的愿景是在云原生基础架构中将 WebAssembly 作为轻量级的 runtime 与 Docker 、 microVM 并列运行。与类似 Docker 容器或 microVM 相比，WebAssembly 提供更高的性能并消耗更少的资源。但就目前而言，Netlify 仅支持在 microVM 中运行 WebAssembly。</p>
</blockquote>
<p>相比运行容器化 NaCl 程序，在 microVM 中运行 WebAssembly 函数有很多优势。</p>
<p>首先，WebAssembly 为独立的函数提供了细颗粒度的 <strong>runtime 隔离</strong>。一个微服务可以有多个函数，并支持在 microVM 中运行的服务。 WebAssembly 可以让微服务更安全、更稳定。</p>
<p>第二，WebAssembly 字节码是<strong>可移植的</strong>。开发者只需构建一次，无需担心未来底层 Netlify serverless runtime 的改变或更新。它还允许开发者在其它云环境中重复使用相同的 WebAssembly 函数。</p>
<p>第三， WebAssembly 应用<strong>很容易部署和管理</strong>。与 NaCl 动态库和可执行文件相比，它们具有更少的平台依赖性和复杂性。</p>
<p>最后， <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.secondstate.io%2Farticles%2Fwasi-tensorflow%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.secondstate.io/articles/wasi-tensorflow/" ref="nofollow noopener noreferrer">WasmEdge Tensorflow API</a> 提供了<strong>最符合 Rust 规范的、执行 Tensorflow 模型的方式</strong>。WasmEdge 安装了 Tensorflow 依赖库的正确组合，并为开发者提供了统一的 API。</p>
<p>概念和解释说了很多，趁热打铁，我们来看看示例应用吧！</p>
<h2 data-id="heading-1">准备工作</h2>
<p>由于我们的 demo WebAssembly 函数是用 Rust 编写的，因此您需要安装 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.rust-lang.org%2Ftools%2Finstall" target="_blank" rel="nofollow noopener noreferrer" title="https://www.rust-lang.org/tools/install" ref="nofollow noopener noreferrer">Rust 编译器</a>。确保按如下方式安装 <code>wasm32-wasi</code> 编译器目标，以生成 WebAssembly 字节码。</p>
<pre><code class="copyable">$ rustup target add wasm32-wasi
<span class="copy-code-btn">复制代码</span></code></pre>
<p>demo 应用前端是用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnextjs.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nextjs.org/" ref="nofollow noopener noreferrer">Next.js</a> 写的，并且部署在 Netlify 上。我们假设你已经有使用 Next.js 和 Netlify 的基本知识了。</p>
<h2 data-id="heading-2">示例 1: 图片处理</h2>
<p>我们的第一个 demo 应用程序是让用户上传图片，然后调用 serverless 函数将其变成<strong>黑白图片</strong>。 开始之前，你可以试用一下这个部署在 Netlify 上的  <a href="https://link.juejin.cn/?target=https%3A%2F%2F60fe22f9ff623f0007656040--reverent-hodgkin-dc1f51.netlify.app%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://60fe22f9ff623f0007656040--reverent-hodgkin-dc1f51.netlify.app/" ref="nofollow noopener noreferrer">demo</a>。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e34b8c907334290a2c34b1fb7bd927c~tplv-k3u1fbpfcp-watermark.image" alt="netlify-wasmedge-runtime.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先 fork <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fnetlify-wasm-runtime" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/second-state/netlify-wasm-runtime" ref="nofollow noopener noreferrer">demo 应用的 GitHub repo</a> 。 要将该应用部署到 Netlify，只需<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.netlify.com%2Fblog%2F2016%2F09%2F29%2Fa-step-by-step-guide-deploying-on-netlify%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.netlify.com/blog/2016/09/29/a-step-by-step-guide-deploying-on-netlify/" ref="nofollow noopener noreferrer">将你的 GitHub repo 添加到 Netlify</a> 上。</p>
<p>这个 repo 是 Netlify 平台的标准 Next.js 应用程序。后端 serverless 函数在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fnetlify-wasm-runtime%2Ftree%2Fmain%2Fapi%2Ffunctions%2Fimage-grayscale" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/second-state/netlify-wasm-runtime/tree/main/api/functions/image-grayscale" ref="nofollow noopener noreferrer"><code>api/functions/image_grayscale</code></a> 文件夹中。 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fnetlify-wasm-runtime%2Fblob%2Fmain%2Fapi%2Ffunctions%2Fimage-grayscale%2Fsrc%2Fmain.rs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/second-state/netlify-wasm-runtime/blob/main/api/functions/image-grayscale/src/main.rs" ref="nofollow noopener noreferrer"><code>src/main.rs</code></a> 文件包含 Rust 程序的源代码。 Rust 程序从 <code>STDIN</code> 读取图片数据，然后将黑白图片输出到 <code>STDOUT</code>。</p>
<pre><code class="copyable">use hex;
use std::io::&#123;self, Read&#125;;
use image::&#123;ImageOutputFormat, ImageFormat&#125;;

fn main() &#123;
  let mut buf = Vec::new();
  io::stdin().read_to_end(&mut buf).unwrap();

  let image_format_detected: ImageFormat = image::guess_format(&buf).unwrap();
  let img = image::load_from_memory(&buf).unwrap();
  let filtered = img.grayscale();
  let mut buf = vec![];
  match image_format_detected &#123;
    ImageFormat::Gif => &#123;
        filtered.write_to(&mut buf, ImageOutputFormat::Gif).unwrap();
    &#125;,
    _ => &#123;
        filtered.write_to(&mut buf, ImageOutputFormat::Png).unwrap();
    &#125;,
  &#125;;
  io::stdout().write_all(&buf).unwrap();
  io::stdout().flush().unwrap();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 Rust 的 <code>cargo</code> 工具将 Rust 程序构建为为 WebAssembly 字节码或者原生代码。</p>
<pre><code class="copyable">$ cd api/functions/image-grayscale/
$ cargo build --release --target wasm32-wasi 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将 build artifacts 复制到 <code>api</code> 文件夹。</p>
<pre><code class="copyable">$ cp target/wasm32-wasi/release/grayscale.wasm ../../
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>Netlify 函数在设置 serverless 函数时运行  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fnetlify-wasm-runtime%2Fblob%2Fmain%2Fapi%2Fpre.sh" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/second-state/netlify-wasm-runtime/blob/main/api/pre.sh" ref="nofollow noopener noreferrer"><code>api/pre.sh</code></a> 。 这时会安装 WasmEdge runtime，然后将 WebAssembly 字节码程序编译为一个本地的  <code>so</code> 库，从而更快地执行。</p>
</blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fnetlify-wasm-runtime%2Fblob%2Fmain%2Fapi%2Fhello.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/second-state/netlify-wasm-runtime/blob/main/api/hello.js" ref="nofollow noopener noreferrer"><code>api/hello.js</code></a> 文本加载 WasmEdge runtime，在 WasmEdge 中启动编译好的 WebAssembly 程序，并通过 STDIN 传递上传的图像数据。这里请注意， <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fnetlify-wasm-runtime%2Fblob%2Fmain%2Fapi%2Fhello.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/second-state/netlify-wasm-runtime/blob/main/api/hello.js" ref="nofollow noopener noreferrer"><code>api/hello.js</code></a> 会运行由 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fnetlify-wasm-runtime%2Fblob%2Fmain%2Fapi%2Fpre.sh" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/second-state/netlify-wasm-runtime/blob/main/api/pre.sh" ref="nofollow noopener noreferrer"><code>api/pre.sh</code></a> 生成的编译好的 <code>grayscale.so</code> 文件，从而得到更好的性能。</p>
<pre><code class="copyable">const fs = require('fs');
const &#123; spawn &#125; = require('child_process');
const path = require('path');

module.exports = (req, res) => &#123;
  const wasmedge = spawn(
      path.join(__dirname, 'wasmedge'), 
      [path.join(__dirname, 'grayscale.so')]);

  let d = [];
  wasmedge.stdout.on('data', (data) => &#123;
    d.push(data);
  &#125;);

  wasmedge.on('close', (code) => &#123;
    let buf = Buffer.concat(d);

    res.setHeader('Content-Type', req.headers['image-type']);
    res.send(buf);
  &#125;);

  wasmedge.stdin.write(req.body);
  wasmedge.stdin.end('');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就完成了。 接下来<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.netlify.com%2Fblog%2F2016%2F09%2F29%2Fa-step-by-step-guide-deploying-on-netlify%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.netlify.com/blog/2016/09/29/a-step-by-step-guide-deploying-on-netlify/" ref="nofollow noopener noreferrer">将 repo 部署到Netlify</a> ，就得到了一个 Jamstack 应用。该应用有着基于 Rust 和 WebAssembly 的高性能 serverless 后端。</p>
<h2 data-id="heading-3">示例 2: AI 推理</h2>
<p>第二个<a href="https://link.juejin.cn/?target=https%3A%2F%2F60ff7e2d10fe590008db70a9--reverent-hodgkin-dc1f51.netlify.app%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://60ff7e2d10fe590008db70a9--reverent-hodgkin-dc1f51.netlify.app/" ref="nofollow noopener noreferrer">demo应用</a>让用户上传图像，然后调用 serverless 函数来识别<strong>图片中的主要物体</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77745d20cc3c43b5bbf69507bf528406~tplv-k3u1fbpfcp-watermark.image" alt="netlify-wasmedge-runtime-tflite.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>它与上一个示例在同一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fnetlify-wasm-runtime%2Ftree%2Ftensorflow" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/second-state/netlify-wasm-runtime/tree/tensorflow" ref="nofollow noopener noreferrer">GitHub repo</a> ，但是在 <code>tensorflow</code> 分支。 用于图片识别的后端 serverless 函数在该分支的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fnetlify-wasm-runtime%2Ftree%2Ftensorflow%2Fapi%2Ffunctions%2Fimage-classification" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/second-state/netlify-wasm-runtime/tree/tensorflow/api/functions/image-classification" ref="nofollow noopener noreferrer"><code>api/functions/image-classification</code></a> 文件夹中。 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fnetlify-wasm-runtime%2Fblob%2Ftensorflow%2Fapi%2Ffunctions%2Fimage-classification%2Fsrc%2Fmain.rs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/second-state/netlify-wasm-runtime/blob/tensorflow/api/functions/image-classification/src/main.rs" ref="nofollow noopener noreferrer"><code>src/main.rs</code></a> 文件包含了 Rust 程序的源代码。 Rust 程序从 <code>STDIN</code> 读取图像数据，然后将文本输出输出到 <code>STDOUT</code>。 它用 WasmEdge Tensorflow API 来运行 AI 推理。</p>
<pre><code class="copyable">pub fn main() &#123;
    // Step 1: Load the TFLite model
    let model_data: &[u8] = include_bytes!("models/mobilenet_v1_1.0_224/mobilenet_v1_1.0_224_quant.tflite");
    let labels = include_str!("models/mobilenet_v1_1.0_224/labels_mobilenet_quant_v1_224.txt");

    // Step 2: Read image from STDIN
    let mut buf = Vec::new();
    io::stdin().read_to_end(&mut buf).unwrap();

    // Step 3: Resize the input image for the tensorflow model
    let flat_img = wasmedge_tensorflow_interface::load_jpg_image_to_rgb8(&buf, 224, 224);

    // Step 4: AI inference
    let mut session = wasmedge_tensorflow_interface::Session::new(&model_data, wasmedge_tensorflow_interface::ModelType::TensorFlowLite);
    session.add_input("input", &flat_img, &[1, 224, 224, 3])
           .run();
    let res_vec: Vec<u8> = session.get_output("MobilenetV1/Predictions/Reshape_1");

    // Step 5: Find the food label that responds to the highest probability in res_vec
    // ... ...
    let mut label_lines = labels.lines();
    for _i in 0..max_index &#123;
      label_lines.next();
    &#125;

    // Step 6: Generate the output text
    let class_name = label_lines.next().unwrap().to_string();
    if max_value > 50 &#123;
      println!("It &#123;&#125; a <a href='https://www.google.com/search?q=&#123;&#125;'>&#123;&#125;</a> in the picture", confidence.to_string(), class_name, class_name);
    &#125; else &#123;
      println!("It does not appears to be any food item in the picture.");
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <code>cargo</code> 工具将 Rust 程序构建为 WebAssembly 字节码或原生代码。</p>
<pre><code class="copyable">$ cd api/functions/image-classification/
$ cargo build --release --target wasm32-wasi
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将 build artifacts 复制到 <code>api</code> 文件夹中</p>
<pre><code class="copyable">$ cp target/wasm32-wasi/release/classify.wasm ../../
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样， <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fnetlify-wasm-runtime%2Fblob%2Ftensorflow%2Fapi%2Fpre.sh" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/second-state/netlify-wasm-runtime/blob/tensorflow/api/pre.sh" ref="nofollow noopener noreferrer"><code>api/pre.sh</code></a> 脚本在此应用程序中安装 WasmEdge runtime 及其 Tensorflow 依赖项。同时在部署时，它将 <code>classify.wasm</code> 字节码程序编译为 <code>classify.so</code> 本地共享库。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fnetlify-wasm-runtime%2Fblob%2Ftensorflow%2Fapi%2Fhello.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/second-state/netlify-wasm-runtime/blob/tensorflow/api/hello.js" ref="nofollow noopener noreferrer"><code>api/hello.js</code></a> 脚本加载 WasmEdge runtime，在 WasmEdge 中启动编译好的 WebAssembly 程序，并通过 <code>STDIN</code> 传递已上传的图像数据。 注意 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fnetlify-wasm-runtime%2Fblob%2Ftensorflow%2Fapi%2Fhello.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/second-state/netlify-wasm-runtime/blob/tensorflow/api/hello.js" ref="nofollow noopener noreferrer"><code>api/hello.js</code></a> 运行由 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fnetlify-wasm-runtime%2Fblob%2Ftensorflow%2Fapi%2Fpre.sh" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/second-state/netlify-wasm-runtime/blob/tensorflow/api/pre.sh" ref="nofollow noopener noreferrer"><code>api/pre.sh</code></a> 生成的编译好的 <code>classify.so</code> 文件，以达到更好的性能。</p>
<pre><code class="copyable">const fs = require('fs');
const &#123; spawn &#125; = require('child_process');
const path = require('path');

module.exports = (req, res) => &#123;
  const wasmedge = spawn(
    path.join(__dirname, 'wasmedge-tensorflow-lite'),
    [path.join(__dirname, 'classify.so')],
    &#123;env: &#123;'LD_LIBRARY_PATH': __dirname&#125;&#125;
  );

  let d = [];
  wasmedge.stdout.on('data', (data) => &#123;
    d.push(data);
  &#125;);

  wasmedge.on('close', (code) => &#123;
    res.setHeader('Content-Type', `text/plain`);
    res.send(d.join(''));
  &#125;);

  wasmedge.stdin.write(req.body);
  wasmedge.stdin.end('');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在可以将你<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.netlify.com%2Fblog%2F2016%2F09%2F29%2Fa-step-by-step-guide-deploying-on-netlify%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.netlify.com/blog/2016/09/29/a-step-by-step-guide-deploying-on-netlify/" ref="nofollow noopener noreferrer">fork 的 repo 部署到 Netlify 上</a>，并得到一个可以进行物体识别的 web 应用。</p>
<h2 data-id="heading-4">接下来呢？</h2>
<p>在 Netlify 目前的 serverless 容器中运行 WasmEdge 是目前将高性能函数添加到 Netlify 应用中的简单方式。未来更好的方法是将WasmEdge作为容器本身使用，这样就无须 Docker 与 Node.js，我们可以以更高的效率运行 serverless 函数。 WasmEdge 已经<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.secondstate.io%2Farticles%2Fmanage-webassembly-apps-in-wasmedge-using-docker-tools%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.secondstate.io/articles/manage-webassembly-apps-in-wasmedge-using-docker-tools/" ref="nofollow noopener noreferrer">与 Docker 工具兼容</a>。如果你有兴趣加入 WasmEdge 和 CNCF 进行这个激动人心的工作，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%23contact" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/WasmEdge/WasmEdge#contact" ref="nofollow noopener noreferrer">欢迎加入我们的 channel</a>！</p></div>  
</div>
            