
---
title: 'Clusternet v0.5.0 重磅发布： 全面解决多集群应用分发的差异化配置难题'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1020/180252_t3nG_4252687.png'
author: 开源中国
comments: false
date: Wed, 20 Oct 2021 18:04:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1020/180252_t3nG_4252687.png'
---

<div>   
<div class="content">
                                                                    
                                                        <blockquote> 
 <p style="margin-left:0; margin-right:0">作者：</p> 
 <p style="margin-left:0; margin-right:0"><span>徐迪，腾讯云容器技术专家。</span></p> 
 <p style="margin-left:0; margin-right:0"><span>汝英哲，腾讯云高级产品经理。</span></p> 
</blockquote> 
<p><span>在做多集群应用分发的时候，经常会遇到以下的差异化问题，比如：</span></p> 
<ol style="margin-left:0; margin-right:0"> 
 <li> <p style="color:#010101; margin-left:0; margin-right:0"><strong><span>在分发的资源上全部打上统一的标签</span></strong><span>，比如<span> </span></span><code><span>apps.my.company/deployed-by: my-platform</span></code><span>；</span></p> </li> 
 <li> <p style="color:#010101; margin-left:0; margin-right:0"><strong><span>在分发到子集群的资源上标记集群的信息</span></strong><span>，比如<span> </span></span><code><span>apps.my.company/running-in: cluster-01</span></code><span>；</span></p> </li> 
 <li> <p style="color:#010101; margin-left:0; margin-right:0"><strong><span>调整应用在每个集群中的副本数目、镜像名称等等</span></strong><span>，比如有一个名为<span> </span></span><code><span>my-nginx</span></code><span><span> </span>（声明的副本数为 3）的<span> </span></span><code><span>Deployment</span></code><span><span> </span>应用要分发到集群 cluster-01，集群 cluster-02，集群 cluster-03 中，我希望在这三个集群的副本数目分别为 3，5，7；</span></p> </li> 
 <li> <p style="color:#010101; margin-left:0; margin-right:0"><span>在分发到集群 cluster-01 之前，调整应用在该集群中的一些配置，比如注入一个 Sidecar 容器等；</span></p> </li> 
 <li> <p style="color:#010101; margin-left:0; margin-right:0"><strong><span>遇到某些特殊场景时</span></strong><span>，例如大促，动态扩容，应用灰度升级时，希望可以针对某个集群进行操作，变更范围小，不影响到其他集群，同时出现问题的时候，可以及时回滚，恢复到变更前的状态；</span></p> </li> 
 <li> <p style="color:#010101; margin-left:0; margin-right:0"><span>如果定义了多个差异化配置，相互之间出现冲突时，该如何解决；</span></p> </li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:center"><span style="color:#0046ff">开源 Clusternet 项目简介</span></h2> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0"><span>Clusternet ( <strong>Cluster</strong> Inter<strong>net</strong> ) 是腾讯云开源的兼具多集群管理和跨集群应用编排的云原生管控项目，<strong>让使用多集群就像上网一样简单</strong>。无论你的 Kubernetes 集群是运行在公有云、私有云、混合云还是边缘云上，都<strong>拥有一致的管理/访问体验，利用 K8s API 集中部署和协调多集群的应用程序和服务</strong>。</span></p> 
