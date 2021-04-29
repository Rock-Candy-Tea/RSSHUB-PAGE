
---
title: 'WebAssembly + Dapr = 下一代云原生运行时？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210429/a80d7372de637f995319eccfa55f9228.jpg'
author: Dockone
comments: false
date: 2021-04-29 12:04:57
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210429/a80d7372de637f995319eccfa55f9228.jpg'
---

<div>   
<br>作者 | 易立<br>
来源 | <a href="https://mp.weixin.qq.com/s/Cp5R-6tfG8Js3MpdTbcD1w">阿里巴巴云原生公众号</a><br>
<br>云计算已经成为了支撑数字经济发展的关键基础设施。云计算基础设施也在持续进化，从 IaaS，到容器即服务（CaaS），再到 Serverless 容器和函数 PaaS（fPaaS 或者 FaaS），新的计算形态相继出现。以容器和 Serverless 为代表的云原生技术正在重塑整个应用生命周期。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210429/a80d7372de637f995319eccfa55f9228.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210429/a80d7372de637f995319eccfa55f9228.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
在 Gartner 分析报告中，云计算基础设施的发展路径，也是云原生特质逐渐增强的过程。其具体表现在：<br>
<ul><li><strong>模块化越来越高</strong>- 更加细粒度的计算单元，如容器和 Serverless 函数，更加适于微服务架构的应用交付，可以更加充分利用云的能力，提升架构敏捷性。</li><li><strong>可编程性越来越高</strong>- 可以通过声明式 API 和策略进行实现自动化管理与运维，可以通过 Immutable Infrastructure （不可变基础设施）进一步提升分布式应用运维的确定性。</li><li><strong>弹性效率越来越高</strong>- VM 可以实现分钟级扩容；容器与 Serverless 容器可以实现秒级扩容；借助调度优化，函数可以做到毫秒级扩容。</li><li><strong>韧性越来越高</strong>- Kubernetes 提供了强大自动化编排能力，提升应用系统自愈性。而 Serverless 进一步将稳定性、可伸缩性和安全等系统级别复杂性下沉到基础设施，开发者只需关注自身业务应用逻辑，进一步释放了生产力，提升系统的可恢复能力。</li></ul><br>
<br>分布式云则是云计算发展的另外一个重要趋势，公有云的服务可以拓展到不同的物理位置，让计算进一步贴近客户。分布式云让客户享受云计算的便利的同时，也可以满足对计算实时性和安全合规的诉求。这也推动了企业应用架构的变化 - 应用要能够在不同的环境进行部署、迁移，以最优化的方式提供服务。<br>
<br>进一步随着移动互联网，AI 与 IoT 等新技术的涌现，无处不在的计算已经成为现实。与此同时，这也在催生算力的多样性，X86 架构一统天下的时代已经过去，ARM/RISC-V 等芯片新势力不但称雄移动通信和嵌入式设备领域，也在向边缘计算和数据中心市场发起进攻。开发者甚至需要让应用支持不同的 CPU 体系架构，比如我们可以将一个图像识别应用部署在边缘或者 IoT 等不同环境、不同体系架构的设备之上运行。<br>
<br>在分布式云、边缘计算、云端一体等新的云计算场景下，下一代云原生应用运行时将具备什么样的特点？<br>
<h3>下一代云原生应用运行时</h3><h4>无处不在的计算催生下一代可移植、高性能、轻量化的安全沙箱</h4>容器应用采用自包含的打包方式——容器镜像，它包含了应用代码和依赖的系统组件，可以实现应用与基础设施解耦，让应用可以在公共云、专有云等不同的运行环境以一致的方式进行部署、运维，简化了弹性和迁移。此外 Docker 镜像规范支持多架构（Multi-Arch）镜像，可以简化不同 CPU 体系架构（如 x86，ARM 等）的应用镜像的构建与分发。<br>
<br>函数应用只包含用于事件响应的代码包，这将应用交付格式从原生二进制文件提升到了高级语言层面。这也给应用的可移植性带来了更大的想象空间，理论上甚至可以屏蔽执行环境 CPU 体系架构的差异。比如对于不依赖本地代码的 Python/NodeJS 等脚本或者 Java 应用，无需修改就可以在 x86 或者 ARM 等不同 CPU 架构上运行。<br>
<br>然而理想很丰满，现实很骨感，可移植性和厂商锁定是函数 PaaS 发展的拦路虎。<br>
<ul><li>很多脚本代码依然需要通过调用原生代码来实现数据处理和调用中间件（如数据库驱动），但是编译原生代码需要构建环境与目标执行环境一致才能保障兼容性。比如 AWS Lambda / 阿里云函数计算都要求二进制原生代码依赖指定的内核和 libc 版本。因此，越来越多的函数 PaaS 服务支持容器镜像作为载体，来简化函数应用打包和依赖管理。</li><li>函数应用通常依赖后端服务（BaaS，Backend as a Service）实现数据访问与计算处理等能力，由于 BaaS 不存在任何标准，这样很难将在 AWS Lambda 上开发的函数应用移植到阿里云的函数计算服务。</li></ul><br>
<br>在 Serverless 计算中，现有的主流技术是利用沙箱容器技术，如 AWS Firecraker 或者阿里云沙箱容器，来实现强隔离的安全执行环境，但是也带来更大的资源消耗。虽然现在阿里云沙箱容器经过优化可以实现 300ms 的冷启动速度，接近 Docker 这样的 OS 容器启动速度，但是还无法满足函数 PaaS 毫秒级的启动要求，目前需要通过的调度策略，预留一定的 standby 实例才可以满足，但是这样也引入了更多的资源消耗。<br>
<br>WebAssembly（WASM）是一个新的 W3C 规范，是一个通用、开放、高效、安全的底层虚拟机抽象。它的设计初衷是为了解决JavaScript的性能问题，使得 Web 应用有接近本机原生应用的性能。可以将现有编程语言应用，如 C/C++，Rust 等，编译成为 WASM 的字节码，运行在浏览器中的一个沙箱环境中。<br>
<br>WASM 让应用开发技术与运行时环境解耦，极大促进了代码复用。Mozilla 更在 2019 年推出了 WebAssembly System Interface（WASI），它提供类似 POSIX 这样的标准 API 来标准化 WebAssembly 与系统资源的交互抽象，比如文件系统访问，内存管理等。WASI 的出现拓展了 WASM 的应用场景，可以让其作为一个虚拟机运行各种类型的服务端应用。WASM/WASI 为应用的可移植性带来全新的希望，为了进一步推动 WebAssembly 生态发展，Mozilla、Fastly、英特尔和红帽公司携手成立了字节码联盟（Bytecode Alliance），共同领导 WASI 标准、 WebAssembly 运行时、工具等工作。<br>
<br>WebAssembly 所具备的的安全、可移植、高效率，轻量化的特点，为应用沙箱的发展带来了全新的思路。WASM 可以轻松实现毫秒级冷启动时间和极低的资源消耗。同时 WASM 字节码比原生机器码有更高的安全级别。此外，WASI 实现了细粒度基于能力的安全模型，遵循最小权限原则。在执行过程中，WASI 应用只能访问由依赖注入指明的确切资源集，这种方式与传统粗粒度的操作系统级隔离相比，进一步收敛了安全攻击面。<br>
<br>正因如此，WASM/WASI 得到了 Serverless、IoT/边缘计算等社区的广泛关注。Fastly、Cloudflare 等厂商相继发布了基于 WebAssembly 技术实现了更加轻量化的 Serverless 服务。<br>
<br>然而 WebAssembly 在服务器端的应用之路依然布满荆棘。首先 WASI 的能力还在非常早期的状态，一些关键能力依然缺失，首当其冲的就是缺乏标准化的网络访问能力：<a href="https://github.com/WebAssembly/WASI/issues/315"></a><a href="https://github.com/WebAssembly/WASI/issues/315" rel="nofollow" target="_blank">https://github.com/WebAssembly/WASI/issues/315</a>。<br>
<br>目前 WASI 应用仅能做一些计算类任务，基本无法实现分布式应用，也无法调用多样性的后端服务和 Redis、MySQL、Kafka 等应用中间件。这大大限制了 WASI 的应用场景。<br>
<br>当理想撞上现实，头破血流还是绝处逢生？<br>
<h4>下一代可移植应用运行时加速编程界面上移，应用基础设施能力下沉</h4>Dapr 是微软开源的面向云原生应用的分布式应用运行时，目标使所有开发人员能够使用任何语言和任何框架轻松地构建弹性的、事件驱动的、可移植的微服务应用。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210429/30e61bee4633ecd21685604415b60bdd.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210429/30e61bee4633ecd21685604415b60bdd.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
Dapr 实现了一系列构建高性能、可伸缩、高可用的分布式应用的设计模式，比如提供了服务发现和服务调用能力，也实现了一个简单、一致的编程模型来支持事件驱动应用架构。<br>
<br>此外 Dapr 通过基础设施屏蔽了应用访问后端服务的技术细节，如资源绑定、安全管理，可观测性等等。这个对 Serverless 应用非常重要，一方面将开发和部署进行了解耦，让开发者和运维团队可以通过关注点分离简化系统复杂性；一方面，可以将短生命周期、无状态的 Serverless 应用逻辑，与数据库连接池管理这样的长期运行，有状态的中间件访问能力进行解耦，提升了 Serverless 应用的可伸缩性和运行效率。<br>
<br>“Any language, any framework, anywhere” 是 Dapr 的重要设计目标。Dapr 通过在应用和后端服务之间，通过 Sidecar 方式提供一个抽象层，并通过标准化的 HTTP/gRPC API 实现了应用的可移植性，和后端服务的可替换性。<br>
<h3>走向诗和远方</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210429/890788bf1ee3ec3df6b20da2a220e08a.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210429/890788bf1ee3ec3df6b20da2a220e08a.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
我们可以将 WebAssembly 和 Dapr 相结合，来实现可移植、强隔离、轻量化的微服务应用架构。Dapr sidecar 与 WASM 虚拟机部署在一起。WASI 应用通过 HTTP/gRPC 访问本地的 Dapr 服务端点，由 Dapr 代理连接各种后端服务或者实现服务间通信。<br>
<br>这样的架构设计让 WASI 应用的安全边界非常清晰，符合 WASI 安全模型，WASI 应用只能通过 Dapr sidecar 实现外部服务访问。同时在这个架构中，只有 WASM 虚拟机和 Dapr 作为可信的环境依赖以原生机器码运行。而应用是可移植的 WASM 字节码，大大提升了架构的可移植性和安全性。<br>
<br>来自微软 Deis Labs 的 Radu Matei，最近提供了一个实验性项目可以为 WASI 添加 HTTP 支持。详见：<a href="https://github.com/WebAssembly/WASI/issues/315"></a><a href="https://deislabs.io/posts/wasi-experimental-http/" rel="nofollow" target="_blank">https://deislabs.io/posts/wasi-experimental-http/</a>。<br>
<br>在此基础上，我们来构建一个最小原型，验证 WebAssembly 与 Dapr 相结合的技术可行性。<br>
<h4>Dapr 环境准备</h4>我们首先按照 <a href="https://docs.dapr.io/getting-started/"></a><a href="https://docs.dapr.io/getting-started/" rel="nofollow" target="_blank">https://docs.dapr.io/getting-started/</a> 的流程：<br>
<pre class="prettyprint">$ dapr init<br>
⌛  Making the jump to hyperspace...<br>
✅  Downloading binaries and setting up components...<br>
✅  Downloaded binaries and completed components set up.<br>
ℹ️  daprd binary has been installed to /Users/yili/.dapr/bin.<br>
ℹ️  dapr_placement container is running.<br>
ℹ️  dapr_redis container is running.<br>
ℹ️  dapr_zipkin container is running.<br>
ℹ️  Use `docker ps` to check running containers.<br>
✅  Success! Dapr is up and running. To get started, go here: https://aka.ms/dapr-getting-started<br>
<br>
<br>
$ dapr run --app-id myapp --dapr-http-port 3500<br>
WARNING: no application command found.<br>
ℹ️  Starting Dapr with id myapp. HTTP Port: 3500. gRPC Port: 63734<br>
ℹ️  Checking if Dapr sidecar is listening on HTTP port 3500<br>
...<br>
ℹ️  Checking if Dapr sidecar is listening on GRPC port 63734<br>
ℹ️  Dapr sidecar is up and running.<br>
✅  You're up and running! Dapr logs will appear here.<br>
</pre><br>
<h4>利用 Redis 作为 WASI 应用的状态存储</h4>我们下面利用 Dapr 的 Get Started 的例子，利用 Redis 作为 WASI 应用的状态存储。具体逻辑如下图。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210429/b1992a4e78c1f7514a117704bff52cbe.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210429/b1992a4e78c1f7514a117704bff52cbe.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>注：下面的应用需要 Rust 和 AssemblyScript 环境配置，请大家自行完成。<br>
<br>我们在 Radu 项目的基础上 fork 了一个版本，首先来下载代码，并进行构建。<br>
<pre class="prettyprint">$ git clone https://github.com/denverdino/wasi-experimental-http<br>
$ cd wasi-experimental-http<br>
$ cargo build<br>
...<br>
Finished dev [unoptimized + debuginfo] target(s) in 3m 02s<br>
</pre><br>
我们利用 AssemblyScript 来实现了这个测试应用，测试代码如下：<br>
<pre class="prettyprint">$ cat tests/dapr/index.ts<br>
// @ts-ignore<br>
import &#123; Console &#125; from "as-wasi";<br>
import &#123; DaprClient, StateItem &#125; from "./dapr";<br>
import &#123; JSON &#125; from "assemblyscript-json";<br>
<br>
<br>
Console.log("Testing Dapr API ....")<br>
<br>
let dapr = new DaprClient()<br>
dapr.saveState("statestore", "weapon", JSON.Value.String("Death Star"))<br>
<br>
let o = JSON.Value.Object()<br>
o.set("name", "Tatooine")<br>
o.set("test", 123)<br>
let item = new StateItem("planets", o)<br>
let items: StateItem[] = [item]<br>
dapr.saveBulkState("statestore", items)<br>
<br>
let testObj = dapr.getState("statestore", "planets")<br>
let testStr = dapr.getState("statestore", "weapon")<br>
<br>
if (testStr.toString() == "Death Star" && testObj.isObj && (<JSON.Integer>(<JSON.Obj>testObj).getInteger("test")).valueOf() == 123) &#123;<br>
Console.log("Test successfully!")<br>
&#125; else &#123;<br>
Console.log("Test failed!")<br>
&#125; <br>
</pre><br>
代码逻辑非常简单，就是创建一个 Dapr 客户端，然后通过 REST API，进行 Dapr 的状态管理。我们可以快速验证一下。<br>
<pre class="prettyprint">$  cargo run<br>
Finished dev [unoptimized + debuginfo] target(s) in 0.19s<br>
 Running `target/debug/wasi-experimental-http-wasmtime-sample`<br>
