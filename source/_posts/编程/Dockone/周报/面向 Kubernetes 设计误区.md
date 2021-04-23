
---
title: '面向 Kubernetes 设计误区'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210421/331842f04fdd92907f442c1e15567483.png'
author: Dockone
comments: false
date: 2021-04-23 00:26:42
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210421/331842f04fdd92907f442c1e15567483.png'
---

<div>   
<br><h3>Kubernetes 设计模式</h3>Kubernetes 是一个具有普遍意义的容器编排工具，它提供了一套基于容器构建分布式系统的基础依赖，其意义等同于 Linux 在操作系统中的地位，可以认为是分布式的操作系统。<br>
<h4>自定义资源</h4>Kubernetes 提供了 Pod、Service、Volume 等一系列基础资源定义，为了更好提供扩展性，CRD 功能是在 1.7 版本被引入。<br>
<br>用户可以根据自己的需求添加自定义的 Kubernetes 对象资源（CRD）。值得注意的是，这里用户自己添加的 Kubernetes 对象资源都是 native 的都是一等公民，和 Kubernetes 中自带的、原生的那些 Pod、Deployment 是同样的对象资源。在 Kubernetes 的 API Server 看来，它们都是存在于 etcd 中的一等资源。同时，自定义资源和原生内置的资源一样，都可以用 kubectl 来去创建、查看，也享有 RBAC、安全功能。用户可以开发自定义控制器来感知或者操作自定义资源的变化。<br>
<h4>Operator</h4>在自定义资源基础上，如何实现自定义资源创建或更新时的逻辑行为，Kubernetes Operator 提供了相应的开发框架。Operator 通过扩展 Kubernetes 定义 Custom Controller，list/watch 对应的自定义资源，在对应资源发生变化时，触发自定义的逻辑。<br>
<br>Operator 开发者可以像使用原生 API 进行应用管理一样，通过声明式的方式定义一组业务应用的期望终态，并且根据业务应用的自身特点进行相应控制器逻辑编写，以此完成对应用运行时刻生命周期的管理并持续维护与期望终态的一致性。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210421/331842f04fdd92907f442c1e15567483.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210421/331842f04fdd92907f442c1e15567483.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>通俗的理解</h4>CRD 是 Kubernetes 标准化的资源扩展能力，以 Java 为例，int、long、Map、Object 是 Java 内置的类，用户可以自定义 Class 实现类的扩展，CRD 就是 Kubernetes 中的自定义类，CR 就是对应类的一个 instance。<br>
<br>Operator 模式 = 自定义类 + 观察者模式，Operator 模式让大家编写 Kubernetes 的扩展变得非常简单快捷，逐渐成为面向 Kubernetes 设计的标准。<br>
<br>Operator 提供了标准化的设计流程：<br>
<ol><li>使用 SDK 创建一个新的 Operator 项目；</li><li>通过添加自定义资源（CRD）定义新的资源 API；</li><li>指定使用 SDK API 来 watch 的资源；</li><li>自定义 Controller 实现 Kubernetes 协调（reconcile）逻辑；</li></ol><br>
<br><h3>有了锤子，看到的只有钉子</h3>我们团队（KubeOne 团队）一直在致力于解决复杂中间件应用如何部署到 Kubernetes，自然也是 Operator 模式的践行者。经历了近 2 年的开发，初步解决了中间件在各个环境 Kubernetes 的部署，当前中间也走了很多弯路，踩了很多坑。  <br>
<br>KubeOne 内核也经历 3 个大版本的迭代，前 2 次开发过程基本都是 follow Operator 标准开发流程进行开发设计。遵循一个标准的、典型的 Operator 的设计过程，看上去一切都是这么的完美，但是每次设计都非常痛苦，践行 Operator 模式之后，最值得反思和借鉴的就是”有了锤子，看到的只有钉子，简单总结一下就是 4 个一切：<br>
<ol><li>一切设计皆 YAML；</li><li>一切皆合一；</li><li>一切皆终态；</li><li>一切交互皆 cr。</li></ol><br>
<br><h3>误区1：一切设计皆 YAML</h3>Kubernetes 的 API 是 YAML 格式，Operator 设计流程也是让大家首先定义 CRD，所以团队开始设计时直接采用了 YAML 格式。<br><br>
<h4>案例</h4>根据标准化流程，团队面向 YAML 设计流程大体如下：<br>
<ul><li>先根据已知的数据初步整理一个大而全的 YAML，做一下初步的分类，例如应用大概包含基础信息，依赖服务，运维逻辑，监控采集等，每个分类做一个子部分。</li><li><br>开会讨论具体的内容是否能满足要求，结果每次开会都难以形成共识。<br>
<ul><li>因为总是有新的需求满足不了，在讨论A时，就有人提到 B、C、D，不断有新的需求；</li><li>每个部分的属性非常难统一，因为不同的实现属性差异较大；</li><li>理解不一致，相同名字但使用时每个人的理解也不同。</li></ul></li><li><br>由于工期很紧，只能临时妥协，做一个中间态，后面再进一步优化。</li><li>后续优化升级，相同的流程再来一遍，还是很难形成共识。</li></ul><br>
<br>这是第 2 个版本的设计：<br>
<pre class="prettyprint">apiVersion: apps.mwops.alibaba-inc.com/v1alpha1<br>
kind: AppDefinition<br>
metadata:<br>
labels:<br>
app: "A"<br>
name: A-1.0 //chart-name+chart-version<br>
namespace: kubeone<br>
spec:<br>
appName: A  //chart-name<br>
version: 1.0 //chart-version<br>
type: apps.mwops.alibaba-inc.com/v1alpha1.argo-helm<br>
workloadSettings:   //注 workloadSettings 标识type应该使用的属性<br>
- name: "deployToK8SName"<br>
  value: ""<br>
