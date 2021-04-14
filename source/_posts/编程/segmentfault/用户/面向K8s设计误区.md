
---
title: '面向K8s设计误区'
categories: 
 - 编程
 - segmentfault
 - 用户
headimg: 'https://segmentfault.com/img/bVcRfnN'
author: segmentfault
comments: false
date: 2021-04-14 08:08:45
thumbnail: 'https://segmentfault.com/img/bVcRfnN'
---

<div>   
<p><strong>K8s设计模式</strong></p><p>Kubernetes是一个具有普遍意义的容器编排工具，它提供了一套基于容器构建分布式系统的基础依赖，其意义等同于Linux在操作系统中的地位，可以认为是分布式的操作系统。</p><p><strong>自定义资源</strong></p><p>K8s提供了Pod、Service、Volume等一系列基础资源定义，为了更好提供扩展性，CRD 功能是在1.7 版本被引入。</p><p>用户可以根据自己的需求添加自定义的 Kubernetes 对象资源（CRD）。值得注意的是，这里用户自己添加的 Kubernetes 对象资源都是 native 的都是一等公民，和 Kubernetes 中自带的、原生的那些 Pod、Deployment 是同样的对象资源。在 Kubernetes 的 API Server 看来，它们都是存在于 etcd 中的一等资源。同时，自定义资源和原生内置的资源一样，都可以用 kubectl 来去创建、查看，也享有 RBAC、安全功能。用户可以开发自定义控制器来感知或者操作自定义资源的变化。</p><p><strong>Operator</strong></p><p>在自定义资源基础上，如何实现自定义资源创建或更新时的逻辑行为，K8s Operator提供了相应的开发框架。Operator通过扩展Kubernetes定义Custom Controller，list/watch 对应的自定义资源，在对应资源发生变化时，触发自定义的逻辑。</p><p>Operator 开发者可以像使用原生 API 进行应用管理一样，通过声明式的方式定义一组业务应用的期望终态，并且根据业务应用的自身特点进行相应控制器逻辑编写，以此完成对应用运行时刻生命周期的管理并持续维护与期望终态的一致性。<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRfnN" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>通俗的理解</p><p>CRD是K8s标准化的资源扩展能力，以java为例，int、long、Map、Object是java内置的类，用户可以自定义Class实现类的扩展，CRD就是K8s中的自定义类，CR就是对应类的一个instance。</p><p>Operator模式 = 自定义类 + 观察者模式，Operator模式让大家编写K8s的扩展变得非常简单快捷，逐渐成为面向K8s设计的标准。</p><p>Operator提供了标准化的设计流程：</p><p>使用 SDK 创建一个新的 Operator 项目<br>通过添加自定义资源（CRD）定义新的资源 API<br>指定使用 SDK API 来 watch 的资源<br>自定义Controller实现K8s协调（reconcile）逻辑<br>有了锤子，看到的只有钉子<br>我们团队（KubeOne团队）一直在致力于解决复杂中间件应用如何部署到K8s，自然也是Operator模式的践行者。经历了近2年的开发，初步解决了中间件在各个环境K8s的部署，当前中间也走了很多弯路，踩了很多坑。</p><p>KubeOne内核也经历3个大版本的迭代，前2次开发过程基本都是follow Operator标准开发流程进行开发设计。遵循一个标准的、典型的Operator的设计过程，看上去一切都是这么的完美，但是每次设计都非常痛苦，践行Operator模式之后，最值得反思和借鉴的就是”有了锤子，看到的只有钉子“，简单总结一下就是4个一切：</p><p>一切设计皆yaml<br>一切皆合一<br>一切皆终态<br>一切交互皆cr<br>误区1 一切设计皆yaml<br>K8s的API是yaml格式，Operator设计流程也是让大家首先定义crd，所以团队开始设计时直接采用了yaml格式。</p><p><strong>案例</strong></p><p>根据标准化流程，团队面向yaml设计流程大体如下：</p><p>先根据已知的数据初步整理一个大而全的yaml，做一下初步的分类，例如应用大概包含基础信息，依赖服务，运维逻辑，监控采集等，每个分类做一个子部分<br>开会讨论具体的内容是否能满足要求，结果每次开会都难以形成共识<br>因为总是有新的需求满足不了，在讨论A时，就有人提到B、C、D，不断有新的需求<br>每个部分的属性非常难统一，因为不同的实现属性差异较大<br>理解不一致，相同名字但使用时每个人的理解也不同<br>由于工期很紧，只能临时妥协，做一个中间态，后面再进一步优化<br>后续优化升级，相同的流程再来一遍，还是很难形成共识<br>这是第2个版本的设计：</p><p>apiVersion: apps.mwops.alibaba-inc.com/v1alpha1<br>kind: AppDefinition<br>metadata:<br>  labels:</p><pre><code>app: "A"</code></pre><p>name: A-1.0 //chart-name+chart-version<br>  namespace: kubeone<br>spec:<br>  appName: A  //chart-name<br>  version: 1.0 //chart-version<br>  type: apps.mwops.alibaba-inc.com/v1alpha1.argo-helm<br>  workloadSettings:   //注 workloadSettings 标识type应该使用的属性</p><pre><code>- name: "deployToK8SName"
  value: ""
