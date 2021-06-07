
---
title: '源码解析：Kubernetes 创建 Pod 时，背后发生了什么（一）'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=9136'
author: Dockone
comments: false
date: 2021-06-07 00:40:14
thumbnail: 'https://picsum.photos/400/300?random=9136'
---

<div>   
<br>本文试图回答以下问题：<strong>敲下 <code class="prettyprint">kubectl run nginx --image=nginx --replicas=3</code> 命令后</strong>， <strong>Kubernetes 中发生了哪些事情？</strong><br>
<br>要弄清楚这个问题，我们需要：<br>
<ol><li>了解 Kubernetes 几个核心组件的启动过程，它们分别做了哪些事情，以及</li><li>从客户端发起请求到 Pod ready 的整个过程。</li></ol><br>
<br><h3>Kubernetes 组件启动过程</h3>首先看几个核心组件的启动过程分别做了哪些事情。<br>
<h4>kube-apiserver 启动</h4><strong>调用栈</strong><br>
<br>创建命令行（<code class="prettyprint">kube-apiserver</code>）入口：<br>
<pre class="prettyprint">main                                         // cmd/kube-apiserver/apiserver.go<br>
|-cmd := app.NewAPIServerCommand()          // cmd/kube-apiserver/app/server.go<br>
|  |-RunE := func() &#123;<br>
|      Complete()<br>
|        |-ApplyAuthorization(s.Authorization)<br>
|        |-if TLS:<br>
|            ServiceAccounts.KeyFiles = []string&#123;CertKey.KeyFile&#125;<br>
|      Validate()<br>
|      Run(completedOptions, handlers) // 核心逻辑<br>
|    &#125;<br>
|-cmd.Execute()<br>
</pre><br>
<code class="prettyprint">kube-apiserver</code> 启动后，会执行到其中的 <code class="prettyprint">Run()</code> 方法：<br>
<pre class="prettyprint">Run()          // cmd/kube-apiserver/app/server.go<br>
|-server = CreateServerChain()<br>
|           |-CreateKubeAPIServerConfig()<br>
|           |   |-buildGenericConfig<br>
|           |   |   |-genericapiserver.NewConfig()     // staging/src/k8s.io/apiserver/pkg/server/config.go<br>
|           |   |   |  |-return &Config&#123;<br>
|           |   |   |       Serializer:             codecs,<br>
|           |   |   |       BuildHandlerChainFunc:  DefaultBuildHandlerChain, // 注册 handler<br>
|           |   |   |    &#125; <br>
|           |   |   |<br>
|           |   |   |-OpenAPIConfig = DefaultOpenAPIConfig()  // OpenAPI schema<br>
|           |   |   |-kubeapiserver.NewStorageFactoryConfig() // etcd 相关配置<br>
|           |   |   |-APIResourceConfig = genericConfig.MergedResourceConfig<br>
|           |   |   |-storageFactoryConfig.Complete(s.Etcd)<br>
|           |   |   |-storageFactory = completedStorageFactoryConfig.New()<br>
|           |   |   |-s.Etcd.ApplyWithStorageFactoryTo(storageFactory, genericConfig)<br>
|           |   |   |-BuildAuthorizer(s, genericConfig.EgressSelector, versionedInformers)<br>
|           |   |   |-pluginInitializers, admissionPostStartHook = admissionConfig.New()<br>
|           |   |<br>
|           |   |-capabilities.Initialize<br>
|           |   |-controlplane.ServiceIPRange()<br>
|           |   |-config := &controlplane.Config&#123;&#125;<br>
|           |   |-AddPostStartHook("start-kube-apiserver-admission-initializer", admissionPostStartHook)<br>
|           |   |-ServiceAccountIssuerURL = s.Authentication.ServiceAccounts.Issuer<br>
|           |   |-ServiceAccountJWKSURI = s.Authentication.ServiceAccounts.JWKSURI<br>
|           |   |-ServiceAccountPublicKeys = pubKeys<br>
|           |<br>
|           |-createAPIExtensionsServer<br>
|           |-CreateKubeAPIServer<br>
|           |-createAggregatorServer    // cmd/kube-apiserver/app/aggregator.go<br>
|           |   |-aggregatorConfig.Complete().NewWithDelegate(delegateAPIServer)   // staging/src/k8s.io/kube-aggregator/pkg/apiserver/apiserver.go<br>
|           |   |  |-apiGroupInfo := NewRESTStorage()<br>
|           |   |  |-GenericAPIServer.InstallAPIGroup(&apiGroupInfo)<br>
|           |   |  |-InstallAPIGroups<br>
|           |   |  |-openAPIModels := s.getOpenAPIModels(APIGroupPrefix, apiGroupInfos...)<br>
|           |   |  |-for apiGroupInfo := range apiGroupInfos &#123;<br>
|           |   |  |   s.installAPIResources(APIGroupPrefix, apiGroupInfo, openAPIModels)<br>
|           |   |  |   s.DiscoveryGroupManager.AddGroup(apiGroup)<br>
|           |   |  |   s.Handler.GoRestfulContainer.Add(discovery.NewAPIGroupHandler(s.Serializer, apiGroup).WebService())<br>
|           |   |  |<br>
|           |   |  |-GenericAPIServer.Handler.NonGoRestfulMux.Handle("/apis", apisHandler)<br>
|           |   |  |-GenericAPIServer.Handler.NonGoRestfulMux.UnlistedHandle("/apis/", apisHandler)<br>
|           |   |  |-<br>
|           |   |-<br>
|-prepared = server.PrepareRun()     // staging/src/k8s.io/kube-aggregator/pkg/apiserver/apiserver.go<br>
|            |-GenericAPIServer.AddPostStartHookOrDie<br>
|            |-GenericAPIServer.PrepareRun<br>
|            |  |-routes.OpenAPI&#123;&#125;.Install()<br>
|            |     |-registerResourceHandlers // staging/src/k8s.io/apiserver/pkg/endpoints/installer.go<br>
|            |         |-POST: XX<br>
|            |         |-GET: XX<br>
|            |<br>
|            |-openapiaggregator.BuildAndRegisterAggregator()<br>
|            |-openapiaggregator.NewAggregationController()<br>
|            |-preparedAPIAggregator&#123;&#125;<br>
|-prepared.Run() // staging/src/k8s.io/kube-aggregator/pkg/apiserver/apiserver.go<br>
|-s.runnable.Run()<br>
</pre><br>
<strong>一些重要步骤</strong><br>
<ol><li><strong>创建 server chain</strong>。Server aggregation（聚合）是一种支持多 apiserver 的方式，其中包括了一个 <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/cmd/kube-apiserver/app/server.go#L219">generic apiserver</a>，作为默认实现。</li><li><strong>生成 OpenAPI schema</strong>，保存到 apiserver 的  <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/apiserver/pkg/server/config.go#L167">Config.OpenAPIConfig 字段</a>。</li><li>遍历 schema 中的所有 API group，为每个 API group 配置一个  <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/kube-aggregator/pkg/apiserver/apiserver.go#L204">storage provider</a>，这是一个通用 backend 存储抽象层。</li><li>遍历每个 group 版本，为每个 HTTP route  <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/apiserver/pkg/endpoints/groupversion.go#L92">配置 REST mappings</a>。稍后处理请求时，就能将 requests 匹配到合适的 handler。</li></ol><br>
<br><h4>controller-manager 启动</h4><strong>调用栈</strong><br>
<pre class="prettyprint">NewDeploymentController<br>
NewReplicaSetController<br>
</pre><br>
<h4>kubelet 启动</h4><strong>调用栈</strong><br>
<pre class="prettyprint">main                                                                            // cmd/kubelet/kubelet.go<br>
|-NewKubeletCommand                                                            // cmd/kubelet/app/server.go<br>
|-Run                                                                        // cmd/kubelet/app/server.go<br>
  |-initForOS                                                               // cmd/kubelet/app/server.go<br>
  |-run                                                                     // cmd/kubelet/app/server.go<br>
    |-initConfigz                                                           // cmd/kubelet/app/server.go<br>
    |-InitCloudProvider<br>
    |-NewContainerManager<br>
    |-ApplyOOMScoreAdj<br>
    |-PreInitRuntimeService<br>
    |-RunKubelet                                                            // cmd/kubelet/app/server.go<br>
    | |-k = createAndInitKubelet                                            // cmd/kubelet/app/server.go<br>
    | |  |-NewMainKubelet<br>
    | |  |  |-watch k8s Service<br>
    | |  |  |-watch k8s Node<br>
    | |  |  |-klet := &Kubelet&#123;&#125;<br>
    | |  |  |-init klet fields<br>
    | |  |<br>
    | |  |-k.BirthCry()<br>
    | |  |-k.StartGarbageCollection()<br>
    | |<br>
    | |-startKubelet(k)                                                     // cmd/kubelet/app/server.go<br>
    |    |-go k.Run()                                                       // -> pkg/kubelet/kubelet.go<br>
    |    |  |-go cloudResourceSyncManager.Run()<br>
    |    |  |-initializeModules<br>
    |    |  |-go volumeManager.Run()<br>
    |    |  |-go nodeLeaseController.Run()<br>
    |    |  |-initNetworkUtil() // setup iptables<br>
    |    |  |-go Until(PerformPodKillingWork, 1*time.Second, neverStop)<br>
    |    |  |-statusManager.Start()<br>
    |    |  |-runtimeClassManager.Start<br>
    |    |  |-pleg.Start()<br>
    |    |  |-syncLoop(updates, kl)                                         // pkg/kubelet/kubelet.go<br>
    |    |<br>
    |    |-k.ListenAndServe<br>
    |<br>
    |-go http.ListenAndServe(healthz)<br>