- name: "deployToNamespace"<br>
  value: $&#123;resources:namespace-resource.name&#125;<br>
parameterValues:   //注 parameterValues标识业务属性<br>
- name: "enableTenant"<br>
  value: "1"<br>
- name: "CPU"<br>
  value: "1"<br>
- name: "MEM"<br>
  value: "2Gi"<br>
- name: "jvm"<br>
  value: "flag;gc"<br>
- name: vip.fileserver-edas.ip<br>
  value: $&#123;resources:fileserver_edas.ip&#125;<br>
- name: DB_NAME<br>
  valueFromConfigMap:<br>
    name: $&#123;resources:rds-resource.cm-name&#125;<br>
    expr: $&#123;database&#125;<br>
- name: DB_PASSWORD<br>
  valueFromSecret:<br>
      name: $&#123;instancename&#125;-rds-secret<br>
      expr: $&#123;password&#125;<br>
- name: object-storage-endpoint<br>
  value: $&#123;resources:object-storage.endpoint&#125;<br>
- name: object-storage-username<br>
  valueFromSecret:<br>
      name: $&#123;resources:object-storage.secret-name&#125;<br>
      expr: $&#123;username&#125;<br>
- name: object-storage-password<br>
  valueFromSecret:<br>
      name: $&#123;resources:object-storage.secret-name&#125;<br>
      expr: $&#123;password&#125;<br>
- name: redis-endpoint<br>
  value: $&#123;resources:redis.endpoint&#125;<br>
- name: redis-password<br>
  value: $&#123;resources:redis.password&#125;<br>