- name: "deployToNamespace"
  value: $&#123;resources:namespace-resource.name&#125;</code></pre><p>parameterValues:   //注 parameterValues标识业务属性</p><pre><code>- name: "enableTenant"
  value: "1"
- name: "CPU"
  value: "1"
- name: "MEM"
  value: "2Gi"
- name: "jvm"
  value: "flag;gc"
- name: vip.fileserver-edas.ip
  value: $&#123;resources:fileserver_edas.ip&#125;
- name: DB_NAME
  valueFromConfigMap:
    name: $&#123;resources:rds-resource.cm-name&#125;
    expr: $&#123;database&#125;
- name: DB_PASSWORD
  valueFromSecret:
      name: $&#123;instancename&#125;-rds-secret
      expr: $&#123;password&#125;
- name: object-storage-endpoint
  value: $&#123;resources:object-storage.endpoint&#125;
- name: object-storage-username
  valueFromSecret:
      name: $&#123;resources:object-storage.secret-name&#125;
      expr: $&#123;username&#125;
- name: object-storage-password
  valueFromSecret:
      name: $&#123;resources:object-storage.secret-name&#125;
      expr: $&#123;password&#125;
- name: redis-endpoint
  value: $&#123;resources:redis.endpoint&#125;
- name: redis-password
  value: $&#123;resources:redis.password&#125;</code></pre><p>resources:</p><pre><code>  - name: tolerations
    type: apps.mwops.alibaba-inc.com/tolerations
    parameterValues:
       - name: key
         value: "sigma.ali/is-ecs"
       - name: key
         value: "sigma.ali/resource-pool"
  - name: namespace-resource
    type: apps.mwops.alibaba-inc.com/v1alpha1.namespace
    parameterValues:
      - name: name
        value: edas
  - name: fileserver-edas
    type: apps.mwops.alibaba-inc.com/v1alpha1.database.vip
    parameterValues:
      - name: port
        value: 21,80,8080,5000
      - name: src_port
        value: 21,80,8080,5000
      - name: type
        value: ClusterIP
      - name: check_type
        value: ""
      - name: uri
        value: ""
      - name: ip
        value: ""
  - name: test-db
    type: apps.mwops.alibaba-inc.com/v1alpha1.database.mysqlha
    parameterValues:
      - name: name
        value: test-db
      - name: user
        value: test-user
      - name: password
        value: test-passwd
      - name: secret
        value: test-db-mysqlha-secret
  - name: service-slb
    type: apps.mwops.alibaba-inc.com/v1alpha1.slb
    mode: post-create
    parameterValues:
      - name: service
        value: "serviceA"
      - name: annotations
        value: "app:a,version:1.0"
      - name: external-ip
        value: 
  - name: service-resource2
    type: apps.mwops.alibaba-inc.com/v1alpha1.service
    parameterValues: 
      - name: second-domain
        value: edas.console
      - name: ports
        value: "80:80"
      - name: selectors
        value: "app:a,version:1.0"
      - name: type
        value: "loadbalance"
  - name: service-dns
    type: apps.mwops.alibaba-inc.com/v1alpha1.dns
    parameterValues:
      - name: domain
        value: edas.server.$&#123;global:domain&#125;
      - name: vip
        value: $&#123;resources:service-resource2.EXTERNAL-IP&#125;
  - name: dns-resource
    type: apps.mwops.alibaba-inc.com/v1alpha1.dns
    parameterValues:
      - name: domain
        value: edas.console.$&#123;global:domain&#125;
      - name: vip
        value: “127.0.0.1”
  - name: cni-resource
    type: apps.mwops.alibaba-inc.com/v1alpha1.cni
    parameterValues:
      - name: count
        value: 4
      - name: ip_list
        value: 
  - name: object-storage
    type: apps.mwops.alibaba-inc.com/v1alpha1.objectStorage.minio
    parameterValues:
      - name: namespace
        value: test-ns
      - name: username
        value: test-user
      - name: password
        value: test-password
      - name: storage-capacity
        value: 20Gi
      - name: secret-name
        value: minio-my-store-access-keys
      - name: endpoint
        value: minio-instance-external-service
  - name: redis
    type: apps.mwops.alibaba-inc.com/v1alpha1.database.redis
    parameterValues:
      - name: cpu
        value: 500m
      - name: memory
        value: 128Mi
      - name: password
        value: i_am_a_password
      - name: storage-capacity
        value: 20Gi
      - name: endpoint
        value: redis-redis-cluster 
  - name: accesskey
    type: apps.mwops.alibaba-inc.com/v1alpha1.accesskey
    parameterValues:
      - name: name
        value: default
      - name: userName
        value: ecs_test@aliyun.com</code></pre><p>exposes:</p><pre><code>- name: dns
  value: $&#123;resources:dns-resource.domain&#125;
