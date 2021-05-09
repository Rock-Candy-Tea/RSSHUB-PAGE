
---
title: '日志多租户架构下的Loki方案'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210507/43bd205475e8aba73061ff0c3298c315.png'
author: Dockone
comments: false
date: 2021-05-09 08:02:15
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210507/43bd205475e8aba73061ff0c3298c315.png'
---

<div>   
<br>当我们在看Loki的架构文档时，社区都会宣称Loki是一个可以支持多租户模式下运行的日志系统，但我们再想进一步了解时，它却含蓄的表示Loki开启多租户只需要满足两个条件：<br>
<ul><li><br>配置文件中添加<code class="prettyprint">auth_enabled: true</code></li><li><br>请求头内带上租户信息<code class="prettyprint">X-Scope-OrgID</code></li></ul><br>
<br>这一切似乎都在告诉你，“快来用我吧，这很简单”，事实上当我们真的要在Kubernetes中构建一个多租户的日志系统时，我们需要考虑的远不止于此。<br>
<br>通常当我们在面对一个多租户的日志系统架构时，出于对日志存储的考虑，我们一般会有两种模式来影响系统的架构。<br>
<h4>日志集中存储（后文以方案A代称）</h4>和Loki原生一样，在日志进入到集群内，经过一系列校验和索引后集中的将日志统一写入后端存储上。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210507/43bd205475e8aba73061ff0c3298c315.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210507/43bd205475e8aba73061ff0c3298c315.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>日志分区存储（后文以方案B代称）</h4>反中心存储架构，每个租户或项目都可以拥有独立的日志服务和存储区块来保存日志。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210507/4f4d363c28b80c01ea28fa254f39d5a5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210507/4f4d363c28b80c01ea28fa254f39d5a5.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
从直觉上来看，日志分区带来的整体结构会更为复杂，除了需要自己开发控制器来管理Loki服务的生命周期外，它还需要为网关提供正确的路由策略。不过，不管多租户的系统选择何种方案，在本文我们也需从日志的整个流程来阐述不同方案的实现。<br>
<h3>第一关：Loki划分</h3>Loki是最终承载日志存储和查询的服务，在多租户的模式下，不管是<code class="prettyprint">大集群</code>还是<code class="prettyprint">小服务</code>，Loki本身也存在一些配置空间需要架构者去适配。其中特别是在面对大集群场景下，保证每个租户的日志写入和查询所占资源的合理分配调度就显得尤为重要。<br>
<br>在原生配置中，大部分关于租户的调整可以在下面两个配置区块中完成：<br>
<ul><li>query_frontend_config</li><li>limits_config</li></ul><br>
<br><h4>query_frontend_config</h4>query_frontend是Loki分布式集群模式下的日志查询最前端，它承担着用户日志查询请求的分解和聚合工作。那么显然，query_frontend对于请求的处理资源应避免被单个用户过分抢占。<br>
<br>每个frontend处理的租户<br>
<pre class="prettyprint">[max_outstanding_per_tenant: <int> | default = 100]<br>
</pre><br>
<h4>limits_config</h4>limits_config基本控制了Loki全局的一些流控参数和局部的租户资源分配，这里面可以通过Loki的<code class="prettyprint">-runtime-config</code>启动参数来让服务动态定期的加载租户限制。这部分可以通过<code class="prettyprint">runtime_config.go</code>中的<code class="prettyprint">runtimeConfigValues</code>结构体内看到：<br>
<pre class="prettyprint">type runtimeConfigValues struct &#123;  <br>
TenantLimits map[string]*validation.Limits `yaml:"overrides"`  <br>
<br>
Multi kv.MultiRuntimeConfig `yaml:"multi_kv_config"`  <br>
&#125; <br>
</pre><br>
可以看到对于TenantLimits内的限制配置是直接继承limits_config的，那么这部分的结构应该就是下面这样：<br>
<pre class="prettyprint">overrides:  <br>
tenantA:  <br>
ingestion_rate_mb: 10  <br>
max_streams_per_user: 100000  <br>
max_chunks_per_query: 100000  <br>
tenantB:  <br>
max_streams_per_user: 1000000  <br>
max_chunks_per_query: 1000000<br>
</pre><br>
当我们在选择采用方案A的日志架构时，关于租户部分的限制逻辑就应该要<code class="prettyprint">根据租户内的日志规模灵活的配置</code>。如果选择方案B，由于每个租户占有完整的Loki资源，所以这部分逻辑就直接由原生的limits_config控制。<br>
<h3>第二关：日志客户端</h3>在Kubernetes环境下，最重要是让日志客户端知道被采集的容器所属的租户信息。这部分实现可以是通过日志Operator或者是解析Kubernetes元数据来实现。虽然这两个实现方式不同，不过最终目的都是让客户端在采集日之后，在日志流的请求上添加租户信息头。下面我分别以logging-operator和FluentBit/FluentD这两种实现方式来描述他们的实现逻辑<br>
<h4>Logging Operator</h4>Logging Operator是BanzaiCloud下开源的一个云原生场景下的日志采集方案。它可以通过创建NameSpace级别的CRD资源flow和output来控制日志的解析和输出。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210507/2695bb75e13be6e9613b7057afccc57f.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210507/2695bb75e13be6e9613b7057afccc57f.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
通过Operator的方式可以精细的控制租户内的日志需要被采集的容器，以及控制它们的流向。以输出到loki举例，通常在只需在租户的命名空间内创建如下资源就能满足需求。<br>
<br>output.yaml，在创建资源时带入租户相关的信息<br>
<pre class="prettyprint">apiVersion: logging.banzaicloud.io/v1beta1  <br>
kind: Output  <br>
metadata:  <br>
name: loki-output  <br>
namespace: <tenantA-namespace>  <br>
spec:  <br>
loki:  <br>
url: http://loki:3100  <br>
username: <tenantA>  <br>
password: <tenantA>  <br>
tenant: <tenantA>  <br>
...<br>
</pre><br>
flow.yaml，在创建资源时关联租户需要被采集日志的容器，以及指定输出<br>
<pre class="prettyprint">apiVersion: logging.banzaicloud.io/v1beta1  <br>
kind: Flow  <br>
metadata:  <br>
name: flow  <br>
namespace:  <tenantA-namespace>  <br>
spec:  <br>
localOutputRefs:  <br>
- loki-output  <br>
match:  <br>
  - select:  <br>
      labels:  <br>
        app: nginx  <br>