resources:<br>
  - name: tolerations<br>
    type: apps.mwops.alibaba-inc.com/tolerations<br>
    parameterValues:<br>
       - name: key<br>
         value: "sigma.ali/is-ecs"<br>
       - name: key<br>
         value: "sigma.ali/resource-pool"<br>
  - name: namespace-resource<br>
    type: apps.mwops.alibaba-inc.com/v1alpha1.namespace<br>
    parameterValues:<br>
      - name: name<br>
        value: edas<br>
  - name: fileserver-edas<br>
    type: apps.mwops.alibaba-inc.com/v1alpha1.database.vip<br>
    parameterValues:<br>
      - name: port<br>
        value: 21,80,8080,5000<br>
      - name: src_port<br>
        value: 21,80,8080,5000<br>
      - name: type<br>
        value: ClusterIP<br>
      - name: check_type<br>
        value: ""<br>
      - name: uri<br>
        value: ""<br>
      - name: ip<br>
        value: ""<br>
  - name: test-db<br>
    type: apps.mwops.alibaba-inc.com/v1alpha1.database.mysqlha<br>
    parameterValues:<br>
      - name: name<br>
        value: test-db<br>
      - name: user<br>
        value: test-user<br>
      - name: password<br>
        value: test-passwd<br>
      - name: secret<br>
        value: test-db-mysqlha-secret<br>
  - name: service-slb<br>
    type: apps.mwops.alibaba-inc.com/v1alpha1.slb<br>
    mode: post-create<br>
    parameterValues:<br>
      - name: service<br>
        value: "serviceA"<br>
      - name: annotations<br>
        value: "app:a,version:1.0"<br>
      - name: external-ip<br>
        value: <br>
  - name: service-resource2<br>
    type: apps.mwops.alibaba-inc.com/v1alpha1.service<br>
    parameterValues: <br>
      - name: second-domain<br>
        value: edas.console<br>
      - name: ports<br>
        value: "80:80"<br>
      - name: selectors<br>
        value: "app:a,version:1.0"<br>
      - name: type<br>
        value: "loadbalance"<br>
  - name: service-dns<br>
    type: apps.mwops.alibaba-inc.com/v1alpha1.dns<br>
    parameterValues:<br>
      - name: domain<br>
        value: edas.server.$&#123;global:domain&#125;<br>
      - name: vip<br>
        value: $&#123;resources:service-resource2.EXTERNAL-IP&#125;<br>
  - name: dns-resource<br>
    type: apps.mwops.alibaba-inc.com/v1alpha1.dns<br>
    parameterValues:<br>
      - name: domain<br>
        value: edas.console.$&#123;global:domain&#125;<br>
      - name: vip<br>
        value: “127.0.0.1”<br>
  - name: cni-resource<br>
    type: apps.mwops.alibaba-inc.com/v1alpha1.cni<br>
    parameterValues:<br>
      - name: count<br>
        value: 4<br>
      - name: ip_list<br>
        value: <br>
  - name: object-storage<br>
    type: apps.mwops.alibaba-inc.com/v1alpha1.objectStorage.minio<br>
    parameterValues:<br>
      - name: namespace<br>
        value: test-ns<br>
      - name: username<br>
        value: test-user<br>
      - name: password<br>
        value: test-password<br>
      - name: storage-capacity<br>
        value: 20Gi<br>
      - name: secret-name<br>
        value: minio-my-store-access-keys<br>
      - name: endpoint<br>
        value: minio-instance-external-service<br>
  - name: redis<br>
    type: apps.mwops.alibaba-inc.com/v1alpha1.database.redis<br>
    parameterValues:<br>
      - name: cpu<br>
        value: 500m<br>
      - name: memory<br>
        value: 128Mi<br>
      - name: password<br>
        value: i_am_a_password<br>
      - name: storage-capacity<br>
        value: 20Gi<br>
      - name: endpoint<br>
        value: redis-redis-cluster <br>
  - name: accesskey<br>
    type: apps.mwops.alibaba-inc.com/v1alpha1.accesskey<br>
    parameterValues:<br>
      - name: name<br>
        value: default<br>
      - name: userName<br>
        value: ecs_test@aliyun.com<br>
exposes:<br>
- name: dns<br>
  value: $&#123;resources:dns-resource.domain&#125;<br>
- name: db-endpoint<br>
  valueFromConfigmap:<br>
    name: $&#123;resources:rds-resource.cm-name&#125;<br>
    expr: $&#123;endpoint&#125;:3306/$&#123;database&#125;<br>
- name: ip_list<br>
  value: $&#123;resources:cni-resource.ip_list&#125;<br>
- name: object-storage-endpoint<br>
  value: $&#123;resources:object-storage.endpoint&#125;.$&#123;resource:namespace-resource.name&#125;<br>
- name: object-storage-username<br>
  valueFromSecret:<br>
      name: $&#123;resources:object-storage.secret-name&#125;<br>
      expr: $&#123;username&#125;<br>
- name: object-storage-password<br>
  valueFromSecret:<br>
      name: $&#123;resources:object-storage.secret-name&#125;<br>
      expr: $&#123;password&#125;<br>
