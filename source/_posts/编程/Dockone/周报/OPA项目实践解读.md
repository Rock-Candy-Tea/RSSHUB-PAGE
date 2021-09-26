
---
title: 'OPA项目实践解读'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/e0ac6db8dce220c3e23a695756693a26.png'
author: Dockone
comments: false
date: 2021-09-26 06:09:32
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/e0ac6db8dce220c3e23a695756693a26.png'
---

<div>   
<br>【编者的话】目前国外越来越多的公司开始使用Policy As Code来替换现有的策略逻辑，但国内的相关研究还处于起步阶段。雅客云安全SimonSun对OPA做了深入研究，并总结出一些看法与大家分享，欢迎探讨。<br>
<br>现代云原生项目中通常涉及到大量的策略逻辑，比如流量的准入控制以及合规性检查等。 然而， 如果使用传统的硬代码去写上述逻辑会带来频繁的程序变更，代码也会越来越难以维护，更重要的是随着时间的推移系统的Bug数量会越来越多，由此给开发者带来开发负担。由CNCF托管的开源策略引擎OPA项目——就是以解决此问题为目的，应运而生的新一代策略引擎。<br>
<h3>OPA的优势</h3>OPA是由 Styra公司于2016年开发，在2019年4月2号OPA正式进入了CNCF，作为孵化级托管项目。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/e0ac6db8dce220c3e23a695756693a26.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/e0ac6db8dce220c3e23a695756693a26.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
上图是OPA官方提供的结构图，OPA使用Json作为数据存储，使用Rego作为 OPA 策略所用到的声明语言。OPA要实现的目标是 Policy As Code。OPA可以作为Golang Library 库引入，也可以以Restful Api，还可以是Sidecar、主机级守护进程同时也能编译为WASM（WebAssembly）。<br>
<br>OPA目前在云原生领域逐渐替代了传统的策略引擎（如RBAC），目前社区比较活跃，并且在微服务、Kubernetes、CI/CD 、API gateways 等各个领域都有实践。很多项目中逐步使用OPA替换原有的策略逻辑。<br>
<h3>OPA的性能</h3>OPA目前最新版本是0.32。如下图所示，OPA在0.4.9的版本解决了性能问题，我们可以看下图，OPA从O(n)的复杂度优化到了常量级别的复杂度。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/7ad54ec556a7deda946736b4557cd74d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/7ad54ec556a7deda946736b4557cd74d.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
OPA具体的优化方式是将Rego的策略列表转换成了一个树，从而可以在毫秒内响应请求。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/11f281435add143a8dba5e1a7c3ca12d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/11f281435add143a8dba5e1a7c3ca12d.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
总体来说OPA的性能表现良好，目前能够满足项目内的多种应用场景。<br>
<h3>Debug工具齐全</h3>OPA像Golang一样，提供了很多实用的工具、命令，使开发Rego更简单一些。不论提供的fmt命令还是eval命令都像Golang一样既简洁又实用。<br>
<pre class="prettyprint">$opa --help<br>
An open source project to policy-enable your service.<br>
<br>
Usage:<br>
opa [command]<br>
<br>
Available Commands:<br>
bench       Benchmark a Rego query<br>
build       Build an OPA bundle<br>
check       Check Rego source files<br>
completion  generate the autocompletion script for the specified shell<br>
deps        Analyze Rego query dependencies<br>
eval        Evaluate a Rego query<br>
fmt         Format Rego source files<br>
help        Help about any command<br>
parse       Parse Rego source file<br>
run         Start OPA in interactive or server mode<br>
sign        Generate an OPA bundle signature<br>
test        Execute Rego test cases<br>
version     Print the version of OPA<br>
<br>
Flags:<br>
-h, --help   help for opa<br>
<br>
Use "opa [command] --help" for more information about a command.<br>
</pre><br>
<h3>声明式指定策略</h3>与K8s的声明式API一样，Rego也是声明式的。如下是一个简单的Rego，其声明了一个HTTP鉴权的逻辑。<br>
<pre class="prettyprint">package acmecorp.api<br>
<br>
import data.acmecorp.roles<br>
<br>
default allow = false<br>
<br>
allow &#123;<br>
input.method = “GET”<br>
input.path = [“accounts”, user]<br>
input.user = user<br>
&#125;<br>
<br>
allow &#123;<br>
input.method = “GET”<br>
input.path = [“accounts”, “report”]<br>
roles[input.user][_] = “admin”<br>
&#125;<br>
<br>
allow &#123;<br>
input.method = “POST”<br>
input.path = [“accounts”]<br>
roles[input.user][_] = “admin”<br>
&#125; <br>
</pre><br>
<h3>包含单元测试、性能测试、覆盖率测试、Mock</h3>测试在如今的分布式、微服务系统架构下的重要性不言而喻，雅客云团队内部使用了自动化测试并且引入了混沌工程，OPA能够提多种类型的测试并且供Json格式的输出，可以很方便的接入自动化测试平台。<br>
<h4>单元测试示例</h4><pre class="prettyprint">$ opa test . -v<br>
data.authz.test_post_allowed: PASS (1.417µs)<br>
data.authz.test_get_anonymous_denied: PASS (426ns)<br>
data.authz.test_get_user_allowed: PASS (367ns)<br>
data.authz.test_get_another_user_denied: PASS (320ns)<br>
--------------------------------------------------------------------------------<br>
PASS: 4/4<br>
</pre><br>
<h4>性能测试示例</h4><pre class="prettyprint">opa test -v --bench example.rego example_test.rego<br>
<br>
data.authz.test_post_allowed           98425             11773 ns/op              9298 timer_rego_query_eval_ns/op            8437 B/op             160 allocs/op<br>
data.authz.test_get_anonymous_denied          131479              9106 ns/op              6841 timer_rego_query_eval_ns/op            6596 B/op             133 allocs/op<br>
data.authz.test_get_user_allowed           96920             12395 ns/op              9920 timer_rego_query_eval_ns/op            8966 B/op             166 allocs/op<br>
data.authz.test_get_another_user_denied          103340             11834 ns/op              9301 timer_rego_query_eval_ns/op            8341 B/op             157 allocs/op<br>
--------------------------------------------------------------------------------<br>
PASS: 4/4<br>
</pre><br>
<h4>覆盖率测试示例</h4><pre class="prettyprint">opa test --coverage --format=json example.rego example_test.rego<br>
<br>
&#123;<br>
"files": &#123;<br>
"example.rego": &#123;<br>
  "covered": [<br>
    &#123;<br>
      "start": &#123;<br>
        "row": 3<br>
      &#125;,<br>
      "end": &#123;<br>
        "row": 5<br>
      &#125;<br>
    &#125;,<br>
    ...<br>
  ],<br>
  "coverage": 100<br>