</blockquote> 
<p><span><span>Clusternet 采用<span> </span></span><strong style="color:black">Addon</strong><span><span> </span>插件的方式，<strong>方便用户一键安装、运维及集成，轻松地管理数以百万计的 Kubernetes 集群</strong>，<strong>让云计算像 Internet 一样无所不在，自由便捷。</strong></span></span></p> 
<p><span><span>Clusternet 支持向不同集群分发和管理各种应用资源，包括原生 Kubernetes 各类资源（Deployment/StatefulSet/ConfigMap/Secret 等）、各类 CRD 资源，以及 HelmChart 应用等等。</span></span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:center"><span style="color:#0046ff">Clusternet 如何解决这些差异化配置难题</span></h2> 
<p><span>Clusternet 在设计应用分发模型的时候，就充分考虑到了上述的那些场景，不希望引入过多的复杂设计，<strong>尽量</strong><strong>减少用户的重复定义，做到精简化、方便配置、可扩展性强、便于变更回滚</strong>等等。</span></p> 
<p><span><span>如果我们将上述的差异化问题进行归纳，大致可以归纳为以下两类：</span></span></p> 
<ol style="margin-left:0; margin-right:0"> 
 <li><span><strong>通用化配置或者全局化配置</strong>，比如对于某些资源进行无差异化的打标签，预配置等等；</span></li> 
 <li><span><strong>专属于某个集群的配置</strong>，比如更改<span> </span></span><code><span>Deployment</span></code><span><span> </span>在某集群对应的副本数，升级镜像，增加 Sidecar 容器等等；</span></li> 