- name: db-endpoint
  valueFromConfigmap:
    name: $&#123;resources:rds-resource.cm-name&#125;
    expr: $&#123;endpoint&#125;:3306/$&#123;database&#125;
- name: ip_list
  value: $&#123;resources:cni-resource.ip_list&#125;
- name: object-storage-endpoint
  value: $&#123;resources:object-storage.endpoint&#125;.$&#123;resource:namespace-resource.name&#125;
- name: object-storage-username
  valueFromSecret:
      name: $&#123;resources:object-storage.secret-name&#125;
      expr: $&#123;username&#125;
- name: object-storage-password
  valueFromSecret:
      name: $&#123;resources:object-storage.secret-name&#125;
      expr: $&#123;password&#125;
- name: redis-endpoint
  value: $&#123;resources:redis.endpoint&#125;.$&#123;resource:namespace-resource.name&#125;
- name: redis-password
  value: $&#123;resources:redis.password&#125;</code></pre><p><strong>反思</strong></p><p>这样的痛苦难以用语言表达，感觉一切都脱离了掌控，没有统一的判断标准，设计标准，公说公有理婆说婆有理，内容一直加，字段一直改。事不过三，第三次设计时，我们集体讨论反思为什么这么难形成共识？为什么每个人理解不同？为什么总是在改？</p><p>结论很一致，没有面向yaml的设计，只有面向对象的设计，设计语言也只有UML，只有这些历经考验、成熟的设计方法论，才是最简单也是最高效的。</p><p>从上面那个一个巨大无比的yaml大家可以体会我们设计的复杂，但是这还是不是最痛苦的。最痛苦的是大家抛弃了原有的设计流程及设计语言，试图使用一个开放的Map来描述一切。当设计没有对象，也没有关系，只剩下Map里一个个属性，也就无所谓对错，也无所谓优劣。最后争来争去，最后不过是再加一个字段，争了一个寂寞。</p><p><strong>适用范围</strong></p><p>那Operator先设计CRD，再开发controller的方式不正确吗？</p><p>答案：部分正确</p><p><strong>适用场景</strong></p><p>与Java Class相同，简单对象不需要经过复杂的设计流程，直接设计yaml简单高效。</p><p><strong>不适用场景</strong></p><p>在设计一个复杂的体系时，例如：应用管理，包含多个对象且对象之间有复杂的关系，有复杂的用户故事，UML和面向对象的设计就显得非常重要。</p><p>设计时只考虑UML和领域语言，设计完成后，CRD可以认为是java的Class，或者是数据库的表结构，只是最终要实现时的一种选择。而且有很多对象不需要持久化，也不需要通过Operator机制触发对应的逻辑，就不需要设计CRD，而是直接实现一个controller即可。</p><p>yaml是接口或Class声明的一种格式化表达，常规yaml要尽可能小，尽可能职责单一，尽可能抽象。复杂的yaml是对简单CRD资源的一种编排结果，提供类似一站式资源配套方案。</p><p>在第3个版本及PaaS-Core设计时，我们就采取了如下的流程：</p><p>UML 用例图<br>梳理用户故事<br>基于用户故事对齐Domain Object，确定关键的业务对象以及对象间关系<br>需要Operator化的对象，每个对象描述为一个CRD，当然CRD缺乏接口、继承等面向对象的能力，可以通过其他方式曲线表达<br>不需要Operator化的对象，直接编写Controller<br>误区2 一切皆合一<br>为了保证一个应用的终态，或者为了使用gitops管理一个应用，是否应该把应用相关的内容都放入一个CRD或一个IAC文件？根据gitops设计，每次变更时需要下发整个文件？</p><p>案例</p><p>案例1: 应用WordPress，需要依赖一个MySQL，终态如何定义?</p><p>apiVersion: apps.mwops.alibaba-inc.com/v1alpha1<br>kind: AppDefinition<br>metadata:<br>  labels:</p><pre><code>app: "WordPress"</code></pre><p>name: WordPress-1.0 //chart-name+chart-version<br>  namespace: kubeone<br>spec:<br>  appName: WordPress  //chart-name<br>  version: 1.0 //chart-version<br>  type: apps.mwops.alibaba-inc.com/v1alpha1.argo-helm<br>  parameterValues:   //注 parameterValues标识业务属性</p><pre><code>- name: "enableTenant"
  value: "1"