Testing Dapr API ....<br>
POST http://127.0.0.1:3500/v1.0/state/statestore with [&#123;"key":"weapon","value":"Death Star"&#125;]<br>
POST http://127.0.0.1:3500/v1.0/state/statestore with [&#123;"key":"planets","value":&#123;"name":"Tatooine","test":123&#125;&#125;]<br>
GET http://127.0.0.1:3500/v1.0/state/statestore/planets<br>
GET http://127.0.0.1:3500/v1.0/state/statestore/weapon<br>
Test successfully!<br>
module instantiation time: 333.16637ms<br>
</pre><br>
<h4>关键要点分析</h4>wasi-experimental-http 项目在 Wasmtime （来自 Bytecode Alliance 的一个 WASM 实现）虚拟机上实现了扩展，支持在 WASI 应用中，访问 HTTP 服务。它还提供了一个 AssemblyScript 的 HTTP Client 实现。<br>
<br>wasi-experimental-http 项目：<a href="https://github.com/deislabs/wasi-experimental-http/"></a><a href="https://github.com/deislabs/wasi-experimental-http/" rel="nofollow" target="_blank">https://github.com/deislabs/wa ... http/</a>。<br>
<br>在此之上，我们为 AssemblyScript 提供一个 Dapr 的封装，可以参见：<a href="https://github.com/denverdino/wasi-experimental-http/blob/main/tests/dapr/dapr.ts"></a><a href="https://github.com/denverdino/wasi-experimental-http/blob/main/tests/dapr/dapr.ts" rel="nofollow" target="_blank">https://github.com/denverdino/ ... pr.ts</a>。<br>
<pre class="prettyprint">// @ts-ignore<br>
import &#123; Console &#125; from "as-wasi";<br>
import &#123; Method, RequestBuilder, Response &#125; from "../../crates/as";<br>
<br>
import &#123; JSONEncoder, JSON &#125; from "assemblyscript-json";<br>
<br>
export class StateItem &#123;<br>
key: string<br>
value: JSON.Value<br>
etag: string | null<br>
metadata: Map<string, string> | null<br>
<br>
constructor(key: string, value: JSON.Value) &#123;<br>
this.key = key<br>
this.value = value<br>
this.etag = null<br>
this.metadata = null<br>
&#125;<br>
&#125;<br>
<br>
...<br>
<br>
export class DaprClient &#123;<br>
port: i32<br>
address: string<br>
<br>
constructor() &#123;<br>
this.address = "127.0.0.1"<br>
this.port = 3500<br>
&#125;<br>
<br>
stateURL(storeName: string): string &#123;<br>
return "http://" + this.address + ":" + this.port.toString() + "/v1.0/state/" + storeName<br>
&#125;<br>
<br>
saveState(storeName: string, key: string, value: JSON.Value): boolean &#123;<br>
let item = new StateItem(key, value)<br>
let items: StateItem[] = [item]<br>
return this.saveBulkState(storeName, items)<br>
&#125;<br>
<br>
saveBulkState(storeName: string, items: StateItem[]): boolean &#123;<br>
// Handle field<br>
let encoder = new JSONEncoder();<br>
<br>
// Construct necessary object<br>
encoder.pushArray(null);<br>
for (let i = 0, len = items.length; i < len; i++) &#123;<br>
  let item = items[i]<br>
  encoder.pushObject(null);<br>
  encoder.setString("key", item.key)<br>
  encodeValue(encoder, "value", item.value)<br>
  if (item.etag != null) &#123;<br>
    encoder.setString("etag", <string>item.etag)<br>
  &#125;<br>
  encoder.popObject()<br>