</ol> 
<p><span>下图是<strong><span> </span>Clusternet 的多集群应用分发模型</strong>，其中绿色的模块是需要用户去创建的，紫色的模块是 Clusternet 内部做流转的资源对象。Clusternet 提供了 kubectl 插件，可以通过 “kubectl clusternet apply” 命令来创建资源。欢迎阅读<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5NjA1MjkxNw%3D%3D%26mid%3D2247516091%26idx%3D1%26sn%3Da2725260a9d873fbf04d5146230b1563%26scene%3D21%23wechat_redirect" target="_blank"><span>Clusternet - 新一代开源多集群管理与应用治理项目</span></a><span>，了解图中的相关概念。</span></p> 
<p><img height="288" src="https://static.oschina.net/uploads/space/2021/1020/180252_t3nG_4252687.png" width="700" referrerpolicy="no-referrer"></p> 
<p><span>Clusternet 资源分发模型采用松耦合的设计，用户无须更改或重新编写已有的资源对象，仅需要额外定义分发策略 （</span><code><span>Subscription</span></code><span>）和差异化配置（</span><code><span>Localization</span></code><span>/</span><code><span>Globalization</span></code><span>）即可实现多集群的应用分发。</span></p> 
<h3 style="margin-left:0; margin-right:10px"><span style="color:#0046ff">Localization 与 Globalization</span></h3> 
<p><span>在 Clusternet 中，每个注册的集群，都会拥有一个专属的 namespace (命名空间)，因此</span><strong><span>我们分别定义了<span> </span></span><code><span>Localization</span></code><span><span> </span>和<span> </span></span><code><span>Globalization</span></code><span><span> </span>这两个 CRD 用于声明差异化配置</span></strong><span>。</span></p> 
<p><span>其中<span> </span></span><code><span>Localization</span></code><span><span> </span>描述 namespace-scoped （命名空间作用域）的差异化配置策略，可用于对单个集群进行配置，比如<span> </span></span><code><span>Deployment</span></code><span><span> </span>在这个集群中的副本数目等。而<span> </span></span><code><span>Globalization</span></code><span><span> </span>描述 cluster-scoped （集群作用域） 的差异化配置策略，比如修改某个<span> </span></span><code><span>HelmChart</span></code><span><span> </span>的通用配置等。</span></p> 
<h3 style="margin-left:0; margin-right:10px"><span style="color:#0046ff">Override 策略</span></h3> 
<p><strong><span>Clusternet 还提供了两种 Overide 策略：</span><code><span>ApplyLater</span></code><span>（默认的策略）和<span> </span></span><code><span>ApplyNow</span></code><span>。</span></strong></p> 
<p><code><span>ApplyLater</span></code><span><span> </span>意味着该<span> </span></span><code><span>Localization</span></code><span>/</span><code><span>Globalization</span></code><span><span> </span>的差异化配置不会立即应用到资源上，只会在随后新创建出来的<span> </span></span><code><span>Description</span></code><span><span> </span>对象或者<span> </span></span><code><span>HelmChart</span></code><span>/</span><code><span>Subscription</span></code><span>/</span><code><span>Description</span></code><span><span> </span>等各个资源对象更新的时候才生效。而<span> </span></span><code><span>ApplyNow</span></code><span><span> </span>意味着会创建后即时生效，Clusternet 会将定义的差异化配置应用到所有匹配的对象中，即时下发到对应的子集群中。</span></p> 
<h3 style="margin-left:0; margin-right:10px"><span style="color:#0046ff">Priority 优先级</span></h3> 
<p><span>此外，两者均<strong>支持按照<span> </span><strong style="color:black">Priority</strong>（优先级）进行管理和配置</strong>，优先级的高低通过 0-1000 的数值来定义，值越小，优先级越低，默认是500。在进行差异化渲染的时候，Clusternet 会按照<span> </span></span><code><span>Globalization</span></code><span><span> </span>(低优先级) -><span> </span></span><code><span>Globalization</span></code><span><span> </span>(高优先级) -><span> </span></span><code><span>Localization</span></code><span><span> </span>(低优先级) -><span> </span></span><code><span>Localization</span></code><span><span> </span>(高优先级) 的次序，依次将声明的 Override 进行 apply。</span></p> 
<p><span>正是借助于这种<em><strong style="color:black">两阶段基于优先级</strong></em>（<strong style="color:black">two-stage priority based</strong>）的差异化配置能力，Clusternet 可以很方便地支持面向多集群的蓝绿发布、金丝雀发布、版本升级等场景。在使用过程中， 你可以定义多个<span> </span></span><code><span>Globalization</span></code><span><span> </span>和<span> </span></span><code><span>Localization</span></code><span><span> </span>对象，并设置不同的优先级策略。</span></p> 
<h3 style="margin-left:0; margin-right:10px"><span style="color:#0046ff">支持 Patch 操作</span></h3> 
<p><span>Clusternet 支持两种格式的 Override，</span><code><span>JSON Patch</span></code><span><span> </span>(<strong style="color:#595959">RFC 6902</strong>[1]) 和<span> </span></span><code><span>JSON Merge Patch</span></code><span><span> </span>(<strong style="color:#595959">RFC 7396</strong>[2])。有关 JSON patch 和 JSON 合并 patch 的比较，大家可以查看<span> </span><strong style="color:#595959">JSON Patch 和 JSON Merge Patch</strong>[3]，也可以参照如下的典型示例。</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:center"><span style="color:#0046ff">典型示例</span></h2> 
<p><span>下面我们来看几个典型的<strong>差异化配置场景</strong>。在如下的例子中，我们通过<span> </span></span><code><span>Localization</span></code><span><span> </span>对象来统一展示。这里使用<span> </span></span><code><span>Globalization</span></code><span><span> </span>也是可以的，这两者的 Spec 定义都是一样的，唯一的区别这两者的作用域和优先级差别。大家在实际使用的时候，可以根据需要进行改写。</span></p> 
<h3 style="margin-left:0; margin-right:10px"><span style="color:#0046ff">增加/更新标签</span></h3> 
<p><span>如果我们想给某个对象增加或者更新标签，可以这么定义如下的<span> </span></span><code><span>Localization</span></code><span><span> </span>对象。在使用的时候，请将<span> </span></span><code><span>metadata.namespace</span></code><span><span> </span>的值替换为真实的注册集群的专属 namespace。</span></p> 
<pre style="margin-left:0; margin-right:0"><code>apiVersion: apps.clusternet.io/v1alpha1
kind: Localization
metadata:
  name: nginx-local-overrides-demo-label
  namespace: clusternet-5l82l <em># 请更新这个值为对应集群的 namespace</em>