- name: redis-endpoint<br>
  value: $&#123;resources:redis.endpoint&#125;.$&#123;resource:namespace-resource.name&#125;<br>
- name: redis-password<br>
  value: $&#123;resources:redis.password&#125; <br>
</pre><br>
<h4>反思</h4>这样的痛苦难以用语言表达，感觉一切都脱离了掌控，没有统一的判断标准，设计标准，公说公有理婆说婆有理，内容一直加，字段一直改。事不过三，第三次设计时，我们集体讨论反思为什么这么难形成共识？为什么每个人理解不同？为什么总是在改？<br>
<br>结论很一致，没有面向 YAML 的设计，只有面向对象的设计，设计语言也只有 UML，只有这些历经考验、成熟的设计方法论，才是最简单也是最高效的。<br>
<br>从上面那个一个巨大无比的 YAML 大家可以体会我们设计的复杂，但是这还是不是最痛苦的。最痛苦的是大家抛弃了原有的设计流程及设计语言，试图使用一个开放的 Map 来描述一切。当设计没有对象，也没有关系，只剩下 Map 里一个个属性，也就无所谓对错，也无所谓优劣。最后争来争去，最后不过是再加一个字段，争了一个寂寞。<br>
<h4>适用范围</h4>那 Operator 先设计 CRD，再开发 controller 的方式不正确吗？<br>
<br>答案：部分正确。<br>
<br>适用场景：与 Java Class 相同，简单对象不需要经过复杂的设计流程，直接设计 YAML 简单高效。<br>
<br>不适用场景：在设计一个复杂的体系时，例如：应用管理，包含多个对象且对象之间有复杂的关系，有复杂的用户故事，UML 和面向对象的设计就显得非常重要。<br>
<br>设计时只考虑 UML 和领域语言，设计完成后，CRD 可以认为是 Java 的 Class，或者是数据库的表结构，只是最终要实现时的一种选择。而且有很多对象不需要持久化，也不需要通过 Operator 机制触发对应的逻辑，就不需要设计 CRD，而是直接实现一个 controller 即可。<br>
<br>YAML 是接口或 Class 声明的一种格式化表达，常规 YAML 要尽可能小，尽可能职责单一，尽可能抽象。复杂的 YAML 是对简单 CRD 资源的一种编排结果，提供类似一站式资源配套方案。<br>
<br>在第 3 个版本及 PaaS-Core 设计时，我们就采取了如下的流程：<br>
<ol><li>UML 用例图；</li><li>梳理用户故事；</li><li>基于用户故事对齐 Domain Object，确定关键的业务对象以及对象间关系；</li><li>需要 Operator 化的对象，每个对象描述为一个 CRD，当然 CRD 缺乏接口、继承等面向对象的能力，可以通过其他方式曲线表达；</li><li>不需要 Operator 化的对象，直接编写 Controller。</li></ol><br>
<br><h3>误区2：一切皆合一</h3>为了保证一个应用的终态，或者为了使用 GitOps 管理一个应用，是否应该把应用相关的内容都放入一个 CRD 或一个 IAC 文件？根据 GitOps 设计，每次变更时需要下发整个文件？<br>
<h4>案例</h4>案例1：应用 WordPress，需要依赖一个 MySQL，终态如何定义？<br>
<pre class="prettyprint">apiVersion: apps.mwops.alibaba-inc.com/v1alpha1<br>
kind: AppDefinition<br>
metadata:<br>
labels:<br>
app: "WordPress"<br>
name: WordPress-1.0 //chart-name+chart-version<br>
namespace: kubeone<br>
spec:<br>
appName: WordPress  //chart-name<br>
version: 1.0 //chart-version<br>
type: apps.mwops.alibaba-inc.com/v1alpha1.argo-helm<br>
parameterValues:   //注 parameterValues标识业务属性<br>
- name: "enableTenant"<br>
  value: "1"<br>
- name: "CPU"<br>
  value: "1"<br>
- name: "MEM"<br>
  value: "2Gi"<br>
- name: "jvm"<br>
  value: "flag;gc"<br>
- name: replicas<br>
    value: 3<br>