&#125;;<br>
encoder.popArray();<br>
// Or get serialized data as string<br>
let jsonString = encoder.toString();<br>
let url = this.stateURL(storeName);<br>
Console.log("POST " + url + " with " + jsonString);<br>
let res = new RequestBuilder(url)<br>
  .method(Method.POST)<br>
  .header("Content-Type", "application/json")<br>
  .body(String.UTF8.encode(jsonString))<br>
  .send();<br>
let ok = res.status.toString() == "200"<br>
res.close();<br>
return ok<br>
&#125;<br>
<br>
getState(storeName: string, key: string): JSON.Value &#123;<br>
let url = this.stateURL(storeName) + "/" + key;<br>
Console.log("GET " + url);<br>
let res = new RequestBuilder(url)<br>
  .method(Method.GET)<br>
  .send();<br>
let ok = res.status.toString() == "200"<br>
let result = <JSON.Value> new JSON.Null()<br>
if (ok) &#123;<br>
  let body = res.bodyReadAll();<br>
  result = <JSON.Value>JSON.parse(body)<br>
&#125;<br>
res.close();<br>
return result<br>
&#125;<br>
&#125;;<br>
</pre><br>
测试应用的 main 函数，会创建一个 Wasmtime 运行时环境，并为其添加为 HTTP 扩展，并加载执行测试应用的 WASM 字节码：<a href="https://github.com/denverdino/wasi-experimental-http/blob/main/src/main.rs"></a><a href="https://github.com/denverdino/wasi-experimental-http/blob/main/src/main.rs" rel="nofollow" target="_blank">https://github.com/denverdino/ ... in.rs</a>。<br>
<pre class="prettyprint">fn main() &#123;<br>
let allowed_domains = Some(vec![<br>
    "http://127.0.0.1:3500".to_string(),<br>
]);<br>
let module = "tests/dapr/build/optimized.wasm";<br>
create_instance(module.to_string(), allowed_domains.clone()).unwrap();<br>
&#125;<br>
<br>
/// Create a Wasmtime::Instance from a compiled module and<br>
/// link the WASI imports.<br>
fn create_instance(<br>
filename: String,<br>
allowed_domains: Option<Vec<String>>,<br>
) -> Result<Instance, Error> &#123;<br>
let start = Instant::now();<br>
let store = Store::default();<br>
let mut linker = Linker::new(&store);<br>
<br>
let ctx = WasiCtxBuilder::new()<br>
    .inherit_stdin()<br>
    .inherit_stdout()<br>
    .inherit_stderr()<br>
    .build()?;<br>