spec:
  overridePolicy: ApplyLater
  <em># 优先级反映着该对象的重要性，数值范围从 0 到 1000，值越小表示优先级越低</em>
  <em># 默认的值为 500.</em>
  priority: 300
  feed: <em># 这里表示要 override 的对象</em>
    apiVersion: apps/v1
    kind: Deployment
    name: my-nginx
    namespace: foo
  overrides: <em># 这里可以定义着多个 override</em>
    - name: add-update-labels
      <span style="color:#e6c07b">type</span>: MergePatch <em># 这里需要指定 override 的类型</em>
      <em># value 可以是 yaml 格式，也可以是 json 格式。</em>
      <em># 如下是 json 格式的例子</em>
      value: <span style="color:#98c379">'&#123;"metadata":&#123;"labels":&#123;"deployed-in-cluster":"clusternet-5l82l"&#125;&#125;&#125;'</span>
</code></pre> 
<p><span>可以在一个<span> </span></span><code><span>Localization</span></code><span><span> </span>对象中定义多个 overrides，在上面的例子中，我们只定义了一个名为<span> </span></span><code><span>add-update-labels</span></code><span><span> </span>的 override，其值为 json 格式的字符串，目的是增加或者更新一个标签<span> </span></span><code><span>deployed-in-cluster: clusternet-5l82l</span></code><span><span> </span>到<span> </span></span><code><span>spec.feed</span></code><span><span> </span>所定义的对象中。</span></p> 
<p style="margin-left:0; margin-right:0"><strong>这里 override 的值也可以 yaml 格式</strong>，见如下的例子。</p> 
<pre style="margin-left:0; margin-right:0"><code>apiVersion: apps.clusternet.io/v1alpha1
kind: Localization
metadata:
  name: nginx-local-overrides-demo-label
  namespace: clusternet-5l82l <em># 请更新这个值为对应集群的 namespace</em>
spec:
  overridePolicy: ApplyLater
  <em># 优先级反映着该对象的重要性，数值范围从 0 到 1000，值越小表示优先级越低</em>
  <em># 默认的值为 500.</em>
  priority: 300
  feed: <em># 这里表示要 override 的对象</em>
    apiVersion: apps/v1
    kind: Deployment
    name: my-nginx
    namespace: foo
  overrides: <em># 这里定义着 override value</em>
    - name: add-update-labels
      <span style="color:#e6c07b">type</span>: MergePatch
      <em># value 可以是 yaml 格式，也可以是 json 格式。</em>
      <em># 如下是 yaml 格式的例子</em>
      value: |-
        metadata:
          labels:
            deployed-in-cluster: clusternet-5l82l
</code></pre> 
<h3 style="margin-left:0; margin-right:10px"><span style="color:#0046ff">替换镜像及副本数目</span></h3> 
<p><span>Override 的类型也可以指定为<span> </span></span><code><span>JSONPatch</span></code><span>。在实际使用的时候，可以根据需要选择一个合适的 override 类型即可。</span></p> 
<p><span>通过如下的例子，可以将 Deployment<span> </span></span><code><span>foo/my-nginx</span></code><span><span> </span>在<span> </span></span><code><span>clusternet-5l82l</span></code><span><span> </span>子集群中的副本数更改为<span> </span><strong style="color:black">3</strong>，替换容器的镜像为<span> </span></span><code><span>nginx:1.14.0-alpine</span></code><span>，并增加一个新的注释<span> </span></span><code><span>foo: bar</span></code><span>。</span></p> 
<pre style="margin-left:0; margin-right:0"><code>apiVersion: apps.clusternet.io/v1alpha1
kind: Localization
metadata:
  name: nginx-local-overrides-demo-image-replicas
  namespace: clusternet-5l82l <em># 请更新这个值为对应集群的 namespace</em>