- name: connectstring<br>
  valueFromConfigMap:<br>
    name: $&#123;resources:test-db.exposes.connectstring&#125;<br>
    expr: $&#123;connectstring&#125;<br>
- name: db_user_name<br>
  valueFromSecret:<br>
      ....<br>
resources:<br>
    - name: test-db //创建一个新的DB<br>
    type: apps.mwops.alibaba-inc.com/v1alpha1.database.mysqlha<br>
    parameterValues:<br>
      - name: cpu<br>
        value: 2<br>
      - name: memory<br>
        value: 4G<br>
      - name: storage<br>
        value: 20Gi <br>
      - name: username<br>
        value: myusername<br>
      - name: password<br>
        value: i_am_a_password<br>
        - name: dbname<br>
        value: wordPress<br>
     exposes:<br>
      - name: connectstring<br>
      - name: username<br>
      - name: password<br>
exposes:<br>
- name: dns<br>
  value: ...<br>
</pre><br>
上方的代码是 wordPress 应用的终态吗？这个文件包含了应用所需要的 DB 的定义和应用的定义，只要一次下发就可以先创建对应的数据库，再把应用拉起。<br>
<br>案例2：每次变更时，直接修改整个 yaml 的部分内容，修改后直接下发到 Kubernetes，引起不必要的变更。例如：要从 3 个节点扩容到 5 个节点，修改上面 YAML 文件的 replicas 之后，需要下发整个 YAML。整个下发的 YAML 经过二次解析成底层的 StatefulSet 或 Deployment，解析逻辑升级后，可能会产生不符合预期的变化，导致所有 Pod 重建。<br>
<h4>反思</h4>先回答第一个问题，上方 YAML 文件不是应用的终态，而是一个编排，此编排包含了 DB 的定义和应用的定义。应用的终态只应该包含自己必须的依赖引用，而不包含依赖是如何创建的。因为这个依赖引用可以是新创建的，也可以是一个已有的，也可以是手工填写的，依赖如何创建与应用终态无关。<br>
<pre class="prettyprint">apiVersion: apps.mwops.alibaba-inc.com/v1alpha1<br>
kind: AppDefinition<br>
metadata:<br>
labels:<br>
app: "WordPress"<br>
name: WordPress-1.0 //chart-name+chart-version<br>
namespace: kubeone<br>
spec:<br>
appName: WordPress  //chart-name<br>
version: 1.0 //chart-version<br>
name: WordPress-test<br>
type: apps.mwops.alibaba-inc.com/v1alpha1.argo-helm<br>
parameterValues:   //注 parameterValues标识业务属性<br>
- ....<br>
resources:<br>
- name: test-db-secret<br>
    value: "wordPress1Secret" //引用已有的secret  <br>
exposes:<br>
- name: dns<br>
  value: ...<br>