</pre><br>
<h4>小结</h4>以上核心组件启动完成后，就可以从命令行发起请求创建 Pod 了。<br>
<h3>kubectl（命令行客户端）</h3><h4>调用栈概览</h4><pre class="prettyprint">NewKubectlCommand                                    // staging/src/k8s.io/kubectl/pkg/cmd/cmd.go<br>
|-matchVersionConfig = NewMatchVersionFlags()<br>
|-f = cmdutil.NewFactory(matchVersionConfig)<br>
|      |-clientGetter = matchVersionConfig<br>
|-NewCmdRun(f)                                      // staging/src/k8s.io/kubectl/pkg/cmd/run/run.go<br>
|  |-Complete                                       // staging/src/k8s.io/kubectl/pkg/cmd/run/run.go<br>
|  |-Run(f)                                         // staging/src/k8s.io/kubectl/pkg/cmd/run/run.go<br>
|    |-validate parameters<br>
|    |-generators = GeneratorFn("run")<br>
|    |-runObj = createGeneratedObject(generators)   // staging/src/k8s.io/kubectl/pkg/cmd/run/run.go<br>
|    |           |-obj = generator.Generate()       // -> staging/src/k8s.io/kubectl/pkg/generate/versioned/run.go<br>
|    |           |        |-get pod params<br>
|    |           |        |-pod = v1.Pod&#123;params&#125;<br>
|    |           |        |-return &pod<br>
|    |           |-mapper = f.ToRESTMapper()        // -> staging/src/k8s.io/cli-runtime/pkg/genericclioptions/config_flags.go<br>
|    |           |  |-f.clientGetter.ToRESTMapper() // -> staging/src/k8s.io/kubectl/pkg/cmd/util/factory_client_access.go<br>
|    |           |     |-f.Delegate.ToRESTMapper()  // -> staging/src/k8s.io/kubectl/pkg/cmd/util/kubectl_match_version.go<br>
|    |           |        |-ToRESTMapper            // -> staging/src/k8s.io/cli-runtime/pkg/resource/builder.go<br>
|    |           |        |-delegate()              //    staging/src/k8s.io/cli-runtime/pkg/resource/builder.go<br>
|    |           |--actualObj = resource.NewHelper(mapping).XX.Create(obj)<br>
|    |-PrintObj(runObj.Object)<br>
|<br>
|-NewCmdEdit(f)      // kubectl edit   命令<br>
|-NewCmdScale(f)     // kubectl scale  命令<br>
|-NewCmdCordon(f)    // kubectl cordon 命令<br>
|-NewCmdUncordon(f)<br>
|-NewCmdDrain(f)<br>
|-NewCmdTaint(f)<br>
|-NewCmdExecute(f)<br>
|-...<br>
</pre><br>
<h4>参数验证（validation）和资源对象生成器（generator）</h4><strong>参数验证</strong><br>
<br>敲下 <code class="prettyprint">kubectl</code> 命令后，它首先会做一些<strong>客户端侧</strong>的验证。 如果命令行参数有问题，例如，<a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/kubectl/pkg/cmd/run/run.go#L262">镜像名为空或格式不对</a>，这里会直接报错，从而避免了将明显错误的请求发给 kube-apiserver，减轻了后者的压力。<br>
<br>此外，kubectl 还会检查其他一些配置，例如：<br>
<ul><li>是否需要记录（record）这条命令（用于 rollout 或审计）</li><li>是否只是测试执行（<code class="prettyprint">--dry-run</code>）</li></ul><br>
<br><strong>创建 HTTP 请求</strong><br>
<br>所有<strong>查询或修改 Kubernetes 资源的操作</strong>都需要与 kube-apiserver 交互，后者会进一步和 etcd 通信。<br>
<br>因此，验证通过之后，kubectl 接下来会<strong>创建发送给 kube-apiserver 的 HTTP 请求</strong>。<br>
<br><strong>Generators</strong><br>
<br><strong>创建 HTTP 请求用到了所谓的</strong> <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/kubectl/pkg/cmd/run/run.go#L300">generator</a>（<a href="https://kubernetes.io/docs/user-guide/kubectl-conventions/#generators">文档</a>），它<strong>封装了资源的序列化（serialization）操作</strong>。 例如，创建 Pod 时用到的 generator 是 <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/kubectl/pkg/generate/versioned/run.go#L233"><code class="prettyprint">BasicPod</code></a>：<br>
<pre class="prettyprint">// staging/src/k8s.io/kubectl/pkg/generate/versioned/run.go<br>
<br>
type BasicPod struct&#123;&#125;<br>
<br>
func (BasicPod) ParamNames() []generate.GeneratorParam &#123;<br>
return []generate.GeneratorParam&#123;<br>
    &#123;Name: "labels", Required: false&#125;,<br>
    &#123;Name: "name", Required: true&#125;,<br>
    &#123;Name: "image", Required: true&#125;,<br>
    ...<br>