&#125;,<br>
"example_test.rego": &#123;<br>
  "covered": [<br>
    ....<br>
  ],<br>
  "coverage": 100<br>
&#125;<br>
&#125;,<br>
"coverage": 100<br>
&#125; <br>
</pre><br>
<h3>IDA插件支持</h3>OPA有IDA插件支持，可以更快速的开发、验证。目前在Vscode、Goland(Jetbrains全家桶)中都有OPA插件。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/1920802b35b247b5555f356d5a481a5f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/1920802b35b247b5555f356d5a481a5f.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/37a5fe2d09bcdbf8ea2cde8c0cae1bd7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/37a5fe2d09bcdbf8ea2cde8c0cae1bd7.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>其他</h3>我们发现当OPA遇到K8s的CRD之后可以给项目带来更多可扩展的可能性，客户可以通过创建K8s的CR来创建Rego从而能够达到多种策略组合、自定义策略等多种模式。<br>
<h3>OPA不足</h3>目前国内OPA使用的还不广泛，相关资料较少，缺少最佳实践，需要自己踩坑。然后Reog语言有上手门槛，需要学习才能够上手使用。<br>
<h3>总结</h3>策略抽离后带来的好处是充分解耦。在代码更容易维护、扩展的同时可以尽可能的减少由策略配置错误导致的Bug。以达到给客户提供更优质服务的目的。<br>
<br>使用OPA后我们可以对策略本身进行版本化、重复的测试、策略复用等。并且可以预见的是就像数据库、队列、CICD、编排等模块一样，策略从代码中抽离出来是未来的趋势。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/JSCtxGfFNBCt48JYpoiLdg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/JSCtxGfFNBCt48JYpoiLdg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            