</pre><br>
创建一个应用，就不能先创建 db，再创建应用吗？  <br>
<br>可以的，多个对象之间依赖是通过编排实现的。编排有单个应用创建的编排，也有一个复杂站点创建的编排。以 Argo 为例：<br>
<pre class="prettyprint">apiVersion: argoproj.io/v1alpha1<br>
kind: Workflow<br>
metadata:<br>
generateName: wordPress-<br>
spec:<br>
templates:<br>
- name: wordPress<br>
steps:<br>
# 创建db<br>
- - name: wordpress-db<br>
  template: wordpress-db<br>
  arguments:<br>
     parameters: [&#123;name: wordpress-db1&#125;]<br>
# 创建应用<br>
 - - name: <br>
 template: wordpress<br>
 arguments:<br>
    parameters: [&#123;db-sercet: wordpress-db1&#125;]<br>
</pre><br>
针对第 2 个案例，是否每次交互都需要下发全部完整的 YAML？<br>
<br>答案：<br>
<ol><li>编排是一次性的配置，编排文件下发一次之后，后续操作都是操作单个对象，例如：变更时，只会单独变更 wordPress，或单独变更 wordPressDB，而不会一次性同时变更 2 个对象。</li><li>单独变更应用时，是否需要下发整个终态 YAML，这个要根据实际情况进行设计，值得大家思考。后面会提出针对整个应用生命周期状态机的设计，里面有详细的解释。</li></ol><br>
<br><h4>适用范围</h4>适用场景：CRD 或 IAC 定义时，单个对象的终态只应该包含自身及对依赖的引用。与面向对象的设计相同，我们不应该把所有类的定义都放到一个 Class 里面。<br>
<br>不适用场景：多个对象要一次性创建，并且需要按照顺序创建，存在依赖关系，需要通过编排层实现。<br>
<h3>误区3：一切皆终态</h3>体验了 Kubernetes 的终态化之后，大家在设计时言必称终态，仿佛不能用上终态设计，不下发一个 YAML 声明对象的终态就是落伍，就是上一代的设计。<br>
<h4>案例</h4>案例1：应用编排<br>
<br>还是以 WordPress 为例，将 WordPressDB 和 WordPress 放在一起进行部署，先部署 DB，再创建应用。示例 YAML 同上。<br>
<br>案例2：应用发布<br>
<br>应用第一次部署及后续的升级直接下发一个完整的应用 YAML，系统会自动帮你到达终态。但为了能够细粒度控制发布的流程，努力在 Deployment 或 StatefulSet 上下功夫，进行 partition 的控制，试图在终态里增加一点点的交互性。<br>
<h4>反思</h4>说到终态，必然要提到命令式、声明式编程，终态其实就是声明式最终的执行结果。我们先回顾一下命令式、终态式编程。<br>
<br><strong>命令式编程</strong><br>
<br>命令式编程的主要思想是关注计算机执行的步骤，即一步一步告诉计算机先做什么再做什么。<br>
<br>比如：如果你想在一个数字集合 collection（变量名）中筛选大于 5 的数字，你需要这样告诉计算机：<br>
<ul><li>第一步，创建一个存储结果的集合变量 results；</li><li>第二步，遍历这个数字集合 collection；</li><li>第三步，一个一个地判断每个数字是不是大于 5，如果是就将这个数字添加到结果集合变量 results 中。</li></ul><br>
<br>代码实现如下：<br>
<pre class="prettyprint">List results = new List();<br>
foreach(var num in collection)<br>
&#123;<br>
if (num > 5)<br>
results.Add(num);<br>
&#125; <br>
</pre><br>
很明显，这个样子的代码是很常见的一种，不管你用的是 C、C++ 还是 C#、Java、Javascript、BASIC、Python、Ruby 等，你都可以以这个方式写。<br>
<br><strong>声明式编程</strong><br>
<br>声明式编程是以数据结构的形式来表达程序执行的逻辑。它的主要思想是告诉计算机应该做什么，但不指定具体要怎么做。<br>
<br>SQL 语句就是最明显的一种声明式编程的例子，例如：<br>
<br>SELECT * FROM collection WHERE num > 5<br>
<br>除了 SQL，网页编程中用到的 HTML 和 CSS 也都属于声明式编程。<br>
<br>通过观察声明式编程的代码我们可以发现它有一个特点是它不需要创建变量用来存储数据。<br>
<br>另一个特点是它不包含循环控制的代码如 for， while。<br>
<br>换言之：<br>
<ul><li>命令式编程：命令“机器”如何去做事情（how），这样不管你想要的是什么（what），它都会按照你的命令实现。</li><li>声明式编程：告诉“机器”你想要的是什么（what），让机器想出如何去做（how）。</li></ul><br>
<br>当接口越是在表达“要什么”，就是越声明式；越是在表达“要怎样”，就是越命令式。SQL就是在表达要什么（数据），而不是表达怎么弄出我要的数据，所以它就很“声明式”。<br>
<br>简单的说，接口的表述方式越接近人类语言——词汇的串行连接（一个词汇实际上是一个概念）——就越“声明式”；越接近计算机语言——“顺序+分支+循环”的操作流程——就越“命令式”。<br>
<br>越是声明式，意味着下层要做更多的东西，或者说能力越强，也意味着效率的损失。越是命令式，意味着上层对下层有更多的操作空间，可以按照自己特定的需求要求下层按照某种方式来处理。<br>
<br>简单的讲，Imperative Programming Language（命令式语言）一般都有 control flow, 并且具有可以和其他设备进行交互的能力。而 Declarative Programming language（声明式语言）一般做不到这些。<br>
<br>基于以上的分析，编排或工作流本质是一个流程性控制的过程，一般是一次性的过程，无需强行终态化，而且建站编排执行结束后，不能保持终态，因为后续会根据单个应用进行发布和升级。案例1是一个典型的编排，只是一次性的创建了 2 个对象 DB 和应用的终态。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210421/029b15db53d7471c84e1caa511ae00eb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210421/029b15db53d7471c84e1caa511ae00eb.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
应用发布其实是通过一个发布单或工作流，控制 2 个不同版本的应用节点和流量的终态化的过程，不应该是应用终态的一部分，而是一个独立的控制流程。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210421/326ca38980e39302752f75c496d65572.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210421/326ca38980e39302752f75c496d65572.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>适用范围</h4>声明式或终态设计。<br>
<br>适用场景：无过多交互，无需关注底层实现的场景，即把声明提供给系统后，系统会自动化达到声明所要求的状态，而不需要人为干预。<br>
<br>不适用场景：一次性的流程编排，有频繁交互的控制流程。<br>
<br>命令式和声明式本就是 2 种互补的编程模式，就像有了面向对象之后，有人就鄙视面向过程的编程，现在有了声明式，就开始鄙视命令式编程，那一屋！<br>
<h3>误区4：一切交互皆 cr</h3>因为 Kubernetes 的 API 交互只能通过 YAML，导致大家的设计都以 cr 为中心，所有的交互都设计为下发一个 cr，通过 watch cr 触发对应的逻辑。<br>
<h4>案例</h4><ul><li>调用一个 http 接口或 function，需要下发一个 cr；</li><li>应用 crud 都下发完整 cr；</li></ul><br>
<br><h4>反思</h4><strong>案例1：是否所有的逻辑都需要下发一个 cr？</strong><br>
<br>下发 cr 其实做了比较多的事情，流程很长，效率并不高，流程如下：<br>
<ul><li>通过 API 传入 cr，cr 保存到 etcd；</li><li>触发 informer；</li><li>controller 接收到对应的事件，触发逻辑；</li><li>更新 cr 状态；</li><li>清理 cr，否则会占用 etcd 存储；</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210421/fd06ee714b5bfaea173bac5dc309661a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210421/fd06ee714b5bfaea173bac5dc309661a.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如果需要频繁的调用对应的接口，尽量通过 sdk 直接调用。<br>
<br><strong>案例2</strong><br>
<br>Kubernetes 对 YAML 操作命令有 create、apply、patch、delete、get 等，但一个应用的生命周期状态机不只是这几个命令可以涵盖，我们比较一下应用状态机（上）和 YAML 状态机（下）：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210421/45e562c8cf598e4e908ff55a5a380528.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210421/45e562c8cf598e4e908ff55a5a380528.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
不同的有状态应用，在收到不同的指令，需要触发不同的逻辑，例如：MQ 在收到 stop 指令时，需要先停写，检查数据是否消费完成。如果只是通过 YAML 状态机是无法涵盖应用状态机相关的 event，所以我们必须打破下发 cr 的模式。对于应用来说，理想的交互方式是通过 event driven 应用状态机的变化，状态发生变换时触发对应的逻辑。<br>
<h4>适用范围</h4>适用场景：需要持久化，保持终态的数据。<br>
<br>不适用场景：<br>
<ul><li>高频的服务调用，无需持久化的数据。</li><li>复杂状态机的驱动。</li></ul><br>
<br><h3>总结</h3>Kubernetes 给我们打开了一扇门，带给了我们很多优秀的设计，优秀的理念，但是这些设计和理念也是有自己的适用的场景，并不是放之四海而皆准。我们不应该盲从，试图一切都要 follow Kubernetes 的设计和规则，而抛弃之前的优秀设计理念。<br>
<br>软件设计经历了 10 多年的发展，形成了一套行之有效的设计方法论，Kubernetes 也是在这些设计方法论的支持下设计出来的。取其精华去其糟粕，是我们程序员应该做的事情。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/W_UjqI0Rd4AAVcafMiaYGA" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/W_UjqI0Rd4AAVcafMiaYGA</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            