- name: "CPU"
  value: "1"
- name: "MEM"
  value: "2Gi"
- name: "jvm"
  value: "flag;gc"
- name: replicas
    value: 3
- name: connectstring
  valueFromConfigMap:
    name: $&#123;resources:test-db.exposes.connectstring&#125;
    expr: $&#123;connectstring&#125;
- name: db_user_name
  valueFromSecret:
      ....</code></pre><p>resources:</p><pre><code>    - name: test-db //创建一个新的DB
    type: apps.mwops.alibaba-inc.com/v1alpha1.database.mysqlha
    parameterValues:
      - name: cpu
        value: 2
      - name: memory
        value: 4G
      - name: storage
        value: 20Gi 
      - name: username
        value: myusername
      - name: password
        value: i_am_a_password
        - name: dbname
        value: wordPress
     exposes:
      - name: connectstring
      - name: username
      - name: password</code></pre><p>exposes:</p><pre><code>- name: dns
  value: ...</code></pre><p>上方的代码是wordPress应用的终态吗？这个文件包含了应用所需要的DB的定义和应用的定义，只要一次下发就可以先创建对应的数据库，再把应用拉起。</p><p>案例2：每次变更时，直接修改整个yaml的部分内容，修改后直接下发到K8s，引起不必要的变更。例如：要从3个节点扩容到5个节点，修改上面yaml文件的replicas之后，需要下发整个yaml。整个下发的yaml经过二次解析成底层的StatefulSet或Deployment，解析逻辑升级后，可能会产生不符合预期的变化，导致所有pod重建。</p><p>反思</p><p>先回答第一个问题，上方yaml文件不是应用的终态，而是一个编排，此编排包含了DB的定义和应用的定义。应用的终态只应该包含自己必须的依赖引用，而不包含依赖是如何创建的。因为这个依赖引用可以是新创建的，也可以是一个已有的，也可以是手工填写的，依赖如何创建与应用终态无关。</p><p>apiVersion: apps.mwops.alibaba-inc.com/v1alpha1<br>kind: AppDefinition<br>metadata:<br>  labels:</p><pre><code>app: "WordPress"</code></pre><p>name: WordPress-1.0 //chart-name+chart-version<br>  namespace: kubeone<br>spec:<br>  appName: WordPress  //chart-name<br>  version: 1.0 //chart-version<br>  name: WordPress-test<br>  type: apps.mwops.alibaba-inc.com/v1alpha1.argo-helm<br>  parameterValues:   //注 parameterValues标识业务属性</p><pre><code>- ....</code></pre><p>resources:</p><pre><code>- name: test-db-secret
    value: "wordPress1Secret" //引用已有的secret  </code></pre><p>exposes:</p><pre><code>- name: dns
  value: ...</code></pre><p>创建一个应用，就不能先创建db，再创建应用吗？</p><p>可以的，多个对象之间依赖是通过编排实现的。编排有单个应用创建的编排，也有一个复杂站点创建的编排。以Argo为例。</p><p>apiVersion: argoproj.io/v1alpha1<br>kind: Workflow<br>metadata:<br>  generateName: wordPress-<br>spec:<br>  templates:</p><ul><li><p>name: wordPress<br>  steps:<br>  # 创建db</p><ul><li><ul><li><p>name: wordpress-db<br>  template: wordpress-db<br>  arguments:</p><pre><code> parameters: [&#123;name: wordpress-db1&#125;]</code></pre></li></ul></li></ul><h1>创建应用</h1><ul><li><ul><li>name: <br>template: wordpress<br>arguments:<br>   parameters: [&#123;db-sercet: wordpress-db1&#125;]</li></ul></li></ul></li></ul><p>针对第2个案例，是否每次交互都需要下发全部完整的yaml？</p><p>答案：</p><p>编排是一次性的配置，，编排文件下发一次之后，后续操作都是操作单个对象，例如：变更时，只会单独变更wordPress，或单独变更wordPressDB，而不会一次性同时变更2个对象。<br>单独变更应用时，是否需要下发整个终态yaml，这个要根据实际情况进行设计，值得大家思考。后面会提出针对整个应用生命周期状态机的设计，里面有详细的解释。<br>适用范围</p><p>适用场景</p><p>CRD或Iac定义时，单个对象的终态只应该包含自身及对依赖的引用。与面向对象的设计相同，我们不应该把所有类的定义都放到一个Class里面。</p><p>不适用场景</p><p>多个对象要一次性创建，并且需要按照顺序创建，存在依赖关系，需要通过编排层实现。</p><p>误区3 一切皆终态<br>体验了K8s的终态化之后，大家在设计时言必称终态，仿佛不能用上终态设计，不下发一个yaml声明对象的终态就是落伍，就是上一代的设计。</p><p>案例</p><p>案例1：应用编排 还是以WordPress为例，将WordPressDB和WordPress放在一起进行部署，先部署DB，再创建应用。示例yaml同上。</p><p>案例2：应用发布 应用第一次部署及后续的升级直接下发一个完整的应用yaml，系统会自动帮你到达终态。但为了能够细粒度控制发布的流程，努力在Deployment或StatefulSet上下功夫，进行partition的控制，试图在终态里增加一点点的交互性。</p><p>反思</p><p>说到终态，必然要提到命令式、声明式编程，终态其实就是声明式最终的执行结果。我们先回顾一下命令式、终态式编程。</p><p>命令式编程</p><p>命令式编程的主要思想是关注计算机执行的步骤，即一步一步告诉计算机先做什么再做什么。</p><p>比如：如果你想在一个数字集合 collection(变量名) 中筛选大于 5 的数字，你需要这样告诉计算机：</p><ol><li>第一步，创建一个存储结果的集合变量 results；</li><li>第二步，遍历这个数字集合 collection；</li><li>第三步：一个一个地判断每个数字是不是大于 5，如果是就将这个数字添加到结果集合变量 results 中。</li></ol><p>代码实现如下：</p><p>List results = new List();<br>foreach(var num in collection)<br>&#123;<br>if (num > 5)<br>results.Add(num);<br>&#125;<br>很明显，这个样子的代码是很常见的一种，不管你用的是 C, C++ 还是 C#, Java, Javascript, BASIC, Python, Ruby 等等，你都可以以这个方式写。</p><p>声明式编程</p><p>声明式编程是以数据结构的形式来表达程序执行的逻辑。它的主要思想是告诉计算机应该做什么，但不指定具体要怎么做。</p><p>SQL 语句就是最明显的一种声明式编程的例子，例如：</p><p>SELECT * FROM collection WHERE num > 5<br>除了 SQL，网页编程中用到的 HTML 和 CSS 也都属于声明式编程。</p><p>通过观察声明式编程的代码我们可以发现它有一个特点是它不需要创建变量用来存储数据。</p><p>另一个特点是它不包含循环控制的代码如 for， while。</p><p>换言之</p><p>• 命令式编程：命令“机器”如何去做事情(how)，这样不管你想要的是什么(what)，它都会按照你的命令实现。</p><p>• 声明式编程：告诉“机器”你想要的是什么(what)，让机器想出如何去做(how)。</p><p>当接口越是在表达“要什么”，就是越声明式；越是在表达“要怎样”，就是越命令式。SQL就是在表达要什么（数据），而不是表达怎么弄出我要的数据，所以它就很“声明式”。</p><p>简单的说，接口的表述方式越接近人类语言——词汇的串行连接（一个词汇实际上是一个概念）——就越“声明式”；越接近计算机语言——“顺序+分支+循环”的操作流程——就越“命令式”。</p><p>越是声明式，意味着下层要做更多的东西，或者说能力越强，也意味着效率的损失。越是命令式，意味着上层对下层有更多的操作空间，可以按照自己特定的需求要求下层按照某种方式来处理。</p><p>简单的讲，Imperative Programming Language (命令式语言)一般都有control flow, 并且具有可以和其他设备进行交互的能力。而Declarative Programming language (声明式语言) 一般做不到这些。</p><p>基于以上的分析，编排或工作流本质是一个流程性控制的过程，一般是一次性的过程，无需强行终态化，而且建站编排执行结束后，不能保持终态，因为后续会根据单个应用进行发布和升级。案例1是一个典型的编排，只是一次性的创建了2个对象DB和应用的终态。<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRfog" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>应用发布其实是通过一个发布单或工作流，控制2个不同版本的应用节点和流量的终态化的过程，不应该是应用终态的一部分，而是一个独立的控制流程。<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRfol" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>适用范围</p><p>声明式或终态设计</p><p>适用场景</p><p>无过多交互，无需关注底层实现的场景，即把声明提供给系统后，系统会自动化达到声明所要求的状态，而不需要人为干预。</p><p>不适用场景</p><p>一次性的流程编排，有频繁交互的控制流程</p><p>命令式和声明式本就是2种互补的编程模式，就像有了面向对象之后，有人就鄙视面向过程的编程，现在有了声明式，就开始鄙视命令式编程，那一屋！</p><p>误区4 一切交互皆cr<br>因为K8s的API交互只能通过yaml，导致大家的设计都以cr为中心，所有的交互都设计为下发一个cr，通过watch cr触发对应的逻辑。</p><p>案例</p><p>调用一个http接口或function，需要下发一个cr<br>应用crud都下发完整cr<br>反思</p><p>案例1</p><p>是否所有的逻辑都需要下发一个cr？</p><p>下发cr其实做了比较多的事情，流程很长，效率并不高，流程如下：</p><p>通过API传入cr，cr 保存到etcd<br>触发informer<br>controller接收到对应的事件，触发逻辑<br>更新cr状态<br>清理cr，否则会占用etcd存储<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRfop" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>如果需要频繁的调用对应的接口，尽量通过sdk直接调用。</p><p>案例2</p><p>K8s 对yaml操作命令有 create、apply、patch、delete、get等，但一个应用的生命周期状态机不只是这几个命令可以涵盖，我们比较一下应用状态机（上）和yaml状态机（下）：<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcRfon" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>不同的有状态应用，在收到不同的指令，需要触发不同的逻辑，例如：MQ在收到stop指令时，需要先停写，检查数据是否消费完成。如果只是通过yaml状态机是无法涵盖应用状态机相关的event，所以我们必须打破下发cr的模式。对于应用来说，理想的交互方式是通过event driven 应用状态机的变化，状态发生变换时触发对应的逻辑。</p><p>适用范围</p><p>适用场景</p><p>需要持久化，保持终态的数据</p><p>不适用场景</p><p>高频的服务调用，无需持久化的数据</p><p>复杂状态机的驱动</p><p><strong>总结</strong><br>K8s给我们打开了一扇门，带给了我们很多优秀的设计，优秀的理念，但是这些设计和理念也是有自己的适用的场景，并不是放之四海而皆准。我们不应该盲从，试图一切都要follow k8s的设计和规则，而抛弃之前的优秀设计理念。</p><p>软件设计经历了10多年的发展，形成了一套行之有效的设计方法论，k8s也是在这些设计方法论的支持下设计出来的。取其精华去其糟粕，是我们程序员应该做的事情。<br><a href="https://developer.aliyun.com/article/783530?utm_content=g_1000262601" rel="nofollow">原文链接</a><br>本文为阿里云原创内容，未经允许不得转载。</p>  
</div>
            