filters:  <br>
  - parser:  <br>
      remove_key_name_field: true  <br>
      reserve_data: true  <br>
      key_name: "log"<br>
</pre><br>
可以看到通过operator来管理多租户的日志是一个非常简单且优雅的方式，同时通过CRD的方式创建资源对开发者集成到项目也十分友好。这也是我比较推荐的日志客户端方案。<br>
<h4>FluentBit/FluentD</h4>FluentBit和FluentD的Loki插件同样支持对多租户的配置。对于它们而言最重要的是让其感知到日志的租户信息。与Operator在CRD中直接声明租户信息不同，直接采用客户端方案就需要通过<code class="prettyprint">Kubernetes Metadata</code>的方式来主动抓取租户信息。对租户信息的定义，我们会声明在资源的label中。不过对于不同的客户端，label定义的路径还是比较有讲究的。它们总体处理流程如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210507/c1197945bb13cf12650420960caeb66f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210507/c1197945bb13cf12650420960caeb66f.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>FluentD</strong><br>
<br>FluentD的kubernetes-metadata-filter可以抓取到namespaces_label，所以我比较推荐将租户信息定义在命名空间内。<br>
<pre class="prettyprint">apiVersion: v1  <br>
kind: Namespace  <br>
metadata:  <br>
labels:  <br>
tenant: <tenantA>  <br>
name: <taenant-namespace><br>
</pre><br>
这样在就可以loki的插件中直接提取namespace中的租户标签内容，实现逻辑如下：<br>
<pre class="prettyprint"><match loki.**>  <br>
@type loki  <br>
@id loki.output  <br>
url "http://loki:3100"  <br>
# 直接提取命名空间内的租户信息  <br>
tenant $&#123;$.kubernetes.namespace_labels.tenant&#125;  <br>
username <username>  <br>
password <password>  <br>
<label>  <br>
tenant $&#123;$.kubernetes.namespace_labels.tenant&#125;  <br>
</label><br>
</pre><br>
<strong>FluentBit</strong><br>
FluentBit的metadata是从Pod中抓取，那么我们就需要将租户信息定义在workload的<code class="prettyprint">template.metadata.labels</code>当中，如下：<br>
<pre class="prettyprint">apiVersion: apps/v1  <br>
kind: Deployment  <br>
metadata:  <br>
labels:  <br>
app:  nginx  <br>
spec:  <br>
template:  <br>
metadata:  <br>
 labels:  <br>
   app: nginx  <br>
   tenant: <tanant-A><br>