spec:
  overridePolicy: ApplyLater
  <em># 优先级反映着该对象的重要性，数值范围从 0 到 1000，值越小表示优先级越低</em>
  <em># 默认的值为 500.</em>
  priority: 400
  feed: <em># 这里表示要 override 的对象</em>
    apiVersion: apps/v1
    kind: Deployment
    name: my-nginx
    namespace: foo
  overrides: <em># 这里定义着 override value</em>
    - name: scale-and-add-annotations
      <span style="color:#e6c07b">type</span>: JSONPatch
      <em># value 可以是 yaml 格式，也可以是 json 格式。</em>
      value: |-
        - path: /spec/replicas
          value: 3
          op: replace
        - path: <span style="color:#98c379">"/spec/template/spec/containers/0/image"</span>
          value: <span style="color:#98c379">"nginx:1.14.0-alpine"</span>
          op: replace
        - path: /metadata/annotations
          value:
            foo: bar
          op: add
</code></pre> 
<h3 style="margin-left:0; margin-right:10px"><span style="color:#0046ff">注入 Sidecar 容器</span></h3> 
<p><span>我们还可以通过<span> </span></span><code><span>Localization</span></code><span><span> </span>来为 Deployment<span> </span></span><code><span>foo/my-nginx</span></code><span><span> </span>在<span> </span></span><code><span>clusternet-5l82l</span></code><span><span> </span>子集群下的实例注入 Sidecar 容器，见如下的示例，</span></p> 
<pre style="margin-left:0; margin-right:0"><code>apiVersion: apps.clusternet.io/v1alpha1
kind: Localization
metadata:
  name: nginx-local-overrides-demo-sidecar
  namespace: clusternet-5l82l <em># 请更新这个值为对应集群的 namespace</em>
spec:
  overridePolicy: ApplyLater
  <em># 优先级反映着该对象的重要性，数值范围从 0 到 1000，值越小表示优先级越低</em>
  <em># 默认的值为 500.</em>
  priority: 600
  feed: <em># 这里表示要 override 的对象</em>
    apiVersion: apps/v1
    kind: Deployment
    name: my-nginx
    namespace: foo
  overrides: <em># 这里定义着 override value</em>
    - name: inject-new-container
      <span style="color:#e6c07b">type</span>: JSONPatch
      <em># value 可以是 yaml 格式，也可以是 json 格式。</em>
      value: |-
        - op: add
          path: <span style="color:#98c379">"/spec/template/spec/containers/1"</span>
          value:
            name: <span style="color:#98c379">"redis-container"</span>
            image: <span style="color:#98c379">"redis:6.2.5"</span>
</code></pre> 
<p><span>通过<span> </span></span><code><span>Localization</span></code><span><span> </span>和<span> </span></span><code><span>Globalization</span></code><span><span> </span>不仅仅可以做如上的差异化配置，还有更多的场景等待着大家去发掘。</span></p> 
<p><span>为了方便大家上手体验一番，Clusternet 提供了<strong style="color:#595959">例子</strong>[4]，大家可以参照<span> </span><strong style="color:#595959">README 中的步骤</strong>[5]来实践一下多集群的应用分发。</span></p> 
<h3 style="margin-left:0; margin-right:10px; text-align:left"><span>参考资料</span></h3> 
<p><span><span>[1]</span>RFC 6902: 【<em>https://tools.ietf.org/html/rfc6902<span style="color:#000000">】</span></em></span></p> 
<p><span><span>[2]</span>RFC 7396:<span> </span><span style="color:#000000">【</span><em>https://tools.ietf.org/html/rfc7386<span style="color:#000000">】</span></em></span></p> 
<p><span><span>[3]</span>JSON Patch 和 JSON Merge Patch:<span> </span><em><span style="color:#000000">【</span>https://erosb.github.io/post/json-patch-vs-merge-patch/<span style="color:#000000">】</span></em></span></p> 
<p><span><span>[4]</span>例子:<span> </span><span style="color:#000000">【</span><em>https://github.com/clusternet/clusternet/tree/main/examples/applications<span style="color:#000000">】</span></em></span></p> 
<p><span><span>[5]</span>README 中的步骤:<span> </span><span style="color:#000000">【</span><em>https://github.com/clusternet/clusternet#deploying-applications-to-multiple-clusters<span style="color:#000000">】</span></em></span></p>
                                        </div>
                                      
</div>
            