&#125;<br>
&#125; <br>
</pre><br>
每个 generator 都实现了一个 <code class="prettyprint">Generate()</code> 方法，用于<strong>生成一个该资源的运行时对象（runtime object）</strong>。 对于 <code class="prettyprint">BasicPod</code>，其<a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/kubectl/pkg/generate/versioned/run.go#L259">实现</a>为：<br>
<pre class="prettyprint">func (BasicPod) Generate(genericParams map[string]interface&#123;&#125;) (runtime.Object, error) &#123;<br>
pod := v1.Pod&#123;<br>
    ObjectMeta: metav1.ObjectMeta&#123;  // metadata 字段<br>
        Name:        name,<br>
        Labels:      labels,<br>
        ...<br>
    &#125;,<br>
    Spec: v1.PodSpec&#123;               // spec 字段<br>
        ServiceAccountName: params["serviceaccount"],<br>
        Containers: []v1.Container&#123;<br>
            &#123;<br>
                Name:            name,<br>
                Image:           params["image"]<br>
            &#125;,<br>
        &#125;,<br>
    &#125;,<br>
&#125;<br>
<br>
return &pod, nil<br>
&#125; <br>
</pre><br>
<h4>API group 和版本协商（version negotiation）</h4>有了 runtime object 之后，kubectl 需要用合适的 API 将请求发送给 kube-apiserver。<br>
<br><strong>API Group</strong><br>
<br>Kubernetes 用 API group 来管理 resource API。 这是一种不同于 monolithic API（所有 API 扁平化）的 API 管理方式。<br>
<br>具体来说，<strong>同一资源的不同版本的 API，会放到一个 group 里面</strong>。 例如 Deployment 资源的 API group 名为 <code class="prettyprint">apps</code>，最新的版本是 <code class="prettyprint">v1</code>。这也是为什么 我们在创建 Deployment 时，需要在 yaml 中指定 <code class="prettyprint">apiVersion: apps/v1</code> 的原因。<br>
<br><strong>版本协商</strong><br>
<br>生成 runtime object 之后，kubectl 就开始 <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/kubectl/pkg/cmd/run/run.go#L610-L619">搜索合适的 API group 和版本</a>：<br>
<pre class="prettyprint">// staging/src/k8s.io/kubectl/pkg/cmd/run/run.go<br>
<br>
obj := generator.Generate(params) // 创建运行时对象<br>
mapper := f.ToRESTMapper()        // 寻找适合这个资源（对象）的 API group<br>
</pre><br>
然后<a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/kubectl/pkg/cmd/run/run.go#L641">创建一个正确版本的客户端（versioned client）</a>：<br>
<pre class="prettyprint">// staging/src/k8s.io/kubectl/pkg/cmd/run/run.go<br>
<br>
gvks, _ := scheme.Scheme.ObjectKinds(obj)<br>
mapping := mapper.RESTMapping(gvks[0].GroupKind(), gvks[0].Version)<br>
</pre><br>
这个客户端能感知资源的 REST 语义。<br>
<br>以上过程称为<strong>版本协商</strong>。在实现上，kubectl 会 <strong>扫描 kube-apiserver 的 <code class="prettyprint">/apis</code> 路径</strong>（OpenAPI 格式的 schema 文档），获取所有的 API groups。<br>
<br>出于性能考虑，kubectl 会 <a href="https://github.com/kubernetes/kubernetes/blob/v1.14.0/staging/src/k8s.io/cli-runtime/pkg/genericclioptions/config_flags.go#L234">缓存这份 OpenAPI schema</a>， 路径是  <code class="prettyprint">~/.kube/cache/discovery</code>。<strong>想查看这个 API discovery 过程，可以删除这个文件</strong>， 然后随便执行一条 kubectl 命令，并指定足够大的日志级别（例如 <code class="prettyprint">kubectl get ds -v 10</code>）。<br>
<br><strong>发送 HTTP 请求</strong><br>
<br>现在有了 runtime object，也找到了正确的 API，因此接下来就是 将请求真正<a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/kubectl/pkg/cmd/run/run.go#L654">发送出去</a>：<br>
<pre class="prettyprint">// staging/src/k8s.io/kubectl/pkg/cmd/cmd.go<br>
<br>
    actualObj = resource.<br>
        NewHelper(client, mapping).<br>
        DryRun(o.DryRunStrategy == cmdutil.DryRunServer).<br>
        WithFieldManager(o.fieldManager).<br>
        Create(o.Namespace, false, obj)<br>
</pre><br>
发送成功后，会以恰当的格式打印返回的消息。<br>
<h4>客户端认证（client auth）</h4>前面其实有意漏掉了一步：客户端认证。它发生在发送 HTTP 请求之前。<br>
<br><strong>用户凭证（credentials）一般都放在 kubeconfig 文件中，但这个文件可以位于多个位置</strong>， 优先级从高到低：<br>
<ul><li>命令行 <code class="prettyprint">--kubeconfig &lt;file></code></li><li>环境变量 <code class="prettyprint">$KUBECONFIG</code></li><li>某些<a href="https://github.com/kubernetes/client-go/blob/v1.21.0/tools/clientcmd/loader.go#L52">预定义的路径</a>，例如 <code class="prettyprint">~/.kube</code>。</li></ul><br>
<br><strong>这个文件中存储了集群、用户认证等信息</strong>，如下面所示：<br>
<pre class="prettyprint">apiVersion: v1<br>
clusters:<br>
- cluster:<br>
certificate-authority: /etc/kubernetes/pki/ca.crt<br>
server: https://192.168.2.100:443<br>
name: k8s-cluster-1<br>
contexts:<br>
- context:<br>
cluster: k8s-cluster-1<br>
user: default-user<br>
name: default-context<br>
current-context: default-context<br>
kind: Config<br>
preferences: &#123;&#125;<br>
users:<br>
- name: default-user<br>
user:<br>
client-certificate: /etc/kubernetes/pki/admin.crt<br>
client-key: /etc/kubernetes/pki/admin.key<br>
</pre><br>
有了这些信息之后，客户端就可以组装 HTTP 请求的认证头了。支持的认证方式有几种：<br>
<ul><li><strong>X509 证书</strong>：放到 <a href="https://github.com/kubernetes/client-go/blob/82aa063804cf055e16e8911250f888bc216e8b61/rest/transport.go#L80-L89">TLS</a> 中发送；</li><li><strong>Bearer token</strong>：放到 HTTP <code class="prettyprint">&quot;Authorization&quot;</code> 头中 <a href="https://github.com/kubernetes/client-go/blob/c6f8cf2c47d21d55fa0df928291b2580544886c8/transport/round_trippers.go#L314">发送</a>；</li><li><strong>用户名密码</strong>：放到 HTTP basic auth <a href="https://github.com/kubernetes/client-go/blob/c6f8cf2c47d21d55fa0df928291b2580544886c8/transport/round_trippers.go#L223">发送</a>；</li><li><strong>OpenID auth</strong>：需要先由用户手动处理，将其转成一个 token，然后和 bearer token 类似发送。</li></ul><br>
<br><h3>kube-apiserver</h3>请求从客户端发出后，便来到服务端，也就是 kube-apiserver。<br>
<h4>调用栈概览</h4><pre class="prettyprint">buildGenericConfig<br>
|-genericConfig = genericapiserver.NewConfig(legacyscheme.Codecs)  // cmd/kube-apiserver/app/server.go<br>
<br>
NewConfig       // staging/src/k8s.io/apiserver/pkg/server/config.go<br>
|-return &Config&#123;<br>
  Serializer:             codecs,<br>
  BuildHandlerChainFunc:  DefaultBuildHandlerChain,<br>
&#125;                          /<br>
                        /<br>
                      /<br>
                    /<br>
DefaultBuildHandlerChain       // staging/src/k8s.io/apiserver/pkg/server/config.go<br>
|-handler := filterlatency.TrackCompleted(apiHandler)<br>
|-handler = genericapifilters.WithAuthorization(handler)<br>
|-handler = genericapifilters.WithAudit(handler)<br>
|-handler = genericapifilters.WithAuthentication(handler)<br>
|-return handler<br>
<br>
<br>
WithAuthentication<br>
|-withAuthentication<br>
|-resp, ok := AuthenticateRequest(req)<br>
|  |-for h := range authHandler.Handlers &#123;<br>
|      resp, ok := currAuthRequestHandler.AuthenticateRequest(req)<br>
|      if ok &#123;<br>
|          return resp, ok, err<br>
|      &#125;<br>
|    &#125;<br>
|    return nil, false, utilerrors.NewAggregate(errlist)<br>
|<br>
|-audiencesAreAcceptable(apiAuds, resp.Audiences)<br>
|-req.Header.Del("Authorization")<br>
|-req = req.WithContext(WithUser(req.Context(), resp.User))<br>
|-return handler.ServeHTTP(w, req)<br>
</pre><br>
<h4>认证（Authentication）</h4>kube-apiserver 首先会对请求进行<strong>认证（authentication）</strong>，以确保用户身份是合法的（verify that the requester is who they say they are）。<br>
<br>具体过程：启动时，检查所有的 <a href="https://kubernetes.io/docs/admin/kube-apiserver/">命令行参数</a>，组织成一个 authenticator list，例如：<br>
<ul><li>如果指定了 <code class="prettyprint">--client-ca-file</code>，就会将 x509 证书加到这个列表；</li><li>如果指定了 <code class="prettyprint">--token-auth-file</code>，就会将 token 加到这个列表；</li></ul><br>
<br>不同 anthenticator 做的事情有所不同：<br>
<ul><li><a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/apiserver/pkg/authentication/request/x509/x509.go#L60">x509 handler</a> 验证该 HTTP 请求是用 TLS key 加密的，并且有 CA root 证书的签名。</li><li><a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/apiserver/pkg/authentication/request/bearertoken/bearertoken.go#L38">bearer token handler</a> 验证请求中带的 token（HTTP Authorization 头中），在 apiserver 的 auth file 中是存在的（<code class="prettyprint">--token-auth-file</code>）。</li><li><a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/apiserver/plugin/pkg/authenticator/request/basicauth/basicauth.go#L37">basicauth handler</a> 对 basic auth 信息进行校验。</li></ul><br>
<br><strong>如果认证成功，就会将 <code class="prettyprint">Authorization</code> 头从请求中删除</strong>，然后在上下文中<a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/apiserver/pkg/endpoints/filters/authentication.go#L71-L75">加上用户信息</a>。这使得后面的步骤（例如鉴权和 admission control）能用到这里已经识别出的用户身份信息。<br>
<pre class="prettyprint">// staging/src/k8s.io/apiserver/pkg/endpoints/filters/authentication.go<br>
<br>
// WithAuthentication creates an http handler that tries to authenticate the given request as a user, and then<br>
// stores any such user found onto the provided context for the request.<br>
// On success, "Authorization" header is removed from the request and handler<br>
// is invoked to serve the request.<br>
func WithAuthentication(handler http.Handler, auth authenticator.Request, failed http.Handler,<br>
apiAuds authenticator.Audiences) http.Handler &#123;<br>
return withAuthentication(handler, auth, failed, apiAuds, recordAuthMetrics)<br>
&#125;<br>
<br>
func withAuthentication(handler http.Handler, auth authenticator.Request, failed http.Handler,<br>
apiAuds authenticator.Audiences, metrics recordMetrics) http.Handler &#123;<br>
return http.HandlerFunc(func(w http.ResponseWriter, req *http.Request) &#123;<br>
    resp, ok := auth.AuthenticateRequest(req) // 遍历所有 authenticator，任何一个成功就返回 OK<br>
    if !ok &#123;<br>
        return failed.ServeHTTP(w, req)       // 所有认证方式都失败了<br>
    &#125;<br>
<br>
    if !audiencesAreAcceptable(apiAuds, resp.Audiences) &#123;<br>
        fmt.Errorf("unable to match the audience: %v , accepted: %v", resp.Audiences, apiAuds)<br>
        failed.ServeHTTP(w, req)<br>
        return<br>
    &#125;<br>
<br>
    req.Header.Del("Authorization") // 认证成功后，这个 header 就没有用了，可以删掉<br>
<br>
    // 将用户信息添加到请求上下文中，供后面的步骤使用<br>
    req = req.WithContext(WithUser(req.Context(), resp.User))<br>
    handler.ServeHTTP(w, req)<br>
&#125;)<br>
&#125; <br>
</pre><br>
<code class="prettyprint">AuthenticateRequest()</code> 实现：遍历所有 authenticator，任何一个成功就返回 OK。<br>
<pre class="prettyprint">// staging/src/k8s.io/apiserver/pkg/authentication/request/union/union.go<br>
<br>
func (authHandler *unionAuthRequestHandler) AuthenticateRequest(req) (*Response, bool) &#123;<br>
for currAuthRequestHandler := range authHandler.Handlers &#123;<br>
    resp, ok := currAuthRequestHandler.AuthenticateRequest(req)<br>
    if ok &#123;<br>
        return resp, ok, err<br>
    &#125;<br>
&#125;<br>
<br>
return nil, false, utilerrors.NewAggregate(errlist)<br>
&#125; <br>
</pre><br>
<h4>鉴权（Authorization）</h4><strong>发送者身份（认证）是一个问题，但他是否有权限执行这个操作（鉴权），是另一个问题</strong>。因此确认发送者身份之后，还需要进行鉴权。<br>
<br>鉴权的过程与认证非常相似，也是逐个匹配 authorizer 列表中的 authorizer：如果都失败了， 返回  <code class="prettyprint">Forbidden</code>  并停止  <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/apiserver/pkg/endpoints/filters/authorization.go#L60">进一步处理</a>。如果成功，就继续。<br>
<br>内置的 <strong>几种 authorizer 类型</strong>：<br>
<ul><li><a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/apiserver/plugin/pkg/authorizer/webhook/webhook.go#L143">webhook</a>：与其他服务交互，验证是否有权限。</li><li><a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/pkg/auth/authorizer/abac/abac.go#L223">ABAC</a>：根据<strong>静态文件中规定的策略</strong>（policies）来进行鉴权。</li><li><a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/plugin/pkg/auth/authorizer/rbac/rbac.go#L43">RBAC</a>：根据 role 进行鉴权，其中 role 是 Kubernetes 管理员提前配置的。</li><li><a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/plugin/pkg/auth/authorizer/node/node_authorizer.go#L67">Node</a>：确保 node clients，例如 kubelet，只能访问本机内的资源。</li></ul><br>
<br>要看它们的具体做了哪些事情，可以查看它们各自的 <code class="prettyprint">Authorize()</code> 方法。<br>
<h4>Admission control</h4>至此，认证和鉴权都通过了。但这还没结束，Kubernetes 中的<strong>其它组件还需要对请求进行检查</strong>，其中就包括 <a href="https://kubernetes.io/docs/admin/admission-controllers/#what-are-they">admission controllers</a>。<br>
<br>与鉴权的区别：<br>
<ul><li>鉴权（authorization）在前面，关注的是<strong>用户是否有操作权限</strong>，</li><li>Admission controllers 在更后面，<strong>对请求进行拦截和过滤，确保它们符合一些更广泛的集群规则和限制</strong>， 是<strong>将请求对象持久化到 etcd 之前的最后堡垒</strong>。</li></ul><br>
<br>工作方式：<br>
<ul><li>与认证和鉴权类似，也是遍历一个列表，</li><li>但有一点核心区别：<strong>任何一个 controller 检查没通过，请求就会失败</strong>。</li></ul><br>
<br>设计：可扩展<br>
<ul><li>每个 controller 作为一个 plugin 存放在 <a href="https://github.com/kubernetes/kubernetes/tree/master/plugin/pkg/admission"><code class="prettyprint">plugin/pkg/admission</code> 目录</a></li><li>设计时已经考虑，只需要实现很少的几个接口</li><li>但注意，<strong>admission controller 最终会编译到 Kubernetes 的二进制文件</strong>（而非独立的 plugin binary）</li></ul><br>
<br>类型：<br>
<br>Admission controllers 通常按不同目的分类，包括：<strong>资源管理、安全管理、默认值管 理、引用一致性</strong>（referential consistency）等类型。<br>
<br>例如，下面是资源管理类的几个 controller：<br>
<ul><li><code class="prettyprint">InitialResources</code>：为容器设置默认的资源限制（基于过去的使用量）；</li><li><code class="prettyprint">LimitRanger</code>：为容器的 requests and limits 设置默认值，或对特定资源设置上限（例如，内存默认 512MB，最高不超过 2GB）。</li><li><code class="prettyprint">ResourceQuota</code>：资源配额。</li></ul><br>
<br><h3>写入 etcd</h3>至此，Kubernetes 已经完成对请求的验证，允许它进行接下来的处理。<br>
<br>kube-apiserver 将<strong>对请求进行反序列化，构造 runtime objects</strong>（ kubectl generator 的反过程），并将它们<strong>持久化到 etcd</strong>。下面详细看这个过程。<br>
<br><h3>调用栈概览</h3>对于本文创建 Pod 的请求，相应的入口是 <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/apiserver/pkg/endpoints/installer.go#L815">POST handler</a>  ，它又会进一步将请求委托给一个创建具体资源的 handler。<br>
<pre class="prettyprint">registerResourceHandlers // staging/src/k8s.io/apiserver/pkg/endpoints/installer.go<br>
|-case POST:<br>
<br>
```<br>
<br>
```<br>
// staging/src/k8s.io/apiserver/pkg/endpoints/installer.go<br>
<br>
    switch () &#123;<br>
    case "POST": // Create a resource.<br>
        var handler restful.RouteFunction<br>
        if isNamedCreater &#123;<br>
            handler = restfulCreateNamedResource(namedCreater, reqScope, admit)<br>
        &#125; else &#123;<br>
            handler = restfulCreateResource(creater, reqScope, admit)<br>
        &#125;<br>
<br>
        handler = metrics.InstrumentRouteFunc(action.Verb, group, version, resource, subresource, .., handler)<br>
        article := GetArticleForNoun(kind, " ")<br>
        doc := "create" + article + kind<br>
        if isSubresource &#123;<br>
            doc = "create " + subresource + " of" + article + kind<br>
        &#125;<br>
<br>
        route := ws.POST(action.Path).To(handler).<br>
            Doc(doc).<br>
            Operation("create"+namespaced+kind+strings.Title(subresource)+operationSuffix).<br>
            Produces(append(storageMeta.ProducesMIMETypes(action.Verb), mediaTypes...)...).<br>
            Returns(http.StatusOK, "OK", producedObject).<br>
            Returns(http.StatusCreated, "Created", producedObject).<br>
            Returns(http.StatusAccepted, "Accepted", producedObject).<br>
            Reads(defaultVersionedObject).<br>
            Writes(producedObject)<br>
<br>
        AddObjectParams(ws, route, versionedCreateOptions)<br>
        addParams(route, action.Params)<br>
        routes = append(routes, route)<br>
    &#125;<br>
<br>
    for route := range routes &#123;<br>
        route.Metadata(ROUTE_META_GVK, metav1.GroupVersionKind&#123;<br>
            Group:   reqScope.Kind.Group,<br>
            Version: reqScope.Kind.Version,<br>
            Kind:    reqScope.Kind.Kind,<br>
        &#125;)<br>
        route.Metadata(ROUTE_META_ACTION, strings.ToLower(action.Verb))<br>
        ws.Route(route)<br>
    &#125; <br>
</pre><br>
<h4>kube-apiserver 请求处理过程</h4>从 apiserver 的请求处理函数开始：<br>
<pre class="prettyprint">// staging/src/k8s.io/apiserver/pkg/server/handler.go<br>
<br>
func (d director) ServeHTTP(w http.ResponseWriter, req *http.Request) &#123;<br>
path := req.URL.Path<br>
<br>
// check to see if our webservices want to claim this path<br>
for _, ws := range d.goRestfulContainer.RegisteredWebServices() &#123;<br>
    switch &#123;<br>
    case ws.RootPath() == "/apis":<br>
        if path == "/apis" || path == "/apis/" &#123;<br>
            return d.goRestfulContainer.Dispatch(w, req)<br>
        &#125;<br>
<br>
    case strings.HasPrefix(path, ws.RootPath()):<br>
        if len(path) == len(ws.RootPath()) || path[len(ws.RootPath())] == '/' &#123;<br>
            return d.goRestfulContainer.Dispatch(w, req)<br>
        &#125;<br>
    &#125;<br>
&#125;<br>
<br>
// if we didn't find a match, then we just skip gorestful altogether<br>
d.nonGoRestfulMux.ServeHTTP(w, req)<br>
&#125; <br>
</pre><br>
如果能匹配到请求（例如匹配到前面注册的路由），它将  <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/apiserver/pkg/server/handler.go#L136">分派给相应的 handler</a>；否则，fall back 到 <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/apiserver/pkg/server/mux/pathrecorder.go#L146">path-based handler</a>（<code class="prettyprint">GET /apis</code> 到达的就是这里）；<br>
<br>基于 path 的 handlers：<br>
<pre class="prettyprint">// staging/src/k8s.io/apiserver/pkg/server/mux/pathrecorder.go<br>
<br>
func (h *pathHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) &#123;<br>
if exactHandler, ok := h.pathToHandler[r.URL.Path]; ok &#123;<br>
    return exactHandler.ServeHTTP(w, r)<br>
&#125;<br>
<br>
for prefixHandler := range h.prefixHandlers &#123;<br>
    if strings.HasPrefix(r.URL.Path, prefixHandler.prefix) &#123;<br>
        return prefixHandler.handler.ServeHTTP(w, r)<br>
    &#125;<br>
&#125;<br>
<br>
h.notFoundHandler.ServeHTTP(w, r)<br>
&#125; <br>
</pre><br>
如果还是没有找到路由，就会 fallback 到 non-gorestful handler，最终可能是一个 not found handler。<br>
<br>对于我们的场景，会匹配到一条已经注册的、名为 <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/apiserver/pkg/endpoints/handlers/create.go#L37"><code class="prettyprint">createHandler</code></a> 为的路由。<br>
<h4>Create handler 处理过程</h4><pre class="prettyprint">// staging/src/k8s.io/apiserver/pkg/endpoints/handlers/create.go<br>
<br>
func createHandler(r rest.NamedCreater, scope *RequestScope, admit Interface, includeName bool) http.HandlerFunc &#123;<br>
return func(w http.ResponseWriter, req *http.Request) &#123;<br>
    namespace, name := scope.Namer.Name(req) // 获取资源的 namespace 和 name（etcd item key）<br>
    s := negotiation.NegotiateInputSerializer(req, false, scope.Serializer)<br>
<br>
    body := limitedReadBody(req, scope.MaxRequestBodyBytes)<br>
    obj, gvk := decoder.Decode(body, &defaultGVK, original)<br>
<br>
    admit = admission.WithAudit(admit, ae)<br>
<br>
    requestFunc := func() (runtime.Object, error) &#123;<br>
        return r.Create(<br>
            name,<br>
            obj,<br>
            rest.AdmissionToValidateObjectFunc(admit, admissionAttributes, scope),<br>
        )<br>
    &#125;<br>
<br>
    result := finishRequest(ctx, func() (runtime.Object, error) &#123;<br>
        if scope.FieldManager != nil &#123;<br>
            liveObj := scope.Creater.New(scope.Kind)<br>
            obj = scope.FieldManager.UpdateNoErrors(liveObj, obj, managerOrUserAgent(options.FieldManager, req.UserAgent()))<br>
            admit = fieldmanager.NewManagedFieldsValidatingAdmissionController(admit)<br>
        &#125;<br>
<br>
        admit.(admission.MutationInterface)<br>
        mutatingAdmission.Handles(admission.Create)<br>
        mutatingAdmission.Admit(ctx, admissionAttributes, scope)<br>
<br>
        return requestFunc()<br>
    &#125;)<br>
<br>
    code := http.StatusCreated<br>
    status, ok := result.(*metav1.Status)<br>
    transformResponseObject(ctx, scope, trace, req, w, code, outputMediaType, result)<br>
&#125;<br>
&#125; <br>
</pre><br>
<ol><li>首先解析 HTTP request，然后执行基本的验证，例如保证 JSON 与 versioned API resource 期望的是一致的；</li><li>执行审计和最终 admission；</li><li><br>将资源最终<a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/apiserver/pkg/endpoints/handlers/create.go#L401">写到 etcd</a>，这会进一步调用到  <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/apiserver/pkg/registry/generic/registry/store.go#L362">storage provider</a>。<br>
<br><strong>etcd key 的格式一般是</strong>：<code class="prettyprint">&lt;namespace>/&lt;name></code>（例如：<code class="prettyprint">default/nginx-0</code>），但这个也是可配置的。</li><li><br>最后，storage provider 执行一次 <code class="prettyprint">get</code> 操作，确保对象真的创建成功了。如果有额外的收尾任务（additional finalization），会执行 post-create handlers 和 decorators。</li><li>返回 <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/staging/src/k8s.io/apiserver/pkg/endpoints/handlers/create.go#L131-L142">生成的</a> HTTP response。</li></ol><br>
<br>以上过程可以看出，apiserver 做了大量的事情。<br>
<br>总结：至此我们的 Pod 资源已经在 etcd 中了。但是，此时 <code class="prettyprint">kubectl get pods -n &lt;ns></code> 还看不见它。<br>
<h3>Initializers</h3><strong>对象持久化到 etcd 之后，apiserver 并未将其置位对外可见，它也不会立即就被调度</strong>，而是要先等一些 <a href="https://kubernetes.io/docs/admin/extensible-admission-controllers/#initializers">initializers</a> 运行完成。<br>
<h4>Initializer</h4>Initializer 是<strong>与特定资源类型（resource type）相关的 controller</strong>。<br>
<ul><li>负责<strong>在该资源对外可见之前对它们执行一些处理</strong></li><li>如果一种资源类型没有注册任何 initializer，这个步骤就会跳过，<strong>资源对外立即可见</strong>。</li></ul><br>
<br>这是一种非常强大的特性，使得我们能<strong>执行一些通用的启动初始化（bootstrap）操作</strong>。例如：<br>
<ul><li>向 Pod 注入 sidecar、暴露 80 端口，或打上特定的 annotation。</li><li>向某个 namespace 内的所有 Pod 注入一个存放了测试证书（test certificates）的 volume。</li><li>禁止创建长度小于 20 个字符的 Secret （例如密码）。</li></ul><br>
<br><h4>InitializerConfiguration</h4>可以用 <code class="prettyprint">InitializerConfiguration</code> <strong>声明对哪些资源类型（resource type）执行哪些 initializer</strong>。<br>
<br>例如，要实现所有 Pod 创建时都运行一个自定义的 initializer <code class="prettyprint">custom-pod-initializer</code>，可以用下面的 yaml：<br>
<pre class="prettyprint">apiVersion: admissionregistration.k8s.io/v1alpha1<br>
kind: InitializerConfiguration<br>
metadata:<br>
name: custom-pod-initializer<br>
initializers:<br>
- name: podimage.example.com<br>
rules:<br>
  - apiGroups:<br>
      - ""<br>
    apiVersions:<br>
      - v1<br>
    resources:<br>
      - pods<br>
</pre><br>
创建以上配置（<code class="prettyprint">kubectl create -f xx.yaml</code>）之后，Kubernetes 会将  <code class="prettyprint">custom-pod-initializer</code> 追加到每个 Pod 的 <code class="prettyprint">metadata.initializers.pending</code> 字段。<br>
<br>在此之前需要<strong>启动 initializer controller</strong>，它会：<br>
<ul><li>定期扫描是否有新 Pod 创建；</li><li>当<strong>检测到它的名字出现在 Pod 的 pending 字段</strong>时，就会执行它的处理逻辑；</li><li>执行完成之后，它会将自己的名字从 pending list 中移除。</li></ul><br>
<br>pending list 中的 initializers，每次只有第一个 initializer 能执行。 当所有 initializer 执行完成，<code class="prettyprint">pending</code>  字段为空之后，就认为  <strong>这个对象已经完成初始化了</strong>（considered initialized）。<br>
<br>细心的同学可能会有疑问：<strong>前面说这个对象还没有对外可见，那用户空间的 initializer controller 又是如何能检测并操作这个对象的呢？</strong>答案是： kube-apiserver 提供了一个  <code class="prettyprint">?includeUninitialized</code>  查询参数，它会返回所有对象， 包括那些还未完成初始化的（uninitialized ones）。<br>
<h3>Control loops（控制循环）</h3>至此，对象已经在 etcd 中了，所有的初始化步骤也已经完成了。 下一步是设置资源拓扑（resource topology）。例如，一个 Deployment 其实就是一组 ReplicaSet，而一个 ReplicaSet 就是一组 Pod。 K8s 是如何根据一个 HTTP 请求创建出这个层级关系的呢？靠的是  <strong>Kubernetes 内置的控制器</strong>（controllers）。<br>
<br>Kubernetes 中大量使用 “controllers”：<br>
<ul><li>一个 controller 就是一个<strong>异步脚本</strong>（an asynchronous script），</li><li>不断检查资源的<strong>当前状态</strong>（current state）和<strong>期望状态</strong>（desired state）是否一致，</li><li>如果不一致就尝试将其变成期望状态，这个过程称为  <strong>reconcile</strong>。</li></ul><br>
<br>每个 controller 负责的东西都比较少，<strong>所有 controller 并行运行， 由 kube-controller-manager 统一管理</strong>。<br>
<br><h4>Deployments controller</h4><strong>Deployments controller 启动</strong><br>
<br>当一个 Deployment record 存储到 etcd 并（被 initializers）初始化之后， kube-apiserver 就会将其置为对外可见的。此后， Deployment controller 监听了 Deployment 资源的变动，因此此时就会检测到这个新创建的资源。<br>
<pre class="prettyprint">// pkg/controller/deployment/deployment_controller.go<br>
<br>
// NewDeploymentController creates a new DeploymentController.<br>
func NewDeploymentController(dInformer DeploymentInformer, rsInformer ReplicaSetInformer,<br>
podInformer PodInformer, client clientset.Interface) (*DeploymentController, error) &#123;<br>
<br>
dc := &DeploymentController&#123;<br>
    client:        client,<br>
    queue:         workqueue.NewNamedRateLimitingQueue(),<br>
&#125;<br>
dc.rsControl = controller.RealRSControl&#123; // ReplicaSet controller<br>
    KubeClient: client,<br>
    Recorder:   dc.eventRecorder,<br>
&#125;<br>
<br>
// 注册 Deployment 事件回调函数<br>
dInformer.Informer().AddEventHandler(cache.ResourceEventHandlerFuncs&#123;<br>
    AddFunc:    dc.addDeployment,    // 有 Deployment 创建时触发<br>
    UpdateFunc: dc.updateDeployment,<br>
    DeleteFunc: dc.deleteDeployment,<br>
&#125;)<br>
// 注册 ReplicaSet 事件回调函数<br>
rsInformer.Informer().AddEventHandler(cache.ResourceEventHandlerFuncs&#123;<br>
    AddFunc:    dc.addReplicaSet,<br>
    UpdateFunc: dc.updateReplicaSet,<br>
    DeleteFunc: dc.deleteReplicaSet,<br>
&#125;)<br>
// 注册 Pod 事件回调函数<br>
podInformer.Informer().AddEventHandler(cache.ResourceEventHandlerFuncs&#123;<br>
    DeleteFunc: dc.deletePod,<br>
&#125;)<br>
<br>
dc.syncHandler = dc.syncDeployment<br>
dc.enqueueDeployment = dc.enqueue<br>
<br>
return dc, nil<br>
&#125; <br>
</pre><br>
<strong>创建 Deployment：回调函数处理</strong><br>
<br>在本文场景中，触发的是 controller <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/pkg/controller/deployment/deployment_controller.go#L122">注册的 addDeployment() 回调函数</a> 其所做的工作就是将 deployment 对象放到一个内部队列：<br>
<pre class="prettyprint">// pkg/controller/deployment/deployment_controller.go<br>
<br>
func (dc *DeploymentController) addDeployment(obj interface&#123;&#125;) &#123;<br>
d := obj.(*apps.Deployment)<br>
dc.enqueueDeployment(d)<br>
&#125; <br>
</pre><br>
<strong>主处理循环</strong><br>
<br>worker 不断遍历这个 queue，从中 dequeue item 并进行处理：<br>
<pre class="prettyprint">// pkg/controller/deployment/deployment_controller.go<br>
<br>
func (dc *DeploymentController) worker() &#123;<br>
for dc.processNextWorkItem() &#123;<br>
&#125;<br>
&#125;<br>
<br>
func (dc *DeploymentController) processNextWorkItem() bool &#123;<br>
key, quit := dc.queue.Get()<br>
dc.syncHandler(key.(string)) // dc.syncHandler = dc.syncDeployment<br>
&#125;<br>
<br>
// syncDeployment will sync the deployment with the given key.<br>
func (dc *DeploymentController) syncDeployment(key string) error &#123;<br>
namespace, name := cache.SplitMetaNamespaceKey(key)<br>
<br>
deployment := dc.dLister.Deployments(namespace).Get(name)<br>
d := deployment.DeepCopy()<br>
<br>
// 获取这个 Deployment 的所有 ReplicaSets, while reconciling ControllerRef through adoption/orphaning.<br>
rsList := dc.getReplicaSetsForDeployment(d)<br>
<br>
// 获取这个 Deployment 的所有 pods, grouped by their ReplicaSet<br>
podMap := dc.getPodMapForDeployment(d, rsList)<br>
<br>
if d.DeletionTimestamp != nil &#123; // 这个 Deployment 已经被标记，等待被删除<br>
    return dc.syncStatusOnly(d, rsList)<br>
&#125;<br>
<br>
dc.checkPausedConditions(d)<br>
if d.Spec.Paused &#123; // pause 状态<br>
    return dc.sync(d, rsList)<br>
&#125;<br>
<br>
if getRollbackTo(d) != nil &#123;<br>
    return dc.rollback(d, rsList)<br>
&#125;<br>
<br>
scalingEvent := dc.isScalingEvent(d, rsList)<br>
if scalingEvent &#123;<br>
    return dc.sync(d, rsList)<br>
&#125;<br>
<br>
switch d.Spec.Strategy.Type &#123;<br>
case RecreateDeploymentStrategyType:             // re-create<br>
    return dc.rolloutRecreate(d, rsList, podMap)<br>
case RollingUpdateDeploymentStrategyType:        // rolling-update<br>
    return dc.rolloutRolling(d, rsList)<br>
&#125;<br>
return fmt.Errorf("unexpected deployment strategy type: %s", d.Spec.Strategy.Type)<br>
&#125; <br>
</pre><br>
controller 会通过 label selector 从 kube-apiserver 查询 与这个 deployment 关联的 ReplicaSet 或 Pod records（然后发现没有）。<br>
<br>如果发现当前状态与预期状态不一致，就会触发同步过程（synchronization process）。 这个同步过程是无状态的，也就是说，它并不区分是新记录还是老记录，一视同仁。<br>
<br><strong>执行扩容（scale up）</strong><br>
<br>如上，发现 Pod 不存在之后，它会开始扩容过程（scaling process）：<br>
<pre class="prettyprint">// pkg/controller/deployment/sync.go<br>
<br>
// scale up/down 或新创建（pause）时都会执行到这里<br>
func (dc *DeploymentController) sync(d *apps.Deployment, rsList []*apps.ReplicaSet) error &#123;<br>
<br>
newRS, oldRSs := dc.getAllReplicaSetsAndSyncRevision(d, rsList, false)<br>
dc.scale(d, newRS, oldRSs)<br>
<br>
// Clean up the deployment when it's paused and no rollback is in flight.<br>
if d.Spec.Paused && getRollbackTo(d) == nil &#123;<br>
    dc.cleanupDeployment(oldRSs, d)<br>
&#125;<br>
<br>
allRSs := append(oldRSs, newRS)<br>
return dc.syncDeploymentStatus(allRSs, newRS, d)<br>
&#125; <br>
</pre><br>
大致步骤：<br>
<ol><li>Rolling out (例如 creating）一个 ReplicaSet resource</li><li>分配一个 label selector</li><li>初始版本好（revision number）置为 1</li></ol><br>
<br>ReplicaSet 的 PodSpec，以及其他一些 metadata 是从 Deployment 的 manifest 拷过来的。<br>
<br>最后会更新 deployment 状态，然后重新进入 reconciliation 循环，直到 deployment 进入预期的状态。<br>
<br><strong>小结</strong><br>
<br>由于  <strong>Deployment controller 只负责 ReplicaSet 的创建</strong>，因此下一步 （ReplicaSet -> Pod）要由 reconciliation 过程中的另一个 controller —— ReplicaSet controller 来完成。<br>
<h4>ReplicaSets controller</h4>上一步周，Deployments controller 已经创建了 Deployment 的第一个 ReplicaSet，但此时还没有任何 Pod。 下面就轮到 ReplicaSet controller 出场了。 它的任务是监控 ReplicaSet 及其依赖资源（Pods）的生命周期，实现方式也是注册事件回调函数。<br>
<br><strong>ReplicaSets controller 启动</strong><br>
<pre class="prettyprint">// pkg/controller/replicaset/replica_set.go<br>
<br>
func NewReplicaSetController(rsInformer ReplicaSetInformer, podInformer PodInformer,<br>
kubeClient clientset.Interface, burstReplicas int) *ReplicaSetController &#123;<br>
<br>
return NewBaseController(rsInformer, podInformer, kubeClient, burstReplicas,<br>
    apps.SchemeGroupVersion.WithKind("ReplicaSet"),<br>
    "replicaset_controller",<br>
    "replicaset",<br>
    controller.RealPodControl&#123;<br>
        KubeClient: kubeClient,<br>
    &#125;,<br>
)<br>
&#125;<br>
<br>
// 抽象出 NewBaseController() 是为了代码复用，例如 NewReplicationController() 也会调用这个函数。<br>
func NewBaseController(rsInformer, podInformer, kubeClient clientset.Interface, burstReplicas int,<br>
gvk GroupVersionKind, metricOwnerName, queueName, podControl PodControlInterface) *ReplicaSetController &#123;<br>
<br>
rsc := &ReplicaSetController&#123;<br>
    kubeClient:       kubeClient,<br>
    podControl:       podControl,<br>
    burstReplicas:    burstReplicas,<br>
    expectations:     controller.NewUIDTrackingControllerExpectations(NewControllerExpectations()),<br>
    queue:            workqueue.NewNamedRateLimitingQueue()<br>
&#125;<br>
<br>
rsInformer.Informer().AddEventHandler(cache.ResourceEventHandlerFuncs&#123;<br>
    AddFunc:    rsc.addRS,<br>
    UpdateFunc: rsc.updateRS,<br>
    DeleteFunc: rsc.deleteRS,<br>
&#125;)<br>
rsc.rsLister = rsInformer.Lister()<br>
<br>
podInformer.Informer().AddEventHandler(cache.ResourceEventHandlerFuncs&#123;<br>
    AddFunc: rsc.addPod,<br>
    UpdateFunc: rsc.updatePod,<br>
    DeleteFunc: rsc.deletePod,<br>
&#125;)<br>
rsc.podLister = podInformer.Lister()<br>
<br>
rsc.syncHandler = rsc.syncReplicaSet<br>
return rsc<br>
&#125; <br>
</pre><br>
<strong>创建 ReplicaSet：回调函数处理</strong><br>
<br><strong>主处理循环</strong><br>
<br>当一个 ReplicaSet 被（Deployment controller）创建之后。<br>
<pre class="prettyprint">// pkg/controller/replicaset/replica_set.go<br>
<br>
// syncReplicaSet will sync the ReplicaSet with the given key if it has had its expectations fulfilled,<br>
// meaning it did not expect to see any more of its pods created or deleted.<br>
func (rsc *ReplicaSetController) syncReplicaSet(key string) error &#123;<br>
<br>
namespace, name := cache.SplitMetaNamespaceKey(key)<br>
rs := rsc.rsLister.ReplicaSets(namespace).Get(name)<br>
<br>
selector := metav1.LabelSelectorAsSelector(rs.Spec.Selector)<br>
<br>
// 包括那些不匹配 rs selector，但有 stale controller ref 的 pod<br>
allPods := rsc.podLister.Pods(rs.Namespace).List(labels.Everything())<br>
filteredPods := controller.FilterActivePods(allPods) // Ignore inactive pods.<br>
filteredPods = rsc.claimPods(rs, selector, filteredPods)<br>
<br>
if rsNeedsSync && rs.DeletionTimestamp == nil &#123; // 需要同步，并且没有被标记待删除<br>
    rsc.manageReplicas(filteredPods, rs)        // *主处理逻辑*<br>
&#125;<br>
<br>
newStatus := calculateStatus(rs, filteredPods, manageReplicasErr)<br>
updatedRS := updateReplicaSetStatus(AppsV1().ReplicaSets(rs.Namespace), rs, newStatus)<br>
&#125; <br>
</pre><br>
RS controller 检查 ReplicaSet 的状态， 发现当前状态和期望状态之间有偏差（skew），因此接下来调用 <code class="prettyprint">manageReplicas()</code> 来 reconcile 这个状态，在这里做的事情就是增加这个 ReplicaSet 的 Pod 数量。<br>
<pre class="prettyprint">// pkg/controller/replicaset/replica_set.go<br>
<br>
func (rsc *ReplicaSetController) manageReplicas(filteredPods []*v1.Pod, rs *apps.ReplicaSet) error &#123;<br>
diff := len(filteredPods) - int(*(rs.Spec.Replicas))<br>
rsKey := controller.KeyFunc(rs)<br>
<br>
if diff < 0 &#123;<br>
    diff *= -1<br>
    if diff > rsc.burstReplicas &#123;<br>
        diff = rsc.burstReplicas<br>
    &#125;<br>
<br>
    rsc.expectations.ExpectCreations(rsKey, diff)<br>
    successfulCreations := slowStartBatch(diff, controller.SlowStartInitialBatchSize, func() &#123;<br>
        return rsc.podControl.CreatePodsWithControllerRef( // 扩容<br>
            // 调用栈 CreatePodsWithControllerRef -> createPod() -> Client.CoreV1().Pods().Create()<br>
            rs.Namespace, &rs.Spec.Template, rs, metav1.NewControllerRef(rs, rsc.GroupVersionKind))<br>
    &#125;)<br>
<br>
    // The skipped pods will be retried later. The next controller resync will retry the slow start process.<br>
    if skippedPods := diff - successfulCreations; skippedPods > 0 &#123;<br>
        for i := 0; i < skippedPods; i++ &#123;<br>
            // Decrement the expected number of creates because the informer won't observe this pod<br>
            rsc.expectations.CreationObserved(rsKey)<br>
        &#125;<br>
    &#125;<br>
    return err<br>
&#125; else if diff > 0 &#123;<br>
    if diff > rsc.burstReplicas &#123;<br>
        diff = rsc.burstReplicas<br>
    &#125;<br>
<br>
    relatedPods := rsc.getIndirectlyRelatedPods(rs)<br>
    podsToDelete := getPodsToDelete(filteredPods, relatedPods, diff)<br>
    rsc.expectations.ExpectDeletions(rsKey, getPodKeys(podsToDelete))<br>
<br>
    for _, pod := range podsToDelete &#123;<br>
        go func(targetPod *v1.Pod) &#123;<br>
            rsc.podControl.DeletePod(rs.Namespace, targetPod.Name, rs) // 缩容<br>
        &#125;(pod)<br>
    &#125;<br>
&#125;<br>
<br>
return nil<br>
&#125; <br>
</pre><br>
增加 Pod 数量的操作比较小心，每次最多不超过 burst count（这个配置是从 ReplicaSet 的父对象 Deployment 那里继承来的）。<br>
<br>另外，创建 Pods 的过程是 <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/pkg/controller/replicaset/replica_set.go#L487">批处理的</a>, “慢启动”操，开始时是  <code class="prettyprint">SlowStartInitialBatchSize</code>，每执行成功一批，下次的 batch size 就翻倍。 这样设计是为了避免给 kube-apiserver 造成不必要的压力，例如，如果由于 quota 不足，这批 pod 大部分都会失败，那 这种方式只会有一小批请求到达 kube-apiserver，而如果一把全上的话，请求全部会打过去。 同样是失败，这种失败方式比较优雅。<br>
<br><strong>Owner reference</strong><br>
<br>Kubernetes <strong>通过 Owner Reference</strong>（子资源中的一个字段，指向的是其父资源的 ID）<strong>维护对象层级</strong>（hierarchy）。这可以带来两方面好处：<br>
<ol><li>实现了 cascading deletion，即父对象被 GC 时会确保 GC 子对象；</li><li>父对象之间不会出现竞争子对象的情况（例如，两个父对象认为某个子对象都是自己的）</li></ol><br>
<br>另一个隐藏的好处是：Owner Reference 是有状态的：如果 controller 重启，重启期间不会影响 系统的其他部分，因为资源拓扑（resource topology）是独立于 controller 的。 这种隔离设计也体现在 controller 自己的设计中：<strong>controller 不应该操作 其他 controller 的资源</strong>（resources they don’t explicitly own）。<br>
<br>有时也可能会出现“孤儿”资源（“orphaned” resources）的情况，例如：<br>
<ol><li>父资源删除了，子资源还在；</li><li>GC 策略导致子资源无法被删除。</li></ol><br>
<br>这种情况发生时，<strong>controller 会确保孤儿资源会被某个新的父资源收养</strong>。 多个父资源都可以竞争成为孤儿资源的父资源，但只有一个会成功（其余的会收到一个 validation 错误）。<br>
<h4>Informers</h4>很多 controller（例如 RBAC authorizer 或 Deployment controller）需要将集群信息拉到本地。<br>
<br>例如 RBAC authorizer 中，authenticator 会将用户信息保存到请求上下文中。随后， RBAC authorizer 会用这个信息获取 etcd 中所有与这个用户相关的 role 和 role bindings。<br>
<br>那么，controller 是如何访问和修改这些资源的？在 Kubernetes 中，这是通过 informer 机制实现的。<br>
<br><strong>informer 是一种 controller 订阅存储（etcd）事件的机制</strong>，能方便地获取它们感兴趣的资源。<br>
<ul><li>这种方式除了提供一种很好的抽象之外，还负责处理缓存（caching，非常重要，因为可 以减少 kube-apiserver 连接数，降低 controller 测和 kube-apiserver 侧的序列化 成本）问题。</li><li>此外，这种设计还使得 controller 的行为是 threadsafe 的，避免影响其他组件或服务。</li></ul><br>
<br>关于 informer 和 controller 的联合工作机制，可参考 <a href="http://borismattijssen.github.io/articles/kubernetes-informers-controllers-reflectors-stores">这篇博客</a>。<br>
<h4>Scheduler（调度器）</h4>以上 controllers 执行完各自的处理之后，etcd 中已经有了一个 Deployment、一个 ReplicaSet 和三个 Pods，可以通过 kube-apiserver 查询到。 但此时，<strong>这三个 Pod 还卡在 Pending 状态，因为它们还没有被调度到任何节点</strong>。<strong>另外一个 controller —— 调度器</strong>  —— 负责做这件事情。<br>
<br>scheduler 作为控制平面的一个独立服务运行，但<strong>工作方式与其他 controller 是一样的</strong>： 监听事件，然后尝试 reconcile 状态。<br>
<br><strong>调用栈概览</strong><br>
<pre class="prettyprint">Run // pkg/scheduler/scheduler.go <br>
|-SchedulingQueue.Run()<br>
|<br>
|-scheduleOne()<br>
 |-bind<br>
 |  |-RunBindPlugins<br>
 |     |-runBindPlugins<br>
 |        |-Bind<br>
 |-sched.Algorithm.Schedule(pod)<br>
    |-findNodesThatFitPod<br>
    |-prioritizeNodes<br>
    |-selectHost<br>
</pre><br>
<strong>调度过程</strong><br>
<pre class="prettyprint">// pkg/scheduler/core/generic_scheduler.go<br>
<br>
// 将 Pod 调度到指定 node list 中的某台 Node 上<br>
func (g *genericScheduler) Schedule(ctx context.Context, fwk framework.Framework,<br>
state *framework.CycleState, pod *v1.Pod) (result ScheduleResult, err error) &#123;<br>
<br>
feasibleNodes, diagnosis := g.findNodesThatFitPod(ctx, fwk, state, pod) // 过滤可用 nodes<br>
if len(feasibleNodes) == 0 &#123;<br>
    return result, &framework.FitError&#123;&#125;<br>
&#125;<br>
<br>
if len(feasibleNodes) == 1 &#123; // 可用 node 只有一个，就选它了<br>
    return ScheduleResult&#123;SuggestedHost:  feasibleNodes[0].Name&#125;, nil<br>
&#125;<br>
<br>
priorityList := g.prioritizeNodes(ctx, fwk, state, pod, feasibleNodes)<br>
host := g.selectHost(priorityList)<br>
<br>
return ScheduleResult&#123;<br>
    SuggestedHost:  host,<br>
    EvaluatedNodes: len(feasibleNodes) + len(diagnosis.NodeToStatusMap),<br>
    FeasibleNodes:  len(feasibleNodes),<br>
&#125;, err<br>
&#125;<br>
<br>
// Filters nodes that fit the pod based on the framework filter plugins and filter extenders.<br>
func (g *genericScheduler) findNodesThatFitPod(ctx context.Context, fwk framework.Framework,<br>
state *framework.CycleState, pod *v1.Pod) ([]*v1.Node, framework.Diagnosis, error) &#123;<br>
<br>
diagnosis := framework.Diagnosis&#123;<br>
    NodeToStatusMap:      make(framework.NodeToStatusMap),<br>
    UnschedulablePlugins: sets.NewString(),<br>
&#125;<br>
<br>
// Run "prefilter" plugins.<br>
s := fwk.RunPreFilterPlugins(ctx, state, pod)<br>
allNodes := g.nodeInfoSnapshot.NodeInfos().List()<br>
<br>
if len(pod.Status.NominatedNodeName) > 0 && featureGate.Enabled(features.PreferNominatedNode) &#123;<br>
    feasibleNodes := g.evaluateNominatedNode(ctx, pod, fwk, state, diagnosis)<br>
    if len(feasibleNodes) != 0 &#123;<br>
        return feasibleNodes, diagnosis, nil<br>
    &#125;<br>
&#125;<br>
<br>
feasibleNodes := g.findNodesThatPassFilters(ctx, fwk, state, pod, diagnosis, allNodes)<br>
feasibleNodes = g.findNodesThatPassExtenders(pod, feasibleNodes, diagnosis.NodeToStatusMap)<br>
return feasibleNodes, diagnosis, nil<br>
&#125; <br>
</pre><br>
它会过滤 <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/plugin/pkg/scheduler/factory/factory.go#L190">过滤 PodSpect 中 NodeName 字段为空的 Pods</a>，尝试为这样的 Pods 挑选一个 Node 调度上去。<br>
<br><strong>调度算法</strong><br>
<br>下面简单看下内置的默认调度算法。<br>
<br><strong><em>注册默认 predicates</em></strong><br>
<br>这些 predicates 其实都是函数，被调用到时，执行相应的 <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/plugin/pkg/scheduler/core/generic_scheduler.go#L117">过滤</a>。例如，<strong>如果 PodSpec 里面显式要求了 CPU 或 RAM 资源，而一个 node 无法满足这些条件</strong>， 那就会将这个 Node 从备选列表中删除。<br>
<pre class="prettyprint">// pkg/scheduler/algorithmprovider/registry.go<br>
<br>
// NewRegistry returns an algorithm provider registry instance.<br>
func NewRegistry() Registry &#123;<br>
defaultConfig := getDefaultConfig()<br>
applyFeatureGates(defaultConfig)<br>
<br>
caConfig := getClusterAutoscalerConfig()<br>
applyFeatureGates(caConfig)<br>
<br>
return Registry&#123;<br>
    schedulerapi.SchedulerDefaultProviderName: defaultConfig,<br>
    ClusterAutoscalerProvider:                 caConfig,<br>
&#125;<br>
&#125;<br>
<br>
func getDefaultConfig() *schedulerapi.Plugins &#123;<br>
plugins := &schedulerapi.Plugins&#123;<br>
    PreFilter: schedulerapi.PluginSet&#123;...&#125;,<br>
    Filter: schedulerapi.PluginSet&#123;<br>
        Enabled: []schedulerapi.Plugin&#123;<br>
            &#123;Name: nodename.Name&#125;,        // 指定 node name 调度<br>
            &#123;Name: tainttoleration.Name&#125;, // 指定 toleration 调度<br>
            &#123;Name: nodeaffinity.Name&#125;,    // 指定 node affinity 调度<br>
            ...<br>
        &#125;,<br>
    &#125;,<br>
    PostFilter: schedulerapi.PluginSet&#123;...&#125;,<br>
    PreScore: schedulerapi.PluginSet&#123;...&#125;,<br>
    Score: schedulerapi.PluginSet&#123;<br>
        Enabled: []schedulerapi.Plugin&#123;<br>
            &#123;Name: interpodaffinity.Name, Weight: 1&#125;,<br>
            &#123;Name: nodeaffinity.Name, Weight: 1&#125;,<br>
            &#123;Name: tainttoleration.Name, Weight: 1&#125;,<br>
            ...<br>
        &#125;,<br>
    &#125;,<br>
    Reserve: schedulerapi.PluginSet&#123;...&#125;,<br>
    PreBind: schedulerapi.PluginSet&#123;...&#125;,<br>
    Bind: schedulerapi.PluginSet&#123;...&#125;,<br>
&#125;<br>
<br>
return plugins<br>
&#125; <br>
</pre><br>
plugin 的实现见：<code class="prettyprint">pkg/scheduler/framework/plugins/</code>，以 <code class="prettyprint">nodename</code>  filter 为例：<br>
<pre class="prettyprint">// pkg/scheduler/framework/plugins/nodename/node_name.go<br>
<br>
// Filter invoked at the filter extension point.<br>
func (pl *NodeName) Filter(ctx context.Context, pod *v1.Pod, nodeInfo *framework.NodeInfo) *framework.Status &#123;<br>
if !Fits(pod, nodeInfo) &#123;<br>
    return framework.NewStatus(UnschedulableAndUnresolvable, ErrReason)<br>
&#125;<br>
return nil<br>
&#125;<br>
<br>
// 如果 Pod 没有指定 NodeName，或者指定的 NodeName 等于该 Node 的 name，返回 true；其他返回 false<br>
func Fits(pod *v1.Pod, nodeInfo *framework.NodeInfo) bool &#123;<br>
return len(pod.Spec.NodeName) == 0 || pod.Spec.NodeName == nodeInfo.Node().Name<br>
&#125; <br>
</pre><br>
<strong><em>对筛选出的 node 排序</em></strong><br>
<br>选择了合适的 Nodes 之后，接下来会执行一系列 priority function  <strong>对这些 Nodes 进行排序</strong>。 例如，如果算法是希望将 Pods 尽量分散到整个集群，那 priority 会选择资源尽量空闲的节点。<br>
<br>这些函数会给每个 Node 打分，<strong>得分最高的 Node 会被选中</strong>，调度到该节点。<br>
<pre class="prettyprint">// pkg/scheduler/core/generic_scheduler.go<br>
<br>
// 运行打分插件（score plugins）对 nodes 进行排序。<br>
func (g *genericScheduler) prioritizeNodes(ctx context.Context, fwk framework.Framework,<br>
state *framework.CycleState, pod *v1.Pod, nodes []*v1.Node,) (framework.NodeScoreList, error) &#123;<br>
<br>
// 如果没有指定 priority 配置，所有 node 将都得 1 分。<br>
if len(g.extenders) == 0 && !fwk.HasScorePlugins() &#123;<br>
    result := make(framework.NodeScoreList, 0, len(nodes))<br>
    for i := range nodes &#123;<br>
        result = append(result, framework.NodeScore&#123; Name:  nodes[i].Name, Score: 1 &#125;)<br>
    &#125;<br>
    return result, nil<br>
&#125;<br>
<br>
preScoreStatus := fwk.RunPreScorePlugins(ctx, state, pod, nodes)       // PreScoe 插件<br>
scoresMap, scoreStatus := fwk.RunScorePlugins(ctx, state, pod, nodes)  // Score 插件<br>
<br>
result := make(framework.NodeScoreList, 0, len(nodes))<br>
for i := range nodes &#123;<br>
    result = append(result, framework.NodeScore&#123;Name: nodes[i].Name, Score: 0&#125;)<br>
    for j := range scoresMap &#123;<br>
        result[i].Score += scoresMap[j][i].Score<br>
    &#125;<br>
&#125;<br>
<br>
if len(g.extenders) != 0 && nodes != nil &#123;<br>
    combinedScores := make(map[string]int64, len(nodes))<br>
    for i := range g.extenders &#123;<br>
        if !g.extenders[i].IsInterested(pod) &#123;<br>
            continue<br>
        &#125;<br>
        go func(extIndex int) &#123;<br>
            prioritizedList, weight := g.extenders[extIndex].Prioritize(pod, nodes)<br>
            for i := range *prioritizedList &#123;<br>
                host, score := (*prioritizedList)[i].Host, (*prioritizedList)[i].Score<br>
                combinedScores[host] += score * weight<br>
            &#125;<br>
        &#125;(i)<br>
    &#125;<br>
<br>
    for i := range result &#123;<br>
        result[i].Score += combinedScores[result[i].Name] * (MaxNodeScore / MaxExtenderPriority)<br>
    &#125;<br>
&#125;<br>
<br>
return result, nil<br>
&#125; <br>
</pre><br>
<strong>创建 <code class="prettyprint">v1.Binding</code> 对象</strong><br>
<br>算法选出一个 Node 之后，调度器会 <a href="https://github.com/kubernetes/kubernetes/blob/v1.21.0/plugin/pkg/scheduler/scheduler.go#L336-L342">创建一个 Binding 对象</a>， Pod 的 <strong>ObjectReference 字段的值就是选中的 Node 的名字</strong>。<br>
<pre class="prettyprint">// pkg/scheduler/framework/runtime/framework.go<br>
<br>
func (f *frameworkImpl) runBindPlugin(ctx context.Context, bp BindPlugin, state *CycleState,<br>
pod *v1.Pod, nodeName string) *framework.Status &#123;<br>
<br>
if !state.ShouldRecordPluginMetrics() &#123;<br>
    return bp.Bind(ctx, state, pod, nodeName)<br>
&#125;<br>
<br>
status := bp.Bind(ctx, state, pod, nodeName)<br>
return status<br>
&#125; <br>
</pre><br>
<pre class="prettyprint">// pkg/scheduler/framework/plugins/defaultbinder/default_binder.go<br>
<br>
// Bind binds pods to nodes using the k8s client.<br>
func (b DefaultBinder) Bind(ctx, state *CycleState, p *v1.Pod, nodeName string) *framework.Status &#123;<br>
binding := &v1.Binding&#123;<br>
    ObjectMeta: metav1.ObjectMeta&#123;Namespace: p.Namespace, Name: p.Name, UID: p.UID&#125;,<br>
    Target:     v1.ObjectReference&#123;Kind: "Node", Name: nodeName&#125;, // ObjectReference 字段为 nodeName<br>
&#125;<br>
<br>
b.handle.ClientSet().CoreV1().Pods(binding.Namespace).Bind(ctx, binding, metav1.CreateOptions&#123;&#125;)<br>
&#125; <br>
</pre><br>
如上，最后 <code class="prettyprint">ClientSet().CoreV1().Pods(binding.Namespace).Bind()</code> 通过一个 <strong>POST 请求发给 apiserver</strong>。<br>
<br><strong>kube-apiserver 更新 Pod 对象</strong><br>
<br>kube-apiserver 收到这个 Binding object 请求后，registry 反序列化对象，更新 Pod 对象的下列字段：<br>
<ul><li>设置 NodeName</li><li>添加 annotations</li><li>设置 <code class="prettyprint">PodScheduled</code> status 为 <code class="prettyprint">True</code></li></ul><br>
<br><pre class="prettyprint">// pkg/registry/core/pod/storage/storage.go<br>
<br>
func (r *BindingREST) setPodHostAndAnnotations(ctx context.Context, podID, oldMachine, machine string,<br>
annotations map[string]string, dryRun bool) (finalPod *api.Pod, err error) &#123;<br>
<br>
podKey := r.store.KeyFunc(ctx, podID)<br>
r.store.Storage.GuaranteedUpdate(ctx, podKey, &api.Pod&#123;&#125;, false, nil,<br>
    storage.SimpleUpdate(func(obj runtime.Object) (runtime.Object, error) &#123;<br>
<br>
    pod, ok := obj.(*api.Pod)<br>
    pod.Spec.NodeName = machine<br>
    if pod.Annotations == nil &#123;<br>
        pod.Annotations = make(map[string]string)<br>
    &#125;<br>
    for k, v := range annotations &#123;<br>
        pod.Annotations[k] = v<br>
    &#125;<br>
    podutil.UpdatePodCondition(&pod.Status, &api.PodCondition&#123;<br>
        Type:   api.PodScheduled,<br>
        Status: api.ConditionTrue,<br>
    &#125;)<br>
<br>
    return pod, nil<br>
&#125;), dryRun, nil)<br>
&#125; <br>
</pre><br>
<strong>自定义调度器</strong><br>
<br>predicate 和 priority function 都是可扩展的，可以通过  <code class="prettyprint">--policy-config-file</code>  指定。<br>
<br>Kubernetes 还可以自定义调度器（自己实现调度逻辑）。<strong>如果 PodSpec 中 schedulerName 字段不为空</strong>，Kubernetes 就会将这个 Pod 的调度权交给指定的调度器。<br>
<h4>小结</h4>总结一下前面已经完成的步骤：<br>
<ol><li>HTTP 请求通过了认证、鉴权、admission control</li><li>Deployment, ReplicaSet 和 Pod resources 已经持久化到 etcd</li><li>一系列 initializers 已经执行完毕</li><li>每个 Pod 也已经调度到了合适的 Node 上</li></ol><br>
<br>但是，<strong>到目前为止，我们看到的所有东西（状态），还只是存在于 etcd 中的元数据</strong>。 下一步就是将这些状态同步到计算节点上，然后计算节点上的 agent（kubelet）就开始干活了。<br>
<br>原文链接：<br>
<ul><li><a href="http://arthurchiao.art/blog/what-happens-when-k8s-creates-pods-1-zh/" rel="nofollow" target="_blank">http://arthurchiao.art/blog/wh ... 1-zh/</a></li><li><a href="http://arthurchiao.art/blog/what-happens-when-k8s-creates-pods-2-zh/" rel="nofollow" target="_blank">http://arthurchiao.art/blog/wh ... 2-zh/</a></li><li><a href="http://arthurchiao.art/blog/what-happens-when-k8s-creates-pods-3-zh/" rel="nofollow" target="_blank">http://arthurchiao.art/blog/wh ... 3-zh/</a></li><li><a href="http://arthurchiao.art/blog/what-happens-when-k8s-creates-pods-4-zh/" rel="nofollow" target="_blank">http://arthurchiao.art/blog/wh ... 4-zh/</a></li></ul>
                                
                                                              
</div>
            