</pre><br>
之后就需要利用rewrite_tag将容器的租户信息提取出来进行日志管道切分。并在output阶段针对不同日志管道进行输出。它的实现逻辑如下：<br>
<pre class="prettyprint">[FILTER]  <br>
Name           kubernetes  <br>
Match          kube.*  <br>
Kube_URL       https://kubernetes.default.svc:443  <br>
Merge_Log      On  <br>
[FILTER]  <br>
Name           rewrite_tag  <br>
Match          kube.*  <br>
#提取pod中的租户信息，并进行日志管道切分  <br>
Rule           $kubernetes['labels']['tenant'] ^(.*)$ tenant.$kubernetes['labels']['tenant'].$TAG false  <br>
Emitter_Name   re_emitted  <br>
[Output]  <br>
Name           grafana-loki  <br>
Match          tenant.tenantA.*  <br>
Url            http://loki:3100/api/prom/push  <br>
TenantID       "tenantA"  <br>
[Output]  <br>
Name           grafana-loki  <br>
Match          tenant.tenantB.*  <br>
Url            http://loki:3100/api/prom/push  <br>
TenantID       "tenantB"<br>
</pre><br>
可以看到不管是用FluentBit还是Fluentd的方式进行多租户的配置，它们不但对标签有一定的要求，对日志的输出路径配置也不是非常灵活。所以<code class="prettyprint">FluentD它比较做适合方案A的日志客户端，而FluentBit比较适合做方案B的日志客户端</code>。<br>
<h3>第三层：日志网关</h3>日志网关准确的说是Loki服务的网关，对于方案A来说，一个大Loki集群前面的网关，只需要简单满足能够横向扩展即可，租户的头信息直接传递给后方的Loki服务处理。这类方案相对简单，并无特别说明。只需注意针对查询接口的配置需调试优化，例如<code class="prettyprint">网关服务与upstream之间的连接超时时间</code>、<code class="prettyprint">网关服务response数据包大小</code>等。<br>
<br>本文想说明的日志网关是针对方案B场景下，解决针对不同租户的日志路由问题。从上文可以看到，在方案B中，我们引入了一个控制器来解决租户Loki实例的管理问题。但是这样就带来一个新的问题需要解决，那就是Loki的服务需要注册到网关，并实现路由规则的生成。这部分可以由集群的控制器CRD资源作为网关的upsteam源配置。控制器的逻辑如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210507/8827938e1be3a4bc351713c70e02cb5d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210507/8827938e1be3a4bc351713c70e02cb5d.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
网关服务在处理租户头信息时，路由部分的逻辑为判断Header中<code class="prettyprint">X-Scope-OrgID</code>带租户信息的日志请求，并将其转发到对应的Loki服务。我们以nginx作为网关举个例，它的核心逻辑如下：<br>
<pre class="prettyprint">#upstream内地址由sidecar从CRD中获取Loki实例后渲染生成  <br>
<br>
upstream tenantA &#123;  <br>
server x.x.x.x:3100;  <br>
&#125;  <br>
upstream tenantB &#123;  <br>
server y.y.y.y:3100;  <br>
&#125;  <br>
server &#123;  <br>
location / &#123;  <br>
    set tenant $http_x_scope_orgid;  <br>
    proxy_pass http://$tenant;  <br>
    include proxy_params;<br>
</pre><br>
<h3>总结</h3>本文介绍了基于Loki在多租户模式下的两种日志架构，分别为<code class="prettyprint">日志集中存储</code>和<code class="prettyprint">日志分区存储</code>。他们分别具备如下的特点：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210507/651fbc76cf92df00ccc89c8fcd77cea4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210507/651fbc76cf92df00ccc89c8fcd77cea4.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
对于团队内具备Kubernetes Operator相关开发经验的同学可以采用<code class="prettyprint">日志分区存储</code>方案，如果团队内偏向运维方向，可以选择<code class="prettyprint">日志集中存储</code>方案。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/QNl1q-v5SKov84MX7Pq_vQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/QNl1q-v5SKov84MX7Pq_vQ</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            