<br>
let wasi = Wasi::new(&store, ctx);<br>
wasi.add_to_linker(&mut linker)?;<br>
// Link `wasi_experimental_http`<br>
let http = HttpCtx::new(allowed_domains, None)?;<br>
http.add_to_linker(&mut linker)?;<br>
<br>
let module = wasmtime::Module::from_file(store.engine(), filename)?;<br>
<br>
let instance = linker.instantiate(&module)?;<br>
let duration = start.elapsed();<br>
println!("module instantiation time: &#123;:#?&#125;", duration);<br>
Ok(instance)<br>
&#125; <br>
</pre><br>
<h3>道阻且长，行则将至</h3>WASM/WASI 为轻量化、可移植、缺省安全的应用运行时提供了良好的基础，在区块链等领域 WebAssembly 已经得到了广泛的应用。然而，对于通用性的服务器端应用，WASM/WASI 的差距还非常明显。由于 berkeley socket 这样标准化的网络编程接口的缺失，只能通过扩展 WASM 虚拟机的方式来进行补齐。此外 WASM 的多线程能力还没有被标准化，目前的 HTTP 调用采用阻塞式同步调用，还无法实现高效和稳定的网络通信。<br>
<br>此外，另外 WASM/WASI 的一个短板就是开发效率和生态建设。目前而言，虽然众多的编程语言已经逐渐开始提供 WebAssembly 的支持，但是对于普通开发者而言，AssemblyScript 这样的脚本语言是更加合适的选择。AssemblyScript 复用了 TypeScript 的语法，与 Rust/C++ 相比，大大降低了学习曲线，也提供了非常好的 IDE 工具体验，如 VS Code 等。但是与 TypeScripty 通过翻译成为 JavaScript 执行不同，AssemblyScript 应用会被编译成 WASM 字节码执行。AssemblyScript 本质上是一个静态类型的编译型语言，本质上与 JS/TS 这样的动态类型的解释型语言非常不同。二者在语法上也有一些不同，比如目前 AssemblyScript 缺少对闭包（closure）和正则表达式（Regex）等常用功能支持，这让开发 WASM 应用还是有一定的技术门槛。<br>
<br>另外与 NPM 强大的生态相比，AssemblyScript 社区也很年轻。很多功能都需要从头构建，比如对 JSON 的序列化与反序列化，我们选择了 <a href="https://github.com/nearprotocol/assemblyscript-json" rel="nofollow" target="_blank">https://github.com/nearprotoco ... -json</a>，但是其易用性和性能与成熟的 JSON 类库还有一定差距。当然我们也看到 AssemblyScript 的快速成长，以及越来越多的开发者开始贡献 AssemblyScript 代码库，比如 regex 支持等等。<br>
<br>Dapr 的出现为 WASM/WASI 开发通用的分布式应用，尤其是为可移植的、Serverless 化的应用带来另外一缕曙光。然而 Dapr 也并非完美：API 标准化在提升对后端服务可移植性的同时也阻碍了对差异化能力的支持。Sidecar 架构在提升灵活性的同时增加了部署和管理复杂性。<br>
<br>作为一个理性乐观派，任何技术都有其青涩的时代，期待社区的共同努力让计算无处不在、创新触手可及的理想成为现实。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            